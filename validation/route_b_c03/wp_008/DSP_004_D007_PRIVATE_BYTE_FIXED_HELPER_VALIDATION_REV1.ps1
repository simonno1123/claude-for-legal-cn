# Closed local synthetic validation. New candidate only; no historical private
# payload access, real Driver/Bootstrap, source admission or integration.
# Native comparisons precede JSON; JSON is an observation record, not authority.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
Import-Module Microsoft.PowerShell.Utility -ErrorAction Stop

$checks = [Collections.Generic.List[object]]::new()
$checkIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
$heldValidationErrors = [Collections.Generic.List[Exception]]::new()
$primaryFailureType = $null
$failureStage = $null
$stage = 'FIXED_SOURCE_PREFLIGHT'
$first = $null
$repeat = $null
$firstCaptured = $null
$repeatCaptured = $null
$oracleDigest = $null
$candidateSha = $null
$fixtureSha = $null
$compiled = $false
$probeCalls = 0
$priorUniqueIds = $null

function Confirm-LocalCheck([string] $Id, [bool] $Pass) {
  if (-not $checkIds.Add($Id)) { throw [InvalidOperationException]::new('DUPLICATE_LOCAL_CHECK_ID') }
  $checks.Add([pscustomobject]@{ Id = $Id; Pass = $Pass })
  if (-not $Pass) { throw [InvalidOperationException]::new('FIXED_LOCAL_CHECK_NOT_MET') }
}

function Capture-PublicObservation([object] $Value, [string] $Prefix) {
  $actual = [ordered]@{}
  $types = [ordered]@{}
  $properties = @($Value.GetType().GetProperties([Reflection.BindingFlags]'Public,Instance,DeclaredOnly'))
  Confirm-LocalCheck "$Prefix.PUBLIC_PROPERTIES_PRESENT" ($properties.Count -gt 0)
  foreach ($property in $properties) {
    Confirm-LocalCheck "$Prefix.GETTER_ONLY.$($property.Name)" ($null -eq $property.GetSetMethod($true) -and $property.GetIndexParameters().Length -eq 0)
    $allowed = $property.PropertyType -in @([string], [bool], [int], [long])
    Confirm-LocalCheck "$Prefix.SAFE_NATIVE_TYPE.$($property.Name)" $allowed
    $observed = $property.GetValue($Value)
    Confirm-LocalCheck "$Prefix.NATIVE_VALUE.$($property.Name)" ($null -eq $observed -or $observed.GetType() -eq $property.PropertyType)
    $actual[$property.Name] = $observed
    $types[$property.Name] = $property.PropertyType.FullName
  }
  [pscustomobject]@{ Actual = $actual; NativeTypes = $types }
}

try {
  $candidatePath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_D007_PRIVATE_BYTE_FIXED_HELPER_HANDOFF_CANDIDATE_REV1.cs'
  $fixturePath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1'
  $candidateBytes = [IO.File]::ReadAllBytes($candidatePath)
  $candidateSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($candidateBytes))
  Confirm-LocalCheck 'PRE.CANDIDATE_FIXED_SHA_LENGTH' ($candidateSha -ceq '666BF56D68FAC64F67E25B55DA26173593E30E8FEC9D4AC89B5DC489B1E4AFD3' -and $candidateBytes.Length -eq 19442)
  $fixtureBytes = [IO.File]::ReadAllBytes($fixturePath)
  $fixtureSha = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($fixtureBytes))
  Confirm-LocalCheck 'PRE.FIXTURE_FIXED_SHA_LENGTH' ($fixtureSha -ceq '46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C' -and $fixtureBytes.Length -eq 70284)
  $strictUtf8 = [Text.UTF8Encoding]::new($false, $true)
  $fixtureText = $strictUtf8.GetString($fixtureBytes)
  $fixtureLines = $fixtureText -split "`n"
  $d007Lines = @($fixtureLines | Where-Object { $_.StartsWith('| D-007 |', [StringComparison]::Ordinal) })
  $k003Lines = @($fixtureLines | Where-Object { $_.StartsWith('| K-003 |', [StringComparison]::Ordinal) })
  Confirm-LocalCheck 'PRE.ONE_D007_ONE_K003' ($d007Lines.Count -eq 1 -and $k003Lines.Count -eq 1)
  $d007Cells = @($d007Lines[0].Split('|') | ForEach-Object { $_.Trim() })
  $k003Cells = @($k003Lines[0].Split('|') | ForEach-Object { $_.Trim() })
  Confirm-LocalCheck 'PRE.D007_NATIVE_SHAPE_FROM_FIXED_LIST' ($d007Cells.Count -eq 6 -and $d007Cells[2] -ceq '原生 byte[]：20177 个 byte 0')
  Confirm-LocalCheck 'PRE.D007_INDEPENDENT_EXPECTED_TEXT' ($d007Cells[3] -ceq 'FIXED_DRIVER_SHA_MISMATCH，仅预置条件满足后才可使用此预期')
  Confirm-LocalCheck 'PRE.D007_DIGEST_PRECONDITION_RECORDED' ($d007Cells[4].Contains('未来准备端独立摘要须先确认该合成数据不等于 K 的完整 DriverSha256；不得用受测函数回填。'))
  $recordedDriverLiteral = '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210'
  Confirm-LocalCheck 'PRE.K003_RECORDED_LITERAL_ONLY' ($k003Cells.Count -eq 6 -and $k003Cells[4] -ceq $recordedDriverLiteral)
  $negativeFields = 'D 全部：Authority=NOT ESTABLISHED，SourceAdmission=NOT ESTABLISHED，FrozenHandoff=NOT IMPLEMENTED，ChildLengthEofShaVerification=NOT OBSERVED，CaseCompletion=NOT ESTABLISHED；'
  Confirm-LocalCheck 'PRE.NEGATIVE_FIELDS_FROM_FIXED_LIST' ($fixtureText.Contains($negativeFields, [StringComparison]::Ordinal))

  $stage = 'SEPARATE_OUTSIDE_SYNTHETIC_ORACLE'
  $oracleBytes = [byte[]]::new(20177)
  Confirm-LocalCheck 'ORACLE.NATIVE_NEW_ZERO_BYTES' ($oracleBytes.GetType() -eq [byte[]] -and $oracleBytes.Length -eq 20177 -and @($oracleBytes | Where-Object { $_ -ne 0 }).Count -eq 0)
  $oracleDigest = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($oracleBytes))
  Confirm-LocalCheck 'ORACLE.FULL_HEX_AND_RECORD_INEQUALITY_BEFORE_PROBE' ($oracleDigest -cmatch '^[0-9A-F]{64}$' -and $oracleDigest -cne $recordedDriverLiteral -and $probeCalls -eq 0)

  $stage = 'FIXED_NEW_CANDIDATE_COMPILE'
  $typeName = 'Dsp004D007PrivateFixedHelper.Dsp004D007PrivateByteFixedHelperHandoffCandidateRev1'
  Confirm-LocalCheck 'COMPILE.TYPE_NOT_ALREADY_LOADED' ($null -eq ($typeName -as [type]))
  $sourceText = $strictUtf8.GetString($candidateBytes)
  $compiledTypes = @(Add-Type -TypeDefinition $sourceText -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
  $compiled = $true
  $candidateType = $typeName -as [type]
  Confirm-LocalCheck 'COMPILE.EXACT_PUBLIC_TYPE' ($null -ne $candidateType -and $candidateType.IsSealed)
  $methods = @($candidateType.GetMethods([Reflection.BindingFlags]'Public,Static,DeclaredOnly'))
  Confirm-LocalCheck 'API.ONLY_FIXED_ZERO_ARGUMENT_ENTRY' ($methods.Count -eq 1 -and $methods[0].Name -ceq 'RunFixedLocalD007Probe' -and $methods[0].GetParameters().Length -eq 0)
  Confirm-LocalCheck 'API.NO_PUBLIC_CONSTRUCTOR_FIELDS_OR_EVENTS' ($candidateType.GetConstructors().Length -eq 0 -and $candidateType.GetFields([Reflection.BindingFlags]'Public,Static,Instance,DeclaredOnly').Length -eq 0 -and $candidateType.GetEvents().Length -eq 0)

  $stage = 'FIRST_FIXED_LOCAL_PROBE'
  $probeCalls++
  $first = [Dsp004D007PrivateFixedHelper.Dsp004D007PrivateByteFixedHelperHandoffCandidateRev1]::RunFixedLocalD007Probe()
  $firstCaptured = Capture-PublicObservation $first 'FIRST'
  $observed = $firstCaptured.Actual
  Confirm-LocalCheck 'FIRST.OUTCOME' ($observed.Outcome -ceq 'LOCAL_D007_NATIVE_HELPER_COMPARISON_PASS' -and -not $observed.RepeatRefused)
  Confirm-LocalCheck 'FIRST.SOURCE_ONCE_EXACT_SHA' ($observed.ControllerReadAttempts -eq 1 -and $observed.ControllerSnapshotSHA256 -ceq '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB' -and $observed.ControllerSnapshotVerified -and $observed.DefinitionStructureVerified)
  Confirm-LocalCheck 'FIRST.PRIVATE_SHAPE_PREPARATION_ONCE' ($observed.PrivatePayloadCreated -and $observed.PrivatePayloadLength -eq 20177 -and $observed.ZeroShapeBeforeDigest -and $observed.ZeroShapeAfterDigest -and $observed.PreparationHashCalls -eq 1)
  Confirm-LocalCheck 'FIRST.NEW_DIGEST_VS_INDEPENDENT_OUTSIDE_ORACLE' ($observed.PreparedSyntheticSHA256 -cmatch '^[0-9A-F]{64}$' -and $observed.PreparedSyntheticSHA256 -ceq $oracleDigest -and $observed.DifferentFromRecordedDriverLiteral -and -not [string]::IsNullOrEmpty($observed.PreparationHashImplementationType))
  Confirm-LocalCheck 'FIRST.FIXED_DEFINITIONS_LOADED_ONCE_SILENT' ($observed.DefinitionLoadAttempts -eq 1 -and $observed.DefinitionLoadReturned -and $observed.DefinitionLoadOutputCount -eq 0 -and $observed.DefinitionLoadNonOutputStreamCount -eq 0)
  Confirm-LocalCheck 'FIRST.CALLER_COMMAND_AND_SAME_REFERENCE_BEFORE' ($observed.CallerCommandShapeBefore -and $observed.CallerParameterNativeByteArray -and $observed.CallerParameterSamePreparedReferenceBefore)
  Confirm-LocalCheck 'FIRST.HELPER_ONCE_ONE_RESULT_SILENT_OTHER_STREAMS' ($observed.HelperInvokeAttempts -eq 1 -and $observed.HelperInvokeReturned -and $observed.HelperOutputCount -eq 1 -and $observed.HelperNonOutputStreamCount -eq 0)
  Confirm-LocalCheck 'FIRST.CALLER_COMMAND_AND_SAME_REFERENCE_AFTER' ($observed.CallerCommandShapeAfter -and $observed.CallerParameterSamePreparedReferenceAfter -and $observed.ZeroShapeAfterInvoke)
  $expectedTarget = [ordered]@{ TargetTextCheck = 'FIXED_DRIVER_SHA_MISMATCH'; TargetAuthority = 'NOT ESTABLISHED'; TargetSourceAdmission = 'NOT ESTABLISHED'; TargetFrozenHandoff = 'NOT IMPLEMENTED'; TargetChildLengthEofShaVerification = 'NOT OBSERVED'; TargetCaseCompletion = 'NOT ESTABLISHED' }
  foreach ($name in $expectedTarget.Keys) { Confirm-LocalCheck "FIRST.NATIVE_TARGET.$name" ($observed[$name].GetType() -eq [string] -and $observed[$name] -ceq $expectedTarget[$name]) }
  Confirm-LocalCheck 'FIRST.NATIVE_COMPARISON_COMPLETE' ($observed.NativeComparisonCompleted -and $observed.LocalComparisonPass)
  foreach ($name in @('InvocationDisposeReturned', 'LoaderDisposeReturned', 'RunspaceCloseReturned', 'RunspaceDisposeReturned', 'PreparationHasherDisposeReturned')) { Confirm-LocalCheck "FIRST.LOCAL_CLEANUP_RETURN.$name" $observed[$name] }
  Confirm-LocalCheck 'FIRST.NO_PRIMARY_OR_SECONDARY_FAILURE' ($null -eq $observed.PrimaryFailureType -and $null -eq $observed.PrimaryFailureStage -and $observed.SecondaryFailureCount -eq 0 -and $observed.SecondaryFailureStagesAndTypes -ceq '')
  Confirm-LocalCheck 'FIRST.LOCAL_TIMER_OBSERVATION_ONLY' ($observed.ElapsedMilliseconds.GetType() -eq [long] -and $observed.ElapsedMilliseconds -ge 0)
  $qualifications = [ordered]@{
    InputScope = 'NEW PRIVATE SYNTHETIC ZERO ARRAY ONLY; NO HISTORICAL PAYLOAD OR REAL DRIVER'
    DigestQualification = 'PREPARATION INTERFACE INDEPENDENT OF HELPER; SAME DOTNET CRYPTO STACK; NOT PROVIDER INDEPENDENCE OR SOURCE VERIFICATION'
    ReferenceQualification = 'CALLER COMMAND PARAMETER REFERENCE OBSERVATION ONLY; CALLEE REFERENCE AND FREEZE NOT ESTABLISHED'
    SourceQualification = 'FIXED LOCAL SNAPSHOT INTEGRITY ONLY; NOT SOURCE ADMISSION OR TRUSTED DEPENDENCY ROOT'
    ResourceQualification = 'LOCAL DISPOSE/CLOSE RETURNS ONLY; NOT COMPLETE ENGINE/RESOURCE SETTLEMENT OR HARD STOP PROOF'
    RetentionQualification = 'RAW ARRAYS/RETURN/ORIGINAL EXCEPTIONS PRIVATE IN THIS PROCESS ONLY; NO CROSS-PROCESS RETENTION PROOF'
    Authority = 'NOT ESTABLISHED'
    SourceAdmission = 'NOT ESTABLISHED'
    PositiveDriverSHA = 'NOT COVERED'
  }
  foreach ($name in $qualifications.Keys) { Confirm-LocalCheck "FIRST.QUALIFICATION.$name" ($observed[$name] -ceq $qualifications[$name]) }

  $stage = 'SAME_ASSEMBLY_REPEAT_REFUSAL'
  $probeCalls++
  $repeat = [Dsp004D007PrivateFixedHelper.Dsp004D007PrivateByteFixedHelperHandoffCandidateRev1]::RunFixedLocalD007Probe()
  $repeatCaptured = Capture-PublicObservation $repeat 'REPEAT'
  $repeatValues = $repeatCaptured.Actual
  Confirm-LocalCheck 'REPEAT.EXACT_REFUSAL' ($repeatValues.Outcome -ceq 'REPEATED_LOCAL_D007_REQUEST_REFUSED' -and $repeatValues.RepeatRefused)
  foreach ($name in $repeatCaptured.NativeTypes.Keys) {
    if ($repeatCaptured.NativeTypes[$name] -ceq 'System.Boolean' -and $name -cne 'RepeatRefused') { Confirm-LocalCheck "REPEAT.NO_NEW_ACTIVITY.$name" (-not $repeatValues[$name]) }
  }
  foreach ($name in @('ControllerReadAttempts', 'PreparationHashCalls', 'DefinitionLoadAttempts', 'HelperInvokeAttempts', 'SecondaryFailureCount')) { Confirm-LocalCheck "REPEAT.ZERO_ATTEMPTS.$name" ($repeatValues[$name] -eq 0) }
  foreach ($name in @('PrivatePayloadLength', 'DefinitionLoadOutputCount', 'DefinitionLoadNonOutputStreamCount', 'HelperOutputCount', 'HelperNonOutputStreamCount', 'ElapsedMilliseconds')) { Confirm-LocalCheck "REPEAT.NO_OBSERVATION.$name" ($repeatValues[$name] -eq -1) }
  foreach ($name in @('ControllerSnapshotSHA256', 'PreparedSyntheticSHA256', 'PreparationHashImplementationType', 'TargetTextCheck', 'TargetAuthority', 'TargetSourceAdmission', 'TargetFrozenHandoff', 'TargetChildLengthEofShaVerification', 'TargetCaseCompletion', 'PrimaryFailureType', 'PrimaryFailureStage')) { Confirm-LocalCheck "REPEAT.NO_NEW_VALUE.$name" ($null -eq $repeatValues[$name]) }
  Confirm-LocalCheck 'REPEAT.NO_SECONDARY_FAILURE' ($repeatValues.SecondaryFailureStagesAndTypes -ceq '')
  foreach ($name in $qualifications.Keys) { Confirm-LocalCheck "REPEAT.QUALIFICATION.$name" ($repeatValues[$name] -ceq $qualifications[$name]) }

  $stage = 'PRIOR_RECORD_ID_DEDUPLICATION_ONLY'
  $priorRecords = @(
    @{ Path = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_REPORTED_RW_CLASSIFICATION_REV1_OBSERVED_RESULT.json'; SHA256 = '492EE32855FDA4E8FABF34586A677BD9BBB3F7CAF377D1BDDF9D2B96C5809451'; Count = 96; Outcome = 'LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS' },
    @{ Path = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_REMAINING_PURE_CHECKS_REV1_OBSERVED_RESULT.json'; SHA256 = 'BA9AAD446C87D1573DF4AA683C99B712F3D6CB80E3897675E1E0EE3064F078B5'; Count = 92; Outcome = 'LOCAL_REMAINING_PURE_CHECKS_PASS' }
  )
  $priorIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  $recordIndex = 0
  foreach ($record in $priorRecords) {
    $recordIndex++
    $recordBytes = [IO.File]::ReadAllBytes($record.Path)
    Confirm-LocalCheck "PRIOR.EXACT_RECORD_SHA.$recordIndex" ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($recordBytes)) -ceq $record.SHA256)
    $prior = $strictUtf8.GetString($recordBytes) | ConvertFrom-Json -Depth 30
    Confirm-LocalCheck "PRIOR.RECORDED_OUTCOME_COUNT.$recordIndex" ($prior.Outcome -ceq $record.Outcome -and $prior.Cases.Count -eq $record.Count -and $prior.NativeComparisonPassCount -eq $record.Count -and $prior.FailedChecks -eq 0)
    foreach ($item in $prior.Cases) { Confirm-LocalCheck "PRIOR.UNIQUE_ID.$($item.Id)" ($item.Id.GetType() -eq [string] -and $priorIds.Add($item.Id)) }
  }
  $priorUniqueIds = $priorIds.Count
  Confirm-LocalCheck 'COVERAGE.PRIOR_188_EXCLUDES_D007' ($priorUniqueIds -eq 188 -and -not $priorIds.Contains('D-007'))
  $plannedIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
  foreach ($line in $fixtureLines) {
    $match = [regex]::Match($line, '^\| ((?:M|RQ|D|F|RD|WR)-[0-9]{3}) \|')
    if ($match.Success) { Confirm-LocalCheck "COVERAGE.PLAN_UNIQUE.$($match.Groups[1].Value)" ($plannedIds.Add($match.Groups[1].Value)) }
  }
  Confirm-LocalCheck 'COVERAGE.NEW_D007_NOT_AN_EXTRA_REPEAT_CASE' ($plannedIds.Count -eq 189 -and $priorIds.Add('D-007') -and $priorIds.SetEquals($plannedIds))
  Confirm-LocalCheck 'POST.CANDIDATE_UNCHANGED' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData([IO.File]::ReadAllBytes($candidatePath))) -ceq $candidateSha)
}
catch {
  $heldValidationErrors.Add($_.Exception)
  $primaryFailureType = $_.Exception.GetType().FullName
  $failureStage = $stage
}

$failedCount = @($checks | Where-Object { -not $_.Pass }).Count
$passed = $null -eq $primaryFailureType -and $failedCount -eq 0 -and $probeCalls -eq 2 -and $null -ne $firstCaptured -and $null -ne $repeatCaptured
[pscustomobject]@{
  RecordKind = 'NEW_PRIVATE_SYNTHETIC_D007_FIXED_HELPER_NATIVE_COMPARISON_ONLY'
  Outcome = $(if ($passed) { 'LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_PASS' } else { 'LOCAL_D007_PRIVATE_FIXED_HELPER_CHECKS_INCOMPLETE' })
  CandidateSHA256 = $candidateSha
  FixtureListSHA256 = $fixtureSha
  ControllerSHA256 = '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB'
  Compiled = $compiled
  PublicProbeCalls = $probeCalls
  NewPlanItemIds = @('D-007')
  PriorRecordUniqueItemIds = $priorUniqueIds
  CombinedLocalPurePlanItems = $(if ($passed) { 189 } else { $null })
  OutsideNewSyntheticOracleSHA256 = $oracleDigest
  DigestOracleQualification = 'SEPARATE NEW ZERO ARRAY; NEVER PASSED TO CANDIDATE OR HELPER; SAME DOTNET CRYPTO STACK; NOT CRYPTO PROVIDER INDEPENDENCE'
  FirstNativeObservation = $firstCaptured
  SameAssemblyRepeatObservation = $repeatCaptured
  CheckCount = $checks.Count
  UniqueCheckIds = $checkIds.Count
  FailedChecks = $failedCount
  PrimaryValidationFailureType = $primaryFailureType
  PrimaryValidationFailureStage = $failureStage
  Checks = $checks.ToArray()
  CoverageQualification = '188 PRIOR RECORDED LOCAL PURE ITEMS PLUS ONE NEW D007 OBSERVATION; NOT FORMAL 189 ITEM ACCEPTANCE OR OVERALL EXECUTION QUALIFICATION'
  PreservedLimited = 'ALL LIMITED RETAINED; CALLEE REFERENCE/FREEZE, TRUSTED DEPENDENCIES, HARD STOP, COMPLETE RESOURCE SETTLEMENT NOT ESTABLISHED'
  PositiveDriverSHA = 'NOT COVERED'
  SourceAdmission = 'NOT ESTABLISHED'
  ActualCapture = 'NOT AUTHORIZED / NOT PERFORMED'
  Integration = 'NOT AUTHORIZED / NOT PERFORMED'
  CandidateAcceptance = 'PENDING PROJECT OWNER DECISION'
  DSP004 = 'OPEN / HOLD'
  B01 = 'OPEN'
  B02 = 'OPEN'
} | ConvertTo-Json -Depth 30
if (-not $passed) { exit 1 }
