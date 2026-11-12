"""C03 V8-A record builder (design C03-GATE-ENFORCEMENT-V8 R2 §七).

Pre-fills mechanical fields only (hashes, references, validity cutoff, the full
enumeration of stop-index events). It never answers a judgment item: every
declaration, checklist item and stop relevance answer must come from the
reviewer, one item at a time, and is transcribed verbatim. Missing answers are
refused.
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from . import gate_records as g

JUDGMENT_ITEMS = {
    "I": {"1", "2", "3", "4", "5", "6"},
    "R_CHECKLIST": set(g.CHECKLIST),
    "P": {"1", "2", "3", "4"},
}


class MissingAnswer(ValueError):
    """Raised when a judgment item has no reviewer answer."""


def build(kind: str, *, refs: dict, formed_at: str, method: str, **fields: Any) -> dict:
    if method not in g.METHODS:
        raise ValueError("unknown method")
    if g.parse_time(formed_at) is None:
        raise ValueError("formed_at needs an explicit offset")
    record = {"record": kind, "schema": g.SCHEMA, "formed_at": formed_at, "method": method, "refs": dict(refs)}
    record.update(fields)
    g.canonical_bytes(record)
    return record


def require_answers(expected: set[str], answers: dict) -> dict:
    """Return answers unchanged if every expected item has a non-empty answer."""
    missing = sorted(k for k in expected if not str(answers.get(k, "")).strip())
    if missing:
        raise MissingAnswer(f"no reviewer answer for: {', '.join(missing)}")
    return {k: answers[k] for k in sorted(expected)}


def enumerate_stop_events(h_events: list[dict], case: str, *, after: str | None = None, upto: str | None = None) -> list[dict]:
    """List every discovery event for the case in the window, for the reviewer to judge one by one."""
    lo = g.parse_time(after) if after else None
    hi = g.parse_time(upto) if upto else None
    out = []
    for ev in h_events:
        if ev.get("event") != "discovery" or ev.get("case") != case:
            continue
        at = g.parse_time(ev.get("at"))
        if (lo and at < lo) or (hi and at >= hi):
            continue
        out.append({"sha256": g.record_sha256(ev), "item": ev.get("item"), "issue": ev.get("issue"), "at": ev.get("at")})
    out.sort(key=lambda e: (e["at"], e["sha256"]))
    return out


def stop_query(enumerated: list[dict], answers: dict) -> dict:
    """Combine the enumeration with reviewer answers; every event needs relevance and a reason."""
    result = {}
    for ev in enumerated:
        a = answers.get(ev["sha256"])
        if not isinstance(a, dict) or a.get("relevant") not in {"相关", "不相关"} or not str(a.get("reason", "")).strip():
            raise MissingAnswer(f"no relevance answer for event {ev['sha256'][:12]}")
        result[ev["sha256"]] = {"relevant": a["relevant"], "reason": a["reason"]}
    last = enumerated[-1]["sha256"] if enumerated else None
    return {"answers": result, "last_event": last}


def validity_cutoff(check_date: str, deadlines: list[dict]) -> str:
    if any(d.get("status") == "未知" for d in deadlines):
        raise MissingAnswer("a deadline is unknown; R3 §9.2 blocks")
    return g.compute_cutoff(check_date, deadlines).isoformat(timespec="minutes")


def now_text(now: datetime) -> str:
    return now.isoformat(timespec="seconds")
