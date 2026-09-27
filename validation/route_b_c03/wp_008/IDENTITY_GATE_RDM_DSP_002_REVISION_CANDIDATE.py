"""Pure metadata identity and authority gate; never opens referenced assets."""

from __future__ import annotations

from .contracts import (
    CapabilityConfigurationReference,
    CapabilityState,
    ExpectedIdentityReference,
    GateDecision,
    GovernedInputEnvelopeReference,
    InvocationState,
    PacketState,
    RevocationState,
    TierBAuthorityPacketReference,
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
) -> GateDecision:
    """Evaluate explicit metadata only and return a closed gate decision."""
    correlation = envelope.audit_correlation_id
    if kill_active:
        return _decision(InvocationState.BLOCKED, "BLOCKED — KILL ACTIVE", correlation)
    if configuration is None or configuration.state is CapabilityState.DISABLED:
        return _decision(
            InvocationState.BLOCKED,
            "BLOCKED — CAPABILITY NOT ACTIVE",
            correlation,
        )
    if configuration.state is CapabilityState.REVOKED:
        return _decision(InvocationState.BLOCKED, "BLOCKED — AUTHORITY FAILURE", correlation)
    if configuration.state is CapabilityState.STALE:
        return _decision(InvocationState.BLOCKED, "BLOCKED — VERSION FAILURE", correlation)
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
    if packet.revocation_state is not RevocationState.CLEAR or not validity_confirmed:
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
    return _decision(
        InvocationState.ELIGIBLE_FOR_MAPPING,
        "ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED",
        correlation,
    )
