# Closed local synthetic private-stage transport checks for the accepted REV2.
# Not the public three-stage batch, source admission, business integration,
# formal WP008 validation, a cleanup-fault injection or an OS sandbox proof.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/'
$checks = [Collections.Generic.List[object]]::new()
$checkIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$cases = [Collections.Generic.List[object]]::new()
$heldErrors = [Collections.Generic.List[Exception]]::new()
$compiled = $false
$privateCalls = 0
$phase = 'FIXED_IDENTITIES'
$primaryFailureType = $null
$primaryFailurePhase = $null
$sourceSha = $null
$runnerSha = $null
$entrySha = $null

function Confirm-FaultCheck([string] $Id,[bool] $Condition) {
  if (-not $checkIds.Add($Id)) { throw [InvalidOperationException]::new('DUPLICATE_FAULT_CHECK_ID') }
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if (-not $Condition) { throw [InvalidOperationException]::new('FIXED_FAULT_CHECK_NOT_MET') }
}
function Copy-TransportMetadata([object] $Observation) {
  $metadata = [ordered]@{}
  foreach ($property in $Observation.GetType().GetProperties([Reflection.BindingFlags]'Public,Instance,DeclaredOnly')) {
    if ($property.Name -ceq 'ChildJsonBody') { continue }
    if ($null -ne $property.GetSetMethod($true) -or $property.GetIndexParameters().Length -ne 0) { throw [InvalidOperationException]::new('PUBLIC_MUTATION_OR_INDEXER') }
    $value = $property.GetValue($Observation)
    if ($null -ne $value -and $value.GetType() -notin @([string],[bool],[int],[long])) { throw [InvalidOperationException]::new('NONSCALAR_TRANSPORT_METADATA') }
    $metadata[$property.Name] = $value
  }
  return $metadata
}

try {
  $sourceBytes = [IO.File]::ReadAllBytes($root+'DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs')
  $sourceSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($sourceBytes))
  Confirm-FaultCheck 'PRE.ACCEPTED_REV2_SOURCE_IDENTITY' ($sourceBytes.Length -eq 24173 -and $sourceSha -ceq '9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E')
  $runnerBytes = [IO.File]::ReadAllBytes('C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe')
  $runnerSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($runnerBytes))
  Confirm-FaultCheck 'PRE.FIXED_RUNNER_FILE_IDENTITY' ($runnerSha -ceq '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139')
  $strictUtf8 = [Text.UTF8Encoding]::new($false,$true)
  Confirm-FaultCheck 'PRE.FRESH_SUPERVISOR_TYPE' ($null -eq ('Dsp004LocalCompositionSupervisorCandidateRev2' -as [type]))
  $newTypes = @(Add-Type -TypeDefinition $strictUtf8.GetString($sourceBytes) -Language CSharp -PassThru -WarningAction Stop -ErrorAction Stop)
  $compiled = $true
  $supervisorType = [Dsp004LocalCompositionSupervisorCandidateRev2]
  $publicMethods = @($supervisorType.GetMethods([Reflection.BindingFlags]'Public,Static,DeclaredOnly'))
  Confirm-FaultCheck 'API.PUBLIC_FIXED_NO_ARGUMENT_SHAPE' ($publicMethods.Count -eq 1 -and $publicMethods[0].Name -ceq 'RunFixedLocalCompositionBatch' -and $publicMethods[0].GetParameters().Length -eq 0 -and $supervisorType.GetConstructors().Length -eq 0)
  $sourceType = $supervisorType.GetNestedType('SourceSpec',[Reflection.BindingFlags]'NonPublic')
  $sourceConstructors = @($sourceType.GetConstructors([Reflection.BindingFlags]'NonPublic,Instance'))
  Confirm-FaultCheck 'API.PRIVATE_SOURCE_CONSTRUCTOR' ($sourceConstructors.Count -eq 1 -and $sourceConstructors[0].GetParameters().Length -eq 4 -and $sourceConstructors[0].GetParameters()[0].ParameterType -eq [string] -and $sourceConstructors[0].GetParameters()[1].ParameterType -eq [string] -and $sourceConstructors[0].GetParameters()[2].ParameterType -eq [string] -and $sourceConstructors[0].GetParameters()[3].ParameterType -eq [int])
  $stageMethod = $supervisorType.GetMethod('RunStage',[Reflection.BindingFlags]'NonPublic,Static,DeclaredOnly')
  Confirm-FaultCheck 'API.PRIVATE_STAGE_METHOD' ($null -ne $stageMethod -and $stageMethod.IsPrivate -and $stageMethod.GetParameters().Length -eq 3 -and $stageMethod.GetParameters()[0].ParameterType -eq $sourceType -and $stageMethod.GetParameters()[1].ParameterType -eq [byte[]] -and $stageMethod.GetParameters()[2].ParameterType -eq [Diagnostics.Stopwatch])
  $normalBody = '{"synthetic":true}'
  $normalPayload = "[Console]::Out.Write('{""synthetic"":true}')"
  $specs = @(
    @{Id='TF-001';Name='VALID_SMALL_JSON';Text=$normalPayload;WrongSha=$false;Allowed=$true;Failure=$null;FailurePhase=$null;Exit=[int]0;Evidence='NORMAL_JSON'},
    @{Id='TF-002';Name='MALFORMED_JSON_BODY';Text="[Console]::Out.Write('not-json')";WrongSha=$false;Allowed=$false;Failure='System.InvalidOperationException';FailurePhase='ACK_AND_BODY';Exit=[int]0;Evidence='BODY_SUPPRESSED'},
    @{Id='TF-003';Name='NONZERO_CHILD_EXIT';Text='exit 9';WrongSha=$false;Allowed=$false;Failure='System.InvalidOperationException';FailurePhase='OWNED_STREAM_TASKS';Exit=[int]9;Evidence='NONZERO_EXIT'},
    @{Id='TF-004';Name='STDERR_DETECTION';Text="[Console]::Error.Write('X'); [Threading.Thread]::Sleep(180000)";WrongSha=$false;Allowed=$false;Failure='System.InvalidOperationException';FailurePhase='OWNED_STREAM_TASKS';Exit=$null;Evidence='STDERR_ONE_DETECTION_BYTE'},
    @{Id='TF-005';Name='STDOUT_BUDGET_EXCEEDED';Text="[Console]::Out.Write(('X' * 262145)); [Threading.Thread]::Sleep(180000)";WrongSha=$false;Allowed=$false;Failure='System.InvalidOperationException';FailurePhase='OWNED_STREAM_TASKS';Exit=$null;Evidence='STDOUT_BUDGET_PLUS_ONE'},
    @{Id='TF-006';Name='INVALID_UTF8_BODY';Text='[Console]::OpenStandardOutput().WriteByte([byte]255)';WrongSha=$false;Allowed=$false;Failure='System.Text.DecoderFallbackException';FailurePhase='ACK_AND_BODY';Exit=[int]0;Evidence='BODY_SUPPRESSED'},
    @{Id='TF-007';Name='CHILD_SNAPSHOT_SHA_MISMATCH';Text=$normalPayload;WrongSha=$true;Allowed=$false;Failure='System.InvalidOperationException';FailurePhase='OWNED_STREAM_TASKS';Exit=$null;Evidence='PRE_ACK_DENIAL'},
    @{Id='TF-008';Name='REAL_MONOTONIC_DEADLINE';Text='[Threading.Thread]::Sleep(180000)';WrongSha=$false;Allowed=$false;Failure='System.TimeoutException';FailurePhase='OWNED_STREAM_TASKS';Exit=$null;Evidence='ACTUAL_120000MS_DEADLINE'}
  )
  foreach ($spec in $specs) {
    $phase = $spec.Id+'_'+$spec.Name
    $payload = $strictUtf8.GetBytes($spec.Text)
    $payloadSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($payload))
    $declaredSha = if ($spec.WrongSha) { '0' * 64 } else { $payloadSha }
    $privateSource = $sourceConstructors[0].Invoke([object[]]@($spec.Id,'CLOSED_SYNTHETIC_MEMORY_ONLY_NOT_A_FILE',$declaredSha,[int]$payload.Length))
    $clock = [Diagnostics.Stopwatch]::StartNew()
    $privateCalls++
    $actual = $stageMethod.Invoke($null,[object[]]@($privateSource,$payload,$clock))
    $outerElapsed = $clock.ElapsedMilliseconds
    $body = $actual.ChildJsonBody
    $transport = Copy-TransportMetadata $actual
    $cases.Add([pscustomobject][ordered]@{
      Id=$spec.Id
      Name=$spec.Name
      PayloadUTF8Bytes=$payload.Length
      ActualPayloadSHA256=$payloadSha
      DeclaredSnapshotSHA256=$declaredSha
      ExpectedTransportPass=$spec.Allowed
      ExpectedFailureType=$spec.Failure
      ExpectedFailurePhase=$spec.FailurePhase
      ExpectedExitCode=$spec.Exit
      ExpectedEvidenceClass=$spec.Evidence
      HarnessElapsedMilliseconds=$outerElapsed
      BodyWasPublished=($null -ne $body)
      Transport=$transport
      Qualification='DIRECT PRIVATE RUNSTAGE SYNTHETIC UNIT INVOCATION; NOT PUBLIC BATCH, FIXED VALIDATOR OR FORMAL WP008 SCENARIO'
    })
    Confirm-FaultCheck ($spec.Id+'.NATIVE_TRANSPORT_GATE') ($actual.TransportOnlyPass.GetType() -eq [bool] -and $actual.TransportOnlyPass -eq $spec.Allowed)
    Confirm-FaultCheck ($spec.Id+'.EXPECTED_FAILURE_TYPE') ($actual.FailureType -ceq $spec.Failure)
    Confirm-FaultCheck ($spec.Id+'.EXPECTED_FAILURE_PHASE') ($actual.FailurePhase -ceq $spec.FailurePhase)
    Confirm-FaultCheck ($spec.Id+'.OWNED_CHILD_START_AND_EXIT') ($actual.StartAttempted -and $actual.ChildStarted -and $actual.ChildExitObserved)
    Confirm-FaultCheck ($spec.Id+'.LOCAL_CLOSE_DISPOSE_RETURNS') ($actual.InputCloseReturned -and $actual.OutputCloseReturned -and $actual.ErrorCloseReturned -and $actual.ProcessDisposeReturned)
    Confirm-FaultCheck ($spec.Id+'.READ_TASKS_ENDED') ($actual.StdoutTaskEnded -and $actual.StderrTaskEnded)
    Confirm-FaultCheck ($spec.Id+'.NO_SECONDARY_CLEANUP_ERRORS') ($actual.SecondaryFailureCount -eq 0 -and $actual.SecondaryFailureStagesAndTypes -ceq '')
    Confirm-FaultCheck ($spec.Id+'.STOP_PATH_SEPARATION') ($actual.StopRequested -eq (-not $spec.Allowed))
    if ($null -ne $spec.Exit) { Confirm-FaultCheck ($spec.Id+'.DECLARED_EXIT_CODE') ($actual.ExitCode -eq $spec.Exit) }
    if ($spec.Allowed) {
      Confirm-FaultCheck ($spec.Id+'.EXACT_NORMAL_BODY_AND_HASH') ($body -ceq $normalBody -and $actual.ChildJsonBodySHA256 -ceq [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($strictUtf8.GetBytes($normalBody))))
      Confirm-FaultCheck ($spec.Id+'.NORMAL_ACK_EOF_BUDGET') ($actual.ChildSnapshotAckQualified -and $actual.StdoutEofObserved -and $actual.StderrEofObserved -and $actual.StderrBytes -eq 0 -and $actual.StdoutBytes -le 262144 -and $actual.CompletionBatchElapsedMilliseconds -ge 0 -and $actual.CompletionBatchElapsedMilliseconds -lt 120000)
    } else {
      Confirm-FaultCheck ($spec.Id+'.DENIAL_SUPPRESSES_BODY_HASH_ACK') ($null -eq $body -and $null -eq $actual.ChildJsonBodySHA256 -and -not $actual.ChildSnapshotAckQualified -and $actual.CompletionBatchElapsedMilliseconds -eq -1)
    }
    switch -CaseSensitive ($spec.Evidence) {
      'STDERR_ONE_DETECTION_BYTE' { Confirm-FaultCheck ($spec.Id+'.ERROR_DETECTION_NO_DRAIN') ($actual.StderrBytes -eq 1 -and -not $actual.StderrEofObserved) }
      'STDOUT_BUDGET_PLUS_ONE' { Confirm-FaultCheck ($spec.Id+'.OUTPUT_DETECTION_NO_DRAIN') ($actual.StdoutBytes -eq 262145 -and -not $actual.StdoutEofObserved) }
      'PRE_ACK_DENIAL' { Confirm-FaultCheck ($spec.Id+'.BOOTSTRAP_SHA_DENIAL') ($declaredSha -cne $payloadSha -and -not $actual.ChildSnapshotAckQualified -and $actual.StderrBytes -eq 1) }
      'ACTUAL_120000MS_DEADLINE' { Confirm-FaultCheck ($spec.Id+'.REAL_CLOCK_DEADLINE_OBSERVED') ($outerElapsed -ge 120000 -and $actual.StopRequested -and $actual.ChildExitObserved -and $actual.ReadTasksSettledAfterStop) }
    }
  }
  Confirm-FaultCheck 'BATCH.EXACT_EIGHT_PRIVATE_STAGE_CALLS' ($cases.Count -eq 8 -and $privateCalls -eq 8)
  Confirm-FaultCheck 'POST.ACCEPTED_REV2_UNCHANGED' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([IO.File]::ReadAllBytes($root+'DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs'))) -ceq $sourceSha)
  $entrySha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([IO.File]::ReadAllBytes($PSCommandPath)))
}
catch {
  $heldErrors.Add($_.Exception)
  $primaryFailureType = $_.Exception.GetBaseException().GetType().FullName
  $primaryFailurePhase = $phase
}
$failedChecks = @($checks | Where-Object {-not $_.Passed}).Count
$passed = $null -eq $primaryFailureType -and $failedChecks -eq 0 -and $cases.Count -eq 8 -and $privateCalls -eq 8
[pscustomobject][ordered]@{
  RecordKind='NEW_CLOSED_PRIVATE_STAGE_TRANSPORT_FAULT_BATCH_NOT_PUBLIC_COMPOSITION_OR_FORMAL_WP008'
  Outcome=$(if($passed){'LOCAL_PRIVATE_STAGE_TRANSPORT_FAULT_CHECKS_PASS'}else{'LOCAL_PRIVATE_STAGE_TRANSPORT_FAULT_CHECKS_INCOMPLETE'})
  CandidateSHA256=$sourceSha
  ValidationEntrySHA256=$entrySha
  RunnerFileSHA256=$runnerSha
  CandidateCompiled=$compiled
  PublicBatchCalls=0
  PrivateStageCalls=$privateCalls
  SyntheticCaseCount=$cases.Count
  CheckCount=$checks.Count
  UniqueCheckIds=$checkIds.Count
  FailedChecks=$failedChecks
  PrimaryValidationFailureType=$primaryFailureType
  PrimaryValidationFailurePhase=$primaryFailurePhase
  Cases=$cases.ToArray()
  Checks=$checks.ToArray()
  ScopeQualification='CLOSED IN-MEMORY SYNTHETIC SCRIPTS AND OWNED LOCAL CHILDREN ONLY; NOT REAL DRIVER, CASE MATERIAL, SOURCE ADMISSION OR BUSINESS CAPTURE'
  InvocationQualification='PRIVATE METHOD UNIT COVERAGE ONLY; PUBLIC PREFLIGHT AND ONE-BATCH GATE NOT EXERCISED; HARNESS BINDS SOURCE/RUNNER FILE IDENTITIES'
  TimingQualification='TF008 USES REAL STOPWATCH AND FIXED 120000MS CANDIDATE DEADLINE; NOT FINAL POST-READ STALL, HARD SYNCHRONOUS BOUND OR EXTERNAL WATCHDOG PROOF'
  ResourceQualification='OWNED CHILD EXIT, TASK END AND LOCAL CLOSE/DISPOSE OBSERVATIONS ONLY; NO CLEANUP-FAILURE INJECTION, MALICIOUS DESCENDANT OR COMPLETE RESOURCE SETTLEMENT PROOF'
  RecordQualification='RAW NEGATIVE STDOUT/STDERR, BODY, ORIGINAL EXCEPTION MESSAGE/STACK AND HANDLES NOT EXPORTED; TYPE AND SCALAR METADATA ONLY'
  AcceptanceQualification='REV2 SOURCE LIMITED ACCEPTANCE IS CONVERSATION-LEVEL; THIS TEST ENTRY AND RESULT NOT ACCEPTED BY TEST SUCCESS'
  Preserved='ALL LIMITED; POSITIVE REAL DRIVER SHA NOT COVERED; DSP004 OPEN/HOLD; B01/B02 OPEN; NO SOURCE ADMISSION, BUSINESS INTEGRATION, DEPLOYMENT OR GAP CLOSURE'
} | Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 20 -Compress
if (-not $passed) { exit 1 }
