"""DSP-004 synthetic execution carrier candidate REV4.

NEW successor for the expressly authorized local synthetic batch only.
Accepted REV3 is unchanged:
329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845
No business sources, provider calls, actual capture or integration are admitted.

The C01-C12 recipes/native oracles are copied exactly. Their results describe
only these synthetic inputs, not the 189-item plan or formal DSP acceptance.
This revision replaces the unconditional reference refusal ONLY in this new
file, with native module/runtime/pipe/source-basis checks. It neither patches
nor calls the accepted REV3 module. Basis objects describe observed local
facts, not approval flags or reusable authorization tokens. Standalone main
still returns 78; only the new fixed bootstrap binds source bytes and pipes.

Native observations/errors remain in-process. All private protocol messages
stay UNVERIFIED_REPORT. No raw errors/objects are serialized. Kill/exit/EOF
do not establish destruction or lossless exception preservation.
LIMITED: full environment/dependency provenance, check-to-use protection,
unobserved schedules, real business source qualification, formal coverage,
durable external ownership and protection against hostile same-process code.
This is not a security sandbox. All previous failures/reviews are preserved.
DSP-004 remains OPEN / HOLD; B-01/B-02 OPEN.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from importlib.machinery import ModuleSpec
from io import FileIO
from math import isfinite
from types import FunctionType, ModuleType
import sys
import os
import stat


CONTRACT_SHA256 = "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C"
DEPENDENCY_SHA256 = "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"
PACKAGE_NAME = "route_b_c03"
DEPENDENCY_NAME = "route_b_c03.contracts"
CONTRACT_NAME = "DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1"
CARRIER_MODULE_NAME = "DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV4"
PREDECESSOR_SHA256 = "329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845"
CONTROL_FRAME_LIMIT = 4096

# Private technical state, not an atomic or global authorization service.
_MODULE_LOAD_RESERVED = False
_HELD_LOAD_RECEIPTS = []

# Formation-time missing checkpoints, not a live environment/authority probe.
UNBOUND_CHECKPOINTS = (
    "EXACT_CARRIER_AND_EXECUTION_AUTHORITY",
    "INTERPRETER_BOOTSTRAP_AND_RECURSIVE_DEPENDENCIES",
    "FIXED_RESOLVER_AND_ROOT_READ_SCOPE",
    "APPROVED_SAME_BYTE_HANDOFF",
    "CASE_SET_ORACLE_AND_ASSERTION_ATTRIBUTION",
    "PRIVATE_CONTROL_PROTOCOL_AND_OUTPUT_BOUNDARY",
    "PROCESS_SCOPE_TIMER_TERMINATION_AND_CLEANUP",
)
NOT_IMPLEMENTED_GROUPS = ("C13_REAL_LOAD_FAILURE_RUNS", "C14_PHYSICAL_SUPERVISION")

EXPECTED_STATES = (
    "INVOCATION_RECEIVED", "GATE_CHECKING", "BLOCKED", "REJECTED",
    "ELIGIBLE_FOR_MAPPING", "MAPPING", "MAPPING_CANDIDATE", "QUARANTINED",
    "HUMAN_REVIEW_PENDING",
)
EXPECTED_BOUNDARIES = ("PROJECT", "SESSION", "PROVIDER")
EXPECTED_CAUSES = (
    "INTERRUPTED_WITHOUT_EXCEPTION", "NO_RETURN", "MISSING_OBSERVATION",
    "CARRIER_IDENTITY_FAILURE", "HANDOFF_INCOMPLETE",
)
GUARD_ARGS = {
    "BOUNDARY": ("boundary requires a declared native CaptureBoundary member",),
    "CAUSE": ("incomplete cause requires a declared native enum member",),
    "PRIOR": ("prior.state requires a declared native InvocationState member",),
}


def _declared_ids() -> tuple[str, ...]:
    """Fixed synthetic directory, independent of subject outputs/modules.

    This is only a candidate catalog, not Owner admission or run evidence.
    Its expansion must exactly match _recipe_catalog; C13/C14 are absent.
    """
    return (
        *("C01-" + field + "-" + label
          for field in ("variant_id", "attempt_id", "input_snapshot_sha256", "audit_correlation_id")
          for label in ("NONE", "BOOL", "SUBCLASS", "EMPTY", "SPACE")),
        *("C01-" + label for label in ("HEX64-LOWER", "HEX64-UPPER", "SHORT", "LONG", "NONHEX")),
        *("C02-" + name + "-" + label for name in EXPECTED_BOUNDARIES
          for label in ("NONE", "INT", "TEXT")),
        *("C02-" + label for label in ("BOUNDARY-TEXT", "TYPE-NAME", "WRONG-TYPE", "SOURCE-NONE")),
        "C02-SOURCE-EMPTY", "C02-SOURCE-SPACE",
        *("C03-SUBSET-" + str(mask) for mask in range(8)),
        *("C03-" + label for label in ("DUPLICATE", "REVERSED", "FOUR", "LIST", "TUPLE-SUBCLASS")),
        *("C04-STATE-" + name for name in EXPECTED_STATES),
        *("C04-" + label for label in ("STATE-TEXT", "REASON-BOOL", "REASON-EMPTY",
          "CORRELATION-NONE", "CORRELATION-OTHER", "WRITES-LIST", "WRITES-SUBCLASS", "WRITES-NONEMPTY")),
        *("C05-STRUCTURAL-" + name for name in ("BLOCKED", "REJECTED", "ELIGIBLE_FOR_MAPPING")),
        *("C05-" + label for label in ("CAPTURE-FALSE", "CLEANUP-FALSE", "HANDOFF-FALSE",
          "CAPTURE-INT", "CLEANUP-INT", "HANDOFF-INT", "BASIS-EMPTY", "BASIS-NONE")),
        *("C05-MISSING-" + str(count) for count in range(3)), "C05-NO-PRIOR",
        "C06-VALUE", "C06-INTERRUPT", "C06-EXIT",
        *("C06-NONEXCEPTION-" + label for label in ("CLASS", "TEXT", "NONE")),
        *("C07-" + str(count) + "-" + mode for count in range(4)
          for mode in ("PRIMARY", "CLEANUP", "BOTH", "SHARED")), "C07-NO-ERRORS",
        *("C08-" + name + "-" + str(count) for name in EXPECTED_CAUSES for count in range(4)),
        "C09-DICT", "C09-FOREIGN", "C09-MATERIALS-ONLY", "C09-RESULT-SUBCLASS",
        "C09-REVALIDATE-COMPLETE", "C09-REVALIDATE-FAILURE", "C09-REVALIDATE-INCOMPLETE",
        *("C10-CONSTRUCTOR-MISSING-" + name for name in (
          "CaptureInvocationBinding", "CapturedReference", "CaptureMaterials",
          "CompleteCaptureReturn", "FailureOccurrence", "CaptureFailure", "IncompleteCapture")),
        *("C10-REVALIDATE-MISSING-" + field for field in ("materials", "stage", "cause")),
        *("C11-" + target + "-" + phase + "-" + label
          for target in ("BOUNDARY", "CAUSE", "PRIOR")
          for phase in ("CONSTRUCT", "REVALIDATE") for label in ("PSEUDO", "CONTROL")),
        "C12-SHALLOW-FREEZE-LIMITATION",
    )


DECLARED_CASE_IDS = _declared_ids()


class PreparationBlocked(RuntimeError):
    """Fixed category only; does not contain sources or exception messages."""


class OracleMismatch(RuntimeError):
    """A carrier assertion failed, not an accepted subject rejection."""


_HELD_SYNTHETIC_BASIS = []


def _bind_synthetic_basis(code: FileIO, command: FileIO, report: FileIO,
                          dependency: bytes, contract: bytes) -> None:
    """One local native basis; no caller label can enable accepted sources."""
    _assert_current_carrier_identity()
    if _HELD_SYNTHETIC_BASIS:
        raise PreparationBlocked("SYNTHETIC_BASIS_ALREADY_BOUND")
    streams = (code, command, report)
    if (any(type(stream) is not FileIO for stream in streams)
            or len({stream.fileno() for stream in streams}) != 3
            or not code.readable() or code.writable()
            or not command.readable() or command.writable()
            or not report.writable() or report.readable()
            or any(not stat.S_ISFIFO(os.fstat(stream.fileno()).st_mode) for stream in streams)):
        raise PreparationBlocked("NATIVE_PIPE_BASIS_REQUIRED")
    dependency = _check_bound_bytes(dependency, DEPENDENCY_SHA256)
    contract = _check_bound_bytes(contract, CONTRACT_SHA256)
    if code.read(1) != b"":
        raise PreparationBlocked("SOURCE_EOF_NOT_OBSERVED")
    _HELD_SYNTHETIC_BASIS.append((streams, dependency, contract))
    _require_execution_binding()


def _require_execution_binding() -> None:
    _assert_current_carrier_identity()
    if (os.name != "nt" or sys.flags.isolated != 1 or sys.flags.no_site != 1
            or sys.dont_write_bytecode is not True
            or len(_HELD_SYNTHETIC_BASIS) != 1):
        raise PreparationBlocked("LOCAL_SYNTHETIC_RUNTIME_UNBOUND")
    streams, dependency, contract = _HELD_SYNTHETIC_BASIS[0]
    if (any(type(stream) is not FileIO or stream.closed for stream in streams)
            or sha256(dependency).hexdigest().upper() != DEPENDENCY_SHA256
            or sha256(contract).hexdigest().upper() != CONTRACT_SHA256):
        raise PreparationBlocked("LOCAL_SYNTHETIC_BASIS_CHANGED")



def run_validation() -> None:
    """Not a standalone runner: require the fixed bootstrap pipe/source basis."""
    _require_execution_binding()


def main() -> int:
    """Silent refusal. A zero exit would falsely suggest a completed run."""
    return 78


def _check(condition: bool) -> None:
    if type(condition) is not bool or condition is not True:
        raise OracleMismatch("STRUCTURAL_ASSERTION_FAILED")


def _check_bound_bytes(data: bytes, expected: str) -> bytes:
    """Pure byte identity only; not a read grant or transport attestation."""
    if type(data) is not bytes:
        raise PreparationBlocked("NATIVE_BYTES_REQUIRED")
    if sha256(data).hexdigest().upper() != expected:
        raise PreparationBlocked("BOUND_SOURCE_SHA_MISMATCH")
    return data


def _assert_current_carrier_identity() -> None:
    """Future bootstrap obligation; not proof of its hash or authority."""
    if type(sys.modules) is not dict:
        raise PreparationBlocked("MODULE_TABLE_NOT_NATIVE")
    current = sys.modules.get(CARRIER_MODULE_NAME)
    if (type(current) is not ModuleType or current.__dict__ is not globals()
            or __name__ != CARRIER_MODULE_NAME):
        raise PreparationBlocked("CARRIER_MODULE_IDENTITY_UNBOUND")
    for name in ("_load_reference_modules", "_recipe_catalog", "_exercise_recipe"):
        function = globals().get(name)
        if type(function) is not FunctionType or function.__globals__ is not globals():
            raise PreparationBlocked("CARRIER_FUNCTION_IDENTITY_UNBOUND")


def _load_reference_modules(dependency_bytes: bytes, contract_bytes: bytes):
    """One owner for B/A; no accepted carrier import or preloading.

    A receipt holds exact module objects before registration/execution, including
    partial-load failures. It is neither a resolver nor cleanup implementation.
    """
    _require_execution_binding()
    global _MODULE_LOAD_RESERVED
    _assert_current_carrier_identity()
    if _MODULE_LOAD_RESERVED:
        raise PreparationBlocked("REFERENCE_LOAD_ALREADY_RESERVED")
    _MODULE_LOAD_RESERVED = True
    receipt = ReferenceLoadReceipt([], "SOURCE_BYTES", None)
    _HELD_LOAD_RECEIPTS.append(receipt)
    try:
        dependency_bytes = _check_bound_bytes(dependency_bytes, DEPENDENCY_SHA256)
        contract_bytes = _check_bound_bytes(contract_bytes, CONTRACT_SHA256)
        names = (PACKAGE_NAME, DEPENDENCY_NAME, CONTRACT_NAME)
        if any(name in sys.modules for name in names):
            raise PreparationBlocked("PREEXISTING_MODULE_IDENTITY")
        package = ModuleType(PACKAGE_NAME)
        package.__package__ = PACKAGE_NAME
        package.__path__ = ()
        package.__spec__ = ModuleSpec(PACKAGE_NAME, loader=None, is_package=True)
        package.__spec__.submodule_search_locations = []
        dependency = ModuleType(DEPENDENCY_NAME)
        dependency.__package__ = PACKAGE_NAME
        dependency.__spec__ = ModuleSpec(DEPENDENCY_NAME, loader=None)
        dependency.__file__ = "<DSP004_FIXED_DEPENDENCY_BYTES>"
        contract = ModuleType(CONTRACT_NAME)
        contract.__package__ = ""
        contract.__spec__ = ModuleSpec(CONTRACT_NAME, loader=None)
        contract.__file__ = "<DSP004_FIXED_CONTRACT_BYTES>"
        for name, module in ((PACKAGE_NAME, package), (DEPENDENCY_NAME, dependency)):
            receipt.owned_slots.append((name, module))
            sys.modules[name] = module
        receipt.stage = "DEPENDENCY_EXECUTION"
        exec(compile(dependency_bytes, dependency.__file__, "exec",
                     dont_inherit=True, optimize=0), dependency.__dict__)
        package.contracts = dependency
        receipt.owned_slots.append((CONTRACT_NAME, contract))
        sys.modules[CONTRACT_NAME] = contract
        receipt.stage = "CONTRACT_EXECUTION"
        exec(compile(contract_bytes, contract.__file__, "exec",
                     dont_inherit=True, optimize=0), contract.__dict__)
        _check(sys.modules[PACKAGE_NAME] is package)
        _check(sys.modules[DEPENDENCY_NAME] is dependency)
        _check(sys.modules[CONTRACT_NAME] is contract)
        _check(contract.GateDecision is dependency.GateDecision)
        _check(contract.InvocationState is dependency.InvocationState)
        validator = contract.validate_capture_result
        _check(type(validator) is FunctionType)
        _check(validator.__globals__ is contract.__dict__)
        receipt.stage = "REFERENCE_MODULES_RETURNED"
        return contract, dependency
    except BaseException as original:
        # Re-raise the SAME object, including real interrupts. Do not render it,
        # convert it to an expected negative, remove slots, or reload to reset.
        receipt.original_error = original
        raise


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class PreparedCall:
    """SETUP product: separate native SUT action and positive oracle."""

    action: object
    oracle: object = None


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CaseRecipe:
    """setup -> zero-argument action; oracle sees return/exception in-process.

    The catalog is private, fixed synthetic code. Arbitrary external callbacks
    are not an admitted input interface. Objects here must not be logged.
    """

    case_id: str
    group: str
    setup: object
    expected_exception: type[BaseException] | None
    expected_args: tuple[str, ...] | None = None


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class CaseObservation:
    """Descriptive in-memory outcome, not authenticated control evidence."""

    case_id: str
    phase: str
    determination: str
    original_error: BaseException | None


def _exercise_recipe(recipe: CaseRecipe) -> CaseObservation:
    """Reference oracle mechanics; no reporter, process or authority grant.

    SETUP is outside the expected-rejection catch. Real interrupts abort the
    batch, unlike merely constructing an interrupt instance as a raw value.
    Unexpected exceptions remain original objects, not message-only records.
    """
    if type(recipe) is not CaseRecipe:
        raise PreparationBlocked("NATIVE_RECIPE_REQUIRED")
    try:
        if type(recipe.setup) is not FunctionType:
            raise PreparationBlocked("NATIVE_SETUP_FUNCTION_REQUIRED")
        prepared = recipe.setup()
        if type(prepared) is not PreparedCall or type(prepared.action) is not FunctionType:
            raise PreparationBlocked("NATIVE_PREPARED_ACTION_REQUIRED")
        if recipe.expected_exception is None:
            if type(prepared.oracle) is not FunctionType:
                raise PreparationBlocked("POSITIVE_ORACLE_REQUIRED")
        elif (recipe.expected_exception is not TypeError and recipe.expected_exception is not ValueError
              or prepared.oracle is not None):
            raise PreparationBlocked("INVALID_NEGATIVE_RECIPE")
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as original:
        return CaseObservation(recipe.case_id, "SETUP", "NOT_EVALUABLE", original)
    try:
        result = prepared.action()
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as original:
        if recipe.expected_exception is None or type(original) is not recipe.expected_exception:
            return CaseObservation(recipe.case_id, "SUT", "FAIL", original)
        if recipe.expected_args is not None:
            arguments = original.args
            if (type(arguments) is not tuple or len(arguments) != 1
                    or type(arguments[0]) is not str or arguments != recipe.expected_args):
                return CaseObservation(recipe.case_id, "SUT", "FAIL", original)
        return CaseObservation(recipe.case_id, "SUT", "PASS", original)
    if recipe.expected_exception is not None:
        return CaseObservation(recipe.case_id, "SUT", "FAIL", None)
    try:
        prepared.oracle(result)
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException as original:
        return CaseObservation(recipe.case_id, "ORACLE", "FAIL", original)
    return CaseObservation(recipe.case_id, "ORACLE", "PASS", None)


def _binding(contract, **changes):
    fields = {
        "variant_id": "SYNTHETIC-CARRIER-VARIANT",
        "attempt_id": "SYNTHETIC-CARRIER-ATTEMPT",
        "input_snapshot_sha256": "1" * 64,
        "audit_correlation_id": "SYNTHETIC-CARRIER-CORRELATION",
    }
    fields.update(changes)
    return contract.CaptureInvocationBinding(**fields)


def _prior(dependency, state_name="BLOCKED", **changes):
    fields = {
        "state": getattr(dependency.InvocationState, state_name),
        "reason_code": "SYNTHETIC-PRIOR-REASON",
        "audit_correlation_id": "SYNTHETIC-CARRIER-CORRELATION",
        "permitted_write_namespaces": (),
    }
    fields.update(changes)
    return dependency.GateDecision(**fields)


def _reference(contract, name="PROJECT", value=None, **changes):
    fields = {
        "boundary": getattr(contract.CaptureBoundary, name),
        "actual_source_identity": "SYNTHETIC-SOURCE-ROLE-ONLY",
        "raw_value": value,
        "raw_type": type(value),
    }
    fields.update(changes)
    return contract.CapturedReference(**fields)


def _materials(contract, dependency, names=(), with_prior=False):
    records = tuple(_reference(contract, name, object()) for name in names)
    return contract.CaptureMaterials(
        _binding(contract), records, _prior(dependency) if with_prior else None,
    )


def _incomplete(contract, dependency, names=(), with_prior=False):
    return contract.IncompleteCapture(
        _materials(contract, dependency, names, with_prior),
        "SYNTHETIC-STRUCTURE-STAGE", contract.CaptureIncompleteCause.NO_RETURN,
    )


def _binding_oracle(contract, expected_digest):
    def oracle(result):
        _check(type(result) is contract.CaptureInvocationBinding)
        for actual, expected in (
            (result.variant_id, "SYNTHETIC-CARRIER-VARIANT"),
            (result.attempt_id, "SYNTHETIC-CARRIER-ATTEMPT"),
            (result.input_snapshot_sha256, expected_digest),
            (result.audit_correlation_id, "SYNTHETIC-CARRIER-CORRELATION"),
        ):
            _check(type(actual) is str)
            _check(actual == expected)
    return oracle


def _material_identity_oracle(contract, dependency, original):
    """Capture pre-action identity anchors, not a semantic Gate oracle."""
    _check(type(original) is contract.CaptureMaterials)
    invocation, acquired, prior = original.invocation, original.acquired, original.prior_decision
    _check(type(invocation) is contract.CaptureInvocationBinding)
    _check(type(acquired) is tuple)
    fields = (invocation.variant_id, invocation.attempt_id,
              invocation.input_snapshot_sha256, invocation.audit_correlation_id)
    records = tuple((record, record.boundary, record.actual_source_identity,
                     record.raw_value, record.raw_type) for record in acquired)
    prior_fields = None
    if prior is not None:
        _check(type(prior) is dependency.GateDecision)
        prior_fields = (prior.state, prior.reason_code, prior.audit_correlation_id,
                        prior.permitted_write_namespaces)

    def oracle(result):
        _check(result is original)
        _check(result.invocation is invocation)
        _check(result.acquired is acquired)
        _check(result.prior_decision is prior)
        for actual, saved in zip((invocation.variant_id, invocation.attempt_id,
                                  invocation.input_snapshot_sha256, invocation.audit_correlation_id), fields):
            _check(actual is saved)
        _check(len(result.acquired) == len(records))
        for record, saved in zip(result.acquired, records):
            _check(record is saved[0])
            _check(record.boundary is saved[1])
            _check(record.actual_source_identity is saved[2])
            _check(record.raw_value is saved[3])
            _check(record.raw_type is saved[4])
        if prior is not None:
            for actual, saved in zip((prior.state, prior.reason_code,
                                      prior.audit_correlation_id, prior.permitted_write_namespaces), prior_fields):
                _check(actual is saved)
    return oracle


def _result_identity_oracle(contract, dependency, original):
    """Before/after reference retention for an already prepared result."""
    kind = type(original)
    _check(kind in (contract.CompleteCaptureReturn, contract.CaptureFailure, contract.IncompleteCapture))
    materials = original.materials
    material_oracle = _material_identity_oracle(contract, dependency, materials)
    if kind is contract.CompleteCaptureReturn:
        saved = (original.capture_completed, original.cleanup_completed,
                 original.handoff_completed, original.cleanup_basis_id)
    elif kind is contract.IncompleteCapture:
        saved = (original.stage, original.cause)
    else:
        saved = (original.primary_failure, original.cleanup_failure)
    occurrences = ()
    if kind is contract.CaptureFailure:
        occurrences = tuple((slot, slot.stage, slot.error) for slot in saved if slot is not None)

    def oracle(result):
        _check(result is original)
        material_oracle(result.materials)
        if kind is contract.CompleteCaptureReturn:
            actual = (result.capture_completed, result.cleanup_completed,
                      result.handoff_completed, result.cleanup_basis_id)
        elif kind is contract.IncompleteCapture:
            actual = (result.stage, result.cause)
        else:
            actual = (result.primary_failure, result.cleanup_failure)
        for value, anchor in zip(actual, saved):
            _check(value is anchor)
        for occurrence, stage, error in occurrences:
            _check(occurrence.stage is stage)
            _check(occurrence.error is error)
    return oracle


def _member_precondition(value, enum_type, declared):
    _check(type(value) is enum_type)
    _check(all(value is not member for member in declared))


def _allocate_pseudo(enum_type, declared, *, string_base=False):
    # Allocation is a proposed runtime-specific technique, not proven here.
    if string_base:
        pseudo = str.__new__(enum_type, "SYNTHETIC-NONMEMBER")
    else:
        pseudo = object.__new__(enum_type)
    _member_precondition(pseudo, enum_type, declared)
    return pseudo


def _assert_declared_names(contract, dependency):
    """Literal catalog oracle, not values inferred from subject decisions."""
    for enum_type, names in (
        (contract.CaptureBoundary, EXPECTED_BOUNDARIES),
        (contract.CaptureIncompleteCause, EXPECTED_CAUSES),
        (dependency.InvocationState, EXPECTED_STATES),
    ):
        _check(tuple(member.name for member in enum_type) == names)
        _check(all(member.value == name for member, name in zip(enum_type, names)))


def _pseudo_setup(contract, dependency, target, revalidate, *, control=False):
    """Return the SUT action only after setup/preconditions have succeeded."""
    types = {
        "BOUNDARY": (contract.CaptureBoundary, EXPECTED_BOUNDARIES),
        "CAUSE": (contract.CaptureIncompleteCause, EXPECTED_CAUSES),
        "PRIOR": (dependency.InvocationState, EXPECTED_STATES),
    }
    enum_type, names = types[target]
    declared = tuple(getattr(enum_type, name) for name in names)
    if control:
        value = declared[0]
    else:
        value = _allocate_pseudo(enum_type, declared, string_base=(target == "PRIOR"))
    if not revalidate:
        if target == "BOUNDARY":
            action = lambda: _reference(contract, boundary=value)
            def oracle(result):
                _check(type(result) is contract.CapturedReference)
                _check(result.boundary is value)
                _check(type(result.actual_source_identity) is str)
                _check(result.actual_source_identity == "SYNTHETIC-SOURCE-ROLE-ONLY")
                _check(result.raw_value is None)
                _check(result.raw_type is type(None))
            return PreparedCall(action, oracle if control else None)
        if target == "CAUSE":
            materials = _materials(contract, dependency)
            material_oracle = _material_identity_oracle(contract, dependency, materials)
            action = lambda: contract.IncompleteCapture(materials, "SYNTHETIC-STAGE", value)
            def oracle(result):
                _check(type(result) is contract.IncompleteCapture)
                material_oracle(result.materials)
                _check(type(result.stage) is str)
                _check(result.stage == "SYNTHETIC-STAGE")
                _check(result.cause is value)
            return PreparedCall(action, oracle if control else None)
        # GateDecision does not reject this itself. Materials is the subject.
        prior = _prior(dependency, state=value)
        prior_fields = (prior.state, prior.reason_code, prior.audit_correlation_id,
                        prior.permitted_write_namespaces)
        binding = _binding(contract)
        acquired = ()
        action = lambda: contract.CaptureMaterials(binding, acquired, prior)
        def oracle(result):
            _check(type(result) is contract.CaptureMaterials)
            _check(result.invocation is binding)
            _check(result.acquired is acquired)
            _check(result.prior_decision is prior)
            _check(result.prior_decision.state is value)
            for actual, saved in zip((prior.state, prior.reason_code, prior.audit_correlation_id,
                                      prior.permitted_write_namespaces), prior_fields):
                _check(actual is saved)
        return PreparedCall(action, oracle if control else None)
    result = _incomplete(
        contract, dependency,
        ("PROJECT",) if target == "BOUNDARY" else (),
        with_prior=(target == "PRIOR"),
    )
    if target == "BOUNDARY":
        object.__setattr__(result.materials.acquired[0], "boundary", value)
    elif target == "CAUSE":
        object.__setattr__(result, "cause", value)
    else:
        object.__setattr__(result.materials.prior_decision, "state", value)
    oracle = _result_identity_oracle(contract, dependency, result) if control else None
    return PreparedCall(lambda: contract.validate_capture_result(result), oracle)


def _recipe_catalog(contract, dependency) -> tuple[CaseRecipe, ...]:
    """Private synthetic catalog for C01-C12, NOT the 189-item input oracle.

    Building this catalog is itself runtime setup and is not authorized now.
    There is no automatic invocation from imports, main or run_validation.
    """
    _assert_declared_names(contract, dependency)
    recipes = []

    def add(case_id, group, setup, error=None, arguments=None, oracle=None):
        def prepare():
            product = setup()
            if type(product) is PreparedCall:
                if oracle is not None:
                    raise PreparationBlocked("CONFLICTING_PREPARED_ORACLE")
                return product
            return PreparedCall(product, oracle)
        recipes.append(CaseRecipe(case_id, group, prepare, error, arguments))

    class TextSubclass(str):
        pass

    class TupleSubclass(tuple):
        pass

    class ForeignResult:
        pass

    for field in ("variant_id", "attempt_id", "input_snapshot_sha256", "audit_correlation_id"):
        for label, value, error in (
            ("NONE", None, TypeError), ("BOOL", True, TypeError),
            ("SUBCLASS", TextSubclass("x"), TypeError),
            ("EMPTY", "", ValueError), ("SPACE", " \t", ValueError),
        ):
            add("C01-" + field + "-" + label, "C01",
                lambda f=field, v=value: lambda: _binding(contract, **{f: v}), error)
    for label, digest, error in (
        ("HEX64-LOWER", "a" * 64, None), ("HEX64-UPPER", "A" * 64, None),
        ("SHORT", "a" * 63, ValueError), ("LONG", "a" * 65, ValueError),
        ("NONHEX", "g" * 64, ValueError),
    ):
        add("C01-" + label, "C01",
            lambda d=digest: lambda: _binding(contract, input_snapshot_sha256=d), error,
            oracle=_binding_oracle(contract, digest) if error is None else None)

    for name in EXPECTED_BOUNDARIES:
        for label, raw in (("NONE", None), ("INT", 4), ("TEXT", "SYNTHETIC")):
            def setup(n=name, value=raw):
                reference = _reference(contract, n, value)
                materials = contract.CaptureMaterials(_binding(contract), (reference,), None)
                result = contract.IncompleteCapture(materials, "SYNTHETIC-STAGE", contract.CaptureIncompleteCause.NO_RETURN)
                identity_oracle = _result_identity_oracle(contract, dependency, result)
                def oracle(checked):
                    identity_oracle(checked)
                    _check(checked.materials.acquired[0] is reference)
                    _check(reference.raw_value is value)
                    _check(reference.raw_type is type(value))
                return PreparedCall(lambda: contract.validate_capture_result(result), oracle)
            add("C02-" + name + "-" + label, "C02", setup)
    for label, changes in (
        ("BOUNDARY-TEXT", {"boundary": "PROJECT"}),
        ("TYPE-NAME", {"raw_type": "NoneType"}),
        ("WRONG-TYPE", {"raw_type": str}),
        ("SOURCE-NONE", {"actual_source_identity": None}),
    ):
        add("C02-" + label, "C02", lambda c=changes: lambda: _reference(contract, **c), TypeError)
    for label, value in (("EMPTY", ""), ("SPACE", " \t")):
        add("C02-SOURCE-" + label, "C02",
            lambda v=value: lambda: _reference(contract, actual_source_identity=v), ValueError)

    for mask in range(8):
        names = tuple(name for index, name in enumerate(EXPECTED_BOUNDARIES) if mask & (1 << index))
        def setup(ns=names):
            binding = _binding(contract)
            records = tuple(_reference(contract, name, object()) for name in ns)
            saved_records = tuple((record.boundary, record.actual_source_identity,
                                   record.raw_value, record.raw_type) for record in records)
            def oracle(result):
                _check(type(result) is contract.CaptureMaterials)
                _check(result.invocation is binding)
                _check(result.acquired is records)
                _check(result.prior_decision is None)
                _check(len(result.acquired) == len(ns))
                for record, name, saved in zip(result.acquired, ns, saved_records):
                    _check(record.boundary is getattr(contract.CaptureBoundary, name))
                    _check(record.raw_type is object)
                    for actual, anchor in zip((record.boundary, record.actual_source_identity,
                                               record.raw_value, record.raw_type), saved):
                        _check(actual is anchor)
            return PreparedCall(lambda: contract.CaptureMaterials(binding, records, None), oracle)
        add("C03-SUBSET-" + str(mask), "C03", setup)
    for label, names in (
        ("DUPLICATE", ("PROJECT", "PROJECT")),
        ("REVERSED", ("PROVIDER", "PROJECT")),
        ("FOUR", ("PROJECT", "SESSION", "PROVIDER", "PROJECT")),
    ):
        def setup(ns=names):
            binding = _binding(contract)
            records = tuple(_reference(contract, name, object()) for name in ns)
            return lambda: contract.CaptureMaterials(binding, records, None)
        add("C03-" + label, "C03", setup, ValueError)
    for label, acquired in (("LIST", []), ("TUPLE-SUBCLASS", TupleSubclass())):
        def setup(value=acquired):
            binding = _binding(contract)
            return lambda: contract.CaptureMaterials(binding, value, None)
        add("C03-" + label, "C03", setup, TypeError)

    for name in EXPECTED_STATES:
        def setup(n=name):
            prior = _prior(dependency, n)
            saved = (prior.state, prior.reason_code, prior.audit_correlation_id,
                     prior.permitted_write_namespaces)
            materials = contract.CaptureMaterials(_binding(contract), (), prior)
            result = contract.IncompleteCapture(materials, "SYNTHETIC-STAGE",
                                                contract.CaptureIncompleteCause.NO_RETURN)
            identity_oracle = _result_identity_oracle(contract, dependency, result)
            def oracle(checked):
                identity_oracle(checked)
                _check(result.materials.prior_decision is prior)
                _check(prior.state is saved[0])
                _check(prior.reason_code is saved[1])
                _check(prior.audit_correlation_id is saved[2])
                _check(prior.permitted_write_namespaces is saved[3])
            return PreparedCall(lambda: contract.validate_capture_result(result), oracle)
        add("C04-STATE-" + name, "C04", setup)
    for label, changes, error in (
        ("STATE-TEXT", {"state": "BLOCKED"}, TypeError),
        ("REASON-BOOL", {"reason_code": True}, TypeError),
        ("REASON-EMPTY", {"reason_code": ""}, ValueError),
        ("CORRELATION-NONE", {"audit_correlation_id": None}, TypeError),
        ("CORRELATION-OTHER", {"audit_correlation_id": "SYNTHETIC-OTHER"}, ValueError),
        ("WRITES-LIST", {"permitted_write_namespaces": []}, TypeError),
        ("WRITES-SUBCLASS", {"permitted_write_namespaces": TupleSubclass()}, TypeError),
        ("WRITES-NONEMPTY", {"permitted_write_namespaces": ("FORBIDDEN",)}, ValueError),
    ):
        def setup(c=changes):
            prior = _prior(dependency, **c)
            binding = _binding(contract)
            return lambda: contract.CaptureMaterials(binding, (), prior)
        add("C04-" + label, "C04", setup, error)

    for name in ("BLOCKED", "REJECTED", "ELIGIBLE_FOR_MAPPING"):
        def setup(n=name):
            records = tuple(_reference(contract, boundary, None) for boundary in EXPECTED_BOUNDARIES)
            materials = contract.CaptureMaterials(_binding(contract), records, _prior(dependency, n))
            material_oracle = _material_identity_oracle(contract, dependency, materials)
            def oracle(result):
                _check(type(result) is contract.CompleteCaptureReturn)
                material_oracle(result.materials)
                _check(result.capture_completed is True)
                _check(result.cleanup_completed is True)
                _check(result.handoff_completed is True)
                _check(type(result.cleanup_basis_id) is str)
                _check(result.cleanup_basis_id == "SYNTHETIC-BASIS")
            return PreparedCall(
                lambda: contract.CompleteCaptureReturn(materials, True, True, True, "SYNTHETIC-BASIS"), oracle,
            )
        add("C05-STRUCTURAL-" + name, "C05", setup)
    for label, changes, error in (
        ("CAPTURE-FALSE", {"capture_completed": False}, ValueError),
        ("CLEANUP-FALSE", {"cleanup_completed": False}, ValueError),
        ("HANDOFF-FALSE", {"handoff_completed": False}, ValueError),
        ("CAPTURE-INT", {"capture_completed": 1}, TypeError),
        ("CLEANUP-INT", {"cleanup_completed": 1}, TypeError),
        ("HANDOFF-INT", {"handoff_completed": 1}, TypeError),
        ("BASIS-EMPTY", {"cleanup_basis_id": ""}, ValueError),
        ("BASIS-NONE", {"cleanup_basis_id": None}, TypeError),
    ):
        def setup(c=changes):
            fields = dict(materials=_materials(contract, dependency, EXPECTED_BOUNDARIES, True),
                          capture_completed=True, cleanup_completed=True,
                          handoff_completed=True, cleanup_basis_id="SYNTHETIC-BASIS")
            fields.update(c)
            return lambda: contract.CompleteCaptureReturn(**fields)
        add("C05-" + label, "C05", setup, error)
    for count in range(3):
        def setup(n=count):
            materials = _materials(contract, dependency, EXPECTED_BOUNDARIES[:n], True)
            return lambda: contract.CompleteCaptureReturn(materials, True, True, True, "SYNTHETIC-BASIS")
        add("C05-MISSING-" + str(count), "C05", setup, ValueError)
    def no_prior_setup():
        materials = _materials(contract, dependency, EXPECTED_BOUNDARIES)
        return lambda: contract.CompleteCaptureReturn(materials, True, True, True, "SYNTHETIC-BASIS")
    add("C05-NO-PRIOR", "C05", no_prior_setup, ValueError)

    for name, exception_type in (("VALUE", ValueError), ("INTERRUPT", KeyboardInterrupt), ("EXIT", SystemExit)):
        def setup(kind=exception_type):
            original = kind()
            def oracle(occurrence):
                _check(type(occurrence) is contract.FailureOccurrence)
                _check(occurrence.error is original)
                _check(type(occurrence.stage) is str)
                _check(occurrence.stage == "SYNTHETIC-STAGE")
            return PreparedCall(lambda: contract.FailureOccurrence("SYNTHETIC-STAGE", original), oracle)
        add("C06-" + name, "C06", setup)
    for label, error_value in (("CLASS", ValueError), ("TEXT", "SYNTHETIC"), ("NONE", None)):
        add("C06-NONEXCEPTION-" + label, "C06",
            lambda v=error_value: lambda: contract.FailureOccurrence("SYNTHETIC-STAGE", v), TypeError)

    for count in range(4):
        for mode in ("PRIMARY", "CLEANUP", "BOTH", "SHARED"):
            def setup(n=count, selected=mode):
                materials = _materials(contract, dependency, EXPECTED_BOUNDARIES[:n])
                first_error, second_error = ValueError(), TypeError()
                first = contract.FailureOccurrence("SYNTHETIC-PRIMARY", first_error)
                second = contract.FailureOccurrence("SYNTHETIC-CLEANUP",
                                                    first_error if selected == "SHARED" else second_error)
                primary = None if selected == "CLEANUP" else first
                cleanup = None if selected == "PRIMARY" else second
                material_oracle = _material_identity_oracle(contract, dependency, materials)
                def oracle(result):
                    _check(type(result) is contract.CaptureFailure)
                    material_oracle(result.materials)
                    _check(result.primary_failure is primary)
                    _check(result.cleanup_failure is cleanup)
                    if primary is not None:
                        _check(primary.error is first_error)
                        _check(type(primary.stage) is str)
                        _check(primary.stage == "SYNTHETIC-PRIMARY")
                    if cleanup is not None:
                        _check(cleanup.error is (first_error if selected == "SHARED" else second_error))
                        _check(type(cleanup.stage) is str)
                        _check(cleanup.stage == "SYNTHETIC-CLEANUP")
                    if selected == "SHARED":
                        _check(result.primary_failure.error is result.cleanup_failure.error)
                return PreparedCall(lambda: contract.CaptureFailure(materials, primary, cleanup), oracle)
            add("C07-" + str(count) + "-" + mode, "C07", setup)
    def no_errors_setup():
        materials = _materials(contract, dependency)
        return lambda: contract.CaptureFailure(materials, None, None)
    add("C07-NO-ERRORS", "C07", no_errors_setup, ValueError)

    for name in EXPECTED_CAUSES:
        for count in range(4):
            def setup(n=count, selected=name):
                materials = _materials(contract, dependency, EXPECTED_BOUNDARIES[:n])
                cause = getattr(contract.CaptureIncompleteCause, selected)
                action = lambda: contract.IncompleteCapture(materials, "SYNTHETIC-STAGE", cause)
                if selected == "MISSING_OBSERVATION" and n == 3:
                    return PreparedCall(action)
                material_oracle = _material_identity_oracle(contract, dependency, materials)
                def oracle(result):
                    _check(type(result) is contract.IncompleteCapture)
                    material_oracle(result.materials)
                    _check(type(result.stage) is str)
                    _check(result.stage == "SYNTHETIC-STAGE")
                    _check(result.cause is cause)
                    _check(len(result.materials.acquired) == n)
                return PreparedCall(action, oracle)
            expected = ValueError if name == "MISSING_OBSERVATION" and count == 3 else None
            add("C08-" + name + "-" + str(count), "C08", setup, expected)

    for label, foreign in (("DICT", {}), ("FOREIGN", ForeignResult())):
        add("C09-" + label, "C09", lambda v=foreign: lambda: contract.validate_capture_result(v), TypeError)
    def material_only_setup():
        value = _materials(contract, dependency)
        return lambda: contract.validate_capture_result(value)
    add("C09-MATERIALS-ONLY", "C09", material_only_setup, TypeError)
    def subclass_setup():
        class ResultSubclass(contract.IncompleteCapture):
            pass
        # Bypass this subclass's inherited rejecting post-init in SETUP.
        value = object.__new__(ResultSubclass)
        return lambda: contract.validate_capture_result(value)
    add("C09-RESULT-SUBCLASS", "C09", subclass_setup, TypeError)
    for kind in ("COMPLETE", "FAILURE", "INCOMPLETE"):
        def setup(selected=kind):
            if selected == "COMPLETE":
                materials = _materials(contract, dependency, EXPECTED_BOUNDARIES, True)
                result = contract.CompleteCaptureReturn(materials, True, True, True, "SYNTHETIC-BASIS")
            elif selected == "FAILURE":
                materials = _materials(contract, dependency, EXPECTED_BOUNDARIES, True)
                error = ValueError()
                primary = contract.FailureOccurrence("SYNTHETIC-PRIMARY", error)
                cleanup = contract.FailureOccurrence("SYNTHETIC-CLEANUP", error)
                result = contract.CaptureFailure(materials, primary, cleanup)
            else:
                result = _incomplete(contract, dependency, ("SESSION",), True)
            oracle = _result_identity_oracle(contract, dependency, result)
            return PreparedCall(lambda: contract.validate_capture_result(result), oracle)
        add("C09-REVALIDATE-" + kind, "C09", setup)

    for name in ("CaptureInvocationBinding", "CapturedReference", "CaptureMaterials",
                 "CompleteCaptureReturn", "FailureOccurrence", "CaptureFailure", "IncompleteCapture"):
        add("C10-CONSTRUCTOR-MISSING-" + name, "C10",
            lambda n=name: lambda: getattr(contract, n)(), TypeError)
    for field in ("materials", "stage", "cause"):
        def setup(missing=field):
            value = _incomplete(contract, dependency)
            object.__delattr__(value, missing)
            return lambda: contract.validate_capture_result(value)
        add("C10-REVALIDATE-MISSING-" + field, "C10", setup, ValueError)

    for target in ("BOUNDARY", "CAUSE", "PRIOR"):
        for revalidate in (False, True):
            phase = "REVALIDATE" if revalidate else "CONSTRUCT"
            for control in (False, True):
                label = "CONTROL" if control else "PSEUDO"
                add("C11-" + target + "-" + phase + "-" + label, "C11",
                    lambda t=target, r=revalidate, c=control: _pseudo_setup(contract, dependency, t, r, control=c),
                    None if control else ValueError, None if control else GUARD_ARGS[target])

    def shallow_setup():
        original = []
        reference = _reference(contract, value=original)
        materials = contract.CaptureMaterials(_binding(contract), (reference,), None)
        result = contract.IncompleteCapture(materials, "SYNTHETIC-STAGE", contract.CaptureIncompleteCause.NO_RETURN)
        original.append("SYNTHETIC-CHANGED")
        identity_oracle = _result_identity_oracle(contract, dependency, result)
        def oracle(checked):
            identity_oracle(checked)
            _check(checked.materials.acquired[0].raw_value is original)
            _check(len(original) == 1)
        return PreparedCall(lambda: contract.validate_capture_result(result), oracle)
    add("C12-SHALLOW-FREEZE-LIMITATION", "C12", shallow_setup)
    identifiers = tuple(recipe.case_id for recipe in recipes)
    _check(len(set(identifiers)) == len(identifiers))
    _check(identifiers == DECLARED_CASE_IDS)
    return tuple(recipes)


@dataclass(slots=True, eq=False, repr=False)
class ReferenceLoadReceipt:
    """Private same-process anchors only; mutable state is not sealed evidence."""

    owned_slots: list
    stage: str
    original_error: BaseException | None


@dataclass(slots=True, eq=False, repr=False)
class ReferenceBatch:
    """Private bridge context; never a grant or a cross-process result."""

    contract: object
    dependency: object
    recipes: tuple
    next_index: int = 0
    stopped: bool = False
    observations: tuple = ()
    interruption: BaseException | None = None
    dispatch_error: BaseException | None = None


_HELD_REFERENCE_BATCHES = []
_HELD_BRIDGE_ERRORS = []


def _prepare_fixed_batch_reference(dependency_bytes: bytes, contract_bytes: bytes):
    """Local-synthetic bridge: fixed bytes -> unique loader -> native recipes."""
    _require_execution_binding()
    phase = "REFERENCE_MODULE_LOAD"
    try:
        contract, dependency = _load_reference_modules(dependency_bytes, contract_bytes)
        phase = "DIRECTORY_SETUP"
        recipes = _recipe_catalog(contract, dependency)
        _check(type(recipes) is tuple and len(recipes) == 158)
        _check(tuple(recipe.case_id for recipe in recipes) == DECLARED_CASE_IDS)
        _check(sum(recipe.expected_exception is None for recipe in recipes) == 79)
        _check(sum(recipe.expected_exception is not None for recipe in recipes) == 79)
        batch = ReferenceBatch(contract, dependency, recipes)
        _HELD_REFERENCE_BATCHES.append(batch)
        return batch
    except BaseException as original:
        _HELD_BRIDGE_ERRORS.append((phase, original))
        raise


def _next_fixed_case_reference(batch: ReferenceBatch) -> CaseObservation:
    """Serial progression; no arbitrary ID/action/oracle supplied."""
    _require_execution_binding()
    owned = False
    try:
        if type(batch) is not ReferenceBatch or not any(
                batch is held for held in _HELD_REFERENCE_BATCHES):
            raise PreparationBlocked("UNOWNED_REFERENCE_BATCH")
        owned = True
        _assert_current_carrier_identity()
        if (batch.stopped or type(batch.next_index) is not int
                or not 0 <= batch.next_index < len(DECLARED_CASE_IDS)):
            raise PreparationBlocked("NO_NEXT_CASE_DISPATCH")
        recipe = batch.recipes[batch.next_index]
        _check(type(recipe) is CaseRecipe)
        _check(recipe.case_id == DECLARED_CASE_IDS[batch.next_index])
        observation = _exercise_recipe(recipe)
        # Keep actual observation/error references before metadata conversion.
        batch.observations += (observation,)
        batch.next_index += 1
        if observation.determination != "PASS":
            batch.stopped = True
        return observation
    except BaseException as original:
        _HELD_BRIDGE_ERRORS.append(("REFERENCE_DISPATCH", original))
        if owned:
            batch.dispatch_error = original
            batch.stopped = True
            if isinstance(original, (KeyboardInterrupt, SystemExit)):
                batch.interruption = original
        raise


def _minimal_report_frame_reference(ordinal: int, observation: CaseObservation) -> bytes:
    """Pure six-field ASCII frame, not IPC or authentication.

    One frame is bounded by the proposed 4KiB ceiling. No original object,
    exception, source bytes, message, repr or traceback is serialized.
    Ordinal is local report order, not an authorization or temporal fact.
    """
    qualification, phase, determination = classify_report_only(observation)
    if (type(ordinal) is not int or not 1 <= ordinal <= len(DECLARED_CASE_IDS)
            or observation.case_id != DECLARED_CASE_IDS[ordinal - 1]):
        raise PreparationBlocked("REPORT_ORDER_MISMATCH")
    text = "|".join(("DSP004-CAPTURE-V1", str(ordinal), observation.case_id,
                     phase, determination, qualification)) + "\n"
    frame = text.encode("ascii", errors="strict")
    if len(frame) > CONTROL_FRAME_LIMIT:
        raise PreparationBlocked("REPORT_FRAME_OVERFLOW")
    return frame


@dataclass(frozen=True, slots=True, eq=False, repr=False)
class ProposedDeadlines:
    """Pure proposed arithmetic, never an actual clock or stop mechanism."""

    t0: float
    work: float
    hard: float

    def __post_init__(self) -> None:
        _finite_time(self.t0)
        _finite_time(self.work)
        _finite_time(self.hard)
        if (self.work != _advance(self.t0, 60.0)
                or self.hard != _advance(self.t0, 70.0) or self.hard <= self.work):
            raise PreparationBlocked("INCONSISTENT_PROPOSED_DEADLINES")

    def case(self, start: float) -> float:
        return min(self._advance_from(start, 2.0), self.work, self.hard)

    def terminate(self, start: float) -> float:
        return min(self._advance_from(start, 5.0), self.hard)

    def cleanup(self, start: float) -> float:
        return min(self._advance_from(start, 5.0), self.hard)

    def _advance_from(self, start: float, seconds: float) -> float:
        start = _finite_time(start)
        if start < self.t0:
            raise PreparationBlocked("TIME_PRECEDES_EXTERNAL_T0")
        # A deadline already in the past is not reset into a new valid window.
        return _advance(start, seconds)


def _finite_time(value: float) -> float:
    if type(value) is not float or not isfinite(value):
        raise PreparationBlocked("FINITE_EXTERNAL_MONOTONIC_TIME_REQUIRED")
    return value


def _advance(start: float, seconds: float) -> float:
    start = _finite_time(start)
    if type(seconds) is not float or not isfinite(seconds) or seconds <= 0.0:
        raise PreparationBlocked("POSITIVE_NATIVE_DURATION_REQUIRED")
    result = start + seconds
    if not isfinite(result) or result <= start or result - start != seconds:
        raise PreparationBlocked("UNREPRESENTABLE_DEADLINE_INCREMENT")
    return result


def proposed_deadlines(t0: float) -> ProposedDeadlines:
    """T0 must precede this batch's reads/hash/IPC/spawn, supplied externally.

    Policy proposal only: 60 work / 2 case / 5 terminate / 5 cleanup / 70 hard.
    No hidden elapsed-time reset or automatic acceptance of these budgets.
    Expiry, late scheduling and inability to stop remain external failures.
    """
    t0 = _finite_time(t0)
    return ProposedDeadlines(t0, _advance(t0, 60.0), _advance(t0, 70.0))


def classify_report_only(observation: CaseObservation) -> tuple[str, str, str]:
    """Pure logical metadata check, NOT a private-channel implementation.

    Content remains carrier-self-reported and UNVERIFIED even when structurally
    acceptable. No process/exit/sequence check can independently certify it.
    Original errors are intentionally not copied into the returned tuple.
    """
    if type(observation) is not CaseObservation:
        raise PreparationBlocked("NATIVE_OBSERVATION_REQUIRED")
    if type(observation.case_id) is not str or observation.case_id not in DECLARED_CASE_IDS:
        raise PreparationBlocked("UNBOUND_CASE_IDENTIFIER")
    if type(observation.phase) is not str or observation.phase not in ("SETUP", "SUT", "ORACLE"):
        raise PreparationBlocked("UNKNOWN_PHASE")
    if (type(observation.determination) is not str
            or observation.determination not in ("PASS", "FAIL", "NOT_EVALUABLE")):
        raise PreparationBlocked("UNKNOWN_DETERMINATION")
    if (observation.phase == "SETUP" and observation.determination != "NOT_EVALUABLE"
            or observation.phase != "SETUP" and observation.determination == "NOT_EVALUABLE"):
        raise PreparationBlocked("INVALID_PHASE_DETERMINATION_PAIR")
    return "UNVERIFIED_REPORT", observation.phase, observation.determination


# Private local-synthetic protocol; never a formal admission or public service.
# These exact ASCII contracts must match the separately pinned supervisor.
_READY_FRAME = b"DSP004-READY-V1|158|UNVERIFIED_REPORT\n"
_END_FRAME = b"DSP004-END-V1|158|UNVERIFIED_REPORT\n"
_STOP_COMMAND = b"DSP004-COMMAND-V1|STOP\n"
_STOPPED_FRAME = b"DSP004-STOPPED-V1|UNVERIFIED_REPORT\n"
_HELD_CONTROL_RECEIPTS = []


@dataclass(slots=True, eq=False, repr=False)
class PrivateControlReceipt:
    """Strong references only within this child; not trusted peer evidence."""

    batch: ReferenceBatch
    command: object
    report: object
    stage: str = "RESERVED"
    stopped: bool = False
    dispatch_attempted: int = 0
    reported: int = 0
    command_eof: bool = False
    original_error: BaseException | None = None


def _read_private_frame_reference(stream: FileIO) -> bytes:
    _require_execution_binding()
    if type(stream) is not FileIO:
        raise PreparationBlocked("NATIVE_COMMAND_FILEIO_REQUIRED")
    data = bytearray()
    while len(data) < CONTROL_FRAME_LIMIT:
        piece = stream.read(1)
        if type(piece) is not bytes or len(piece) != 1:
            # Includes EOF, None from nonblocking I/O and impossible over-read.
            raise PreparationBlocked("COMMAND_EOF_OR_INCOMPLETE")
        data.extend(piece)
        if piece == b"\n":
            return bytes(data)
        if not 33 <= piece[0] <= 126:
            raise PreparationBlocked("COMMAND_NONCANONICAL_ASCII")
    raise PreparationBlocked("COMMAND_FRAME_OVERFLOW")


def _write_private_frame_reference(stream: FileIO, frame: bytes) -> None:
    _require_execution_binding()
    if (type(stream) is not FileIO or type(frame) is not bytes
            or not 1 <= len(frame) <= CONTROL_FRAME_LIMIT or not frame.endswith(b"\n")):
        raise PreparationBlocked("PRIVATE_REPORT_FRAME_UNBOUND")
    offset = 0
    while offset < len(frame):
        count = stream.write(frame[offset:])
        if type(count) is not int or not 1 <= count <= len(frame) - offset:
            raise PreparationBlocked("REPORT_WRITE_INCOMPLETE")
        offset += count
    # A returned write is not remote receipt, durable storage or peer proof.


def _serve_private_control_reference(batch: ReferenceBatch, command: FileIO,
                                     report: FileIO) -> PrivateControlReceipt:
    """Serial local-synthetic native execution; basis required before I/O.

    One report follows one NEXT; no parallel dispatch or arbitrary recipe IDs.
    STOP after a non-PASS is allowed, NEXT is not. STOP requires actual EOF on
    the command stream before STOPPED. That read can block: outside control
    must retain ownership and stop on deadline, never call it safe cleanup.
    """
    _require_execution_binding()
    if (type(batch) is not ReferenceBatch
            or not any(batch is held for held in _HELD_REFERENCE_BATCHES)):
        raise PreparationBlocked("UNOWNED_CONTROL_BATCH")
    if (type(command) is not FileIO or type(report) is not FileIO
            or command is report or command.fileno() == report.fileno()
            or not command.readable() or command.writable()
            or not report.writable() or report.readable()):
        raise PreparationBlocked("PRIVATE_CONTROL_ENDPOINTS_UNBOUND")
    if (batch.next_index != 0 or batch.stopped
            or any(held.batch is batch for held in _HELD_CONTROL_RECEIPTS)):
        raise PreparationBlocked("CONTROL_BATCH_ALREADY_USED")
    receipt = PrivateControlReceipt(batch, command, report)
    _HELD_CONTROL_RECEIPTS.append(receipt)  # Before the first control I/O.
    try:
        receipt.stage = "READY_WRITE"
        _write_private_frame_reference(report, _READY_FRAME)
        while True:
            receipt.stage = "COMMAND_READ"
            frame = _read_private_frame_reference(command)
            if frame == _STOP_COMMAND:
                receipt.stopped = True
                batch.stopped = True
                receipt.stage = "COMMAND_EOF"
                tail = command.read(1)
                if type(tail) is not bytes or tail != b"":
                    raise PreparationBlocked("COMMAND_AFTER_STOP_OR_EOF_UNCONFIRMED")
                receipt.command_eof = True
                receipt.stage = "STOPPED_WRITE"
                _write_private_frame_reference(report, _STOPPED_FRAME)
                receipt.stage = "STOPPED_REPORTED_UNVERIFIED"
                return receipt
            if receipt.stopped or batch.stopped or batch.next_index >= len(DECLARED_CASE_IDS):
                raise PreparationBlocked("NEXT_AFTER_STOP_FAILURE_OR_END")
            ordinal = batch.next_index + 1
            expected = ("DSP004-COMMAND-V1|NEXT|" + str(ordinal) + "|"
                        + DECLARED_CASE_IDS[ordinal - 1] + "\n").encode("ascii")
            if frame != expected:
                raise PreparationBlocked("COMMAND_ORDER_OR_ID_MISMATCH")
            receipt.stage = "NATIVE_DISPATCH"
            receipt.dispatch_attempted = ordinal  # BEFORE native SETUP/SUT.
            observation = _next_fixed_case_reference(batch)
            receipt.stage = "REPORT_WRITE"
            _write_private_frame_reference(
                report, _minimal_report_frame_reference(ordinal, observation))
            receipt.reported = ordinal
            if observation.determination != "PASS":
                receipt.stopped = True
                # Retain observation and original error in batch. Only STOP now.
            elif batch.next_index == len(DECLARED_CASE_IDS):
                receipt.stage = "END_WRITE"
                _write_private_frame_reference(report, _END_FRAME)
                receipt.stopped = True
    except BaseException as original:
        receipt.original_error = original
        receipt.stopped = True
        batch.stopped = True
        _HELD_BRIDGE_ERRORS.append(("PRIVATE_CONTROL", original))
        if isinstance(original, (KeyboardInterrupt, SystemExit)):
            batch.interruption = original
        raise




def _native_synthetic_supplement(batch: ReferenceBatch) -> int:
    """Eight fixed in-process checks, separate from the preserved 158 catalog.

    They check ORIGINAL exception identity and failure routing, not real sources.
    These are new test inputs under this batch; they do not rewrite the catalog.
    """
    _require_execution_binding()
    count = 0
    for kind in (KeyboardInterrupt, SystemExit):
        original = kind()
        def action(error=original):
            raise error
        recipe = CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT",
                            lambda a=action: PreparedCall(a, lambda result: None), None)
        try:
            _exercise_recipe(recipe)
        except BaseException as observed:
            _check(observed is original)
            count += 1
        else:
            raise OracleMismatch("REAL_INTERRUPT_WAS_NOT_RERAISED")

    setup_error = TypeError("SYNTHETIC-SETUP")
    def bad_setup():
        raise setup_error
    recipe = CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT", bad_setup, TypeError)
    observed = _exercise_recipe(recipe)
    _check(observed.phase == "SETUP" and observed.determination == "NOT_EVALUABLE")
    _check(observed.original_error is setup_error)
    count += 1

    oracle_error = ValueError("SYNTHETIC-ORACLE")
    def bad_oracle(result):
        raise oracle_error
    recipe = CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT",
                        lambda: PreparedCall(lambda: None, bad_oracle), None)
    observed = _exercise_recipe(recipe)
    _check(observed.phase == "ORACLE" and observed.determination == "FAIL")
    _check(observed.original_error is oracle_error)
    count += 1

    unexpected = ValueError("SYNTHETIC-WRONG-TYPE")
    def wrong_exception():
        raise unexpected
    recipe = CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT",
                        lambda: PreparedCall(wrong_exception), TypeError)
    observed = _exercise_recipe(recipe)
    _check(observed.phase == "SUT" and observed.determination == "FAIL")
    _check(observed.original_error is unexpected)
    count += 1

    stopped = ReferenceBatch(batch.contract, batch.dependency, (
        CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT", bad_setup, TypeError),))
    _HELD_REFERENCE_BATCHES.append(stopped)
    observed = _next_fixed_case_reference(stopped)
    _check(stopped.stopped and observed.determination == "NOT_EVALUABLE")
    _check(stopped.observations[0] is observed and observed.original_error is setup_error)
    count += 1
    try:
        _next_fixed_case_reference(stopped)
    except PreparationBlocked as original:
        _check(stopped.dispatch_error is original)
        _check(stopped.next_index == 1 and len(stopped.observations) == 1)
        count += 1
    else:
        raise OracleMismatch("DISPATCH_AFTER_FAILURE")

    interruption = KeyboardInterrupt()
    def interrupt_action():
        raise interruption
    interrupted = ReferenceBatch(batch.contract, batch.dependency, (
        CaseRecipe(DECLARED_CASE_IDS[0], "SUPPLEMENT",
                   lambda: PreparedCall(interrupt_action, lambda result: None), None),))
    _HELD_REFERENCE_BATCHES.append(interrupted)
    try:
        _next_fixed_case_reference(interrupted)
    except KeyboardInterrupt as original:
        _check(original is interruption and interrupted.interruption is original)
        _check(interrupted.stopped and interrupted.next_index == 0)
        _check(interrupted.dispatch_error is original)
        count += 1
    else:
        raise OracleMismatch("REAL_BATCH_INTERRUPT_WAS_NOT_RERAISED")
    _check(count == 8)
    return count


if __name__ == "__main__":
    raise SystemExit(main())
