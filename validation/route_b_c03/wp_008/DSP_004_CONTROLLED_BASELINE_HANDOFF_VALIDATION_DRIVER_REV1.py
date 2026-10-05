"""DSP-004 controlled handoff validation driver, REV1 source candidate only.

Source formation is not review, acceptance, source admission, or run permission.
This file has no automatic entry, launcher, subprocess, output, or file writer.
The accepted caller, reader, and synthetic baseline must remain unchanged.

Before loading this driver, an independently authorized controller must bind
its complete physical SHA, actual interpreter identity/version, dependency
origins, startup code, purpose, and individual case permissions. It must verify
and consume the same driver bytes, not hash a path and reopen it for execution.
The trusted starting point is external; this candidate cannot attest its own
authority, environment, or hash. No historical Python version is presumed.

The controller must establish stdout/stderr control before interpreter startup
and early imports, use the separately bound -I -S -B startup conditions, and
terminate each dedicated process after one case. Checking those flags here is
only a minimum technical check, not environmental binding or a security sandbox.
The controller, not this file, enforces whole-batch scope and STOP_BATCH results.
There is no next-case dispatch, automatic retry, or reload-to-reset permission.

Each case loads the fixed caller from one checked bytes snapshot into an
unregistered ModuleType namespace. No ordinary import, runpy, file loader,
cached caller, source patch, or caller-global replacement is used. Preflight
checks of reader/baseline bytes are distinct from the caller's own later reads.
They do not prove same-call causality, real source trust, or zero I/O effects.

Full-entry assertions observe literal record shape/order/values and the reader
slot after return. Original tuple/element identity and same-bytes consumption
remain source-level observations where there is no runtime observer. The hash
negative case calls only the actual private helper with a local NON-ASSET stub;
it does not inject the stub into the full entry. Slot fixtures and helper probes
require their own exact permission before invocation. Their synthetic facts
are not full-entry failure, historical registration, or source-admission facts.

The coexistence probe constructs the actual loaded carrier with two synthetic
BaseException objects. It does not trigger an actual double-failure workflow.
Full-entry SHA rejection, injected initialization/extraction/cleanup failures,
second-entry rejection, and extreme interruption remain UNEXERCISED here.

Only allowlisted minimal case/status codes are returned. No records, input
bytes, original messages, tracebacks, or exception representations are output.
Actual exception objects remain in private process memory; retaining or dropping
references is not a destruction, confidentiality, or zero-disclosure guarantee.
Unexpected errors, assertion failures, asset drift, or unbound prerequisites
stop the case/batch; they are never counted as expected rejection success.
Forced termination, repeated interruption, and early-startup output remain
external limitations, not silently repaired by this candidate.

Inherited registration-history/cleanup observation limits and upstream item 8
LIMITED remain. DSP-004 stays OPEN/HOLD; B-01/B-02 stay OPEN. This source does
not create an evidence ledger, acceptance archive, actual capture, integration,
provider/Gate invocation, formal findings, or an overall project PASS.
"""

from hashlib import sha256
from pathlib import Path
import sys
from types import FunctionType, ModuleType


_CALLER_PATH = Path(
    "C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/"
    "validation/route_b_c03/wp_008/"
    "DSP_004_CONTROLLED_BASELINE_HANDOFF_CALLER_CANDIDATE_REV1.py"
)
_READER_PATH = Path(
    "C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/"
    "validation/route_b_c03/wp_008/"
    "DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py"
)
_BASELINE_PATH = Path(
    "C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/"
    "docs/phase2/route-b/"
    "TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md"
)
_CALLER_SHA256 = "EF554C3051318BD305EDE6B8511C433C1BB9E20B10E93E5FB5F71C9AFF7A7E63"
_READER_SHA256 = "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"
_BASELINE_SHA256 = "BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368"
_CALLER_MODULE_NAME = "dsp004_baseline_handoff_caller_controlled_entry_rev1"
_READER_MODULE_NAME = "dsp004_reader_controlled_entry_rev1"
_FIELD_NAMES = (
    "source_role", "candidate_source_identity", "record_locator", "expected_reference"
)

# Independently fixed literal oracle from the synthetic baseline, never derived
# from the entry's returned records. No actual provider/session data is captured.
_EXPECTED_RECORD_FIELDS = (
    (
        "SRC004-E-PROJECT",
        "DSP004-EXPECTED-PROJECT-V1",
        "本文件第 3.1 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-PROJECT-001",
    ),
    (
        "SRC004-E-SESSION",
        "DSP004-EXPECTED-SESSION-V1",
        "本文件第 3.2 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-SESSION-001",
    ),
    (
        "SRC004-E-PROVIDER",
        "DSP004-EXPECTED-PROVIDER-V1",
        "本文件第 3.3 节，Field = Expected Reference 的唯一表格行",
        "SYNTHETIC-PROVIDER-001",
    ),
)
_HASH_PROBE_PAYLOAD = b"DSP-004 SYNTHETIC / NON-ASSET hash refusal probe REV1\n"
_CASE_LEVELS = {
    "FULL_ENTRY_LITERAL_RECORDS": "FULL_ENTRY_LOCAL_OBSERVATION",
    "FULL_ENTRY_OCCUPIED_SLOT": "FULL_ENTRY_PRECONDITION_REFUSAL",
    "HELPER_SYNTHETIC_SHA_REFUSAL": "NON_ASSET_PRIVATE_HELPER_PROBE",
    "HELPER_CLEAN_OWNED_SLOT": "SYNTHETIC_CLEANUP_HELPER_PROBE",
    "HELPER_CLEAN_MISSING_SLOT": "SYNTHETIC_CLEANUP_HELPER_PROBE",
    "HELPER_CLEAN_REPLACED_SLOT": "SYNTHETIC_CLEANUP_HELPER_PROBE",
    "HELPER_CLEAN_TABLE_IDENTITY": "SYNTHETIC_CLEANUP_HELPER_PROBE",
    "CARRIER_REFERENCE_CONSTRUCTION": "SYNTHETIC_CARRIER_CONSTRUCTION",
}
_DRIVER_ATTEMPT_USED = False
_RETAINED_ERRORS = []
_ACTIVE_PHASE = "NOT_STARTED"
_ABSENT = object()


class _PrerequisiteUnbound(RuntimeError):
    """A local technical stop, never an expected negative-case success."""


class _CaseAssertionFailure(RuntimeError):
    """Fixed diagnostic code only; no record or original exception formatting."""


def _require(condition: bool, code: str) -> None:
    if not condition:
        raise _CaseAssertionFailure(code)


def _retain(phase: str, error: BaseException) -> None:
    # Actual object references only; no serialization, repr, str, or file log.
    _RETAINED_ERRORS.append((phase, error))


def _verify_snapshot(path: Path, digest: str) -> bytes:
    if path.resolve(strict=True) != path:
        raise _PrerequisiteUnbound("FIXED_LOCATOR_DRIFT")
    payload = path.read_bytes()
    if sha256(payload).hexdigest().upper() != digest:
        raise _PrerequisiteUnbound("REAL_FIXED_ASSET_SHA_DRIFT")
    return payload


def _function(namespace: dict, name: str) -> FunctionType:
    entry = namespace[name]
    _require(
        type(entry) is FunctionType and entry.__globals__ is namespace,
        "CALLER_FUNCTION_NAMESPACE_MISMATCH",
    )
    return entry


def _load_fixed_caller() -> dict:
    global _ACTIVE_PHASE
    _ACTIVE_PHASE = "LOCAL_PREFLIGHT"
    if not (
        sys.flags.isolated == 1
        and sys.flags.no_site == 1
        and sys.flags.dont_write_bytecode == 1
    ):
        raise _PrerequisiteUnbound("REQUIRED_STARTUP_FLAGS_ABSENT")
    if type(sys.modules) is not dict:
        raise _PrerequisiteUnbound("MODULE_TABLE_NOT_NATIVE_DICT")
    if _CALLER_MODULE_NAME in sys.modules or _READER_MODULE_NAME in sys.modules:
        raise _PrerequisiteUnbound("PREEXISTING_FIXED_MODULE_SLOT")

    # Real asset drift stops every case, including planned negative probes.
    caller_bytes = _verify_snapshot(_CALLER_PATH, _CALLER_SHA256)
    _verify_snapshot(_READER_PATH, _READER_SHA256)
    _verify_snapshot(_BASELINE_PATH, _BASELINE_SHA256)
    _ACTIVE_PHASE = "CALLER_CONTROLLED_LOAD"
    caller_code = compile(
        caller_bytes, str(_CALLER_PATH), "exec", dont_inherit=True, optimize=0
    )
    module = ModuleType(_CALLER_MODULE_NAME)
    module.__file__ = str(_CALLER_PATH)
    namespace = module.__dict__
    exec(caller_code, namespace)
    _require(_CALLER_MODULE_NAME not in sys.modules, "CALLER_WAS_REGISTERED")
    _require(_READER_MODULE_NAME not in sys.modules, "UNEXPECTED_READER_AT_LOAD")
    _require(namespace["_TECHNICAL_ATTEMPT_USED"] is False, "CALLER_ALREADY_USED")
    _require(namespace["_READER_PATH"] == _READER_PATH, "READER_LOCATOR_MISMATCH")
    _require(namespace["_BASELINE_PATH"] == _BASELINE_PATH, "BASELINE_LOCATOR_MISMATCH")
    _require(namespace["_READER_SHA256"] == _READER_SHA256, "READER_DIGEST_MISMATCH")
    _require(namespace["_BASELINE_SHA256"] == _BASELINE_SHA256, "BASELINE_DIGEST_MISMATCH")
    _require(namespace["_READER_MODULE_NAME"] == _READER_MODULE_NAME, "READER_NAME_MISMATCH")
    for name in (
        "read_and_extract_fixed_baseline", "_read_fixed_bytes", "_clean_reader_entry"
    ):
        _function(namespace, name)
    carrier = namespace["DSP004FailureCoexistenceError"]
    _require(
        type(carrier) is type
        and issubclass(carrier, BaseException)
        and carrier.__module__ == _CALLER_MODULE_NAME
        and type(carrier.__init__) is FunctionType
        and carrier.__init__.__globals__ is namespace,
        "CARRIER_NAMESPACE_MISMATCH",
    )
    return namespace


def _expect_runtime_error(error: BaseException, message: str) -> None:
    # Exact error category/message is a pre-fixed refusal check, not output.
    # It cannot establish any unobserved caller stage or historical event.
    _retain("EXPECTED_REFUSAL_OBSERVATION", error)
    _require(type(error) is RuntimeError, "UNEXPECTED_REFUSAL_TYPE")
    _require(error.args == (message,), "UNEXPECTED_REFUSAL_VALUE")


def _assert_slot_absent(table: dict) -> None:
    _require(sys.modules is table, "MODULE_TABLE_IDENTITY_CHANGED")
    _require(_READER_MODULE_NAME not in table, "READER_SLOT_NOT_ABSENT")
    _require(_CALLER_MODULE_NAME not in table, "CALLER_SLOT_NOT_ABSENT")


def _full_entry_literal_records(namespace: dict) -> str:
    table = sys.modules
    _assert_slot_absent(table)
    records = _function(namespace, "read_and_extract_fixed_baseline")()
    _require(type(records) is tuple and len(records) == 3, "RECORD_TUPLE_SHAPE")
    record_type = type(records[0])
    _require(record_type.__name__ == "ExpectedBaselineRecord", "RECORD_CLASS_NAME")
    _require(record_type.__module__ == _READER_MODULE_NAME, "RECORD_CLASS_MODULE")
    _require(record_type.__slots__ == _FIELD_NAMES, "RECORD_SLOTS")
    _require(tuple(record_type.__dataclass_fields__) == _FIELD_NAMES, "RECORD_FIELDS")
    _require(record_type.__dataclass_params__.frozen is True, "RECORD_NOT_FROZEN")
    for record, expected in zip(records, _EXPECTED_RECORD_FIELDS):
        _require(type(record) is record_type, "RECORD_CLASS_CONSISTENCY")
        actual = tuple(getattr(record, name) for name in _FIELD_NAMES)
        _require(all(type(value) is str for value in actual), "RECORD_FIELD_TYPES")
        _require(actual == expected, "LITERAL_RECORD_ORDER_OR_VALUE")
    _require(namespace["_TECHNICAL_ATTEMPT_USED"] is True, "ENTRY_MARKER_NOT_USED")
    _assert_slot_absent(table)
    return "LOCAL_ASSERTIONS_OBSERVED"


def _release_synthetic_slot(table: dict, owned: ModuleType, allow_absent: bool) -> None:
    _require(sys.modules is table, "FIXTURE_MODULE_TABLE_IDENTITY_CHANGED")
    entry = table.get(_READER_MODULE_NAME, _ABSENT)
    if entry is _ABSENT and allow_absent:
        return
    _require(entry is owned, "FIXTURE_SLOT_MISSING_OR_FOREIGN")
    del table[_READER_MODULE_NAME]


def _slot_probe(namespace: dict, case_id: str) -> str:
    table = sys.modules
    _assert_slot_absent(table)
    original = ModuleType(_READER_MODULE_NAME)
    replacement = ModuleType(_READER_MODULE_NAME)
    installed = replacement if case_id == "HELPER_CLEAN_REPLACED_SLOT" else original
    primary_error = None
    cleanup_error = None
    slot_deleted_by_helper = False
    try:
        # Driver-owned synthetic fixture only; never overwrite an existing slot.
        _require(_READER_MODULE_NAME not in table, "FIXTURE_SLOT_BECAME_OCCUPIED")
        table[_READER_MODULE_NAME] = installed
        _require(table.get(_READER_MODULE_NAME) is installed, "FIXTURE_INSTALLATION")
        if case_id == "FULL_ENTRY_OCCUPIED_SLOT":
            try:
                _function(namespace, "read_and_extract_fixed_baseline")()
            except BaseException as error:
                _expect_runtime_error(error, "The fixed reader module name is already occupied")
            else:
                raise _CaseAssertionFailure("OCCUPIED_ENTRY_DID_NOT_REFUSE")
            _require(namespace["_TECHNICAL_ATTEMPT_USED"] is True, "ENTRY_MARKER_NOT_USED")
            _require(table.get(_READER_MODULE_NAME) is installed, "OCCUPIED_SLOT_CHANGED")
        elif case_id == "HELPER_CLEAN_OWNED_SLOT":
            _function(namespace, "_clean_reader_entry")(table, original, True)
            _require(_READER_MODULE_NAME not in table, "OWNED_SLOT_NOT_REMOVED")
            slot_deleted_by_helper = True
        elif case_id == "HELPER_CLEAN_REPLACED_SLOT":
            try:
                _function(namespace, "_clean_reader_entry")(table, original, True)
            except BaseException as error:
                _expect_runtime_error(
                    error, "Reader module entry is missing or belongs to another object"
                )
            else:
                raise _CaseAssertionFailure("REPLACED_SLOT_DID_NOT_REFUSE")
            _require(table.get(_READER_MODULE_NAME) is replacement, "REPLACEMENT_DELETED")
        else:
            raise _CaseAssertionFailure("UNBOUND_SLOT_PROBE")
    except BaseException as error:
        primary_error = error
        _retain("SYNTHETIC_SLOT_PROBE_PRIMARY", error)
    try:
        _release_synthetic_slot(table, installed, slot_deleted_by_helper)
    except BaseException as error:
        cleanup_error = error
        _retain("SYNTHETIC_FIXTURE_CLEANUP", error)
    # Retain both actual objects if both fail; neither is converted to a return
    # success or made into a fake caller failure stage. The outer entry stops.
    if primary_error is not None:
        raise primary_error
    if cleanup_error is not None:
        raise cleanup_error
    _assert_slot_absent(table)
    return "EXPECTED_REFUSAL_OBSERVED" if case_id != "HELPER_CLEAN_OWNED_SLOT" else "LOCAL_ASSERTIONS_OBSERVED"


def _synthetic_sha_refusal(namespace: dict) -> str:
    class _NonAssetLocator:
        """Local SYNTHETIC / NON-ASSET stub, not a Path or source carrier."""

        def __init__(self) -> None:
            self.operations = []

        def resolve(self, *, strict: bool):
            _require(strict is True, "SYNTHETIC_RESOLVE_ARGUMENT")
            self.operations.append("RESOLVE_STRICT")
            return self

        def read_bytes(self) -> bytes:
            self.operations.append("READ_SYNTHETIC_BYTES")
            return _HASH_PROBE_PAYLOAD

    table = sys.modules
    _assert_slot_absent(table)
    digest = namespace["_BASELINE_SHA256"]
    _require(sha256(_HASH_PROBE_PAYLOAD).hexdigest().upper() != digest, "SYNTHETIC_HASH_NOT_DIFFERENT")
    locator = _NonAssetLocator()
    try:
        _function(namespace, "_read_fixed_bytes")(locator, digest)
    except BaseException as error:
        _expect_runtime_error(error, "Fixed asset bytes differ from the bound digest")
    else:
        raise _CaseAssertionFailure("SYNTHETIC_HASH_DID_NOT_REFUSE")
    _require(locator.operations == ["RESOLVE_STRICT", "READ_SYNTHETIC_BYTES"], "SYNTHETIC_CONTROL_POINT")
    _require(namespace["_TECHNICAL_ATTEMPT_USED"] is False, "FULL_ENTRY_UNEXPECTEDLY_USED")
    _assert_slot_absent(table)
    return "EXPECTED_REFUSAL_OBSERVED"


def _cleanup_without_slot(namespace: dict, case_id: str) -> str:
    table = sys.modules
    _assert_slot_absent(table)
    synthetic_reader = ModuleType(_READER_MODULE_NAME)
    if case_id == "HELPER_CLEAN_MISSING_SLOT":
        argument_table = table
        expected_message = "Reader module entry is missing or belongs to another object"
    else:
        # Explicit synthetic argument, never replace sys.modules or caller globals.
        argument_table = {}
        expected_message = "Reader module table identity changed during the attempt"
    try:
        _function(namespace, "_clean_reader_entry")(argument_table, synthetic_reader, True)
    except BaseException as error:
        _expect_runtime_error(error, expected_message)
    else:
        raise _CaseAssertionFailure("CLEANUP_CONTRACT_DID_NOT_REFUSE")
    _require(namespace["_TECHNICAL_ATTEMPT_USED"] is False, "FULL_ENTRY_UNEXPECTEDLY_USED")
    _assert_slot_absent(table)
    return "EXPECTED_REFUSAL_OBSERVED"


def _carrier_construction(namespace: dict) -> str:
    table = sys.modules
    _assert_slot_absent(table)
    primary = KeyboardInterrupt()
    cleanup = SystemExit()
    carrier_type = namespace["DSP004FailureCoexistenceError"]
    carrier = carrier_type("EXTRACTION", primary, cleanup)
    _retain("SYNTHETIC_CARRIER_CONSTRUCTION", carrier)
    _require(type(carrier) is carrier_type, "CARRIER_ACTUAL_CLASS")
    _require(carrier.primary_stage == "EXTRACTION", "SYNTHETIC_CARRIER_STAGE")
    _require(carrier.primary_error is primary, "PRIMARY_REFERENCE_CHANGED")
    _require(carrier.cleanup_error is cleanup, "CLEANUP_REFERENCE_CHANGED")
    _require(not isinstance(primary, Exception) and not isinstance(cleanup, Exception), "NON_EXCEPTION_FIXTURE")
    _require(carrier.args == ("DSP-004 primary failure and module-entry cleanup failure coexist",), "CARRIER_FIXED_MESSAGE")
    _require(not hasattr(carrier, "code") and not hasattr(carrier, "detail"), "CARRIER_SUPPLEMENTED_FIELDS")
    _require(namespace["_TECHNICAL_ATTEMPT_USED"] is False, "FULL_ENTRY_UNEXPECTEDLY_USED")
    _assert_slot_absent(table)
    return "CONSTRUCTION_ASSERTIONS_OBSERVED"


def run_single_synthetic_case(case_id: str) -> tuple:
    """Future separately permitted entry; returns only fixed minimal status codes.

    A return value is not permission, evidence admission, acceptance, or PASS.
    The external controller must end the dedicated process and obey STOP_BATCH.
    Unobserved full-workflow paths remain UNEXERCISED, not inferred from helpers.
    The one-use marker is technical, not atomic, concurrent, or governing.
    """
    global _DRIVER_ATTEMPT_USED, _ACTIVE_PHASE
    if _DRIVER_ATTEMPT_USED:
        return ("DRIVER_ALREADY_USED", "NO_NEW_OBSERVATION", "NOT_RUN", "STOP_BATCH")
    _DRIVER_ATTEMPT_USED = True
    if type(case_id) is not str or case_id not in _CASE_LEVELS:
        return ("UNBOUND_CASE", "NO_OBSERVATION", "NOT_RUN", "STOP_BATCH")
    level = _CASE_LEVELS[case_id]
    try:
        namespace = _load_fixed_caller()
        _ACTIVE_PHASE = case_id
        if case_id == "FULL_ENTRY_LITERAL_RECORDS":
            observation = _full_entry_literal_records(namespace)
        elif case_id in (
            "FULL_ENTRY_OCCUPIED_SLOT", "HELPER_CLEAN_OWNED_SLOT", "HELPER_CLEAN_REPLACED_SLOT"
        ):
            observation = _slot_probe(namespace, case_id)
        elif case_id == "HELPER_SYNTHETIC_SHA_REFUSAL":
            observation = _synthetic_sha_refusal(namespace)
        elif case_id in ("HELPER_CLEAN_MISSING_SLOT", "HELPER_CLEAN_TABLE_IDENTITY"):
            observation = _cleanup_without_slot(namespace, case_id)
        else:
            observation = _carrier_construction(namespace)
        _require(_CALLER_MODULE_NAME not in sys.modules, "CALLER_WAS_REGISTERED")
        _ACTIVE_PHASE = "CASE_ENDED"
        return (case_id, level, observation, "END_CASE")
    except _PrerequisiteUnbound as error:
        _retain(_ACTIVE_PHASE, error)
        return (case_id, level, "NOT_RUN", "STOP_BATCH")
    except BaseException as error:
        _retain(_ACTIVE_PHASE, error)
        return (case_id, level, "INCOMPLETE", "STOP_BATCH")
