"""C03 V8-A local wrapper: read a private record folder and run the pure validator.

Read-only. Usage:
  python -I -S -B gate_cli.py validate <folder> [--stage review|application|authorization|use]
  python -I -S -B gate_cli.py enumerate-h <folder> --case CODE [--after TIME] [--upto TIME]

Folder layout: M.json I.json T.json R.json and optionally E.json S.json P.json
Q1.json Q2.json Q3.json AUTH.json; X*.json V*.json W*.json CORR*.json; G.jsonl; H_index.jsonl.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
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
    args = ap.parse_args(argv)
    folder = pathlib.Path(args.folder)
    if args.cmd == "validate":
        try:
            bundle = load_bundle(folder)
        except (g.RecordError, OSError) as exc:
            print(json.dumps({"result": "BLOCKED", "reasons": ["RECORD_INVALID"], "detail": str(exc)}, ensure_ascii=False))
            return 1
        now = datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")
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
