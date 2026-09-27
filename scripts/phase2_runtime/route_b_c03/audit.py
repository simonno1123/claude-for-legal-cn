"""Redacted append-only audit candidate construction; no persistence."""

from __future__ import annotations

from .contracts import AuditRecordCandidate, require_sha256, require_text

_PROHIBITED_MARKERS = (
    "password",
    "secret",
    "token",
    "cookie",
    "authorization:",
    "bearer ",
    "private key",
    "prompt content",
    "attachment content",
    "raw payload",
)


def _assert_redacted(values: tuple[str, ...]) -> None:
    for value in values:
        lowered = value.lower()
        if any(marker in lowered for marker in _PROHIBITED_MARKERS):
            raise ValueError("QUARANTINED — AUDIT REDACTION FAILURE")


def build_audit_candidate(
    *,
    audit_id: str,
    correlation_id: str,
    capability_reference: str,
    implementation_sha256: str,
    configuration_sha256: str,
    domain_reference: str,
    tier_b_packet_reference: str,
    matter_reference: str,
    actor_reference: str,
    purpose: str,
    operation: str,
    prior_state: str,
    next_state: str,
    reason_code: str,
    decision_reference: str,
    created_at: str,
    redaction_state: str,
    input_artifact_references: tuple[str, ...] = (),
    supersedes: str = "NONE",
) -> AuditRecordCandidate:
    """Build an immutable candidate from explicit caller-supplied metadata."""
    require_sha256(implementation_sha256, "implementation_sha256")
    require_sha256(configuration_sha256, "configuration_sha256", allow_none=True)
    for name, value in (
        ("audit_id", audit_id), ("correlation_id", correlation_id),
        ("capability_reference", capability_reference),
        ("domain_reference", domain_reference),
        ("reason_code", reason_code), ("created_at", created_at),
        ("redaction_state", redaction_state),
    ):
        require_text(value, name)
    _assert_redacted(
        (
            audit_id, correlation_id, capability_reference, domain_reference,
            tier_b_packet_reference, matter_reference, actor_reference, purpose,
            operation, prior_state, next_state, reason_code, decision_reference,
            created_at, redaction_state, *input_artifact_references, supersedes,
        )
    )
    return AuditRecordCandidate(
        audit_id, correlation_id, capability_reference, implementation_sha256,
        configuration_sha256, domain_reference, tier_b_packet_reference,
        matter_reference, actor_reference, purpose, operation, prior_state,
        next_state, reason_code, decision_reference, created_at, redaction_state,
        input_artifact_references, supersedes,
    )
