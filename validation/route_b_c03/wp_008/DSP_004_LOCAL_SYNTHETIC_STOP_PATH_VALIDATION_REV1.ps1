# Authorized NEW local closed synthetic test batch. Preserve all fixed files.
# This independent test adapter does NOT exercise REV2's public runtime entry.
# No real driver/materials, source admission, actual capture or integration.
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$WarningPreference='Stop'
$ProgressPreference='SilentlyContinue'
$PSModuleAutoLoadingPreference='None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskRoot='C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008'
$taskRev2Sha='FA6625FA2917B056801A598B445C3A68E86A147C2A237260893A784B4449A066'
$taskCarrierSha='14A50ABB4AF415316A862572197162BB1A4DA5C79C277FD255587E3D84C4041B'
$taskChecks=[Collections.Generic.List[object]]::new()
$taskCases=@()
$taskRepeat=@()
$taskCompiled=$false
$taskPrimaryType=$null
$taskOriginalException=$null
$taskBatchCalls=0
$taskRefusalCalls=0

function Add-ObservedCheck {
    param([string]$Id,[bool]$Condition,[string]$Scope)
    [void]$taskChecks.Add([pscustomobject][ordered]@{Id=$Id; Scope=$Scope; Passed=$Condition})
    if(-not $Condition){throw [InvalidOperationException]::new('OBSERVED_SYNTHETIC_CHECK_FAILED')}
}

try {
    $taskRev2Bytes=[IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot,'DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_SUPERVISOR_REV2.cs'))
    $taskCarrierBytes=[IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot,'DSP_004_LOCAL_SYNTHETIC_STOP_PATH_CARRIER_REV1.cs'))
    if($taskRev2Bytes.Length -ne 16018 -or [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskRev2Bytes)) -cne $taskRev2Sha){throw [InvalidOperationException]::new('ACCEPTED_REV2_SOURCE_MISMATCH')}
    if($taskCarrierBytes.Length -ne 15590 -or [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskCarrierBytes)) -cne $taskCarrierSha){throw [InvalidOperationException]::new('NEW_CARRIER_SOURCE_MISMATCH')}
    if($null -ne [Management.Automation.PSTypeName]::new('Dsp004SyntheticStops.Dsp004LocalSyntheticStopPathCarrierRev1').Type){throw [InvalidOperationException]::new('PREEXISTING_CARRIER_TYPE')}
    $taskSource=[Text.UTF8Encoding]::new($false,$true).GetString($taskRev2Bytes)+[char]10+[Text.UTF8Encoding]::new($false,$true).GetString($taskCarrierBytes)
    [void](Microsoft.PowerShell.Utility\Add-Type -TypeDefinition $taskSource -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
    $taskCompiled=$true
    $taskType=[Management.Automation.PSTypeName]::new('Dsp004SyntheticStops.Dsp004LocalSyntheticStopPathCarrierRev1').Type
    $taskFlags=[Reflection.BindingFlags]::Public -bor [Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::Static -bor [Reflection.BindingFlags]::DeclaredOnly
    $taskMethods=@($taskType.GetMethods($taskFlags)|Where-Object{-not $_.IsSpecialName})
    Add-ObservedCheck 'API-01' ($taskType.IsSealed -and $taskType.GetConstructors().Count -eq 0 -and $taskMethods.Count -eq 1 -and $taskMethods[0].Name -ceq 'RunFixedSyntheticBatch' -and $taskMethods[0].GetParameters().Count -eq 0) 'New test carrier has one fixed zero-argument entry; no path/script/clock injection'
    $taskBatchCalls++
    $taskCases=@([Dsp004SyntheticStops.Dsp004LocalSyntheticStopPathCarrierRev1]::RunFixedSyntheticBatch())
    $taskById=[ordered]@{}
    foreach($taskCase in $taskCases){if($taskById.Contains($taskCase.CaseId)){throw [InvalidOperationException]::new('DUPLICATE_CASE')}; $taskById[$taskCase.CaseId]=$taskCase}
    Add-ObservedCheck 'SET-01' ($taskCases.Count -eq 7 -and $taskById.Count -eq 7) 'Seven unique live synthetic scenario records'
    $taskExpectedReasons=[ordered]@{ 'S-01'='SYNTHETIC_CONTROL_CAPTURED_ONLY'; 'S-02'='SYNTHETIC_TEST_DEADLINE'; 'S-03'='STDOUT_OVER_BUDGET'; 'S-04'='UNEXPECTED_STDERR'; 'S-05'='ACK_ABSENT'; 'S-06'='NONZERO_CHILD_EXIT'; 'S-07'='START_FAILURE' }
    foreach($taskEntry in $taskExpectedReasons.GetEnumerator()) {
        $taskCase=$taskById[$taskEntry.Key]
        Add-ObservedCheck ($taskEntry.Key+'-CAUSE') ($taskCase.FirstReason -ceq $taskEntry.Value) 'Independent fixed expected cause, not generated from returned outcome'
        Add-ObservedCheck ($taskEntry.Key+'-SCOPE') ($taskCase.ObservationScope -ceq 'NEW INDEPENDENT SYNTHETIC TEST ADAPTER; NOT REV2 PUBLIC RUNTIME PATH' -and $taskCase.AckQualification -ceq 'SYNTHETIC OUTPUT FRAME ONLY; NO INPUT SHA VERIFICATION OR AUTHORITY' -and $taskCase.Authority -ceq 'NOT ESTABLISHED' -and $taskCase.SourceAdmission -ceq 'NOT ESTABLISHED') 'Literal scope/authority disclaimers only; not independent non-execution proof'
        if($taskEntry.Key -ceq 'S-01') {
            $taskState=$taskCase.StartAttempted -and $taskCase.ChildStarted -and $taskCase.ChildExitObserved -and $taskCase.ExitCode -eq 0 -and -not $taskCase.StopLatched -and $taskCase.ControlBodyRecorded -and $taskCase.SyntheticFrameQualified -and $null -eq $taskCase.PrimaryFailureType
            $taskRead=$taskCase.StdoutTaskEnded -and $taskCase.StderrTaskEnded -and $taskCase.StdoutEofObserved -and $taskCase.StderrEofObserved
        } elseif($taskEntry.Key -ceq 'S-07') {
            $taskState=$taskCase.StartAttempted -and -not $taskCase.ChildStarted -and -not $taskCase.ChildExitObserved -and $taskCase.StopLatched -and -not $taskCase.ControlBodyRecorded -and -not $taskCase.SyntheticFrameQualified -and $taskCase.StopResultNotRestored -and -not $taskCase.KillRequested -and $taskCase.ExitCode -eq -1
            $taskRead=-not $taskCase.StdoutTaskEnded -and -not $taskCase.StderrTaskEnded -and -not $taskCase.StdoutEofObserved -and -not $taskCase.StderrEofObserved -and $taskCase.StdoutReadCount -eq -1 -and $taskCase.StderrReadCount -eq -1
        } else {
            $taskState=$taskCase.StartAttempted -and $taskCase.ChildStarted -and $taskCase.ChildExitObserved -and $taskCase.StopLatched -and -not $taskCase.ControlBodyRecorded -and -not $taskCase.SyntheticFrameQualified -and $taskCase.StopResultNotRestored -and $taskCase.CompletionDecisionElapsedMilliseconds -eq -1 -and $null -ne $taskCase.PrimaryFailureType
            $taskRead=$taskCase.StdoutTaskEnded -and $taskCase.StderrTaskEnded
        }
        Add-ObservedCheck ($taskEntry.Key+'-STATE') $taskState 'Actual local state combination; stop never restores body/confirmation qualification'
        Add-ObservedCheck ($taskEntry.Key+'-READ') $taskRead 'Actual observed read-task state; absent tasks are not reported as EOF'
        Add-ObservedCheck ($taskEntry.Key+'-CLEAN') ($taskCase.LocalProcessDisposeReturned -and $taskCase.SecondaryFailureCount -eq 0) 'Dispose returned and no secondary failure observed; NOT full resource/descendant settlement'
    }
    $taskBodyBytes=[Text.Encoding]::ASCII.GetByteCount('{"synthetic":"CONTROL_ONLY"}'+[char]10)
    $taskFrameBytes=23+$taskBodyBytes
    Add-ObservedCheck 'CONTROL-01' ($taskById['S-01'].StdoutReadCount -eq $taskFrameBytes -and $taskById['S-01'].StderrReadCount -eq 0 -and $taskById['S-01'].CompletionDecisionElapsedMilliseconds -ge 0 -and $taskById['S-01'].CompletionDecisionElapsedMilliseconds -lt 5000) 'Exact independent synthetic control byte count and short normal sample'
    Add-ObservedCheck 'TIMEOUT-01' ($taskById['S-02'].ElapsedMilliseconds -ge 5000 -and $taskById['S-02'].ElapsedMilliseconds -lt 9000 -and $taskById['S-02'].KillRequested -and $taskById['S-02'].KillCallReturned -and $taskById['S-02'].StdoutEofObserved -and $taskById['S-02'].StderrEofObserved -and $taskById['S-02'].StdoutReadCount -eq $taskFrameBytes -and $taskById['S-02'].PrimaryFailureType -ceq 'System.TimeoutException') 'Real short timeout and this child exit/read completion only; synthetic body stays discarded'
    Add-ObservedCheck 'STDOUT-01' ($taskById['S-03'].StdoutReadCount -eq 65537 -and -not $taskById['S-03'].StdoutEofObserved -and $taskById['S-03'].KillRequested -and $taskById['S-03'].KillCallReturned) 'One stdout detection byte; no fabricated normal EOF after stopping read'
    Add-ObservedCheck 'STDERR-01' ($taskById['S-04'].StderrReadCount -eq 1 -and -not $taskById['S-04'].StderrEofObserved -and $taskById['S-04'].KillRequested -and $taskById['S-04'].KillCallReturned) 'One stderr detection byte; zero body budget respected'
    Add-ObservedCheck 'MISSINGACK-01' ($taskById['S-05'].ExitCode -eq 0 -and $taskById['S-05'].StdoutReadCount -eq $taskBodyBytes -and $taskById['S-05'].StdoutEofObserved -and -not $taskById['S-05'].KillRequested) 'Exit zero/EOF cannot repair absent synthetic confirmation'
    Add-ObservedCheck 'NONZERO-01' ($taskById['S-06'].ExitCode -eq 7 -and $taskById['S-06'].StdoutReadCount -eq $taskFrameBytes -and $taskById['S-06'].StdoutEofObserved -and -not $taskById['S-06'].KillRequested) 'Actual nonzero exit with body discarded by this NEW test policy'
    Add-ObservedCheck 'STARTFAIL-01' ($taskById['S-07'].PrimaryFailureType -ceq 'System.ComponentModel.Win32Exception') 'Actual fixed missing-executable start failure type'

    $taskRefusalCalls++
    $taskRepeat=@([Dsp004SyntheticStops.Dsp004LocalSyntheticStopPathCarrierRev1]::RunFixedSyntheticBatch())
    Add-ObservedCheck 'REPEAT-01' ($taskRepeat.Count -eq 1 -and $taskRepeat[0].CaseId -ceq 'BATCH-REPEAT' -and $taskRepeat[0].FirstReason -ceq 'REPEATED_TEST_BATCH_REFUSED') 'Actual repeat of new test carrier refused in the same compiled assembly'
    Add-ObservedCheck 'REPEAT-02' (-not $taskRepeat[0].StartAttempted -and -not $taskRepeat[0].ChildStarted -and -not $taskRepeat[0].ControlBodyRecorded -and -not $taskRepeat[0].SyntheticFrameQualified -and $taskRepeat[0].ElapsedMilliseconds -eq -1 -and $taskRepeat[0].TimeQualification -ceq 'NOT TIMED; REPEATED TEST BATCH REFUSED') 'Refused repeat has no invented launch/frame/time observations'
    Add-ObservedCheck 'REPEAT-03' ($taskBatchCalls -eq 1 -and $taskRefusalCalls -eq 1 -and @($taskCases|Where-Object{$_.ChildStarted}).Count -eq 6 -and @($taskCases|Where-Object{$_.StartAttempted}).Count -eq 7) 'Six started synthetic children, seven start attempts, no second batch'
}
catch { $taskOriginalException=$_.Exception; $taskPrimaryType=$_.Exception.GetType().FullName }

$taskFailed=@($taskChecks|Where-Object{-not $_.Passed}).Count
$taskIds=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach($taskCheck in $taskChecks){[void]$taskIds.Add($taskCheck.Id)}
$taskAll=$taskCompiled -and $null -eq $taskPrimaryType -and $taskChecks.Count -eq 47 -and $taskIds.Count -eq 47 -and $taskFailed -eq 0
$taskRecord=[pscustomobject][ordered]@{
    RecordKind='LOCAL_NEW_SYNTHETIC_STOP_ADAPTER_OBSERVATION_NOT_OWNER_ACCEPTANCE'
    Outcome=if($taskAll){'LOCAL_SYNTHETIC_STOP_CHECKS_PASS'}else{'LOCAL_SYNTHETIC_STOP_CHECKS_FAIL'}
    AcceptedRev2SHA256=$taskRev2Sha
    NewTestCarrierSHA256=$taskCarrierSha
    CompileCompleted=$taskCompiled
    BatchCalls=$taskBatchCalls
    RefusalCalls=$taskRefusalCalls
    CheckCount=$taskChecks.Count
    UniqueCheckIds=$taskIds.Count
    FailedChecks=$taskFailed
    PrimaryValidationFailureType=$taskPrimaryType
    Cases=$taskCases
    Repeat=$taskRepeat
    Checks=$taskChecks.ToArray()
    AcceptedRev2PublicEntry='NOT CALLED BY THIS NEW BATCH CODE PATH'
    InputShaVerification='NOT PERFORMED; CONFIRMATION MARKERS ARE FIXED SYNTHETIC OUTPUT'
    Scope='NEW TEST ADAPTER ONLY; SHARED PURE CLASSIFIERS DO NOT TRANSFER REAL REV2 PATH COVERAGE'
    StopQualification='REAL SHORT SINGLE-CHILD OBSERVATIONS ONLY; NOT HARD REALTIME OR COMPLETE DESCENDANT/RESOURCE PROOF'
    ExceptionQualification='ORIGINAL OBJECTS HELD PRIVATELY IN ORIGIN PROCESS ONLY; NO MESSAGE/STACK OR CROSS-PROCESS RETENTION CLAIM'
    Uncovered=[string[]]@('REV2_ACTUAL_120_SECOND_PATH','ALL_DESCENDANT_AND_RESOURCE_SETTLEMENT','SYNCHRONOUS_CALL_HARD_BOUNDS','COMPLEX_CANCEL_AND_RESOURCE_EXHAUSTION','PRIMARY_PLUS_CLEANUP_FAILURE_INJECTION','TRUSTED_ROOT_AND_TRANSITIVE_DEPENDENCIES','POSITIVE_DRIVER_SHA','CALLEE_REFERENCE_AND_FREEZE','FULL_189_ITEM_PLAN')
    Preserved='ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN; NO SOURCE ADMISSION, ACTUAL CAPTURE OR INTEGRATION'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskRecord -Depth 10 -Compress
if($taskAll){exit 0}else{exit 1}
