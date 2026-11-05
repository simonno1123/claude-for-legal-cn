"""Pure metadata identity and authority gate; never opens referenced assets."""

from __future__ import annotations

from .contracts import (
    ARTIFACT_READY,
    ARTIFACT_VALIDATED,
    CapabilityConfigurationReference,
    CapabilityState,
    ExpectedIdentityReference,
    GateDecision,
    GovernedInputEnvelopeReference,
    InvocationState,
    PacketState,
    RevocationState,
    TierBAuthorityPacketReference,
    is_utc_timestamp,
)


def _decision(state: InvocationState, reason: str, correlation: str) -> GateDecision:
    return GateDecision(state, reason, correlation, ())


def evaluate_identity_gate(
    configuration: CapabilityConfigurationReference | None,
    packet: TierBAuthorityPacketReference | None,
    envelope: GovernedInputEnvelopeReference,
    *,
    expected: ExpectedIdentityReference,
    validity_confirmed: bool,
    kill_active: bool,
    evaluated_at: str,
) -> GateDecision:
    """Evaluate explicit metadata only and return a closed gate decision.

    Every check is an allow-list: only a kill flag that is exactly False, an exact
    ENABLED_CAPABILITY_ONLY member, an exact ACCEPTED/CLEAR packet inside its validity window and
    ready, validated artifact references can reach ELIGIBLE_FOR_MAPPING.
    """
    correlation = envelope.audit_correlation_id
    if kill_active is not False:
        return _decision(InvocationState.BLOCKED, "BLOCKED — KILL ACTIVE", correlation)
    if configuration is None or type(configuration.state) is not CapabilityState:
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — CAPABILITY NOT ACTIVE",
            correlation,
        )
    if configuration.state is CapabilityState.REVOKED:
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY FAILURE", correlation)
    if configuration.state is CapabilityState.STALE:
        return _decision(InvocationState.BLOCKED, "BLOCKED — VERSION FAILURE", correlation)
    if configuration.state is not CapabilityState.ENABLED_CAPABILITY_ONLY:
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — CAPABILITY NOT ACTIVE",
            correlation,
        )
    if (
        configuration.capability_id != expected.capability_id
        or configuration.capability_version != expected.capability_version
        or configuration.implementation_sha256 != expected.implementation_sha256
        or configuration.configuration_sha256 != expected.configuration_sha256
        or configuration.activation_decision_reference
        != expected.activation_decision_reference
    ):
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — CAPABILITY IDENTITY FAILURE",
            correlation,
        )
    if (
        envelope.route != expected.route
        or envelope.route_version != expected.route_version
        or envelope.domain_id != expected.domain_id
        or envelope.domain_version != expected.domain_version
        or envelope.adapter_contract_version != expected.adapter_contract_version
    ):
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — DOMAIN IDENTITY FAILURE",
            correlation,
        )
    if packet is None:
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — TIER B AUTHORITY REQUIRED",
            correlation,
        )
    if packet.state is not PacketState.ACCEPTED:
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY FAILURE", correlation)
    if packet.revocation_state is not RevocationState.CLEAR or validity_confirmed is not True:
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY FAILURE", correlation)
    if not (
        is_utc_timestamp(evaluated_at)
        and is_utc_timestamp(packet.valid_from)
        and is_utc_timestamp(packet.valid_until)
        and packet.valid_from <= evaluated_at < packet.valid_until
    ):
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY FAILURE", correlation)
    if (
        packet.matter_id != envelope.matter_id
        or packet.matter_version != envelope.matter_version
        or packet.actor_reference != envelope.actor_reference
    ):
        return _decision(InvocationState.REJECTED, "REJECTED — ISOLATION FAILURE", correlation)
    if packet.purpose != envelope.purpose or packet.operation != envelope.operation:
        return _decision(InvocationState.REJECTED, "REJECTED — SCOPE FAILURE", correlation)
    if packet.input_set_sha256 != envelope.input_set_sha256:
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — INPUT SET IDENTITY FAILURE",
            correlation,
        )
    if packet.output_class not in envelope.requested_output_scope:
        return _decision(InvocationState.REJECTED, "REJECTED — OUTPUT BOUNDARY FAILURE", correlation)
    if (
        envelope.matter_authorization_reference
        != expected.matter_authorization_reference
        or envelope.execution_authorization_reference
        != expected.execution_authorization_reference
        or packet.decision_reference != expected.execution_authorization_reference
    ):
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY BINDING FAILURE", correlation)
    if not envelope.input_artifact_references or any(
        artifact.readiness_state != ARTIFACT_READY
        or artifact.validation_state != ARTIFACT_VALIDATED
        for artifact in envelope.input_artifact_references
    ):
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — READINESS/PROVENANCE FAILURE",
            correlation,
        )
    return _decision(
        InvocationState.ELIGIBLE_FOR_MAPPING,
        "ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED",
        correlation,
    )
