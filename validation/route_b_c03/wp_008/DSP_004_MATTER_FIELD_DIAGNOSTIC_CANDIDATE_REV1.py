"""DSP-004 matter-field diagnostic candidate, REV1; synthetic metadata only.

Loading identity: DSP_004_MATTER_FIELD_DIAGNOSTIC_CANDIDATE_REV1.
The five diagnostic classes are independent candidate classes, not additions
to route_b_c03.contracts, context BoundaryCheck classes, or integrated types.
This source implements the conversation-only adopted matter diagnostic REV1;
its materialization/tests do not accept this candidate or admit any source.

Preparation design record SHA-256:
DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4
Existing contracts.py SHA-256:
7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4
Existing identity_gate.py SHA-256 (read-only reference; never executed here):
9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445
Accepted denial-preserver candidate SHA-256:
61D424C35D262C3CC9FE03863F4BCB4D39FF96E248E5A7A08B8EAE6F8D598245

Hash binding belongs to the controlled loader, not this pure module. Inputs
are caller-supplied synthetic metadata. An isolation reason restricts scope;
it does not establish the failing field, prior gate execution, trusted inputs,
or same-call origin. Equal correlation strings do not prove one call. Neither
native class identity nor these selected-field checks validate the complete
packet/envelope, authority, their construction provenance, or source admission.

MATCH/MISMATCH below mean literal supplied-value comparison only. Missing or
invalid fields yield NOT_EVALUATED with both display values absent; they are
not repaired, stringified, or treated as mismatch. Inputs stay unchanged.
If upstream objects cannot be constructed, upstream must stop separately as
CONSTRUCTION_FAILURE; partial synthetic diagnostics are not a substitute for
valid inputs, context observations, or a newly constructed GateDecision.

All three MATCH with the supplied isolation rejection is an input relationship
contradiction: the diagnostic exposes those values and preserves the rejection,
but does not attribute its cause, clear it, or open further checks. Actor-only
mismatch is not matter ID/version mismatch. Any NOT_EVALUATED prevents complete
attribution. Even a complete matter mismatch remains candidate value evidence,
not trusted boundary evidence or authorization for supplementary observations.

No sources/files are read, gate invoked, actuals captured, context checks
created, fixture mapped, or routing/permission verdict issued. Original result
identity and all four fields stay intact. Empty write metadata does not prove
zero I/O, real isolation, no disclosure, formal validation, or integration.
"""

from dataclasses import dataclass
from enum import Enum, unique

from route_b_c03.contracts import (
    GateDecision,
    GovernedInputEnvelopeReference,
    InvocationState,
    TierBAuthorityPacketReference,
)
from DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1 import preserve_denied_decision


@unique
class MatterFieldKind(Enum):
    MATTER_ID = "MATTER_ID"
    MATTER_VERSION = "MATTER_VERSION"
    ACTOR_REFERENCE = "ACTOR_REFERENCE"


@unique
class MatterFieldState(Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    NOT_EVALUATED = "NOT_EVALUATED"


@unique
class MatterFieldCause(Enum):
    EXACT_EQUAL = "EXACT_EQUAL"
    EXACT_UNEQUAL = "EXACT_UNEQUAL"
    FIELD_UNAVAILABLE = "FIELD_UNAVAILABLE"
    INVALID_REFERENCE_TYPE = "INVALID_REFERENCE_TYPE"


@dataclass(frozen=True, slots=True)
class MatterFieldCheck:
    field_kind: MatterFieldKind
    state: MatterFieldState
    cause: MatterFieldCause
    packet_reference: str | None
    envelope_reference: str | None
    audit_correlation_id: str

    def __post_init__(self) -> None:
        _validate_field_check(self)


@dataclass(frozen=True, slots=True)
class MatterFieldDiagnostic:
    prior_decision: GateDecision
    checks: tuple[MatterFieldCheck, ...]

    def __post_init__(self) -> None:
        _validate_diagnostic(self)


_MISSING = object()
_FIELD_ORDER = (
    MatterFieldKind.MATTER_ID,
    MatterFieldKind.MATTER_VERSION,
    MatterFieldKind.ACTOR_REFERENCE,
)


def _require_native_text(value: str, field: str) -> None:
    if type(value) is not str:
        raise TypeError(f"{field} requires native str")
    if not value or value.isspace():
        raise ValueError(f"{field} requires nonempty, non-whitespace text")


def _require_isolation_prior(prior: GateDecision) -> None:
    preserve_denied_decision(prior)
    if prior.state is not InvocationState.REJECTED:
        raise ValueError("only native REJECTED isolation input is in scope")
    if prior.reason_code != "REJECTED — ISOLATION FAILURE":
        raise ValueError("complete isolation reason required; no attribution inferred")


def _validate_field_check(check: MatterFieldCheck) -> None:
    if type(check) is not MatterFieldCheck:
        raise TypeError("check requires this independent candidate's MatterFieldCheck")
    try:
        kind = check.field_kind
        state = check.state
        cause = check.cause
        packet_value = check.packet_reference
        envelope_value = check.envelope_reference
        correlation = check.audit_correlation_id
    except AttributeError as error:
        raise ValueError("check requires all six initialized fields") from error
    if type(kind) is not MatterFieldKind:
        raise TypeError("field_kind requires candidate MatterFieldKind")
    if type(state) is not MatterFieldState:
        raise TypeError("state requires candidate MatterFieldState")
    if type(cause) is not MatterFieldCause:
        raise TypeError("cause requires candidate MatterFieldCause")
    _require_native_text(correlation, "check.audit_correlation_id")
    if state is MatterFieldState.NOT_EVALUATED:
        if cause not in (MatterFieldCause.FIELD_UNAVAILABLE, MatterFieldCause.INVALID_REFERENCE_TYPE):
            raise ValueError("NOT_EVALUATED requires an unavailable/invalid field cause")
        if packet_value is not None or envelope_value is not None:
            raise ValueError("NOT_EVALUATED must omit both display values")
        return
    _require_native_text(packet_value, "check.packet_reference")
    _require_native_text(envelope_value, "check.envelope_reference")
    if state is MatterFieldState.MATCH:
        if cause is not MatterFieldCause.EXACT_EQUAL or packet_value != envelope_value:
            raise ValueError("MATCH requires EXACT_EQUAL and literally equal supplied values")
    elif cause is not MatterFieldCause.EXACT_UNEQUAL or packet_value == envelope_value:
        raise ValueError("MISMATCH requires EXACT_UNEQUAL and literally unequal supplied values")


def _validate_diagnostic(diagnostic: MatterFieldDiagnostic) -> None:
    if type(diagnostic) is not MatterFieldDiagnostic:
        raise TypeError("diagnostic requires this independent candidate's native class")
    try:
        prior = diagnostic.prior_decision
        checks = diagnostic.checks
    except AttributeError as error:
        raise ValueError("diagnostic requires both initialized fields") from error
    _require_isolation_prior(prior)
    if type(checks) is not tuple:
        raise TypeError("checks requires native tuple, not JSON/list or a subclass")
    if len(checks) != 3:
        raise ValueError("checks requires exactly three independent field records")
    for position, check in enumerate(checks):
        _validate_field_check(check)
        if check.field_kind is not _FIELD_ORDER[position]:
            raise ValueError("field order must be matter ID, version, actor")
        if check.audit_correlation_id != prior.audit_correlation_id:
            raise ValueError("correlation conflict; equality would still not prove one call")


def _diagnose_field(
    kind: MatterFieldKind,
    attribute: str,
    packet: TierBAuthorityPacketReference,
    envelope: GovernedInputEnvelopeReference,
    correlation: str,
) -> MatterFieldCheck:
    if type(kind) is not MatterFieldKind or type(attribute) is not str:
        raise TypeError("field selection requires candidate kind and native attribute text")
    if (kind, attribute) not in (
        (MatterFieldKind.MATTER_ID, "matter_id"),
        (MatterFieldKind.MATTER_VERSION, "matter_version"),
        (MatterFieldKind.ACTOR_REFERENCE, "actor_reference"),
    ):
        raise ValueError("field selection must be one of the three exact kind/attribute pairs")
    if (type(packet) is not TierBAuthorityPacketReference
            or type(envelope) is not GovernedInputEnvelopeReference):
        raise TypeError("selected-field checks require the existing native input classes")
    _require_native_text(correlation, "selected-field correlation")
    packet_value = getattr(packet, attribute, _MISSING)
    envelope_value = getattr(envelope, attribute, _MISSING)
    if packet_value is _MISSING or envelope_value is _MISSING:
        return MatterFieldCheck(kind, MatterFieldState.NOT_EVALUATED,
                                MatterFieldCause.FIELD_UNAVAILABLE, None, None, correlation)
    if (type(packet_value) is not str or type(envelope_value) is not str
            or not packet_value or packet_value.isspace()
            or not envelope_value or envelope_value.isspace()):
        return MatterFieldCheck(kind, MatterFieldState.NOT_EVALUATED,
                                MatterFieldCause.INVALID_REFERENCE_TYPE, None, None, correlation)
    if packet_value == envelope_value:
        return MatterFieldCheck(kind, MatterFieldState.MATCH, MatterFieldCause.EXACT_EQUAL,
                                packet_value, envelope_value, correlation)
    return MatterFieldCheck(kind, MatterFieldState.MISMATCH, MatterFieldCause.EXACT_UNEQUAL,
                            packet_value, envelope_value, correlation)


def diagnose_matter_fields(
    prior: GateDecision,
    packet: TierBAuthorityPacketReference,
    envelope: GovernedInputEnvelopeReference,
) -> MatterFieldDiagnostic:
    """Inspect supplied synthetic field values without attributing a real gate failure.

    Partial/malformed field data is diagnostic metadata only, never evidence of
    valid upstream construction. The caller must not use this function to bypass
    CONSTRUCTION_FAILURE, source controls, or the retained rejection. A returned
    record has no aggregate matter verdict, eligibility flag, or routing action.
    """
    _require_isolation_prior(prior)
    if type(packet) is not TierBAuthorityPacketReference:
        raise TypeError("packet requires the existing native authority-packet class")
    if type(envelope) is not GovernedInputEnvelopeReference:
        raise TypeError("envelope requires the existing native input-envelope class")
    try:
        correlation = envelope.audit_correlation_id
    except AttributeError as error:
        raise ValueError("envelope requires an initialized correlation") from error
    _require_native_text(correlation, "envelope.audit_correlation_id")
    if correlation != prior.audit_correlation_id:
        raise ValueError("prior/envelope correlation conflict; no same-call proof inferred")
    checks = (
        _diagnose_field(MatterFieldKind.MATTER_ID, "matter_id", packet, envelope, correlation),
        _diagnose_field(MatterFieldKind.MATTER_VERSION, "matter_version", packet, envelope, correlation),
        _diagnose_field(MatterFieldKind.ACTOR_REFERENCE, "actor_reference", packet, envelope, correlation),
    )
    return MatterFieldDiagnostic(prior, checks)
