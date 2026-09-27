"""Closed C03 facade. Default construction is disabled and side-effect free."""

from __future__ import annotations

from dataclasses import dataclass, field

from .contracts import (
    CapabilityConfigurationReference,
    ExpectedIdentityReference,
    GateDecision,
    GovernedInputEnvelopeReference,
    InvocationState,
    TierBAuthorityPacketReference,
)
from .identity_gate import evaluate_identity_gate
from .provider_port import NullProviderPort, ProviderPortResult


@dataclass(frozen=True, slots=True)
class C03Capability:
    configuration: CapabilityConfigurationReference | None = None
    provider: NullProviderPort = field(
        default_factory=NullProviderPort,
        init=False,
        repr=False,
    )

    @property
    def is_active(self) -> bool:
        return False if self.configuration is None else (
            self.configuration.state.value == "ENABLED_CAPABILITY_ONLY"
        )

    def evaluate_gate(
        self,
        envelope: GovernedInputEnvelopeReference,
        packet: TierBAuthorityPacketReference | None = None,
        *,
        expected_identity: ExpectedIdentityReference,
        validity_confirmed: bool = False,
        kill_active: bool = False,
    ) -> GateDecision:
        return evaluate_identity_gate(
            self.configuration,
            packet,
            envelope,
            expected=expected_identity,
            validity_confirmed=validity_confirmed,
            kill_active=kill_active,
        )

    def submit_provider_reference(self, request_reference: str) -> ProviderPortResult:
        """Always blocked for the authorized null-provider materialization."""
        return self.provider.submit_reference(request_reference)

    def mapping_execution_state(self) -> GateDecision:
        """Expose the current materialization boundary without executing mapping."""
        return GateDecision(
            InvocationState.BLOCKED,
            "BLOCKED — MATTER INVOCATION AUTHORITY REQUIRED",
            "NONE",
            (),
        )
