<#
DSP-004 outer controller, REV1 SOURCE CANDIDATE ONLY.

Materialization authority: conversation authorization 47308, following the
limited adoption of scope design 86253 REV2 and adaptation 50784 REV2.
This source is NOT accepted, admitted, integrated, loaded, or executed by its
creation or static parsing. Definitions below have not been invoked.

Implemented scope: fixed contract copies, in-memory byte/framing checks,
classification of caller-supplied read/write observations, a fixed future
Python bootstrap literal, and an unconditional single-case startup refusal.
NOT IMPLEMENTED: trusted authority/binding acquisition, disk reads, process
creation, stream adapters, concurrent scheduling, task ownership, timers,
bounded stop/cleanup, or result publication. There is no enable switch.
The bootstrap is inert text, not an alternative launcher or public code loader.

Only function definitions occur at script top level. There is no automatic
entry, host output, environment mutation, import, hook, or global registration.
This structural property does NOT prove silent/safe loading: parsing, parameter
conversion, allocation, runtime errors and outer host logging remain unverified.
Loading/invocation still requires separate authority and an externally bound
load/early-output/consumption channel. Pure checks establish neither authority
nor the truth of their supplied observations. They must not be used as an
execution-readiness, source-admission, acceptance, or aggregate PASS interface.

All upstream LIMITED remain, including the two review limitations, five actual
capability limitations, item 8 provenance/re-review scope, registration history,
cleanup observation, same-call causality, and extreme/repeated interruption.
No real-person identity is required or inferred. No governance-token, signature
service, new coordination-system interface, actual capture or provider is added.
DSP-004: OPEN / HOLD. B-01 / B-02: OPEN.
Overall input: PARTIAL_OBSERVABLE / NOT_RUN.
#>

function Get-DSP004CaseContract {
    # Fresh fixed records only. Membership is NOT case execution permission.
    @(
        @{ CaseId = 'FULL_ENTRY_LITERAL_RECORDS'; Level = 'FULL_ENTRY_LOCAL_OBSERVATION'; Observation = 'LOCAL_ASSERTIONS_OBSERVED' }
        @{ CaseId = 'FULL_ENTRY_OCCUPIED_SLOT'; Level = 'FULL_ENTRY_PRECONDITION_REFUSAL'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_SYNTHETIC_SHA_REFUSAL'; Level = 'NON_ASSET_PRIVATE_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_OWNED_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'LOCAL_ASSERTIONS_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_MISSING_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_REPLACED_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_TABLE_IDENTITY'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'CARRIER_REFERENCE_CONSTRUCTION'; Level = 'SYNTHETIC_CARRIER_CONSTRUCTION'; Observation = 'CONSTRUCTION_ASSERTIONS_OBSERVED' }
    )
}

function Get-DSP004StatusCombinations {
    # Exactly eight fixed normal tuples, sixteen corresponding stop tuples,
    # and two protection tuples; never a Cartesian product of status words.
    foreach ($dspCase in (Get-DSP004CaseContract)) {
        '{0}|{1}|{2}|END_CASE' -f $dspCase.CaseId, $dspCase.Level, $dspCase.Observation
        '{0}|{1}|NOT_RUN|STOP_BATCH' -f $dspCase.CaseId, $dspCase.Level
        '{0}|{1}|INCOMPLETE|STOP_BATCH' -f $dspCase.CaseId, $dspCase.Level
    }
    'DRIVER_ALREADY_USED|NO_NEW_OBSERVATION|NOT_RUN|STOP_BATCH'
    'UNBOUND_CASE|NO_OBSERVATION|NOT_RUN|STOP_BATCH'
}

function Get-DSP004FixedContract {
    # New in-memory copies on each call; no filesystem or environment inquiry.
    [pscustomobject]@{
        CandidateQualification = 'SOURCE CANDIDATE ONLY - NOT EXECUTION READY'
        DriverPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_VALIDATION_DRIVER_REV1.py'
        DriverSha256 = '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210'
        DriverBodyBytes = 20177
        DriverInputCeiling = 65536
        DriverTailDetectionBytes = 1
        CallerPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_CALLER_CANDIDATE_REV1.py'
        CallerSha256 = 'EF554C3051318BD305EDE6B8511C433C1BB9E20B10E93E5FB5F71C9AFF7A7E63'
        ReaderPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py'
        ReaderSha256 = 'AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727'
        BaselinePath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md'
        BaselineSha256 = 'BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368'
        StdoutBodyBudget = 256
        StdoutDetectionBudget = 1
        StderrBodyBudget = 0
        StderrDetectionBudget = 1
        WholeCaseDeadlineSeconds = 30
        StopConfirmationMaximumSeconds = 5
        FrameMarker = 'DSP004-STATUS-V1'
        CaseContract = @(Get-DSP004CaseContract)
        StatusCombinations = @(Get-DSP004StatusCombinations)
        OuterReasons = @('START_NOT_PERMITTED', 'START_FAILED', 'INPUT_REJECTED', 'OUTPUT_REJECTED', 'TIMEOUT', 'EXIT_UNCONFIRMED')
        AuthorityChannel = 'UNBOUND - NO ACCEPTANCE OR ENABLE INTERFACE'
        ControllerFullShaBinding = 'EXTERNAL - NOT SELF-COMPUTED AUTHORITY'
        BootstrapTextEncodingAndShaBinding = 'EXTERNAL - UNBOUND'
        LiveAdapters = 'NOT IMPLEMENTED - START REFUSED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
}

function Test-DSP004RequestedCaseText {
    param([AllowNull()][object]$CaseId)
    if ($CaseId -isnot [string]) {
        return $false
    }
    foreach ($dspCase in (Get-DSP004CaseContract)) {
        if ([string]::Equals($CaseId, $dspCase.CaseId, [StringComparison]::Ordinal)) {
            return $true
        }
    }
    return $false
}

function Test-DSP004DriverBytesInMemory {
    param([AllowNull()][object]$Payload)
    # No source access. A local clone is not an externally frozen snapshot or
    # proof against concurrent mutation during copying; no bytes are forwarded.
    $dspCode = 'NATIVE_BYTES_REQUIRED'
    if ($Payload -is [byte[]]) {
        $dspLength = [Buffer]::ByteLength($Payload)
        if ($dspLength -ne 20177) {
            $dspCode = 'EXACT_DRIVER_LENGTH_REQUIRED'
        }
        else {
            [byte[]]$dspCopy = [byte[]]::new(20177)
            [Buffer]::BlockCopy($Payload, 0, $dspCopy, 0, 20177)
            $dspHash = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($dspCopy))
            if ([string]::Equals($dspHash, '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210', [StringComparison]::Ordinal)) {
                $dspCode = 'FIXED_BYTE_IDENTITY_MATCH_ONLY'
            }
            else {
                $dspCode = 'FIXED_DRIVER_SHA_MISMATCH'
            }
        }
    }
    [pscustomobject]@{
        TextCheck = $dspCode
        Authority = 'NOT ESTABLISHED'
        SourceAdmission = 'NOT ESTABLISHED'
        FrozenHandoff = 'NOT IMPLEMENTED'
        ChildLengthEofShaVerification = 'NOT OBSERVED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
}

function Test-DSP004FrameBytesInMemory {
    param([AllowNull()][object]$Payload, [AllowNull()][object]$RequestedCase)
    # Pure framing inspection, not stream EOF, process exit, authority or task
    # settlement. Returned minimal codes are not a consumable driver result.
    $dspCode = 'FRAME_REJECTED'
    $dspAction = 'NO_MATCH'
    $dspProtection = $false
    $dspLength = 0
    if ($Payload -is [byte[]]) {
        $dspLength = [Buffer]::ByteLength($Payload)
    }
    if ((Test-DSP004RequestedCaseText -CaseId $RequestedCase) -and
        $Payload -is [byte[]] -and $dspLength -ge 1 -and $dspLength -le 256) {
        [byte[]]$dspCopy = [byte[]]::new($dspLength)
        [Buffer]::BlockCopy($Payload, 0, $dspCopy, 0, $dspLength)
        $dspAscii = $true
        for ($dspIndex = 0; $dspIndex -lt $dspLength; $dspIndex++) {
            if ($dspIndex -eq ($dspLength - 1)) {
                if ($dspCopy[$dspIndex] -ne 10) { $dspAscii = $false }
            }
            elseif ($dspCopy[$dspIndex] -lt 33 -or $dspCopy[$dspIndex] -gt 126) {
                $dspAscii = $false
            }
        }
        if ($dspAscii) {
            $dspBody = [Text.Encoding]::ASCII.GetString($dspCopy, 0, $dspLength - 1)
            $dspPrefix = 'DSP004-STATUS-V1|'
            if ($dspBody.StartsWith($dspPrefix, [StringComparison]::Ordinal)) {
                $dspTuple = $dspBody.Substring($dspPrefix.Length)
                foreach ($dspAllowed in (Get-DSP004StatusCombinations)) {
                    if ([string]::Equals($dspTuple, $dspAllowed, [StringComparison]::Ordinal)) {
                        $dspParts = $dspTuple.Split('|')
                        $dspProtection = [string]::Equals($dspParts[0], 'DRIVER_ALREADY_USED', [StringComparison]::Ordinal) -or
                            [string]::Equals($dspParts[0], 'UNBOUND_CASE', [StringComparison]::Ordinal)
                        if ($dspProtection -or [string]::Equals($dspParts[0], $RequestedCase, [StringComparison]::Ordinal)) {
                            $dspCode = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                            $dspAction = $dspParts[3]
                        }
                        break
                    }
                }
            }
        }
    }
    [pscustomobject]@{
        TextCheck = $dspCode
        RecordedAction = $dspAction
        ProtectionRecord = $dspProtection
        Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
        PeerEof = 'NOT OBSERVED'
        TaskSettlement = 'NOT OBSERVED'
        ProcessExit = 'NOT OBSERVED'
        Deadline = 'NOT OBSERVED'
        Authority = 'NOT ESTABLISHED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
}

function Get-DSP004ReadObservationClassification {
    param(
        [AllowNull()][object]$Channel,
        [AllowNull()][object]$BodyBytesBefore,
        [AllowNull()][object]$RequestedCount,
        [AllowNull()][object]$OriginalTaskState,
        [AllowNull()][object]$ReturnedCount,
        [AllowNull()][object]$ReadEndLocallyClosed,
        [AllowNull()][object]$StopLatched
    )
    # All events are caller-supplied records; this function never performs a
    # read, proves EOF, owns a task, or authorizes normal result publication.
    $dspCode = 'INVALID_REPORTED_READ_RECORD'
    $dspBodyAfter = $null
    $dspTail = 'NOT CLASSIFIED'
    $dspShape = $Channel -is [string] -and $BodyBytesBefore -is [int] -and
        $RequestedCount -is [int] -and $ReturnedCount -is [int] -and
        $OriginalTaskState -is [string] -and $ReadEndLocallyClosed -is [bool] -and
        $StopLatched -is [bool]
    if ($dspShape -and ($Channel -ceq 'STDOUT' -or $Channel -ceq 'STDERR')) {
        $dspBudget = if ($Channel -ceq 'STDOUT') { 256 } else { 0 }
        if ($BodyBytesBefore -ge 0 -and $BodyBytesBefore -le $dspBudget -and
            $RequestedCount -gt 0 -and $RequestedCount -le ($dspBudget - $BodyBytesBefore + 1) -and
            @('PENDING', 'RAN_TO_COMPLETION', 'FAULTED', 'CANCELED', 'SYNCHRONOUS_FAILURE') -ccontains $OriginalTaskState -and
            (($OriginalTaskState -ceq 'RAN_TO_COMPLETION' -and $ReturnedCount -ge 0 -and $ReturnedCount -le $RequestedCount) -or
             ($OriginalTaskState -cne 'RAN_TO_COMPLETION' -and $ReturnedCount -eq -1))) {
            if ($StopLatched -or $ReadEndLocallyClosed) {
                $dspCode = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
            }
            elseif ($OriginalTaskState -ceq 'RAN_TO_COMPLETION' -and
                $ReturnedCount -ge 0 -and $ReturnedCount -le $RequestedCount) {
                if ($ReturnedCount -eq 0) {
                    $dspCode = 'REPORTED_POSITIVE_NORMAL_READ_ZERO_ONLY'
                    $dspBodyAfter = $BodyBytesBefore
                }
                elseif (($BodyBytesBefore + $ReturnedCount) -gt $dspBudget) {
                    $dspCode = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
                    $dspTail = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'
                }
                else {
                    $dspCode = 'REPORTED_BODY_BYTES_ONLY - SHORT_READ_IS_NOT_EOF'
                    $dspBodyAfter = $BodyBytesBefore + $ReturnedCount
                }
            }
            elseif ($OriginalTaskState -ceq 'PENDING' -and $ReturnedCount -eq -1) {
                $dspCode = 'ORIGINAL_READ_PENDING - NO EOF_INFERENCE'
            }
            elseif (($OriginalTaskState -ceq 'FAULTED' -or $OriginalTaskState -ceq 'CANCELED' -or
                $OriginalTaskState -ceq 'SYNCHRONOUS_FAILURE') -and $ReturnedCount -eq -1) {
                $dspCode = 'REPORTED_READ_FAILURE - NO EOF_INFERENCE'
            }
        }
    }
    [pscustomobject]@{
        Classification = $dspCode
        ReportedBodyBytesAfter = $dspBodyAfter
        DetectionByte = $dspTail
        Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
        ActualPeerEof = 'NOT OBSERVED'
        ResourceOwnership = 'NOT IMPLEMENTED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
}

function Get-DSP004WriteObservationClassification {
    param(
        [AllowNull()][object]$RequestedOffset,
        [AllowNull()][object]$RequestedCount,
        [AllowNull()][object]$OriginalTaskState,
        [AllowNull()][object]$WaitState,
        [AllowNull()][object]$StopLatched
    )
    # Stream.WriteAsync has no byte-count result. No short-write count,
    # resend, normal close or child verification is invented by this classifier.
    $dspCode = 'INVALID_REPORTED_WRITE_RECORD'
    $dspProgress = 'UNKNOWN'
    $dspShape = $RequestedOffset -is [int] -and $RequestedCount -is [int] -and
        $OriginalTaskState -is [string] -and $WaitState -is [string] -and
        $StopLatched -is [bool]
    if ($dspShape -and $RequestedOffset -eq 0 -and $RequestedCount -eq 20177 -and
        @('PENDING', 'RAN_TO_COMPLETION', 'FAULTED', 'CANCELED', 'SYNCHRONOUS_FAILURE') -ccontains $OriginalTaskState -and
        @('PENDING', 'ENDED', 'TIMED_OUT', 'CANCELED', 'FAULTED') -ccontains $WaitState) {
        if ($StopLatched) {
            $dspCode = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
        }
        elseif ($WaitState -ceq 'TIMED_OUT' -or $WaitState -ceq 'CANCELED' -or $WaitState -ceq 'FAULTED') {
            $dspCode = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
        }
        elseif ($OriginalTaskState -ceq 'RAN_TO_COMPLETION') {
            $dspCode = 'REPORTED_FULL_RANGE_TASK_NORMAL_ONLY'
            $dspProgress = 'NO BYTE COUNT - CHILD RECEIPT REMAINS UNVERIFIED'
        }
        elseif ($OriginalTaskState -ceq 'PENDING') {
            $dspCode = 'ORIGINAL_WRITE_PENDING - NO NORMAL_INPUT_CLOSE'
        }
        else {
            $dspCode = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
        }
    }
    [pscustomobject]@{
        Classification = $dspCode
        ActualPartialProgress = $dspProgress
        WriteByteCount = 'NOT RETURNED BY INTERFACE'
        ChildLengthEofShaVerification = 'NOT OBSERVED'
        InputClose = 'NOT PERFORMED'
        AutomaticResend = 'PROHIBITED'
        Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
        ResourceOwnership = 'NOT IMPLEMENTED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
}

function Get-DSP004FutureBootstrapText {
    # Fixed text inside this sole source carrier. Nothing compiles, invokes,
    # imports, sends or substitutes this string in this PowerShell candidate.
    # Its COMPLETE text/encoding/SHA must be externally bound before any use.
    # Future argv: separately bound interpreter, -I, -S, -B, -c, this text,
    # one separately authorized case. No shell string/PATH/fallback launcher.
    # Positive reads may block: parent concurrent bounded I/O/deadline/stop
    # ability is NOT IMPLEMENTED. Early imports, encoding/runtime availability,
    # output failures and extreme interruption still need external containment.
    @'
import sys

_bootstrap_errors = []

def _single_bound_driver_case():
    from hashlib import sha256
    from types import FunctionType, ModuleType

    if not (sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1):
        raise RuntimeError("REQUIRED_STARTUP_FLAGS_ABSENT")
    if type(sys.modules) is not dict or len(sys.argv) != 2:
        raise RuntimeError("STARTUP_ARGUMENT_OR_MODULE_TABLE_UNBOUND")
    driver_name = "dsp004_handoff_validation_driver_controlled_entry_rev1"
    driver_path = "C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_VALIDATION_DRIVER_REV1.py"
    digest = "6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210"
    cases = (
        ("FULL_ENTRY_LITERAL_RECORDS", "FULL_ENTRY_LOCAL_OBSERVATION", "LOCAL_ASSERTIONS_OBSERVED"),
        ("FULL_ENTRY_OCCUPIED_SLOT", "FULL_ENTRY_PRECONDITION_REFUSAL", "EXPECTED_REFUSAL_OBSERVED"),
        ("HELPER_SYNTHETIC_SHA_REFUSAL", "NON_ASSET_PRIVATE_HELPER_PROBE", "EXPECTED_REFUSAL_OBSERVED"),
        ("HELPER_CLEAN_OWNED_SLOT", "SYNTHETIC_CLEANUP_HELPER_PROBE", "LOCAL_ASSERTIONS_OBSERVED"),
        ("HELPER_CLEAN_MISSING_SLOT", "SYNTHETIC_CLEANUP_HELPER_PROBE", "EXPECTED_REFUSAL_OBSERVED"),
        ("HELPER_CLEAN_REPLACED_SLOT", "SYNTHETIC_CLEANUP_HELPER_PROBE", "EXPECTED_REFUSAL_OBSERVED"),
        ("HELPER_CLEAN_TABLE_IDENTITY", "SYNTHETIC_CLEANUP_HELPER_PROBE", "EXPECTED_REFUSAL_OBSERVED"),
        ("CARRIER_REFERENCE_CONSTRUCTION", "SYNTHETIC_CARRIER_CONSTRUCTION", "CONSTRUCTION_ASSERTIONS_OBSERVED"),
    )
    case_id = sys.argv[1]
    if type(case_id) is not str or case_id not in tuple(row[0] for row in cases):
        raise RuntimeError("UNBOUND_REQUESTED_CASE")
    if driver_name in sys.modules:
        raise RuntimeError("PREEXISTING_DRIVER_MODULE_SLOT")
    payload = bytearray()
    while len(payload) < 20177:
        chunk = sys.stdin.buffer.read(20177 - len(payload))
        if type(chunk) is not bytes or not chunk or len(chunk) > 20177 - len(payload):
            raise RuntimeError("DRIVER_BODY_INCOMPLETE_OR_INVALID")
        payload.extend(chunk)
    tail = sys.stdin.buffer.read(1)
    if type(tail) is not bytes or tail != b"":
        raise RuntimeError("DRIVER_EOF_NOT_CONFIRMED")
    driver_bytes = bytes(payload)
    if len(driver_bytes) != 20177 or sha256(driver_bytes).hexdigest().upper() != digest:
        raise RuntimeError("DRIVER_FIXED_LENGTH_OR_SHA_MISMATCH")
    module = ModuleType(driver_name)
    module.__file__ = driver_path
    namespace = module.__dict__
    code = compile(driver_bytes, driver_path, "exec", dont_inherit=True, optimize=0)
    exec(code, namespace)
    if driver_name in sys.modules:
        raise RuntimeError("DRIVER_WAS_REGISTERED")
    entry = namespace["run_single_synthetic_case"]
    if type(entry) is not FunctionType or entry.__globals__ is not namespace:
        raise RuntimeError("DRIVER_ENTRY_NAMESPACE_MISMATCH")
    result = entry(case_id)
    if type(result) is not tuple or len(result) != 4 or any(type(value) is not str for value in result):
        raise RuntimeError("DRIVER_RESULT_NOT_NATIVE_FOUR_STRINGS")
    allowed = set()
    for name, level, observation in cases:
        allowed.add((name, level, observation, "END_CASE"))
        allowed.add((name, level, "NOT_RUN", "STOP_BATCH"))
        allowed.add((name, level, "INCOMPLETE", "STOP_BATCH"))
    protections = {
        ("DRIVER_ALREADY_USED", "NO_NEW_OBSERVATION", "NOT_RUN", "STOP_BATCH"),
        ("UNBOUND_CASE", "NO_OBSERVATION", "NOT_RUN", "STOP_BATCH"),
    }
    allowed.update(protections)
    if result not in allowed or (result not in protections and result[0] != case_id):
        raise RuntimeError("DRIVER_RESULT_COMBINATION_MISMATCH")
    frame = ("DSP004-STATUS-V1|" + "|".join(result) + "\n").encode("ascii", errors="strict")
    if len(frame) > 256:
        raise RuntimeError("FRAME_BODY_OVER_BUDGET")
    if sys.stdout.buffer.write(frame) != len(frame):
        raise RuntimeError("STATUS_WRITE_INCOMPLETE")
    sys.stdout.buffer.flush()

_exit_code = 1
try:
    _single_bound_driver_case()
    _exit_code = 0
except BaseException as _error:
    _bootstrap_errors.append(_error)
    # Real object only; no fabricated tuple, message, traceback, repr or ACK.
    # A partial frame on write failure is not repaired or resent.
sys.exit(_exit_code)
'@
}

function Invoke-DSP004SingleCase {
    param([AllowNull()][object]$RequestedCase)
    # Intentional unconditional denial before all side effects. This source has
    # no trusted external acquisition/verification channel and no live adapters.
    # Neither a bool/string/environment value nor a pure-check result can open
    # this entry. It deliberately does not inspect or dispatch user input before
    # refusal (including no dynamic GetType/ToString or helper call). There is no
    # bootstrap invocation or public I/O helper bypass.
    # The fixed text getter is not permission to run that text independently.
    [pscustomobject]@{
        Disposition = 'START_REFUSED_UNBOUND'
        FirstOuterReason = 'START_NOT_PERMITTED'
        SecondaryOuterReasons = @()
        RequestQualification = 'NOT INSPECTED - TRUSTED BINDING CHANNEL ABSENT'
        AuthorityBinding = 'UNBOUND'
        CreationObservation = 'NOT_ATTEMPTED_BY_THIS_ENTRY'
        TechnicalObservation = 'NOT_RUN'
        DriverStatus = $null
        CaseCompletion = 'NOT ESTABLISHED'
        ResultPublication = 'NOT PERFORMED'
        NextCase = 'PROHIBITED'
        StopLock = 'START REFUSED - LIVE STOP COORDINATOR NOT IMPLEMENTED'
    }
}

<#
Preserved future live-flow contract; NONE of this is implemented by comments.

1. No side effect may start before externally verified exact per-case read/use,
   probe/output/stop authority, accepted scope, revocation/kill state, source
   identity/admission, frozen same-byte snapshot and no-shared-writer boundary.
   Full controller/bootstrap SHA, trusted load channel, interpreter/dependencies,
   absolute workdir, encoding/argv retention and outer consumer must be bound.
2. A future separately authorized revision must implement redirected startup,
   concurrent stdin/stdout/stderr/deadline work, original operation ownership and
   separate wait-wrapper ownership. No serial send/exit wait before reads.
3. Positive reads only; remaining body budget + one detection byte is the upper
   request bound. Exhausted body budgets still require positive one-byte reads.
   Short reads, local close/dispose, cancellation, faults, wrapper timeout or a
   late zero after stop are not valid EOF. No unlimited drain or raw forwarding.
4. WriteAsync full-range normal task completion is not child receipt/EOF/SHA
   verification. Fault/cancel/timeout partial progress stays UNKNOWN; no resend.
   Normal input close follows normal full request completion and is distinct
   from stop-close; closing/disposing is not automatically complete or bounded.
5. Whole-case monotonic deadline is thirty seconds, anchored no later than first
   driver read or creation attempt, covering prechecks/create/send/case/exit/EOF
   and task settlement. No per-phase reset. At most five seconds after ending
   request for stop confirmation, without extending valid result consumption.
6. First stop latches irreversibly, discards unpublished results, forbids another
   case and coordinates bounded close/cancel/kill/settlement without blocking
   other stop responsibilities. Cleanup calls themselves must be bounded; a
   wrapper timeout does not stop the original operation. Request is not response.
   Kill return and parent process exit do not prove all descendants ended.
7. Retain original tasks/resources until actual settlement. Process exit, double
   EOF, input/close settlement, output operations and monitors are separate facts.
   Publication needs every gate, unique complete valid frame/case, exit zero,
   whole-case deadline, no stop, and independently bound outer consumption.
   Protection tuples and ALL STOP_BATCH tuples never count as case completion.
8. First/secondary six fixed outer reasons remain separate from driver tuples.
   Unknown creation => START_FAILED / HOLD / UNCONFIRMED, never confirmed NOT_RUN.
   Unconfirmed process exit => EXIT_UNCONFIRMED / HOLD. Known process exit with
   unsettled tasks => HOLD / settlement unconfirmed, not EXIT_UNCONFIRMED or an
   invented input/output fault. Cleanup failure must not replace first reason.
9. Real failures remain actual technical-process objects per fixed driver/caller;
   cross-process minimal classifications never replace those objects or invent
   a driver failure stage. No raw bytes/source/messages/tracebacks/persistent log.

Absent bindings/implementations keep the sole entry refused. This candidate
does not use a grant field, mock completion, debug callback, alternate launcher,
test mode, batch loop, retry, reload, config, second source, or external service.
#>
