"""DSP-004 fixed local-synthetic bootstrap successor REV2.

The accepted REV1 remains unchanged at SHA-256:
4281385A8694C870A96E7EC7B98A9CB027A470C1AC2EE5F31BABCF9D56F46007
This NEW source has a concrete inherited-pipe entry for the authorized local
synthetic batch, not a formal runtime/source-admission service. Its receiver,
single N registration and native exception/cleanup retention are preserved.
No accepted source is patched or loaded by its old private refusal path.

The parent creates a suspended fixed Python process already assigned to its
own kill-on-close Job, and explicitly lists the five inherited pipe handles.
Here stdin is the dedicated code pipe; the two canonical numeric arguments
are command-read and report-write pipe handles, not paths or approval flags.
Runtime flags and handle types are checked. Physical peer provenance remains
a parent-bound observation, not cryptographic authentication.
All unhandled entry failures return silent nonzero; native errors are retained
only in this child. No raw exception/source/objects go to stdout/stderr.
Complete code SHA/length and actual EOF precede N registration and B/A loading.
Memory is not durable evidence; stop/close/exit do not prove destruction.
DSP-004 OPEN / HOLD; B-01/B-02 OPEN; all prior history/LIMITED preserved.
"""

from __future__ import annotations

from hashlib import sha256
from importlib.machinery import ModuleSpec
from io import FileIO
from types import FunctionType, ModuleType
import sys
import os
import msvcrt
import ctypes


_N_NAME = "DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV4"
_SOURCE_PREFIX = b"DSP004-CAPTURE-SOURCES-V1\n"
# These are fixed snapshot identities, not authority or environment checks.
_SOURCE_DESCRIPTORS = (
    ("B", 16475, "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"),
    ("A", 18301, "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C"),
    ("N", 62240, "A16904C8E67EAF4B459F0DB9688D3C685269810AD0D0CB3911BF03B852F1E11A"),
)
# 26-byte prefix + three 73-byte headers + the three fixed payloads.
_FIXED_FRAME_LENGTH = 26 + 3 * 73 + 16475 + 18301 + 62240
_CODE_LIMIT = 262144  # Proposed separate code ceiling, not an old-limit waiver.
_RESERVED = False
_HELD_RECEIPTS = []


class BootstrapBlocked(RuntimeError):
    """Fixed codes only; never contains raw input or native exception text."""


class BootstrapReceipt:
    __slots__ = ("sources", "module", "stage", "read_attempted", "eof",
                 "original_error", "cleanup_errors", "streams",
                 "load_attempted", "batch", "control_receipt")

    def __init__(self, streams):
        self.sources = ()
        self.module = None
        self.stage = "RESERVED"
        self.read_attempted = False
        self.eof = False
        self.original_error = None
        self.cleanup_errors = []
        self.streams = streams
        self.load_attempted = False
        self.batch = None
        self.control_receipt = None


def _require_execution_binding() -> None:
    expected = "C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe"
    if (os.name != "nt" or sys.flags.isolated != 1 or sys.flags.no_site != 1
            or sys.dont_write_bytecode is not True
            or os.path.normcase(os.path.abspath(sys.executable)) != os.path.normcase(expected)):
        raise BootstrapBlocked("FIXED_LOCAL_INTERPRETER_REQUIRED")


_ENTRY_ERRORS = []


def main() -> int:
    owned = []
    outcome = 78
    try:
        _require_execution_binding()
        if len(sys.argv) != 3:
            raise BootstrapBlocked("TWO_INHERITED_PIPE_HANDLES_REQUIRED")
        handles = []
        get_type = ctypes.WinDLL("kernel32", use_last_error=True).GetFileType
        get_type.argtypes = (ctypes.c_void_p,)
        get_type.restype = ctypes.c_uint32
        for argument in sys.argv[1:]:
            value = int(argument)
            if str(value) != argument or value <= 0 or value >= 1 << (8 * ctypes.sizeof(ctypes.c_void_p)):
                raise BootstrapBlocked("NONCANONICAL_PIPE_HANDLE")
            if get_type(value) != 3:
                raise BootstrapBlocked("INHERITED_HANDLE_NOT_PIPE")
            handles.append(value)
        if handles[0] == handles[1]:
            raise BootstrapBlocked("ALIASED_PRIVATE_HANDLES")
        code = sys.stdin.buffer.raw
        if type(code) is not FileIO:
            raise BootstrapBlocked("NATIVE_STDIN_PIPE_REQUIRED")
        owned.append(code)
        command = FileIO(msvcrt.open_osfhandle(handles[0], os.O_RDONLY | os.O_BINARY), "rb")
        owned.append(command)
        report = FileIO(msvcrt.open_osfhandle(handles[1], os.O_WRONLY | os.O_BINARY), "wb")
        owned.append(report)
        _run_closed_reference(code, command, report)
        outcome = 0
    except BaseException as original:
        _ENTRY_ERRORS.append(original)
        outcome = 78
    finally:
        for stream in owned:
            try:
                stream.close()
            except BaseException as cleanup:
                _ENTRY_ERRORS.append(cleanup)
    return outcome if not _ENTRY_ERRORS else 78


def _read_exact_reference(stream: FileIO, count: int,
                          receipt: BootstrapReceipt) -> bytes:
    _require_execution_binding()
    if (type(stream) is not FileIO or type(count) is not int
            or not 0 < count <= _CODE_LIMIT):
        raise BootstrapBlocked("FIXED_READ_BOUNDARY_UNBOUND")
    chunks = []
    remaining = count
    while remaining:
        receipt.read_attempted = True
        piece = stream.read(min(remaining, 65536))
        if type(piece) is not bytes or not 0 < len(piece) <= remaining:
            raise BootstrapBlocked("CODE_INPUT_INCOMPLETE")
        chunks.append(piece)
        remaining -= len(piece)
    return b"".join(chunks)


def _receive_fixed_sources_reference(stream: FileIO,
                                     receipt: BootstrapReceipt) -> tuple:
    _require_execution_binding()
    if (type(receipt) is not BootstrapReceipt
            or not any(receipt is held for held in _HELD_RECEIPTS)
            or receipt.read_attempted or receipt.sources or receipt.eof):
        raise BootstrapBlocked("UNOWNED_OR_REPEATED_RECEIVER")
    # Reserve the whole receive attempt before prefix/header/allocation work.
    # A failure with zero verified payloads must still never permit re-entry.
    receipt.read_attempted = True
    if _FIXED_FRAME_LENGTH > _CODE_LIMIT:
        raise BootstrapBlocked("FIXED_FRAME_OVERFLOW")
    receipt.stage = "SOURCE_PREFIX"
    if _read_exact_reference(stream, len(_SOURCE_PREFIX), receipt) != _SOURCE_PREFIX:
        raise BootstrapBlocked("SOURCE_PREFIX_MISMATCH")
    verified = []
    for role, count, expected_sha in _SOURCE_DESCRIPTORS:
        receipt.stage = role + "_HEADER"
        header = (role + "|" + str(count) + "|" + expected_sha + "\n").encode("ascii")
        if len(header) != 73 or _read_exact_reference(stream, len(header), receipt) != header:
            raise BootstrapBlocked("SOURCE_ORDER_HEADER_OR_LENGTH_MISMATCH")
        receipt.stage = role + "_PAYLOAD"
        data = _read_exact_reference(stream, count, receipt)
        if sha256(data).hexdigest().upper() != expected_sha:
            raise BootstrapBlocked("SOURCE_SHA_MISMATCH")
        verified.append(data)
        receipt.sources = tuple(verified)  # Retain each verified prefix privately.
    receipt.stage = "SOURCE_EOF"
    receipt.read_attempted = True
    tail = stream.read(1)
    if type(tail) is not bytes or tail != b"":
        raise BootstrapBlocked("SOURCE_TAIL_OR_EOF_UNCONFIRMED")
    receipt.eof = True
    receipt.stage = "SOURCE_RECEIVED_EXACT"
    return receipt.sources


def _load_single_n_reference(receipt: BootstrapReceipt):
    _require_execution_binding()
    if (type(receipt) is not BootstrapReceipt
            or not any(receipt is held for held in _HELD_RECEIPTS)
            or not receipt.eof or len(receipt.sources) != 3
            or receipt.load_attempted):
        raise BootstrapBlocked("SINGLE_LOAD_RECEIPT_UNBOUND")
    receipt.load_attempted = True  # No retry, including partial load failure.
    if type(sys.modules) is not dict or _N_NAME in sys.modules:
        raise BootstrapBlocked("N_SLOT_OCCUPIED_OR_MODULE_TABLE_UNBOUND")
    # Exact held immutable bytes, rechecked without reopening any file.
    data = receipt.sources[2]
    if (type(data) is not bytes or len(data) != _SOURCE_DESCRIPTORS[2][1]
            or sha256(data).hexdigest().upper() != _SOURCE_DESCRIPTORS[2][2]):
        raise BootstrapBlocked("N_HELD_BYTES_CHANGED")
    module = ModuleType(_N_NAME)
    module.__package__ = ""
    module.__spec__ = ModuleSpec(_N_NAME, loader=None)
    module.__file__ = "<DSP004_FIXED_N_REV4_BYTES>"
    receipt.module = module  # Strong reference BEFORE registration and execution.
    receipt.stage = "N_REGISTER"
    sys.modules[_N_NAME] = module
    receipt.stage = "N_EXECUTION"
    exec(compile(data, module.__file__, "exec", dont_inherit=True, optimize=0),
         module.__dict__)
    if (sys.modules.get(_N_NAME) is not module or module.__name__ != _N_NAME
            or module.CARRIER_MODULE_NAME != _N_NAME):
        raise BootstrapBlocked("N_NATIVE_MODULE_IDENTITY_MISMATCH")
    for name in ("_bind_synthetic_basis", "_prepare_fixed_batch_reference", "_serve_private_control_reference"):
        function = module.__dict__.get(name)
        if type(function) is not FunctionType or function.__globals__ is not module.__dict__:
            raise BootstrapBlocked("N_NATIVE_ENTRY_IDENTITY_MISMATCH")
    receipt.stage = "N_REGISTERED_NOT_ADMITTED"
    return module


def _run_closed_reference(code: FileIO, command: FileIO,
                          report: FileIO) -> BootstrapReceipt:
    """Fixed local-synthetic entry; not an acceptance or reusable grant.

    Stream identity checks do not prove OS handles/peer/roots. Endpoint owner
    contract here takes these three existing native endpoints and retains them
    BEFORE any read. It does not reopen a path or close foreign N module slots.
    """
    _require_execution_binding()
    global _RESERVED
    if _RESERVED:
        raise BootstrapBlocked("BOOTSTRAP_ALREADY_RESERVED")
    _RESERVED = True
    if (any(type(stream) is not FileIO for stream in (code, command, report))
            or len({code.fileno(), command.fileno(), report.fileno()}) != 3
            or not code.readable() or code.writable()
            or not command.readable() or command.writable()
            or not report.writable() or report.readable()):
        raise BootstrapBlocked("THREE_DISTINCT_NATIVE_ENDPOINTS_REQUIRED")
    receipt = BootstrapReceipt((code, command, report))
    _HELD_RECEIPTS.append(receipt)
    try:
        dependency, contract, _ = _receive_fixed_sources_reference(code, receipt)
        module = _load_single_n_reference(receipt)
        receipt.stage = "SYNTHETIC_PIPE_AND_SOURCE_BASIS"
        module._bind_synthetic_basis(code, command, report, dependency, contract)
        receipt.stage = "N_OWNS_B_AND_A"
        receipt.batch = module._prepare_fixed_batch_reference(dependency, contract)
        receipt.stage = "NATIVE_SUPPLEMENT"
        count = module._native_synthetic_supplement(receipt.batch)
        if count != 8:
            raise BootstrapBlocked("NATIVE_SUPPLEMENT_COUNT")
        module._write_private_frame_reference(
            report, b"DSP004-NATIVE-SUPPLEMENT-V1|8|PASS|UNVERIFIED_REPORT\n")
        receipt.stage = "PRIVATE_CONTROL"
        receipt.control_receipt = module._serve_private_control_reference(
            receipt.batch, command, report)
        receipt.stage = "CONTROL_RETURNED_UNVERIFIED"
    except BaseException as original:
        receipt.original_error = original  # Original object, no rendering.
    finally:
        # Attempt all owned closes; a cleanup failure never replaces the primary.
        # Native synchronous close may block: actual external stopping is UNBOUND.
        for role, stream in (("REPORT_CLOSE", report), ("COMMAND_CLOSE", command),
                             ("CODE_CLOSE", code)):
            try:
                stream.close()
            except BaseException as cleanup:
                receipt.cleanup_errors.append((role, cleanup))
    if receipt.original_error is not None:
        raise receipt.original_error
    if receipt.cleanup_errors:
        raise receipt.cleanup_errors[0][1]
    return receipt


if __name__ == "__main__":
    raise SystemExit(main())
