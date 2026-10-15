# Closed synthetic JSON decoder checks only. The original validation entry is NOT run.
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

# Independent, literal expectations are fixed before any decoder invocation.
$cases = @(
  [pscustomobject]@{Id='CJ-001';Expected='ACCEPT';Text='{}';Meaning='Empty object'},
  [pscustomobject]@{Id='CJ-002';Expected='ACCEPT';Text='{"synthetic":true,"kind":"local"}';Meaning='Boolean and string'},
  [pscustomobject]@{Id='CJ-003';Expected='ACCEPT';Text='{"node":{"value":"x"}}';Meaning='Nested object'},
  [pscustomobject]@{Id='CJ-004';Expected='ACCEPT';Text='{"items":[{"id":"A"},{"id":"B"}]}';Meaning='Object array'},
  [pscustomobject]@{Id='CJ-005';Expected='ACCEPT';Text='{"text":"\u4e2d\u6587"}';Meaning='Unicode escapes'},
  [pscustomobject]@{Id='CJ-006';Expected='ACCEPT';Text='{"text":"a\"b\\c"}';Meaning='Quote and slash escapes'},
  [pscustomobject]@{Id='CJ-007';Expected='ACCEPT';Text='{"small":7,"ratio":1.5}';Meaning='Integer and fraction'},
  [pscustomobject]@{Id='CJ-008';Expected='ACCEPT';Text='{"large":9223372036854775807}';Meaning='Int64 maximum'},
  [pscustomobject]@{Id='CJ-009';Expected='ACCEPT';Text='{"large":-9223372036854775808}';Meaning='Int64 minimum'},
  [pscustomobject]@{Id='CJ-010';Expected='ACCEPT';Text='{"value":null,"flag":false}';Meaning='Null and false'},
  [pscustomobject]@{Id='CJ-011';Expected='ACCEPT';Text=([string][char]13+[char]10+[char]9+'{"ok":true}'+[char]9+[char]13+[char]10);Meaning='JSON outer whitespace'},
  [pscustomobject]@{Id='CJ-012';Expected='ACCEPT';Text='{"text":"[IO.File]::ReadAllText(\"NOT_A_PATH\")"}';Meaning='Code-like string remains data'},
  [pscustomobject]@{Id='CJ-013';Expected='REJECT';Text='{"a":}';Meaning='Malformed value'},
  [pscustomobject]@{Id='CJ-014';Expected='REJECT';Text='{}{} ';Meaning='Multiple roots'},
  [pscustomobject]@{Id='CJ-015';Expected='REJECT';Text='[]';Meaning='Array root'},
  [pscustomobject]@{Id='CJ-016';Expected='REJECT';Text='"data"';Meaning='String root'},
  [pscustomobject]@{Id='CJ-017';Expected='REJECT';Text='123';Meaning='Numeric root'},
  [pscustomobject]@{Id='CJ-018';Expected='REJECT';Text='null';Meaning='Null root'},
  [pscustomobject]@{Id='CJ-019';Expected='REJECT';Text='{"a":1,"a":2}';Meaning='Root duplicate'},
  [pscustomobject]@{Id='CJ-020';Expected='REJECT';Text='{"obj":{"k":1,"k":2}}';Meaning='Nested duplicate'},
  [pscustomobject]@{Id='CJ-021';Expected='REJECT';Text='{"arr":[{"id":"A","id":"B"}]}';Meaning='Array object duplicate'},
  [pscustomobject]@{Id='CJ-022';Expected='REJECT';Text='{"a":1,"\u0061":2}';Meaning='Escaped equivalent duplicate'},
  [pscustomobject]@{Id='CJ-023';Expected='REJECT';Text='{"arr":[{"deep":[{"k":1,"k":1}]}]}';Meaning='Deep nested duplicate'},
  [pscustomobject]@{Id='CJ-024';Expected='REJECT';Text='{"a":1,}';Meaning='Trailing comma'}
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
  $phase = 'CLOSED_SYNTHETIC_INPUTS'
  foreach ($case in $cases) {
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
        'CJ-001' { @($value.PSObject.Properties).Count -eq 0 }
        'CJ-002' { @($value.PSObject.Properties).Count -eq 2 -and $value.synthetic -is [bool] -and $value.synthetic -eq $true -and $value.kind -ceq 'local' }
        'CJ-003' { @($value.PSObject.Properties).Count -eq 1 -and $value.node -is [pscustomobject] -and $value.node.value -ceq 'x' }
        'CJ-004' { $value.items -is [object[]] -and $value.items.Count -eq 2 -and $value.items[0].id -ceq 'A' -and $value.items[1].id -ceq 'B' }
        'CJ-005' { $value.text -is [string] -and $value.text -ceq '中文' }
        'CJ-006' { $value.text -is [string] -and $value.text -ceq 'a"b\c' }
        'CJ-007' { $value.small -eq 7 -and $value.ratio -eq 1.5 }
        'CJ-008' { $value.large -is [long] -and $value.large -eq [long]::MaxValue -and $value.large.ToString([Globalization.CultureInfo]::InvariantCulture) -ceq '9223372036854775807' }
        'CJ-009' { $value.large -is [long] -and $value.large -eq [long]::MinValue -and $value.large.ToString([Globalization.CultureInfo]::InvariantCulture) -ceq '-9223372036854775808' }
        'CJ-010' { @($value.PSObject.Properties).Count -eq 2 -and $null -eq $value.value -and $value.flag -is [bool] -and $value.flag -eq $false }
        'CJ-011' { $value.ok -is [bool] -and $value.ok -eq $true }
        'CJ-012' { $value.text -is [string] -and $value.text -ceq '[IO.File]::ReadAllText("NOT_A_PATH")' }
        default { $false }
      }
      if ($case.Id -cin @('CJ-008','CJ-009')) {
        # Retain Int64 diagnostics as strings; no JSON/JavaScript numeric rounding.
        $nativeNote = [pscustomobject]@{Property='large';NativeType=$value.large.GetType().FullName;InvariantValueText=$value.large.ToString([Globalization.CultureInfo]::InvariantCulture)}
      }
    }
    $hasResult = $null -ne $value
    $rootType = if ($hasResult) {$value.GetType().FullName} else {$null}
    $caseRecords.Add([pscustomobject]@{
      Id=$case.Id
      Meaning=$case.Meaning
      InputText=$case.Text
      InputUTF8Bytes=$utf8.GetByteCount($case.Text)
      InputSHA256=(Get-LocalDigest ($utf8.GetBytes($case.Text)))
      Expected=$case.Expected
      Actual=$actual
      ResultReleased=$hasResult
      RootType=$rootType
      ExceptionType=$exceptionType
      NativeValueCheck=$valueOK
      NativeIntegerObservation=$nativeNote
    })
    Confirm-Check ($case.Id+'.DISPOSITION') ($actual -ceq $case.Expected)
    Confirm-Check ($case.Id+'.RESULT_RELEASE') $(if ($case.Expected -ceq 'ACCEPT') {$hasResult -and $value -is [pscustomobject]} else {-not $hasResult})
    Confirm-Check ($case.Id+'.EXCEPTION_BOUNDARY') $(if ($case.Expected -ceq 'ACCEPT') {$null -eq $exceptionType} else {-not [string]::IsNullOrEmpty($exceptionType)})
    if ($case.Expected -ceq 'ACCEPT') { Confirm-Check ($case.Id+'.NATIVE_VALUE') ($valueOK -eq $true) }
  }
  $phase = 'POST_READONLY_INTEGRITY'
  Confirm-Check 'POST.CASE_COUNT' ($caseRecords.Count -eq 24)
  $sourceAfter = Get-LocalDigest ([IO.File]::ReadAllBytes($sourcePath))
  Confirm-Check 'POST.SOURCE_UNCHANGED' ($sourceAfter -ceq $sourceBefore -and $sourceAfter -ceq $sourceSHA)
  Confirm-Check 'POST.CHECK_COUNT' ($checks.Count -eq 93)
  $phase = 'COMPLETE'
} catch {
  $primaryType = $_.Exception.GetBaseException().GetType().FullName
  $failurePhase = $phase
}

$failed = @($checks | Where-Object {-not $_.Passed})
$summary = [pscustomobject]@{
  Batch='DSP_004_CLOSED_RECORD_JSON_REV1'
  Outcome=$(if ($null -eq $primaryType) {'LOCAL_CLOSED_JSON_DECODER_CHECKS_PASS'} else {'LOCAL_CLOSED_JSON_DECODER_CHECKS_FAIL'})
  CaseCount=$caseRecords.Count
  AcceptedCount=@($caseRecords | Where-Object {$_.Actual -ceq 'ACCEPT'}).Count
  RejectedCount=@($caseRecords | Where-Object {$_.Actual -ceq 'REJECT'}).Count
  CheckCount=$checks.Count
  FailedChecks=$failed.Count
  ExtractedFunctionCount=$extractedRecords.Count
  SourceSHA256Before=$sourceBefore
  SourceSHA256After=$sourceAfter
  FailurePhase=$failurePhase
  PrimaryExceptionType=$primaryType
}
[pscustomobject]@{
  RecordVersion='DSP004-CLOSED-JSON-REV1'
  Scope='EXACT_FUNCTIONS_ONLY / LOCAL_SYNTHETIC / NOT_FORMAL_WP008'
  Summary=$summary
  ExtractedFunctions=$extractedRecords.ToArray()
  Cases=$caseRecords.ToArray()
  Checks=$checks.ToArray()
  Limits=@(
    'No whole-entry execution or C# compilation',
    'No record schema or source-provenance acceptance',
    'No byte transport, child lifecycle or timing claim',
    'No coverage of the accepted 189-item list',
    'No source admission, business capture, integration or deployment',
    'DSP-004 OPEN / HOLD; B-01 OPEN; B-02 OPEN',
    'All upstream LIMITED and failure histories preserved'
  )
} | Microsoft.PowerShell.Utility\ConvertTo-Json -Depth 12
if ($null -ne $primaryType) { exit 1 }
exit 0
