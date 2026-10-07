"""DSP-004 boundary-contract candidate, REV1; local synthetic use only.

Candidate loading identity: DSP_004_NATIVE_CONTRACT_CANDIDATE_REV1.
The adopted future contract layer remains route_b_c03.contracts. This separate
candidate is not that module, is not integrated into it, and does not establish
the approved native identity of its classes. Existing contracts and Gate code
remain unchanged. Candidate acceptance is not established by materialization.

Design-text source record SHA-256:
DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4

This module validates structural metadata only. States and causes are supplied
by the caller; it does not read sources, capture actual values, compare reference
values, select a Gate outcome, or establish trust, source admission, same-call
provenance, authority, isolation, or a review verdict. Nonempty source IDs do
not establish that either source was controlled or bound. Correlation equality
does not prove that records came from one call. These checks are not substitutes
for the separately authorized capture, source-binding, and comparison layers.
"""

from dataclasses import dataclass
from enum import Enum, unique


@unique
class BoundaryKind(Enum):
    PROJECT = "PROJECT"
    SESSION = "SESSION"
    PROVIDER = "PROVIDER"


@unique
class BoundaryCheckState(Enum):
    MATCH = "MATCH"
    MISMATCH = "MISMATCH"
    UNBOUND = "UNBOUND"
    NOT_EVALUATED = "NOT_EVALUATED"


@unique
class BoundaryCheckCause(Enum):
    EXACT_EQUAL = "EXACT_EQUAL"
    EXACT_UNEQUAL = "EXACT_UNEQUAL"
    SOURCE_UNBOUND = "SOURCE_UNBOUND"
    INVALID_REFERENCE_TYPE = "INVALID_REFERENCE_TYPE"
    PRIOR_DENIAL = "PRIOR_DENIAL"


def _require_native_text(value: str, field: str) -> None:
    if type(value) is not str:
        raise TypeError(f"{field} requires native str")
    if not value or value.isspace():
        raise ValueError(f"{field} requires nonempty, non-whitespace text")


def _require_source_id(value: str | None, field: str, *, required: bool) -> None:
    if value is None:
        if required:
            raise ValueError(f"{field} is required for MATCH or MISMATCH")
        return
    _require_native_text(value, field)


@dataclass(frozen=True, slots=True)
class BoundaryCheck:
    """Six literal fields; structural validity is not a trusted observation."""

    boundary: BoundaryKind
    state: BoundaryCheckState
    cause: BoundaryCheckCause
    audit_correlation_id: str
    expected_source_id: str | None
    actual_source_id: str | None

    def __post_init__(self) -> None:
        if type(self.boundary) is not BoundaryKind:
            raise TypeError("boundary requires this candidate's native BoundaryKind")
        if type(self.state) is not BoundaryCheckState:
            raise TypeError("state requires this candidate's native BoundaryCheckState")
        if type(self.cause) is not BoundaryCheckCause:
            raise TypeError("cause requires this candidate's native BoundaryCheckCause")
        _require_native_text(self.audit_correlation_id, "audit_correlation_id")

        allowed_causes = {
            BoundaryCheckState.MATCH: (BoundaryCheckCause.EXACT_EQUAL,),
            BoundaryCheckState.MISMATCH: (BoundaryCheckCause.EXACT_UNEQUAL,),
            BoundaryCheckState.UNBOUND: (
                BoundaryCheckCause.SOURCE_UNBOUND,
                BoundaryCheckCause.INVALID_REFERENCE_TYPE,
            ),
            BoundaryCheckState.NOT_EVALUATED: (BoundaryCheckCause.PRIOR_DENIAL,),
        }
        if self.cause not in allowed_causes[self.state]:
            raise ValueError("state and cause do not form an allowed pair")
        source_ids_required = self.state in (
            BoundaryCheckState.MATCH,
            BoundaryCheckState.MISMATCH,
        )
        _require_source_id(
            self.expected_source_id, "expected_source_id", required=source_ids_required
        )
        _require_source_id(
            self.actual_source_id, "actual_source_id", required=source_ids_required
        )


def validate_boundary_check_sequence(
    checks: tuple[BoundaryCheck, BoundaryCheck, BoundaryCheck],
) -> tuple[BoundaryCheck, BoundaryCheck, BoundaryCheck]:
    """Validate candidate-native structure and return the same exact tuple.

    No dictionaries, lists, subclasses, or same-named foreign classes are
    converted. No fields are repaired, normalized, synthesized, or backfilled.
    The returned tuple is not an aggregate outcome or same-call proof.
    """
    if type(checks) is not tuple:
        raise TypeError("checks requires native tuple")
    if len(checks) != 3:
        raise ValueError("checks requires exactly three elements")
    for check in checks:
        if type(check) is not BoundaryCheck:
            raise TypeError("each element requires this candidate's native BoundaryCheck")
        # Revalidate even if low-level caller code bypassed dataclass freezing.
        BoundaryCheck.__post_init__(check)
    if tuple(check.boundary for check in checks) != (
        BoundaryKind.PROJECT,
        BoundaryKind.SESSION,
        BoundaryKind.PROVIDER,
    ):
        raise ValueError("boundary order requires PROJECT, SESSION, PROVIDER")
    if any(
        check.audit_correlation_id != checks[0].audit_correlation_id
        for check in checks[1:]
    ):
        raise ValueError("audit correlation values differ")
    return checks
