# Closed synthetic JSON gate/conversion boundary checks. Original top-level entry is NOT run.
# No accepted-file change, C# compilation, child stage, real Driver or source admission.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME,'Modules','Microsoft.PowerShell.Utility','Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop
$root = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/'
$sourcePath = $root+'validation/route_b_c03/wp_008/DSP_004_LOCAL_COMPOSITION_VALIDATION_REV2.ps1'
$sourceSHA = 'ADAB2850039C9A15C0A175F0028B751F983FC21EB218835102247F9CD50D5262'
$runnerPath = 'C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/powershell/pwsh.exe'
$runnerSHA = '362A356CE7F0940EC74F73A8FC2C990A2CC24A38A11C90BBD8ECA947110AD139'
$utf8 = [Text.UTF8Encoding]::new($false,$true)
[Console]::OutputEncoding = $utf8
$OutputEncoding = $utf8
$checks = [Collections.Generic.List[object]]::new()
$checkIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$caseRecords = [Collections.Generic.List[object]]::new()
$extractedRecords = [Collections.Generic.List[object]]::new()
$primaryType = $null
$failurePhase = $null
$phase = 'READ_FIXED_SOURCE'
$sourceBefore = $null
$sourceAfter = $null

function Get-LocalDigest([byte[]] $Data) {
  return [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($Data))
}
function Confirm-Check([string] $Id, [bool] $Condition) {
  if (-not $checkIds.Add($Id)) { throw [InvalidOperationException]::new('DUPLICATE_CHECK_ID') }
  $checks.Add([pscustomobject]@{Id=$Id;Passed=$Condition})
  if (-not $Condition) { throw [InvalidOperationException]::new('SYNTHETIC_CHECK_NOT_MET') }
}

# Test-only observation adapter: System.Text.Json parse, object-root guard, exact
# ordinal uniqueness function. It is NOT a new production decoder.
function Observe-OrdinalGate([string] $Text) {
  $document = $null
  try {
    $document = [System.Text.Json.JsonDocument]::Parse($Text)
    if ($document.RootElement.ValueKind -ne [System.Text.Json.JsonValueKind]::Object) { throw [InvalidOperationException]::new('JSON_OBJECT_REQUIRED') }
    Check-JsonKeyUniqueness $document.RootElement
    return [pscustomobject]@{Outcome='ACCEPT';ExceptionType=$null}
  } catch {
    return [pscustomobject]@{Outcome='REJECT';ExceptionType=$_.Exception.GetBaseException().GetType().FullName}
  } finally {
    if ($null -ne $document) { $document.Dispose() }
  }
}
function New-ObjectFixture([int] $Depth) {
  $text = '"leaf"'
  for ($i=0; $i -lt $Depth; $i++) { $text = '{"n":'+$text+'}' }
  return $text
}
function New-ArrayFixture([int] $Depth) {
  $text = '"leaf"'
  for ($i=0; $i -lt $Depth; $i++) { $text = '['+$text+']' }
  return '{"n":'+$text+'}'
}
# Both expectations are literal and fixed before either subject is invoked.
$cases = @(
  [pscustomobject]@{Id='JG-001';Gate='ACCEPT';Decoder='REJECT';Text='{"A":1,"a":2}';Meaning='Root case collision'},
  [pscustomobject]@{Id='JG-002';Gate='ACCEPT';Decoder='REJECT';Text='{"obj":{"K":1,"k":2}}';Meaning='Nested case collision'},
  [pscustomobject]@{Id='JG-003';Gate='ACCEPT';Decoder='REJECT';Text='{"arr":[{"ID":1,"id":2}]}';Meaning='Array object case collision'},
  [pscustomobject]@{Id='JG-004';Gate='ACCEPT';Decoder='REJECT';Text='{"":"empty"}';Meaning='Root empty property name'},
  [pscustomobject]@{Id='JG-005';Gate='ACCEPT';Decoder='REJECT';Text='{"obj":{"":"empty"}}';Meaning='Nested empty property name'},
  [pscustomobject]@{Id='JG-006';Gate='ACCEPT';Decoder='REJECT';Text='{"arr":[{"":"empty"}]}';Meaning='Array object empty property name'},
  [pscustomobject]@{Id='JG-007';Gate='REJECT';Decoder='REJECT';Text='// synthetic comment'+[char]10+'{"a":1}';Meaning='Leading comment'},
  [pscustomobject]@{Id='JG-008';Gate='REJECT';Decoder='REJECT';Text='{/* synthetic */"a":1}';Meaning='Interior comment'},
  [pscustomobject]@{Id='JG-009';Gate='REJECT';Decoder='REJECT';Text='{"n":NaN}';Meaning='Unquoted NaN'},
  [pscustomobject]@{Id='JG-010';Gate='REJECT';Decoder='REJECT';Text='{"n":Infinity}';Meaning='Unquoted Infinity'},
  [pscustomobject]@{Id='JG-011';Gate='REJECT';Decoder='REJECT';Text='{"n":01}';Meaning='Leading zero'},
  [pscustomobject]@{Id='JG-012';Gate='REJECT';Decoder='REJECT';Text='{"n":1.}';Meaning='Incomplete fraction'},
  [pscustomobject]@{Id='JG-013';Gate='REJECT';Decoder='REJECT';Text='{"n":+1}';Meaning='Leading plus'},
  [pscustomobject]@{Id='JG-014';Gate='ACCEPT';Decoder='REJECT';Text=(New-ObjectFixture 50);Meaning='Object nesting 50'},
  [pscustomobject]@{Id='JG-015';Gate='ACCEPT';Decoder='REJECT';Text=(New-ArrayFixture 50);Meaning='Array nesting 50 within root object'},
  [pscustomobject]@{Id='JG-016';Gate='REJECT';Decoder='REJECT';Text=(New-ObjectFixture 65);Meaning='Object nesting 65'},
  [pscustomobject]@{Id='JG-017';Gate='REJECT';Decoder='REJECT';Text='{"a":"unterminated}';Meaning='Unterminated string'},
  [pscustomobject]@{Id='JG-018';Gate='REJECT';Decoder='REJECT';Text=('{"a":"x'+[char]9+'y"}');Meaning='Unescaped tab in string'},
  [pscustomobject]@{Id='JG-019';Gate='ACCEPT';Decoder='ACCEPT';Text=(New-ObjectFixture 10);Meaning='Object nesting 10'},
  [pscustomobject]@{Id='JG-020';Gate='ACCEPT';Decoder='ACCEPT';Text=(New-ArrayFixture 10);Meaning='Array nesting 10 within root object'},
  [pscustomobject]@{Id='JG-021';Gate='ACCEPT';Decoder='ACCEPT';Text='{"姓名":"合成","金额":3}';Meaning='Chinese property names'},
  [pscustomobject]@{Id='JG-022';Gate='ACCEPT';Decoder='ACCEPT';Text='{"a.b":"dot","x[y]":"bracket"}';Meaning='Punctuation property names'},
  [pscustomobject]@{Id='JG-023';Gate='ACCEPT';Decoder='ACCEPT';Text='{" ":"space"}';Meaning='Whitespace property name'},
  [pscustomobject]@{Id='JG-024';Gate='ACCEPT';Decoder='ACCEPT';Text='{"a\nb":"line"}';Meaning='Escaped newline property name'}
)

try {
  $sourceBytes = [IO.File]::ReadAllBytes($sourcePath)
  $sourceBefore = Get-LocalDigest $sourceBytes
  Confirm-Check 'PRE.SOURCE_BINDING' ($sourceBytes.Length -eq 19481 -and $sourceBefore -ceq $sourceSHA)
  Confirm-Check 'PRE.RUNNER_BINDING' ((Get-LocalDigest ([IO.File]::ReadAllBytes($runnerPath))) -ceq $runnerSHA)
  $sourceText = $utf8.GetString($sourceBytes)
  $tokens = $null; $errors = $null
  $sourceAst = [Management.Automation.Language.Parser]::ParseInput($sourceText,[ref]$tokens,[ref]$errors)
  if ($errors.Count -ne 0) { throw [InvalidOperationException]::new('SOURCE_AST_ERRORS') }
  $phase = 'EXTRACT_EXACT_FUNCTION_EXTENTS'
  $required = @(
    [pscustomobject]@{Name='Check-JsonKeyUniqueness';Bytes=619;SHA256='E573D366827177B9178C3F87C79E383AE8F9E973C473ED42852E1F2428E382CC'},
    [pscustomobject]@{Name='Decode-ClosedJson';Bytes=439;SHA256='458877E0C9AFD1E7E666A2CF23F8FF1722429C8CC3107F43A633EAE6ED2E8A59'}
  )
  $definitions = [Collections.Generic.List[string]]::new()
  foreach ($item in $required) {
    $nodes = @($sourceAst.FindAll({param($n) $n -is [Management.Automation.Language.FunctionDefinitionAst] -and $n.Name -ceq $item.Name},$true))
    Confirm-Check ('PRE.'+$item.Name+'.UNIQUE') ($nodes.Count -eq 1)
    $exactText = $nodes[0].Extent.Text
    $exactBytes = $utf8.GetBytes($exactText)
    $exactSHA = Get-LocalDigest $exactBytes
    Confirm-Check ('PRE.'+$item.Name+'.EXTENT_BINDING') ($exactBytes.Length -eq $item.Bytes -and $exactSHA -ceq $item.SHA256)
    $definitions.Add($exactText)
    $extractedRecords.Add([pscustomobject]@{
      Name=$item.Name
      StartLine=$nodes[0].Extent.StartLineNumber
      EndLine=$nodes[0].Extent.EndLineNumber
      ExtractedTextBytes=$exactBytes.Length
      ExtractedTextSHA256=$exactSHA
    })
  }
  $onlyText = [string]::Join([string][char]10,$definitions)
  $onlyTokens = $null; $onlyErrors = $null
  $onlyAst = [Management.Automation.Language.Parser]::ParseInput($onlyText,[ref]$onlyTokens,[ref]$onlyErrors)
  $statements = @($onlyAst.EndBlock.Statements)
  Confirm-Check 'PRE.FUNCTIONS_ONLY_PARSE' ($onlyErrors.Count -eq 0 -and $statements.Count -eq 2 -and @($statements | Where-Object {$_ -isnot [Management.Automation.Language.FunctionDefinitionAst]}).Count -eq 0)
  # Exact function definitions only; the source entry's top-level batch is never invoked.
  . ([ScriptBlock]::Create($onlyText))
  $phase = 'CLOSED_GATE_AND_CONVERSION_INPUTS'
  foreach ($case in $cases) {
    $gateObservation = Observe-OrdinalGate $case.Text
    $value = $null
    $exceptionType = $null
    $actual = 'ACCEPT'
    try { $value = Decode-ClosedJson $case.Text }
    catch {
      $actual = 'REJECT'
      $exceptionType = $_.Exception.GetBaseException().GetType().FullName
    }
    $valueOK = $null
    $nativeNote = $null
    if ($actual -ceq 'ACCEPT') {
      $valueOK = switch -Exact ($case.Id) {
        'JG-019' {
          $node = $value
          $valid = $true
          for ($i=0; $i -lt 10; $i++) {
            if ($node -isnot [pscustomobject] -or @($node.PSObject.Properties).Count -ne 1 -or $null -eq $node.PSObject.Properties['n']) { $valid=$false; break }
            $node = $node.n
          }
          $valid -and $node -is [string] -and $node -ceq 'leaf'
        }
        'JG-020' {
          $node = $value.n
          $valid = $true
          for ($i=0; $i -lt 10; $i++) {
            if ($node -isnot [object[]] -or $node.Count -ne 1) { $valid=$false; break }
            $node = $node[0]
          }
          $valid -and $node -is [string] -and $node -ceq 'leaf'
        }
        'JG-021' { @($value.PSObject.Properties).Count -eq 2 -and $value.PSObject.Properties['姓名'].Value -ceq '合成' -and $value.PSObject.Properties['金额'].Value -eq 3 }
        'JG-022' { @($value.PSObject.Properties).Count -eq 2 -and $value.PSObject.Properties['a.b'].Value -ceq 'dot' -and $value.PSObject.Properties['x[y]'].Value -ceq 'bracket' }
        'JG-023' { @($value.PSObject.Properties).Count -eq 1 -and $value.PSObject.Properties[' '].Value -ceq 'space' }
        'JG-024' { @($value.PSObject.Properties).Count -eq 1 -and $value.PSObject.Properties[('a'+[char]10+'b')].Value -ceq 'line' }
        default { $false }
      }
      $nativeNote = [pscustomobject]@{
        RootType=$value.GetType().FullName
        RootPropertyCount=@($value.PSObject.Properties).Count
        RootPropertyNames=@($value.PSObject.Properties | ForEach-Object {$_.Name})
      }
    }
    $hasResult = $null -ne $value
    $caseRecords.Add([pscustomobject]@{
      Id=$case.Id
      Meaning=$case.Meaning
      InputText=$case.Text
      InputUTF8Bytes=$utf8.GetByteCount($case.Text)
      InputSHA256=(Get-LocalDigest ($utf8.GetBytes($case.Text)))
      ExpectedGate=$case.Gate
      ActualGate=$gateObservation.Outcome
      GateExceptionType=$gateObservation.ExceptionType
      ExpectedDecoder=$case.Decoder
      ActualDecoder=$actual
      ResultReleased=$hasResult
      DecoderExceptionType=$exceptionType
      NativeValueCheck=$valueOK
      NativeObservation=$nativeNote
    })
    Confirm-Check ($case.Id+'.GATE_DISPOSITION') ($gateObservation.Outcome -ceq $case.Gate)
    Confirm-Check ($case.Id+'.DECODER_DISPOSITION') ($actual -ceq $case.Decoder)
    Confirm-Check ($case.Id+'.GATE_EXCEPTION') $(if ($case.Gate -ceq 'ACCEPT') {$null -eq $gateObservation.ExceptionType} else {-not [string]::IsNullOrEmpty($gateObservation.ExceptionType)})
    Confirm-Check ($case.Id+'.RESULT_RELEASE') $(if ($case.Decoder -ceq 'ACCEPT') {$hasResult -and $value -is [pscustomobject]} else {-not $hasResult})
    Confirm-Check ($case.Id+'.DECODER_EXCEPTION') $(if ($case.Decoder -ceq 'ACCEPT') {$null -eq $exceptionType} else {-not [string]::IsNullOrEmpty($exceptionType)})
    if ($case.Decoder -ceq 'ACCEPT') { Confirm-Check ($case.Id+'.NATIVE_VALUE') ($valueOK -eq $true) }
  }
  $phase = 'POST_READONLY_INTEGRITY'
  Confirm-Check 'POST.CASE_COUNT' ($caseRecords.Count -eq 24)
  Confirm-Check 'POST.LAYER_COUNTS' (@($caseRecords | Where-Object {$_.ActualGate -ceq 'ACCEPT'}).Count -eq 14 -and @($caseRecords | Where-Object {$_.ActualDecoder -ceq 'ACCEPT'}).Count -eq 6)
  $sourceAfter = Get-LocalDigest ([IO.File]::ReadAllBytes($sourcePath))
  Confirm-Check 'POST.SOURCE_UNCHANGED' ($sourceAfter -ceq $sourceBefore -and $sourceAfter -ceq $sourceSHA)
  Confirm-Check 'POST.CHECK_COUNT' ($checks.Count -eq 136)
  $phase = 'COMPLETE'
} catch {
  $primaryType = $_.Exception.GetBaseException().GetType().FullName
  $failurePhase = $phase
}

$failed = @($checks | Where-Object {-not $_.Passed})
$summary = [pscustomobject]@{
  Batch='DSP_004_JSON_GATE_CONVERSION_BOUNDARY_REV1'
  Outcome=$(if ($null -eq $primaryType) {'LOCAL_JSON_GATE_CONVERSION_BOUNDARY_CHECKS_PASS'} else {'LOCAL_JSON_GATE_CONVERSION_BOUNDARY_CHECKS_FAIL'})
  CaseCount=$caseRecords.Count
  GateAcceptedCount=@($caseRecords | Where-Object {$_.ActualGate -ceq 'ACCEPT'}).Count
  GateRejectedCount=@($caseRecords | Where-Object {$_.ActualGate -ceq 'REJECT'}).Count
  DecoderAcceptedCount=@($caseRecords | Where-Object {$_.ActualDecoder -ceq 'ACCEPT'}).Count
  DecoderRejectedCount=@($caseRecords | Where-Object {$_.ActualDecoder -ceq 'REJECT'}).Count
  GateAcceptedDecoderRejectedCount=@($caseRecords | Where-Object {$_.ActualGate -ceq 'ACCEPT' -and $_.ActualDecoder -ceq 'REJECT'}).Count
  CheckCount=$checks.Count
  FailedChecks=$failed.Count
  ExtractedFunctionCount=$extractedRecords.Count
  SourceSHA256Before=$sourceBefore
  SourceSHA256After=$sourceAfter
  FailurePhase=$failurePhase
  PrimaryExceptionType=$primaryType
}
[pscustomobject]@{
  RecordVersion='DSP004-JSON-GATE-CONVERSION-BOUNDARY-REV1'
  Scope='EXACT_FUNCTIONS_PLUS_TEST_ONLY_GATE_OBSERVER / LOCAL_SYNTHETIC / NOT_FORMAL_WP008'
  Summary=$summary
  ExtractedFunctions=$extractedRecords.ToArray()
  Cases=$caseRecords.ToArray()
  Checks=$checks.ToArray()
  Limits=@(
    'Gate observer is a test adapter, not a new production decoder',
    'No whole-entry execution or C# compilation',
    'No business schema, source admission or provenance acceptance',
    'No general JSON compatibility or universal depth-boundary claim',
    'No byte transport, child lifecycle or timing claim',
    'No coverage of the accepted 189-item list',
    'No business capture, integration or deployment',
    'DSP-004 OPEN / HOLD; B-01 OPEN; B-02 OPEN',
    'All upstream LIMITED and failure histories preserved'
  )
} | Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 15
if ($null -ne $primaryType) { exit 1 }
exit 0
