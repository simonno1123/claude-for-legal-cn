"""DSP-004 eligible-only decision-combination candidate, REV1.

Loading identity: DSP_004_ELIGIBLE_DECISION_COMBINER_CANDIDATE_REV1.
This is an unintegrated local synthetic diagnostic, not the current identity
gate, a trusted capture layer, source admission, or formal WP-008 validation.
It consumes caller-provided synthetic labels; it does not establish that the
prior decision came from the real gate or that checks came from controlled
sources or one call. Correlation equality is structural, not provenance proof.

Design record SHA-256:
DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4
Existing contracts.py SHA-256 (GateDecision / InvocationState only):
7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4
Independent boundary-contract candidate SHA-256:
1544B7D8101493072E9BCA5C23B09C3C811F1B52CB1E9F5A8D73C976576FC312

The boundary classes retain their independent candidate loading identity;
they are not the future route_b_c03.contracts boundary classes. Hash binding
belongs to the controlled test loader, not to this pure function. Existing
contracts, gate, accepted candidates, and design files remain unchanged.

Only ELIGIBLE_FOR_MAPPING input is in scope. Type errors raise TypeError;
value, structure, or scope errors raise ValueError without a GateDecision.
Non-eligible input is not passed through or evaluated. NOT_EVALUATED input
fails before the seven-level priority, even with another invalid/unbound item.
The function does not generate observations, read/compare reference values,
execute the gate, map fixtures, capture actuals, or authorize mapping/provider
execution. Returned metadata is not a privacy/security or isolation verdict.
"""

from route_b_c03.contracts import GateDecision, InvocationState
from DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1 import (
    BoundaryCheck,
    BoundaryCheckCause,
    BoundaryCheckState,
    validate_boundary_check_sequence,
)


def _require_native_text(value: str, field: str) -> None:
    if type(value) is not str:
        raise TypeError(f"{field} requires native str")
    if not value or value.isspace():
        raise ValueError(f"{field} requires nonempty, non-whitespace text")


def _validate_prior(prior: GateDecision) -> None:
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
    if state is not InvocationState.ELIGIBLE_FOR_MAPPING:
        raise ValueError("only ELIGIBLE_FOR_MAPPING prior input is in scope")


def combine_eligible_decision(
    prior: GateDecision,
    checks: tuple[BoundaryCheck, BoundaryCheck, BoundaryCheck],
) -> GateDecision:
    """Combine valid synthetic eligible metadata without changing input objects.

    Checks use the accepted independent candidate's exact types and order.
    Invalid input raises; no substitute checks or gate result are constructed.
    All-MATCH returns the same prior object with its complete reason unchanged.
    New protective decisions carry the unchanged correlation and empty tuple.
    """
    _validate_prior(prior)
    try:
        checks = validate_boundary_check_sequence(checks)
    except AttributeError as error:
        raise ValueError("checks require initialized native fields") from error
    if any(check.audit_correlation_id != prior.audit_correlation_id for check in checks):
        raise ValueError("check and prior audit correlation values differ")
    if any(check.state is BoundaryCheckState.NOT_EVALUATED for check in checks):
        raise ValueError("NOT_EVALUATED is outside eligible-combination input scope")

    if any(check.cause is BoundaryCheckCause.INVALID_REFERENCE_TYPE for check in checks):
        return GateDecision(
            InvocationState.BLOCKED,
            "BLOCKED — CONTEXT REFERENCE INVALID",
            prior.audit_correlation_id,
            (),
        )
    if any(check.cause is BoundaryCheckCause.SOURCE_UNBOUND for check in checks):
        return GateDecision(
            InvocationState.BLOCKED,
            "BLOCKED — CONTEXT SOURCE UNBOUND",
            prior.audit_correlation_id,
            (),
        )

    mismatches = tuple(check.state is BoundaryCheckState.MISMATCH for check in checks)
    if sum(mismatches) >= 2:
        return GateDecision(
            InvocationState.REJECTED,
            "REJECTED — MULTIPLE CONTEXT MISMATCHES",
            prior.audit_correlation_id,
            (),
        )
    if mismatches[0]:
        return GateDecision(
            InvocationState.REJECTED,
            "REJECTED — PROJECT CONTEXT MISMATCH",
            prior.audit_correlation_id,
            (),
        )
    if mismatches[1]:
        return GateDecision(
            InvocationState.REJECTED,
            "REJECTED — SESSION CONTEXT MISMATCH",
            prior.audit_correlation_id,
            (),
        )
    if mismatches[2]:
        return GateDecision(
            InvocationState.REJECTED,
            "REJECTED — PROVIDER CONTEXT MISMATCH",
            prior.audit_correlation_id,
            (),
        )
    return prior
