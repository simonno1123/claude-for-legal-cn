"""DSP-004 capture-result validation carrier candidate, REV2.

AUTHORIZED SCOPE: TWO NEW SOURCES AND INDEPENDENT STATIC REVIEW ONLY.
No loading, compilation, tests, environment probing, source admission,
actual capture or integration is authorized by source materialization.
The accepted REV1 and every accepted dependency remain unchanged.

Predecessor source SHA-256:
2C03E9D87BB747A58491CB3B992780FE4252ABDDCF4F35B1A2BC4F0078C4E942
Its 158-case C01-C12 directory, recipes, native oracles, exception handling,
proposed arithmetic and report-only classifier are preserved as source text.
They remain NOT_RUN. They neither replace nor complete the separate 189-item
input plan. Initial REV1 failures and all subsequent reviews remain history.

Fixed contract: E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C
Fixed dependency: 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4
Design basis: the conversation-level executor-handoff design REV2 and its
independent read-only review. No physical SHA is assigned to that design,
and this source does not declare its acceptance by the Project Owner.

EXECUTION IS CLOSED. run_validation, the sole B/A loader and the reference
batch bridge all hit an unconditional refusal before side effects. main
silently returns 78. There is no boolean grant, CLI switch, callback, path
override, reusable approval token or enabling setter. A later separately
authorized and independently reviewed revision/driver contract must supply
the missing execution facts; a run authorization alone cannot fill them.
Calling private reference helpers or patching this gate is a boundary bypass,
not permission. These Python controls are not a security sandbox.

This new module owns only the fixed package/B/A slots on its closed reference
path. A future fixed bootstrap must first register THIS module under its exact
name, before executing its dataclass declarations. It must not pre-load B/A,
invoke the accepted REV1 loader, clear foreign slots, or retry a partial load.
Owned module identities and actual load exceptions are retained privately in
a receipt before execution, without claiming cleanup or trusted resolution.

The reference bridge separates SETUP, SUT and ORACLE, keeps native objects
in-process, latches failures, and describes a minimal bounded report frame.
An expected negative requires the exact bound exception type; args are checked
only where the preserved recipe has expected_args. Real KeyboardInterrupt and
SystemExit abort and remain original objects, not expected-rejection success.
Frames are UNVERIFIED_REPORT only. Serialization is not channel authentication.

LIMITED L1: exact interpreter/bootstrap and recursive dependency origins,
fixed resolver, roots/read authority, module source identity and same-byte
physical handoff are unbound. Same bytes do not make the environment trusted.
LIMITED L2: 158 recipes including pseudo-member allocation are not verified in
a bound interpreter; coverage/oracle admission remains pending.
LIMITED L3: private IPC, zero-body stdout/stderr control before startup, real
monotonic timing, process scope, stopping and cleanup are NOT implemented by
this Python source. The sibling supervisor candidate also refuses startup.
4KiB is a proposed report-buffer ceiling, not a physical channel guarantee.
60/2/5/5/70 seconds remain proposed arithmetic, not hard-stop capability.
C13 real load-failure runs and C14 physical supervision remain NOT_IMPLEMENTED.

Actual raw values, invalid original Gates and errors require private in-process
retention; no JSON/pickle/repr, traceback export, durable exception storage or
cross-process identity preservation is offered. Failed-load receipts are not
cleanup certificates; interruption or process termination can lose memory.
Closing a channel is not destruction; no zero-disclosure guarantee is made.

DSP-004 remains OPEN / HOLD; B-01 and B-02 remain OPEN. All LIMITED and historical
failures are retained. No aggregate privacy/security/legal verdict, finding,
register, governance acceptance, runtime grant or automatic transition exists.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from importlib.machinery import ModuleSpec
from math import isfinite
from types import FunctionType, ModuleType
import sys


CONTRACT_SHA256 = "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C"
DEPENDENCY_SHA256 = "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"
PACKAGE_NAME = "route_b_c03"
DEPENDENCY_NAME = "route_b_c03.contracts"
CONTRACT_NAME = "DSP_004_CAPTURE_RESULT_CONTRACT_CANDIDATE_REV1"
CARRIER_MODULE_NAME = "DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV2"
PREDECESSOR_SHA256 = "2C03E9D87BB747A58491CB3B992780FE4252ABDDCF4F35B1A2BC4F0078C4E942"
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


def _require_execution_binding() -> None:
    # No accepting branch and no caller-supplied grant. Missing facts stay missing.
    raise PreparationBlocked("EXECUTION_BINDINGS_NOT_ESTABLISHED")


def run_validation() -> None:
    """No loading, setup, hashing, clocks, processes or tests are started."""
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
    """One CLOSED owner for B/A; no accepted REV1 import or preloading.

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
    """CLOSED bridge: source bytes -> unique loader -> fixed native recipes."""
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
    """CLOSED serial progression; no arbitrary ID/action/oracle supplied."""
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


if __name__ == "__main__":
    raise SystemExit(main())
