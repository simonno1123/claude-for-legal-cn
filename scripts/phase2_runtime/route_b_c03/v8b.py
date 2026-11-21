"""C03 V8-B owner-run integrity layer (design TASK_PHASE2_ROUTE_B_C03_V8B_INTEGRITY_DESIGN R3, B2 not enabled).

This program is meant to run ONLY from the owner's trust folder (a folder never connected to any
Claude session), started by the owner in their own terminal. The recorder must not run it.

Usage (owner terminal):
  python -I -S -B v8b.py sign     <folder> --stage S1|S2|S3 --trust DIR --key KEY [--h H_INDEX]
  python -I -S -B v8b.py verify   <folder> --trust DIR [--h H_INDEX]
  python -I -S -B v8b.py use      <folder> --candidate FILE --dest DIR --trust DIR --key KEY [--h H_INDEX]
  python -I -S -B v8b.py withdraw --case CODE [--m SHA] --reason TEXT --trust DIR
  python -I -S -B v8b.py recover  --trust DIR [--resolve SEQ --as committed|aborted --note TEXT]

One stop index is authoritative per run: --h if given, otherwise <folder>/H_index.jsonl. It is the
index V8-A validates against, the index checkpointed in the trust folder, and the index scanned for
stops after Q3.

Trust folder contents (append-only JSONL, each line chained to the SHA-256 of the previous line):
  allowed_signers        owner's public key, principal REVIEWER-01, namespace c03-gate
  sign_log.jsonl         one line per signature, time taken after signing completes
  stop_checkpoints.jsonl stop-index length and prefix SHA at each signature
  withdrawals.jsonl      owner-registered withdrawals (authoritative)
  registry.jsonl         global use registry: intent / committed / aborted
  registry.lock          global lock (exclusive create); remove by hand only after a crash

The use command works on an in-memory snapshot taken under the global lock and the folder's G lock:
it validates and signs the snapshot, re-reads the clock and the folder after signing, and publishes
the snapshot's candidate bytes only if nothing changed and the cutoff has not passed.
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
from typing import Callable

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
SINGLE = ("M", "I", "T", "R", "E", "S", "P", "Q1", "Q2", "Q3", "AUTH")
MULTI = ("X", "V", "W", "CORR")
Clock = Callable[[], str]


class TrustError(Exception):
    """A trust-folder log is missing, unreadable, rolled back, or its chain is broken."""


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest().upper()


def _now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def _lines(data: bytes) -> list[bytes]:
    return [ln for ln in data.split(b"\n") if ln.strip()]


# ---------------------------------------------------------------- trust-folder logs

class ChainLog:
    """Append-only JSONL whose every line carries `seq` and `prev` (SHA-256 of the previous line)."""

    def __init__(self, path: pathlib.Path):
        self.path = path

    def _raw(self) -> list[bytes]:
        if not self.path.exists():
            return []
        lines = self.path.read_bytes().split(b"\n")
        if lines and lines[-1] == b"":
            lines.pop()
        return lines

    def read(self) -> list[dict]:
        out, prev = [], None
        for i, raw in enumerate(self._raw(), 1):
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
        raw = self._raw()
        existing = self.read()
        rec = {"seq": len(existing) + 1, "prev": _sha(raw[-1]) if raw else None, **entry}
        with self.path.open("ab") as fh:
            fh.write(g.canonical_bytes(rec) + b"\n")
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

    def read_registry(self) -> list[dict]:
        """Registry lines, refused if shorter than the high-water mark recorded by signed S4 entries."""
        reg = self.registry.read()
        marks = [e["registry_seq"] for e in self.sign_log.read() if e.get("stage") == "S4"]
        if marks and len(reg) < max(marks):
            raise TrustError("registry shorter than the sequence already signed in S4 (rolled back)")
        for e in self.sign_log.read():
            if e.get("stage") == "S4":
                intent = reg[e["registry_seq"] - 1] if len(reg) >= e["registry_seq"] else None
                if not intent or intent["type"] != "intent" or intent.get("challenge") != e.get("challenge"):
                    raise TrustError("registry intent does not match the signed S4 sequence")
        return reg


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


# ---------------------------------------------------------------- folder snapshot

class View:
    """Byte snapshot of a record folder plus the authoritative stop index."""

    def __init__(self, folder: pathlib.Path, h: str | None):
        self.folder = folder
        self.h_path = pathlib.Path(h) if h else folder / "H_index.jsonl"
        self.files: dict[str, bytes] = {}
        for p in sorted(folder.iterdir()):
            if p.is_file():
                self.files[p.name] = p.read_bytes()
        self.h_bytes = self.h_path.read_bytes() if self.h_path.exists() else b""

    def same_as_disk(self) -> bool:
        return View(self.folder, str(self.h_path)).fingerprint() == self.fingerprint()

    def fingerprint(self) -> str:
        parts = [f"{n}:{_sha(b)}" for n, b in sorted(self.files.items())] + [f"H:{_sha(self.h_bytes)}"]
        return _sha("\n".join(parts).encode())

    def get(self, name: str) -> bytes | None:
        return self.files.get(name)

    def bundle(self) -> dict:
        bd: dict = {}
        for n in SINGLE:
            data = self.get(f"{n}.json")
            if data is not None:
                bd[n] = g.parse_record(data.decode("utf-8"))
        for n in MULTI:
            bd[n] = [g.parse_record(self.files[k].decode("utf-8")) for k in sorted(self.files)
                     if k.startswith(f"{n}_") and k.endswith(".json")]
        bd["G"] = [g.parse_record(ln.decode("utf-8")) for ln in _lines(self.get("G.jsonl") or b"")]
        bd["H"] = [g.parse_record(ln.decode("utf-8")) for ln in _lines(self.h_bytes)]
        return bd


def _record_names(view: View, stage: str, bundle: dict) -> list[str]:
    if stage == "S1":
        names = [f"{n}.json" for n in ("M", "I", "T", "R") + tuple(n for n in ("E", "S") if bundle.get(n))]
        names += sorted(k for k in view.files if k.split("_")[0] in ("V", "W", "X") and k.endswith(".json") and "_" in k)
        return names
    return {"S2": ["P.json"], "S3": ["Q1.json", "Q2.json", "AUTH.json"], "S4": ["Q3.json"]}[stage]


def _records(view: View, stage: str, bundle: dict) -> dict[str, str]:
    names = _record_names(view, stage, bundle)
    missing = [n for n in names if view.get(n) is None]
    if missing:
        raise TrustError(f"records missing for {stage}: {', '.join(missing)}")
    return {n: _sha(view.files[n]) for n in names}


def _is_l2(bundle: dict) -> bool:
    return bool(bundle.get("X") or bundle.get("P") or bundle.get("E"))


def _expected(bundle: dict) -> list[str]:
    return ["S1", "S2", "S3"] if _is_l2(bundle) else ["S1", "S3"]


def _h_refs(R: dict) -> list[str]:
    answers = R.get("h_query", {}).get("answers", {})
    return sorted(set(answers) | {a["clearance"] for a in answers.values() if a.get("clearance")})


# ---------------------------------------------------------------- stop-index checkpoints

def _prefix_sha(lines: list[bytes], n: int) -> str:
    return _sha(b"\n".join(lines[:n]))


def _checkpoint_ok(trust: Trust, case: str, view: View) -> bool:
    """Current index must extend every recorded checkpoint for this case (checked against the latest,
    which itself was only recorded after extending the one before)."""
    cps = [c for c in trust.checkpoints.read() if c["case"] == case]
    if not cps:
        return True
    lines = _lines(view.h_bytes)
    cp = cps[-1]
    return len(lines) >= cp["lines"] and _prefix_sha(lines, cp["lines"]) == cp["prefix_sha"]


# ---------------------------------------------------------------- chain verification

def verify_chain(view: View, trust: Trust, signer: SshSigner, *, upto: str) -> dict:
    reasons: list[str] = []
    try:
        trust.check()
        bundle = view.bundle()
        log = trust.sign_log.read()
        registry = trust.read_registry() if upto == "S4" else None
    except (TrustError, g.RecordError, OSError, UnicodeDecodeError) as exc:
        return {"ok": False, "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    m_sha = g.record_sha256(bundle["M"]) if bundle.get("M") else None
    wanted = [s for s in _expected(bundle) + ["S4"] if STAGE_ORDER.index(s) <= STAGE_ORDER.index(upto)]
    prev_sig, stages, nonce = None, {}, None
    for stage in wanted:
        data, sig = view.get(f"V8B_{stage}.json"), view.get(f"V8B_{stage}.json.sig")
        if data is None or sig is None:
            reasons.append(f"SIGNATURE_MISSING:{stage}")
            break
        if not signer.verify(data, sig, trust.allowed_signers):
            reasons.append(f"SIGNATURE_INVALID:{stage}")
            break
        manifest = json.loads(data.decode("utf-8"))
        if manifest.get("stage") != stage or manifest.get("version") != VERSION or manifest.get("M") != m_sha:
            reasons.append(f"SIGNED_MANIFEST_MISMATCH:{stage}")
            break
        if manifest.get("prev_sig") != prev_sig:
            reasons.append(f"SIGNATURE_CHAIN_BROKEN:{stage}")
            break
        try:
            current = _records(view, stage, bundle)
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
        if stage == "S4" and not _s4_effect_ok(view, bundle, manifest, registry):
            reasons.append("USE_EVENT_MISMATCH:S4")
            break
        stages[stage] = {"at": entry["at"], "sig_sha": _sha(sig)}
        prev_sig = _sha(sig)
    return {"ok": not reasons, "reasons": reasons, "stages": stages, "nonce": nonce, "last_sig": prev_sig}


def _s4_effect_ok(view: View, bundle: dict, manifest: dict, registry: list[dict] | None) -> bool:
    """After S4: G = signed prefix + exactly this use event; registry has the signed intent, committed."""
    g_bytes = view.get("G.jsonl") or b""
    prefix = bytes.fromhex(manifest.get("g_prefix_hex", ""))
    if _sha(prefix) != manifest.get("g_prefix_sha") or not g_bytes.startswith(prefix):
        return False
    rest = _lines(g_bytes[len(prefix):])
    if len(rest) != 1:
        return False
    ev = g.parse_record(rest[0].decode("utf-8"))
    if ev.get("kind") != "use" or ev.get("auth") != g.record_sha256(bundle["AUTH"]) or ev.get("q3") != g.record_sha256(bundle["Q3"]):
        return False
    if registry is None or len(registry) < manifest["registry_seq"]:
        return False
    intent = registry[manifest["registry_seq"] - 1]
    if intent["type"] != "intent" or intent.get("challenge") != manifest.get("challenge"):
        return False
    return any(e["type"] == "committed" and e.get("intent") == intent["seq"] for e in registry)


# ---------------------------------------------------------------- signing

def _sign_and_log(view: View, stage: str, manifest: dict, trust: Trust, signer: SshSigner, clock: Clock) -> dict:
    """Write the manifest, sign it, then log with the clock read AFTER signing completes."""
    lines = _lines(view.h_bytes)
    if not _checkpoint_ok(trust, manifest["case"], view):
        return {"result": "REFUSED", "reasons": ["STOP_INDEX_ROLLED_BACK"]}
    mp = view.folder / f"V8B_{stage}.json"
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
    at = clock()
    extra = {k: manifest[k] for k in ("registry_seq", "challenge") if k in manifest}
    entry = trust.sign_log.append({"stage": stage, "case": manifest["case"], "M": manifest["M"],
                                   "manifest_sha": _sha(data), "sig_sha": _sha(sig), "at": at, **extra})
    trust.checkpoints.append({"case": manifest["case"], "h_file": view.h_path.name, "lines": len(lines),
                              "prefix_sha": _prefix_sha(lines, len(lines)), "at": at})
    return {"result": "SIGNED", "stage": stage, "manifest": mp.name, "sign_log_seq": entry["seq"], "at": at,
            "sig": sig, "data": data}


def _quarantine(path: pathlib.Path) -> None:
    """Move a file aside (never delete)."""
    if path.exists():
        os.replace(path, path.with_name(f"_void_{datetime.now().strftime('%Y%m%dT%H%M%S%f')}_{path.name}"))


def sign_stage(folder: pathlib.Path, stage: str, trust: Trust, signer: SshSigner, *, h: str | None = None,
               now: str | None = None, clock: Clock | None = None) -> dict:
    if clock is None:
        clock = (lambda: now) if now else _now
    now = now or clock()
    try:
        trust.check()
        view = View(folder, h)
        bundle = view.bundle()
    except (TrustError, g.RecordError, OSError, UnicodeDecodeError) as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    if view.get(f"V8B_{stage}.json") is not None:
        return {"result": "REFUSED", "reasons": ["SIGNATURE_EXISTS"]}
    l2 = _is_l2(bundle)
    extra: dict = {}
    if stage == "S1":
        out = g.validate(bundle, now=now, stage="review")
        left = [r for r in out["reasons"] if not (l2 and r == "RECONFIRMATION_MISSING")]
        check = "review_commit" if l2 else "review"
        if left:
            return {"result": "REFUSED", "reasons": left, "check": check}
        prev = None
        extra["h_refs"] = _h_refs(bundle["R"])
    elif stage == "S2":
        if not l2:
            return {"result": "REFUSED", "reasons": ["STAGE_NOT_APPLICABLE"]}
        chain = verify_chain(view, trust, signer, upto="S1")
        if not chain["ok"]:
            return {"result": "REFUSED", "reasons": chain["reasons"]}
        s1_at = g.parse_time(chain["stages"]["S1"]["at"])
        if g.parse_time(now) < s1_at + COOLING:
            return {"result": "REFUSED", "reasons": ["COOLING_PERIOD_UNMET"], "earliest": (s1_at + COOLING).isoformat()}
        out = g.validate(bundle, now=now, stage="review")
        check = "review"
        if out["reasons"]:
            return {"result": "REFUSED", "reasons": out["reasons"], "check": check}
        prev = chain["last_sig"]
        extra["cooling_basis"] = {"s1_signed_at": chain["stages"]["S1"]["at"], "checked_at": now}
    elif stage == "S3":
        chain = verify_chain(view, trust, signer, upto="S2" if l2 else "S1")
        if not chain["ok"]:
            return {"result": "REFUSED", "reasons": chain["reasons"]}
        out = g.validate(bundle, now=now, stage="authorization")
        check = "authorization"
        if out["reasons"]:
            return {"result": "REFUSED", "reasons": out["reasons"], "check": check}
        prev = chain["last_sig"]
        extra["nonce"] = secrets.token_hex(16)
        extra["auth_sha"] = g.record_sha256(bundle["AUTH"])
    else:
        return {"result": "REFUSED", "reasons": ["USE_STAGE_IS_SIGNED_BY_USE_COMMAND"]}
    try:
        records = _records(view, stage, bundle)
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["RECORDS_MISSING"], "detail": str(exc)}
    manifest = {"version": VERSION, "stage": stage, "case": bundle["M"]["case"]["code"], "M": g.record_sha256(bundle["M"]),
                "records": records, "prev_sig": prev, "validator": {"stage": check, "result": out["result"]},
                "checked_at": now, **extra}
    res = _sign_and_log(view, stage, manifest, trust, signer, clock)
    if res["result"] == "SIGNED" and stage == "S2":
        if g.parse_time(res["at"]) < s1_at + COOLING:  # defensive: clock moved backwards while signing
            return {"result": "REFUSED", "reasons": ["COOLING_PERIOD_UNMET"]}
    res.pop("sig", None)
    res.pop("data", None)
    return res


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


def _state_reasons(view: View, bundle: dict, trust: Trust, now: str) -> list[str]:
    """Current-state checks shared by the pre-sign and post-sign passes."""
    reasons: list[str] = []
    pre = g.validate(bundle, now=now, stage="use")
    if pre["result"] != "PRE_USE_RECORDS_COMPLETE":
        reasons += pre["reasons"] or ["PRE_USE_CHECK_FAILED"]
    case, m_sha = bundle["M"]["case"]["code"], g.record_sha256(bundle["M"])
    if any(w["case"] == case and w["M"] in ("*", m_sha) for w in trust.withdrawals.read()):
        reasons.append("WITHDRAWN_OR_SUPERSEDED")
    if not _checkpoint_ok(trust, case, view):
        reasons.append("STOP_INDEX_ROLLED_BACK")
    q3_at = g.parse_time(bundle["Q3"]["formed_at"]) if bundle.get("Q3") else None
    if q3_at and any(ev.get("event") == "discovery" and ev.get("case") == case and g.parse_time(ev["at"]) > q3_at
                     for ev in bundle["H"]):
        reasons.append("NEW_STOP_AFTER_Q3")
    return reasons


def use(folder: pathlib.Path, candidate: pathlib.Path, dest: pathlib.Path, trust: Trust, signer: SshSigner, *,
        h: str | None = None, now: str | None = None, clock: Clock | None = None) -> dict:
    clock = clock or ((lambda: now) if now else _now)
    try:
        trust.check()
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    if not _acquire(trust.lock_path):
        return {"result": "REFUSED", "reasons": ["BUSY_GLOBAL"]}
    try:
        g_path = folder / "G.jsonl"
        if not g_path.exists():
            return {"result": "REFUSED", "reasons": ["USAGE_LOG_MISSING"]}
        with g_path.open("r+b") as handle:
            if not gate_cli._lock(handle):
                return {"result": "REFUSED", "reasons": ["BUSY"]}
            return _use_locked(folder, candidate, dest, trust, signer, handle, h=h, clock=clock)
    except TrustError as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_LOG_CORRUPT"], "detail": str(exc)}
    finally:
        _release(trust.lock_path)


def _use_locked(folder, candidate, dest, trust: Trust, signer: SshSigner, handle, *, h, clock: Clock) -> dict:
    registry = trust.read_registry()
    if _orphans(registry):
        return {"result": "REFUSED", "reasons": ["REGISTRY_RECOVERY_REQUIRED"]}
    now = clock()
    try:
        view = View(folder, h)
        bundle = view.bundle()
        cand_bytes = candidate.read_bytes()
    except (g.RecordError, OSError, UnicodeDecodeError) as exc:
        return {"result": "REFUSED", "reasons": ["TRUST_OR_RECORD_UNREADABLE"], "detail": str(exc)}
    if view.get("V8B_S4.json") is not None:
        return {"result": "REFUSED", "reasons": ["SIGNATURE_EXISTS"]}
    chain = verify_chain(view, trust, signer, upto="S3")
    if not chain["ok"]:
        return {"result": "REFUSED", "reasons": chain["reasons"]}
    auth_sha = g.record_sha256(bundle["AUTH"])
    auth_key = f"{auth_sha}:{chain['nonce']}"
    reasons: list[str] = []
    committed = [e for e in registry if e["type"] == "committed" and e["auth_key"].split(":")[0] == auth_sha]
    if bundle["AUTH"]["max_uses"] is not None and len(committed) >= bundle["AUTH"]["max_uses"]:
        reasons.append("AUTHORIZATION_REPLAYED")
    if _sha(cand_bytes) != bundle["M"]["candidate"]["output_sha256"]:
        reasons.append("CANDIDATE_SHA_MISMATCH")
    reasons += [r for r in _state_reasons(view, bundle, trust, now) if r not in reasons]
    if reasons:
        return {"result": "REFUSED", "reasons": reasons}
    challenge = secrets.token_hex(16)
    g_bytes = view.get("G.jsonl") or b""
    case = bundle["M"]["case"]["code"]
    manifest = {"version": VERSION, "stage": "S4", "case": case, "M": g.record_sha256(bundle["M"]),
                "records": _records(view, "S4", bundle), "prev_sig": chain["last_sig"],
                "validator": {"stage": "use", "result": "PRE_USE_RECORDS_COMPLETE"}, "checked_at": now,
                "challenge": challenge, "auth_key": auth_key, "registry_seq": len(registry) + 1,
                "g_prefix_sha": _sha(g_bytes), "g_prefix_hex": g_bytes.hex(), "candidate_sha": _sha(cand_bytes),
                "snapshot": view.fingerprint()}
    # Intent first: a crash from here on leaves an open intent that recover must resolve.
    intent = trust.registry.append({"type": "intent", "auth_key": auth_key, "case": case, "folder": folder.name,
                                    "challenge": challenge, "at": now})

    def abort(reason: str, quarantine: bool = True, **more) -> dict:
        if quarantine:
            _quarantine(folder / "V8B_S4.json")
            _quarantine(folder / "V8B_S4.json.sig")
        trust.registry.append({"type": "aborted", "intent": intent["seq"], "auth_key": auth_key, "case": case,
                               "folder": folder.name, "result": reason, "at": clock()})
        return {"result": "REFUSED", "reasons": [reason], **more}

    signed = _sign_and_log(view, "S4", manifest, trust, signer, clock)
    if signed["result"] != "SIGNED":
        return abort(signed["reasons"][0], quarantine=False, detail=signed.get("detail"))

    # Post-signing pass: real time now, unchanged folder, unchanged current state.
    now2 = clock()
    after = View(folder, h)
    expected = dict(view.files)
    expected["V8B_S4.json"] = signed["data"]
    expected["V8B_S4.json.sig"] = signed["sig"]
    if after.files != expected or after.h_bytes != view.h_bytes or candidate.read_bytes() != cand_bytes:
        return abort("RECORDS_CHANGED_DURING_SIGNING")
    later = _state_reasons(view, bundle, trust, now2)
    if later:
        return abort(later[0], all_reasons=later)
    # Publish: write the snapshot's bytes straight to the final name (no swappable temp path), then
    # read the published file back and require the signed SHA before and after the G append. The
    # output's SHA goes into the committed registry entry, so later tampering is detectable by
    # `verify --output`.
    target = dest / candidate.name
    if target.exists():
        return abort("DESTINATION_EXISTS")
    want = _sha(cand_bytes)
    try:
        dest.mkdir(parents=True, exist_ok=True)
        with target.open("xb") as out:
            out.write(cand_bytes)
            out.flush()
            os.fsync(out.fileno())
    except OSError as exc:
        _quarantine(target)
        return abort("COPY_FAILED", detail=str(exc))
    if _file_sha(target) != want:
        _quarantine(target)
        return abort("OUTPUT_TAMPERED")
    event = {"kind": "use", "auth": auth_sha, "q3": g.record_sha256(bundle["Q3"]), "at": now2}
    handle.seek(0, 2)
    size = handle.tell()
    try:
        gate_cli._append_use(handle, event)
    except OSError as exc:
        if gate_cli._restore_log(handle, size):
            _quarantine(target)
            return abort("USAGE_LOG_WRITE_FAILED", detail=str(exc))
        # G state unknown: leave the intent open so recover must be run before any further use.
        return {"result": "USAGE_LOG_INCONSISTENT", "reasons": ["USAGE_LOG_WRITE_FAILED"], "registry_intent": intent["seq"]}
    result = "USED"
    if _file_sha(target) != want:
        _quarantine(target)
        result = "USED_OUTPUT_TAMPERED"
    trust.registry.append({"type": "committed", "intent": intent["seq"], "auth_key": auth_key, "case": case,
                           "folder": folder.name, "result": result, "output_name": target.name,
                           "output_sha": want, "at": clock()})
    return {"result": result, "copied_to": str(target), "sha256": want, "at": now2,
            "registry_intent": intent["seq"], "challenge": challenge}


def _file_sha(path: pathlib.Path) -> str | None:
    try:
        return _sha(path.read_bytes())
    except OSError:
        return None


def verify_output(trust: Trust, output: pathlib.Path) -> dict:
    """Check a published output against the SHA recorded in the committed registry entry."""
    reg = trust.read_registry()
    entries = [e for e in reg if e["type"] == "committed" and e.get("output_name") == output.name]
    if not entries:
        return {"ok": False, "reasons": ["OUTPUT_NOT_REGISTERED"]}
    ok = _file_sha(output) == entries[-1]["output_sha"]
    return {"ok": ok, "reasons": [] if ok else ["OUTPUT_TAMPERED"], "registered_sha": entries[-1]["output_sha"]}


# ---------------------------------------------------------------- withdraw / recover

def withdraw(trust: Trust, case: str, m: str | None, reason: str, *, now: str | None = None) -> dict:
    rec = trust.withdrawals.append({"case": case, "M": m or "*", "reason": reason, "at": now or _now()})
    return {"result": "WITHDRAWN", "seq": rec["seq"]}


def recover(trust: Trust, resolve: int | None = None, as_: str | None = None, note: str = "", *,
            now: str | None = None) -> dict:
    registry = trust.read_registry()
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
    v = sub.add_parser("verify"); v.add_argument("folder"); v.add_argument("--output")
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
        view = View(pathlib.Path(a.folder), a.h)
        present = [st for st in STAGE_ORDER if view.get(f"V8B_{st}.json") is not None]
        out = verify_chain(view, trust, signer, upto=present[-1] if present else "S1")
        if a.output:
            out["output"] = verify_output(trust, pathlib.Path(a.output))
            out["ok"] = out["ok"] and out["output"]["ok"]
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
