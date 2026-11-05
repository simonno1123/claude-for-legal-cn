"""Closed C03 facade. Default construction is disabled and side-effect free."""

from __future__ import annotations

from dataclasses import dataclass, field

from .contracts import (
    CapabilityConfigurationReference,
    CapabilityState,
    ExpectedIdentityReference,
    GateDecision,
    GovernedInputEnvelopeReference,
    InvocationState,
    RevocationOrKillReference,
    TierBAuthorityPacketReference,
)
from .failures import ControlDetermination, evaluate_control_precedence
from .identity_gate import evaluate_identity_gate
from .provider_port import NullProviderPort, ProviderPortResult

NO_ACTIVE_CONTROL = "PROTECTED_BLOCKED — NO ACTIVE CONTROL; EXECUTION NOT AUTHORIZED"


@dataclass(frozen=True, slots=True)
class TransitionDetermination:
    """Result of the pre-transition check: controls first, then the identity gate (V7)."""

    control: ControlDetermination
    gate: GateDecision | None
    state: InvocationState
    reason_code: str
    execution_authorized: bool = False

    def __post_init__(self) -> None:
        if self.execution_authorized is not False:
            raise ValueError("a transition determination never authorizes execution")
        if type(self.control) is not ControlDetermination or type(self.state) is not InvocationState:
            raise ValueError("control and state must be exact contract types")
        if self.gate is None:
            if self.state is not InvocationState.BLOCKED or self.reason_code != self.control.reason_code:
                raise ValueError("without a gate decision the transition is BLOCKED by the control")
        elif (
            type(self.gate) is not GateDecision
            or self.control.reason_code != NO_ACTIVE_CONTROL
            or self.state is not self.gate.state
            or self.reason_code != self.gate.reason_code
        ):
            raise ValueError("a gate decision is reported only when no control is active, and unchanged")


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
        return self.configuration is not None and (
            self.configuration.state is CapabilityState.ENABLED_CAPABILITY_ONLY
        )

    def evaluate_gate(
        self,
        envelope: GovernedInputEnvelopeReference,
        packet: TierBAuthorityPacketReference | None = None,
        *,
        expected_identity: ExpectedIdentityReference,
        validity_confirmed: bool,
        kill_active: bool,
        evaluated_at: str,
    ) -> GateDecision:
        """The kill state, validity confirmation and evaluation time have no defaults."""
        return evaluate_identity_gate(
            self.configuration,
            packet,
            envelope,
            expected=expected_identity,
            validity_confirmed=validity_confirmed,
            kill_active=kill_active,
            evaluated_at=evaluated_at,
        )

    def evaluate_transition(
        self,
        envelope: GovernedInputEnvelopeReference,
        packet: TierBAuthorityPacketReference | None = None,
        *,
        expected_identity: ExpectedIdentityReference,
        validity_confirmed: bool,
        evaluated_at: str,
        kill: RevocationOrKillReference | None,
        revocation: RevocationOrKillReference | None,
        control_state_known: bool,
        subject_scope: str,
    ) -> TransitionDetermination:
        """The check required before every significant transition (WP-009 design): kill, then revocation, then
        unknown control state, are decided first; only with no active control is the identity gate evaluated.
        Neither path executes anything."""
        control = evaluate_control_precedence(
            kill=kill,
            revocation=revocation,
            control_state_known=control_state_known,
            subject_scope=subject_scope,
        )
        if control.reason_code != NO_ACTIVE_CONTROL:
            return TransitionDetermination(control, None, InvocationState.BLOCKED, control.reason_code)
        gate = self.evaluate_gate(
            envelope,
            packet,
            expected_identity=expected_identity,
            validity_confirmed=validity_confirmed,
            kill_active=False,
            evaluated_at=evaluated_at,
        )
        return TransitionDetermination(control, gate, gate.state, gate.reason_code)

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
