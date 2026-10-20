"""DSP-004 new local-synthetic supervisor REV3.

Runs only fixed local test subjects in owned Windows Jobs and explicit pipes.
This is NOT the accepted C# supervisor, a provider connector or business runtime.
The independent outer driver process owns another kill-on-close Job, including
this host and all subject descendants. Reports remain UNVERIFIED_REPORT.
"""
from __future__ import annotations

import time
from dsp004_windows_scope import JobChild, BoundaryFailure

READY = b"DSP004-READY-V1|158|UNVERIFIED_REPORT\n"
END = b"DSP004-END-V1|158|UNVERIFIED_REPORT\n"
STOP = b"DSP004-COMMAND-V1|STOP\n"
STOPPED = b"DSP004-STOPPED-V1|UNVERIFIED_REPORT\n"
SUPPLEMENT = b"DSP004-NATIVE-SUPPLEMENT-V1|8|PASS|UNVERIFIED_REPORT\n"
PREFIX = b"DSP004-CAPTURE-SOURCES-V1\n"
_HELD_PROTOCOL_ERRORS = []

CASE_IDS = (
    "C01-variant_id-NONE",
    "C01-variant_id-BOOL",
    "C01-variant_id-SUBCLASS",
    "C01-variant_id-EMPTY",
    "C01-variant_id-SPACE",
    "C01-attempt_id-NONE",
    "C01-attempt_id-BOOL",
    "C01-attempt_id-SUBCLASS",
    "C01-attempt_id-EMPTY",
    "C01-attempt_id-SPACE",
    "C01-input_snapshot_sha256-NONE",
    "C01-input_snapshot_sha256-BOOL",
    "C01-input_snapshot_sha256-SUBCLASS",
    "C01-input_snapshot_sha256-EMPTY",
    "C01-input_snapshot_sha256-SPACE",
    "C01-audit_correlation_id-NONE",
    "C01-audit_correlation_id-BOOL",
    "C01-audit_correlation_id-SUBCLASS",
    "C01-audit_correlation_id-EMPTY",
    "C01-audit_correlation_id-SPACE",
    "C01-HEX64-LOWER",
    "C01-HEX64-UPPER",
    "C01-SHORT",
    "C01-LONG",
    "C01-NONHEX",
    "C02-PROJECT-NONE",
    "C02-PROJECT-INT",
    "C02-PROJECT-TEXT",
    "C02-SESSION-NONE",
    "C02-SESSION-INT",
    "C02-SESSION-TEXT",
    "C02-PROVIDER-NONE",
    "C02-PROVIDER-INT",
    "C02-PROVIDER-TEXT",
    "C02-BOUNDARY-TEXT",
    "C02-TYPE-NAME",
    "C02-WRONG-TYPE",
    "C02-SOURCE-NONE",
    "C02-SOURCE-EMPTY",
    "C02-SOURCE-SPACE",
    "C03-SUBSET-0",
    "C03-SUBSET-1",
    "C03-SUBSET-2",
    "C03-SUBSET-3",
    "C03-SUBSET-4",
    "C03-SUBSET-5",
    "C03-SUBSET-6",
    "C03-SUBSET-7",
    "C03-DUPLICATE",
    "C03-REVERSED",
    "C03-FOUR",
    "C03-LIST",
    "C03-TUPLE-SUBCLASS",
    "C04-STATE-INVOCATION_RECEIVED",
    "C04-STATE-GATE_CHECKING",
    "C04-STATE-BLOCKED",
    "C04-STATE-REJECTED",
    "C04-STATE-ELIGIBLE_FOR_MAPPING",
    "C04-STATE-MAPPING",
    "C04-STATE-MAPPING_CANDIDATE",
    "C04-STATE-QUARANTINED",
    "C04-STATE-HUMAN_REVIEW_PENDING",
    "C04-STATE-TEXT",
    "C04-REASON-BOOL",
    "C04-REASON-EMPTY",
    "C04-CORRELATION-NONE",
    "C04-CORRELATION-OTHER",
    "C04-WRITES-LIST",
    "C04-WRITES-SUBCLASS",
    "C04-WRITES-NONEMPTY",
    "C05-STRUCTURAL-BLOCKED",
    "C05-STRUCTURAL-REJECTED",
    "C05-STRUCTURAL-ELIGIBLE_FOR_MAPPING",
    "C05-CAPTURE-FALSE",
    "C05-CLEANUP-FALSE",
    "C05-HANDOFF-FALSE",
    "C05-CAPTURE-INT",
    "C05-CLEANUP-INT",
    "C05-HANDOFF-INT",
    "C05-BASIS-EMPTY",
    "C05-BASIS-NONE",
    "C05-MISSING-0",
    "C05-MISSING-1",
    "C05-MISSING-2",
    "C05-NO-PRIOR",
    "C06-VALUE",
    "C06-INTERRUPT",
    "C06-EXIT",
    "C06-NONEXCEPTION-CLASS",
    "C06-NONEXCEPTION-TEXT",
    "C06-NONEXCEPTION-NONE",
    "C07-0-PRIMARY",
    "C07-0-CLEANUP",
    "C07-0-BOTH",
    "C07-0-SHARED",
    "C07-1-PRIMARY",
    "C07-1-CLEANUP",
    "C07-1-BOTH",
    "C07-1-SHARED",
    "C07-2-PRIMARY",
    "C07-2-CLEANUP",
    "C07-2-BOTH",
    "C07-2-SHARED",
    "C07-3-PRIMARY",
    "C07-3-CLEANUP",
    "C07-3-BOTH",
    "C07-3-SHARED",
    "C07-NO-ERRORS",
    "C08-INTERRUPTED_WITHOUT_EXCEPTION-0",
    "C08-INTERRUPTED_WITHOUT_EXCEPTION-1",
    "C08-INTERRUPTED_WITHOUT_EXCEPTION-2",
    "C08-INTERRUPTED_WITHOUT_EXCEPTION-3",
    "C08-NO_RETURN-0",
    "C08-NO_RETURN-1",
    "C08-NO_RETURN-2",
    "C08-NO_RETURN-3",
    "C08-MISSING_OBSERVATION-0",
    "C08-MISSING_OBSERVATION-1",
    "C08-MISSING_OBSERVATION-2",
    "C08-MISSING_OBSERVATION-3",
    "C08-CARRIER_IDENTITY_FAILURE-0",
    "C08-CARRIER_IDENTITY_FAILURE-1",
    "C08-CARRIER_IDENTITY_FAILURE-2",
    "C08-CARRIER_IDENTITY_FAILURE-3",
    "C08-HANDOFF_INCOMPLETE-0",
    "C08-HANDOFF_INCOMPLETE-1",
    "C08-HANDOFF_INCOMPLETE-2",
    "C08-HANDOFF_INCOMPLETE-3",
    "C09-DICT",
    "C09-FOREIGN",
    "C09-MATERIALS-ONLY",
    "C09-RESULT-SUBCLASS",
    "C09-REVALIDATE-COMPLETE",
    "C09-REVALIDATE-FAILURE",
    "C09-REVALIDATE-INCOMPLETE",
    "C10-CONSTRUCTOR-MISSING-CaptureInvocationBinding",
    "C10-CONSTRUCTOR-MISSING-CapturedReference",
    "C10-CONSTRUCTOR-MISSING-CaptureMaterials",
    "C10-CONSTRUCTOR-MISSING-CompleteCaptureReturn",
    "C10-CONSTRUCTOR-MISSING-FailureOccurrence",
    "C10-CONSTRUCTOR-MISSING-CaptureFailure",
    "C10-CONSTRUCTOR-MISSING-IncompleteCapture",
    "C10-REVALIDATE-MISSING-materials",
    "C10-REVALIDATE-MISSING-stage",
    "C10-REVALIDATE-MISSING-cause",
    "C11-BOUNDARY-CONSTRUCT-PSEUDO",
    "C11-BOUNDARY-CONSTRUCT-CONTROL",
    "C11-BOUNDARY-REVALIDATE-PSEUDO",
    "C11-BOUNDARY-REVALIDATE-CONTROL",
    "C11-CAUSE-CONSTRUCT-PSEUDO",
    "C11-CAUSE-CONSTRUCT-CONTROL",
    "C11-CAUSE-REVALIDATE-PSEUDO",
    "C11-CAUSE-REVALIDATE-CONTROL",
    "C11-PRIOR-CONSTRUCT-PSEUDO",
    "C11-PRIOR-CONSTRUCT-CONTROL",
    "C11-PRIOR-REVALIDATE-PSEUDO",
    "C11-PRIOR-REVALIDATE-CONTROL",
    "C12-SHALLOW-FREEZE-LIMITATION",
)

FAULTS = (
    "HANG", "STDOUT", "STDERR", "BAD_READY", "PARTIAL", "OVERLONG",
    "EARLY_EOF", "DUPLICATE", "OUT_OF_ORDER", "SETUP_NE", "CASE_FAIL",
    "TRAILER", "DESCENDANT", "REAL_INTERRUPT", "STDOUT_LATE", "STDERR_LATE",
)
SOURCE_CASES = (
    "NORMAL", "BAD_B_SHA", "BAD_ORDER", "TRUNCATED_SOURCE", "EXTRA_SOURCE",
    "KEEP_CODE_OPEN", "EARLY_STOP", "BAD_COMMAND", "NEXT_DUPLICATE", "EXTRA_AFTER_STOP",
)
ALLOWED = SOURCE_CASES + FAULTS + ("HOST_HANG", "HOST_STALL_WITH_CHILD")

def source_frame(assets):
    from hashlib import sha256
    body = bytearray(PREFIX)
    for role in ("B", "A", "N"):
        value = assets[role]
        if type(value) is not bytes:
            raise BoundaryFailure("NATIVE_SOURCE_BYTES_REQUIRED")
        body.extend((role + "|" + str(len(value)) + "|" + sha256(value).hexdigest().upper() + "\n").encode("ascii"))
        body.extend(value)
    if len(body) > 262144:
        raise BoundaryFailure("SOURCE_INPUT_LIMIT")
    return bytes(body)

def parse_report(frame, ordinal):
    if not frame.endswith(b"\n") or len(frame) > 4096:
        raise BoundaryFailure("REPORT_FRAME")
    fields = frame[:-1].decode("ascii", "strict").split("|")
    if (len(fields) != 6 or fields[0] != "DSP004-CAPTURE-V1"
            or fields[1] != str(ordinal) or fields[2] != CASE_IDS[ordinal - 1]
            or fields[5] != "UNVERIFIED_REPORT"):
        raise BoundaryFailure("REPORT_ORDER_OR_ID")
    if not ((fields[3] == "SETUP" and fields[4] == "NOT_EVALUABLE")
            or fields[3] in ("SUT", "ORACLE") and fields[4] in ("PASS", "FAIL")):
        raise BoundaryFailure("REPORT_PHASE_VALUE")
    return fields[3], fields[4]

def require_eof(scope, due):
    while True:
        scope.check(due, protective=True)
        scope.monitor_zero()
        piece = scope.poll("report")
        if piece == b"":
            return
        if piece:
            raise BoundaryFailure("EXTRA_REPORT_AFTER_STOPPED")
        time.sleep(0.002)

def run_case(case, assets, cwd, batch_t0, host_signal):
    if case not in ALLOWED:
        raise BoundaryFailure("UNDECLARED_SYNTHETIC_CASE")
    work_due, hard_due = batch_t0 + 60.0, batch_t0 + 70.0
    scope = JobChild(batch_t0, hard_due)
    reports, passes, attempted, supplement = 0, 0, 0, 0
    reason, status = None, "INCOMPLETE_UNCONFIRMED"
    maximum_active = 0
    ready_observed = False
    last_phase, last_determination = None, None
    try:
        if case == "HOST_HANG":
            host_signal(b"DSP004-HOST-STALL-READY\n")
            time.sleep(60)
            raise BoundaryFailure("HOST_STALL_UNEXPECTED_RETURN")
        mode = "HANG" if case == "HOST_STALL_WITH_CHILD" else case
        fixture = mode in FAULTS
        payload = b"" if fixture else source_frame(assets)
        if case == "BAD_B_SHA":
            offset = len(PREFIX) + 73
            payload = payload[:offset] + bytes((payload[offset] ^ 1,)) + payload[offset + 1:]
        elif case == "BAD_ORDER":
            first = len(PREFIX)
            payload = payload[:first] + b"A" + payload[first + 1:]
        elif case == "TRUNCATED_SOURCE":
            payload = payload[:-1]
        elif case == "EXTRA_SOURCE":
            payload += b"X"
        script = assets["FAULT"] if fixture else assets["BOOT"]
        scope.start(script, cwd, (mode,) if fixture else ())
        maximum_active = scope.active()
        write = scope.write("code", payload, work_due, close_after=case != "KEEP_CODE_OPEN")
        scope.wait_write(write, work_due)
        if case == "HOST_STALL_WITH_CHILD":
            host_signal(b"DSP004-HOST-STALL-READY\n")
            time.sleep(60)
            raise BoundaryFailure("HOST_STALL_UNEXPECTED_RETURN")
        ready_due = min(work_due, time.monotonic() + 0.5) if case in (
            "HANG", "PARTIAL", "KEEP_CODE_OPEN", "DESCENDANT") else work_due
        if not fixture:
            if scope.frame(ready_due) != SUPPLEMENT:
                raise BoundaryFailure("NATIVE_SUPPLEMENT_FRAME")
            supplement = 8
        ready = scope.frame(ready_due)
        if case == "DESCENDANT":
            if ready != b"DSP004-DESCENDANT-V1\n":
                raise BoundaryFailure("DESCENDANT_MARKER")
            until = min(time.monotonic() + 0.5, work_due)
            while time.monotonic() < until:
                maximum_active = max(maximum_active, scope.active())
                if maximum_active >= 2:
                    raise BoundaryFailure("DESCENDANT_STOP_EXERCISE")
                time.sleep(0.002)
            raise BoundaryFailure("DESCENDANT_NOT_OBSERVED")
        if ready != READY:
            raise BoundaryFailure("READY_FRAME")
        ready_observed = True
        if case != "EARLY_STOP":
            for ordinal in range(1, len(CASE_IDS) + 1):
                due = min(time.monotonic() + 2.0, work_due, hard_due)
                sent_ordinal = 1 if case == "NEXT_DUPLICATE" and ordinal == 2 else ordinal
                identifier = "UNDECLARED" if case == "BAD_COMMAND" else CASE_IDS[sent_ordinal - 1]
                frame = ("DSP004-COMMAND-V1|NEXT|" + str(sent_ordinal) + "|" + identifier + "\n").encode("ascii")
                attempted += 1  # Attempted or unknown; not proof of child execution.
                task = scope.write("command", frame, due)
                scope.wait_write(task, due)
                phase, determination = parse_report(scope.frame(due), ordinal)
                last_phase, last_determination = phase, determination
                reports += 1
                if determination != "PASS":
                    status = "STOPPED_ON_NONPASS"
                    break
                passes += 1
            if reports == len(CASE_IDS) and passes == reports:
                if scope.frame(work_due) != END:
                    raise BoundaryFailure("END_FRAME")
                status = "NATIVE_DIRECTORY_REPORTED_COMPLETE"
        else:
            status = "EARLY_STOP"
        scope.stop_latch()
        due = min(time.monotonic() + 5.0, hard_due)
        command = STOP + (b"EXTRA\n" if case == "EXTRA_AFTER_STOP" else b"")
        task = scope.write("command", command, due, stopping=True, close_after=True)
        scope.wait_write(task, due, protective=True)
        if scope.frame(due, protective=True) != STOPPED:
            raise BoundaryFailure("STOPPED_FRAME")
        require_eof(scope, due)
        while not scope.exited():
            scope.check(due, protective=True)
            scope.monitor_zero()
            time.sleep(0.002)
        if scope.exit_code() != 0:
            raise BoundaryFailure("NONZERO_EXIT_AFTER_HANDSHAKE")
        # Even 158 PASS frames remain unverified child metadata.
    except BaseException as original:
        _HELD_PROTOCOL_ERRORS.append((case, original))
        scope.keep_error("PROTOCOL", original)
        status = "PROTECTED_STOP"
        if type(original) is BoundaryFailure:
            reason = original.args[0]  # Fixed local code, not subject error text.
        else:
            reason = "NATIVE_IO_OR_RUNTIME_ERROR"
    finally:
        cleanup_due = min(time.monotonic() + 5.0, hard_due)
        # A report-close can precede the interpreter's natural nonzero exit.
        # Stop new work immediately, then give only this protective observation
        # a short portion of the EXISTING cleanup/hard budget, not a reset.
        if status == "PROTECTED_STOP" and scope.resumed and reason in (
                "REPORT_EOF", "NATIVE_IO_OR_RUNTIME_ERROR", "STOP_LATCHED"):
            scope.stop_latch()
            grace_due = min(time.monotonic() + 0.1, cleanup_due)
            while time.monotonic() < grace_due:
                try:
                    if scope.exited() and scope.active() == 0:
                        break
                    scope.monitor_zero()
                except BaseException as secondary:
                    scope.keep_error("NATURAL_EXIT_OBSERVATION", secondary)
                    break
                time.sleep(0.002)
        clean = scope.settle(cleanup_due, terminate=status == "PROTECTED_STOP")
    if any(scope.standard_detected.values()):
        status = "PROTECTED_STOP"
        role = "stdout" if scope.standard_detected["stdout"] else "stderr"
        reason = "FORBIDDEN_" + role.upper() + "_BYTE"
    return {
        "case": case, "status": status, "reason": reason,
        "reports": reports, "pass_reports": passes,
        "native_supplement_reports": supplement,
        "ready_observed": ready_observed,
        "last_report_phase": last_phase,
        "last_report_determination": last_determination,
        "child_created": scope.created, "child_resumed": scope.resumed,
        "dispatch_attempts_or_unknown": attempted,
        "tail_status": "NOT_INFERRED_FROM_REPORTS",
        "qualification": "UNVERIFIED_REPORT",
        "standard_bytes_detected": dict(scope.standard_detected),
        "standard_eof_observed": {role: scope.eof.get(role, False) for role in ("stdout", "stderr")},
        "maximum_active_observed": maximum_active,
        "active_after_stop": scope.last_active,
        "direct_exit_observed": scope.observed_exit,
        "kill_requested": scope.kill_requested, "kill_returned": scope.kill_returned,
        "writers_settled": scope.writers_settled(),
        "native_errors_held": len(scope.errors),
        "cleanup_errors_held": len(scope.cleanup_errors),
        "scope_clean_observed": clean,
    }
