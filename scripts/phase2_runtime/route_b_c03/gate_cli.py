"""C03 V8-A local wrapper: read a private record folder and run the pure validator.

Usage:
  python -I -S -B gate_cli.py validate <folder> [--stage review|application|authorization|use]
  python -I -S -B gate_cli.py enumerate-h <folder> --case CODE [--after TIME] [--upto TIME]
  python -I -S -B gate_cli.py record-use <folder> --candidate FILE --dest DIR

validate and enumerate-h are read-only. record-use is the only command that writes. Under
an exclusive lock on G.jsonl it runs the use-stage validation and, only if the result is
PRE_USE_RECORDS_COMPLETE, writes the exact validated candidate bytes (SHA-256 equal to M)
to a temporary file, appends the use event to G.jsonl, then renames the file into place.
A concurrent call is refused (BUSY). A failure before the G event leaves G unchanged and
publishes nothing.

Folder layout: M.json I.json T.json R.json and optionally E.json S.json P.json
Q1.json Q2.json Q3.json AUTH.json; X*.json V*.json W*.json CORR*.json; G.jsonl; H_index.jsonl.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
import pathlib
import sys

if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from phase2_runtime.route_b_c03 import gate_records as g  # type: ignore
    from phase2_runtime.route_b_c03 import gate_record_builder as b  # type: ignore
else:
    from . import gate_records as g
    from . import gate_record_builder as b


def _load(path: pathlib.Path) -> dict:
    return g.parse_record(path.read_text(encoding="utf-8"))


def _load_lines(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    return [g.parse_record(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def load_bundle(folder: pathlib.Path) -> dict:
    bundle: dict = {}
    for name in ("M", "I", "T", "R", "E", "S", "P", "Q1", "Q2", "Q3", "AUTH"):
        f = folder / f"{name}.json"
        if f.exists():
            bundle[name] = _load(f)
    for name in ("X", "V", "W", "CORR"):
        bundle[name] = [_load(f) for f in sorted(folder.glob(f"{name}_*.json"))]
    bundle["G"] = _load_lines(folder / "G.jsonl")
    bundle["H"] = _load_lines(folder / "H_index.jsonl")
    return bundle


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _lock(handle) -> bool:
    """Non-blocking exclusive lock on the open G.jsonl handle; False if another process holds it."""
    try:
        import fcntl
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            return True
        except OSError:
            return False
    except ImportError:  # Windows
        import msvcrt
        try:
            handle.seek(0)
            msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
            return True
        except OSError:
            return False


def _append_use(handle, event: dict) -> None:
    handle.seek(0, 2)
    handle.write(g.canonical_bytes(event) + b"\n")
    handle.flush()
    os.fsync(handle.fileno())


def record_use(folder: pathlib.Path, candidate: pathlib.Path, dest: pathlib.Path, *, now: str | None = None) -> dict:
    """Validate, then use: one locked critical section per record folder.

    Order: lock G.jsonl -> load and validate (use stage) -> read the candidate once and check
    its SHA-256 against M -> write those same bytes to a temporary file in DEST -> append and
    fsync the G use event -> atomically rename the temporary file to its final name.
    If anything fails before the G event is durable, G is rolled back to its original length and
no final file exists; if the rollback itself cannot be confirmed, the result is
USAGE_LOG_INCONSISTENT and the folder needs manual inspection before any further use.
    """
    now = now or _now()
    g_path = folder / "G.jsonl"
    if not g_path.exists():
        return {"result": "REFUSED", "reason": "USAGE_LOG_MISSING"}
    target = dest / candidate.name
    partial = dest / f".{candidate.name}.partial"
    with g_path.open("r+b") as handle:
        if not _lock(handle):
            return {"result": "REFUSED", "reason": "BUSY"}
        try:
            bundle = load_bundle(folder)
        except (g.RecordError, OSError) as exc:
            return {"result": "REFUSED", "reason": "RECORD_INVALID", "detail": str(exc)}
        pre = g.validate(bundle, now=now, stage="use")
        if pre["result"] != "PRE_USE_RECORDS_COMPLETE":
            return {"result": "REFUSED", "reason": "PRE_USE_CHECK_FAILED", "pre_use": pre}
        data = candidate.read_bytes()
        digest = hashlib.sha256(data).hexdigest().upper()
        if digest != bundle["M"]["candidate"]["output_sha256"]:
            return {"result": "REFUSED", "reason": "CANDIDATE_SHA_MISMATCH"}
        if target.exists() or partial.exists():
            return {"result": "REFUSED", "reason": "DESTINATION_EXISTS"}
        try:
            dest.mkdir(parents=True, exist_ok=True)
            with partial.open("xb") as out:
                out.write(data)
                out.flush()
                os.fsync(out.fileno())
        except OSError as exc:
            return {"result": "REFUSED", "reason": "COPY_FAILED", "detail": str(exc), "leftover": _cleanup(partial)}
        event = {"kind": "use", "auth": g.record_sha256(bundle["AUTH"]), "q3": g.record_sha256(bundle["Q3"]), "at": now}
        handle.seek(0, 2)
        original_size = handle.tell()
        try:
            _append_use(handle, event)
        except OSError as exc:
            restored = _restore_log(handle, original_size)
            out = {"result": "REFUSED" if restored else "USAGE_LOG_INCONSISTENT", "reason": "USAGE_LOG_WRITE_FAILED",
                   "detail": str(exc), "log_restored": restored, "leftover": _cleanup(partial)}
            return out
        try:
            os.replace(partial, target)
        except OSError as exc:
            return {"result": "USED_NOT_PUBLISHED", "reason": "RENAME_FAILED", "detail": str(exc),
                    "partial": str(partial), "sha256": digest, "at": now}
    return {"result": "USED", "pre_use": pre["result"], "copied_to": str(target), "sha256": digest, "at": now}


def _restore_log(handle, size: int) -> bool:
    """Roll G.jsonl back to its pre-append length; True only if the restore is confirmed on disk."""
    try:
        handle.truncate(size)
        handle.flush()
        os.fsync(handle.fileno())
        handle.seek(0, 2)
        return handle.tell() == size
    except OSError:
        return False


def _cleanup(path: pathlib.Path) -> str | None:
    """Remove an unpublished temporary file; report it if the filesystem refuses deletion."""
    try:
        path.unlink(missing_ok=True)
        return None
    except OSError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    v = sub.add_parser("validate")
    v.add_argument("folder")
    v.add_argument("--stage", default="review", choices=g.STAGES)
    e = sub.add_parser("enumerate-h")
    e.add_argument("folder")
    e.add_argument("--case", required=True)
    e.add_argument("--after")
    e.add_argument("--upto")
    u = sub.add_parser("record-use")
    u.add_argument("folder")
    u.add_argument("--candidate", required=True)
    u.add_argument("--dest", required=True)
    args = ap.parse_args(argv)
    folder = pathlib.Path(args.folder)
    if args.cmd == "record-use":
        out = record_use(folder, pathlib.Path(args.candidate), pathlib.Path(args.dest))
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return 0 if out["result"] == "USED" else 1
    if args.cmd == "validate":
        try:
            bundle = load_bundle(folder)
        except (g.RecordError, OSError) as exc:
            print(json.dumps({"result": "BLOCKED", "reasons": ["RECORD_INVALID"], "detail": str(exc)}, ensure_ascii=False))
            return 1
        now = _now()
        out = g.validate(bundle, now=now, stage=args.stage)
        out["checked_at"] = now
        out["note"] = "记录齐全且符合规则不等于授权；下游仍阻断，直至 AR-B-010 逐项决定。"
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return 0 if not out["reasons"] else 1
    events = _load_lines(folder / "H_index.jsonl")
    print(json.dumps(b.enumerate_stop_events(events, args.case, after=args.after, upto=args.upto), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
