"""DSP-004 fixed-byte receiver / single-N-loader candidate REV1.

NEW SOURCE AND INDEPENDENT STATIC REVIEW ONLY. Not admitted or runnable.
No source was loaded/compiled/tested to materialize this file. No environment
was re-probed. The conversation-level startup design REV2 has no file SHA.

Code input is a dedicated native FileIO: fixed prefix, exact B/A/N headers,
bounded exact payloads and full SHA-256, then one-byte actual EOF observation.
Only that held N bytes object can reach the sole N module loader; no file
paths, imports of candidate files, JSON, pickle, eval, callback or retry.
N must be registered under its exact name BEFORE its dataclass declarations.
Occupied N slots are rejected, never removed/replaced. N alone loads B/A.

Command and report FileIO endpoints are DISTINCT from code input and each
other. Their physical handle origin, peer binding and pre-start stdout/stderr
redirection are NOT established here. No endpoint opening or process creation
is implemented. Private functions are CLOSED before I/O/compilation/loading.
main silently returns 78. Reflective/private bypass is not authorization.
A future driver/revision requires separate review and execution binding.

All native errors and owned module/stream objects are retained in child
memory, including primary+cleanup coexistence. Nothing renders exception
messages or source bytes. Memory can be lost when the process/host ends.
Returned writes, STOPPED, stream closure, EOF and process exit are distinct
observations; none proves total cleanup, confidentiality or trusted execution.
Recursive dependencies/resolver/interpreter/roots, sustained outside ownership,
actual timing and independent hard stop remain LIMITED and UNBOUND.
158 directory cases remain NOT_RUN; no transfer of the 189-item plan.
DSP-004 OPEN / HOLD; B-01/B-02 OPEN. All prior LIMITED/history preserved.
No source admission, real capture, integration, acceptance or deployment.
"""

from __future__ import annotations

from hashlib import sha256
from importlib.machinery import ModuleSpec
from io import FileIO
from types import FunctionType, ModuleType
import sys


_N_NAME = "DSP_004_CAPTURE_RESULT_VALIDATION_CARRIER_CANDIDATE_REV3"
_SOURCE_PREFIX = b"DSP004-CAPTURE-SOURCES-V1\n"
# These are fixed snapshot identities, not authority or environment checks.
_SOURCE_DESCRIPTORS = (
    ("B", 16475, "7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4"),
    ("A", 18301, "E9472328847617EBF629FB01A0A163C0805226690600E5E13EBE1209E2F6705C"),
    ("N", 57623, "329EC4A1C12351667F9A52946E4E11F6B01E287796FBDE42211FE5861CC14845"),
)
# 26-byte prefix + three 73-byte headers + the three fixed payloads.
_FIXED_FRAME_LENGTH = 26 + 3 * 73 + 16475 + 18301 + 57623
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
    raise BootstrapBlocked("EXECUTION_BINDINGS_NOT_ESTABLISHED")


def main() -> int:
    # No reads, hash, parse, clock, load or channel open. Silent non-success.
    return 78


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
    module.__file__ = "<DSP004_FIXED_N_REV3_BYTES>"
    receipt.module = module  # Strong reference BEFORE registration and execution.
    receipt.stage = "N_REGISTER"
    sys.modules[_N_NAME] = module
    receipt.stage = "N_EXECUTION"
    exec(compile(data, module.__file__, "exec", dont_inherit=True, optimize=0),
         module.__dict__)
    if (sys.modules.get(_N_NAME) is not module or module.__name__ != _N_NAME
            or module.CARRIER_MODULE_NAME != _N_NAME):
        raise BootstrapBlocked("N_NATIVE_MODULE_IDENTITY_MISMATCH")
    for name in ("_prepare_fixed_batch_reference", "_serve_private_control_reference"):
        function = module.__dict__.get(name)
        if type(function) is not FunctionType or function.__globals__ is not module.__dict__:
            raise BootstrapBlocked("N_NATIVE_ENTRY_IDENTITY_MISMATCH")
    receipt.stage = "N_REGISTERED_NOT_ADMITTED"
    return module


def _run_closed_reference(code: FileIO, command: FileIO,
                          report: FileIO) -> BootstrapReceipt:
    """Source-only reference wiring; no accepting entry or private grant.

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
        receipt.stage = "N_OWNS_B_AND_A"
        receipt.batch = module._prepare_fixed_batch_reference(dependency, contract)
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
