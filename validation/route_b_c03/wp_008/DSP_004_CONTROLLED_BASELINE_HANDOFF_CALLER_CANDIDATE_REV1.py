"""DSP-004 fixed baseline handoff caller, REV1 source candidate only.

Creation does not review, accept, admit, integrate, or execute this candidate.
The inherited upstream item 8 LIMITED remains; no complete upstream re-review
or execution readiness is claimed. No test or launcher is created with it.

Before loading this source, a separately authorized local launcher must bind
its complete source SHA, consume the same verified bytes, and bind the actual
interpreter, dependencies, startup channel, dedicated process, and purpose.
The caller must be loaded in a local ModuleType namespace, not registered or
imported under its own name. Its own digest is intentionally not embedded.

The sole entry takes no arguments. It is limited to one serial, non-reentrant
attempt per loaded instance, even on failure. Reloading to reset the marker is
outside the permitted workflow. The marker is not governance authorization,
an atomic concurrency guard, or a security replay-prevention mechanism.

Future invocation needs separate permission for both fixed assets, reader
initialization and extraction, and use of the three literal records. This code
does not establish those permissions, source trust, or six-side binding.
It does not call a provider or Gate, capture actual values, compare references,
write evidence, print results, or produce a review or admission verdict.

Only a completed extraction AND reader-entry cleanup may return the original
tuple. Failures retain real exception objects. References and tracebacks can
retain inputs or modules; cleanup is not proof of destruction or zero effects.
The future launcher must handle BaseException and default traceback output;
this source does not guarantee silence, zero disclosure, or complete handoff
under forced termination, resource exhaustion, or repeated interruption.
"""

from hashlib import sha256
from pathlib import Path
import sys
from types import FunctionType, ModuleType


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
_READER_SHA256 = (
    "AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727"
)
_BASELINE_SHA256 = (
    "BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368"
)
_READER_MODULE_NAME = "dsp004_reader_controlled_entry_rev1"
_TECHNICAL_ATTEMPT_USED = False
_ABSENT = object()


class DSP004FailureCoexistenceError(BaseException):
    """Keep two actual failures, not a normal return or an exchange record.

    The outer exception does not reproduce the original matching behavior,
    interrupt effect, or exit status. Its actual loaded class must be handled by
    the separately bound launcher, which must terminate the affected attempt.
    """

    def __init__(
        self,
        primary_stage: str,
        primary_error: BaseException,
        cleanup_error: BaseException,
    ) -> None:
        self.primary_stage = primary_stage
        self.primary_error = primary_error
        self.cleanup_error = cleanup_error
        super().__init__(
            "DSP-004 primary failure and module-entry cleanup failure coexist"
        )


def _read_fixed_bytes(path: Path, expected_sha256: str) -> bytes:
    """Internal fixed-asset operation, not a public path or SHA interface."""
    if path.resolve(strict=True) != path:
        raise RuntimeError("Fixed asset locator resolves to another location")
    payload = path.read_bytes()
    if sha256(payload).hexdigest().upper() != expected_sha256:
        raise RuntimeError("Fixed asset bytes differ from the bound digest")
    return payload


def _clean_reader_entry(
    module_table: dict,
    reader_module: ModuleType,
    registration_completed: bool,
) -> None:
    """Delete only this instance's reader entry; never remove a replacement."""
    if sys.modules is not module_table:
        raise RuntimeError("Reader module table identity changed during the attempt")
    entry = module_table.get(_READER_MODULE_NAME, _ABSENT)
    if not registration_completed and entry is _ABSENT:
        # There is no observed owned entry to remove after interrupted/failed
        # registration. Do not invent a cleanup failure or claim that prior
        # registration history or full handoff has been established.
        return
    if entry is not reader_module:
        raise RuntimeError("Reader module entry is missing or belongs to another object")
    del module_table[_READER_MODULE_NAME]


def read_and_extract_fixed_baseline() -> tuple:
    """Return the same native tuple only after successful reader-entry cleanup.

    The caller of this entry owns the prior authorization and environment checks.
    Neither invoking the function nor reaching its byte checks supplies authority.
    Private helpers, globals, or returned records are not permission interfaces.
    """
    global _TECHNICAL_ATTEMPT_USED
    if _TECHNICAL_ATTEMPT_USED:
        raise RuntimeError("This caller instance's technical attempt is already used")
    _TECHNICAL_ATTEMPT_USED = True

    module_table = sys.modules
    if type(module_table) is not dict:
        raise RuntimeError("The reader registration table is not a native dict")
    if _READER_MODULE_NAME in module_table:
        raise RuntimeError("The fixed reader module name is already occupied")

    # Retain both complete, unmodified byte snapshots. The helpers receive only
    # these fixed constants, never caller-supplied paths, digests, or callbacks.
    reader_bytes = _read_fixed_bytes(_READER_PATH, _READER_SHA256)
    baseline_bytes = _read_fixed_bytes(_BASELINE_PATH, _BASELINE_SHA256)
    reader_code = compile(
        reader_bytes,
        str(_READER_PATH),
        "exec",
        dont_inherit=True,
        optimize=0,
    )
    reader_module = ModuleType(_READER_MODULE_NAME)
    reader_module.__file__ = str(_READER_PATH)
    reader_namespace = reader_module.__dict__

    # Recheck immediately before this attempt's registration. No overwrite,
    # alternate name, ordinary import, cached module, or file-loader fallback.
    if sys.modules is not module_table:
        raise RuntimeError("Reader module table changed before registration")
    if _READER_MODULE_NAME in module_table:
        raise RuntimeError("The fixed reader module name became occupied")

    registration_completed = False
    primary_stage = "MODULE_REGISTRATION"
    failure_stage = None
    primary_error = None
    cleanup_error = None
    result = None
    try:
        module_table[_READER_MODULE_NAME] = reader_module
        registration_completed = True
        primary_stage = "READER_INITIALIZATION"
        exec(reader_code, reader_namespace)
        primary_stage = "EXTRACTION"
        extractor = reader_namespace["extract_expected_baseline"]
        if (
            type(extractor) is not FunctionType
            or extractor.__globals__ is not reader_namespace
        ):
            raise RuntimeError("Reader entry is not defined in this reader namespace")
        result = extractor(baseline_bytes)
        if type(result) is not tuple:
            raise RuntimeError("Reader did not return a native tuple")
    except BaseException as error:
        primary_error = error
        failure_stage = primary_stage

    # One cleanup attempt covers success and actual registered failure paths.
    # It also observes an owned entry when registration was interrupted before
    # the completion marker. It is not an atomic proof of registration history.
    try:
        _clean_reader_entry(module_table, reader_module, registration_completed)
    except BaseException as error:
        cleanup_error = error

    if primary_error is not None and cleanup_error is not None:
        raise DSP004FailureCoexistenceError(
            failure_stage,
            primary_error,
            cleanup_error,
        )
    if primary_error is not None:
        raise primary_error
    if cleanup_error is not None:
        raise cleanup_error
    return result
