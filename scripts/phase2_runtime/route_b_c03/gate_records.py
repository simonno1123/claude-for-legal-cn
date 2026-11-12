"""C03 V8-A: pure validator for AR-B-005 gate records (design C03-GATE-ENFORCEMENT-V8 R2).

The validator encodes the adopted gate design R3 (revision 9). It never reads a
clock, the network or files; the caller passes every record and the current time.
The best possible result only says that the records are complete and consistent
(for example ELIGIBLE_TO_REQUEST_AR_B_010). It never authorizes or executes anything.

Exact field contracts are documented in validation/route_b_c03/v8/RECORD_CONTRACTS.md.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
import hashlib
import json
from typing import Any, Callable

SCHEMA = "C03-V8-R1"
DESIGN_ID = "C03-GATE-DESIGN-005"
CHECKLIST_ID = "CL-005-R2"
ADOPTED_R3_SHA256 = "1029BD425BDBC10DD641FA4AC6A85A2845E75AD0C17B7FABA1342C3E49C0CFEB"
MAX_SAFE_INT = 2**53 - 1
BEIJING = timezone(timedelta(hours=8))

CHECKLIST = tuple(f"C{i}" for i in range(1, 12))
METHODS = {"file_a", "file_b", "chat_c"}
DISPOSITIONS = (
    "REJECT",
    "REQUEST CORRECTION",
    "KEEP BLOCKED",
    "APPROVE A SPECIFIC CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP",
)
APPROVE = DISPOSITIONS[3]
PERMITTED_CLASSES = {
    "C03_ISSUE_MATRIX_CANDIDATE",
    "C03_ADVERSE_CONDITION_REGISTER_CANDIDATE",
    "C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE",
    "C03_AUTHORITY_CHECK_REQUEST_CANDIDATE",
    "C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE",
}
AUDIENCE = "复核人本人"
# R3 §4.2 closed allowed-use table: use code -> (tier, permitted classes, next step)
ALLOWED_USES = {
    "U1": ("L1", PERMITTED_CLASSES, "内部存档整理"),
    "U2": ("L2", PERMITTED_CLASSES - {"C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE"}, "自行起草参考"),
    "U3": ("L2", PERMITTED_CLASSES - {"C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE"}, "自行沟通准备参考"),
}
PROHIBITED_PURPOSE_MARKERS = ("对外", "转发", "附件", "提交法院", "发送委托人", "发给委托人")
POST_REVIEW_FIELDS = {"disposition", "checklist", "actual_scope", "validity_cutoff", "reason"}
VISIBLE_OPINIONS = {"通过", "不通过", "无法判断-可见范围内"}
# R3 §6.2: the only sub-judgments that may be marked as de-identification blind scope
BLIND_SUBS = {
    "C1": "真实案件身份",
    "C2": "原件SHA与证据矩阵",
    "C3": "出处是否真实支持",
    "C4": "依据是否仍有效",
    "C5": "真实日期与是否届满",
    "C9": "原件中未列出的冲突",
    "C10": "原包最少化",
    "C11": "原包输入输出SHA",
}
STAGES = ("review", "application", "authorization", "use")
Q_ROW_KEYS = {"deadlines", "new_deadlines", "expired_deadlines", "cutoff", "authority", "qualification", "withdrawal"}
AUTH_CHECK_KEYS = {"exists", "not_withdrawn", "own_deadline_ok", "count_ok", "action_scope_match"}

# Ordered reason codes (design §五). Output keeps this order.
REASON_ORDER = (
    "RECORD_INVALID",
    "DESIGN_VERSION_MISMATCH",
    "CHAIN_BROKEN",
    "BINDING_MISMATCH",
    "M_CONTAINS_POST_REVIEW_FIELD",
    "PRE_REVIEW_DECLARATION_INVALID",
    "PURPOSE_PROHIBITED",
    "TIER_INVALID",
    "PURPOSE_NOT_ESTABLISHED",
    "OUTPUT_CLASS_NOT_PERMITTED",
    "EGRESS_CHAIN_INVALID",
    "RESEND_DETECTED",
    "MULTIPLE_CROSS_CHECKS",
    "CROSS_CHECK_INCOMPLETE",
    "SAME_MODEL_FAMILY",
    "MODEL_SOURCE_UNKNOWN",
    "STOP_UNRESOLVED",
    "STOP_RELEVANCE_UNANSWERED",
    "STOP_INDEX_NOT_CLEARED",
    "PAUSED_PENDING_STOP",
    "R_INVALIDATED_BY_NEW_STOP",
    "DISPOSITION_NOT_APPROVE",
    "CHECKLIST_NOT_ALL_PASS",
    "MATERIAL_CONFLICT_OPEN",
    "WITHDRAWN_OR_SUPERSEDED",
    "DEADLINE_STATUS_UNKNOWN",
    "VALIDITY_CUTOFF_MISMATCH",
    "EVENT_ORDER_INVALID",
    "COOLING_PERIOD_UNMET",
    "RECONFIRMATION_MISSING",
    "VALIDITY_EXPIRED",
    "RECHECK_MISSING",
    "AUTHORIZATION_INVALID",
    "USAGE_COUNT_UNVERIFIED",
)


class RecordError(ValueError):
    """Raised for a record that cannot be parsed or canonicalized."""


# ---------------------------------------------------------------- JCS (RFC 8785)

def _check_value(value: Any) -> None:
    if value is None or isinstance(value, bool):
        return
    if isinstance(value, int):
        if not -MAX_SAFE_INT <= value <= MAX_SAFE_INT:
            raise RecordError("integer outside the safe range")
        return
    if isinstance(value, float):
        raise RecordError("floating-point numbers are not allowed")
    if isinstance(value, str):
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as exc:  # lone surrogate
            raise RecordError("string is not valid Unicode") from exc
        return
    if isinstance(value, list):
        for item in value:
            _check_value(item)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            if not isinstance(key, str):
                raise RecordError("object keys must be strings")
            _check_value(key)
            _check_value(item)
        return
    raise RecordError(f"unsupported type {type(value).__name__}")


def _jcs(value: Any) -> str:
    if value is None:
        return "null"
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, str):
        return json.dumps(value, ensure_ascii=False)
    if isinstance(value, list):
        return "[" + ",".join(_jcs(v) for v in value) + "]"
    keys = sorted(value, key=lambda k: k.encode("utf-16-be"))
    return "{" + ",".join(json.dumps(k, ensure_ascii=False) + ":" + _jcs(value[k]) for k in keys) + "}"


def canonical_bytes(value: Any) -> bytes:
    """RFC 8785 canonical form for the constrained domain (no floats, safe integers)."""
    _check_value(value)
    return _jcs(value).encode("utf-8")


def record_sha256(value: Any) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest().upper()


def parse_record(text: str) -> dict:
    """Parse one JSON record; reject duplicate keys, floats and non-objects."""

    def no_dupes(pairs):
        out = {}
        for key, val in pairs:
            if key in out:
                raise RecordError(f"duplicate key {key!r}")
            out[key] = val
        return out

    def no_float(_text):
        raise RecordError("floating-point numbers are not allowed")

    try:
        value = json.loads(text, object_pairs_hook=no_dupes, parse_float=no_float)
    except json.JSONDecodeError as exc:
        raise RecordError(f"invalid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise RecordError("a record must be a JSON object")
    _check_value(value)
    return value


# ---------------------------------------------------------------- field checks

def parse_time(value: Any) -> datetime | None:
    if not isinstance(value, str) or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError:
        return None
    if parsed.tzinfo is None:
        return None
    return parsed


def is_sha(value: Any) -> bool:
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789ABCDEF" for c in value)


def is_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def is_date(value: Any) -> bool:
    try:
        date.fromisoformat(value)
        return isinstance(value, str) and len(value) == 10
    except (TypeError, ValueError):
        return False


def _obj(value: Any, spec: dict[str, Callable[[Any], bool]]) -> bool:
    return isinstance(value, dict) and set(value) == set(spec) and all(check(value[k]) for k, check in spec.items())


def _list_of(check: Callable[[Any], bool], *, nonempty: bool = False) -> Callable[[Any], bool]:
    return lambda v: isinstance(v, list) and (bool(v) or not nonempty) and all(check(i) for i in v)


def _const(*allowed: Any) -> Callable[[Any], bool]:
    return lambda v: v in allowed


def _opt(check: Callable[[Any], bool]) -> Callable[[Any], bool]:
    return lambda v: v is None or check(v)


def _answers_shape(v: Any) -> bool:
    """Stop-index query: per discovery event the reviewer's answers (design §七 item 1)."""
    if not isinstance(v, dict) or set(v) != {"answers", "last_event"} or not _opt(is_sha)(v["last_event"]):
        return False
    if not isinstance(v["answers"], dict):
        return False
    for key, a in v["answers"].items():
        if not is_sha(key) or not isinstance(a, dict) or set(a) != {"relevant", "reason", "covered", "clearance"}:
            return False
        if a["relevant"] not in {"相关", "不相关"} or not is_text(a["reason"]):
            return False
        if a["relevant"] == "不相关" and (a["covered"] != "不适用" or a["clearance"] is not None):
            return False
        if a["relevant"] == "相关" and not (
            (a["covered"] == "已覆盖" and is_sha(a["clearance"])) or (a["covered"] == "未覆盖" and a["clearance"] is None)
        ):
            return False
    return True


def _deadline(v: Any) -> bool:
    return (isinstance(v, dict) and set(v) == {"item", "status", "expiry"} and is_text(v["item"])
            and v["status"] in {"适用", "无适用期限", "不适用", "未知"}
            and (v["expiry"] is None or parse_time(v["expiry"]) is not None))


def _opinion(item: str) -> Callable[[Any], bool]:
    def check(v: Any) -> bool:
        if not isinstance(v, dict) or set(v) != {"visible", "blind"} or v["visible"] not in VISIBLE_OPINIONS:
            return False
        if v["blind"] is None:
            return True
        return item in BLIND_SUBS and v["blind"] == {"sub": BLIND_SUBS[item], "value": "无法判断-脱敏盲区"}
    return check


def _evidence_item(v: Any) -> bool:
    return _obj(v, {"code": is_text, "sha256": is_sha, "locator": is_text})


SPECS: dict[str, dict[str, Callable[[Any], bool]]] = {
    "M": {
        "candidate": lambda v: _obj(v, {
            "id": is_text, "version": is_text, "output_sha256": is_sha, "generated_at": lambda t: parse_time(t) is not None,
            "class": is_text, "capability": is_text, "operation": is_text, "generator": is_text,
            "generator_model_family": is_text}),
        "case": lambda v: _obj(v, {"code": is_text, "version": is_text}),
        "trace_refs": lambda v: isinstance(v, dict) and bool(v) and all(
            is_text(k) and _obj(r, {"path": is_text, "sha256": is_sha}) for k, r in v.items()),
        "contract_refs": _list_of(is_sha),
        "omission_conflict_adverse_refs": _list_of(is_sha),
        "failure_audit_refs": _list_of(is_sha),
        "authority": lambda v: _obj(v, {"pack_sha256": is_sha, "check_date": is_date, "entries": _list_of(is_text)}),
        "known_limitations": is_text,
        "prohibited_uses": is_text,
        "design_version": lambda v: _obj(v, {"design_id": is_text, "text_sha256": is_sha, "checklist": is_text}),
        "planned_scope": is_text,
        "reviewer": lambda v: _obj(v, {"code": is_text, "qualification_ref": is_text}),
    },
    "I": {"reviewer_name": is_text, "items": lambda v: isinstance(v, dict)},
    "T": {
        "use_code": lambda v: isinstance(v, str), "output_class": is_text, "audience": is_text,
        "next_step": lambda v: isinstance(v, str), "l1_positive_confirmation": _opt(lambda b: isinstance(b, bool)),
        "h_query": _opt(_answers_shape),
        "corrections": _list_of(lambda c: _obj(c, {"discovery": is_sha, "description": is_text, "diff_ref": is_sha})),
    },
    "E": {
        "d_sha256": is_sha, "task_sha256": is_sha, "scope": is_text, "allowed_fields": _list_of(is_text, nonempty=True),
        "receiver": is_text, "conditions": lambda v: isinstance(v, dict), "config_sha256": is_sha,
        "window": lambda v: _obj(v, {"start": lambda t: parse_time(t) is not None, "end": lambda t: parse_time(t) is not None}),
        "withdrawn": lambda v: isinstance(v, bool),
    },
    "S": {
        "sent_sha256": is_sha, "scope": is_text, "receiver": is_text, "config_sha256": is_sha,
        "checks": lambda v: isinstance(v, dict), "h_check": _answers_shape, "request_id": is_text,
        "sent_at": lambda t: parse_time(t) is not None,
    },
    "X": {
        "opinions": lambda v: isinstance(v, dict), "provider": is_text, "model": is_text,
        "model_family": lambda v: isinstance(v, str), "received_at": lambda t: parse_time(t) is not None,
        "request_id": is_text,
    },
    "V": {"item": _const(*CHECKLIST), "issue": is_text,
          "clearance_type": _const("MODEL_FINDING_REFUTED_BY_ORIGINAL", "ORIGINAL_VERIFICATION_OF_BLIND_SCOPE"),
          "evidence": _list_of(_evidence_item, nonempty=True)},
    "W": {"result": _const("通过", "不通过"), "location": _list_of(_evidence_item, nonempty=True)},
    "R": {
        "h_query": _answers_shape, "actual_scope": is_text, "checklist": lambda v: isinstance(v, dict),
        "c11_original_verified": lambda v: isinstance(v, bool), "deadlines": _list_of(_deadline),
        "no_deadline_declaration": lambda v: isinstance(v, bool), "validity_cutoff": _opt(lambda t: parse_time(t) is not None),
        "material_conflict": _const("有", "无"), "withdrawn": lambda v: isinstance(v, bool),
        "disposition": _const(*DISPOSITIONS), "reason": is_text,
    },
    "CORR": {"items": lambda v: isinstance(v, dict) and set(v) <= set(CHECKLIST) and all(x in {"通过", "不通过"} for x in v.values()),
             "statement": is_text},
    "P": {"reconfirm": lambda v: isinstance(v, dict), "authority_recheck_at": lambda t: parse_time(t) is not None,
          "h_increment": _answers_shape},
    "Q": {"stage": _const("Q1", "Q2", "Q3"), "rows": lambda v: isinstance(v, dict), "h_increment": _answers_shape,
          "auth_checks": _opt(lambda v: isinstance(v, dict))},
    "AUTH": {"action": is_text, "scope": lambda v: _obj(v, {"candidate": is_text, "version": is_text, "M": is_sha}),
             "own_deadline": _opt(lambda t: parse_time(t) is not None),
             "max_uses": _opt(lambda n: isinstance(n, int) and not isinstance(n, bool) and n >= 1)},
}
COMMON = {"record", "schema", "formed_at", "method", "refs"}
H_SPECS = {
    "discovery": {"event": _const("discovery"), "type": _const("模型停点", "人工停点"), "case": is_text,
                  "item": is_text, "issue": is_text, "candidate": is_text, "M": is_sha, "X": lambda v: is_sha(v) or v == "不适用",
                  "stage": is_text, "at": lambda t: parse_time(t) is not None},
    "clearance": {"event": _const("clearance"), "type": _const("FINDING_REFUTED", "CORRECTED_IN_CANDIDATE"),
                  "refs_discovery": is_sha, "scope_candidate": _opt(lambda v: isinstance(v, list) and len(v) == 3
                                                                    and is_text(v[0]) and is_text(v[1]) and is_sha(v[2])),
                  "evidence": _list_of(lambda e: _evidence_item(e) or _obj(e, {"record": _const("W", "X"), "sha256": is_sha}),
                                       nonempty=True),
                  "at": lambda t: parse_time(t) is not None},
}
G_SPECS = {
    "initial": {"kind": _const("initial"), "auth": is_sha, "max_uses": lambda n: isinstance(n, int) and not isinstance(n, bool),
                "used": _const(0), "at": lambda t: parse_time(t) is not None},
    "use": {"kind": _const("use"), "auth": is_sha, "q3": is_sha, "at": lambda t: parse_time(t) is not None},
}


def _contract_ok(rec: Any, kind: str) -> bool:
    if not isinstance(rec, dict) or rec.get("record") != kind or rec.get("schema") != SCHEMA:
        return False
    spec = SPECS[kind]
    if set(rec) != COMMON | set(spec):
        return False
    if rec["method"] not in METHODS or parse_time(rec["formed_at"]) is None:
        return False
    if not isinstance(rec["refs"], dict) or not all(is_sha(v) for v in rec["refs"].values()):
        return False
    return all(check(rec[k]) for k, check in spec.items())


def _h_ok(ev: Any) -> bool:
    return isinstance(ev, dict) and ev.get("event") in H_SPECS and _obj(ev, H_SPECS[ev["event"]])


def _g_ok(ev: Any) -> bool:
    return isinstance(ev, dict) and ev.get("kind") in G_SPECS and _obj(ev, G_SPECS[ev["kind"]])


# ---------------------------------------------------------------- dates

def authority_cutoff(check_date: str) -> datetime:
    """R3 §9.2 item 1: 00:00 Beijing time on the 30th day after the check date."""
    day = date.fromisoformat(check_date)
    return datetime.combine(day + timedelta(days=30), datetime.min.time(), BEIJING)


def compute_cutoff(check_date: str, deadlines: list[dict]) -> datetime:
    cutoff = authority_cutoff(check_date)
    for entry in deadlines:
        if entry.get("status") == "适用":
            expiry = parse_time(entry.get("expiry"))
            if expiry is not None and expiry < cutoff:
                cutoff = expiry
    return cutoff


# ---------------------------------------------------------------- validator

class _Ctx:
    def __init__(self, bundle: dict, now: datetime, stage: str):
        self.b = bundle
        self.now = now
        self.stage = stage
        self.reasons: set[str] = set()

    def add(self, code: str) -> None:
        self.reasons.add(code)


def validate(bundle: dict, *, now: str, stage: str = "review") -> dict:
    """Validate one candidate's record bundle.

    bundle keys: M, I, T, R (dicts); optional E, S, P, Q1, Q2, Q3, AUTH (dicts);
    X, V, W, CORR, G (lists of dicts); H (list of stop-index events).
    Returns {"result": ..., "reasons": [...]}.
    """
    now_t = parse_time(now)
    if now_t is None or stage not in STAGES:
        return {"result": "BLOCKED", "reasons": ["RECORD_INVALID"]}
    c = _Ctx(bundle, now_t, stage)
    if not _check_contracts(c):
        return _finish(c)

    b = c.b
    M, I, T, R = b["M"], b["I"], b["T"], b["R"]
    sha = {k: record_sha256(b[k]) for k in ("M", "I", "T", "R")}
    c.sha = sha
    c.case = M["case"]["code"]
    c.cand = [M["candidate"]["id"], M["candidate"]["version"], sha["M"]]
    c.discoveries = [e for e in b["H"] if e["event"] == "discovery" and e["case"] == c.case]
    c.clearances = [e for e in b["H"] if e["event"] == "clearance"]
    c.trace = {r["sha256"] for r in M["trace_refs"].values()}

    if M["design_version"] != {"design_id": DESIGN_ID, "text_sha256": ADOPTED_R3_SHA256, "checklist": CHECKLIST_ID}:
        c.add("DESIGN_VERSION_MISMATCH")
    _ref(c, I, "M", sha["M"])
    _ref(c, T, "M", sha["M"])
    _ref(c, T, "I", sha["I"])
    _ref(c, R, "M", sha["M"])
    _ref(c, R, "I", sha["I"])
    _ref(c, R, "T", sha["T"])
    if POST_REVIEW_FIELDS & set(M) or POST_REVIEW_FIELDS & set(M["candidate"]):
        c.add("M_CONTAINS_POST_REVIEW_FIELD")

    _check_declaration(c, I, T)
    tier = _check_purpose(c, M, T)
    x_main = _check_l2(c) if tier == "L2" else None
    if tier == "L1" and (b.get("E") or b.get("S") or b["X"]):
        c.add("EGRESS_CHAIN_INVALID")
    _check_stops_before_r(c, tier, x_main)
    _check_disposition(c, R)
    cutoff = _check_deadlines(c, M, R)
    t_r = parse_time(R["formed_at"])
    if not parse_time(T["formed_at"]) < t_r:
        c.add("EVENT_ORDER_INVALID")
    if cutoff is not None and not t_r < cutoff:
        c.add("VALIDITY_EXPIRED")
    stage_records = []
    if tier == "L2":
        P = _check_p(c, x_main, t_r, cutoff)
        if P is not None:
            stage_records.append(P)
    if cutoff is not None and not c.now < cutoff:
        c.add("VALIDITY_EXPIRED")
    stage_records += _check_q(c, tier, cutoff)
    _check_increments(c, t_r, stage_records)
    _check_stops_after_r(c, t_r, stage_records)
    return _finish(c)


def _check_contracts(c: _Ctx) -> bool:
    b = c.b
    for k in ("M", "I", "T", "R"):
        if b.get(k) is None:
            c.add("CHAIN_BROKEN")
    for k in ("X", "V", "W", "CORR", "G", "H"):
        b.setdefault(k, [])
        if not isinstance(b[k], list):
            c.add("RECORD_INVALID")
    if c.reasons:
        return False
    try:
        for k, v in b.items():
            for rec in (v if isinstance(v, list) else [v]):
                if rec is not None:
                    canonical_bytes(rec)
    except RecordError:
        c.add("RECORD_INVALID")
        return False
    for kind in ("M", "I", "T", "R", "E", "S", "P", "AUTH"):
        if b.get(kind) is not None and not _contract_ok(b[kind], kind):
            c.add("RECORD_INVALID")
    for q in ("Q1", "Q2", "Q3"):
        if b.get(q) is not None and not (_contract_ok(b[q], "Q") and b[q]["stage"] == q):
            c.add("RECORD_INVALID")
    for kind in ("X", "V", "W", "CORR"):
        for rec in b[kind]:
            if not _contract_ok(rec, kind):
                c.add("RECORD_INVALID")
    if not all(_h_ok(e) for e in b["H"]) or not all(_g_ok(e) for e in b["G"]):
        c.add("RECORD_INVALID")
    return not c.reasons


def _ref(c: _Ctx, rec: dict, name: str, target: str | None) -> None:
    got = rec["refs"].get(name)
    if got is None or target is None:
        c.add("CHAIN_BROKEN")
    elif got != target:
        c.add("BINDING_MISMATCH")


def _check_declaration(c: _Ctx, I: dict, T: dict) -> None:
    items = I["items"]
    ok = (set(items) == {"1", "2", "3", "4", "5", "6"}
          and all(items[k] == "确认" for k in ("1", "2", "3", "5", "6"))
          and items["4"] in {"提供并确认", "仅确认", "未参与"})
    if not ok or not parse_time(I["formed_at"]) < parse_time(T["formed_at"]):
        c.add("PRE_REVIEW_DECLARATION_INVALID")


def _check_purpose(c: _Ctx, M: dict, T: dict) -> str | None:
    use, step = T["use_code"], T["next_step"]
    if T["audience"] != AUDIENCE or any(m in step for m in PROHIBITED_PURPOSE_MARKERS):
        c.add("PURPOSE_PROHIBITED")
    if T["output_class"] != M["candidate"]["class"]:
        c.add("BINDING_MISMATCH")
    if T["output_class"] not in PERMITTED_CLASSES:
        c.add("OUTPUT_CLASS_NOT_PERMITTED")
    if use not in ALLOWED_USES:
        c.add("PURPOSE_NOT_ESTABLISHED")
        return None
    tier, classes, wanted_step = ALLOWED_USES[use]
    if step != wanted_step and "PURPOSE_PROHIBITED" not in c.reasons:
        c.add("PURPOSE_NOT_ESTABLISHED")
    if (tier == "L1" and T["l1_positive_confirmation"] is not True) or (tier == "L2" and T["l1_positive_confirmation"] is True):
        c.add("TIER_INVALID")
    if tier == "L2" and T["h_query"] is None:
        c.add("STOP_RELEVANCE_UNANSWERED")
    if T["output_class"] not in classes:
        c.add("OUTPUT_CLASS_NOT_PERMITTED")
    return tier


def _check_l2(c: _Ctx) -> dict | None:
    b, M, T = c.b, c.b["M"], c.b["T"]
    E, S, X = b.get("E"), b.get("S"), b["X"]
    if E is None or S is None:
        c.add("EGRESS_CHAIN_INVALID")
        return None
    sha_e, sha_s = record_sha256(E), record_sha256(S)
    if E["refs"] != {"M": c.sha["M"], "T": c.sha["T"]} or S["refs"] != {"E": sha_e}:
        c.add("EGRESS_CHAIN_INVALID")
    cond = E["conditions"]
    if set(cond) != {"retention", "training", "reshare", "region"} or any(v != "接受" for v in cond.values()) or E["withdrawn"]:
        c.add("EGRESS_CHAIN_INVALID")
    checks = S["checks"]
    if set(checks) != {"1", "2", "3", "4", "5", "6"} or any(v != "通过" for v in checks.values()):
        c.add("EGRESS_CHAIN_INVALID")
    if (S["sent_sha256"] != E["d_sha256"] or S["receiver"] != E["receiver"] or S["scope"] != E["scope"]
            or S["config_sha256"] != E["config_sha256"]):
        c.add("EGRESS_CHAIN_INVALID")
    w0, w1, sent = parse_time(E["window"]["start"]), parse_time(E["window"]["end"]), parse_time(S["sent_at"])
    if not (parse_time(E["formed_at"]) < sent and w0 <= sent < w1 and parse_time(T["formed_at"]) < parse_time(E["formed_at"])):
        c.add("EGRESS_CHAIN_INVALID")
    # R3 §7.4 item 6: pre-send stop-index check between T and the send, answered event by event
    pre_send = [e for e in c.discoveries if parse_time(T["formed_at"]) <= parse_time(e["at"]) < sent]
    if not _answered(S["h_check"], pre_send):
        c.add("EGRESS_CHAIN_INVALID")
    for ev in pre_send:
        if _is_related(S["h_check"], ev) and not _covered(c, ev, before=sent, allow_correction=False, answers=S["h_check"]):
            c.add("EGRESS_CHAIN_INVALID")
    # R3 §6.5 item 1: one send and one cross-check per M
    if len(X) != 1:
        c.add("MULTIPLE_CROSS_CHECKS" if len(X) > 1 else "CROSS_CHECK_INCOMPLETE")
        if not X:
            return None
    x = X[0]
    if x["refs"] != {"S": sha_s}:
        c.add("CHAIN_BROKEN")
    received = parse_time(x["received_at"])
    if x["request_id"] != S["request_id"] or received < sent:
        c.add("EGRESS_CHAIN_INVALID")
    ops = x["opinions"]
    if set(ops) != set(CHECKLIST) or not all(_opinion(item)(op) for item, op in ops.items()):
        c.add("CROSS_CHECK_INCOMPLETE")
    family = x["model_family"].strip()
    if not family or family == "未知":
        c.add("MODEL_SOURCE_UNKNOWN")
    elif family == M["candidate"]["generator_model_family"]:
        c.add("SAME_MODEL_FAMILY")
    return x


def _answered(query: dict, events: list[dict]) -> bool:
    answers = query["answers"]
    return all(record_sha256(ev) in answers for ev in events)


def _is_related(query: dict, ev: dict) -> bool:
    return query["answers"].get(record_sha256(ev), {}).get("relevant") != "不相关"


def _evidence_in_m(c: _Ctx, evidence: list) -> bool:
    return bool(evidence) and all("code" in e and e["sha256"] in c.trace for e in evidence)


def _covered(c: _Ctx, ev: dict, *, before: datetime, allow_correction: bool, answers: dict) -> bool:
    """A related discovery is covered only if the reviewer answered 已覆盖 and the cited clearance checks out."""
    a = answers["answers"].get(record_sha256(ev))
    if not a or a["covered"] != "已覆盖":
        return False
    for cl in c.clearances:
        if record_sha256(cl) != a["clearance"] or cl["refs_discovery"] != record_sha256(ev):
            continue
        if not parse_time(cl["at"]) < before:
            return False
        if cl["type"] == "FINDING_REFUTED":
            return _evidence_in_m(c, cl["evidence"])
        return allow_correction and _correction_ok(c, ev, cl)
    return False


def _correction_ok(c: _Ctx, ev: dict, cl: dict) -> bool:
    """R3 §6.5 item 5: T records the correction; L1 needs W, L2 needs this round's X passing the item."""
    if cl["scope_candidate"] != c.cand:
        return False
    ev_sha = record_sha256(ev)
    T = c.b["T"]
    if not any(k["discovery"] == ev_sha for k in T["corrections"]):
        return False
    cl_at = parse_time(cl["at"])
    for e in cl["evidence"]:
        if e.get("record") == "W":
            for w in c.b["W"]:
                if (record_sha256(w) == e["sha256"] and w["result"] == "通过"
                        and w["refs"] == {"M": c.sha["M"], "T": c.sha["T"], "discovery": ev_sha}
                        and parse_time(w["formed_at"]) < cl_at):
                    return True
        if e.get("record") == "X":
            for x in c.b["X"]:
                op = x["opinions"].get(ev["item"])
                if (record_sha256(x) == e["sha256"] and isinstance(op, dict) and op.get("visible") == "通过"
                        and op.get("blind") is None and parse_time(x["received_at"]) < cl_at):
                    return True
    return False


def _check_stops_before_r(c: _Ctx, tier: str | None, x_main: dict | None) -> None:
    b, R = c.b, c.b["R"]
    t_r = parse_time(R["formed_at"])
    if x_main is not None and set(x_main["opinions"]) == set(CHECKLIST):
        sha_x = record_sha256(x_main)
        for item, op in x_main["opinions"].items():
            needs = []
            if op.get("visible") != "通过":
                needs.append("MODEL_FINDING_REFUTED_BY_ORIGINAL")
            if op.get("blind") is not None:
                needs.append("ORIGINAL_VERIFICATION_OF_BLIND_SCOPE")
            for wanted in needs:
                if not any(v["item"] == item and v["clearance_type"] == wanted
                           and v["refs"] == {"M": c.sha["M"], "T": c.sha["T"], "X": sha_x}
                           and _evidence_in_m(c, v["evidence"]) and parse_time(v["formed_at"]) < t_r for v in b["V"]):
                    c.add("STOP_UNRESOLVED")
    before_r = [e for e in c.discoveries if parse_time(e["at"]) < t_r]
    if not _answered(R["h_query"], before_r):
        c.add("STOP_RELEVANCE_UNANSWERED")
    if tier == "L2" and b["T"]["h_query"] is not None:
        before_t = [e for e in c.discoveries if parse_time(e["at"]) < parse_time(b["T"]["formed_at"])]
        if not _answered(b["T"]["h_query"], before_t):
            c.add("STOP_RELEVANCE_UNANSWERED")
    for ev in before_r:
        if _is_related(R["h_query"], ev) and not _covered(c, ev, before=t_r, allow_correction=True, answers=R["h_query"]):
            c.add("STOP_INDEX_NOT_CLEARED")


def _check_disposition(c: _Ctx, R: dict) -> None:
    if R["disposition"] != APPROVE:
        c.add("DISPOSITION_NOT_APPROVE")
    checklist = dict(R["checklist"])
    for corr in sorted(c.b["CORR"], key=lambda x: parse_time(x["formed_at"])):
        if corr["refs"] != {"R": c.sha["R"]}:
            c.add("BINDING_MISMATCH")
            continue
        checklist.update(corr["items"])
    if set(checklist) != set(CHECKLIST) or any(checklist[k] != "通过" for k in CHECKLIST) or not R["c11_original_verified"]:
        c.add("CHECKLIST_NOT_ALL_PASS")
    if R["material_conflict"] != "无":
        c.add("MATERIAL_CONFLICT_OPEN")
    if R["withdrawn"]:
        c.add("WITHDRAWN_OR_SUPERSEDED")


def _check_deadlines(c: _Ctx, M: dict, R: dict) -> datetime | None:
    deadlines = R["deadlines"]
    unknown = (any(d["status"] == "未知" for d in deadlines)
               or any(d["status"] == "适用" and d["expiry"] is None for d in deadlines)
               or (not deadlines and not R["no_deadline_declaration"]))
    if unknown:
        c.add("DEADLINE_STATUS_UNKNOWN")
        return None
    cutoff = compute_cutoff(M["authority"]["check_date"], deadlines)
    if parse_time(R["validity_cutoff"]) != cutoff:
        c.add("VALIDITY_CUTOFF_MISMATCH")
    return cutoff


def _check_p(c: _Ctx, x_main: dict | None, t_r: datetime, cutoff: datetime | None) -> dict | None:
    P = c.b.get("P")
    if P is None:
        c.add("RECONFIRMATION_MISSING")
        return None
    if P["refs"] != {"R": c.sha["R"]}:
        c.add("BINDING_MISMATCH")
    t_p = parse_time(P["formed_at"])
    if x_main is not None and not parse_time(x_main["received_at"]) < t_r < t_p:
        c.add("EVENT_ORDER_INVALID")
    if t_p - t_r < timedelta(hours=24):
        c.add("COOLING_PERIOD_UNMET")
    if cutoff is not None and not t_p < cutoff:
        c.add("VALIDITY_EXPIRED")
    rec = P["reconfirm"]
    recheck = parse_time(P["authority_recheck_at"])
    if set(rec) != {"1", "2", "3", "4"} or any(v != "已重查" for v in rec.values()) or not t_r < recheck <= t_p:
        c.add("RECONFIRMATION_MISSING")
    return P


def _check_q(c: _Ctx, tier: str | None, cutoff: datetime | None) -> list[dict]:
    b, R = c.b, c.b["R"]
    needed = {"review": (), "application": ("Q1",), "authorization": ("Q1", "Q2"), "use": ("Q1", "Q2", "Q3")}[c.stage]
    P = b.get("P") if tier == "L2" else None
    prev_t = parse_time(P["formed_at"]) if P is not None else parse_time(R["formed_at"])
    out = []
    shas = {}
    for name in ("Q1", "Q2", "Q3"):
        q = b.get(name)
        if q is None:
            if name in needed:
                c.add("RECHECK_MISSING")
            continue
        shas[name] = record_sha256(q)
        t_q = parse_time(q["formed_at"])
        rows = q["rows"]
        rows_ok = (set(rows) == Q_ROW_KEYS and rows["deadlines"] == R["deadlines"]
                   and rows["new_deadlines"] == "无" and rows["expired_deadlines"] == "无"
                   and cutoff is not None and parse_time(rows["cutoff"]) == cutoff
                   and rows["authority"] == "仍有效" and rows["qualification"] == "无变化" and rows["withdrawal"] == "未撤回")
        if not rows_ok or not prev_t < t_q or (cutoff is not None and not t_q < cutoff):
            c.add("RECHECK_MISSING")
        prev_t = t_q
        out.append(q)
    # exact record chain (R3 §9.6, §十一)
    base = {"R": c.sha["R"]}
    if P is not None:
        base["P"] = record_sha256(P)
    q1, q2, q3, auth = b.get("Q1"), b.get("Q2"), b.get("Q3"), b.get("AUTH")
    if q1 is not None:
        body = q1["refs"].get("application_body")
        if q1["refs"] != {**base, "application_body": body}:
            c.add("BINDING_MISMATCH")
        if q2 is not None and q2["refs"] != {"Q1": shas["Q1"], "application_body": body}:
            c.add("BINDING_MISMATCH")
        if auth is not None and q2 is not None and auth["refs"] != {"Q2": shas["Q2"], "application_body": body}:
            c.add("AUTHORIZATION_INVALID")
    if c.stage == "use":
        _check_use(c, q3, auth, shas)
    return out


def _check_use(c: _Ctx, q3: dict | None, auth: dict | None, shas: dict) -> None:
    if auth is None or q3 is None or "Q2" not in shas:
        c.add("AUTHORIZATION_INVALID")
        return
    auth_sha = record_sha256(auth)
    if q3["refs"] != {"AUTH": auth_sha, "Q2": shas["Q2"]}:
        c.add("AUTHORIZATION_INVALID")
    if parse_time(auth["formed_at"]) >= parse_time(q3["formed_at"]):
        c.add("AUTHORIZATION_INVALID")
    checks = q3["auth_checks"]
    if not isinstance(checks, dict) or set(checks) != AUTH_CHECK_KEYS or any(v is not True for v in checks.values()):
        c.add("AUTHORIZATION_INVALID")
    if auth["scope"] != {"candidate": c.cand[0], "version": c.cand[1], "M": c.cand[2]} or auth["action"] != c.b["T"]["next_step"]:
        c.add("AUTHORIZATION_INVALID")
    if auth["own_deadline"] is not None and not c.now < parse_time(auth["own_deadline"]):
        c.add("AUTHORIZATION_INVALID")
    if auth["max_uses"] is not None:
        events = [g for g in c.b["G"] if g["auth"] == auth_sha]
        initial = [g for g in events if g["kind"] == "initial"]
        uses = [g for g in events if g["kind"] == "use"]
        ok = (len(initial) == 1 and initial[0]["max_uses"] == auth["max_uses"]
              and parse_time(initial[0]["at"]) <= parse_time(q3["formed_at"])
              and all(parse_time(u["at"]) > parse_time(initial[0]["at"]) and parse_time(u["at"]) <= c.now for u in uses)
              and len(uses) < auth["max_uses"])
        if not ok:
            c.add("USAGE_COUNT_UNVERIFIED")


def _check_increments(c: _Ctx, t_r: datetime, stage_records: list[dict]) -> None:
    """Each P/Q answers every discovery event since the previous query, one by one."""
    prev = t_r
    for rec in stage_records:
        t = parse_time(rec["formed_at"])
        window = [e for e in c.discoveries if prev <= parse_time(e["at"]) < t]
        if not _answered(rec["h_increment"], window):
            c.add("STOP_RELEVANCE_UNANSWERED")
        prev = t


def _check_stops_after_r(c: _Ctx, t_r: datetime, stage_records: list[dict]) -> None:
    """R3 §6.5 item 3 rules 1-3: pause; refute with originals in M and re-form the stage record; else R is invalid."""
    for ev in c.discoveries:
        at = parse_time(ev["at"])
        if not t_r <= at < c.now:
            continue
        ev_sha = record_sha256(ev)
        if any(cl["refs_discovery"] == ev_sha and cl["type"] == "CORRECTED_IN_CANDIDATE" for cl in c.clearances):
            c.add("R_INVALIDATED_BY_NEW_STOP")
            continue
        later = [r for r in stage_records if parse_time(r["formed_at"]) > at]
        if not later:
            c.add("PAUSED_PENDING_STOP")
            continue
        first = later[0]
        answer = first["h_increment"]["answers"].get(ev_sha)
        if answer is None:
            c.add("STOP_RELEVANCE_UNANSWERED")
            continue
        if answer["relevant"] == "不相关":
            continue
        refuted = answer["covered"] == "已覆盖" and any(
            record_sha256(cl) == answer["clearance"] and cl["refs_discovery"] == ev_sha and cl["type"] == "FINDING_REFUTED"
            and at <= parse_time(cl["at"]) < parse_time(first["formed_at"]) and _evidence_in_m(c, cl["evidence"])
            for cl in c.clearances)
        if not refuted:
            c.add("PAUSED_PENDING_STOP")


def _finish(c: _Ctx) -> dict:
    ordered = [r for r in REASON_ORDER if r in c.reasons]
    if ordered:
        return {"result": "BLOCKED", "reasons": ordered}
    positive = {
        "review": "ELIGIBLE_TO_REQUEST_AR_B_010",
        "application": "APPLICATION_RECORDS_COMPLETE",
        "authorization": "AUTHORIZATION_RECORDS_COMPLETE",
        "use": "PRE_USE_RECORDS_COMPLETE",
    }[c.stage]
    return {"result": positive, "reasons": []}
