# Fixed local in-memory synthetic batch only. No child process or real cleanup.
# No accepted candidate is loaded or modified. No owner acceptance is issued.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME, 'Modules', 'Microsoft.PowerShell.Utility', 'Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskSourcePath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_SYNTHETIC_FAILURE_COEXISTENCE_CANDIDATE_REV1.cs'
$taskSourceSha = '06D2729B96BEBE2EB3A29CEF66B91982CD3ABE73B0491D6BEE37C903A4E830D9'
$taskChecks = [Collections.Generic.List[object]]::new()
$taskCases = @()
$taskRepeat = @()
$taskCompiled = $false
$taskPrimaryType = $null
$taskOriginalValidationException = $null
$taskBatchCalls = 0
$taskRepeatCalls = 0

function Add-ObservedCheck {
    param([string]$Id, [bool]$Condition, [string]$Scope)
    [void]$taskChecks.Add([pscustomobject][ordered]@{Id = $Id; Scope = $Scope; Passed = $Condition})
    if (-not $Condition) { throw [InvalidOperationException]::new('FIXED_SYNTHETIC_CHECK_FAILED') }
}

try {
    $taskBytes = [IO.File]::ReadAllBytes($taskSourcePath)
    if ($taskBytes.Length -ne 9039 -or [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskBytes)) -cne $taskSourceSha) {
        throw [InvalidOperationException]::new('FIXED_NEW_SOURCE_MISMATCH')
    }
    $taskTypeName = 'Dsp004SyntheticFailureCoexistence.Dsp004SyntheticFailureCoexistenceCandidateRev1'
    if ($null -ne [Management.Automation.PSTypeName]::new($taskTypeName).Type) { throw [InvalidOperationException]::new('PREEXISTING_CANDIDATE_TYPE') }
    $taskSource = [Text.UTF8Encoding]::new($false, $true).GetString($taskBytes)
    [void](Microsoft.PowerShell.Utility\Add-Type -TypeDefinition $taskSource -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
    $taskCompiled = $true
    $taskType = [Management.Automation.PSTypeName]::new($taskTypeName).Type
    $taskFlags = [Reflection.BindingFlags]::Public -bor [Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::Static -bor [Reflection.BindingFlags]::DeclaredOnly
    $taskMethods = @($taskType.GetMethods($taskFlags) | Where-Object {-not $_.IsSpecialName})
    Add-ObservedCheck 'API-01' ($taskType.IsSealed -and $taskType.GetConstructors().Count -eq 0 -and $taskType.GetFields($taskFlags).Count -eq 0 -and $taskMethods.Count -eq 1 -and $taskMethods[0].Name -ceq 'RunFixedSyntheticBatch' -and $taskMethods[0].GetParameters().Count -eq 0) 'Closed fixed zero-argument public entry; public metadata inspection only'

    # Independent fixed expectations from the plan; not inferred from outcomes.
    $taskExpected = [ordered]@{
        'F-01' = @('NO_SYNTHETIC_FAILURE', $false, 0, '', '', $false, $false, 1, 1, $true)
        'F-02' = @('PRIMARY_FAILURE', $true, 0, '', '', $false, $true, 1, 0, $false)
        'F-03' = @('CLEANUP_FAILURE_WITHOUT_PRIMARY', $false, 1, 'System.InvalidOperationException', 'SYNTHETIC_CLOSE', $false, $false, 1, 0, $false)
        'F-04' = @('PRIMARY_FAILURE', $true, 1, 'System.InvalidOperationException', 'SYNTHETIC_CLOSE', $false, $true, 1, 0, $false)
        'F-05' = @('PRIMARY_FAILURE', $true, 2, 'System.InvalidOperationException;System.ObjectDisposedException', 'SYNTHETIC_CLOSE;SYNTHETIC_DISPOSE', $false, $true, 1, 0, $false)
        'F-06' = @('PRIMARY_FAILURE', $true, 2, 'System.InvalidOperationException;System.InvalidOperationException', 'SYNTHETIC_CLOSE;SYNTHETIC_DISPOSE', $true, $true, 1, 0, $false)
        'F-07' = @('CLEANUP_FAILURE_WITHOUT_PRIMARY', $false, 2, 'System.InvalidOperationException;System.ObjectDisposedException', 'SYNTHETIC_CLOSE;SYNTHETIC_DISPOSE', $false, $false, 1, 0, $false)
        'F-08' = @('PRIMARY_FAILURE', $true, 1, 'System.InvalidOperationException', 'SYNTHETIC_CLOSE', $false, $true, 2, 0, $false)
        'F-09' = @('CLEANUP_FAILURE_WITHOUT_PRIMARY', $false, 1, 'System.InvalidOperationException', 'SYNTHETIC_CLOSE', $false, $false, 2, 1, $false)
    }
    $taskBatchCalls++
    $taskCases = @([Dsp004SyntheticFailureCoexistence.Dsp004SyntheticFailureCoexistenceCandidateRev1]::RunFixedSyntheticBatch())
    $taskById = [ordered]@{}
    foreach ($taskCase in $taskCases) {
        if ($taskById.Contains($taskCase.CaseId)) { throw [InvalidOperationException]::new('DUPLICATE_CASE_ID') }
        $taskById[$taskCase.CaseId] = $taskCase
    }
    Add-ObservedCheck 'SET-01' ($taskCases.Count -eq 9 -and $taskById.Count -eq 9) 'Nine fixed unique local synthetic records'

    foreach ($taskEntry in $taskExpected.GetEnumerator()) {
        $taskCase = $taskById[$taskEntry.Key]
        $taskE = $taskEntry.Value
        Add-ObservedCheck ($taskEntry.Key + '-CAUSE') ($taskCase.FirstReason -ceq $taskE[0]) 'First protective cause preserved; cleanup cannot overwrite a primary cause'
        $taskPrimary = $taskCase.PrimaryAttempted -and ($taskCase.PrimaryReturned -eq (-not $taskE[1])) -and ($taskCase.PrimaryFailurePresent -eq $taskE[1]) -and ($taskCase.PrimaryReferenceRetained -eq $taskE[1])
        if ($taskE[1]) { $taskPrimary = $taskPrimary -and $taskCase.PrimaryFailureType -ceq 'System.InvalidOperationException' }
        else { $taskPrimary = $taskPrimary -and $null -eq $taskCase.PrimaryFailureType }
        Add-ObservedCheck ($taskEntry.Key + '-PRIMARY') $taskPrimary 'Original primary exception reference or explicit absence; no cleanup-to-primary substitution'
        Add-ObservedCheck ($taskEntry.Key + '-SECONDARY') ($taskCase.CleanupFailureOccurrences -eq $taskE[2] -and $taskCase.CleanupFailureTypes -ceq $taskE[3] -and $taskCase.CleanupFailureStages -ceq $taskE[4] -and $taskCase.AllCleanupReferencesRetained -and ($taskCase.SameExceptionHasTwoCleanupOccurrences -eq $taskE[5])) 'Ordered actual synthetic exception occurrences; same-instance duplicates retain both events'
        Add-ObservedCheck ($taskEntry.Key + '-CLEANUP') ($taskCase.CleanupAttempts -eq 3 -and $taskCase.CleanupReturned -eq (3 - $taskE[2]) -and ($taskCase.StopLatchedBeforeCleanup -eq $taskE[6])) 'All three independent synthetic cleanup methods attempted; not OS cleanup proof'
        $taskStopped = $taskEntry.Key -cne 'F-01'
        Add-ObservedCheck ($taskEntry.Key + '-STOP') (($taskCase.StopLatched -eq $taskStopped) -and ($taskCase.StoppedResultNotRestored -eq $taskStopped) -and -not $taskCase.RepeatRefused) 'Stop latch and final result rejection retained without fabricating a repeat refusal'
        Add-ObservedCheck ($taskEntry.Key + '-COMPLETE') ($taskCase.CompletionAttempts -eq $taskE[7] -and $taskCase.HistoricalCompletionSuccesses -eq $taskE[8] -and ($taskCase.SyntheticBodyRecorded -eq $taskE[9])) 'Historical tentative completion distinct from final body; no late recovery after a stop'
        Add-ObservedCheck ($taskEntry.Key + '-SCOPE') ($taskCase.ObservationScope -ceq 'NEW FIXED IN-MEMORY SYNTHETIC OPERATIONS ONLY; NOT ACCEPTED SUPERVISOR OR PROCESS CLEANUP' -and $taskCase.IdentityQualification -ceq 'IN-PROCESS REFERENCE CHECK ONLY; NO CROSS-PROCESS RETENTION OR FREEZE PROOF' -and $taskCase.CleanupQualification -ceq 'SYNTHETIC DISPOSE METHODS ONLY; NO OS RESOURCE OR DESCENDANT SETTLEMENT CLAIM' -and $taskCase.Authority -ceq 'NOT ESTABLISHED' -and $taskCase.SourceAdmission -ceq 'NOT ESTABLISHED') 'Scope qualifications are recorded metadata, not external non-execution proof'
        $taskProperties = @($taskCase.GetType().GetProperties($taskFlags))
        $taskInvalidProperties = @($taskProperties | Where-Object {$_.CanWrite -or $_.PropertyType -notin @([string], [bool], [int])})
        $taskObservationMethods = @($taskCase.GetType().GetMethods($taskFlags) | Where-Object {-not $_.IsSpecialName})
        Add-ObservedCheck ($taskEntry.Key + '-OUTPUT') ($taskInvalidProperties.Count -eq 0 -and $taskObservationMethods.Count -eq 0 -and $taskCase.GetType().GetConstructors().Count -eq 0 -and $taskCase.GetType().GetFields($taskFlags).Count -eq 0) 'Public observation surface contains getter-only primitive metadata; no Exception/array export'
    }

    $taskRepeatCalls++
    $taskRepeat = @([Dsp004SyntheticFailureCoexistence.Dsp004SyntheticFailureCoexistenceCandidateRev1]::RunFixedSyntheticBatch())
    Add-ObservedCheck 'REPEAT-01' ($taskRepeat.Count -eq 1 -and $taskRepeat[0].CaseId -ceq 'F-REPEAT' -and $taskRepeat[0].FirstReason -ceq 'REPEATED_LOCAL_BATCH_REFUSED' -and $taskRepeat[0].RepeatRefused) 'Actual second request refused within the same compiled assembly'
    Add-ObservedCheck 'REPEAT-02' (-not $taskRepeat[0].PrimaryAttempted -and -not $taskRepeat[0].PrimaryFailurePresent -and $taskRepeat[0].CleanupAttempts -eq 0 -and $taskRepeat[0].CleanupFailureOccurrences -eq 0 -and $taskRepeat[0].CompletionAttempts -eq 0 -and -not $taskRepeat[0].SyntheticBodyRecorded -and $taskBatchCalls -eq 1 -and $taskRepeatCalls -eq 1) 'Refused request has no invented synthetic primary, cleanup or completion operation'
}
catch { $taskOriginalValidationException = $_.Exception; $taskPrimaryType = $_.Exception.GetType().FullName }

$taskFailed = @($taskChecks | Where-Object {-not $_.Passed}).Count
$taskIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($taskCheck in $taskChecks) { [void]$taskIds.Add($taskCheck.Id) }
$taskAll = $taskCompiled -and $null -eq $taskPrimaryType -and $taskChecks.Count -eq 76 -and $taskIds.Count -eq 76 -and $taskFailed -eq 0
$taskRecord = [pscustomobject][ordered]@{
    RecordKind = 'LOCAL_SYNTHETIC_FAILURE_COEXISTENCE_OBSERVATION_NOT_OWNER_ACCEPTANCE'
    Outcome = if ($taskAll) {'LOCAL_SYNTHETIC_FAILURE_COEXISTENCE_CHECKS_PASS'} else {'LOCAL_SYNTHETIC_FAILURE_COEXISTENCE_CHECKS_FAIL'}
    CandidateSHA256 = $taskSourceSha
    CompileCompleted = $taskCompiled
    BatchCalls = $taskBatchCalls
    RefusalCalls = $taskRepeatCalls
    CheckCount = $taskChecks.Count
    UniqueCheckIds = $taskIds.Count
    FailedChecks = $taskFailed
    PrimaryValidationFailureType = $taskPrimaryType
    Cases = $taskCases
    Repeat = $taskRepeat
    Checks = $taskChecks.ToArray()
    ProcessStart = 'NOT IMPLEMENTED OR CALLED IN THIS NEW BATCH'
    RealResourceCleanup = 'NOT IMPLEMENTED OR CALLED; DISPOSE METHODS ARE FIXED SYNTHETIC OPERATIONS'
    AcceptedCandidateInvocation = 'NONE IN THIS BATCH CODE PATH'
    CoverageQualification = 'NEW IN-MEMORY CANDIDATE ONLY; NOT ACTUAL PROCESS/STREAM CLEANUP FAILURE INJECTION'
    ReferenceQualification = 'ORIGINAL EXCEPTIONS RETAINED PRIVATELY IN THIS PROCESS; PUBLIC BOOLEANS ARE NOT CROSS-PROCESS OBJECT RETENTION'
    Uncovered = [string[]]@('ACCEPTED_SUPERVISOR_FAILURE_PATHS', 'REAL_PROCESS_STREAM_CLEANUP_FAILURE_INJECTION', 'ALL_DESCENDANT_AND_RESOURCE_SETTLEMENT', 'SYNCHRONOUS_CALL_HARD_BOUNDS', 'TRUSTED_ROOT_AND_TRANSITIVE_DEPENDENCIES', 'POSITIVE_DRIVER_SHA', 'CALLEE_REFERENCE_AND_FREEZE', 'FULL_189_ITEM_PLAN')
    Preserved = 'ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN; NO SOURCE ADMISSION, ACTUAL CAPTURE OR INTEGRATION'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskRecord -Depth 10 -Compress
if ($taskAll) {exit 0} else {exit 1}
