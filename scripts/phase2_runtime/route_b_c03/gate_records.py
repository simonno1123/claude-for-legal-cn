"""C03 V8-A: pure validator for AR-B-005 gate records (design C03-GATE-ENFORCEMENT-V8 R2).

The validator encodes the adopted gate design R3 (revision 9). It never reads a
clock, the network or files; the caller passes every record and the current time.
The best possible result only says that the records are complete and consistent
(for example ELIGIBLE_TO_REQUEST_AR_B_010). It never authorizes or executes anything.
"""

from __future__ import annotations

from datetime import date, datetime, timedelta, timezone
import hashlib
import json
from typing import Any, Iterable

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
M_POST_REVIEW_FIELDS = {"disposition", "checklist", "actual_scope", "validity_cutoff", "reason"}
OPINIONS = {"通过", "不通过", "无法判断-可见范围内", "无法判断-脱敏盲区"}
# R3 §6.2: items whose visible part must be judged; blind scope is never allowed for these
NO_BLIND_ITEMS = {"C6", "C7", "C8"}
HARD_STOP_ITEMS = {"C5", "C6", "C7"}
STAGES = ("review", "application", "authorization", "use")

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


# ---------------------------------------------------------------- helpers

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


# Closed record contracts (design §4.2). Value is the set of required fields;
# a record may contain only common fields plus these.
COMMON = {"record", "schema", "formed_at", "method", "refs"}
CONTRACTS: dict[str, set[str]] = {
    "M": {
        "candidate", "case", "trace_refs", "contract_refs", "omission_conflict_adverse_refs",
        "failure_audit_refs", "authority", "known_limitations", "prohibited_uses",
        "design_version", "planned_scope", "reviewer",
    },
    "I": {"reviewer_name", "items"},
    "T": {"use_code", "output_class", "audience", "next_step", "l1_positive_confirmation", "h_query"},
    "E": {"d_sha256", "task_sha256", "scope", "allowed_fields", "receiver", "conditions", "config_sha256", "window", "withdrawn"},
    "S": {"sent_sha256", "scope", "receiver", "config_sha256", "checks", "h_last_event", "request_id", "sent_at"},
    "X": {"opinions", "provider", "model", "model_family", "received_at", "request_id"},
    "V": {"item", "issue", "clearance_type", "evidence"},
    "W": {"result", "location"},
    "R": {
        "h_query", "actual_scope", "checklist", "c11_original_verified", "deadlines",
        "no_deadline_declaration", "validity_cutoff", "material_conflict", "withdrawn",
        "disposition", "reason",
    },
    "CORR": {"items", "statement"},
    "P": {"reconfirm", "authority_recheck_at", "h_increment"},
    "Q": {"stage", "rows", "h_increment", "auth_checks"},
    "AUTH": {"action", "scope", "own_deadline", "max_uses"},
}
M_CANDIDATE_FIELDS = {"id", "version", "output_sha256", "generated_at", "class", "capability", "operation", "generator", "generator_model_family"}
H_DISCOVERY_FIELDS = {"event", "type", "case", "item", "issue", "candidate", "M", "X", "stage", "at"}
H_CLEARANCE_FIELDS = {"event", "type", "refs_discovery", "scope_candidate", "evidence", "at"}


def _contract_ok(rec: Any, kind: str) -> bool:
    if not isinstance(rec, dict) or rec.get("record") != kind or rec.get("schema") != SCHEMA:
        return False
    required = COMMON | CONTRACTS[kind]
    if set(rec) != required:
        return False
    if rec.get("method") not in METHODS or parse_time(rec.get("formed_at")) is None:
        return False
    if not isinstance(rec.get("refs"), dict):
        return False
    if kind == "M":
        cand = rec["candidate"]
        if not isinstance(cand, dict) or set(cand) != M_CANDIDATE_FIELDS:
            return False
        if not all(isinstance(rec[f], str) and rec[f].strip() for f in ("known_limitations", "prohibited_uses", "planned_scope")):
            return False
        auth = rec["authority"]
        if not isinstance(auth, dict) or set(auth) != {"pack_sha256", "check_date", "entries"}:
            return False
        if not isinstance(rec["trace_refs"], dict) or not rec["trace_refs"]:
            return False
    return True


def _h_ok(ev: Any) -> bool:
    if not isinstance(ev, dict):
        return False
    if ev.get("event") == "discovery":
        return set(ev) == H_DISCOVERY_FIELDS and ev.get("type") in {"模型停点", "人工停点"} and parse_time(ev.get("at")) is not None
    if ev.get("event") == "clearance":
        return (set(ev) == H_CLEARANCE_FIELDS and ev.get("type") in {"FINDING_REFUTED", "CORRECTED_IN_CANDIDATE"}
                and parse_time(ev.get("at")) is not None)
    return False


# ---------------------------------------------------------------- validator

def validate(bundle: dict, *, now: str, stage: str = "review") -> dict:
    """Validate one candidate's record bundle.

    bundle keys: M, I, T, R (dicts); optional E, S, P, Q1, Q2, Q3, AUTH (dicts);
    X, V, W, CORR, G (lists of dicts); H (list of H events).
    Returns {"result": ..., "reasons": [...]}.
    """
    reasons: set[str] = set()
    add = reasons.add
    now_t = parse_time(now)
    if now_t is None or stage not in STAGES:
        return {"result": "BLOCKED", "reasons": ["RECORD_INVALID"]}

    singles = {k: bundle.get(k) for k in ("M", "I", "T", "R", "E", "S", "P", "Q1", "Q2", "Q3", "AUTH")}
    lists = {k: bundle.get(k) or [] for k in ("X", "V", "W", "CORR", "G", "H")}
    for k in ("M", "I", "T", "R"):
        if singles[k] is None:
            add("CHAIN_BROKEN")
    try:
        for k, rec in singles.items():
            if rec is not None:
                canonical_bytes(rec)
        for k, items in lists.items():
            for rec in items:
                canonical_bytes(rec)
    except RecordError:
        add("RECORD_INVALID")
        return _finish(reasons, stage)

    M, I, T, R = (singles[k] for k in ("M", "I", "T", "R"))
    E, S, P, AUTH = (singles[k] for k in ("E", "S", "P", "AUTH"))
    X, V, W, CORR, H = (lists[k] for k in ("X", "V", "W", "CORR", "H"))

    # rule 1: contracts
    for kind, rec in (("M", M), ("I", I), ("T", T), ("R", R), ("E", E), ("S", S), ("P", P), ("AUTH", AUTH)):
        if rec is not None and not _contract_ok(rec, kind):
            add("RECORD_INVALID")
    for q in ("Q1", "Q2", "Q3"):
        if singles[q] is not None and not _contract_ok(singles[q], "Q"):
            add("RECORD_INVALID")
    for kind, items in (("X", X), ("V", V), ("W", W), ("CORR", CORR)):
        for rec in items:
            if not _contract_ok(rec, kind):
                add("RECORD_INVALID")
    for ev in H:
        if not _h_ok(ev):
            add("RECORD_INVALID")
    if "RECORD_INVALID" in reasons or "CHAIN_BROKEN" in reasons:
        return _finish(reasons, stage)

    sha = {name: record_sha256(rec) for name, rec in (("M", M), ("I", I), ("T", T), ("R", R)) if rec is not None}

    # rule 2: design version
    dv = M["design_version"]
    if dv != {"design_id": DESIGN_ID, "text_sha256": ADOPTED_R3_SHA256, "checklist": CHECKLIST_ID}:
        add("DESIGN_VERSION_MISMATCH")

    # rule 3: chain
    def ref(rec: dict, name: str, target: str | None) -> None:
        got = rec["refs"].get(name)
        if got is None or target is None:
            add("CHAIN_BROKEN")
        elif got != target:
            add("BINDING_MISMATCH")

    ref(I, "M", sha["M"])
    ref(T, "M", sha["M"])
    ref(T, "I", sha["I"])
    ref(R, "M", sha["M"])
    ref(R, "I", sha["I"])
    ref(R, "T", sha["T"])

    # rule 4: M contains no post-review field
    if M_POST_REVIEW_FIELDS & set(M) or M_POST_REVIEW_FIELDS & set(M["candidate"]):
        add("M_CONTAINS_POST_REVIEW_FIELD")

    # rule 5: pre-review declaration
    items = I["items"]
    decl_ok = (
        isinstance(items, dict)
        and set(items) == {"1", "2", "3", "4", "5", "6"}
        and all(items[k] == "确认" for k in ("1", "2", "3", "5", "6"))
        and items["4"] in {"提供并确认", "仅确认", "未参与"}
        and isinstance(I["reviewer_name"], str) and I["reviewer_name"].strip()
    )
    t_i, t_t = parse_time(I["formed_at"]), parse_time(T["formed_at"])
    if not decl_ok or not (t_i < t_t):
        add("PRE_REVIEW_DECLARATION_INVALID")

    # rules 6-9: purpose and tier
    use = T["use_code"]
    next_step = T["next_step"] if isinstance(T["next_step"], str) else ""
    if T["audience"] != AUDIENCE or any(m in next_step for m in PROHIBITED_PURPOSE_MARKERS):
        add("PURPOSE_PROHIBITED")
    tier = None
    if use not in ALLOWED_USES:
        add("PURPOSE_NOT_ESTABLISHED")
    else:
        tier, classes, step = ALLOWED_USES[use]
        if next_step != step and "PURPOSE_PROHIBITED" not in reasons:
            add("PURPOSE_NOT_ESTABLISHED")
        if tier == "L1" and T["l1_positive_confirmation"] is not True:
            add("TIER_INVALID")
        if tier == "L2" and T["l1_positive_confirmation"] not in (False, None):
            add("TIER_INVALID")
        if T["output_class"] not in classes:
            add("OUTPUT_CLASS_NOT_PERMITTED")
    if T["output_class"] != M["candidate"]["class"]:
        add("BINDING_MISMATCH")
    if T["output_class"] not in PERMITTED_CLASSES:
        add("OUTPUT_CLASS_NOT_PERMITTED")

    # L2: egress, cross-check
    x_main = None
    if tier == "L2":
        x_main = _check_l2(M, T, E, S, X, sha, add)

    # stop clearance (rules 14, 15)
    _check_stops(M, T, R, X, V, W, H, sha, x_main, tier, add)

    # rule 16-18
    if R["disposition"] not in DISPOSITIONS:
        add("RECORD_INVALID")
    if R["disposition"] != APPROVE:
        add("DISPOSITION_NOT_APPROVE")
    checklist = dict(R["checklist"]) if isinstance(R["checklist"], dict) else {}
    r_sha = sha["R"]
    for corr in sorted(CORR, key=lambda c: c["formed_at"]):
        if corr["refs"].get("R") != r_sha:
            add("BINDING_MISMATCH")
            continue
        checklist.update(corr["items"])
    if set(checklist) != set(CHECKLIST) or any(checklist[c] != "通过" for c in CHECKLIST) or R["c11_original_verified"] is not True:
        add("CHECKLIST_NOT_ALL_PASS")
    if R["material_conflict"] != "无":
        add("MATERIAL_CONFLICT_OPEN")
    if R["withdrawn"] is not False:
        add("WITHDRAWN_OR_SUPERSEDED")

    # rules 19-22: deadlines and validity
    deadlines = R["deadlines"] if isinstance(R["deadlines"], list) else []
    if any(d.get("status") == "未知" for d in deadlines) or any(
        d.get("status") not in {"适用", "无适用期限", "不适用"} for d in deadlines
    ):
        add("DEADLINE_STATUS_UNKNOWN")
    if any(d.get("status") == "适用" and parse_time(d.get("expiry")) is None for d in deadlines):
        add("DEADLINE_STATUS_UNKNOWN")
    if not deadlines and R["no_deadline_declaration"] is not True:
        add("DEADLINE_STATUS_UNKNOWN")
    cutoff = None
    if "DEADLINE_STATUS_UNKNOWN" not in reasons:
        try:
            cutoff = compute_cutoff(M["authority"]["check_date"], deadlines)
        except (ValueError, TypeError):
            add("RECORD_INVALID")
        if cutoff is not None:
            recorded = parse_time(R["validity_cutoff"])
            if recorded is None or recorded != cutoff:
                add("VALIDITY_CUTOFF_MISMATCH")
    t_r = parse_time(R["formed_at"])
    if not (t_t < t_r):
        add("EVENT_ORDER_INVALID")
    if cutoff is not None and not (t_r < cutoff):
        add("VALIDITY_EXPIRED")

    case = M["case"].get("code") if isinstance(M["case"], dict) else None
    later_answers: dict = {}
    if tier == "L2":
        _check_p(R, P, x_main, t_r, cutoff, sha, add)
        if P is not None:
            t_p = parse_time(P["formed_at"])
            if not _increment_ok(P["h_increment"], H, case, t_r, t_p):
                add("STOP_RELEVANCE_UNANSWERED")
            later_answers.update(_answers(P["h_increment"]))
    if cutoff is not None and not (now_t < cutoff):
        add("VALIDITY_EXPIRED")

    # rule 23: Q records by stage
    _check_q(stage, singles, AUTH, lists["G"], R, P, tier, cutoff, now_t, H, case, later_answers, add)

    # rule 15c: stops discovered after R (R3 §6.5 item 3 rules 1-3)
    _post_r_stops(R, M, H, t_r, now_t, later_answers, add, sha)

    return _finish(reasons, stage)


def _check_l2(M, T, E, S, X, sha, add):
    if E is None or S is None:
        add("EGRESS_CHAIN_INVALID")
        return None
    sha_e, sha_s = record_sha256(E), record_sha256(S)
    if E["refs"].get("M") != sha["M"] or E["refs"].get("T") != sha["T"] or S["refs"].get("E") != sha_e:
        add("EGRESS_CHAIN_INVALID")
    cond = E["conditions"]
    if (not isinstance(cond, dict) or set(cond) != {"retention", "training", "reshare", "region"}
            or any(v != "接受" for v in cond.values()) or E["withdrawn"] is not False):
        add("EGRESS_CHAIN_INVALID")
    checks = S["checks"]
    if not isinstance(checks, dict) or set(checks) != {"1", "2", "3", "4", "5", "6"} or any(v != "通过" for v in checks.values()):
        add("EGRESS_CHAIN_INVALID")
    if (S["sent_sha256"] != E["d_sha256"] or S["receiver"] != E["receiver"] or S["scope"] != E["scope"]
            or S["config_sha256"] != E["config_sha256"]):
        add("EGRESS_CHAIN_INVALID")
    window = E["window"] if isinstance(E["window"], dict) else {}
    w0, w1, sent = parse_time(window.get("start")), parse_time(window.get("end")), parse_time(S["sent_at"])
    t_e = parse_time(E["formed_at"])
    if None in (w0, w1, sent) or not (t_e < sent and w0 <= sent < w1):
        add("EGRESS_CHAIN_INVALID")
    # one S and one X per M (R3 §6.5 item 1)
    xs = [x for x in X]
    if len(xs) > 1:
        add("MULTIPLE_CROSS_CHECKS")
    if not xs:
        add("CROSS_CHECK_INCOMPLETE")
        return None
    x = xs[0]
    if x["refs"].get("S") != sha_s:
        add("CHAIN_BROKEN")
    if x["request_id"] != S["request_id"]:
        add("EGRESS_CHAIN_INVALID")
    received = parse_time(x["received_at"])
    if received is None or sent is None or received < sent:
        add("EGRESS_CHAIN_INVALID")
    ops = x["opinions"]
    if not isinstance(ops, dict) or set(ops) != set(CHECKLIST):
        add("CROSS_CHECK_INCOMPLETE")
    else:
        for item, op in ops.items():
            if not isinstance(op, dict) or op.get("value") not in OPINIONS:
                add("CROSS_CHECK_INCOMPLETE")
            elif op["value"] == "无法判断-脱敏盲区" and (item in NO_BLIND_ITEMS or not op.get("blind_sub")):
                add("CROSS_CHECK_INCOMPLETE")
    family = x["model_family"]
    gen_family = M["candidate"]["generator_model_family"]
    if not isinstance(family, str) or not family.strip() or family == "未知":
        add("MODEL_SOURCE_UNKNOWN")
    elif family == gen_family:
        add("SAME_MODEL_FAMILY")
    return x


def _relevance_ok(query: Any, events: list[dict]) -> bool:
    """Every enumerated discovery event needs a reviewer answer and reason."""
    if not isinstance(query, dict) or not isinstance(query.get("answers"), dict):
        return False
    answers = query["answers"]
    for ev in events:
        a = answers.get(record_sha256(ev))
        if not isinstance(a, dict) or a.get("relevant") not in {"相关", "不相关"} or not str(a.get("reason", "")).strip():
            return False
    return True


def _check_stops(M, T, R, X, V, W, H, sha, x_main, tier, add):
    case = M["case"].get("code") if isinstance(M["case"], dict) else None
    cand = M["candidate"]["id"], M["candidate"]["version"]
    t_r = parse_time(R["formed_at"])
    discoveries = [e for e in H if e["event"] == "discovery" and e["case"] == case]
    clearances = [e for e in H if e["event"] == "clearance"]

    # current-round model stops from X need a V (rule 14)
    if x_main is not None and isinstance(x_main["opinions"], dict):
        sha_x = record_sha256(x_main)
        for item, op in x_main["opinions"].items():
            value = op.get("value") if isinstance(op, dict) else None
            needs = value in {"不通过", "无法判断-可见范围内", "无法判断-脱敏盲区"}
            if not needs:
                continue
            wanted = "ORIGINAL_VERIFICATION_OF_BLIND_SCOPE" if value == "无法判断-脱敏盲区" else "MODEL_FINDING_REFUTED_BY_ORIGINAL"
            ok = any(
                v["item"] == item and v["clearance_type"] == wanted and v["refs"].get("X") == sha_x
                and v["refs"].get("M") == sha["M"] and _evidence_ok(v["evidence"], M)
                for v in V
            )
            if not ok:
                add("STOP_UNRESOLVED")

    # H relevance answers: L1 in R, L2 in T and R (rule 15a)
    before_r = [e for e in discoveries if parse_time(e["at"]) < t_r]
    if not _relevance_ok(R["h_query"], before_r):
        add("STOP_RELEVANCE_UNANSWERED")
    if tier == "L2":
        t_t = parse_time(T["formed_at"])
        if not _relevance_ok(T["h_query"], [e for e in discoveries if parse_time(e["at"]) < t_t]):
            add("STOP_RELEVANCE_UNANSWERED")

    answers = R["h_query"].get("answers", {}) if isinstance(R["h_query"], dict) else {}
    for ev in before_r:
        a = answers.get(record_sha256(ev), {})
        if a.get("relevant") == "不相关":
            continue
        if not _covered(ev, clearances, cand, M, W, sha, t_r, pre_r=True):
            add("STOP_INDEX_NOT_CLEARED")


def _evidence_ok(evidence: Any, M: dict) -> bool:
    if not isinstance(evidence, list) or not evidence:
        return False
    trace = {v.get("sha256") for v in M["trace_refs"].values() if isinstance(v, dict)}
    return all(isinstance(e, dict) and e.get("sha256") in trace and str(e.get("locator", "")).strip() for e in evidence)


def _covered(ev, clearances, cand, M, W, sha, before, *, pre_r):
    ev_sha = record_sha256(ev)
    for c in clearances:
        if c["refs_discovery"] != ev_sha or parse_time(c["at"]) >= before:
            continue
        if c["type"] == "FINDING_REFUTED" and _evidence_ok(c["evidence"], M):
            return True
        if pre_r and c["type"] == "CORRECTED_IN_CANDIDATE" and c["scope_candidate"] == [cand[0], cand[1], sha["M"]]:
            return True
    return False


def _answers(query: Any) -> dict:
    if isinstance(query, dict) and isinstance(query.get("answers"), dict):
        return query["answers"]
    return {}


def _post_r_stops(R, M, H, after, upto, answers, add, sha):
    """R3 §6.5 item 3 rules 1-3 for stops discovered after R."""
    case = M["case"].get("code")
    cand = M["candidate"]["id"], M["candidate"]["version"]
    clearances = [e for e in H if e["event"] == "clearance"]
    for ev in H:
        if ev["event"] != "discovery" or ev["case"] != case:
            continue
        at = parse_time(ev["at"])
        if not (after <= at < upto):
            continue
        if answers.get(record_sha256(ev), {}).get("relevant") == "不相关":
            continue
        if _covered(ev, clearances, cand, M, [], sha, upto, pre_r=False):
            continue
        corrected = any(
            c["refs_discovery"] == record_sha256(ev) and c["type"] == "CORRECTED_IN_CANDIDATE" for c in clearances
        )
        add("R_INVALIDATED_BY_NEW_STOP" if corrected else "PAUSED_PENDING_STOP")


def _increment_ok(inc: Any, H: list, case: str, after: datetime, upto: datetime) -> bool:
    events = [e for e in H if e["event"] == "discovery" and e["case"] == case and after <= parse_time(e["at"]) < upto]
    return _relevance_ok(inc, events)


def _check_p(R, P, x_main, t_r, cutoff, sha, add):
    if P is None:
        add("RECONFIRMATION_MISSING")
        return
    if P["refs"].get("R") != sha["R"]:
        add("BINDING_MISMATCH")
    t_p = parse_time(P["formed_at"])
    if x_main is not None:
        received = parse_time(x_main["received_at"])
        if received is None or not (received < t_r < t_p):
            add("EVENT_ORDER_INVALID")
    if t_p - t_r < timedelta(hours=24):
        add("COOLING_PERIOD_UNMET")
    if cutoff is not None and not (t_p < cutoff):
        add("VALIDITY_EXPIRED")
    rec = P["reconfirm"]
    recheck = parse_time(P["authority_recheck_at"])
    if (not isinstance(rec, dict) or set(rec) != {"1", "2", "3", "4"} or any(v != "已重查" for v in rec.values())
            or recheck is None or not (t_r < recheck <= t_p)):
        add("RECONFIRMATION_MISSING")


def _check_q(stage, singles, AUTH, G, R, P, tier, cutoff, now_t, H, case, later_answers, add):
    needed = {"review": (), "application": ("Q1",), "authorization": ("Q1", "Q2"), "use": ("Q1", "Q2", "Q3")}[stage]
    prev = parse_time(P["formed_at"]) if (tier == "L2" and P is not None) else parse_time(R["formed_at"])
    for name in needed:
        q = singles.get(name)
        if q is None or q["stage"] != name:
            add("RECHECK_MISSING")
            continue
        t_q = parse_time(q["formed_at"])
        rows = q["rows"]
        if (not isinstance(rows, dict) or not rows or any(v != "满足" for v in rows.values())
                or not (prev < t_q) or (cutoff is not None and not (t_q < cutoff))):
            add("RECHECK_MISSING")
        if not _increment_ok(q["h_increment"], H, case, prev, t_q):
            add("STOP_RELEVANCE_UNANSWERED")
        later_answers.update(_answers(q["h_increment"]))
        prev = t_q
    if stage == "use":
        q3 = singles.get("Q3")
        checks = q3["auth_checks"] if q3 is not None else None
        keys = {"exists", "not_withdrawn", "own_deadline_ok", "count_ok", "action_scope_match"}
        if AUTH is None or not isinstance(checks, dict) or set(checks) != keys or any(v is not True for v in checks.values()):
            add("AUTHORIZATION_INVALID")
        if AUTH is not None:
            own = AUTH["own_deadline"]
            if own is not None and (parse_time(own) is None or not now_t < parse_time(own)):
                add("AUTHORIZATION_INVALID")
            if AUTH["max_uses"] is not None:
                auth_sha = record_sha256(AUTH)
                initial = [g for g in G if g.get("kind") == "initial" and g.get("auth") == auth_sha and g.get("used") == 0]
                uses = [g for g in G if g.get("kind") == "use" and g.get("auth") == auth_sha]
                if len(initial) != 1 or len(uses) >= AUTH["max_uses"]:
                    add("USAGE_COUNT_UNVERIFIED")


def _finish(reasons: set[str], stage: str) -> dict:
    ordered = [r for r in REASON_ORDER if r in reasons]
    if ordered:
        return {"result": "BLOCKED", "reasons": ordered}
    positive = {
        "review": "ELIGIBLE_TO_REQUEST_AR_B_010",
        "application": "APPLICATION_RECORDS_COMPLETE",
        "authorization": "AUTHORIZATION_RECORDS_COMPLETE",
        "use": "PRE_USE_RECORDS_COMPLETE",
    }[stage]
    return {"result": positive, "reasons": []}


def check_post_r_stops(bundle: dict, *, now: str) -> list[str]:
    """Expose the R3 §6.5 item 3 post-R rule for stages after R (used by validate)."""
    out: set[str] = set()
    M, R = bundle["M"], bundle["R"]
    sha = {"M": record_sha256(M), "R": record_sha256(R)}
    _post_r_stops(R, M, bundle.get("H") or [], parse_time(R["formed_at"]), parse_time(now), {}, out.add, sha)
    return [r for r in REASON_ORDER if r in out]
