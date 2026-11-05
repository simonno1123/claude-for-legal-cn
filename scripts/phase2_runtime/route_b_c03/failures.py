"""Pure protected-state, failure, retry, release and recovery-control determinations.

Every function here is a pure evaluation of explicit caller-supplied references: nothing is stored, no clock is
read, nothing is executed. Each returns a protected state; none can reach an executing or activated state.
"""

from __future__ import annotations

from dataclasses import dataclass, fields
from enum import Enum
import hashlib
import json

from .contracts import (
    AuditRecordCandidate,
    CapabilityState,
    ControlState,
    FailureRecord,
    IdempotencyKeyReference,
    IdempotencyRecord,
    InvocationState,
    ReleaseDecisionReference,
    RetryPolicyReference,
    RevocationOrKillReference,
    RollbackReference,
    SupersessionReference,
    TimeoutPolicyReference,
    is_utc_timestamp,
)

class FailureCode(str, Enum):
    TRANSIENT_FAILURE = "TRANSIENT_FAILURE"
    CAPABILITY_DISABLED = "CAPABILITY_DISABLED"
    TIER_B_AUTHORITY_REQUIRED = "TIER_B_AUTHORITY_REQUIRED"
    AUTHORITY_FAILURE = "AUTHORITY_FAILURE"
    IDENTITY_FAILURE = "IDENTITY_FAILURE"
    ISOLATION_FAILURE = "ISOLATION_FAILURE"
    INTEGRITY_FAILURE = "INTEGRITY_FAILURE"
    CREDENTIAL_FAILURE = "CREDENTIAL_FAILURE"
    CONTENT_BOUNDARY_FAILURE = "CONTENT_BOUNDARY_FAILURE"
    OUTPUT_BOUNDARY_FAILURE = "OUTPUT_BOUNDARY_FAILURE"
    DEPENDENCY_NOT_AUTHORIZED = "DEPENDENCY_NOT_AUTHORIZED"
    PROVIDER_NOT_AUTHORIZED = "PROVIDER_NOT_AUTHORIZED"
    KILL_ACTIVE = "KILL_ACTIVE"
    REVOKED = "REVOKED"
    STALE = "STALE"
    TIMEOUT_INCOMPLETE = "TIMEOUT_INCOMPLETE"

    @property
    def retry_eligible_category(self) -> bool:
        return self is FailureCode.TRANSIENT_FAILURE


@dataclass(frozen=True, slots=True)
class RetryDetermination:
    state: ControlState
    reason_code: str
    next_attempt: int | None = None


def build_failure_record(
    failure_id: str,
    reason_code: str,
    correlation_id: str,
    *,
    quarantined: bool = False,
    rejected: bool = False,
) -> FailureRecord:
    state = (
        InvocationState.QUARANTINED
        if quarantined
        else InvocationState.REJECTED
        if rejected
        else InvocationState.BLOCKED
    )
    control = ControlState.QUARANTINED if quarantined else ControlState.PROTECTED_BLOCKED
    return FailureRecord(failure_id, reason_code, state, control, correlation_id)


def protected_state(*, kill_active: bool, revoked: bool, stale: bool) -> ControlState:
    if kill_active:
        return ControlState.KILLED
    if revoked:
        return ControlState.REVOKED
    if stale:
        return ControlState.STALE
    return ControlState.PROTECTED_BLOCKED


def evaluate_retry(
    policy: RetryPolicyReference,
    failure_code: FailureCode,
    completed_attempts: int,
    *,
    identical_scope: bool,
    deadline_valid: bool,
    kill_active: bool,
    revoked: bool,
    stale: bool,
    quarantined: bool,
) -> RetryDetermination:
    if kill_active or revoked or stale or quarantined:
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — PROTECTED STATE")
    if not identical_scope or not deadline_valid:
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — SCOPE/DEADLINE")
    if not isinstance(failure_code, FailureCode):
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — UNKNOWN FAILURE")
    if not failure_code.retry_eligible_category:
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — TERMINAL FAILURE")
    if failure_code.value not in policy.eligible_failure_codes:
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — INELIGIBLE")
    if completed_attempts >= policy.maximum_attempts:
        return RetryDetermination(ControlState.RETRY_DENIED, "RETRY DENIED — EXHAUSTED")
    return RetryDetermination(
        ControlState.RETRY_ELIGIBILITY_PENDING,
        "RETRY ELIGIBLE — EXECUTION NOT AUTHORIZED",
        completed_attempts + 1,
    )


def evaluate_release(
    decision: ReleaseDecisionReference | None,
    *,
    protected_state_reference: str,
    resolution_evidence_reference: str,
) -> ControlState:
    if decision is None:
        return ControlState.RELEASE_PENDING
    if (
        decision.protected_state_reference != protected_state_reference
        or decision.resolution_evidence_reference != resolution_evidence_reference
        or decision.next_state is not ControlState.RELEASED_DISABLED
    ):
        return ControlState.PROTECTED_BLOCKED
    return ControlState.RELEASED_DISABLED


# ---------------------------------------------------------------------------
# WP-009 recovery-control evaluators (AR-B-009, V5)
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class ControlDetermination:
    state: ControlState
    reason_code: str


_SHA256_HEX = frozenset("0123456789ABCDEFabcdef")
AUDIT_CHAIN_GENESIS = "0" * 64
ALL_SCOPES = "ALL"


def _cd(state: ControlState, reason: str) -> ControlDetermination:
    return ControlDetermination(state, reason)


def _is_text(value: object) -> bool:
    return type(value) is str and bool(value.strip())


def _is_sha(value: object) -> bool:
    return type(value) is str and len(value) == 64 and all(c in _SHA256_HEX for c in value)


def _norm(value: str) -> str:
    return value.strip().casefold()


def _is_text_tuple(value: object, *, allow_empty: bool) -> bool:
    return type(value) is tuple and (allow_empty or bool(value)) and all(_is_text(v) for v in value)


def _flag_state(flag: object, state: ControlState, reason: str) -> ControlDetermination | None:
    """True -> the protected state; False -> None (not active); anything else -> control state unknown."""
    if flag is True:
        return _cd(state, reason)
    if flag is False:
        return None
    return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — CONTROL STATE UNKNOWN")


def _days_from_civil(y: int, m: int, d: int) -> int:
    y -= m <= 2
    era = y // 400
    yoe = y - era * 400
    doy = (153 * (m + (-3 if m > 2 else 9)) + 2) // 5 + d - 1
    doe = yoe * 365 + yoe // 4 - yoe // 100 + doy
    return era * 146097 + doe - 719468


def _utc_seconds(value: object) -> int | None:
    """Seconds since 1970 for a valid YYYY-MM-DDTHH:MM:SSZ calendar time, else None (no clock is read)."""
    if not is_utc_timestamp(value):
        return None
    y, mo, d = int(value[0:4]), int(value[5:7]), int(value[8:10])
    hh, mi, ss = int(value[11:13]), int(value[14:16]), int(value[17:19])
    leap = y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)
    month_days = (31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    if not (1 <= mo <= 12 and 1 <= d <= month_days[mo - 1] and hh < 24 and mi < 60 and ss < 60):
        return None
    return _days_from_civil(y, mo, d) * 86400 + hh * 3600 + mi * 60 + ss


def _duration_seconds(value: object) -> int | None:
    """Only the form PT<n>S with n >= 1 is accepted."""
    if type(value) is not str or not value.startswith("PT") or not value.endswith("S"):
        return None
    digits = value[2:-1]
    if not digits or not all(c in "0123456789" for c in digits) or int(digits) < 1:
        return None
    return int(digits)


def evaluate_control_precedence(
    *,
    kill: RevocationOrKillReference | None,
    revocation: RevocationOrKillReference | None,
    control_state_known: bool,
    subject_scope: str,
) -> ControlDetermination:
    """Kill before revocation before anything else; unknown control state fails closed (design 13, 8)."""
    if control_state_known is not True or not _is_text(subject_scope):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — CONTROL STATE UNKNOWN")
    for ref, state, reason in (
        (kill, ControlState.KILLED, "BLOCKED — KILL ACTIVE"),
        (revocation, ControlState.REVOKED, "BLOCKED — REVOKED"),
    ):
        if ref is None:
            continue
        if type(ref) is not RevocationOrKillReference or ref.effective_state is not state:
            return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — STATE CONTRACT FAILURE")
        if not _is_text(ref.affected_scope):
            return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — STATE CONTRACT FAILURE")
        if _norm(ref.affected_scope) in (_norm(subject_scope), _norm(ALL_SCOPES)):
            return _cd(state, reason)
    return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — NO ACTIVE CONTROL; EXECUTION NOT AUTHORIZED")


def evaluate_idempotency(
    key: IdempotencyKeyReference | None,
    prior_records: tuple[IdempotencyRecord, ...],
    *,
    scope_sha256: str,
    evaluated_at: str,
    window_from: str,
    superseded_or_revoked: bool,
) -> ControlDetermination:
    """Duplicate, collision and replay determination over caller-supplied prior records (design 10)."""
    if superseded_or_revoked is not False:
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — VERSION/AUTHORITY FAILURE")
    if (
        type(key) is not IdempotencyKeyReference
        or not _is_text(key.canonicalization_version)
        or key.digest_algorithm != "SHA-256"
        or not _is_text(key.replay_window_reference)
        or not _is_sha(scope_sha256)
        or type(prior_records) is not tuple
        or any(type(r) is not IdempotencyRecord for r in prior_records)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — IDEMPOTENCY UNBOUND")
    if not (is_utc_timestamp(evaluated_at) and is_utc_timestamp(window_from) and window_from <= evaluated_at):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — REPLAY FAILURE")
    key_id = key.key_sha256.upper()
    matches = [r for r in prior_records if r.key_sha256.upper() == key_id]
    if any(r.recorded_at > evaluated_at for r in matches):
        return _cd(ControlState.QUARANTINED, "QUARANTINED — IDEMPOTENCY RECORD INCONSISTENT")
    if any(r.scope_sha256.upper() != scope_sha256.upper() for r in matches):
        return _cd(ControlState.QUARANTINED, "QUARANTINED — IDEMPOTENCY COLLISION")
    in_window = [r for r in matches if r.recorded_at >= window_from]
    if matches and not in_window:
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — REPLAY FAILURE")
    if any(r.effect_reference != "NONE" for r in in_window):
        return _cd(ControlState.PROTECTED_BLOCKED, "DUPLICATE DENIED — NO SECOND EFFECT")
    if in_window:
        return _cd(ControlState.PROTECTED_BLOCKED, "DUPLICATE DENIED — PRIOR PROTECTED REFERENCE")
    return _cd(ControlState.PROTECTED_BLOCKED, "FIRST USE — EXECUTION NOT AUTHORIZED")


def evaluate_timeout(
    policy: TimeoutPolicyReference | None,
    *,
    started_at: str,
    deadline_at: str,
    observed_at: str,
    result_received_at: str | None,
) -> ControlDetermination:
    """Timeout and late-result determination over caller-supplied times; no clock is read (design 11).

    The deadline must equal started_at plus the policy's own duration (PT<n>S), so the caller cannot widen it.
    """
    start_s = _utc_seconds(started_at)
    deadline_s = _utc_seconds(deadline_at)
    observed_s = _utc_seconds(observed_at)
    duration_s = _duration_seconds(policy.deadline_duration) if type(policy) is TimeoutPolicyReference else None
    if (
        type(policy) is not TimeoutPolicyReference
        or policy.terminal_state is not ControlState.QUARANTINED
        or policy.late_result_policy != "DENY_USE"
        or policy.retry_effect != "NONE"
        or None in (start_s, deadline_s, observed_s, duration_s)
        or deadline_s - start_s != duration_s
        or not start_s <= observed_s
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — TIMEOUT POLICY UNBOUND")
    if result_received_at is not None:
        result_s = _utc_seconds(result_received_at)
        if result_s is None or not start_s <= result_s <= observed_s:
            return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — TIMEOUT POLICY UNBOUND")
        if result_received_at >= deadline_at:
            return _cd(ControlState.QUARANTINED, "QUARANTINED — LATE RESULT DENIED")
        return _cd(ControlState.PROTECTED_BLOCKED, "RESULT WITHIN DEADLINE — CONSUMPTION NOT AUTHORIZED")
    if observed_at >= deadline_at:
        return _cd(ControlState.QUARANTINED, "QUARANTINED — INCOMPLETE")
    return _cd(ControlState.PROTECTED_BLOCKED, "DEADLINE PENDING — NO RESULT")


def evaluate_rollback(
    reference: RollbackReference | None,
    *,
    accepted_prior_identities: tuple[str, ...],
    decision_reference_valid: bool,
    kill_active: bool,
    revoked: bool,
) -> ControlDetermination:
    """Rollback eligibility only; never restores (design 14). Text comparisons ignore case and outer spaces."""
    for flag, state, reason in (
        (kill_active, ControlState.KILLED, "BLOCKED — KILL ACTIVE"),
        (revoked, ControlState.REVOKED, "BLOCKED — REVOKED"),
    ):
        protected = _flag_state(flag, state, reason)
        if protected is not None:
            return protected
    if (
        type(reference) is not RollbackReference
        or not all(_is_text(v) for v in (reference.rollback_id, reference.version, reference.current_identity,
                                         reference.target_identity, reference.decision_reference))
        or not _is_text_tuple(reference.restoration_surface, allow_empty=False)
        or not _is_text_tuple(reference.prohibited_surface, allow_empty=False)
        or not _is_text_tuple(reference.preconditions, allow_empty=True)
        or not _is_text_tuple(accepted_prior_identities, allow_empty=True)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — REFERENCE INVALID")
    if reference.post_restore_state is not CapabilityState.DISABLED:
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — RESTORE MUST RETURN TO DISABLED")
    target = _norm(reference.target_identity)
    if target == _norm(reference.current_identity) or target not in {_norm(a) for a in accepted_prior_identities}:
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — TARGET NOT AN ACCEPTED PRIOR VERSION")
    restoration = {_norm(v) for v in reference.restoration_surface}
    prohibited = {_norm(v) for v in reference.prohibited_surface}
    if _norm("AUDIT_HISTORY") not in prohibited or _norm(ALL_SCOPES) in restoration or restoration & prohibited:
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — SURFACE NOT BOUNDED")
    if decision_reference_valid is True and _norm(reference.decision_reference) == _norm("NONE"):
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — REFERENCE INVALID")
    if decision_reference_valid is not True:
        return _cd(ControlState.ROLLBACK_PENDING, "ROLLBACK ELIGIBILITY ONLY — DECISION REQUIRED")
    return _cd(ControlState.ROLLBACK_PENDING, "ROLLBACK DECISION RECORDED — EXECUTION NOT AUTHORIZED")


def evaluate_supersession(
    identity: str,
    supersessions: tuple[SupersessionReference, ...],
) -> ControlDetermination:
    """A superseded identity is stale; no fallback to it or from it (design 14)."""
    if (
        not _is_text(identity)
        or type(supersessions) is not tuple
        or any(type(s) is not SupersessionReference for s in supersessions)
        or any(not _is_text(s.superseded_identity) or not _is_text(s.replacement_identity) for s in supersessions)
        or any(s.stale_effect != "BLOCK_CURRENT_USE" or s.history_preservation != "APPEND_ONLY" for s in supersessions)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — STATE CONTRACT FAILURE")
    if any(_norm(s.superseded_identity) == _norm(identity) for s in supersessions):
        return _cd(ControlState.STALE, "STALE — SUPERSEDED IDENTITY; NO FALLBACK")
    return _cd(ControlState.PROTECTED_BLOCKED, "CURRENT IDENTITY — EXECUTION NOT AUTHORIZED")


def audit_record_digest(record: AuditRecordCandidate, previous_digest: str) -> str:
    """SHA-256 over the previous digest and a canonical JSON encoding of every record field."""
    payload = json.dumps(
        {f.name: getattr(record, f.name) for f in fields(record)},
        ensure_ascii=True, sort_keys=True, separators=(",", ":"),
    )
    return hashlib.sha256((previous_digest.upper() + "\n" + payload).encode("ascii")).hexdigest().upper()


def verify_audit_chain(
    records: tuple[AuditRecordCandidate, ...],
    *,
    expected_head_sha256: str,
) -> ControlDetermination:
    """Independent chain check over caller-supplied candidates; nothing is persisted or repaired (design 15)."""
    if (
        type(records) is not tuple
        or not records
        or any(type(r) is not AuditRecordCandidate for r in records)
        or not _is_sha(expected_head_sha256)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — AUDIT CHAIN UNAVAILABLE")
    ids = [r.audit_id for r in records]
    if len(set(ids)) != len(ids):
        return _cd(ControlState.QUARANTINED, "QUARANTINED — INTEGRITY FAILURE")
    previous_id = "NONE"
    head = AUDIT_CHAIN_GENESIS
    for record in records:
        if record.supersedes != previous_id:
            return _cd(ControlState.QUARANTINED, "QUARANTINED — INTEGRITY FAILURE")
        head = audit_record_digest(record, head)
        previous_id = record.audit_id
    if head != expected_head_sha256.upper():
        return _cd(ControlState.QUARANTINED, "QUARANTINED — INTEGRITY FAILURE")
    return _cd(ControlState.PROTECTED_BLOCKED, "AUDIT CHAIN MATCHED — CANDIDATE ONLY; NOT PERSISTED")


def evaluate_dependency(
    requested_dependency: str,
    *,
    authorized_dependencies: tuple[str, ...],
    availability_state: str,
) -> ControlDetermination:
    """Unavailable or unauthorized dependencies block; no substitution or degraded route (design 17, V-013)."""
    if not _is_text(requested_dependency) or type(authorized_dependencies) is not tuple:
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — DEPENDENCY UNBOUND")
    if requested_dependency not in authorized_dependencies:
        return _cd(ControlState.PROTECTED_BLOCKED, "BLOCKED — DEPENDENCY NOT AUTHORIZED")
    if availability_state != "AVAILABLE":
        return _cd(ControlState.PROTECTED_BLOCKED, "BLOCKED — DEPENDENCY OR PROVIDER UNAVAILABLE; NO SUBSTITUTION")
    return _cd(ControlState.PROTECTED_BLOCKED, "DEPENDENCY AVAILABLE — EXECUTION NOT AUTHORIZED")
