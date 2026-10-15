# Local synthetic byte-stream unit checks only. No public batch, child stage or business input.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$sourcePath = $root+'validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_SUPERVISOR_CANDIDATE_REV2.cs'
$sourceSHA = '9B165A04AFE786224965C5E33364140265FF3CB0B4B99A8E63A7AE7562C33E4E'
$fixturePath = $root+'validation/route_b_c03/wp_008/DSP_004_BOUNDED_READ_SYNTHETIC_FIXTURE_REV1.cs'
$fixtureSHA = '00EC5B2D1A6998E1E59319EBDD64C30481AF5B38A142155D9D407B19A55893B0'
$runnerPath = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe'
$runnerSHA = '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139'
$utf8 = [Text.UTF8Encoding]::new($false,$true)
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8
$checks = [Collections.Generic.List[object]]::new()
$checkIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$records = [Collections.Generic.List[object]]::new()
$heldReadExceptions = [Collections.Generic.List[Exception]]::new()
$primaryType = $null
$failurePhase = $null
$sourceBefore = $null
$sourceAfter = $null
$fixtureAfter = $null
$phase = 'FIXED_SOURCE_BINDING'
function Digest([byte[]] $Bytes) { return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Bytes)) }
function Confirm-Check([string] $Id,[bool] $Condition) {
  if (-not $checkIds.Add($Id)) { throw [InvalidOperationException]::new('DUPLICATE_BOUNDED_READ_CHECK_ID') }
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if (-not $Condition) { throw [InvalidOperationException]::new('BOUNDED_READ_EXPECTATION_NOT_MET') }
}
# Closed expectations are fixed before compilation and any private-method call.
$cases = @(
  [pscustomobject]@{Id='BR-001';Budget=0;Length=0;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=0;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=0;ExpectedReadCalls=1;Meaning='Zero budget empty'},
  [pscustomobject]@{Id='BR-002';Budget=0;Length=1;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=1;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=1;ExpectedReadCalls=1;Meaning='Zero budget detection byte'},
  [pscustomobject]@{Id='BR-003';Budget=1;Length=0;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=0;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=0;ExpectedReadCalls=1;Meaning='One-byte budget empty'},
  [pscustomobject]@{Id='BR-004';Budget=1;Length=1;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=1;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=1;ExpectedReadCalls=2;Meaning='One-byte budget exact'},
  [pscustomobject]@{Id='BR-005';Budget=1;Length=2;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=2;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=2;ExpectedReadCalls=1;Meaning='One-byte budget exceeded'},
  [pscustomobject]@{Id='BR-006';Budget=4;Length=3;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=3;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=3;ExpectedReadCalls=2;Meaning='Small budget below'},
  [pscustomobject]@{Id='BR-007';Budget=4;Length=4;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=4;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=4;ExpectedReadCalls=2;Meaning='Small budget exact'},
  [pscustomobject]@{Id='BR-008';Budget=4;Length=5;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=5;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=5;ExpectedReadCalls=1;Meaning='Small budget exceeded'},
  [pscustomobject]@{Id='BR-009';Budget=4096;Length=4095;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=4095;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=4095;ExpectedReadCalls=2;Meaning='Chunk boundary below'},
  [pscustomobject]@{Id='BR-010';Budget=4096;Length=4096;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=4096;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=4096;ExpectedReadCalls=2;Meaning='Chunk boundary exact'},
  [pscustomobject]@{Id='BR-011';Budget=4096;Length=4097;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=4097;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=4097;ExpectedReadCalls=2;Meaning='Chunk boundary exceeded'},
  [pscustomobject]@{Id='BR-012';Budget=262144;Length=262143;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=262143;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=262143;ExpectedReadCalls=65;Meaning='Fixed stdout budget below'},
  [pscustomobject]@{Id='BR-013';Budget=262144;Length=262144;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=262144;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=262144;ExpectedReadCalls=65;Meaning='Fixed stdout budget exact'},
  [pscustomobject]@{Id='BR-014';Budget=262144;Length=262145;Chunk=4096;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=262145;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=262145;ExpectedReadCalls=65;Meaning='Fixed stdout detection byte'},
  [pscustomobject]@{Id='BR-015';Budget=4;Length=9;Chunk=1;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=5;ExpectedOverflow=$true;ExpectedEof=$false;ExpectedBytesReturned=5;ExpectedReadCalls=5;Meaning='One-byte fragmented overflow'},
  [pscustomobject]@{Id='BR-016';Budget=8;Length=8;Chunk=3;FailCall=0;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='RanToCompletion';ExpectedCount=8;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=8;ExpectedReadCalls=4;Meaning='Three-byte fragmented exact'},
  [pscustomobject]@{Id='BR-017';Budget=8;Length=8;Chunk=3;FailCall=1;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='Faulted';ExpectedCount=$null;ExpectedOverflow=$null;ExpectedEof=$null;ExpectedBytesReturned=0;ExpectedReadCalls=1;Meaning='I/O fault before any bytes'},
  [pscustomobject]@{Id='BR-018';Budget=8;Length=8;Chunk=3;FailCall=2;CancelCall=0;EarlyEofCall=0;ExpectedTaskState='Faulted';ExpectedCount=$null;ExpectedOverflow=$null;ExpectedEof=$null;ExpectedBytesReturned=3;ExpectedReadCalls=2;Meaning='I/O fault after prefix'},
  [pscustomobject]@{Id='BR-019';Budget=8;Length=8;Chunk=3;FailCall=0;CancelCall=1;EarlyEofCall=0;ExpectedTaskState='Canceled';ExpectedCount=$null;ExpectedOverflow=$null;ExpectedEof=$null;ExpectedBytesReturned=0;ExpectedReadCalls=1;Meaning='Canceled first read'},
  [pscustomobject]@{Id='BR-020';Budget=8;Length=8;Chunk=3;FailCall=0;CancelCall=0;EarlyEofCall=2;ExpectedTaskState='RanToCompletion';ExpectedCount=3;ExpectedOverflow=$false;ExpectedEof=$true;ExpectedBytesReturned=3;ExpectedReadCalls=2;Meaning='Early EOF after prefix'}
)
try {
  $sourceBytes = [IO.File]::ReadAllBytes($sourcePath)
  $sourceBefore = Digest $sourceBytes
  Confirm-Check 'PRE.SOURCE_BINDING' ($sourceBytes.Length -eq 24173 -and $sourceBefore -ceq $sourceSHA)
  $fixtureBytes = [IO.File]::ReadAllBytes($fixturePath)
  Confirm-Check 'PRE.FIXTURE_BINDING' ($fixtureBytes.Length -eq 3209 -and (Digest $fixtureBytes) -ceq $fixtureSHA)
  Confirm-Check 'PRE.RUNNER_BINDING' ((Digest ([IO.File]::ReadAllBytes($runnerPath))) -ceq $runnerSHA)
  $phase = 'MEMORY_COMPILATION_AND_PRIVATE_METHOD_BINDING'
  $sourceTypes = @(Add-Type -TypeDefinition ($utf8.GetString($sourceBytes)) -PassThru)
  $fixtureTypes = @(Add-Type -TypeDefinition ($utf8.GetString($fixtureBytes)) -PassThru)
  $subjectType = @($sourceTypes | Where-Object {$_.FullName -ceq 'Dsp004LocalCompositionSupervisorCandidateRev2'})
  $fixtureType = @($fixtureTypes | Where-Object {$_.FullName -ceq 'Dsp004BoundedReadSyntheticFixtureRev1'})
  if ($subjectType.Count -ne 1 -or $fixtureType.Count -ne 1) { throw [InvalidOperationException]::new('UNIQUE_COMPILED_TYPES_REQUIRED') }
  $subjectType = $subjectType[0]
  $fixtureType = $fixtureType[0]
  $method = $subjectType.GetMethod('ReadBounded',[Reflection.BindingFlags]'NonPublic,Static')
  $parameters = $method.GetParameters()
  Confirm-Check 'PRE.PRIVATE_METHOD_SHAPE' ($null -ne $method -and $parameters.Count -eq 2 -and $parameters[0].ParameterType -eq [IO.Stream] -and $parameters[1].ParameterType -eq [int] -and $method.ReturnType.BaseType -eq [Threading.Tasks.Task])
  Confirm-Check 'PRE.FIXTURE_SHAPE' ($fixtureType.BaseType -eq [IO.Stream] -and $fixtureType.IsSealed)
  $fields = [Reflection.BindingFlags]'NonPublic,Instance'
  $phase = 'SYNTHETIC_BOUNDED_READ_CASES'
  foreach ($case in $cases) {
    [byte[]]$data = [Dsp004BoundedReadSyntheticFixtureRev1]::CreateData($case.Length)
    $inputSHA = Digest $data
    $stream = [Dsp004BoundedReadSyntheticFixtureRev1]::new($data,$case.Chunk,$case.FailCall,$case.CancelCall,$case.EarlyEofCall)
    $task = $null
    $result = $null
    $original = $null
    $body = $null
    $count = $null
    $overflow = $null
    $eof = $null
    $bodySHA = $null
    $bodyMatches = $null
    $expectedBodySHA = $null
    $originalIdentity = $null
    $notDisposedBySubject = $false
    try {
      $task = $method.Invoke($null,[object[]]@($stream,[int]$case.Budget))
      if (-not $task.IsCompleted) { throw [InvalidOperationException]::new('FIXTURE_MUST_COMPLETE_SYNCHRONOUSLY') }
      try {
        $null = ([Threading.Tasks.Task]$task).GetAwaiter().GetResult()
        $result = $task.GetType().GetProperty('Result').GetValue($task)
      } catch {
        $original = $_.Exception.GetBaseException()
        $heldReadExceptions.Add($original)
      }
      if ($null -ne $result) {
        $type = $result.GetType()
        $body = $type.GetField('Body',$fields).GetValue($result)
        $count = $type.GetField('Count',$fields).GetValue($result)
        $overflow = $type.GetField('Overflow',$fields).GetValue($result)
        $eof = $type.GetField('Eof',$fields).GetValue($result)
        if ($null -ne $case.ExpectedCount) {
          $expectedLength = if ($case.ExpectedOverflow) {0} else {$case.ExpectedCount}
          $expectedBytes = [byte[]]::new($expectedLength)
          if ($expectedLength -gt 0) { [Array]::Copy($data,0,$expectedBytes,0,$expectedLength) }
          $expectedBodySHA = Digest $expectedBytes
          $bodySHA = Digest $body
          $bodyMatches = $body -is [byte[]] -and [Convert]::ToBase64String($body) -ceq [Convert]::ToBase64String($expectedBytes) -and $bodySHA -ceq $expectedBodySHA
        }
      }
      if ($case.FailCall -gt 0) { $originalIdentity = [object]::ReferenceEquals($original,$stream.HeldFailure) }
      $notDisposedBySubject = -not $stream.WasDisposed
    } finally {
      $stream.Dispose()
    }
    $errorType = if ($null -ne $original) {$original.GetType().FullName} else {$null}
    $record = [pscustomobject]@{
      Id=$case.Id
      Meaning=$case.Meaning
      Budget=$case.Budget
      InputLength=$data.Length
      InputSHA256=$inputSHA
      Chunk=$case.Chunk
      FailOnCall=$case.FailCall
      CancelOnCall=$case.CancelCall
      EarlyEofOnCall=$case.EarlyEofCall
      ExpectedTaskState=$case.ExpectedTaskState
      ActualTaskState=$task.Status.ToString()
      ExpectedCount=$case.ExpectedCount
      ActualCount=$count
      ExpectedOverflow=$case.ExpectedOverflow
      ActualOverflow=$overflow
      ExpectedEof=$case.ExpectedEof
      ActualEof=$eof
      ExpectedReadCalls=$case.ExpectedReadCalls
      ActualReadCalls=$stream.ReadCalls
      ExpectedBytesReturned=$case.ExpectedBytesReturned
      ActualBytesReturned=$stream.ReturnedBytes
      MaximumRequestedBytes=$stream.MaximumRequested
      StreamReturnedZero=$stream.ZeroReturned
      ResultReleased=($null -ne $result)
      BodyBytes=$(if ($null -ne $body) {$body.Length} else {$null})
      BodySHA256=$bodySHA
      ExpectedBodySHA256=$expectedBodySHA
      BodyByteComparison=$bodyMatches
      ErrorType=$errorType
      OriginalIOExceptionReferenceRetained=$originalIdentity
      InputNotDisposedBySubject=$notDisposedBySubject
      FixtureDisposeReturned=$stream.WasDisposed
      InputSHA256After=(Digest $data)
    }
    $records.Add($record)
    Confirm-Check ($case.Id+'.TASK_COMPLETED') $task.IsCompleted
    Confirm-Check ($case.Id+'.TASK_STATE') ($task.Status.ToString() -ceq $case.ExpectedTaskState)
    Confirm-Check ($case.Id+'.RESULT_DISPOSITION') $(if ($case.ExpectedTaskState -ceq 'RanToCompletion') {$null -ne $result -and $null -eq $original} else {$null -eq $result -and $null -ne $original})
    Confirm-Check ($case.Id+'.STREAM_COUNTS') ($stream.ReadCalls -eq $case.ExpectedReadCalls -and $stream.ReturnedBytes -eq $case.ExpectedBytesReturned)
    Confirm-Check ($case.Id+'.INPUT_OWNERSHIP') $notDisposedBySubject
    Confirm-Check ($case.Id+'.FIXTURE_CLEANUP') $stream.WasDisposed
    Confirm-Check ($case.Id+'.INPUT_UNCHANGED') ($record.InputSHA256After -ceq $inputSHA)
    if ($case.ExpectedTaskState -ceq 'RanToCompletion') {
      Confirm-Check ($case.Id+'.RESULT_FIELDS') ($count -eq $case.ExpectedCount -and $overflow -eq $case.ExpectedOverflow -and $eof -eq $case.ExpectedEof)
      Confirm-Check ($case.Id+'.BODY_BYTES') ($bodyMatches -eq $true)
    } elseif ($case.ExpectedTaskState -ceq 'Faulted') {
      Confirm-Check ($case.Id+'.ORIGINAL_EXCEPTION') ($originalIdentity -eq $true -and $original -is [IO.IOException])
    } else {
      Confirm-Check ($case.Id+'.CANCELLATION') ($task.IsCanceled -and $original -is [OperationCanceledException])
    }
  }
  $phase = 'POST_READONLY_INTEGRITY'
  Confirm-Check 'POST.CASE_COUNT' ($records.Count -eq 20)
  Confirm-Check 'POST.TERMINAL_COUNTS' (@($records|Where-Object {$_.ActualTaskState -ceq 'RanToCompletion'}).Count -eq 17 -and @($records|Where-Object {$_.ActualTaskState -ceq 'Faulted'}).Count -eq 2 -and @($records|Where-Object {$_.ActualTaskState -ceq 'Canceled'}).Count -eq 1)
  $sourceAfter = Digest ([IO.File]::ReadAllBytes($sourcePath))
  Confirm-Check 'POST.SOURCE_UNCHANGED' ($sourceAfter -ceq $sourceSHA)
  $fixtureAfter = Digest ([IO.File]::ReadAllBytes($fixturePath))
  Confirm-Check 'POST.FIXTURE_UNCHANGED' ($fixtureAfter -ceq $fixtureSHA)
  Confirm-Check 'POST.CHECK_COUNT' ($checks.Count -eq 186)
  $phase = 'COMPLETE'
} catch {
  $primaryType = $_.Exception.GetBaseException().GetType().FullName
  $failurePhase = $phase
}
$summary = [pscustomobject]@{
  Batch='DSP_004_BOUNDED_READ_BOUNDARY_REV1'
  Outcome=$(if ($null -eq $primaryType) {'LOCAL_SYNTHETIC_BOUNDED_READ_CHECKS_PASS'} else {'LOCAL_SYNTHETIC_BOUNDED_READ_CHECKS_FAIL'})
  CaseCount=$records.Count
  CompletedResultCount=@($records|Where-Object {$_.ActualTaskState -ceq 'RanToCompletion'}).Count
  OverflowCount=@($records|Where-Object {$_.ActualOverflow -eq $true}).Count
  EofCount=@($records|Where-Object {$_.ActualEof -eq $true}).Count
  FaultedCount=@($records|Where-Object {$_.ActualTaskState -ceq 'Faulted'}).Count
  CanceledCount=@($records|Where-Object {$_.ActualTaskState -ceq 'Canceled'}).Count
  CheckCount=$checks.Count
  FailedChecks=@($checks|Where-Object {-not $_.Passed}).Count
  HeldNativeReadExceptionCount=$heldReadExceptions.Count
  SourceSHA256Before=$sourceBefore
  SourceSHA256After=$sourceAfter
  FixtureSHA256After=$fixtureAfter
  FailurePhase=$failurePhase
  PrimaryExceptionType=$primaryType
}
[pscustomobject]@{
  RecordVersion='DSP004-BOUNDED-READ-BOUNDARY-REV1'
  Scope='PRIVATE_READ_METHOD_ONLY / MEMORY_SYNTHETIC / NOT_FORMAL_WP008'
  Summary=$summary
  Cases=$records.ToArray()
  Checks=$checks.ToArray()
  Limits=@(
    'No RunStage, public composition batch or child process stage',
    'No real pipe, socket, file stream, cancellation race or asynchronous delay',
    'Original I/O exceptions retained only inside this test process',
    'Early EOF is a stream observation, not complete-source proof',
    'Fixture disposal only; no injected cleanup failure or full resource settlement',
    'No trusted root, source admission, business capture, integration or deployment',
    'All upstream LIMITED and failure records preserved',
    'DSP-004 OPEN / HOLD; B-01 OPEN; B-02 OPEN'
  )
}|Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 15
if ($null -ne $primaryType) { exit 1 }
exit 0
