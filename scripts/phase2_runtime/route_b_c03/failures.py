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
        if ref.affected_scope in (subject_scope, ALL_SCOPES):
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
    """Timeout and late-result determination over caller-supplied times; no clock is read (design 11)."""
    if (
        type(policy) is not TimeoutPolicyReference
        or policy.terminal_state is not ControlState.QUARANTINED
        or policy.late_result_policy != "DENY_USE"
        or policy.retry_effect != "NONE"
        or not (is_utc_timestamp(started_at) and is_utc_timestamp(deadline_at) and is_utc_timestamp(observed_at))
        or not started_at < deadline_at
        or not started_at <= observed_at
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — TIMEOUT POLICY UNBOUND")
    if result_received_at is not None:
        if not is_utc_timestamp(result_received_at) or not started_at <= result_received_at <= observed_at:
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
    """Rollback eligibility only; never restores (design 14)."""
    if kill_active is not False:
        return _cd(ControlState.KILLED, "BLOCKED — KILL ACTIVE")
    if revoked is not False:
        return _cd(ControlState.REVOKED, "BLOCKED — REVOKED")
    if (
        type(reference) is not RollbackReference
        or type(accepted_prior_identities) is not tuple
        or type(reference.restoration_surface) is not tuple
        or type(reference.prohibited_surface) is not tuple
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — REFERENCE INVALID")
    if reference.post_restore_state is not CapabilityState.DISABLED:
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — RESTORE MUST RETURN TO DISABLED")
    if reference.target_identity == reference.current_identity or reference.target_identity not in accepted_prior_identities:
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — TARGET NOT AN ACCEPTED PRIOR VERSION")
    if (
        not reference.restoration_surface
        or "AUDIT_HISTORY" not in reference.prohibited_surface
        or set(reference.restoration_surface) & set(reference.prohibited_surface)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "ROLLBACK BLOCKED — SURFACE NOT BOUNDED")
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
        or any(s.stale_effect != "BLOCK_CURRENT_USE" or s.history_preservation != "APPEND_ONLY" for s in supersessions)
    ):
        return _cd(ControlState.PROTECTED_BLOCKED, "PROTECTED_BLOCKED — STATE CONTRACT FAILURE")
    if any(s.superseded_identity == identity for s in supersessions):
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
