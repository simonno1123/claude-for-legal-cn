"""Namespace, reference-only and output-classification boundary checks with no I/O."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

from .contracts import CandidateClass, InvocationState

LOCAL_CANDIDATE_NAMESPACE = "route_b_c03.local_candidate"
PROHIBITED_WRITE_NAMESPACES = (
    "route_a",
    "evidence",
    "matter_decision",
    "legal_reasoning",
    "human_decision",
    "external_domain",
    "acos_source_project",
)
PROHIBITED_REFERENCE_KEYS = (
    "bytes",
    "content",
    "payload",
    "prompt",
    "attachment",
    "history",
    "credential",
    "secret",
    "token",
    "cookie",
    "authorization_header",
    "private_endpoint",
)


class IsolationViolation(ValueError):
    """Raised when a namespace or reference crosses the closed boundary."""


def assert_permitted_write_set(write_set: Mapping[str, Sequence[str]]) -> None:
    for namespace in PROHIBITED_WRITE_NAMESPACES:
        if tuple(write_set.get(namespace, ())) != ():
            raise IsolationViolation(f"REJECTED — PROHIBITED WRITE: {namespace}")
    unknown = set(write_set) - set(PROHIBITED_WRITE_NAMESPACES) - {
        LOCAL_CANDIDATE_NAMESPACE
    }
    if unknown:
        raise IsolationViolation("REJECTED — UNKNOWN WRITE NAMESPACE")


# Value markers of secret material (V7); compared case-insensitively as substrings of str values.
PROHIBITED_VALUE_MARKERS = (
    "-----begin",
    "bearer ",
    "authorization:",
    "password=",
    "password:",
    "secret=",
    "secret:",
    "token=",
    "token:",
    "api_key=",
    "api_key:",
    "apikey=",
    "private_key",
)
MAX_REFERENCE_DEPTH = 8


def _check_reference_value(value: object, depth: int) -> None:
    if depth > MAX_REFERENCE_DEPTH:
        raise IsolationViolation("QUARANTINED — REFERENCE NESTING TOO DEEP")
    if type(value) in (bytes, bytearray, memoryview):
        raise IsolationViolation("QUARANTINED — RAW BYTES PROHIBITED")
    if isinstance(value, str):
        folded = value.casefold()
        if any(marker in folded for marker in PROHIBITED_VALUE_MARKERS):
            raise IsolationViolation("QUARANTINED — SECRET MARKER IN VALUE")
        return
    if isinstance(value, Mapping):
        _check_reference_mapping(value, depth + 1)
        return
    if isinstance(value, (tuple, list, set, frozenset)):
        for item in value:
            _check_reference_value(item, depth + 1)


def _check_reference_mapping(record: Mapping[str, object], depth: int) -> None:
    for key, value in record.items():
        if not isinstance(key, str):
            raise IsolationViolation("QUARANTINED — NON-TEXT FIELD NAME")
        normalized = key.lower().replace("-", "_")
        if any(term in normalized for term in PROHIBITED_REFERENCE_KEYS):
            raise IsolationViolation(f"QUARANTINED — CONTENT FIELD PROHIBITED: {key}")
        _check_reference_value(value, depth)


def assert_reference_only(record: Mapping[str, object]) -> None:
    """Field names at every nesting level and str values are screened; raw bytes are refused (V-005, V7)."""
    _check_reference_mapping(record, 0)


# ---------------------------------------------------------------------------
# Output-classification boundary (V-015, RDM-DSP-012; WP-007 design 16)
# ---------------------------------------------------------------------------

# Design 16.2: output classes the capability may never produce, whoever asks.
PROHIBITED_OUTPUT_CLASSES = (
    "FINAL_LEGAL_OPINION",
    "ENFORCEMENT_STRATEGY_OR_TACTIC",
    "COURT_OR_AUTHORITY_SUBMISSION",
    "ASSET_SEARCH_OR_TRACING_INSTRUCTION",
    "ADDITIONAL_PARTY_OR_LIABILITY_CONCLUSION",
    "OBJECTION_OR_REMEDY_CONCLUSION",
    "SETTLEMENT_OR_PAYMENT_INSTRUCTION",
    "OUTCOME_PREDICTION",
    "SUCCESS_PROBABILITY",
    "AUTOMATED_RISK_OR_COMPLIANCE_SCORE",
)
# Design 16.3: the only qualified-human dispositions; none of them lifts the downstream block.
HUMAN_DISPOSITIONS = (
    "REJECT",
    "REQUEST CORRECTION",
    "KEEP BLOCKED",
    "APPROVE A SPECIFIC CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP",
)


@dataclass(frozen=True, slots=True)
class ClassificationDetermination:
    request_state: InvocationState
    candidate_state: InvocationState
    downstream_blocked: bool
    reason_code: str

    def __post_init__(self) -> None:
        # The type itself keeps the boundary: no determination can unblock downstream use or leave review.
        if type(self.request_state) is not InvocationState or self.request_state not in (
            InvocationState.REJECTED, InvocationState.HUMAN_REVIEW_PENDING,
        ):
            raise ValueError("request_state must be REJECTED or HUMAN_REVIEW_PENDING")
        if self.candidate_state is not InvocationState.HUMAN_REVIEW_PENDING:
            raise ValueError("candidate_state must remain HUMAN_REVIEW_PENDING")
        if self.downstream_blocked is not True:
            raise ValueError("downstream_blocked must remain True")
        if type(self.reason_code) is not str or not self.reason_code:
            raise ValueError("reason_code must be a non-empty str")


def evaluate_classification_request(
    requested_class: object,
    *,
    human_disposition: str | None,
) -> ClassificationDetermination:
    """Only an exact permitted CandidateClass member is accepted as a candidate class; anything else, including
    legal advice, a prohibited design-16.2 class or a raw string, is rejected. In every case the candidate stays
    HUMAN_REVIEW_PENDING and downstream use stays blocked; a human disposition cannot change that."""
    pending = InvocationState.HUMAN_REVIEW_PENDING
    if human_disposition is not None and (type(human_disposition) is not str or human_disposition not in HUMAN_DISPOSITIONS):
        return ClassificationDetermination(InvocationState.REJECTED, pending, True, "REJECTED — HUMAN DISPOSITION UNKNOWN")
    if type(requested_class) is not CandidateClass:
        if type(requested_class) is str and requested_class.strip().upper() in PROHIBITED_OUTPUT_CLASSES:
            reason = "REJECTED — OUTPUT BOUNDARY FAILURE: PROHIBITED CLASS"
        else:
            reason = "REJECTED — OUTPUT BOUNDARY FAILURE: CLASS NOT PERMITTED"
        return ClassificationDetermination(InvocationState.REJECTED, pending, True, reason)
    if human_disposition == HUMAN_DISPOSITIONS[3]:
        return ClassificationDetermination(pending, pending, True, "APPROVED FOR A SEPARATE NEXT STEP ONLY — DOWNSTREAM STILL BLOCKED")
    return ClassificationDetermination(pending, pending, True, "CANDIDATE CLASS PERMITTED — HUMAN REVIEW PENDING; DOWNSTREAM BLOCKED")
