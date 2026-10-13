# Fixed local pure-classification batch. Never invokes live entry/Bootstrap.
# Native comparison precedes JSON; supplied event records are not real I/O.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME, 'Modules', 'Microsoft.PowerShell.Utility', 'Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskRoot = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008'
$taskListSha = '46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C'
$taskControllerSha = '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB'
$taskChecks = [Collections.Generic.List[object]]::new()
$taskCases = [Collections.Generic.List[object]]::new()
$taskCleanupTypes = [Collections.Generic.List[object]]::new()
$taskHeldCleanupExceptions = [Collections.Generic.List[Exception]]::new()
$taskRunspace = $null
$taskLoader = $null
$taskCurrent = $null
$taskRunspaceOpened = $false
$taskRunspaceCloseReturned = $false
$taskRunspaceDisposeReturned = $false
$taskLoadOutputCount = -1
$taskLoadCount = 0
$taskCalls = 0
$taskPrimaryType = $null
$taskHeldPrimary = $null

function Add-ObservedCheck {
    param([string]$Id, [bool]$Condition)
    [void]$taskChecks.Add([pscustomobject][ordered]@{Id = $Id; Passed = $Condition})
    if (-not $Condition) { throw [InvalidOperationException]::new('FIXED_CLASSIFICATION_CHECK_FAILED') }
}

function Add-CleanupFailure {
    param([string]$Stage, [Exception]$ErrorObject)
    [void]$taskHeldCleanupExceptions.Add($ErrorObject)
    [void]$taskCleanupTypes.Add([pscustomobject][ordered]@{Stage = $Stage; Type = $ErrorObject.GetType().FullName})
}

function Get-NativeTypeName {
    param([AllowNull()][object]$Value)
    if ($null -eq $Value) { return 'ABSENT_NULL' }
    return $Value.GetType().FullName
}

$taskStates = [ordered]@{
    'S-N' = 'RAN_TO_COMPLETION'; 'S-P' = 'PENDING'; 'S-F' = 'FAULTED';
    'S-C' = 'CANCELED'; 'S-S' = 'SYNCHRONOUS_FAILURE'
}
$taskReadCodes = [ordered]@{
    'R-INVALID' = 'INVALID_REPORTED_READ_RECORD'
    'R-STOP' = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
    'R-ZERO' = 'REPORTED_POSITIVE_NORMAL_READ_ZERO_ONLY'
    'R-BODY' = 'REPORTED_BODY_BYTES_ONLY - SHORT_READ_IS_NOT_EOF'
    'R-DETECT' = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
    'R-PENDING' = 'ORIGINAL_READ_PENDING - NO EOF_INFERENCE'
    'R-FAIL' = 'REPORTED_READ_FAILURE - NO EOF_INFERENCE'
}
$taskDetection = [ordered]@{'R-NOTCLASS' = 'NOT CLASSIFIED'; 'R-PRESENT' = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'}
$taskWriteCodes = [ordered]@{
    'W-INVALID' = 'INVALID_REPORTED_WRITE_RECORD'
    'W-STOP' = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
    'W-WAITFAIL' = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
    'W-NORMAL' = 'REPORTED_FULL_RANGE_TASK_NORMAL_ONLY'
    'W-PENDING' = 'ORIGINAL_WRITE_PENDING - NO NORMAL_INPUT_CLOSE'
    'W-FAIL' = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
}
$taskProgress = [ordered]@{'W-UNKNOWN' = 'UNKNOWN'; 'W-NOCOUNT' = 'NO BYTE COUNT - CHILD RECEIPT REMAINS UNVERIFIED'}

function Convert-FixedNativeScalar {
    param([string]$Token)
    if ($Token -ceq 'null') { return $null }
    if ($Token -ceq 'true') { return $true }
    if ($Token -ceq 'false') { return $false }
    if ($taskStates.Contains($Token)) { return [string]$taskStates[$Token] }
    if ($Token -cmatch '^-?[0-9]+$') { return [int]::Parse($Token, [Globalization.CultureInfo]::InvariantCulture) }
    if ($Token -ceq 'int:0') { return [int]0 }
    if ($Token -ceq 'int64:0') { return [long]0 }
    if ($Token -ceq 'int64:20177') { return [long]20177 }
    if ($Token -ceq 'string:0') { return [string]'0' }
    if ($Token -ceq 'string:1') { return [string]'1' }
    if ($Token -ceq 'string:20177') { return [string]'20177' }
    if (@('STDOUT', 'STDERR', 'stdout', 'OTHER', 'UNKNOWN', 'ran_to_completion', 'ENDED', 'PENDING', 'TIMED_OUT', 'CANCELED', 'FAULTED', 'ended') -ccontains $Token) { return [string]$Token }
    throw [InvalidOperationException]::new('UNKNOWN_FIXED_NATIVE_TOKEN')
}

function Get-StreamCounts {
    param([Management.Automation.PowerShell]$Pipeline)
    [ordered]@{
        Error = $Pipeline.Streams.Error.Count; Warning = $Pipeline.Streams.Warning.Count
        Debug = $Pipeline.Streams.Debug.Count; Verbose = $Pipeline.Streams.Verbose.Count
        Information = $Pipeline.Streams.Information.Count; Progress = $Pipeline.Streams.Progress.Count
    }
}

try {
    $taskListBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_LOCAL_VALIDATION_CARRIER_CANDIDATE_REV1.ps1'))
    $taskControllerBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1'))
    Add-ObservedCheck 'HASH-LIST' ($taskListBytes.Length -eq 70284 -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskListBytes)) -ceq $taskListSha)
    Add-ObservedCheck 'HASH-CONTROLLER' ($taskControllerBytes.Length -eq 25573 -and [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskControllerBytes)) -ceq $taskControllerSha)
    $taskListText = [Text.UTF8Encoding]::new($false, $true).GetString($taskListBytes)
    $taskControllerText = [Text.UTF8Encoding]::new($false, $true).GetString($taskControllerBytes)

    $taskAliases = [ordered]@{}
    foreach ($taskEntry in $taskStates.GetEnumerator()) { $taskAliases[$taskEntry.Key] = '原生 string ' + $taskEntry.Value }
    foreach ($taskMap in @($taskReadCodes, $taskWriteCodes)) {
        foreach ($taskEntry in $taskMap.GetEnumerator()) { $taskAliases[$taskEntry.Key] = 'Classification = ' + $taskEntry.Value }
    }
    foreach ($taskEntry in $taskDetection.GetEnumerator()) { $taskAliases[$taskEntry.Key] = 'DetectionByte = ' + $taskEntry.Value }
    foreach ($taskEntry in $taskProgress.GetEnumerator()) { $taskAliases[$taskEntry.Key] = 'ActualPartialProgress = ' + $taskEntry.Value }
    $taskAliasesMatch = $taskAliases.Count -eq 22
    foreach ($taskEntry in $taskAliases.GetEnumerator()) {
        $taskPattern = '(?m)^\| ' + [regex]::Escape($taskEntry.Key) + ' \| ([^\r\n|]+) \|$'
        $taskMatches = [regex]::Matches($taskListText, $taskPattern)
        if ($taskMatches.Count -ne 1 -or $taskMatches[0].Groups[1].Value -cne $taskEntry.Value) { $taskAliasesMatch = $false }
    }
    Add-ObservedCheck 'ALIASES-01' $taskAliasesMatch

    $taskRows = [Collections.Generic.List[object]]::new()
    $taskSourceLines = $taskListText.Split([char]10)
    for ($taskLineIndex = 0; $taskLineIndex -lt $taskSourceLines.Length; $taskLineIndex++) {
        $taskLine = $taskSourceLines[$taskLineIndex]
        if ($taskLine -cmatch '^\| (RD-[0-9]{3}|WR-[0-9]{3}) \|') {
            $taskPieces = $taskLine.Split([char]'|')
            if ($taskPieces[0] -cne '' -or $taskPieces[-1] -cne '') { throw [InvalidOperationException]::new('FIXED_TABLE_EDGE_MISMATCH') }
            $taskCells = @($taskPieces[1..($taskPieces.Length - 2)] | ForEach-Object {$_.Trim()})
            $taskRead = $taskCells[0].StartsWith('RD-', [StringComparison]::Ordinal)
            if (($taskRead -and $taskCells.Count -ne 11) -or (-not $taskRead -and $taskCells.Count -ne 8)) { throw [InvalidOperationException]::new('FIXED_TABLE_COLUMN_MISMATCH') }
            [void]$taskRows.Add([pscustomobject]@{Id = $taskCells[0]; Read = $taskRead; Cells = $taskCells; SourceLine = $taskLineIndex + 1})
        }
    }
    $taskRowIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
    foreach ($taskRow in $taskRows) { [void]$taskRowIds.Add($taskRow.Id) }
    $taskExactSet = $taskRows.Count -eq 96 -and $taskRowIds.Count -eq 96
    for ($taskN = 1; $taskN -le 52; $taskN++) { $taskExactSet = $taskExactSet -and $taskRowIds.Contains('RD-' + $taskN.ToString('D3')) }
    for ($taskN = 1; $taskN -le 44; $taskN++) { $taskExactSet = $taskExactSet -and $taskRowIds.Contains('WR-' + $taskN.ToString('D3')) }
    Add-ObservedCheck 'TABLE-01' $taskExactSet

    $taskTokens = $null; $taskParseErrors = $null
    $taskAst = [Management.Automation.Language.Parser]::ParseInput($taskControllerText, [ref]$taskTokens, [ref]$taskParseErrors)
    $taskFunctionNames = @('Get-DSP004CaseContract', 'Get-DSP004StatusCombinations', 'Get-DSP004FixedContract', 'Test-DSP004RequestedCaseText', 'Test-DSP004DriverBytesInMemory', 'Test-DSP004FrameBytesInMemory', 'Get-DSP004ReadObservationClassification', 'Get-DSP004WriteObservationClassification', 'Get-DSP004FutureBootstrapText', 'Invoke-DSP004SingleCase')
    $taskTopFunctions = @($taskAst.EndBlock.Statements)
    $taskAstMatch = @($taskParseErrors).Count -eq 0 -and $null -eq $taskAst.ParamBlock -and $null -eq $taskAst.BeginBlock -and $null -eq $taskAst.ProcessBlock -and $null -eq $taskAst.DynamicParamBlock -and $taskTopFunctions.Count -eq 10
    for ($taskIndex = 0; $taskIndex -lt $taskTopFunctions.Count; $taskIndex++) {
        if ($taskTopFunctions[$taskIndex] -isnot [Management.Automation.Language.FunctionDefinitionAst] -or $taskIndex -ge 10 -or $taskTopFunctions[$taskIndex].Name -cne $taskFunctionNames[$taskIndex]) { $taskAstMatch = $false }
    }
    Add-ObservedCheck 'AST-01' $taskAstMatch
    $taskInitialState = [Management.Automation.Runspaces.InitialSessionState]::Create()
    $taskInitialState.LanguageMode = [Management.Automation.PSLanguageMode]::FullLanguage
    $taskRunspace = [Management.Automation.Runspaces.RunspaceFactory]::CreateRunspace($taskInitialState)
    $taskRunspace.Open(); $taskRunspaceOpened = $true
    $taskLoader = [Management.Automation.PowerShell]::Create(); $taskLoader.Runspace = $taskRunspace
    [void]$taskLoader.AddScript($taskControllerText, $false)
    $taskLoadCount++
    $taskLoadOutput = $taskLoader.Invoke(); $taskLoadOutputCount = $taskLoadOutput.Count
    $taskLoadStreams = Get-StreamCounts -Pipeline $taskLoader
    Add-ObservedCheck 'LOAD-01' ($taskLoadCount -eq 1 -and $taskLoadOutputCount -eq 0 -and -not $taskLoader.HadErrors -and @($taskLoadStreams.Values | Where-Object {$_ -ne 0}).Count -eq 0)

    foreach ($taskRow in $taskRows) {
        $taskInputCount = if ($taskRow.Read) {7} else {5}
        $taskInputTokens = @($taskRow.Cells[1..$taskInputCount])
        $taskNative = [Collections.Generic.List[object]]::new()
        $taskNativeTypes = [Collections.Generic.List[string]]::new()
        foreach ($taskToken in $taskInputTokens) {
            $taskValue = Convert-FixedNativeScalar -Token $taskToken
            [void]$taskNative.Add($taskValue); [void]$taskNativeTypes.Add((Get-NativeTypeName -Value $taskValue))
        }
        $taskName = if ($taskRow.Read) {'Get-DSP004ReadObservationClassification'} else {'Get-DSP004WriteObservationClassification'}
        $taskParameterNames = if ($taskRow.Read) {@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')} else {@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')}
        $taskCurrent = [Management.Automation.PowerShell]::Create(); $taskCurrent.Runspace = $taskRunspace
        [void]$taskCurrent.AddCommand($taskName)
        for ($taskIndex = 0; $taskIndex -lt $taskParameterNames.Count; $taskIndex++) { [void]$taskCurrent.AddParameter($taskParameterNames[$taskIndex], $taskNative[$taskIndex]) }
        $taskCalls++
        $taskOutput = $taskCurrent.Invoke()
        $taskStreams = Get-StreamCounts -Pipeline $taskCurrent
        $taskCaseRecord = [ordered]@{Id = $taskRow.Id; SourceLine = $taskRow.SourceLine; Function = $taskName; InputTokens = $taskInputTokens; NativeInputTypes = $taskNativeTypes.ToArray(); OutputCount = $taskOutput.Count; Streams = $taskStreams; Actual = $null; NativeReturnTypes = @(); Comparison = 'INCOMPLETE'}
        [void]$taskCases.Add($taskCaseRecord)
        Add-ObservedCheck ($taskRow.Id + '-CHANNELS') ($taskOutput.Count -eq 1 -and -not $taskCurrent.HadErrors -and @($taskStreams.Values | Where-Object {$_ -ne 0}).Count -eq 0)
        $taskActual = $taskOutput[0]
        $taskActualFields = [ordered]@{}; $taskReturnTypes = [Collections.Generic.List[string]]::new()
        foreach ($taskProperty in $taskActual.PSObject.Properties) {
            $taskActualFields[$taskProperty.Name] = $taskProperty.Value
            [void]$taskReturnTypes.Add($taskProperty.Name + '=' + (Get-NativeTypeName -Value $taskProperty.Value))
        }
        $taskCaseRecord.Actual = $taskActualFields; $taskCaseRecord.NativeReturnTypes = $taskReturnTypes.ToArray()
        $taskRequired = if ($taskRow.Read) {@('Classification', 'ReportedBodyBytesAfter', 'DetectionByte', 'Qualification', 'ActualPeerEof', 'ResourceOwnership', 'CaseCompletion')} else {@('Classification', 'ActualPartialProgress', 'WriteByteCount', 'ChildLengthEofShaVerification', 'InputClose', 'AutomaticResend', 'Qualification', 'ResourceOwnership', 'CaseCompletion')}
        $taskSurface = $taskActualFields.Count -eq $taskRequired.Count
        foreach ($taskField in $taskRequired) { $taskSurface = $taskSurface -and $taskActualFields.Contains($taskField) }
        foreach ($taskEntry in $taskActualFields.GetEnumerator()) {
            if ($taskEntry.Key -ceq 'ReportedBodyBytesAfter') { $taskSurface = $taskSurface -and ($null -eq $taskEntry.Value -or $taskEntry.Value.GetType() -eq [int]) }
            else { $taskSurface = $taskSurface -and $null -ne $taskEntry.Value -and $taskEntry.Value.GetType() -eq [string] }
        }
        Add-ObservedCheck ($taskRow.Id + '-SURFACE') $taskSurface
        if ($taskRow.Read) {
            if (-not $taskReadCodes.Contains($taskRow.Cells[8]) -or -not $taskDetection.Contains($taskRow.Cells[10])) { throw [InvalidOperationException]::new('UNKNOWN_FIXED_READ_EXPECTATION') }
            $taskExpectedAfter = Convert-FixedNativeScalar -Token $taskRow.Cells[9]
            $taskAfterMatches = if ($null -eq $taskExpectedAfter) {$null -eq $taskActualFields.ReportedBodyBytesAfter} else {$taskActualFields.ReportedBodyBytesAfter -is [int] -and $taskActualFields.ReportedBodyBytesAfter -eq $taskExpectedAfter}
            Add-ObservedCheck ($taskRow.Id + '-VALUES') ($taskActualFields.Classification -ceq $taskReadCodes[$taskRow.Cells[8]] -and $taskAfterMatches -and $taskActualFields.DetectionByte -ceq $taskDetection[$taskRow.Cells[10]])
            Add-ObservedCheck ($taskRow.Id + '-LIMITS') ($taskActualFields.Qualification -ceq 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED' -and $taskActualFields.ActualPeerEof -ceq 'NOT OBSERVED' -and $taskActualFields.ResourceOwnership -ceq 'NOT IMPLEMENTED' -and $taskActualFields.CaseCompletion -ceq 'NOT ESTABLISHED')
        }
        else {
            if (-not $taskWriteCodes.Contains($taskRow.Cells[6]) -or -not $taskProgress.Contains($taskRow.Cells[7])) { throw [InvalidOperationException]::new('UNKNOWN_FIXED_WRITE_EXPECTATION') }
            Add-ObservedCheck ($taskRow.Id + '-VALUES') ($taskActualFields.Classification -ceq $taskWriteCodes[$taskRow.Cells[6]] -and $taskActualFields.ActualPartialProgress -ceq $taskProgress[$taskRow.Cells[7]])
            Add-ObservedCheck ($taskRow.Id + '-LIMITS') ($taskActualFields.WriteByteCount -ceq 'NOT RETURNED BY INTERFACE' -and $taskActualFields.ChildLengthEofShaVerification -ceq 'NOT OBSERVED' -and $taskActualFields.InputClose -ceq 'NOT PERFORMED' -and $taskActualFields.AutomaticResend -ceq 'PROHIBITED' -and $taskActualFields.Qualification -ceq 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED' -and $taskActualFields.ResourceOwnership -ceq 'NOT IMPLEMENTED' -and $taskActualFields.CaseCompletion -ceq 'NOT ESTABLISHED')
        }
        $taskCaseRecord.Comparison = 'LOCAL_NATIVE_COMPARISON_PASS'
        try { $taskCurrent.Dispose() } catch { Add-CleanupFailure 'CASE_PIPELINE_DISPOSE' $_.Exception }
        $taskCurrent = $null
    }
}
catch { $taskHeldPrimary = $_.Exception; $taskPrimaryType = $_.Exception.GetType().FullName }
finally {
    if ($null -ne $taskCurrent) { try {$taskCurrent.Dispose()} catch {Add-CleanupFailure 'CURRENT_PIPELINE_DISPOSE' $_.Exception} }
    if ($null -ne $taskLoader) { try {$taskLoader.Dispose()} catch {Add-CleanupFailure 'LOADER_DISPOSE' $_.Exception} }
    if ($null -ne $taskRunspace) {
        if ($taskRunspaceOpened) { try {$taskRunspace.Close(); $taskRunspaceCloseReturned = $true} catch {Add-CleanupFailure 'RUNSPACE_CLOSE' $_.Exception} }
        try {$taskRunspace.Dispose(); $taskRunspaceDisposeReturned = $true} catch {Add-CleanupFailure 'RUNSPACE_DISPOSE' $_.Exception}
    }
}

$taskIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($taskCheck in $taskChecks) { [void]$taskIds.Add($taskCheck.Id) }
$taskFalse = @($taskChecks | Where-Object {-not $_.Passed}).Count
$taskCasePass = @($taskCases | Where-Object {$_.Comparison -ceq 'LOCAL_NATIVE_COMPARISON_PASS'}).Count
$taskAll = $null -eq $taskPrimaryType -and $taskCleanupTypes.Count -eq 0 -and $taskChecks.Count -eq 390 -and $taskIds.Count -eq 390 -and $taskFalse -eq 0 -and $taskCalls -eq 96 -and $taskCasePass -eq 96 -and $taskRunspaceCloseReturned -and $taskRunspaceDisposeReturned
$taskRecord = [pscustomobject][ordered]@{
    RecordKind = 'LOCAL_FIXED_REPORTED_READ_WRITE_CLASSIFICATION_NOT_IO_OR_ACCEPTANCE'
    Outcome = if ($taskAll) {'LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_PASS'} else {'LOCAL_REPORTED_RW_CLASSIFICATION_CHECKS_FAIL'}
    FixtureListSHA256 = $taskListSha
    ControllerSHA256 = $taskControllerSha
    LoadCount = $taskLoadCount
    LoadOutputCount = $taskLoadOutputCount
    ClassifierCalls = $taskCalls
    NativeComparisonPassCount = $taskCasePass
    CheckCount = $taskChecks.Count
    UniqueCheckIds = $taskIds.Count
    FailedChecks = $taskFalse
    PrimaryValidationFailureType = $taskPrimaryType
    CleanupFailures = $taskCleanupTypes.ToArray()
    RunspaceCloseCallReturned = $taskRunspaceCloseReturned
    RunspaceDisposeCallReturned = $taskRunspaceDisposeReturned
    Cases = $taskCases.ToArray()
    Checks = $taskChecks.ToArray()
    Scope = 'RD-001..052 AND WR-001..044 ONLY; CALLER-SUPPLIED SYNTHETIC EVENT RECORDS, NOT ACTUAL I/O'
    Serialization = 'NATIVE TYPE/VALUE COMPARISON BEFORE JSON; JSON ALONE DOES NOT PRESERVE INT32/INT64 IDENTITY'
    Excluded = [string[]]@('M_6', 'RQ_18', 'D_7', 'F_62', 'REAL_DRIVER_OR_BOOTSTRAP', 'REAL_READ_WRITE_TASKS', 'SOURCE_ADMISSION', 'ACTUAL_CAPTURE', 'INTEGRATION', 'OTHER_PROJECTS')
    CleanupQualification = 'LOCAL CLOSE/DISPOSE CALL RETURN OBSERVATIONS ONLY; NOT FULL ENGINE OR RESOURCE SETTLEMENT'
    Preserved = 'ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN; NO AGGREGATE OR FULL-189 VERDICT'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskRecord -Depth 12 -Compress
if ($taskAll) {exit 0} else {exit 1}
