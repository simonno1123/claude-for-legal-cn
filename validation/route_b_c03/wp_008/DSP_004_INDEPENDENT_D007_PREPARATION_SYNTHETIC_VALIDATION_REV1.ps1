# Authorized local synthetic validation of one fixed candidate only.
# No DUT/controller/189-item plan loading, real material, integration or grants.
# This harness does not establish an OS security boundary or a trusted root.
# A fresh, bounded outer process must separately supervise this script.
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$WarningPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$PSModuleAutoLoadingPreference = 'None'

Import-Module -Name ([System.IO.Path]::Combine($PSHOME, 'Modules', 'Microsoft.PowerShell.Utility', 'Microsoft.PowerShell.Utility.psd1')) -ErrorAction Stop

$taskCandidatePath = [System.IO.Path]::Combine($PSScriptRoot, 'DSP_004_INDEPENDENT_D007_PREPARATION_CANDIDATE_REV1.cs')
$taskCandidateExpectedSha = 'CFCECB173FB5941958649C7135E77B638BAFF41AAA96074971DE53050BA301B5'
$taskRecordedDriverSha = '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210'
$taskChecks = [System.Collections.Generic.List[object]]::new()
$taskCandidateCalls = 0
$taskCompileCompleted = $false
$taskSyntheticDigest = $null
$taskCandidateDigest = $null
$taskCandidateRelation = $null
$taskFailureType = $null
$taskSourceObservedSha = $null
$taskRuntimeMetadata = $null
$taskOracleProvider = $null
$taskCryptoAssembly = $null
$taskCryptoAssemblySha = $null
$taskCandidateMetadata = [ordered]@{}

function Add-LocalCheck {
    param([string]$Id, [bool]$Condition, [string]$Scope)
    [void]$taskChecks.Add([pscustomobject][ordered]@{
        Id = $Id
        Scope = $Scope
        Passed = $Condition
    })
}

try {
    # Verify the exact owned source snapshot that will be decoded and compiled.
    # Do not re-read source text after this snapshot check or alter its content.
    $taskSourceBytes = [System.IO.File]::ReadAllBytes($taskCandidatePath)
    $taskSourceObservedSha = [System.BitConverter]::ToString([System.Security.Cryptography.SHA256]::HashData($taskSourceBytes)).Replace('-', '')
    Add-LocalCheck 'SRC-01' ($taskSourceBytes.Length -eq 7617) 'Fixed candidate source byte length'
    Add-LocalCheck 'SRC-02' ([string]::Equals($taskSourceObservedSha, $taskCandidateExpectedSha, [System.StringComparison]::Ordinal)) 'Exact source snapshot SHA-256'
    if ($taskSourceBytes.Length -ne 7617 -or $taskSourceObservedSha -cne $taskCandidateExpectedSha) {
        throw [System.InvalidOperationException]::new('FIXED_SOURCE_SNAPSHOT_MISMATCH')
    }
    $taskHasBom = $taskSourceBytes.Length -ge 3 -and $taskSourceBytes[0] -eq 239 -and $taskSourceBytes[1] -eq 187 -and $taskSourceBytes[2] -eq 191
    Add-LocalCheck 'SRC-03' (-not $taskHasBom) 'No UTF-8 BOM in the verified snapshot'
    if ($taskHasBom) { throw [System.InvalidOperationException]::new('SOURCE_BOM_REJECTED') }
    $taskSourceText = [System.Text.UTF8Encoding]::new($false, $true).GetString($taskSourceBytes)

    $taskPriorType = [System.Management.Automation.PSTypeName]::new('Dsp004IndependentD007PreparationCandidateRev1').Type
    Add-LocalCheck 'LOAD-01' ($null -eq $taskPriorType) 'No existing candidate type in this fresh child'
    if ($null -ne $taskPriorType) { throw [System.InvalidOperationException]::new('PREEXISTING_CANDIDATE_TYPE_REJECTED') }

    # PowerShell's bundled compiler produces an in-memory assembly. No SDK,
    # restore, package download, binary output or modified candidate is used.
    $taskCompiledTypes = @(Microsoft.PowerShell.Utility\Add-Type -TypeDefinition $taskSourceText -Language CSharp -PassThru -ErrorAction Stop -WarningAction Stop)
    $taskCompileCompleted = $true
    Add-LocalCheck 'LOAD-02' ($taskCompiledTypes.Count -eq 1) 'One compiled public candidate type'
    if ($taskCompiledTypes.Count -ne 1) { throw [System.InvalidOperationException]::new('COMPILED_TYPE_COUNT_MISMATCH') }
    $taskCandidateType = $taskCompiledTypes[0]
    Add-LocalCheck 'LOAD-03' ($taskCandidateType.FullName -ceq 'Dsp004IndependentD007PreparationCandidateRev1') 'Exact compiled type identity'
    if ($taskCandidateType.FullName -cne 'Dsp004IndependentD007PreparationCandidateRev1') {
        throw [System.InvalidOperationException]::new('COMPILED_TYPE_NAME_MISMATCH')
    }
    Add-LocalCheck 'API-01' ($taskCandidateType.IsSealed -and $taskCandidateType.IsPublic) 'Sealed public candidate type'
    Add-LocalCheck 'API-02' ($taskCandidateType.GetConstructors().Count -eq 0) 'No public constructors'
    $taskPublicFlags = [System.Reflection.BindingFlags]::Public -bor [System.Reflection.BindingFlags]::Instance -bor [System.Reflection.BindingFlags]::Static -bor [System.Reflection.BindingFlags]::DeclaredOnly
    Add-LocalCheck 'API-03' ($taskCandidateType.GetFields($taskPublicFlags).Count -eq 0) 'No public raw fields'
    $taskPublicMethods = @($taskCandidateType.GetMethods($taskPublicFlags) | Where-Object { -not $_.IsSpecialName })
    Add-LocalCheck 'API-04' ($taskPublicMethods.Count -eq 1) 'Exactly one public non-accessor method'
    if ($taskPublicMethods.Count -ne 1) { throw [System.InvalidOperationException]::new('PUBLIC_METHOD_COUNT_MISMATCH') }
    $taskPrepareMethod = $taskPublicMethods[0]
    $taskMethodShape = $taskPrepareMethod.Name -ceq 'PrepareD007Only' -and $taskPrepareMethod.IsStatic -and $taskPrepareMethod.GetParameters().Count -eq 0 -and $taskPrepareMethod.ReturnType -eq $taskCandidateType
    Add-LocalCheck 'API-05' $taskMethodShape 'Exact zero-argument preparation method, not a DUT'
    if (-not $taskMethodShape) { throw [System.InvalidOperationException]::new('PREPARATION_METHOD_SHAPE_MISMATCH') }
    $taskPublicProperties = @($taskCandidateType.GetProperties($taskPublicFlags))
    $taskPropertiesSafe = $taskPublicProperties.Count -eq 16
    foreach ($taskProperty in $taskPublicProperties) {
        if ($taskProperty.CanWrite -or $taskProperty.PropertyType -ne [string] -or $taskProperty.GetIndexParameters().Count -ne 0) {
            $taskPropertiesSafe = $false
        }
    }
    Add-LocalCheck 'API-06' $taskPropertiesSafe 'Sixteen read-only, non-indexed string metadata properties'
    if (-not $taskPropertiesSafe) { throw [System.InvalidOperationException]::new('PUBLIC_PROPERTY_SHAPE_MISMATCH') }

    # Independent oracle construction and a different .NET SHA API path.
    # It is NOT an independent provider/library implementation, nor the same
    # byte[] privately created by the candidate, nor any real driver bytes.
    $taskOraclePayload = [byte[]]::new(20177)
    Add-LocalCheck 'ORACLE-01' ($taskOraclePayload.GetType() -eq [byte[]] -and $taskOraclePayload.Length -eq 20177) 'Separate native synthetic oracle input shape'
    $taskOracleZeros = $true
    foreach ($taskByte in $taskOraclePayload) { if ($taskByte -ne 0) { $taskOracleZeros = $false; break } }
    Add-LocalCheck 'ORACLE-02' $taskOracleZeros 'Separate synthetic oracle input is all-zero'
    if (-not $taskOracleZeros) { throw [System.InvalidOperationException]::new('ORACLE_ZERO_SHAPE_MISMATCH') }
    $taskHashOracle = [System.Security.Cryptography.SHA256]::Create()
    try {
        $taskOracleProvider = $taskHashOracle.GetType().FullName
        $taskOracleDigestBytes = $taskHashOracle.ComputeHash($taskOraclePayload)
    }
    finally { $taskHashOracle.Dispose() }
    Add-LocalCheck 'ORACLE-03' ($taskOracleDigestBytes.GetType() -eq [byte[]] -and $taskOracleDigestBytes.Length -eq 32) 'Separate oracle digest native shape'
    $taskSyntheticDigest = [System.BitConverter]::ToString($taskOracleDigestBytes).Replace('-', '')
    Add-LocalCheck 'ORACLE-04' ($taskSyntheticDigest -cmatch '\A[A-F0-9]{64}\z') 'Separate oracle digest full uppercase hex'
    $taskExpectedRelation = if ([string]::Equals($taskSyntheticDigest, $taskRecordedDriverSha, [System.StringComparison]::Ordinal)) { 'EQUAL_TO_RECORDED_LITERAL' } else { 'DIFFERENT_FROM_RECORDED_LITERAL' }

    # One actual call to the preparation candidate only. Do not invoke any DUT,
    # reflect private arrays, mutate retained objects, or construct new routes.
    $taskCandidateCalls++
    $taskObservedResult = $taskPrepareMethod.Invoke($null, [object[]]@())
    Add-LocalCheck 'RUN-01' ($null -ne $taskObservedResult -and $taskObservedResult.GetType() -eq $taskCandidateType) 'Preparation returned the exact candidate result type'
    if ($null -eq $taskObservedResult -or $taskObservedResult.GetType() -ne $taskCandidateType) {
        throw [System.InvalidOperationException]::new('PREPARATION_RETURN_TYPE_MISMATCH')
    }
    $taskCandidateDigest = $taskObservedResult.SyntheticDigestHex
    $taskCandidateRelation = $taskObservedResult.PreparationRelation
    Add-LocalCheck 'RUN-02' ($taskCandidateDigest -is [string] -and $taskCandidateDigest -cmatch '\A[A-F0-9]{64}\z') 'Actual candidate digest string shape'
    Add-LocalCheck 'RUN-03' ([string]::Equals($taskCandidateDigest, $taskSyntheticDigest, [System.StringComparison]::Ordinal)) 'Candidate digest matches independently constructed oracle'
    Add-LocalCheck 'RUN-04' ([string]::Equals($taskCandidateRelation, $taskExpectedRelation, [System.StringComparison]::Ordinal)) 'Relation matches oracle comparison with the recorded literal'
    Add-LocalCheck 'RUN-05' (-not [string]::Equals($taskSyntheticDigest, $taskRecordedDriverSha, [System.StringComparison]::Ordinal)) 'Observed synthetic digest differs from recorded K-003 literal only'

    $taskExpectedMetadata = [ordered]@{
        PreparationRelation = $taskExpectedRelation
        ObservationCode = 'BOUNDED_SYNTHETIC_DIGEST_RELATION_OBSERVED'
        SyntheticDigestHex = $taskSyntheticDigest
        DigestQualification = 'SYNTHETIC BYTE DIGEST ONLY; COMPARED WITH RECORDED LITERAL; NOT REAL SOURCE VERIFICATION'
        PayloadRetentionQualification = 'PRIVATE REFERENCE ONLY; EXCLUSIVE OWNERSHIP, FREEZE AND LIFETIME NOT ESTABLISHED'
        DigestRetentionQualification = 'PRIVATE REFERENCE ONLY; IMPLEMENTATION IDENTITY AND TRUST NOT ESTABLISHED'
        ExceptionRetentionQualification = 'NO PREPARATION EXCEPTION REFERENCE RECORDED'
        Authority = 'NOT ESTABLISHED'
        SourceAdmission = 'NOT ESTABLISHED'
        TrustedHostIdentity = 'UNBOUND'
        HashImplementationIdentity = 'UNBOUND'
        FrozenHandoff = 'NOT IMPLEMENTED'
        SamePayloadDutUse = 'NOT ESTABLISHED'
        DutInvocation = 'NOT PERFORMED BY THIS API'
        D007ExecutionOutcome = 'NOT DETERMINED'
        TimingAndOuterStop = 'NOT ESTABLISHED'
    }
    $taskMetadataIndex = 0
    foreach ($taskEntry in $taskExpectedMetadata.GetEnumerator()) {
        $taskMetadataIndex++
        $taskActual = $taskObservedResult.($taskEntry.Key)
        $taskCandidateMetadata[$taskEntry.Key] = $taskActual
        Add-LocalCheck ('META-{0:D2}' -f $taskMetadataIndex) ($taskActual -is [string] -and [string]::Equals($taskActual, $taskEntry.Value, [System.StringComparison]::Ordinal)) ('Literal metadata only: ' + $taskEntry.Key)
    }

    $taskCryptoAssembly = [System.Security.Cryptography.SHA256].Assembly
    $taskCryptoAssemblySha = [System.BitConverter]::ToString([System.Security.Cryptography.SHA256]::HashData([System.IO.File]::ReadAllBytes($taskCryptoAssembly.Location))).Replace('-', '')
    $taskRuntimeMetadata = [ordered]@{
        PSEdition = $PSVersionTable.PSEdition
        PSVersion = $PSVersionTable.PSVersion.ToString()
        Framework = [System.Runtime.InteropServices.RuntimeInformation]::FrameworkDescription
        Architecture = [System.Runtime.InteropServices.RuntimeInformation]::ProcessArchitecture.ToString()
        CompilerAssembly = (Get-Command -Name 'Microsoft.PowerShell.Utility\Add-Type' -CommandType Cmdlet).ImplementingType.Assembly.FullName
        CryptoAssembly = $taskCryptoAssembly.FullName
        CryptoModuleVersionId = $taskCryptoAssembly.ManifestModule.ModuleVersionId.ToString()
        CryptoAssemblySHA256 = $taskCryptoAssemblySha
        OracleProviderType = $taskOracleProvider
        IdentityQualification = 'OBSERVED LOCAL METADATA ONLY; NOT TRUSTED-ROOT OR TRANSITIVE-DEPENDENCY VERIFICATION'
    }
    Add-LocalCheck 'BOUNDARY-01' ($taskCandidateCalls -eq 1) 'Exactly one preparation-candidate invocation'
}
catch {
    # Do not publish arbitrary exception messages, stack traces or private data.
    $taskFailureType = $_.Exception.GetType().FullName
}

$taskPassedCount = @($taskChecks | Where-Object { $_.Passed }).Count
$taskFailedCount = @($taskChecks | Where-Object { -not $_.Passed }).Count
$taskAllPassed = $taskCompileCompleted -and $taskCandidateCalls -eq 1 -and $null -eq $taskFailureType -and $taskChecks.Count -eq 38 -and $taskFailedCount -eq 0
$taskOutput = [pscustomobject][ordered]@{
    Scope = 'LOCAL_SYNTHETIC_CANDIDATE_VALIDATION_ONLY'
    Outcome = if ($taskAllPassed) { 'LOCAL_SYNTHETIC_CHECKS_PASS' } else { 'LOCAL_SYNTHETIC_CHECKS_FAIL' }
    CandidateSourceSHA256 = $taskSourceObservedSha
    CompileCompleted = $taskCompileCompleted
    CandidateCalls = $taskCandidateCalls
    CheckCount = $taskChecks.Count
    PassedChecks = $taskPassedCount
    FailedChecks = $taskFailedCount
    FailureType = $taskFailureType
    OracleSyntheticDigestSHA256 = $taskSyntheticDigest
    CandidateSyntheticDigestSHA256 = $taskCandidateDigest
    CandidateRelation = $taskCandidateRelation
    RecordedK003LiteralSHA256 = $taskRecordedDriverSha
    OracleIndependenceQualification = 'SEPARATE INPUT AND API PATH; SAME DOTNET CRYPTO STACK; NOT AN INDEPENDENT CRYPTO IMPLEMENTATION OR SAME-PAYLOAD HANDOFF PROOF'
    CandidateMetadata = $taskCandidateMetadata
    RuntimeMetadata = $taskRuntimeMetadata
    Checks = $taskChecks.ToArray()
    Uncovered = [string[]]@('EQUAL_RELATION_BRANCH', 'INPUT_SHAPE_FAILURE_BRANCH', 'DIGEST_SHAPE_FAILURE_BRANCH', 'EXCEPTION_RETENTION_BRANCH', 'FATAL_OR_RESULT_ALLOCATION_FAILURE', 'DUT_POSITIVE_SHA_BRANCH', 'OWNERSHIP_FREEZE_AND_SAME_PAYLOAD_DUT_USE', 'TRUSTED_ROOT_AND_TRANSITIVE_DEPENDENCIES', 'OUTPUT_CLOSURE_AND_ADVERSARIAL_TIMEOUT_STOP')
    DutInvocationsByThisHarness = 0
    Full189ItemPlanInvocationsByThisHarness = 0
    RealDriverReadByThisHarness = $false
    SourceAdmissionByThisHarness = $false
    OwnerAcceptanceByThisHarness = $false
    PreservedLimitations = 'ALL LIMITED PRESERVED; DSP-004 OPEN / HOLD; B-01 AND B-02 OPEN'
}
Microsoft.PowerShell.Utility\ConvertTo-Json -InputObject $taskOutput -Depth 7 -Compress
if ($taskAllPassed) { exit 0 } else { exit 1 }
