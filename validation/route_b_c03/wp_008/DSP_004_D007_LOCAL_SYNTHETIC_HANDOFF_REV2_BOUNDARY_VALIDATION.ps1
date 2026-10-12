# NEW authorized local synthetic boundary-validation batch only.
# Preserve all accepted/fixed sources and REV1. No business-source admission,
# actual capture, integration, external model, independent ACOS or other project.
# Pure artificial elapsed samples and ACK fixtures are distinct from live
# process observations. No 120-second/adversarial stop proof is claimed.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME, 'Modules', 'Microsoft.PowerShell.Utility', 'Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskRoot = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008'
$taskSupervisorSha = 'FA6625FA2917B056801A598B445C3A68E86A147C2A237260893A784B4449A066'
$taskTestsSha = 'B76082A7285261603CE559082F84CA3B340DE03FDD20ED201BC3FF305CE9BCCC'
$taskRuntimeChecks = [Collections.Generic.List[object]]::new()
$taskPureChecks = @()
$taskCompiled = $false
$taskNormal = $null
$taskRepeat = $null
$taskChild = $null
$taskNormalCalls = 0
$taskRefusalCalls = 0
$taskPrimaryFailure = $null
$taskRetainedException = $null

function Add-RuntimeCheck {
    param([string]$Id, [bool]$Condition, [string]$Scope)
    [void]$taskRuntimeChecks.Add([pscustomobject][ordered]@{Id=$Id; Scope=$Scope; Passed=$Condition})
    if (-not $Condition) { throw [InvalidOperationException]::new('RUNTIME_OBSERVATION_CHECK_FAILED') }
}

try {
    $taskSupervisorBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_SUPERVISOR_REV2.cs'))
    $taskTestsBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_D007_LOCAL_SYNTHETIC_HANDOFF_REV2_BOUNDARY_TESTS.cs'))
    if ($taskSupervisorBytes.Length -ne 16018 -or [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskSupervisorBytes)) -cne $taskSupervisorSha) { throw [InvalidOperationException]::new('FIXED_SUPERVISOR_SNAPSHOT_MISMATCH') }
    if ($taskTestsBytes.Length -ne 5250 -or [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskTestsBytes)) -cne $taskTestsSha) { throw [InvalidOperationException]::new('FIXED_BOUNDARY_TEST_SNAPSHOT_MISMATCH') }
    if ($null -ne [Management.Automation.PSTypeName]::new('Dsp004D007LocalSyntheticHandoffSupervisorRev2').Type) { throw [InvalidOperationException]::new('PREEXISTING_REV2_TYPE') }
    $taskSource = [Text.UTF8Encoding]::new($false,$true).GetString($taskSupervisorBytes) + [char]10 + [Text.UTF8Encoding]::new($false,$true).GetString($taskTestsBytes)
    [void](Microsoft.PowerShell.Utility\Add-Type -TypeDefinition $taskSource -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
    $taskCompiled = $true
    $taskType = [Management.Automation.PSTypeName]::new('Dsp004D007LocalSyntheticHandoffSupervisorRev2').Type
    $taskFlags = [Reflection.BindingFlags]::Public -bor [Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::Static -bor [Reflection.BindingFlags]::DeclaredOnly
    $taskMethods = @($taskType.GetMethods($taskFlags) | Where-Object{-not $_.IsSpecialName})
    Add-RuntimeCheck 'API-01' ($taskType.IsSealed -and $taskType.GetConstructors().Count -eq 0 -and $taskMethods.Count -eq 1 -and $taskMethods[0].Name -ceq 'RunSingleLocalBatch' -and $taskMethods[0].GetParameters().Count -eq 0) 'Public supervisor entry remains fixed and zero-argument; pure helpers are internal'

    $taskPureChecks = @([Dsp004D007LocalSyntheticHandoffRev2BoundaryTests]::RunPureBoundaryChecks())
    $taskPureIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($taskCheck in $taskPureChecks) { [void]$taskPureIds.Add($taskCheck.Id) }
    if ($taskPureChecks.Count -ne 24 -or $taskPureIds.Count -ne 24 -or @($taskPureChecks | Where-Object{-not $_.Passed}).Count -ne 0) { throw [InvalidOperationException]::new('PURE_SYNTHETIC_BOUNDARY_CHECK_FAILED') }

    # Exactly one real local child run through this new supervisor version.
    $taskNormalCalls++
    $taskNormal = [Dsp004D007LocalSyntheticHandoffSupervisorRev2]::RunSingleLocalBatch()
    Add-RuntimeCheck 'RUN-01' ($taskNormal.Outcome -ceq 'LOCAL_CHILD_NORMAL_RETURN_OBSERVED' -and $taskNormal.ExitCode -eq 0 -and $taskNormal.ChildExitObserved -and $taskNormal.LaunchAttempted) 'Actual normal child exit observation'
    Add-RuntimeCheck 'RUN-02' ($taskNormal.InputCloseReturned -and -not $taskNormal.StopRequested -and $taskNormal.StderrBytes -eq 0 -and $taskNormal.StdoutBytes -gt 0 -and $taskNormal.StdoutBytes -le 65536) 'Actual bounded normal stream/count observations only'
    Add-RuntimeCheck 'RUN-03' ($taskNormal.ChildSnapshotAckQualified -and $taskNormal.InputSnapshotQualification -ceq 'FIXED BOOTSTRAP SNAPSHOT ACK OBSERVED; NOT TRUSTED ROOT OR AUTHORITY') 'Fixed ACK observed and qualified in this normal result; not authority/trust'
    Add-RuntimeCheck 'RUN-04' ($taskNormal.CompletionDecisionElapsedMilliseconds -ge 0 -and $taskNormal.CompletionDecisionElapsedMilliseconds -lt 120000 -and $taskNormal.ElapsedMilliseconds -ge $taskNormal.CompletionDecisionElapsedMilliseconds -and $taskNormal.ElapsedMilliseconds -lt 120000) 'Real normal decision sample within threshold; not hard bounded-stop proof'
    $taskChild = Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject $taskNormal.ChildJsonBody -ErrorAction Stop
    Add-RuntimeCheck 'RUN-05' ($taskChild.Scope -ceq 'LOCAL_SYNTHETIC_SLOT_REFUSAL_AND_SEPARATE_FIXED_HELPER_VALIDATION_ONLY' -and $taskChild.AcceptedSlotSourceSHA256 -ceq '904146E082C2CAE73E2E25BAD1549C15DD076E6E206A6FC0854E18A43DA543B3' -and $taskChild.ControllerSourceSHA256 -ceq '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB') 'Exact target record scope and fixed code snapshot identities'
    $taskChildIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($taskCheck in $taskChild.Checks) { [void]$taskChildIds.Add($taskCheck.Id) }
    Add-RuntimeCheck 'RUN-06' ($taskChild.Outcome -ceq 'LOCAL_SYNTHETIC_CHECKS_PASS' -and $taskChild.CompileCompleted -and $taskChild.CheckCount -eq 85 -and $taskChild.PassedChecks -eq 85 -and $taskChild.FailedChecks -eq 0 -and $taskChild.Checks.Count -eq 85 -and $taskChildIds.Count -eq 85 -and @($taskChild.Checks | Where-Object{-not $_.Passed}).Count -eq 0) '85 existing harness checks observed in THIS new child; not inherited success'
    $taskExpected = [ordered]@{TextCheck='FIXED_DRIVER_SHA_MISMATCH'; Authority='NOT ESTABLISHED'; SourceAdmission='NOT ESTABLISHED'; FrozenHandoff='NOT IMPLEMENTED'; ChildLengthEofShaVerification='NOT OBSERVED'; CaseCompletion='NOT ESTABLISHED'}
    $taskExactFields = @($taskChild.FixedHelperMetadata.PSObject.Properties).Count -eq 6
    foreach ($taskEntry in $taskExpected.GetEnumerator()) { if ($taskChild.FixedHelperMetadata.($taskEntry.Key) -isnot [string] -or $taskChild.FixedHelperMetadata.($taskEntry.Key) -cne $taskEntry.Value) { $taskExactFields = $false } }
    Add-RuntimeCheck 'RUN-07' $taskExactFields 'Exact six independently specified synthetic mismatch metadata values'
    Add-RuntimeCheck 'RUN-08' ($taskChild.SlotPreparationCalls -eq 1 -and $taskChild.SlotRequestCalls -eq 2 -and $taskChild.LocalFixedHelperAttempts -eq 1 -and $taskChild.LocalFixedHelperNormalReturns -eq 1) 'Actual single-child local helper invocation counts'

    # One real repeat call in the SAME compiled supervisor assembly. It must
    # refuse before another child and must not claim an input ACK observation.
    $taskRefusalCalls++
    $taskRepeat = [Dsp004D007LocalSyntheticHandoffSupervisorRev2]::RunSingleLocalBatch()
    Add-RuntimeCheck 'REFUSE-01' ($taskRepeat.Outcome -ceq 'REPEATED_BATCH_REFUSED' -and -not $taskRepeat.LaunchAttempted -and -not $taskRepeat.ChildExitObserved -and $null -eq $taskRepeat.ChildJsonBody) 'Actual same-assembly repeat refused before child launch'
    Add-RuntimeCheck 'REFUSE-02' (-not $taskRepeat.ChildSnapshotAckQualified -and $taskRepeat.InputSnapshotQualification -ceq 'NO QUALIFIED CHILD SNAPSHOT ACK OBSERVATION') 'Refusal does not overstate child input verification'
    Add-RuntimeCheck 'REFUSE-03' ($taskRepeat.CompletionDecisionElapsedMilliseconds -eq -1 -and -not $taskRepeat.InputCloseReturned -and $taskRepeat.StdoutBytes -eq -1 -and $taskRepeat.StderrBytes -eq -1 -and $taskNormalCalls -eq 1 -and $taskRefusalCalls -eq 1) 'No fabricated completion/stream measurements for refused request'
}
catch {
    $taskRetainedException = $_.Exception
    $taskPrimaryFailure = $_.Exception.GetType().FullName
}

$taskRuntimeFailed = @($taskRuntimeChecks | Where-Object{-not $_.Passed}).Count
$taskPureFailed = @($taskPureChecks | Where-Object{-not $_.Passed}).Count
$taskComplete = $taskCompiled -and $null -eq $taskPrimaryFailure -and $taskPureChecks.Count -eq 24 -and $taskPureFailed -eq 0 -and $taskRuntimeChecks.Count -eq 12 -and $taskRuntimeFailed -eq 0
$taskRecord = [pscustomobject][ordered]@{
    RecordKind = 'LOCAL_SYNTHETIC_REV2_BOUNDARY_VALIDATION_NOT_OWNER_ACCEPTANCE'
    Outcome = if($taskComplete){'LOCAL_BOUNDARY_BATCH_PASS'}else{'LOCAL_BOUNDARY_BATCH_FAIL'}
    SupervisorSourceSHA256 = $taskSupervisorSha
    BoundaryTestsSourceSHA256 = $taskTestsSha
    CompileCompleted = $taskCompiled
    PureBoundaryCheckCount = $taskPureChecks.Count
    PureBoundaryFailed = $taskPureFailed
    PureBoundaryChecks = $taskPureChecks
    RuntimeCheckCount = $taskRuntimeChecks.Count
    RuntimeFailed = $taskRuntimeFailed
    RuntimeChecks = $taskRuntimeChecks.ToArray()
    PrimaryFailureType = $taskPrimaryFailure
    NormalSupervisorCalls = $taskNormalCalls
    RefusedSupervisorCalls = $taskRefusalCalls
    NormalSupervisorObservation = $taskNormal
    RefusedSupervisorObservation = $taskRepeat
    ParsedNormalChildRecord = $taskChild
    PureTimeSampleQualification = 'ARTIFICIAL ELAPSED VALUES ONLY; NO REAL 120-SECOND TIMEOUT OR ADVERSARIAL TERMINATION TEST'
    InputAckQualification = 'FIXED ACK REPORT OBSERVATION ONLY; NOT TRUSTED ROOT, INDEPENDENT SOURCE VERIFICATION OR AUTHORITY'
    FailureRetentionQualification = 'ORIGINAL EXCEPTION RETAINED ONLY IN THIS PROCESS; TYPE METADATA ONLY; NO CROSS-PROCESS RETENTION CLAIM'
    Uncovered = [string[]]@('REAL_TIMEOUT_PATH','STOP_AND_DESCENDANT_SETTLEMENT','PROCESS_START_CLOSE_KILL_HARD_BOUNDS','OVERFLOW_AND_RESOURCE_EXHAUSTION','POSITIVE_DRIVER_SHA','CALLEE_REFERENCE_AND_FREEZE','TRUSTED_ROOT_AND_FULL_DEPENDENCIES','FULL_189_ITEM_PLAN')
    PreservedLimitations = 'ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN; NO SOURCE ADMISSION, ACTUAL CAPTURE OR INTEGRATION'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskRecord -Depth 14 -Compress
if($taskComplete){exit 0}else{exit 1}
