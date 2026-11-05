"""Redacted append-only audit candidate construction; no persistence.

All field, identity and redaction checks live in AuditRecordCandidate.__post_init__, so a candidate
cannot be built around them, whether through this function or by constructing the record directly.
"""

from __future__ import annotations

from .contracts import AuditRecordCandidate


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
    return AuditRecordCandidate(
        audit_id, correlation_id, capability_reference, implementation_sha256,
        configuration_sha256, domain_reference, tier_b_packet_reference,
        matter_reference, actor_reference, purpose, operation, prior_state,
        next_state, reason_code, decision_reference, created_at, redaction_state,
        input_artifact_references, supersedes,
    )
