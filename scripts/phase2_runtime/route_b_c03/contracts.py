"""Closed immutable contracts for the capability-only C03 implementation."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import re
from typing import Any

_SHA256 = re.compile(r"^[0-9A-Fa-f]{64}$")


def require_text(value: str, field: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field} must be a non-empty explicit value")


def require_sha256(value: str, field: str, *, allow_none: bool = False) -> None:
    if allow_none and value == "NONE":
        return
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{field} must be a complete SHA-256 value")


class CapabilityState(str, Enum):
    DISABLED = "DISABLED"
    ENABLED_CAPABILITY_ONLY = "ENABLED_CAPABILITY_ONLY"
    REVOKED = "REVOKED"
    STALE = "STALE"


class InvocationState(str, Enum):
    INVOCATION_RECEIVED = "INVOCATION_RECEIVED"
    GATE_CHECKING = "GATE_CHECKING"
    BLOCKED = "BLOCKED"
    REJECTED = "REJECTED"
    ELIGIBLE_FOR_MAPPING = "ELIGIBLE_FOR_MAPPING"
    MAPPING = "MAPPING"
    MAPPING_CANDIDATE = "MAPPING_CANDIDATE"
    QUARANTINED = "QUARANTINED"
    HUMAN_REVIEW_PENDING = "HUMAN_REVIEW_PENDING"


class PacketState(str, Enum):
    ACCEPTED = "ACCEPTED"
    BLOCKED = "BLOCKED"
    WITHDRAWN = "WITHDRAWN"
    STALE = "STALE"
    REVOKED = "REVOKED"


class RevocationState(str, Enum):
    CLEAR = "CLEAR"
    REVOKED = "REVOKED"
    UNKNOWN = "UNKNOWN"


class TransformationType(str, Enum):
    DIRECT_COPY = "DIRECT_COPY"
    ENUMERATION_MAP = "ENUMERATION_MAP"
    FORMAT_NORMALIZATION = "FORMAT_NORMALIZATION"
    EXPLICIT_OMISSION = "EXPLICIT_OMISSION"


class CandidateClass(str, Enum):
    ISSUE_MATRIX = "C03_ISSUE_MATRIX_CANDIDATE"
    ADVERSE_CONDITION_REGISTER = "C03_ADVERSE_CONDITION_REGISTER_CANDIDATE"
    CONFLICT_AND_INFORMATION_GAP_REGISTER = (
        "C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE"
    )
    AUTHORITY_CHECK_REQUEST = "C03_AUTHORITY_CHECK_REQUEST_CANDIDATE"
    QUALIFIED_HUMAN_REVIEW_PACKET = (
        "C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE"
    )


class ControlState(str, Enum):
    CONTROL_DISABLED = "CONTROL_DISABLED"
    PROTECTED_BLOCKED = "PROTECTED_BLOCKED"
    RETRY_ELIGIBILITY_PENDING = "RETRY_ELIGIBILITY_PENDING"
    RETRY_DENIED = "RETRY_DENIED"
    QUARANTINED = "QUARANTINED"
    REVOKED = "REVOKED"
    KILLED = "KILLED"
    ROLLBACK_PENDING = "ROLLBACK_PENDING"
    STALE = "STALE"
    RELEASE_PENDING = "RELEASE_PENDING"
    RELEASED_DISABLED = "RELEASED_DISABLED"


class TamperState(str, Enum):
    UNCHECKED = "UNCHECKED"
    MATCHED = "MATCHED"
    MISMATCH = "MISMATCH"
    UNAVAILABLE = "UNAVAILABLE"


MANDATORY_CANDIDATE_NOTICES = (
    "CANDIDATE — REQUIRES QUALIFIED HUMAN REVIEW",
    "NOT LEGAL ADVICE",
    "NOT AN ENFORCEMENT INSTRUCTION",
    "NOT AUTHORIZED FOR FILING, CONTACT, TRANSFER, OR EXECUTION",
)


@dataclass(frozen=True, slots=True)
class CapabilityConfigurationReference:
    capability_id: str
    capability_version: str
    implementation_sha256: str
    configuration_sha256: str = "NONE"
    activation_decision_reference: str | None = None
    state: CapabilityState = CapabilityState.DISABLED
    revocation_reference: str | None = None
    validity: str = "NON_ACTIVE"

    def __post_init__(self) -> None:
        require_text(self.capability_id, "capability_id")
        require_text(self.capability_version, "capability_version")
        require_sha256(self.implementation_sha256, "implementation_sha256")
        require_sha256(
            self.configuration_sha256, "configuration_sha256", allow_none=True
        )
        if self.state is CapabilityState.ENABLED_CAPABILITY_ONLY:
            require_text(
                self.activation_decision_reference or "",
                "activation_decision_reference",
            )
        if self.state is CapabilityState.REVOKED:
            require_text(self.revocation_reference or "", "revocation_reference")


@dataclass(frozen=True, slots=True)
class ExpectedIdentityReference:
    capability_id: str
    capability_version: str
    implementation_sha256: str
    configuration_sha256: str
    activation_decision_reference: str
    route: str
    route_version: str
    domain_id: str
    domain_version: str
    adapter_contract_version: str
    matter_authorization_reference: str
    execution_authorization_reference: str

    def __post_init__(self) -> None:
        require_sha256(self.implementation_sha256, "implementation_sha256")
        require_sha256(
            self.configuration_sha256, "configuration_sha256", allow_none=True
        )
        for field in (
            "capability_id", "capability_version",
            "activation_decision_reference", "route", "route_version",
            "domain_id", "domain_version", "adapter_contract_version",
            "matter_authorization_reference", "execution_authorization_reference",
        ):
            require_text(getattr(self, field), field)


@dataclass(frozen=True, slots=True)
class TierBAuthorityPacketReference:
    packet_id: str
    packet_version: str
    packet_sha256: str
    matter_id: str
    matter_version: str
    actor_reference: str
    purpose: str
    operation: str
    input_set_sha256: str
    output_class: CandidateClass
    decision_reference: str
    valid_from: str
    valid_until: str
    revocation_state: RevocationState
    state: PacketState

    def __post_init__(self) -> None:
        for field in (
            "packet_id", "packet_version", "matter_id", "matter_version",
            "actor_reference", "purpose", "operation", "decision_reference",
            "valid_from", "valid_until",
        ):
            require_text(getattr(self, field), field)
        require_sha256(self.packet_sha256, "packet_sha256")
        require_sha256(self.input_set_sha256, "input_set_sha256")


@dataclass(frozen=True, slots=True)
class ArtifactReference:
    artifact_id: str
    artifact_type: str
    version: str
    sha256: str
    source_reference: str
    readiness_state: str
    validation_state: str
    human_review_reference: str

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "artifact sha256")
        for field in (
            "artifact_id", "artifact_type", "version", "source_reference",
            "readiness_state", "validation_state", "human_review_reference",
        ):
            require_text(getattr(self, field), field)


@dataclass(frozen=True, slots=True)
class GovernedInputEnvelopeReference:
    envelope_id: str
    route: str
    route_version: str
    domain_id: str
    domain_version: str
    adapter_contract_version: str
    matter_id: str
    matter_version: str
    matter_authorization_reference: str
    actor_reference: str
    role: str
    authority_reference: str
    purpose: str
    operation: str
    input_set_sha256: str
    requested_output_scope: tuple[CandidateClass, ...]
    prohibited_output_scope: tuple[str, ...]
    execution_authorization_reference: str
    audit_correlation_id: str
    input_artifact_references: tuple[ArtifactReference, ...] = ()

    def __post_init__(self) -> None:
        require_sha256(self.input_set_sha256, "input_set_sha256")
        for field in (
            "envelope_id", "route", "route_version", "domain_id",
            "domain_version", "adapter_contract_version", "matter_id",
            "matter_version", "matter_authorization_reference",
            "actor_reference", "role", "authority_reference", "purpose",
            "operation", "execution_authorization_reference",
            "audit_correlation_id",
        ):
            require_text(getattr(self, field), field)


@dataclass(frozen=True, slots=True)
class MappingRule:
    rule_id: str
    source_path: str
    target_path: str
    transformation_type: TransformationType
    allowed_source_states: tuple[str, ...]
    null_policy: str
    conflict_policy: str
    provenance_required: bool = True
    human_review_required: bool = True
    enumeration_version: str | None = None
    enumeration_pairs: tuple[tuple[Any, Any], ...] = ()
    normalization_version: str | None = None
    normalization_pairs: tuple[tuple[Any, Any], ...] = ()
    omission_reason: str | None = None


@dataclass(frozen=True, slots=True)
class MappingTrace:
    rule_id: str
    transformation_type: TransformationType
    source_path: str
    target_path: str
    source_artifact_reference: str
    source_version: str
    original_representation: str
    resulting_representation: str
    authorization_reference: str


@dataclass(frozen=True, slots=True)
class GateDecision:
    state: InvocationState
    reason_code: str
    audit_correlation_id: str
    permitted_write_namespaces: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class RecoveryContextReference:
    control_context_id: str
    capability_reference: str
    implementation_sha256: str
    configuration_sha256: str
    invocation_id: str
    tier_b_packet_reference: str
    matter_reference: str
    actor_reference: str
    purpose: str
    operation: str
    output_class: CandidateClass
    prior_state: str
    expected_next_state: str
    revocation_state: RevocationState
    kill_state: str
    stale_state: str
    audit_correlation_id: str


@dataclass(frozen=True, slots=True)
class RetryPolicyReference:
    policy_id: str
    version: str
    sha256: str
    eligible_failure_codes: tuple[str, ...] = ()
    maximum_attempts: int = 0
    backoff_policy_reference: str = "NONE"
    deadline_reference: str = "NONE"
    scope_lock_sha256: str = "NONE"
    terminal_codes: tuple[str, ...] = ()
    authorization_reference: str = "NONE"

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "retry policy sha256")
        require_sha256(self.scope_lock_sha256, "scope_lock_sha256", allow_none=True)
        if self.maximum_attempts < 0:
            raise ValueError("maximum_attempts cannot be negative")


@dataclass(frozen=True, slots=True)
class IdempotencyKeyReference:
    canonicalization_version: str
    digest_algorithm: str
    key_sha256: str
    replay_window_reference: str

    def __post_init__(self) -> None:
        require_sha256(self.key_sha256, "idempotency key sha256")


@dataclass(frozen=True, slots=True)
class TimeoutPolicyReference:
    policy_id: str
    version: str
    sha256: str
    start_category: str
    deadline_duration: str
    late_result_policy: str = "DENY_USE"
    terminal_state: ControlState = ControlState.QUARANTINED
    retry_effect: str = "NONE"

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "timeout policy sha256")
        for field in (
            "policy_id", "version", "start_category", "deadline_duration",
            "late_result_policy", "retry_effect",
        ):
            require_text(getattr(self, field), field)


@dataclass(frozen=True, slots=True)
class QuarantineReference:
    quarantine_id: str
    version: str
    subject_reference: str
    reason_code: str
    entry_state: str
    scope: str
    redaction_state: str
    resolution_evidence_reference: str = "NONE"
    release_decision_reference: str = "NONE"
    state: str = "ACTIVE"


@dataclass(frozen=True, slots=True)
class RevocationOrKillReference:
    control_id: str
    version: str
    sha256: str
    trigger_reference: str
    authority_reference: str
    effective_state: ControlState
    affected_scope: str
    propagation_boundary: str
    response_target: str
    release_authority_required: bool = True

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "revocation/kill sha256")
        for field in (
            "control_id", "version", "trigger_reference", "authority_reference",
            "affected_scope", "propagation_boundary", "response_target",
        ):
            require_text(getattr(self, field), field)
        if self.effective_state not in (ControlState.REVOKED, ControlState.KILLED):
            raise ValueError("effective_state must be REVOKED or KILLED")
        if not self.release_authority_required:
            raise ValueError("release authority is mandatory")


@dataclass(frozen=True, slots=True)
class RollbackReference:
    rollback_id: str
    version: str
    current_identity: str
    target_identity: str
    restoration_surface: tuple[str, ...]
    preconditions: tuple[str, ...]
    prohibited_surface: tuple[str, ...]
    decision_reference: str
    post_restore_state: CapabilityState = CapabilityState.DISABLED


@dataclass(frozen=True, slots=True)
class SupersessionReference:
    supersession_id: str
    superseded_identity: str
    replacement_identity: str
    reason_reference: str
    stale_effect: str = "BLOCK_CURRENT_USE"
    history_preservation: str = "APPEND_ONLY"


@dataclass(frozen=True, slots=True)
class AuditIntegrityReference:
    policy_id: str
    version: str
    sha256: str
    chain_reference: str
    subject_hashes: tuple[str, ...]
    redaction_state: str
    tamper_state: TamperState = TamperState.UNCHECKED
    retention_reference: str = "NONE"
    access_reference: str = "NONE"
    supersedes: str = "NONE"

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "audit integrity sha256")
        for subject_sha in self.subject_hashes:
            require_sha256(subject_sha, "subject hash")
        for field in ("policy_id", "version", "chain_reference", "redaction_state"):
            require_text(getattr(self, field), field)


@dataclass(frozen=True, slots=True)
class ReleaseDecisionReference:
    decision_id: str
    version: str
    sha256: str
    protected_state_reference: str
    resolution_evidence_reference: str
    permitted_release_scope: str
    remaining_limitations: tuple[str, ...]
    validity: str
    next_state: ControlState = ControlState.RELEASED_DISABLED

    def __post_init__(self) -> None:
        require_sha256(self.sha256, "release decision sha256")
        for field in (
            "decision_id", "version", "protected_state_reference",
            "resolution_evidence_reference", "permitted_release_scope", "validity",
        ):
            require_text(getattr(self, field), field)
        if self.next_state is not ControlState.RELEASED_DISABLED:
            raise ValueError("release may return only to RELEASED_DISABLED")


@dataclass(frozen=True, slots=True)
class CandidateRecord:
    candidate_id: str
    candidate_version: str
    candidate_sha256: str
    candidate_class: CandidateClass
    capability_reference: str
    matter_reference: str
    purpose: str
    operation: str
    input_set_sha256: str
    mapping_trace_references: tuple[str, ...]
    notices: tuple[str, ...] = MANDATORY_CANDIDATE_NOTICES
    state: InvocationState = InvocationState.HUMAN_REVIEW_PENDING
    downstream_blocked: bool = True

    def __post_init__(self) -> None:
        require_sha256(self.candidate_sha256, "candidate_sha256")
        require_sha256(self.input_set_sha256, "input_set_sha256")
        for field in (
            "candidate_id", "candidate_version", "capability_reference",
            "matter_reference", "purpose", "operation",
        ):
            require_text(getattr(self, field), field)
        if self.notices != MANDATORY_CANDIDATE_NOTICES:
            raise ValueError("mandatory candidate notices must remain exact")
        if self.state is not InvocationState.HUMAN_REVIEW_PENDING:
            raise ValueError("candidate must remain HUMAN_REVIEW_PENDING")
        if not self.downstream_blocked:
            raise ValueError("candidate must remain downstream blocked")


@dataclass(frozen=True, slots=True)
class FailureRecord:
    failure_id: str
    reason_code: str
    invocation_state: InvocationState
    control_state: ControlState
    audit_correlation_id: str
    automatic_retry: bool = False
    upstream_write_namespaces: tuple[str, ...] = ()


@dataclass(frozen=True, slots=True)
class AuditRecordCandidate:
    audit_id: str
    correlation_id: str
    capability_reference: str
    implementation_sha256: str
    configuration_sha256: str
    domain_reference: str
    tier_b_packet_reference: str
    matter_reference: str
    actor_reference: str
    purpose: str
    operation: str
    prior_state: str
    next_state: str
    reason_code: str
    decision_reference: str
    created_at: str
    redaction_state: str
    input_artifact_references: tuple[str, ...] = ()
    supersedes: str = "NONE"
