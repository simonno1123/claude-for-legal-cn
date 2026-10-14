# Closed new composition validation. No real Driver, business capture, source
# admission, external model, dependency installation or accepted-file change.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/'
$checks = [Collections.Generic.List[object]]::new()
$checkIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$stageRecords = [Collections.Generic.List[object]]::new()
$heldExceptions = [Collections.Generic.List[Exception]]::new()
$primaryType = $null
$phase = 'FIXED_SOURCE_PREPARATION'
$failurePhase = $null
$first = $null
$repeat = $null
$candidateSha = $null
$candidateCompiled = $false
$calls = 0
$newItemIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)

function Confirm-Check([string] $Id, [bool] $Condition) {
  if (-not $checkIds.Add($Id)) { throw [InvalidOperationException]::new('DUPLICATE_COMPOSITION_CHECK_ID') }
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if (-not $Condition) { throw [InvalidOperationException]::new('FIXED_COMPOSITION_CHECK_NOT_MET') }
}
function Check-JsonKeyUniqueness([System.Text.Json.JsonElement] $Element) {
  if ($Element.ValueKind -eq [System.Text.Json.JsonValueKind]::Object) {
    $names = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($property in $Element.EnumerateObject()) {
      if (-not $names.Add($property.Name)) { throw [InvalidOperationException]::new('DUPLICATE_JSON_PROPERTY') }
      Check-JsonKeyUniqueness $property.Value
    }
  } elseif ($Element.ValueKind -eq [System.Text.Json.JsonValueKind]::Array) {
    foreach ($item in $Element.EnumerateArray()) { Check-JsonKeyUniqueness $item }
  }
}
function Decode-ClosedJson([string] $Text) {
  $document = [System.Text.Json.JsonDocument]::Parse($Text)
  try {
    if ($document.RootElement.ValueKind -ne [System.Text.Json.JsonValueKind]::Object) { throw [InvalidOperationException]::new('JSON_OBJECT_REQUIRED') }
    Check-JsonKeyUniqueness $document.RootElement
  } finally { $document.Dispose() }
  return (Microsoft.PowerShell.Utility\ConvertFrom-Json -InputObject $Text -Depth 40)
}
function Capture-Transport([object] $Observation) {
  $output = [ordered]@{}
  foreach ($property in $Observation.GetType().GetProperties([Reflection.BindingFlags]'Public,Instance,DeclaredOnly')) {
    if ($property.Name -ceq 'ChildJsonBody') { continue }
    if ($null -ne $property.GetSetMethod($true) -or $property.GetIndexParameters().Length -ne 0) { throw [InvalidOperationException]::new('TRANSPORT_PUBLIC_MUTATION_SURFACE') }
    $value = $property.GetValue($Observation)
    if ($null -ne $value -and $value.GetType() -notin @([string],[bool],[int],[long])) { throw [InvalidOperationException]::new('TRANSPORT_NONSCALAR_FIELD') }
    $output[$property.Name] = $value
  }
  return $output
}

try {
  $candidateBytes = [IO.File]::ReadAllBytes($root+'DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV1.cs')
  $candidateSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($candidateBytes))
  Confirm-Check 'PRE.FIXED_NEW_CANDIDATE' ($candidateBytes.Length -eq 22783 -and $candidateSha -ceq '03D037FFAA2F87EA0AE8855A760CA422EF5FA6B827B5452070D52444387500FA')
  $listBytes = [IO.File]::ReadAllBytes($root+'DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1')
  Confirm-Check 'PRE.FIXED_LIST' ($listBytes.Length -eq 70284 -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($listBytes)) -ceq '46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C')
  $strictUtf8 = [Text.UTF8Encoding]::new($false,$true)
  $planIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  foreach ($line in ($strictUtf8.GetString($listBytes) -split "`n")) {
    $match = [regex]::Match($line,'^\| ((?:M|RQ|D|F|RD|WR)-[0-9]{3}) \|')
    if ($match.Success) { Confirm-Check ('PLAN.ID.'+$match.Groups[1].Value) ($planIds.Add($match.Groups[1].Value)) }
  }
  Confirm-Check 'PLAN.EXACT_189' ($planIds.Count -eq 189)
  Confirm-Check 'API.FRESH_TYPE' ($null -eq ('Dsp004LocalCompositionSupervisorCandidateRev1' -as [type]))
  $compiledTypes = @(Add-Type -TypeDefinition $strictUtf8.GetString($candidateBytes) -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
  $candidateCompiled = $true
  $publicMethods = @([Dsp004LocalCompositionSupervisorCandidateRev1].GetMethods([Reflection.BindingFlags]'Public,Static,DeclaredOnly'))
  Confirm-Check 'API.ONLY_NO_ARGUMENT_FIXED_BATCH' ($publicMethods.Count -eq 1 -and $publicMethods[0].Name -ceq 'RunFixedLocalCompositionBatch' -and $publicMethods[0].GetParameters().Length -eq 0)
  Confirm-Check 'API.NO_PUBLIC_CONSTRUCTOR' ([Dsp004LocalCompositionSupervisorCandidateRev1].GetConstructors().Length -eq 0)
  $phase = 'FIXED_THREE_CHILD_COMPOSITION'
  $calls++
  $first = [Dsp004LocalCompositionSupervisorCandidateRev1]::RunFixedLocalCompositionBatch()
  Confirm-Check 'BATCH.TRANSPORT_COMPLETED' ($first.Outcome -ceq 'LOCAL_COMPOSITION_TRANSPORT_OBSERVED_ONLY' -and $first.TransportBatchPass -and -not $first.RepeatRefused -and $first.Stages.Count -eq 3)
  Confirm-Check 'BATCH.PRE_POST_IDENTITIES' ($first.SourceSnapshotsVerified -eq 8 -and $first.PostSourceIdentitiesVerified -eq 8 -and $first.SourceReadAttempts -eq 16)
  Confirm-Check 'BATCH.EXECUTABLE_BOUND_ONCE' ($first.ExecutableReadAttempts -eq 1 -and $first.ExecutableVerified -and $first.ExecutableFileSHA256 -ceq '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139')
  Confirm-Check 'BATCH.NO_FAILURE' ($null -eq $first.FailureType -and $null -eq $first.FailurePhase)
  $specs = @(
    @{Id='RW';SHA='FBF43F9789E1034D91B944DBAAE76CF09BC46C659985874809803310B995F1E8';Checks=390;Items=96;Outcome='LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS'},
    @{Id='PURE';SHA='39614FA04D50971921117E46066F73E548925C817398CDD4560B9C50A0CD5869';Checks=373;Items=92;Outcome='LOCAL_REMAINING_PURE_CHECKS_PASS'},
    @{Id='D007';SHA='FA17F8C28D9982BC3467B2C4AB4FC8DA213E04E4EAC2BE7044E8FBD7E5C99BA4';Checks=815;Items=1;Outcome='LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_PASS'}
  )
  for ($index=0; $index -lt 3; $index++) {
    $spec = $specs[$index]
    $actual = $first.Stages[$index]
    $prefix = $spec.Id
    Confirm-Check "$prefix.STAGE_ORDER_SHA" ($actual.StageId -ceq $prefix -and $actual.EntrySHA256 -ceq $spec.SHA)
    Confirm-Check "$prefix.OWNED_NORMAL_TRANSPORT" ($actual.TransportOnlyPass -and $actual.StartAttempted -and $actual.ChildStarted -and $actual.WriteTaskReturned -and $actual.InputCloseReturned -and $actual.ChildExitObserved -and $actual.ExitCode -eq 0 -and $actual.ChildSnapshotAckQualified)
    Confirm-Check "$prefix.STREAMS_AND_TASKS" ($actual.StdoutBytes -gt 0 -and $actual.StdoutBytes -le 262144 -and $actual.StderrBytes -eq 0 -and $actual.StdoutEofObserved -and $actual.StderrEofObserved -and $actual.StdoutTaskEnded -and $actual.StderrTaskEnded)
    Confirm-Check "$prefix.LOCAL_CLEANUP_NO_STOP" ($actual.OutputCloseReturned -and $actual.ErrorCloseReturned -and $actual.ProcessDisposeReturned -and -not $actual.StopRequested -and -not $actual.KillCallReturned -and $null -eq $actual.FailureType -and $null -eq $actual.FailurePhase -and $actual.SecondaryFailureCount -eq 0 -and $actual.SecondaryFailureStagesAndTypes -ceq '')
    Confirm-Check "$prefix.COMPLETION_WITHIN_NEW_BUDGET" ($actual.CompletionBatchElapsedMilliseconds -ge 0 -and $actual.CompletionBatchElapsedMilliseconds -lt 120000 -and $actual.ElapsedMilliseconds -ge 0)
    $rawBody = $actual.ChildJsonBody
    Confirm-Check "$prefix.RECEIVED_BODY_HASH" ($null -ne $rawBody -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([Text.Encoding]::UTF8.GetBytes($rawBody))) -ceq $actual.ChildJsonBodySHA256)
    $phase = $prefix+'_STRICT_RECEIVED_RECORD'
    $record = Decode-ClosedJson $rawBody
    Confirm-Check "$prefix.RECORD_OUTCOME_AND_BINDINGS" ($record.Outcome -ceq $spec.Outcome -and $record.FixtureListSHA256 -ceq '46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C' -and $record.ControllerSHA256 -ceq '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB')
    Confirm-Check "$prefix.RECORDED_CHECK_COUNTS" ($record.CheckCount -eq $spec.Checks -and $record.UniqueCheckIds -eq $spec.Checks -and $record.Checks.Count -eq $spec.Checks -and $record.FailedChecks -eq 0 -and $null -eq $record.PrimaryValidationFailureType)
    $withinStageIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($row in $record.Checks) {
      $pass = if ($prefix -ceq 'D007') { $row.Pass } else { $row.Passed }
      Confirm-Check "$prefix.RECEIVED_CHECK.$($row.Id)" ($row.Id.GetType() -eq [string] -and $withinStageIds.Add($row.Id) -and $pass.GetType() -eq [bool] -and $pass)
    }
    if ($prefix -cne 'D007') {
      Confirm-Check "$prefix.FRESH_ITEM_COUNT_AND_CLEANUP" ($record.Cases.Count -eq $spec.Items -and $record.NativeComparisonPassCount -eq $spec.Items -and $record.CleanupFailures.Count -eq 0 -and $record.RunspaceCloseCallReturned -and $record.RunspaceDisposeCallReturned)
      foreach ($item in $record.Cases) { Confirm-Check "$prefix.FRESH_ITEM.$($item.Id)" ($item.Comparison -ceq 'LOCAL_NATIVE_COMPARISON_PASS' -and $newItemIds.Add($item.Id)) }
    } else {
      Confirm-Check 'D007.FIXED_ACCEPTED_SOURCE_NEW_RUN' ($record.CandidateSHA256 -ceq '666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3' -and $record.Compiled -and $record.PublicProbeCalls -eq 2 -and $record.NewPlanItemIds.Count -eq 1 -and $record.NewPlanItemIds[0] -ceq 'D-007')
      $probe = $record.FirstNativeObservation.Actual
      $denial = $record.SameAssemblyRepeatObservation.Actual
      Confirm-Check 'D007.PRIVATE_PREPARATION_AND_HELPER_NEW_OBSERVATION' ($probe.PrivatePayloadCreated -and $probe.PrivatePayloadLength -eq 20177 -and $probe.PreparationHashCalls -eq 1 -and $probe.HelperInvokeAttempts -eq 1 -and $probe.HelperInvokeReturned -and $probe.NativeComparisonCompleted -and $probe.LocalComparisonPass -and $probe.TargetTextCheck -ceq 'FIXED_DRIVER_SHA_MISMATCH')
      Confirm-Check 'D007.CALLER_REFERENCE_ONLY' ($probe.CallerParameterSamePreparedReferenceBefore -and $probe.CallerParameterSamePreparedReferenceAfter -and $probe.ReferenceQualification -ceq 'CALLER COMMAND PARAMETER REFERENCE OBSERVATION ONLY; CALLEE REFERENCE AND FREEZE NOT ESTABLISHED')
      Confirm-Check 'D007.REPEAT_WITHOUT_HELPER' ($denial.RepeatRefused -and $denial.ControllerReadAttempts -eq 0 -and $denial.PreparationHashCalls -eq 0 -and $denial.HelperInvokeAttempts -eq 0 -and -not $denial.PrivatePayloadCreated)
      Confirm-Check 'D007.FRESH_ID_NOT_HISTORICAL_COVERAGE_FIELD' ($newItemIds.Add('D-007'))
    }
    $stageRecords.Add([pscustomobject]@{StageId=$prefix;Transport=(Capture-Transport $actual);ReceivedParsedRecord=$record;RecordQualification='ACTUAL NEW CHILD RECORD; PARENT JSON CHECK DOES NOT RECREATE CHILD NATIVE TYPES OR CROSS-CHILD REFERENCES'})
  }
  Confirm-Check 'COMPOSITION.NEW_189_EXACT_ID_SET' ($newItemIds.Count -eq 189 -and $newItemIds.SetEquals($planIds))
  $phase = 'SAME_ASSEMBLY_COMPOSITION_REPEAT'
  $calls++
  $repeat = [Dsp004LocalCompositionSupervisorCandidateRev1]::RunFixedLocalCompositionBatch()
  Confirm-Check 'REPEAT.NO_ACTIVITY' ($repeat.Outcome -ceq 'REPEATED_COMPOSITION_BATCH_REFUSED' -and $repeat.RepeatRefused -and -not $repeat.TransportBatchPass -and $repeat.Stages.Count -eq 0 -and $repeat.SourceReadAttempts -eq 0 -and $repeat.SourceSnapshotsVerified -eq 0 -and $repeat.PostSourceIdentitiesVerified -eq 0 -and $repeat.ExecutableReadAttempts -eq 0 -and -not $repeat.ExecutableVerified -and $null -eq $repeat.ExecutableFileSHA256 -and $repeat.ElapsedMilliseconds -eq -1 -and $null -eq $repeat.FailureType)
  Confirm-Check 'POST.NEW_SUPERVISOR_UNCHANGED' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([IO.File]::ReadAllBytes($root+'DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV1.cs'))) -ceq $candidateSha)
}
catch {
  $heldExceptions.Add($_.Exception)
  $primaryType = $_.Exception.GetType().FullName
  $failurePhase = $phase
}

$failures = @($checks | Where-Object { -not $_.Passed }).Count
$passed = $null -eq $primaryType -and $failures -eq 0 -and $calls -eq 2 -and $stageRecords.Count -eq 3 -and $newItemIds.Count -eq 189
$batchMetadata = if ($null -ne $first) {
  [ordered]@{Outcome=$first.Outcome;TransportBatchPass=$first.TransportBatchPass;SourceReadAttempts=$first.SourceReadAttempts;SourceSnapshotsVerified=$first.SourceSnapshotsVerified;PostSourceIdentitiesVerified=$first.PostSourceIdentitiesVerified;ExecutableFileSHA256=$first.ExecutableFileSHA256;ElapsedMilliseconds=$first.ElapsedMilliseconds;FailureType=$first.FailureType;FailurePhase=$first.FailurePhase;Scope=$first.Scope;InputQualification=$first.InputQualification;DependencyQualification=$first.DependencyQualification;ResourceQualification=$first.ResourceQualification;Preserved=$first.Preserved}
} else { $null }
$partialTransports = if ($null -ne $first -and -not $passed) { @($first.Stages | ForEach-Object { Capture-Transport $_ }) } else { @() }
[pscustomobject][ordered]@{
  RecordKind='NEW_CLOSED_LOCAL_SYNTHETIC_THREE_STAGE_COMPOSITION_NOT_FORMAL_WP008_OR_ACCEPTANCE'
  Outcome=$(if($passed){'LOCAL_SYNTHETIC_COMPOSITION_CHECKS_PASS'}else{'LOCAL_SYNTHETIC_COMPOSITION_INCOMPLETE'})
  SupervisorCandidateSHA256=$candidateSha
  CandidateCompiled=$candidateCompiled
  PublicBatchCalls=$calls
  FirstBatch=$batchMetadata
  ActualStageRecords=$stageRecords.ToArray()
  PartialTransportRecords=$partialTransports
  NewUniquePlanItemCount=$newItemIds.Count
  NewUniquePlanItemIds=@($newItemIds | Sort-Object)
  ParentCheckCount=$checks.Count
  ParentUniqueCheckIds=$checkIds.Count
  ParentFailedChecks=$failures
  PrimaryValidationFailureType=$primaryType
  PrimaryValidationFailurePhase=$failurePhase
  ParentChecks=$checks.ToArray()
  SameAssemblyRepeatRefused=($null -ne $repeat -and $repeat.RepeatRefused)
  ChildOriginalCheckCountQualification='RW390/PURE373/D007815; D007 INCLUDES HISTORICAL ID AUDIT; NOT 1578 NEW CASES'
  CompositionQualification='THREE FRESH CLOSED CHILD EXECUTIONS; NOT ONE SHARED RUNSPACE, SHARED PAYLOAD, BUSINESS CAPTURE OR FORMAL SCENARIO VALIDATION'
  CleanupQualification='NORMAL LOCAL CLOSE/DISPOSE RETURN OBSERVATIONS; NO REAL CLEANUP FAILURE INJECTION, COMPLETE RESOURCES OR HARD STOP PROOF'
  CandidateAcceptance='NOT ESTABLISHED FOR NEW COMPOSITION SUPERVISOR'
  Preserved='ALL LIMITED; DSP004 OPEN/HOLD; B01/B02 OPEN; NO GAP CLOSURE OR DOWNSTREAM AUTHORITY'
} | Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 40 -Compress
if (-not $passed) { exit 1 }
