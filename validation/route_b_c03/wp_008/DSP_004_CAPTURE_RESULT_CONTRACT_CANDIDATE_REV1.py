"""DSP-004 in-memory capture-result contract candidate, REV1.

Loading identity: DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1.
These independent candidate classes are not route_b_c03.contracts additions,
BoundaryCheck classes, a capture adapter, or an integrated runtime protocol.
Creation does not accept, admit, load, compile, test, or execute this source.

Design sources are the conversation-level, limited-adopted Actual Capture
Interface Contract REV2 and Capture Return / Failure Representation REV2.
They have no independent physical file SHA. The fixed design reference is:
docs/phase2/route-b/DSP_004_SOURCE_USE_AND_INPUT_EXTENSION_REV1_CANDIDATE.md
F4B995D8F2DA424E68D94EA7E31FB6387F628C7681BEF5CC05807A29D6684A2F
Existing contracts.py identity, for GateDecision / InvocationState only:
7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4
The separately authorized loader, not these constructors, binds real classes,
dependencies, verified bytes, actual interpreter, source permissions and use.

This file only validates caller-supplied structural metadata. It does not read
sources, capture references, call a Gate/provider, compare expected and actual
references, run cleanup, transport results, record evidence, hash data, or grant
authority. Nonempty source/basis IDs, snapshot-shaped SHA strings and matching
correlations do not establish provenance, source admission, one invocation,
snapshot completeness, freezing, cleanup success or physical isolation.

CompleteCaptureReturn describes an ALREADY completed handoff, not a promise or
pre-handoff acknowledgement. Its three explicit True flags remain caller
claims, not witnesses of real events. No factory sets them or manufactures an
acknowledgement before delivery. CaptureMaterials is the distinct material
holder; even three acquired records are not a successful return. Receipt,
necessary-cleanup applicability/basis and actual handoff remain external and
LIMITED; constructing or validating a descriptor performs none of them.

The candidate is in-memory only. raw_value holds the supplied original object
reference; raw_type must be its actual type object, not a type-name string.
This is not permission to admit arbitrary source values or serialize objects.
Approved source value ranges and exact formal/partial/failure encodings remain
LIMITED. No stringify, repr, JSON, pickle, deepcopy, normalization, observed
SHA, automatic matching, or cross-process conversion is provided. None in a
CapturedReference is an acquired value; an absent record denotes no acquired
value for that boundary. It is never padded with a fabricated None record.

Frozen/slotted objects are shallow metadata carriers, not a trust boundary or
proof of immutable raw values. Equality/repr generation is disabled to avoid
implicitly comparing/displaying payloads. This does not guarantee silence,
zero disclosure, zero side effects or destruction. Raw references, exceptions,
tracebacks and cause chains can retain inputs, modules and local state. Default
exception output, reference escape, resource exhaustion, forced termination
and repeated interruption are not controlled here. A descriptive failure
container is not a raised wrapper and does not reproduce exception matching,
interrupt effects or exit status.

Exact carrier fields and type checks below are candidate implementation choices,
not prior acceptance of native types, source identities or failure-saving
mechanisms. They do not define formal record encoding or a runtime Schema.
All prior LIMITED and historical failures remain. DSP-004 is OPEN / HOLD;
B-01 / B-02 remain OPEN. Accepted files and the 189-item list stay unchanged.
"""

from dataclasses import dataclass
from enum import Enum, unique

from route_b_c03.contracts import GateDecision, InvocationState


@unique
class CaptureBoundary(Enum):
    """Candidate-local labels, not the existing BoundaryKind class."""

    PROJECT = "PROJECT"
    SESSION = "SESSION"
    PROVIDER = "PROVIDER"


@unique
class CaptureIncompleteCause(Enum):
    """Descriptive non-exception facts, never Gate/BoundaryCheck outcomes."""

    INTERRUPTED_WITHOUT_EXCEPTION = "INTERRUPTED_WITHOUT_EXCEPTION"
    NO_RETURN = "NO_RETURN"
    MISSING_OBSERVATION = "MISSING_OBSERVATION"
    CARRIER_IDENTITY_FAILURE = "CARRIER_IDENTITY_FAILURE"
    HANDOFF_INCOMPLETE = "HANDOFF_INCOMPLETE"


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CaptureInvocationBinding:
    """Four literal identifiers; their structure is not a same-call proof."""

    variant_id: str
    attempt_id: str
    input_snapshot_sha256: str
    audit_correlation_id: str

    def __post_init__(self) -> None:
        _validate_binding(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CapturedReference:
    """One supplied acquired value, including a genuinely acquired None.

    Presence means the caller describes acquisition, not that this constructor
    performed or authenticated it. raw_type is retained by identity. Source
    identity mapping to BoundaryCheck.actual_source_id remains external.
    """

    boundary: CaptureBoundary
    actual_source_identity: str
    raw_value: object
    raw_type: type

    def __post_init__(self) -> None:
        _validate_reference(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CaptureMaterials:
    """Zero to three acquired records, in boundary order, without padding.

    Three records can still be failure materials after cleanup/return failure.
    A missing boundary is the complement of this unique ordered subsequence.
    prior_decision=None means no valid original GateDecision was preserved;
    it never stands for a captured reference or a newly fabricated gate result.
    The real prior object is held as supplied, never projected or rebuilt.
    A real prior that violates this field contract must still be preserved by
    a separately governed outer failure path, not silently relabeled None or
    never-returned. That malformed-prior preservation path is not implemented
    by this candidate; these carriers do not cover every invalid Gate output.
    """

    invocation: CaptureInvocationBinding
    acquired: tuple[CapturedReference, ...]
    prior_decision: GateDecision | None

    def __post_init__(self) -> None:
        _validate_materials(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CompleteCaptureReturn:
    """Retrospective structural description, NOT a capture/cleanup receipt.

    All flags must be native True and explicitly supplied. cleanup_basis_id is
    only a literal reference to a separately bound applicability/completion
    basis. Its presence cannot prove approval, that cleanup ran, or that no
    cleanup was required. No missing-error inference or True default exists.
    Successful handoff cannot be self-certified before it happens. An outer
    separately governed receiving workflow must establish real completion;
    this file neither implements that workflow nor opens normal comparison.
    Reference validity, matching and Gate routing are not decided here.
    """

    materials: CaptureMaterials
    capture_completed: bool
    cleanup_completed: bool
    handoff_completed: bool
    cleanup_basis_id: str

    def __post_init__(self) -> None:
        _validate_complete(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class FailureOccurrence:
    """A supplied original BaseException and its descriptive actual stage.

    No exception is created, raised, stringified, cleared or replaced. This
    cannot prove the supplied object was raised, or authenticate the stage.
    Stage text is not an expression, callback, import or dispatch instruction.
    """

    stage: str
    error: BaseException

    def __post_init__(self) -> None:
        _validate_occurrence(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CaptureFailure:
    """Primary-only, cleanup-only, or both; never a normal success result.

    None means no exception occurrence is supplied for that particular slot;
    it is not a made-up exception or a missing captured value. Both slots may
    retain the same exception object if that is what the actual events used;
    identity alone is not grounds to deduplicate or invent another object.
    Zero to three acquired records are allowed as failed-handoff materials.
    """

    materials: CaptureMaterials
    primary_failure: FailureOccurrence | None
    cleanup_failure: FailureOccurrence | None

    def __post_init__(self) -> None:
        _validate_failure(self)


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class IncompleteCapture:
    """Incomplete fact with no available original exception object.

    Known original exceptions belong in CaptureFailure, not silently here.
    This class does not prove absence of an exception, rename a failure into
    CONSTRUCTION_FAILURE/SOURCE_UNBOUND/INVALID_REFERENCE_TYPE, or authorize
    any observation. Stage/cause are supplied descriptions, not real capture.
    """

    materials: CaptureMaterials
    stage: str
    cause: CaptureIncompleteCause

    def __post_init__(self) -> None:
        _validate_incomplete(self)


def _require_native_text(value: str, field: str) -> None:
    if type(value) is not str:
        raise TypeError(f"{field} requires native str")
    if not value or value.isspace():
        raise ValueError(f"{field} requires nonempty, non-whitespace text")


def _validate_binding(binding: CaptureInvocationBinding) -> None:
    if type(binding) is not CaptureInvocationBinding:
        raise TypeError("invocation requires this candidate's native binding")
    try:
        variant = binding.variant_id
        attempt = binding.attempt_id
        digest = binding.input_snapshot_sha256
        correlation = binding.audit_correlation_id
    except AttributeError as error:
        raise ValueError("invocation requires all four initialized fields") from error
    _require_native_text(variant, "variant_id")
    _require_native_text(attempt, "attempt_id")
    _require_native_text(digest, "input_snapshot_sha256")
    _require_native_text(correlation, "audit_correlation_id")
    if len(digest) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in digest
    ):
        raise ValueError("input_snapshot_sha256 requires complete 64-digit hex")


def _validate_reference(reference: CapturedReference) -> None:
    if type(reference) is not CapturedReference:
        raise TypeError("acquired entry requires this candidate's native reference")
    try:
        boundary = reference.boundary
        source = reference.actual_source_identity
        value = reference.raw_value
        value_type = reference.raw_type
    except AttributeError as error:
        raise ValueError("reference requires all four initialized fields") from error
    if type(boundary) is not CaptureBoundary:
        raise TypeError("boundary requires this candidate's native CaptureBoundary")
    if not any(boundary is member for member in CaptureBoundary):
        raise ValueError("boundary requires a declared native CaptureBoundary member")
    _require_native_text(source, "actual_source_identity")
    if value_type is not type(value):
        raise TypeError("raw_type must be the actual raw_value type object")


def _validate_prior(prior: GateDecision | None, correlation: str) -> None:
    if prior is None:
        return
    if type(prior) is not GateDecision:
        raise TypeError("prior_decision requires the existing native GateDecision")
    try:
        state = prior.state
        reason = prior.reason_code
        prior_correlation = prior.audit_correlation_id
        namespaces = prior.permitted_write_namespaces
    except AttributeError as error:
        raise ValueError("prior_decision requires all four initialized fields") from error
    if type(state) is not InvocationState:
        raise TypeError("prior.state requires the existing native InvocationState")
    if not any(state is member for member in InvocationState):
        raise ValueError("prior.state requires a declared native InvocationState member")
    _require_native_text(reason, "prior.reason_code")
    _require_native_text(prior_correlation, "prior.audit_correlation_id")
    if type(namespaces) is not tuple:
        raise TypeError("prior.permitted_write_namespaces requires native tuple")
    if namespaces:
        raise ValueError("prior.permitted_write_namespaces must be empty")
    if prior_correlation != correlation:
        raise ValueError("prior and invocation correlations differ")


def _validate_materials(materials: CaptureMaterials) -> None:
    if type(materials) is not CaptureMaterials:
        raise TypeError("materials requires this candidate's native CaptureMaterials")
    try:
        invocation = materials.invocation
        acquired = materials.acquired
        prior = materials.prior_decision
    except AttributeError as error:
        raise ValueError("materials requires all three initialized fields") from error
    _validate_binding(invocation)
    if type(acquired) is not tuple:
        raise TypeError("acquired requires native tuple, not a list or subclass")
    if len(acquired) > 3:
        raise ValueError("acquired permits only zero to three boundary records")
    order = (
        CaptureBoundary.PROJECT,
        CaptureBoundary.SESSION,
        CaptureBoundary.PROVIDER,
    )
    last_position = -1
    for reference in acquired:
        _validate_reference(reference)
        position = order.index(reference.boundary)
        if position <= last_position:
            raise ValueError("acquired requires unique records in boundary order")
        last_position = position
    _validate_prior(prior, invocation.audit_correlation_id)


def _validate_complete(result: CompleteCaptureReturn) -> None:
    if type(result) is not CompleteCaptureReturn:
        raise TypeError("result requires this candidate's native complete-return class")
    try:
        materials = result.materials
        capture = result.capture_completed
        cleanup = result.cleanup_completed
        handoff = result.handoff_completed
        cleanup_basis = result.cleanup_basis_id
    except AttributeError as error:
        raise ValueError("complete return requires all five initialized fields") from error
    _validate_materials(materials)
    if len(materials.acquired) != 3:
        raise ValueError("complete return requires all three acquired references")
    if materials.prior_decision is None:
        raise ValueError("complete return requires a preserved native prior decision")
    for flag in (capture, cleanup, handoff):
        if type(flag) is not bool:
            raise TypeError("completion flags require native bool")
        if flag is not True:
            raise ValueError("complete return requires all completion flags True")
    _require_native_text(cleanup_basis, "cleanup_basis_id")


def _validate_occurrence(occurrence: FailureOccurrence) -> None:
    if type(occurrence) is not FailureOccurrence:
        raise TypeError("failure requires this candidate's native FailureOccurrence")
    try:
        stage = occurrence.stage
        original_error = occurrence.error
    except AttributeError as error:
        raise ValueError("failure occurrence requires both initialized fields") from error
    _require_native_text(stage, "failure.stage")
    if not issubclass(type(original_error), BaseException):
        raise TypeError("failure.error requires an original BaseException object")


def _validate_failure(result: CaptureFailure) -> None:
    if type(result) is not CaptureFailure:
        raise TypeError("result requires this candidate's native CaptureFailure")
    try:
        materials = result.materials
        primary = result.primary_failure
        cleanup = result.cleanup_failure
    except AttributeError as error:
        raise ValueError("capture failure requires all three initialized fields") from error
    _validate_materials(materials)
    if primary is None and cleanup is None:
        raise ValueError("capture failure requires at least one real exception occurrence")
    if primary is not None:
        _validate_occurrence(primary)
    if cleanup is not None:
        _validate_occurrence(cleanup)


def _validate_incomplete(result: IncompleteCapture) -> None:
    if type(result) is not IncompleteCapture:
        raise TypeError("result requires this candidate's native IncompleteCapture")
    try:
        materials = result.materials
        stage = result.stage
        cause = result.cause
    except AttributeError as error:
        raise ValueError("incomplete capture requires all three initialized fields") from error
    _validate_materials(materials)
    _require_native_text(stage, "incomplete.stage")
    if type(cause) is not CaptureIncompleteCause:
        raise TypeError("incomplete cause requires this candidate's native enum")
    if not any(cause is member for member in CaptureIncompleteCause):
        raise ValueError("incomplete cause requires a declared native enum member")
    if cause is CaptureIncompleteCause.MISSING_OBSERVATION and len(materials.acquired) == 3:
        raise ValueError("MISSING_OBSERVATION cannot describe three acquired records")


def validate_capture_result(
    result: CompleteCaptureReturn | CaptureFailure | IncompleteCapture,
) -> CompleteCaptureReturn | CaptureFailure | IncompleteCapture:
    """Revalidate a candidate-native descriptor and return the identical object.

    Materials alone are not a complete result; dictionaries, subclasses and
    same-named foreign classes are not coerced. Failure/incomplete descriptors
    remain failure/incomplete descriptors; this does not open a success route.
    No original reference, exception or prior GateDecision is reconstructed.
    Revalidation is not an atomic freeze or proof against hostile mutation.
    """
    if type(result) is CompleteCaptureReturn:
        _validate_complete(result)
    elif type(result) is CaptureFailure:
        _validate_failure(result)
    elif type(result) is IncompleteCapture:
        _validate_incomplete(result)
    else:
        raise TypeError("result requires one of this candidate's three exact result classes")
    return result
