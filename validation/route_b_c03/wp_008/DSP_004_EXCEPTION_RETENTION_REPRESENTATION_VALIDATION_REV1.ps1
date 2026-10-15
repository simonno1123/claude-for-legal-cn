# Synthetic exception-state representation and private task-observer unit checks only.
Set-StrictMode -Version Latest
$ErrorActionPreference='Stop'
$WarningPreference='Stop'
$PSModuleAutoLoadingPreference='None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root='C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$sourcePath=$root+'validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs'
$sourceSHA='9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E'
$runner='C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe'
$runnerSHA='362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139'
$utf8=[Text.UTF8Encoding]::new($false,$true)
[Console]::OutputEncoding=$utf8
$OutputEncoding=$utf8
$checks=[Collections.Generic.List[object]]::new()
$checkIds=[Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$records=[Collections.Generic.List[object]]::new()
$heldNativeErrors=[Collections.Generic.List[Exception]]::new()
$primaryType=$null;$failurePhase=$null;$phase='FIXED_SOURCE_BINDING'
$sourceBefore=$null;$sourceAfter=$null
function Digest([byte[]]$Bytes){return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes))}
function Confirm-Check([string]$Id,[bool]$Condition){
  if(-not $checkIds.Add($Id)){throw [InvalidOperationException]::new('DUPLICATE_RETENTION_CHECK_ID')}
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if(-not $Condition){throw [InvalidOperationException]::new('RETENTION_UNIT_EXPECTATION_NOT_MET')}
}
function New-SyntheticError([string]$Kind){
  switch -Exact($Kind){
    'IO' {return [IO.IOException]::new('DSP004_PRIVATE_IO_MESSAGE')}
    'INVALID' {return [InvalidOperationException]::new('DSP004_PRIVATE_INVALID_MESSAGE')}
    'TIMEOUT' {return [TimeoutException]::new('DSP004_PRIVATE_TIMEOUT_MESSAGE')}
    'AGGREGATE' {return [AggregateException]::new('DSP004_PRIVATE_AGGREGATE_MESSAGE',[Exception[]]@([IO.IOException]::new('DSP004_PRIVATE_INNER_MESSAGE')))}
    default {throw [InvalidOperationException]::new('CLOSED_ERROR_KIND_REQUIRED')}
  }
}
function Capture-SelectedView([object]$View){
  return [pscustomobject]@{
    FailureType=$View.FailureType
    FailurePhase=$View.FailurePhase
    SecondaryFailureCount=$View.SecondaryFailureCount
    SecondaryFailureStagesAndTypes=$View.SecondaryFailureStagesAndTypes
    TransportOnlyPass=$View.TransportOnlyPass
    FailureRetentionQualification=$View.FailureRetentionQualification
  }
}
function Invoke-TaskObserver([Reflection.MethodInfo]$Method,[Threading.Tasks.Task]$Task){
  try{
    $value=$Method.Invoke($null,[object[]]@($Task))
    return [pscustomobject]@{Returned=$true;ValueIsNull=($null -eq $value);NativeError=$null;WrapperCount=0}
  }catch{
    $native=$_.Exception
    $wrappers=0
    while(($native -is [Management.Automation.RuntimeException] -or $native -is [Reflection.TargetInvocationException]) -and $null -ne $native.InnerException){
      $native=$native.InnerException
      $wrappers++
    }
    # Do not call GetBaseException or flatten an original AggregateException.
    return [pscustomobject]@{Returned=$false;ValueIsNull=$true;NativeError=$native;WrapperCount=$wrappers}
  }
}
# Literal model scenarios. They are NOT real cleanup-failure events.
$stateCases=@(
  [pscustomobject]@{Id='ER-001';Primary=$null;PrimaryPhase=$null;SecondaryKinds=@();SecondaryPhases=@();SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-002';Primary='IO';PrimaryPhase='PRIMARY_READ';SecondaryKinds=@();SecondaryPhases=@();SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-003';Primary=$null;PrimaryPhase=$null;SecondaryKinds=@('IO');SecondaryPhases=@('INPUT_CLOSE');SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-004';Primary='IO';PrimaryPhase='PRIMARY_READ';SecondaryKinds=@('INVALID');SecondaryPhases=@('INPUT_CLOSE');SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-005';Primary='IO';PrimaryPhase='PRIMARY_READ';SecondaryKinds=@('INVALID','TIMEOUT','IO');SecondaryPhases=@('KILL_REQUEST','EXIT_WAIT','OUTPUT_CLOSE');SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-006';Primary='IO';PrimaryPhase='PRIMARY_READ';SecondaryKinds=@('IO','IO');SecondaryPhases=@('INPUT_CLOSE','PROCESS_DISPOSE');SharedSecondary=$true;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-007';Primary='AGGREGATE';PrimaryPhase='PRIMARY_AGGREGATE';SecondaryKinds=@('AGGREGATE');SecondaryPhases=@('PROCESS_DISPOSE');SharedSecondary=$false;AppendAfterView=$false},
  [pscustomobject]@{Id='ER-008';Primary='IO';PrimaryPhase='PRIMARY_READ';SecondaryKinds=@('IO');SecondaryPhases=@('INPUT_CLOSE');SharedSecondary=$false;AppendAfterView=$true}
)
$taskCases=@(
  [pscustomobject]@{Id='ER-009';Kind='COMPLETE';State='RanToCompletion';Disposition='RETURN';ErrorType=$null},
  [pscustomobject]@{Id='ER-010';Kind='IO';State='Faulted';Disposition='THROW';ErrorType='System.IO.IOException'},
  [pscustomobject]@{Id='ER-011';Kind='CANCEL';State='Canceled';Disposition='THROW';ErrorType='System.Threading.Tasks.TaskCanceledException'},
  [pscustomobject]@{Id='ER-012';Kind='PENDING';State='WaitingForActivation';Disposition='RETURN';ErrorType=$null},
  [pscustomobject]@{Id='ER-013';Kind='AGGREGATE';State='Faulted';Disposition='THROW';ErrorType='System.AggregateException'}
)
try{
  $bytes=[IO.File]::ReadAllBytes($sourcePath)
  $sourceBefore=Digest $bytes
  Confirm-Check 'PRE.SOURCE_BINDING' ($bytes.Length -eq 24173 -and $sourceBefore -ceq $sourceSHA)
  Confirm-Check 'PRE.RUNNER_BINDING' ((Digest ([IO.File]::ReadAllBytes($runner))) -ceq $runnerSHA)
  $phase='MEMORY_COMPILATION_AND_SHAPE'
  $compiled=@(Add-Type -TypeDefinition ($utf8.GetString($bytes)) -PassThru)
  $top=@($compiled|Where-Object {$_.FullName -ceq 'Dsp004LocalCompositionSupervisorCandidateRev2'})
  if($top.Count -ne 1){throw [InvalidOperationException]::new('UNIQUE_SUBJECT_TYPE_REQUIRED')}
  $top=$top[0]
  $instanceFlags=[Reflection.BindingFlags]'NonPublic,Instance'
  $stateType=$top.GetNestedType('StageState',[Reflection.BindingFlags]'NonPublic')
  $viewType=$top.GetNestedType('StageObservation',[Reflection.BindingFlags]'Public')
  $stateCtor=$stateType.GetConstructor($instanceFlags,$null,[type[]]@([string],[string]),$null)
  $viewCtor=$viewType.GetConstructor($instanceFlags,$null,[type[]]@($stateType),$null)
  $keepPrimary=$stateType.GetMethod('KeepPrimary',$instanceFlags)
  $keepSecondary=$stateType.GetMethod('KeepSecondary',$instanceFlags)
  $primaryField=$stateType.GetField('Primary',$instanceFlags)
  $phaseField=$stateType.GetField('PrimaryPhase',$instanceFlags)
  $secondaryField=$stateType.GetField('Secondary',$instanceFlags)
  Confirm-Check 'PRE.KEEP_METHODS' ($null -ne $stateCtor -and $null -ne $viewCtor -and $keepPrimary.GetParameters().Count -eq 2 -and $keepSecondary.GetParameters().Count -eq 2 -and $null -ne $primaryField -and $null -ne $secondaryField)
  $properties=@($viewType.GetProperties([Reflection.BindingFlags]'Public,Instance,DeclaredOnly'))
  $noSetter=$properties.Count -gt 0
  foreach($p in $properties){if($null -ne $p.GetSetMethod($true) -or $p.PropertyType -notin @([string],[bool],[int],[long])){$noSetter=$false}}
  Confirm-Check 'PRE.VIEW_GET_ONLY_SCALARS' $noSetter
  $taskMethod=$top.GetMethod('ObserveTaskFailure',[Reflection.BindingFlags]'NonPublic,Static')
  Confirm-Check 'PRE.TASK_OBSERVER_SIGNATURE' ($null -ne $taskMethod -and $taskMethod.ReturnType -eq [void] -and $taskMethod.GetParameters().Count -eq 1 -and $taskMethod.GetParameters()[0].ParameterType -eq [Threading.Tasks.Task])
  $metadataDigest=Digest ($utf8.GetBytes('SYNTHETIC_EXCEPTION_STATE_NOT_A_REAL_ASSET'))
  $phase='STATE_REPRESENTATION_ONLY'
  foreach($case in $stateCases){
    $state=$stateCtor.Invoke([object[]]@($case.Id,$metadataDigest))
    $original=$null
    if($null -ne $case.Primary){
      $original=New-SyntheticError $case.Primary
      $heldNativeErrors.Add($original)
      $null=$keepPrimary.Invoke($state,[object[]]@($case.PrimaryPhase,$original))
    }
    $secondaries=[Collections.Generic.List[Exception]]::new()
    $shared=$null
    for($i=0;$i -lt $case.SecondaryKinds.Count;$i++){
      if($case.SharedSecondary -and $null -ne $shared){$errorObject=$shared}else{$errorObject=New-SyntheticError $case.SecondaryKinds[$i]}
      if($case.SharedSecondary){$shared=$errorObject}
      $heldNativeErrors.Add($errorObject)
      $secondaries.Add($errorObject)
    }
    $view=$null;$before=$null
    if($case.AppendAfterView){$view=$viewCtor.Invoke([object[]]@($state));$before=Capture-SelectedView $view}
    for($i=0;$i -lt $secondaries.Count;$i++){$null=$keepSecondary.Invoke($state,[object[]]@($case.SecondaryPhases[$i],$secondaries[$i]))}
    if($null -eq $view){$view=$viewCtor.Invoke([object[]]@($state))}
    $actualPrimary=$primaryField.GetValue($state)
    $actualPhase=$phaseField.GetValue($state)
    $actualSecondary=$secondaryField.GetValue($state)
    $primarySame=[object]::ReferenceEquals($actualPrimary,$original)
    $sequenceSame=$actualSecondary.Count -eq $secondaries.Count
    $expectedMetadata=[Collections.Generic.List[string]]::new()
    for($i=0;$i -lt $secondaries.Count;$i++){
      if($actualSecondary[$i].Key -cne $case.SecondaryPhases[$i] -or -not [object]::ReferenceEquals($actualSecondary[$i].Value,$secondaries[$i])){$sequenceSame=$false}
      $expectedMetadata.Add($case.SecondaryPhases[$i]+':'+$secondaries[$i].GetType().FullName)
    }
    $expectedType=if($null -ne $original){$original.GetType().FullName}else{$null}
    $selected=Capture-SelectedView $view
    $compact=$selected|Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 8 -Compress
    $privateMessagesAbsent=-not $compact.Contains('DSP004_PRIVATE_',[StringComparison]::Ordinal)
    $record=[pscustomobject]@{
      Id=$case.Id;Kind='SYNTHETIC_STATE_REPRESENTATION';ExpectedPrimaryType=$expectedType
      ExpectedPrimaryPhase=$case.PrimaryPhase;ExpectedSecondaryCount=$secondaries.Count
      ExpectedSecondaryMetadata=[string]::Join(';',$expectedMetadata)
      PrimaryNativeReferenceSame=$primarySame;SecondaryNativeReferencesAndOrderSame=$sequenceSame
      PrivateSentinelAbsentFromSelectedProjection=$privateMessagesAbsent
      BeforeAppendSelectedProjection=$before;SelectedProjection=$selected
      SharedSecondaryReferenceScenario=$case.SharedSecondary
    }
    $records.Add($record)
    Confirm-Check ($case.Id+'.PRIMARY_REFERENCE_PHASE') ($primarySame -and $actualPhase -ceq $case.PrimaryPhase)
    Confirm-Check ($case.Id+'.SECONDARY_REFERENCE_ORDER') $sequenceSame
    Confirm-Check ($case.Id+'.VIEW_PRIMARY') ($selected.FailureType -ceq $expectedType -and $selected.FailurePhase -ceq $case.PrimaryPhase)
    Confirm-Check ($case.Id+'.VIEW_SECONDARY') ($selected.SecondaryFailureCount -eq $secondaries.Count -and $selected.SecondaryFailureStagesAndTypes -ceq $record.ExpectedSecondaryMetadata)
    Confirm-Check ($case.Id+'.SELECTED_MESSAGE_BOUNDARY') $privateMessagesAbsent
    Confirm-Check ($case.Id+'.MODEL_NOT_TRANSPORT_PASS') (-not $selected.TransportOnlyPass)
    if($case.AppendAfterView){Confirm-Check ($case.Id+'.LIVE_VIEW_NOT_FROZEN') ($before.SecondaryFailureCount -eq 0 -and $selected.SecondaryFailureCount -eq 1)}
  }
  $phase='PRIVATE_TASK_OBSERVER_ONLY'
  foreach($case in $taskCases){
    $original=$null;$completion=$null;$token=[Threading.CancellationToken]::None
    switch -Exact($case.Kind){
      'COMPLETE' {$task=[Threading.Tasks.Task]::CompletedTask}
      'IO' {$original=New-SyntheticError 'IO';$heldNativeErrors.Add($original);$task=[Threading.Tasks.Task]::FromException($original)}
      'AGGREGATE' {$original=New-SyntheticError 'AGGREGATE';$heldNativeErrors.Add($original);$task=[Threading.Tasks.Task]::FromException($original)}
      'CANCEL' {$token=[Threading.CancellationToken]::new($true);$task=[Threading.Tasks.Task]::FromCanceled($token)}
      'PENDING' {$completion=[Threading.Tasks.TaskCompletionSource[bool]]::new();$task=$completion.Task}
    }
    $beforeState=$task.Status.ToString()
    $observation=Invoke-TaskObserver $taskMethod $task
    $afterState=$task.Status.ToString()
    $native=$observation.NativeError
    if($null -ne $native){$heldNativeErrors.Add($native)}
    $actualDisposition=if($observation.Returned){'RETURN'}else{'THROW'}
    $errorType=if($null -ne $native){$native.GetType().FullName}else{$null}
    $nativeSame=if($null -ne $original){[object]::ReferenceEquals($native,$original)}else{$null}
    $cancelBound=if($case.Kind -ceq 'CANCEL'){$native -is [OperationCanceledException] -and $native.CancellationToken.Equals($token)}else{$null}
    $aggregatePreserved=if($case.Kind -ceq 'AGGREGATE'){$native -is [AggregateException] -and $native.InnerExceptions.Count -eq 1 -and $native.InnerExceptions[0] -is [IO.IOException]}else{$null}
    $ownerRelease=$null
    if($case.Kind -ceq 'PENDING'){$ownerRelease=$completion.TrySetResult($true)}
    $records.Add([pscustomobject]@{
      Id=$case.Id;Kind='SYNTHETIC_TASK_OBSERVER';TaskFixture=$case.Kind
      ExpectedTaskState=$case.State;TaskStateBefore=$beforeState;TaskStateAfterMethod=$afterState
      ExpectedDisposition=$case.Disposition;ActualDisposition=$actualDisposition
      ExpectedErrorType=$case.ErrorType;ActualErrorType=$errorType
      MethodValueIsNull=$observation.ValueIsNull;ReflectionWrappersRemoved=$observation.WrapperCount
      OriginalNativeExceptionReferenceSame=$nativeSame
      OriginalCancellationTokenBound=$cancelBound;OriginalAggregateNotFlattened=$aggregatePreserved
      PendingFixtureCompletedByOwner=$ownerRelease;FinalTaskState=$task.Status.ToString()
    })
    Confirm-Check ($case.Id+'.METHOD_DISPOSITION') ($actualDisposition -ceq $case.Disposition -and $errorType -ceq $case.ErrorType)
    Confirm-Check ($case.Id+'.TASK_STATE_UNCHANGED') ($beforeState -ceq $case.State -and $afterState -ceq $case.State)
    Confirm-Check ($case.Id+'.VOID_RETURN_BOUNDARY') $observation.ValueIsNull
    if($null -ne $original){Confirm-Check ($case.Id+'.ORIGINAL_NATIVE_EXCEPTION') ($nativeSame -eq $true)}
    if($case.Kind -ceq 'CANCEL'){Confirm-Check ($case.Id+'.CANCEL_TOKEN') ($cancelBound -eq $true)}
    if($case.Kind -ceq 'PENDING'){Confirm-Check ($case.Id+'.OWNER_RELEASE_ONLY') ($ownerRelease -eq $true -and $task.IsCompletedSuccessfully)}
    if($case.Kind -ceq 'AGGREGATE'){Confirm-Check ($case.Id+'.AGGREGATE_NOT_FLATTENED') ($aggregatePreserved -eq $true)}
  }
  $phase='POST_READONLY_INTEGRITY'
  Confirm-Check 'POST.CASE_COUNT' ($records.Count -eq 13)
  $sourceAfter=Digest ([IO.File]::ReadAllBytes($sourcePath))
  Confirm-Check 'POST.SOURCE_UNCHANGED' ($sourceAfter -ceq $sourceSHA)
  Confirm-Check 'POST.CHECK_COUNT' ($checks.Count -eq 76)
  $phase='COMPLETE'
}catch{
  $primaryType=$_.Exception.GetType().FullName
  $failurePhase=$phase
}
$summary=[pscustomobject]@{
  Batch='DSP_004_EXCEPTION_RETENTION_REPRESENTATION_REV1'
  Outcome=$(if($null -eq $primaryType){'LOCAL_EXCEPTION_REPRESENTATION_AND_TASK_OBSERVER_CHECKS_PASS'}else{'LOCAL_EXCEPTION_REPRESENTATION_AND_TASK_OBSERVER_CHECKS_FAIL'})
  CaseCount=$records.Count;StateRepresentationCases=@($records|Where-Object {$_.Kind -ceq 'SYNTHETIC_STATE_REPRESENTATION'}).Count
  TaskObserverCases=@($records|Where-Object {$_.Kind -ceq 'SYNTHETIC_TASK_OBSERVER'}).Count
  CheckCount=$checks.Count;FailedChecks=@($checks|Where-Object {-not $_.Passed}).Count
  SourceSHA256Before=$sourceBefore;SourceSHA256After=$sourceAfter
  FailurePhase=$failurePhase;PrimaryExceptionType=$primaryType
}
[pscustomobject]@{
  RecordVersion='DSP004-EXCEPTION-RETENTION-REPRESENTATION-REV1'
  Scope='PRIVATE_STATE_AND_TASK_METHODS_ONLY / SYNTHETIC_MEMORY / NOT_ACTUAL_CLEANUP_FAILURE'
  Summary=$summary;Cases=$records.ToArray();Checks=$checks.ToArray()
  Limits=@(
    'State errors injected by direct private method calls, not failing cleanup operations',
    'Get-only view is live over held state, not an immutable frozen snapshot',
    'Selected metadata projection only; no general redaction or leakage proof',
    'Native exception references checked only in this test process',
    'Pending task observer return does not mean task settlement',
    'No RunStage, public batch, child stage, real sources, capture or integration',
    'All LIMITED retained; DSP-004 OPEN/HOLD; B-01 and B-02 OPEN'
  )
}|Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 18
if($null -ne $primaryType){exit 1}
exit 0
