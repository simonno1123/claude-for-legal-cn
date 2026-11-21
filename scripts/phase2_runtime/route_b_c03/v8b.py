"""C03 V8-B owner-run integrity layer (design TASK_PHASE2_ROUTE_B_C03_V8B_INTEGRITY_DESIGN R3, B2 not enabled).

This program is meant to run ONLY from the owner's trust folder (a folder never connected to any
Claude session), started by the owner in their own terminal. The recorder must not run it.

Usage (owner terminal):
  python -I -S -B v8b.py sign     <folder> --stage S1|S2|S3 --trust DIR --key KEY [--h H_INDEX]
  python -I -S -B v8b.py verify   <folder> --trust DIR [--h H_INDEX]
  python -I -S -B v8b.py use      <folder> --candidate FILE --dest DIR --trust DIR --key KEY [--h H_INDEX]
  python -I -S -B v8b.py withdraw --case CODE [--m SHA] --reason TEXT --trust DIR
  python -I -S -B v8b.py recover  --trust DIR [--resolve SEQ --as committed|aborted --note TEXT]

Trust folder contents (all append-only JSONL, each line chained to the SHA-256 of the previous line):
  allowed_signers        owner's public key, principal REVIEWER-01, namespace c03-gate
  sign_log.jsonl         one line per signature: stage, case, M, manifest and signature SHA, local time
  stop_checkpoints.jsonl H index length and last-line SHA at each signature
  withdrawals.jsonl      owner-registered withdrawals (authoritative)
  registry.jsonl         global use registry: intent / committed / aborted
  registry.lock          global lock (exclusive create)

Signatures use `ssh-keygen -Y sign/verify` with namespace c03-gate. Only the trust folder's
allowed_signers is ever read. V8-A's pure validator is called unchanged; the review_commit check
(S1 under L2) only drops the single RECONFIRMATION_MISSING reason.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
import pathlib
import secrets
import subprocess
import sys
import tempfile

if __package__ in (None, ""):
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from phase2_runtime.route_b_c03 import gate_records as g  # type: ignore
    from phase2_runtime.route_b_c03 import gate_cli  # type: ignore
else:
    from . import gate_records as g
    from . import gate_cli

VERSION = "v8b-1"
NAMESPACE = "c03-gate"
PRINCIPAL = "REVIEWER-01"
COOLING = timedelta(hours=24)
STAGE_ORDER = ("S1", "S2", "S3", "S4")


class TrustError(Exception):
    """A trust-folder log is missing, unreadable, or its chain is broken."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


# ---------------------------------------------------------------- trust-folder logs

class ChainLog:
    """Append-only JSONL whose every line carries `prev`: the SHA-256 of the previous line's bytes."""

    def __init__(self, path: pathlib.Path):
        self.path = path

    def read(self) -> list[dict]:
        if not self.path.exists():
            return []
        lines = self.path.read_bytes().split(b"\n")
        if lines and lines[-1] == b"":
            lines.pop()
        out, prev = [], None
        for i, raw in enumerate(lines, 1):
            try:
                rec = g.parse_record(raw.decode("utf-8"))
            except (g.RecordError, UnicodeDecodeError, ValueError) as exc:
                raise TrustError(f"{self.path.name} line {i} unreadable: {exc}") from exc
            if rec.get("seq") != i or rec.get("prev") != prev:
                raise TrustError(f"{self.path.name} chain broken at line {i}")
            out.append(rec)
            prev = _sha(raw)
        return out

    def append(self, entry: dict) -> dict:
        existing = self.read()
        prev = _sha(self.path.read_bytes().split(b"\n")[len(existing) - 1]) if existing else None
        rec = {"seq": len(existing) + 1, "prev": prev, **entry}
        data = g.canonical_bytes(rec) + b"\n"
        with self.path.open("ab") as fh:
            fh.write(data)
            fh.flush()
            os.fsync(fh.fileno())
        if self.read()[-1] != rec:
            raise TrustError(f"{self.path.name} does not end with the appended entry")
        return rec


class Trust:
    def __init__(self, root: pathlib.Path):
        self.root = root
        self.allowed_signers = root / "allowed_signers"
        self.sign_log = ChainLog(root / "sign_log.jsonl")
        self.checkpoints = ChainLog(root / "stop_checkpoints.jsonl")
        self.withdrawals = ChainLog(root / "withdrawals.jsonl")
        self.registry = ChainLog(root / "registry.jsonl")
        self.lock_path = root / "registry.lock"

    def check(self) -> None:
        if not self.allowed_signers.is_file():
            raise TrustError("allowed_signers missing in trust folder")


# ---------------------------------------------------------------- signatures

class SshSigner:
    """ssh-keygen based signer/verifier. The passphrase prompt (if any) goes to the owner's terminal."""

    def __init__(self, key: pathlib.Path | None = None):
        self.key = key

    def sign(self, manifest: pathlib.Path) -> bytes:
        if self.key is None:
            raise TrustError("signing key not given")
        sig = manifest.with_name(manifest.name + ".sig")
        if sig.exists():
            raise TrustError("signature file already exists")
        subprocess.run(["ssh-keygen", "-Y", "sign", "-n", NAMESPACE, "-f", str(self.key), str(manifest)], check=True)
        return sig.read_bytes()

    def verify(self, data: bytes, sig: bytes, allowed_signers: pathlib.Path) -> bool:
        with tempfile.TemporaryDirectory() as d:
            sp = pathlib.Path(d) / "m.sig"
            sp.write_bytes(sig)
            r = subprocess.run(["ssh-keygen", "-Y", "verify", "-f", str(allowed_signers), "-I", PRINCIPAL,
                                "-n", NAMESPACE, "-s", str(sp)], input=data, capture_output=True)
            return r.returncode == 0


# ---------------------------------------------------------------- helpers over a record folder

def _file_sha(path: pathlib.Path) -> str:
    return _sha(path.read_bytes())


def _record_files(folder: pathlib.Path, stage: str, bundle: dict) -> dict[str, str]:
    """Closed set of record files each stage covers (design §3), name -> SHA-256 of file bytes."""
    if stage == "S1":
        names = ["M", "I", "T", "R"] + [n for n in ("E", "S") if bundle.get(n)]
        files = [folder / f"{n}.json" for n in names]
        for prefix in ("V", "W", "X"):
            files += sorted(folder.glob(f"{prefix}_*.json"))
    elif stage == "S2":
        files = [folder / "P.json"]
    elif stage == "S3":
        files = [folder / f"{n}.json" for n in ("Q1", "Q2", "AUTH")]
    elif stage == "S4":
        files = [folder / "Q3.json"]
    else:
        raise ValueError(stage)
    missing = [f.name for f in files if not f.is_file()]
    if missing:
        raise TrustError(f"records missing for {stage}: {', '.join(missing)}")
    return {f.name: _file_sha(f) for f in files}


def _h_refs(R: dict) -> list[str]:
    answers = R.get("h_query", {}).get("answers", {})
    refs = set(answers)
    refs |= {a["clearance"] for a in answers.values() if a.get("clearance")}
    return sorted(refs)


def _is_l2(bundle: dict) -> bool:
    return bool(bundle.get("X") or bundle.get("P") or bundle.get("E"))


def _h_path(folder: pathlib.Path, h: str | None) -> pathlib.Path:
    return pathlib.Path(h) if h else folder / "H_index.jsonl"


def _h_lines(path: pathlib.Path) -> list[bytes]:
    if not path.exists():
        return []
    lines = [ln for ln in path.read_bytes().split(b"\n") if ln.strip()]
    return lines


def _manifest_path(folder: pathlib.Path, stage: str) -> pathlib.Path:
    return folder / f"V8B_{stage}.json"


def _load_signed(folder: pathlib.Path, stage: str) -> tuple[dict, bytes, bytes] | None:
    mp = _manifest_path(folder, stage)
    sp = mp.with_name(mp.name + ".sig")
    if not mp.exists() and not sp.exists():
        return None
    if not (mp.exists() and sp.exists()):
        return ({}, b"", b"")
    data = mp.read_bytes()
    return (json.loads(data.decode("utf-8")), data, sp.read_bytes())


def _expected_stages(bundle: dict) -> list[str]:
    return ["S1", "S2", "S3"] if _is_l2(bundle) else ["S1", "S3"]


# ---------------------------------------------------------------- chain verification

def verify_chain(folder: pathlib.Path, trust: Trust, signer: SshSigner, *, upto: str, h: str | None = None) -> dict:
    """Verify every expected signature up to and including `upto`. Returns {ok, reasons, stages, nonce}."""
    reasons: list[str] = []
    try:
        trust.check()
        bundle = gate_cli.load_bundle(folder)
        log = trust.sign_log.read()
    except (TrustError, g.RecordError, OSError) as exc:
        return {"ok": False, "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    m_sha = g.record_sha256(bundle["M"]) if bundle.get("M") else None
    wanted = [s for s in _expected_stages(bundle) + ["S4"] if STAGE_ORDER.index(s) <= STAGE_ORDER.index(upto)]
    prev_sig, stages, nonce = None, {}, None
    for stage in wanted:
        got = _load_signed(folder, stage)
        if got is None:
            reasons.append(f"SIGNATURE_MISSING:{stage}")
            break
        manifest, data, sig = got
        if not data or not sig or not signer.verify(data, sig, trust.allowed_signers):
            reasons.append(f"SIGNATURE_INVALID:{stage}")
            break
        if manifest.get("stage") != stage or manifest.get("version") != VERSION or manifest.get("M") != m_sha:
            reasons.append(f"SIGNED_MANIFEST_MISMATCH:{stage}")
            break
        if manifest.get("prev_sig") != prev_sig:
            reasons.append(f"SIGNATURE_CHAIN_BROKEN:{stage}")
            break
        try:
            current = _record_files(folder, stage, bundle)
        except TrustError:
            current = None
        if current != manifest.get("records"):
            reasons.append(f"SIGNED_MANIFEST_MISMATCH:{stage}")
            break
        entry = next((e for e in log if e.get("manifest_sha") == _sha(data) and e.get("sig_sha") == _sha(sig)), None)
        if entry is None or entry.get("stage") != stage:
            reasons.append(f"SIGN_LOG_MISSING:{stage}")
            break
        if stage == "S3":
            nonce = manifest.get("nonce")
        if stage == "S4":
            g_lines = (folder / "G.jsonl").read_bytes() if (folder / "G.jsonl").exists() else b""
            if not g_lines.startswith(_prefix_bytes(manifest)) or _sha(_prefix_bytes(manifest)) != manifest.get("g_prefix_sha"):
                reasons.append("SIGNED_MANIFEST_MISMATCH:S4")
                break
        stages[stage] = {"at": entry["at"], "sig_sha": _sha(sig)}
        prev_sig = _sha(sig)
    return {"ok": not reasons, "reasons": reasons, "stages": stages, "nonce": nonce, "last_sig": prev_sig}


def _prefix_bytes(manifest: dict) -> bytes:
    return bytes.fromhex(manifest.get("g_prefix_hex", ""))


# ---------------------------------------------------------------- sign S1 / S2 / S3

def _validate(bundle: dict, now: str, stage: str) -> dict:
    return g.validate(bundle, now=now, stage=stage)


def sign_stage(folder: pathlib.Path, stage: str, trust: Trust, signer: SshSigner, *, h: str | None = None,
               now: str | None = None) -> dict:
    now = now or _now()
    try:
        trust.check()
        bundle = gate_cli.load_bundle(folder)
    except (TrustError, g.RecordError, OSError) as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    if _manifest_path(folder, stage).exists():
        return {"result": "REFUSED", "reasons": ["SIGNATURE_EXISTS"]}
    l2 = _is_l2(bundle)
    extra: dict = {}
    if stage == "S1":
        out = _validate(bundle, now, "review")
        left = [r for r in out["reasons"] if not (l2 and r == "RECONFIRMATION_MISSING")]
        if left:
            return {"result": "REFUSED", "reasons": left, "check": "review_commit" if l2 else "review"}
        prev = None
        extra["h_refs"] = _h_refs(bundle["R"])
        check = "review_commit" if l2 else "review"
    elif stage == "S2":
        if not l2:
            return {"result": "REFUSED", "reasons": ["STAGE_NOT_APPLICABLE"]}
        chain = verify_chain(folder, trust, signer, upto="S1", h=h)
        if not chain["ok"]:
            return {"result": "REFUSED", "reasons": chain["reasons"]}
        s1_at = g.parse_time(chain["stages"]["S1"]["at"])
        if g.parse_time(now) < s1_at + COOLING:
            return {"result": "REFUSED", "reasons": ["COOLING_PERIOD_UNMET"], "earliest": (s1_at + COOLING).isoformat()}
        out = _validate(bundle, now, "review")
        if out["reasons"]:
            return {"result": "REFUSED", "reasons": out["reasons"], "check": "review"}
        prev = chain["last_sig"]
        extra["cooling_basis"] = {"s1_signed_at": chain["stages"]["S1"]["at"], "checked_at": now}
        check = "review"
    elif stage == "S3":
        chain = verify_chain(folder, trust, signer, upto="S2" if l2 else "S1", h=h)
        if not chain["ok"]:
            return {"result": "REFUSED", "reasons": chain["reasons"]}
        out = _validate(bundle, now, "authorization")
        if out["reasons"]:
            return {"result": "REFUSED", "reasons": out["reasons"], "check": "authorization"}
        prev = chain["last_sig"]
        extra["nonce"] = secrets.token_hex(16)
        extra["auth_sha"] = g.record_sha256(bundle["AUTH"])
        check = "authorization"
    else:
        return {"result": "REFUSED", "reasons": ["USE_STAGE_IS_SIGNED_BY_USE_COMMAND"]}
    try:
        records = _record_files(folder, stage, bundle)
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["RECORDS_MISSING"], "detail": str(exc)}
    manifest = {"version": VERSION, "stage": stage, "case": bundle["M"]["case"]["code"], "M": g.record_sha256(bundle["M"]),
                "records": records, "prev_sig": prev, "validator": {"stage": check, "result": out["result"]},
                "signed_at_local": now, **extra}
    return _sign_and_log(folder, stage, manifest, trust, signer, h=h, now=now)


def _sign_and_log(folder: pathlib.Path, stage: str, manifest: dict, trust: Trust, signer: SshSigner, *,
                  h: str | None, now: str) -> dict:
    mp = _manifest_path(folder, stage)
    data = g.canonical_bytes(manifest)
    with mp.open("xb") as fh:
        fh.write(data)
    try:
        sig = signer.sign(mp)
    except (subprocess.CalledProcessError, TrustError, OSError) as exc:
        _quarantine(mp)
        return {"result": "REFUSED", "reasons": ["SIGNING_FAILED"], "detail": str(exc)}
    if not signer.verify(data, sig, trust.allowed_signers):
        _quarantine(mp)
        _quarantine(mp.with_name(mp.name + ".sig"))
        return {"result": "REFUSED", "reasons": ["SIGNATURE_INVALID"], "detail": "key not in trust allowed_signers"}
    entry = trust.sign_log.append({"stage": stage, "case": manifest["case"], "M": manifest["M"],
                                   "manifest_sha": _sha(data), "sig_sha": _sha(sig), "at": now})
    hp = _h_path(folder, h)
    lines = _h_lines(hp)
    trust.checkpoints.append({"case": manifest["case"], "h_file": hp.name, "lines": len(lines),
                              "last_sha": _sha(lines[-1]) if lines else None, "at": now})
    return {"result": "SIGNED", "stage": stage, "manifest": mp.name, "sign_log_seq": entry["seq"], "at": now}


def _quarantine(path: pathlib.Path) -> None:
    """Move a file aside (never delete) so a failed signing leaves no half-signed stage."""
    if path.exists():
        dest = path.with_name(f"_void_{datetime.now().strftime('%Y%m%dT%H%M%S')}_{path.name}")
        os.replace(path, dest)


# ---------------------------------------------------------------- use (S4 + global registry)

def _acquire(lock: pathlib.Path) -> bool:
    try:
        fd = os.open(str(lock), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError:
        return False
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(f"pid={os.getpid()} at={_now()}\n")
    return True


def _release(lock: pathlib.Path) -> None:
    try:
        lock.unlink()
    except FileNotFoundError:
        pass


def _orphans(registry: list[dict]) -> list[dict]:
    closed = {e["intent"] for e in registry if e["type"] in ("committed", "aborted")}
    return [e for e in registry if e["type"] == "intent" and e["seq"] not in closed]


def _checkpoint_ok(trust: Trust, case: str, hp: pathlib.Path) -> bool:
    cps = [c for c in trust.checkpoints.read() if c["case"] == case and c["h_file"] == hp.name]
    if not cps:
        return False
    cp = cps[-1]
    lines = _h_lines(hp)
    if len(lines) < cp["lines"]:
        return False
    return cp["lines"] == 0 or _sha(lines[cp["lines"] - 1]) == cp["last_sha"]


def use(folder: pathlib.Path, candidate: pathlib.Path, dest: pathlib.Path, trust: Trust, signer: SshSigner, *,
        h: str | None = None, now: str | None = None) -> dict:
    now = now or _now()
    try:
        trust.check()
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    if not _acquire(trust.lock_path):
        return {"result": "REFUSED", "reasons": ["BUSY_GLOBAL"]}
    try:
        return _use_locked(folder, candidate, dest, trust, signer, h=h, now=now)
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_LOG_CORRUPT"], "detail": str(exc)}
    finally:
        _release(trust.lock_path)


def _use_locked(folder, candidate, dest, trust: Trust, signer: SshSigner, *, h, now) -> dict:
    registry = trust.registry.read()
    if _orphans(registry):
        return {"result": "REFUSED", "reasons": ["REGISTRY_RECOVERY_REQUIRED"]}
    try:
        bundle = gate_cli.load_bundle(folder)
    except (g.RecordError, OSError) as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    chain = verify_chain(folder, trust, signer, upto="S3", h=h)
    if not chain["ok"]:
        return {"result": "REFUSED", "reasons": chain["reasons"]}
    if _manifest_path(folder, "S4").exists():
        return {"result": "REFUSED", "reasons": ["SIGNATURE_EXISTS"]}
    reasons: list[str] = []
    auth_sha = g.record_sha256(bundle["AUTH"])
    auth_key = f"{auth_sha}:{chain['nonce']}"
    used = sum(1 for e in registry if e["type"] == "committed" and e["auth_key"] == auth_key)
    used_elsewhere = sum(1 for e in registry if e["type"] == "committed" and e["auth_key"].split(":")[0] == auth_sha)
    if used >= bundle["AUTH"]["max_uses"] or used_elsewhere >= bundle["AUTH"]["max_uses"]:
        reasons.append("AUTHORIZATION_REPLAYED")
    pre = g.validate(bundle, now=now, stage="use")
    if pre["result"] != "PRE_USE_RECORDS_COMPLETE":
        reasons += [r for r in pre["reasons"] if r not in reasons] or ["PRE_USE_CHECK_FAILED"]
    case, m_sha = bundle["M"]["case"]["code"], g.record_sha256(bundle["M"])
    if any(w["case"] == case and w["M"] in ("*", m_sha) for w in trust.withdrawals.read()):
        reasons.append("WITHDRAWN_OR_SUPERSEDED")
    hp = _h_path(folder, h)
    if not _checkpoint_ok(trust, case, hp):
        reasons.append("STOP_INDEX_ROLLED_BACK")
    q3_at = g.parse_time(bundle["Q3"]["formed_at"]) if bundle.get("Q3") else None
    for raw in _h_lines(hp):
        ev = g.parse_record(raw.decode("utf-8"))
        if ev.get("event") == "discovery" and ev.get("case") == case and q3_at and g.parse_time(ev["at"]) > q3_at:
            reasons.append("NEW_STOP_AFTER_Q3")
            break
    if reasons:
        return {"result": "REFUSED", "reasons": reasons}
    g_bytes = (folder / "G.jsonl").read_bytes()
    challenge = secrets.token_hex(16)
    manifest = {"version": VERSION, "stage": "S4", "case": case, "M": m_sha,
                "records": _record_files(folder, "S4", bundle), "prev_sig": chain["last_sig"],
                "validator": {"stage": "use", "result": pre["result"]}, "signed_at_local": now,
                "challenge": challenge, "auth_key": auth_key, "registry_seq": len(registry) + 1,
                "g_prefix_sha": _sha(g_bytes), "g_prefix_hex": g_bytes.hex()}
    signed = _sign_and_log(folder, "S4", manifest, trust, signer, h=h, now=now)
    if signed["result"] != "SIGNED":
        return signed
    intent = trust.registry.append({"type": "intent", "auth_key": auth_key, "case": case, "folder": folder.name,
                                    "challenge": challenge, "at": now})
    out = gate_cli.record_use(folder, candidate, dest, now=now)
    if out["result"] in ("USED", "USED_NOT_PUBLISHED"):
        trust.registry.append({"type": "committed", "intent": intent["seq"], "auth_key": auth_key, "case": case,
                               "folder": folder.name, "result": out["result"], "at": _now()})
    elif out["result"] == "REFUSED":
        trust.registry.append({"type": "aborted", "intent": intent["seq"], "auth_key": auth_key, "case": case,
                               "folder": folder.name, "result": out.get("reason", "REFUSED"), "at": _now()})
    # USAGE_LOG_INCONSISTENT leaves the intent open: recover must be run before any further use.
    return {"result": out["result"], "record_use": out, "registry_intent": intent["seq"], "challenge": challenge}


# ---------------------------------------------------------------- withdraw / recover

def withdraw(trust: Trust, case: str, m: str | None, reason: str, *, now: str | None = None) -> dict:
    rec = trust.withdrawals.append({"case": case, "M": m or "*", "reason": reason, "at": now or _now()})
    return {"result": "WITHDRAWN", "seq": rec["seq"]}


def recover(trust: Trust, resolve: int | None = None, as_: str | None = None, note: str = "", *,
            now: str | None = None) -> dict:
    registry = trust.registry.read()
    orphans = _orphans(registry)
    if resolve is None:
        return {"result": "ORPHANS", "orphans": orphans}
    target = next((o for o in orphans if o["seq"] == resolve), None)
    if target is None or as_ not in ("committed", "aborted"):
        return {"result": "REFUSED", "reasons": ["NO_SUCH_ORPHAN_OR_BAD_RESOLUTION"]}
    rec = trust.registry.append({"type": as_, "intent": resolve, "auth_key": target["auth_key"], "case": target["case"],
                                 "folder": target["folder"], "result": f"RECOVERED: {note}", "at": now or _now()})
    return {"result": "RESOLVED", "seq": rec["seq"]}


# ---------------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="C03 V8-B owner-run integrity layer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sign"); s.add_argument("folder"); s.add_argument("--stage", required=True, choices=("S1", "S2", "S3"))
    v = sub.add_parser("verify"); v.add_argument("folder")
    u = sub.add_parser("use"); u.add_argument("folder"); u.add_argument("--candidate", required=True); u.add_argument("--dest", required=True)
    w = sub.add_parser("withdraw"); w.add_argument("--case", required=True); w.add_argument("--m"); w.add_argument("--reason", required=True)
    r = sub.add_parser("recover"); r.add_argument("--resolve", type=int); r.add_argument("--as", dest="as_"); r.add_argument("--note", default="")
    for p in (s, v, u, w, r):
        p.add_argument("--trust", required=True)
    for p in (s, u):
        p.add_argument("--key", required=True)
    for p in (s, v, u):
        p.add_argument("--h")
    a = ap.parse_args(argv)
    trust = Trust(pathlib.Path(a.trust))
    signer = SshSigner(pathlib.Path(a.key) if getattr(a, "key", None) else None)
    if a.cmd == "sign":
        out = sign_stage(pathlib.Path(a.folder), a.stage, trust, signer, h=a.h)
        ok = out["result"] == "SIGNED"
    elif a.cmd == "verify":
        folder = pathlib.Path(a.folder)
        present = [st for st in STAGE_ORDER if _manifest_path(folder, st).exists()]
        out = verify_chain(folder, trust, signer, upto=present[-1] if present else "S1", h=a.h)
        ok = out["ok"]
    elif a.cmd == "use":
        out = use(pathlib.Path(a.folder), pathlib.Path(a.candidate), pathlib.Path(a.dest), trust, signer, h=a.h)
        ok = out["result"] == "USED"
    elif a.cmd == "withdraw":
        out = withdraw(trust, a.case, a.m, a.reason)
        ok = True
    else:
        out = recover(trust, a.resolve, a.as_, a.note)
        ok = out["result"] in ("ORPHANS", "RESOLVED")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
