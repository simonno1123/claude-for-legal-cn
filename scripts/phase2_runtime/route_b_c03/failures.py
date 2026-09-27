"""Pure protected-state, failure, retry, and release determinations."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .contracts import (
    ControlState,
    FailureRecord,
    InvocationState,
    ReleaseDecisionReference,
    RetryPolicyReference,
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
