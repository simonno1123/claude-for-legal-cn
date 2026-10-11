# Authorized local synthetic implementation/validation batch only.
# This NEW carrier is not accepted, integrated or a source-admission interface.
# The accepted private-slot candidate is unchanged and still refuses dispatch.
# This carrier separately owns a new synthetic array and invokes exactly one
# fixed helper from the complete, hash-bound controller text in an empty local
# runspace. It does NOT extract or forward the candidate's private payload.
# No real driver, 189-item carrier, business material or external service is read.
# A separately bound outer supervisor must control startup, I/O and elapsed time.
# Local reference/return observations are not trust, immutability, callee-identity,
# complete resource-settlement, authority, admission or overall completion proof.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$PSModuleAutoLoadingPreference = 'None'
Import-Module -Name ([IO.Path]::Combine($PSHOME, 'Modules', 'Microsoft.PowerShell.Utility', 'Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskRoot = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008'
$taskSlotSha = '904146E082C2CAE73E2E25BAD1549C15DD076E6E206A6FC0854E18A43DA543B3'
$taskControllerSha = '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB'
$taskRecordedLiteral = '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210'
$taskChecks = [Collections.Generic.List[object]]::new()
$taskRetainedErrors = [Collections.Generic.List[Exception]]::new()
$taskPrimaryFailureType = $null
$taskCleanupFailureTypes = [Collections.Generic.List[string]]::new()
$taskCompileCompleted = $false
$taskSlotCalls = 0
$taskRequestCalls = 0
$taskControllerLoadAttempts = 0
$taskDutAttempts = 0
$taskDutReturns = 0
$taskOracleHex = $null
$taskCarrierHex = $null
$taskPostHex = $null
$taskSlotHex = $null
$taskSlotMetadata = [ordered]@{}
$taskRequestCodes = [Collections.Generic.List[string]]::new()
$taskDutMetadata = [ordered]@{}
$taskRuntimeMetadata = $null
$taskRunspace = $null
$taskPowerShell = $null
$taskCleanupObservation = 'NOT ATTEMPTED'
$taskFailureStage = 'SOURCE_CHECKS'
$taskArgumentReferenceObserved = $false

function Add-LocalCheck {
    param([string]$Id, [bool]$Condition, [string]$Scope)
    [void]$taskChecks.Add([pscustomobject][ordered]@{ Id = $Id; Scope = $Scope; Passed = $Condition })
    if (-not $Condition) { throw [InvalidOperationException]::new('LOCAL_CHECK_FAILED') }
}

try {
    # Read each owned code source once, verify that snapshot, then use THAT text.
    $taskSlotBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_D007_CONTROLLED_SAME_PAYLOAD_HANDOFF_CANDIDATE_REV1.cs'))
    Add-LocalCheck 'SLOT-SRC-01' ($taskSlotBytes.Length -eq 11843) 'Fixed accepted source byte length'
    Add-LocalCheck 'SLOT-SRC-02' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskSlotBytes)) -ceq $taskSlotSha) 'Exact accepted source snapshot SHA'
    Add-LocalCheck 'SLOT-SRC-03' (-not ($taskSlotBytes[0] -eq 239 -and $taskSlotBytes[1] -eq 187 -and $taskSlotBytes[2] -eq 191)) 'No source BOM'
    $taskSlotText = [Text.UTF8Encoding]::new($false, $true).GetString($taskSlotBytes)
    $taskControllerBytes = [IO.File]::ReadAllBytes([IO.Path]::Combine($taskRoot, 'DSP_004_OUTER_CONTROLLER_CANDIDATE_REV1.ps1'))
    Add-LocalCheck 'DUT-SRC-01' ($taskControllerBytes.Length -eq 25573) 'Complete fixed controller byte length'
    Add-LocalCheck 'DUT-SRC-02' ([Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskControllerBytes)) -ceq $taskControllerSha) 'Complete controller snapshot SHA'
    Add-LocalCheck 'DUT-SRC-03' (-not ($taskControllerBytes[0] -eq 239 -and $taskControllerBytes[1] -eq 187 -and $taskControllerBytes[2] -eq 191)) 'No controller source BOM'
    $taskControllerText = [Text.UTF8Encoding]::new($false, $true).GetString($taskControllerBytes)

    Add-LocalCheck 'SLOT-LOAD-01' ($null -eq [Management.Automation.PSTypeName]::new('Dsp004D007ControlledSamePayloadHandoffCandidateRev1').Type) 'No preexisting candidate type'
    $taskTypes = @(Microsoft.PowerShell.Utility\Add-Type -TypeDefinition $taskSlotText -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
    $taskCompileCompleted = $true
    Add-LocalCheck 'SLOT-LOAD-02' ($taskTypes.Count -eq 3) 'Three compiler-reported types including the private slot type; no private-member access'
    $taskType = [Management.Automation.PSTypeName]::new('Dsp004D007ControlledSamePayloadHandoffCandidateRev1').Type
    $taskRecordType = $taskType.GetNestedType('FixedHandoffRequestRecord', [Reflection.BindingFlags]::Public)
    $taskPrivateTypeNames = @($taskTypes | Where-Object { $_.IsNestedPrivate } | ForEach-Object { $_.FullName })
    Add-LocalCheck 'SLOT-LOAD-03' ($taskTypes -contains $taskType -and $taskTypes -contains $taskRecordType -and $taskPrivateTypeNames.Count -eq 1 -and $taskPrivateTypeNames[0] -ceq 'Dsp004D007ControlledSamePayloadHandoffCandidateRev1+PrivatePayloadSlot') 'Exact compiler-reported type identities only'
    $taskFlags = [Reflection.BindingFlags]::Public -bor [Reflection.BindingFlags]::Instance -bor [Reflection.BindingFlags]::Static -bor [Reflection.BindingFlags]::DeclaredOnly
    Add-LocalCheck 'SLOT-API-01' ($taskType.IsSealed -and $taskType.IsPublic -and $taskType.GetConstructors().Count -eq 0) 'Sealed type with no public constructor'
    Add-LocalCheck 'SLOT-API-02' ($taskType.GetFields($taskFlags).Count -eq 0) 'No public raw fields'
    $taskMethods = @($taskType.GetMethods($taskFlags) | Where-Object { -not $_.IsSpecialName })
    Add-LocalCheck 'SLOT-API-03' ($taskMethods.Count -eq 2) 'Exactly preparation and refusal request methods'
    $taskPrepare = $taskType.GetMethod('PrepareD007ParameterSlotOnly', $taskFlags)
    $taskRequest = $taskType.GetMethod('RequestFixedD007Handoff', $taskFlags)
    Add-LocalCheck 'SLOT-API-04' ($taskPrepare.IsStatic -and $taskPrepare.GetParameters().Count -eq 0 -and $taskPrepare.ReturnType -eq $taskType) 'Zero-argument preparation shape'
    Add-LocalCheck 'SLOT-API-05' (-not $taskRequest.IsStatic -and $taskRequest.GetParameters().Count -eq 0 -and $taskRequest.ReturnType -eq $taskRecordType) 'Zero-argument per-instance refusal request shape'
    $taskProperties = @($taskType.GetProperties($taskFlags))
    $taskSafeProperties = $taskProperties.Count -eq 23
    foreach ($taskProperty in $taskProperties) {
        if ($taskProperty.CanWrite -or $taskProperty.PropertyType -ne [string] -or $taskProperty.GetIndexParameters().Count -ne 0) { $taskSafeProperties = $false }
    }
    Add-LocalCheck 'SLOT-API-06' $taskSafeProperties '23 read-only non-indexed string properties; no private-field reflection'
    $taskRecordProperties = @($taskRecordType.GetProperties($taskFlags))
    $taskSafeRecord = $taskRecordType.IsSealed -and $taskRecordType.GetConstructors().Count -eq 0 -and $taskRecordProperties.Count -eq 7
    foreach ($taskProperty in $taskRecordProperties) {
        if ($taskProperty.CanWrite -or $taskProperty.PropertyType -ne [string] -or $taskProperty.GetIndexParameters().Count -ne 0) { $taskSafeRecord = $false }
    }
    Add-LocalCheck 'SLOT-API-07' $taskSafeRecord 'Sealed readonly request metadata only'

    # Separate oracle input/API; same local .NET crypto stack, not a provider audit.
    $taskOracleBytes = [byte[]]::new(20177)
    Add-LocalCheck 'ORACLE-01' ($taskOracleBytes.GetType() -eq [byte[]] -and $taskOracleBytes.Length -eq 20177) 'Independent native oracle fixture shape'
    $taskOracleZeros = $true
    foreach ($taskByte in $taskOracleBytes) { if ($taskByte -ne 0) { $taskOracleZeros = $false; break } }
    Add-LocalCheck 'ORACLE-02' $taskOracleZeros 'Oracle fixture all-zero content'
    $taskHashOracle = [Security.Cryptography.SHA256]::Create()
    try { $taskOracleHex = [BitConverter]::ToString($taskHashOracle.ComputeHash($taskOracleBytes)).Replace('-', '') }
    finally { $taskHashOracle.Dispose() }
    Add-LocalCheck 'ORACLE-03' ($taskOracleHex -cmatch '\A[A-F0-9]{64}\z') 'Full oracle digest'
    Add-LocalCheck 'ORACLE-04' ($taskOracleHex -cne $taskRecordedLiteral) 'Synthetic mismatch relation only; no real driver verification'

    $taskSlotCalls++
    $taskSlot = $taskPrepare.Invoke($null, [object[]]@())
    Add-LocalCheck 'SLOT-RUN-01' ($taskSlot.GetType() -eq $taskType) 'Exact candidate result type'
    $taskSlotHex = $taskSlot.SyntheticDigestHex
    Add-LocalCheck 'SLOT-RUN-02' ($taskSlotHex -ceq $taskOracleHex) 'Preparation digest equals separate oracle'
    $taskExpectedSlot = [ordered]@{
        PreparationRelation = 'DIFFERENT_FROM_RECORDED_LITERAL'
        ObservationCode = 'INTERNAL_SLOT_REFERENCE_RECORDED_ONLY'
        SyntheticDigestHex = $taskOracleHex
        FixedTargetName = 'Test-DSP004DriverBytesInMemory'
        FixedParameterName = 'Payload'
        RecordedParameterSignature = 'SINGLE OBJECT PARAMETER; BYTE ARRAY VALUE REQUIRED'
        ParameterSlotQualification = 'INTERNAL PREPARATION-TO-SLOT REFERENCE ONLY; ACTUAL ARGUMENT BINDING NOT OBSERVED'
        PayloadRetentionQualification = 'PRIVATE REFERENCE ONLY; EXCLUSIVE OWNERSHIP, FREEZE AND LIFETIME NOT ESTABLISHED'
        DigestRetentionQualification = 'PRIVATE REFERENCE ONLY; IMPLEMENTATION IDENTITY AND TRUST NOT ESTABLISHED'
        ExceptionRetentionQualification = 'NO PREPARATION EXCEPTION REFERENCE RECORDED'
        DigestQualification = 'SYNTHETIC BYTE DIGEST ONLY; RECORDED LITERAL COMPARISON; NOT REAL SOURCE VERIFICATION'
        Authority = 'NOT ESTABLISHED'
        SourceAdmission = 'NOT ESTABLISHED'
        TrustedLoadIdentity = 'UNBOUND'
        HashImplementationIdentity = 'UNBOUND'
        FixedInvocationAdapter = 'NOT IMPLEMENTED'
        ActualParameterIdentity = 'NOT OBSERVED'
        FrozenHandoff = 'NOT IMPLEMENTED'
        SamePayloadDutUse = 'NOT ESTABLISHED'
        DutInvocation = 'NOT PERFORMED BY THIS API'
        D007ItemOutcome = 'NOT DETERMINED BY THIS API'
        TimingAndOuterStop = 'NOT ESTABLISHED'
        PrivateFailureRetentionQualification = 'NO EXCEPTION GETTER OR FORMATTING; FAILURE RETENTION LIMITED'
    }
    $taskIndex = 0
    foreach ($taskEntry in $taskExpectedSlot.GetEnumerator()) {
        $taskIndex++
        $taskActual = $taskSlot.($taskEntry.Key)
        $taskSlotMetadata[$taskEntry.Key] = $taskActual
        Add-LocalCheck ('SLOT-META-{0:D2}' -f $taskIndex) ($taskActual -is [string] -and $taskActual -ceq $taskEntry.Value) ('Candidate string only: ' + $taskEntry.Key)
    }
    for ($taskRequestIndex = 1; $taskRequestIndex -le 2; $taskRequestIndex++) {
        $taskRequestCalls++
        $taskRequestResult = $taskRequest.Invoke($taskSlot, [object[]]@())
        Add-LocalCheck ('REQUEST-{0}-TYPE' -f $taskRequestIndex) ($taskRequestResult.GetType() -eq $taskRecordType) 'Exact request result type'
        $taskExpectedRequest = [ordered]@{
            RequestCode = if ($taskRequestIndex -eq 1) { 'FIRST_REQUEST_REFUSED_UNBOUND' } else { 'REPEATED_REQUEST_REFUSED' }
            ReservationQualification = 'PER-INSTANCE LOCAL REQUEST ONLY; NOT A DUT ATTEMPT RECORD'
            Disposition = 'UNCONDITIONALLY REFUSED; NO FIXED INVOCATION ADAPTER'
            LocalAttemptQualification = 'THIS API HAS NOT ATTEMPTED DUT CALL OR DUT RESULT CONSUMPTION'
            ItemOutcome = 'NOT DETERMINED; EXTERNAL ATTEMPT EVIDENCE NOT INSPECTED'
            ResourceSettlement = 'NOT OBSERVED; NO LIVE DUT RESOURCES CREATED BY THIS API'
            Authority = 'NOT ESTABLISHED'
        }
        $taskIndex = 0
        foreach ($taskEntry in $taskExpectedRequest.GetEnumerator()) {
            $taskIndex++
            Add-LocalCheck ('REQUEST-{0}-META-{1:D2}' -f $taskRequestIndex, $taskIndex) ($taskRequestResult.($taskEntry.Key) -is [string] -and $taskRequestResult.($taskEntry.Key) -ceq $taskEntry.Value) ('Refusal string only: ' + $taskEntry.Key)
        }
        [void]$taskRequestCodes.Add($taskRequestResult.RequestCode)
    }

    # NEW carrier fixture, independent of both the oracle and candidate arrays.
    $taskCarrierPayload = [byte[]]::new(20177)
    Add-LocalCheck 'ADAPTER-PREP-01' ($taskCarrierPayload.GetType() -eq [byte[]] -and $taskCarrierPayload.Length -eq 20177 -and -not [object]::ReferenceEquals($taskCarrierPayload, $taskOracleBytes)) 'New carrier-owned native fixture, not oracle/private candidate input'
    $taskCarrierZeros = $true
    foreach ($taskByte in $taskCarrierPayload) { if ($taskByte -ne 0) { $taskCarrierZeros = $false; break } }
    Add-LocalCheck 'ADAPTER-PREP-02' $taskCarrierZeros 'Carrier zero-shape precheck'
    $taskCarrierHex = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskCarrierPayload))
    Add-LocalCheck 'ADAPTER-PREP-03' ($taskCarrierHex -ceq $taskOracleHex -and $taskCarrierHex -cne $taskRecordedLiteral) 'Independent preparation relation before DUT use'

    $taskTokens = $null
    $taskParseErrors = $null
    $taskAst = [Management.Automation.Language.Parser]::ParseInput($taskControllerText, [ref]$taskTokens, [ref]$taskParseErrors)
    Add-LocalCheck 'ADAPTER-LOAD-01' ($taskParseErrors.Count -eq 0) 'Complete controller parses without errors'
    $taskDefinitionsOnly = $null -eq $taskAst.ParamBlock -and $null -eq $taskAst.BeginBlock -and $null -eq $taskAst.ProcessBlock -and $taskAst.EndBlock.Statements.Count -eq 10
    foreach ($taskStatement in $taskAst.EndBlock.Statements) { if ($taskStatement -isnot [Management.Automation.Language.FunctionDefinitionAst]) { $taskDefinitionsOnly = $false } }
    Add-LocalCheck 'ADAPTER-LOAD-02' $taskDefinitionsOnly 'Full source has only ten top-level function definitions'
    # Create() defaults to NoLanguage. FullLanguage is explicitly needed for
    # these authorized fixed definitions; an empty command table is NOT an OS
    # sandbox or a restricted-language security boundary.
    $taskInitialState = [Management.Automation.Runspaces.InitialSessionState]::Create()
    $taskInitialState.LanguageMode = [Management.Automation.PSLanguageMode]::FullLanguage
    $taskRunspace = [Management.Automation.Runspaces.RunspaceFactory]::CreateRunspace($taskInitialState)
    $taskRunspace.Open()
    Add-LocalCheck 'ADAPTER-LOAD-03' ($taskRunspace.RunspaceStateInfo.State -eq [Management.Automation.Runspaces.RunspaceState]::Opened) 'Fresh initially empty in-process runspace opened'
    $taskRunspace.SessionStateProxy.SetVariable('ErrorActionPreference', 'Stop')
    $taskPowerShell = [Management.Automation.PowerShell]::Create()
    $taskPowerShell.Runspace = $taskRunspace
    [void]$taskPowerShell.AddScript($taskControllerText, $false)
    $taskControllerLoadAttempts++
    $taskFailureStage = 'CONTROLLER_DEFINITION_LOAD'
    $taskLoadOutput = $taskPowerShell.Invoke()
    Add-LocalCheck 'ADAPTER-LOAD-04' ($taskLoadOutput.Count -eq 0) 'Complete fixed controller definition load returned no success output'
    $taskLoadStreamsEmpty = $taskPowerShell.Streams.Error.Count -eq 0 -and $taskPowerShell.Streams.Warning.Count -eq 0 -and $taskPowerShell.Streams.Verbose.Count -eq 0 -and $taskPowerShell.Streams.Debug.Count -eq 0 -and $taskPowerShell.Streams.Information.Count -eq 0 -and $taskPowerShell.Streams.Progress.Count -eq 0
    Add-LocalCheck 'ADAPTER-LOAD-05' $taskLoadStreamsEmpty 'All six observed controller-load streams empty'
    $taskFailureStage = 'FIXED_COMMAND_BINDING'
    $taskCommand = $taskRunspace.SessionStateProxy.InvokeCommand.GetCommand('Test-DSP004DriverBytesInMemory', [Management.Automation.CommandTypes]::Function)
    Add-LocalCheck 'ADAPTER-BIND-01' ($null -ne $taskCommand -and $taskCommand.Name -ceq 'Test-DSP004DriverBytesInMemory' -and $taskCommand.Parameters.Count -eq 1 -and $taskCommand.Parameters['Payload'].ParameterType -eq [object]) 'Exact fixed function and one object Payload parameter'
    $taskTargetAst = @($taskAst.EndBlock.Statements | Where-Object { $_.Name -ceq 'Test-DSP004DriverBytesInMemory' })
    # FunctionInfo preserves the whole FunctionDefinitionAst, not only Body.
    Add-LocalCheck 'ADAPTER-BIND-02' ($taskTargetAst.Count -eq 1 -and $taskCommand.ScriptBlock.Ast.Extent.Text -ceq $taskTargetAst[0].Extent.Text) 'Loaded whole function definition equals the verified source definition'
    $taskPowerShell.Commands.Clear()
    [void]$taskPowerShell.AddCommand($taskCommand).AddParameter('Payload', $taskCarrierPayload)
    Add-LocalCheck 'ADAPTER-BIND-03' ($taskPowerShell.Commands.Commands.Count -eq 1 -and $taskPowerShell.Commands.Commands[0].Parameters.Count -eq 1) 'One actual command slot and one Payload argument'
    $taskParameter = $taskPowerShell.Commands.Commands[0].Parameters[0]
    Add-LocalCheck 'ADAPTER-BIND-04' ($taskParameter.Name -ceq 'Payload' -and $taskParameter.Value.GetType() -eq [byte[]] -and [object]::ReferenceEquals($taskParameter.Value, $taskCarrierPayload)) 'Preparation-array reference equals actual command-slot value; NOT callee instrumentation'
    $taskArgumentReferenceObserved = $true

    # Exactly one local fixed helper invocation. No candidate dispatch enable.
    $taskDutAttempts++
    $taskFailureStage = 'FIXED_HELPER_INVOCATION_AND_RETURN_CHECKS'
    $taskReturned = $taskPowerShell.Invoke()
    $taskDutReturns++
    Add-LocalCheck 'DUT-RETURN-01' ($taskReturned.Count -eq 1) 'Exactly one captured success-stream object'
    $taskDutStreamsEmpty = $taskPowerShell.Streams.Error.Count -eq 0 -and $taskPowerShell.Streams.Warning.Count -eq 0 -and $taskPowerShell.Streams.Verbose.Count -eq 0 -and $taskPowerShell.Streams.Debug.Count -eq 0 -and $taskPowerShell.Streams.Information.Count -eq 0 -and $taskPowerShell.Streams.Progress.Count -eq 0
    Add-LocalCheck 'DUT-RETURN-02' $taskDutStreamsEmpty 'All six observed helper streams empty'
    $taskExpectedDut = [ordered]@{
        TextCheck = 'FIXED_DRIVER_SHA_MISMATCH'
        Authority = 'NOT ESTABLISHED'
        SourceAdmission = 'NOT ESTABLISHED'
        FrozenHandoff = 'NOT IMPLEMENTED'
        ChildLengthEofShaVerification = 'NOT OBSERVED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
    # PowerShell unwraps PSObject results; inspect their PSObject member view.
    $taskReturnedProperties = @($taskReturned[0].PSObject.Properties)
    Add-LocalCheck 'DUT-RETURN-03' ($taskReturnedProperties.Count -eq 6) 'Exactly six returned metadata properties'
    $taskIndex = 0
    foreach ($taskEntry in $taskExpectedDut.GetEnumerator()) {
        $taskIndex++
        $taskNote = $taskReturned[0].PSObject.Properties[$taskEntry.Key]
        Add-LocalCheck ('DUT-META-{0:D2}' -f $taskIndex) ($taskNote -is [Management.Automation.PSNoteProperty] -and $taskNote.Value -is [string] -and $taskNote.Value -ceq $taskEntry.Value) ('Independent fixed literal comparison: ' + $taskEntry.Key)
        $taskDutMetadata[$taskEntry.Key] = $taskNote.Value
    }
    $taskPostZeros = $true
    foreach ($taskByte in $taskCarrierPayload) { if ($taskByte -ne 0) { $taskPostZeros = $false; break } }
    $taskPostHex = [Convert]::ToHexString([Security.Cryptography.SHA256]::HashData($taskCarrierPayload))
    Add-LocalCheck 'ADAPTER-POST-01' ($taskPostZeros -and $taskCarrierPayload.Length -eq 20177 -and $taskPostHex -ceq $taskCarrierHex) 'Post-call content observation only; not absence of transient mutation'
    Add-LocalCheck 'ADAPTER-POST-02' ([object]::ReferenceEquals($taskParameter.Value, $taskCarrierPayload)) 'Command slot still holds the same carrier reference after normal return'
    Add-LocalCheck 'BOUNDARY-01' ($taskSlotCalls -eq 1 -and $taskRequestCalls -eq 2 -and $taskControllerLoadAttempts -eq 1 -and $taskDutAttempts -eq 1 -and $taskDutReturns -eq 1) 'Exact local invocation counts, no retry/189-item loop'
    $taskRuntimeMetadata = [ordered]@{
        PSVersion = $PSVersionTable.PSVersion.ToString()
        Framework = [Runtime.InteropServices.RuntimeInformation]::FrameworkDescription
        Architecture = [Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture.ToString()
        CryptoAssembly = [Security.Cryptography.SHA256].Assembly.FullName
        PowerShellAssembly = [Management.Automation.PowerShell].Assembly.FullName
        InnerRunspaceLanguageMode = $taskInitialState.LanguageMode.ToString()
        Qualification = 'OBSERVED LOCAL METADATA ONLY; NOT TRUSTED ROOT OR TRANSITIVE DEPENDENCY VERIFICATION'
    }
}
catch {
    [void]$taskRetainedErrors.Add($_.Exception)
    $taskPrimaryFailureType = $_.Exception.GetType().FullName
}
finally {
    # These calls can block/fail. Outer supervision is separate; returned
    # disposal calls do not prove settlement of every engine/descendant resource.
    $taskCleanupObservation = 'LOCAL DISPOSE CALLS RETURNED ONLY; COMPLETE RESOURCE SETTLEMENT NOT ESTABLISHED'
    if ($null -ne $taskPowerShell) {
        try { $taskPowerShell.Dispose() }
        catch { [void]$taskRetainedErrors.Add($_.Exception); [void]$taskCleanupFailureTypes.Add($_.Exception.GetType().FullName) }
    }
    if ($null -ne $taskRunspace) {
        try { $taskRunspace.Dispose() }
        catch { [void]$taskRetainedErrors.Add($_.Exception); [void]$taskCleanupFailureTypes.Add($_.Exception.GetType().FullName) }
    }
    if ($taskCleanupFailureTypes.Count -gt 0) { $taskCleanupObservation = 'LOCAL CLEANUP FAILURE RECORDED; SETTLEMENT NOT ESTABLISHED' }
}

$taskPassed = @($taskChecks | Where-Object { $_.Passed }).Count
$taskFailed = @($taskChecks | Where-Object { -not $_.Passed }).Count
$taskUniqueIds = [Collections.Generic.HashSet[string]]::new([StringComparer]::Ordinal)
foreach ($taskCheck in $taskChecks) { [void]$taskUniqueIds.Add($taskCheck.Id) }
$taskAllPassed = $null -eq $taskPrimaryFailureType -and $taskCleanupFailureTypes.Count -eq 0 -and $taskFailed -eq 0 -and $taskChecks.Count -eq 85 -and $taskUniqueIds.Count -eq 85 -and $taskDutReturns -eq 1
$taskOutput = [pscustomobject][ordered]@{
    Scope = 'LOCAL_SYNTHETIC_SLOT_REFUSAL_AND_SEPARATE_FIXED_HELPER_VALIDATION_ONLY'
    Outcome = if ($taskAllPassed) { 'LOCAL_SYNTHETIC_CHECKS_PASS' } else { 'LOCAL_SYNTHETIC_CHECKS_FAIL' }
    AcceptedSlotSourceSHA256 = $taskSlotSha
    ControllerSourceSHA256 = $taskControllerSha
    CompileCompleted = $taskCompileCompleted
    SlotPreparationCalls = $taskSlotCalls
    SlotRequestCalls = $taskRequestCalls
    SlotRequestCodes = $taskRequestCodes.ToArray()
    ControllerDefinitionLoadAttempts = $taskControllerLoadAttempts
    LocalFixedHelperAttempts = $taskDutAttempts
    LocalFixedHelperNormalReturns = $taskDutReturns
    CheckCount = $taskChecks.Count
    PassedChecks = $taskPassed
    FailedChecks = $taskFailed
    UniqueCheckIds = $taskUniqueIds.Count
    PrimaryFailureType = $taskPrimaryFailureType
    FailureStage = if ($null -eq $taskPrimaryFailureType) { $null } else { $taskFailureStage }
    CleanupFailureTypes = $taskCleanupFailureTypes.ToArray()
    CleanupObservation = $taskCleanupObservation
    FailureRetentionQualification = 'ACTUAL EXCEPTIONS RETAINED LOCALLY; ONLY TYPE METADATA EXPORTED; NO CROSS-PROCESS OBJECT RETENTION CLAIM'
    OracleDigestSHA256 = $taskOracleHex
    AcceptedSlotDigestSHA256 = $taskSlotHex
    NewCarrierDigestSHA256 = $taskCarrierHex
    NewCarrierPostCallDigestSHA256 = $taskPostHex
    RecordedK003LiteralSHA256 = $taskRecordedLiteral
    OracleQualification = 'SEPARATE INPUT AND API PATH; SAME DOTNET CRYPTO STACK; NOT INDEPENDENT CRYPTO IMPLEMENTATION'
    HandoffQualification = if ($taskArgumentReferenceObserved) { 'NEW CARRIER PREPARATION ARRAY EQUALS COMMAND SLOT REFERENCE; CALLEE PARAMETER IDENTITY NOT INSTRUMENTED; EXCLUSIVITY AND FREEZE NOT ESTABLISHED' } else { 'NO QUALIFIED ACTUAL ARGUMENT REFERENCE OBSERVATION' }
    AcceptedSlotQualification = 'NO PRIVATE ARRAY ACCESS OR OUTCOME TRANSFER; ORIGINAL API STILL REFUSES DUT DISPATCH'
    LocalD007Qualification = if ($taskDutReturns -eq 1 -and $taskDutMetadata.Count -eq 6) { 'ONE SYNTHETIC MISMATCH HELPER RETURN OBSERVED; FULL D007 ADMISSION AND ITEM COMPLETION NOT ESTABLISHED' } else { 'NO COMPLETE QUALIFIED SYNTHETIC HELPER RETURN; FULL D007 ADMISSION AND ITEM COMPLETION NOT ESTABLISHED' }
    SlotMetadata = $taskSlotMetadata
    FixedHelperMetadata = $taskDutMetadata
    RuntimeMetadata = $taskRuntimeMetadata
    Checks = $taskChecks.ToArray()
    Uncovered = [string[]]@('POSITIVE_FIXED_SHA_BRANCH', 'CANDIDATE_EQUAL_OR_FAILURE_BRANCHES', 'CONCURRENT_OR_REPEATED_BATCH_RESERVATION', 'CALLEE_REFERENCE_INSTRUMENTATION', 'EXCLUSIVE_IMMUTABLE_FREEZE', 'TRUSTED_HOST_AND_FULL_DEPENDENCY_CLOSURE', 'FAILURE_AND_CLEANUP_COEXISTENCE_INJECTION', 'ADVERSARIAL_TIMEOUT_OUTPUT_OR_RESOURCE_EXHAUSTION', 'COMPLETE_DESCENDANT_SETTLEMENT', 'FULL_189_ITEM_PLAN')
    RealDriverRead = $false
    SourceAdmission = $false
    ActualBusinessCapture = $false
    Integration = $false
    AggregateVerdict = 'NOT ISSUED'
    PreservedLimitations = 'ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskOutput -Depth 8 -Compress
if ($taskAllPassed) { exit 0 } else { exit 1 }
