"""DSP-004 denied-decision preservation candidate, REV1; synthetic use only.

Loading identity: DSP_004_DENIED_DECISION_PRESERVER_CANDIDATE_REV1.
This independent candidate is not integrated into the current gate. It only
validates and returns caller-provided synthetic BLOCKED / REJECTED metadata.
It does not prove that a prior result came from the gate or a trusted source.

Design record SHA-256:
DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4
Existing contracts.py SHA-256 (GateDecision / InvocationState only):
7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4

Hash binding is the controlled test loader's responsibility, not this function.
All existing contracts, gate code, designs, and accepted candidates stay intact.
No replacement gate classes, boundary observations, reason interpretation,
matter/actor diagnosis, reference comparison, actual capture, or source reading
are provided here. Returning the same object is not actual gate execution,
source admission, same-call provenance, full denial-branch coverage, formal
WP-008 validation, integration, isolation proof, or downstream authority.

Type errors raise TypeError. Missing fields, invalid values, and states outside
BLOCKED / REJECTED raise ValueError. Failure never constructs a substitute
GateDecision. A valid result is returned by identity with every field unchanged.
An empty write tuple is only metadata, not proof of zero actual I/O.
"""

from route_b_c03.contracts import GateDecision, InvocationState


def _require_native_text(value: str, field: str) -> None:
    if type(value) is not str:
        raise TypeError(f"{field} requires native str")
    if not value or value.isspace():
        raise ValueError(f"{field} requires nonempty, non-whitespace text")


def preserve_denied_decision(prior: GateDecision) -> GateDecision:
    """Return the same valid native denied result without generating observations.

    Only native BLOCKED and REJECTED states are in this candidate's scope.
    Reason and correlation strings are preserved literally, never interpreted,
    trimmed, normalized, or used to infer which gate condition occurred.
    """
    if type(prior) is not GateDecision:
        raise TypeError("prior requires the existing native GateDecision")
    try:
        state = prior.state
        reason = prior.reason_code
        correlation = prior.audit_correlation_id
        namespaces = prior.permitted_write_namespaces
    except AttributeError as error:
        raise ValueError("prior requires all four initialized fields") from error
    if type(state) is not InvocationState:
        raise TypeError("prior.state requires the existing native InvocationState")
    _require_native_text(reason, "prior.reason_code")
    _require_native_text(correlation, "prior.audit_correlation_id")
    if type(namespaces) is not tuple:
        raise TypeError("prior.permitted_write_namespaces requires native tuple")
    if namespaces:
        raise ValueError("prior.permitted_write_namespaces must be empty")
    if state not in (InvocationState.BLOCKED, InvocationState.REJECTED):
        raise ValueError("only BLOCKED or REJECTED prior input is in scope")
    return prior
