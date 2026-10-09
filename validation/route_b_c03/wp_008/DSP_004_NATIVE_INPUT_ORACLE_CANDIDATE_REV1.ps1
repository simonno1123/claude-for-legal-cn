<#
DSP-004 native-input / independent-oracle REV1 CONSTRUCTION SOURCE CANDIDATE.
P1 ONLY. This new candidate neither replaces nor loads the accepted carrier
or outer controller. There is no dispatcher, invocation, enable flag, process,
file access, hash preparer, capture, comparator, output protocol or supervisor.

Historical accepted source and design identities (recorded bindings only):
Carrier: 46AF48E3227BF85CD0612D2FA6D5D92DFFE6F242D0E1785BA9CF1FCBFC34C53C
Controller: 891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB
Input catalog REV2: 4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E
Controlled-load design REV2: 7B7CA6E96D86621790AC37397B600FD19812B955A916390970C188A3CA4D2608
These literal strings do not verify physical assets or grant any authority.

Only a function definition is present at top level. Its future invocation
would construct private typed parameter/oracle data; no DUT function is called.
Loading/invoking even this getter remains unperformed and requires a separately
bound trusted host, early-output closure and private domain. NoProfile is not
trusted-load evidence. Construction syntax has NOT been run to verify types.

M/RQ/D/F/RD/WR: 6/18/7/62/52/44 items, total 189. A/T/K are 8/26/27
independent literal references, not extra cases. Aliases are fully expanded in
parameter/expected values. OriginalTextRow is provenance text, never parsed
or evaluated at runtime. Numeric ASCII literals implement only the finite
F-row transformations specified in the accepted catalog, without a DUT oracle.

Parameters are named values held in a dictionary: arrays must later be passed
as one -object argument with their exact native identity. ParameterOrder is
a binding description, not permission to execute dynamic dispatch.
ExpectedValuePerCall is an independent DATA oracle. ExpectedOutputKind requires
exact actual container/member kind before values are inspected: M case records
are hashtables, M fixed/D/F/RD/WR are PSCustomObject with NoteProperty only,
RQ is Boolean, tuples are String. Dictionary key and property name sets must
match exactly (ordinal), ignoring enumeration order; array order is fixed.
All values require exact native types, ordinal strings and null handling,
including all fixed negative fields. No formatting/JSON/ToString comparison.

M-004/005/006: check the complete FIRST capture against the pristine oracle;
apply ONLY the listed mutations to first DUT capture; then perform a fresh
SECOND call and check its complete capture. Also verify IdentityAssertions.
The independent oracle is never passed to DUT, mutated or filled from returns.
String reference freshness is not required. The capture collection in M-005
belongs to the eventual capturer; this file does not claim the DUT returns
one direct array. This candidate does not execute any mutation or identity test.

Returned plan/reference data are fresh construction proposals, NOT immutable
snapshots or proof of exclusive ownership. A trusted private owner and
read-only oracle discipline remain UNBOUND. No caller-controlled flag is an
admission interface. Caller mutation cannot be accepted as amended expected data.

D-007's conditional expected mismatch is NOT observed. Its zero-array expression
is inert until getter invocation. Independent preparation must check THIS same
private fixture before ANY D-007 DUT call, without using the DUT as a probe.
This candidate has no preparation grant, digest, ownership proof or gate.
D-007 remains UNBOUND / NOT_RUN; driver positive SHA branch remains NOT COVERED.

Private capture (empty output versus explicit null versus null member), safe
member inspection/comparison, source/helper identity, output isolation, atomic
consumption and outside stop are NOT IMPLEMENTED. This plan does not return
MATCH/NOT_MATCH/NOT_RUN/INCOMPLETE observation records. No 189-test PASS is issued.
120/5/5 budgets remain DESIGN PROPOSALS ONLY. All upstream LIMITED remain.
DSP-004 OPEN / HOLD. B-01 OPEN. B-02 OPEN. No source admission, actual capture,
integration, real materials, provider, independent ACOS or other-project action.
#>

function Get-DSP004NativeInputOracleCandidatePlan {
    # Independent literal oracle; NEVER obtained from any controller getter.
    $dspCaseReference = [object[]]@(
        @{ CaseId = 'FULL_ENTRY_LITERAL_RECORDS'; Level = 'FULL_ENTRY_LOCAL_OBSERVATION'; Observation = 'LOCAL_ASSERTIONS_OBSERVED' }
        @{ CaseId = 'FULL_ENTRY_OCCUPIED_SLOT'; Level = 'FULL_ENTRY_PRECONDITION_REFUSAL'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_SYNTHETIC_SHA_REFUSAL'; Level = 'NON_ASSET_PRIVATE_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_OWNED_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'LOCAL_ASSERTIONS_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_MISSING_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_REPLACED_SLOT'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'HELPER_CLEAN_TABLE_IDENTITY'; Level = 'SYNTHETIC_CLEANUP_HELPER_PROBE'; Observation = 'EXPECTED_REFUSAL_OBSERVED' }
        @{ CaseId = 'CARRIER_REFERENCE_CONSTRUCTION'; Level = 'SYNTHETIC_CARRIER_CONSTRUCTION'; Observation = 'CONSTRUCTION_ASSERTIONS_OBSERVED' }
    )
    $dspTupleReference = [string[]]@(
        'FULL_ENTRY_LITERAL_RECORDS|FULL_ENTRY_LOCAL_OBSERVATION|LOCAL_ASSERTIONS_OBSERVED|END_CASE'
        'FULL_ENTRY_LITERAL_RECORDS|FULL_ENTRY_LOCAL_OBSERVATION|NOT_RUN|STOP_BATCH'
        'FULL_ENTRY_LITERAL_RECORDS|FULL_ENTRY_LOCAL_OBSERVATION|INCOMPLETE|STOP_BATCH'
        'FULL_ENTRY_OCCUPIED_SLOT|FULL_ENTRY_PRECONDITION_REFUSAL|EXPECTED_REFUSAL_OBSERVED|END_CASE'
        'FULL_ENTRY_OCCUPIED_SLOT|FULL_ENTRY_PRECONDITION_REFUSAL|NOT_RUN|STOP_BATCH'
        'FULL_ENTRY_OCCUPIED_SLOT|FULL_ENTRY_PRECONDITION_REFUSAL|INCOMPLETE|STOP_BATCH'
        'HELPER_SYNTHETIC_SHA_REFUSAL|NON_ASSET_PRIVATE_HELPER_PROBE|EXPECTED_REFUSAL_OBSERVED|END_CASE'
        'HELPER_SYNTHETIC_SHA_REFUSAL|NON_ASSET_PRIVATE_HELPER_PROBE|NOT_RUN|STOP_BATCH'
        'HELPER_SYNTHETIC_SHA_REFUSAL|NON_ASSET_PRIVATE_HELPER_PROBE|INCOMPLETE|STOP_BATCH'
        'HELPER_CLEAN_OWNED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|LOCAL_ASSERTIONS_OBSERVED|END_CASE'
        'HELPER_CLEAN_OWNED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|NOT_RUN|STOP_BATCH'
        'HELPER_CLEAN_OWNED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|INCOMPLETE|STOP_BATCH'
        'HELPER_CLEAN_MISSING_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|EXPECTED_REFUSAL_OBSERVED|END_CASE'
        'HELPER_CLEAN_MISSING_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|NOT_RUN|STOP_BATCH'
        'HELPER_CLEAN_MISSING_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|INCOMPLETE|STOP_BATCH'
        'HELPER_CLEAN_REPLACED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|EXPECTED_REFUSAL_OBSERVED|END_CASE'
        'HELPER_CLEAN_REPLACED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|NOT_RUN|STOP_BATCH'
        'HELPER_CLEAN_REPLACED_SLOT|SYNTHETIC_CLEANUP_HELPER_PROBE|INCOMPLETE|STOP_BATCH'
        'HELPER_CLEAN_TABLE_IDENTITY|SYNTHETIC_CLEANUP_HELPER_PROBE|EXPECTED_REFUSAL_OBSERVED|END_CASE'
        'HELPER_CLEAN_TABLE_IDENTITY|SYNTHETIC_CLEANUP_HELPER_PROBE|NOT_RUN|STOP_BATCH'
        'HELPER_CLEAN_TABLE_IDENTITY|SYNTHETIC_CLEANUP_HELPER_PROBE|INCOMPLETE|STOP_BATCH'
        'CARRIER_REFERENCE_CONSTRUCTION|SYNTHETIC_CARRIER_CONSTRUCTION|CONSTRUCTION_ASSERTIONS_OBSERVED|END_CASE'
        'CARRIER_REFERENCE_CONSTRUCTION|SYNTHETIC_CARRIER_CONSTRUCTION|NOT_RUN|STOP_BATCH'
        'CARRIER_REFERENCE_CONSTRUCTION|SYNTHETIC_CARRIER_CONSTRUCTION|INCOMPLETE|STOP_BATCH'
        'DRIVER_ALREADY_USED|NO_NEW_OBSERVATION|NOT_RUN|STOP_BATCH'
        'UNBOUND_CASE|NO_OBSERVATION|NOT_RUN|STOP_BATCH'
    )
    $dspFixedReference = [ordered]@{
        CandidateQualification = 'SOURCE CANDIDATE ONLY - NOT EXECUTION READY'
        DriverPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_VALIDATION_DRIVER_REV1.py'
        DriverSha256 = '6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210'
        DriverBodyBytes = [int]20177
        DriverInputCeiling = [int]65536
        DriverTailDetectionBytes = [int]1
        CallerPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_CONTROLLED_BASELINE_HANDOFF_CALLER_CANDIDATE_REV1.py'
        CallerSha256 = 'EF554C3051318BD305EDE6B8511C433C1BB9E20B10E93E5FB5F71C9AFF7A7E63'
        ReaderPath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/DSP_004_EXPECTED_BASELINE_READER_CANDIDATE_REV1.py'
        ReaderSha256 = 'AE1389EDA1C3B9129A0546DA5764C1F68A6B0193A22DA3431CAA89BAB8DC0727'
        BaselinePath = 'C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md'
        BaselineSha256 = 'BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368'
        StdoutBodyBudget = [int]256
        StdoutDetectionBudget = [int]1
        StderrBodyBudget = [int]0
        StderrDetectionBudget = [int]1
        WholeCaseDeadlineSeconds = [int]30
        StopConfirmationMaximumSeconds = [int]5
        FrameMarker = 'DSP004-STATUS-V1'
        CaseContract = $dspCaseReference
        StatusCombinations = $dspTupleReference
        OuterReasons = [string[]]@('START_NOT_PERMITTED', 'START_FAILED', 'INPUT_REJECTED', 'OUTPUT_REJECTED', 'TIMEOUT', 'EXIT_UNCONFIRMED')
        AuthorityChannel = 'UNBOUND - NO ACCEPTANCE OR ENABLE INTERFACE'
        ControllerFullShaBinding = 'EXTERNAL - NOT SELF-COMPUTED AUTHORITY'
        BootstrapTextEncodingAndShaBinding = 'EXTERNAL - UNBOUND'
        LiveAdapters = 'NOT IMPLEMENTED - START REFUSED'
        CaseCompletion = 'NOT ESTABLISHED'
    }
    $dspItems = [object[]]@(
        [pscustomobject]@{
            Id = 'M-001'
            OriginalTextRow = '| M-001 | Get-DSP004CaseContract；无参数；在未来载体捕获其管道结果为有序集合 | 8 个 hashtable；各仅 CaseId、Level、Observation 三键；逐项内容/序列与 A-01 至 A-08 相同，无 Action。按键名而非键枚举顺序比较。 |'
            FunctionName = 'Get-DSP004CaseContract'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'ORDERED_PIPELINE_HASHTABLES'
            ExpectedOutputCountPerCall = [int]8
            ExpectedValuePerCall = $dspCaseReference
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'M-002'
            OriginalTextRow = '| M-002 | Get-DSP004StatusCombinations；无参数；在未来载体捕获其管道结果为有序集合 | 26 个原生 string；序列精确为 T-001 至 T-026 的四字段以单个竖线拼接，集合无重复；不得用本返回值回填 T 表。 |'
            FunctionName = 'Get-DSP004StatusCombinations'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'ORDERED_PIPELINE_STRINGS'
            ExpectedOutputCountPerCall = [int]26
            ExpectedValuePerCall = $dspTupleReference
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'M-003'
            OriginalTextRow = '| M-003 | Get-DSP004FixedContract；无参数 | 一个 PSCustomObject；属性名集合及内容与 K 表相同（K-020、K-021 为集合内容引用）；不要求属性枚举序。 |'
            FunctionName = 'Get-DSP004FixedContract'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $dspFixedReference
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'M-004'
            OriginalTextRow = '| M-004 | Get-DSP004CaseContract 两次新调用；只修改第一返回集合首项 CaseId 为原生 string CALLER_COPY_SENTINEL | 第二次仍精确 M-001；两次首项 hashtable 引用不同。只改调用者持有的副本，不改函数/已接受源/注册表；不要求固定字面量 string 为新引用。 |'
            FunctionName = 'Get-DSP004CaseContract'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'ORDERED_PIPELINE_HASHTABLES'
            ExpectedOutputCountPerCall = [int]8
            ExpectedValuePerCall = $dspCaseReference
            InvocationCount = [int]2
            MutationsBetweenCalls = [object[]]@([ordered]@{ CapturedReturnPath = '[0].CaseId'; Value = 'CALLER_COPY_SENTINEL'; ValueType = 'System.String'; AfterCall = [int]1; BeforeCall = [int]2 })
            IdentityAssertions = [string[]]@('FIRST[0] HASHTABLE IS NOT SECOND[0] HASHTABLE')
            Preconditions = [string[]]@('CHECK BOTH COMPLETE CAPTURES AGAINST PRISTINE ORACLE; MUTATE ONLY FIRST DUT CAPTURE BETWEEN CALLS')
        }
        [pscustomobject]@{
            Id = 'M-005'
            OriginalTextRow = '| M-005 | Get-DSP004StatusCombinations 两次新调用；将第一次未来捕获集合的首槽替换为 CALLER_COPY_SENTINEL | 第二次仍精确 M-002；捕获集合槽位变更不影响以后结果。集合 capture 由载体创建，不宣称函数直接返回同一个/新 array；不要求 string 引用身份。 |'
            FunctionName = 'Get-DSP004StatusCombinations'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'ORDERED_PIPELINE_STRINGS'
            ExpectedOutputCountPerCall = [int]26
            ExpectedValuePerCall = $dspTupleReference
            InvocationCount = [int]2
            MutationsBetweenCalls = [object[]]@([ordered]@{ CapturedReturnPath = '[0]'; Value = 'CALLER_COPY_SENTINEL'; ValueType = 'System.String'; AfterCall = [int]1; BeforeCall = [int]2 })
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@('CHECK BOTH COMPLETE CAPTURES AGAINST PRISTINE ORACLE; MUTATE ONLY FIRST DUT CAPTURE BETWEEN CALLS')
        }
        [pscustomobject]@{
            Id = 'M-006'
            OriginalTextRow = '| M-006 | Get-DSP004FixedContract 两次新调用；只改首次 CandidateQualification 为 CALLER_COPY_SENTINEL、CaseContract[0].CaseId 为该 sentinel、StatusCombinations[0] 为该 sentinel | 第二次仍精确 M-003；PSCustomObject 和可变嵌套集合/hashtable 不共享可变状态（按真实对象及集合持有方式比较）。复制与 fresh 不证明输入冻结或防并发写。 |'
            FunctionName = 'Get-DSP004FixedContract'
            ParameterOrder = [string[]]@()
            Parameters = [ordered]@{

            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $dspFixedReference
            InvocationCount = [int]2
            MutationsBetweenCalls = [object[]]@([ordered]@{ CapturedReturnPath = 'CandidateQualification'; Value = 'CALLER_COPY_SENTINEL'; ValueType = 'System.String'; AfterCall = [int]1; BeforeCall = [int]2 }, [ordered]@{ CapturedReturnPath = 'CaseContract[0].CaseId'; Value = 'CALLER_COPY_SENTINEL'; ValueType = 'System.String'; AfterCall = [int]1; BeforeCall = [int]2 }, [ordered]@{ CapturedReturnPath = 'StatusCombinations[0]'; Value = 'CALLER_COPY_SENTINEL'; ValueType = 'System.String'; AfterCall = [int]1; BeforeCall = [int]2 })
            IdentityAssertions = [string[]]@('FIRST PSCUSTOMOBJECT IS NOT SECOND PSCUSTOMOBJECT', 'FIRST.CaseContract COLLECTION IS NOT SECOND.CaseContract COLLECTION', 'FIRST.StatusCombinations COLLECTION IS NOT SECOND.StatusCombinations COLLECTION', 'FIRST.CaseContract[0] HASHTABLE IS NOT SECOND.CaseContract[0] HASHTABLE', 'FIRST.CaseContract[1] HASHTABLE IS NOT SECOND.CaseContract[1] HASHTABLE', 'FIRST.CaseContract[2] HASHTABLE IS NOT SECOND.CaseContract[2] HASHTABLE', 'FIRST.CaseContract[3] HASHTABLE IS NOT SECOND.CaseContract[3] HASHTABLE', 'FIRST.CaseContract[4] HASHTABLE IS NOT SECOND.CaseContract[4] HASHTABLE', 'FIRST.CaseContract[5] HASHTABLE IS NOT SECOND.CaseContract[5] HASHTABLE', 'FIRST.CaseContract[6] HASHTABLE IS NOT SECOND.CaseContract[6] HASHTABLE', 'FIRST.CaseContract[7] HASHTABLE IS NOT SECOND.CaseContract[7] HASHTABLE')
            Preconditions = [string[]]@('CHECK BOTH COMPLETE CAPTURES AGAINST PRISTINE ORACLE; MUTATE ONLY FIRST DUT CAPTURE BETWEEN CALLS')
        }
        [pscustomobject]@{
            Id = 'RQ-001'
            OriginalTextRow = '| RQ-001 | 原生 string：FULL_ENTRY_LITERAL_RECORDS | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-002'
            OriginalTextRow = '| RQ-002 | 原生 string：FULL_ENTRY_OCCUPIED_SLOT | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'FULL_ENTRY_OCCUPIED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-003'
            OriginalTextRow = '| RQ-003 | 原生 string：HELPER_SYNTHETIC_SHA_REFUSAL | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'HELPER_SYNTHETIC_SHA_REFUSAL'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-004'
            OriginalTextRow = '| RQ-004 | 原生 string：HELPER_CLEAN_OWNED_SLOT | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'HELPER_CLEAN_OWNED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-005'
            OriginalTextRow = '| RQ-005 | 原生 string：HELPER_CLEAN_MISSING_SLOT | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'HELPER_CLEAN_MISSING_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-006'
            OriginalTextRow = '| RQ-006 | 原生 string：HELPER_CLEAN_REPLACED_SLOT | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'HELPER_CLEAN_REPLACED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-007'
            OriginalTextRow = '| RQ-007 | 原生 string：HELPER_CLEAN_TABLE_IDENTITY | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'HELPER_CLEAN_TABLE_IDENTITY'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-008'
            OriginalTextRow = '| RQ-008 | 原生 string：CARRIER_REFERENCE_CONSTRUCTION | true |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $true
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-009'
            OriginalTextRow = '| RQ-009 | 原生 string：full_entry_literal_records | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'full_entry_literal_records'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-010'
            OriginalTextRow = '| RQ-010 | 原生 string：一个 ASCII space 后接 A-01 CaseId | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = ' FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-011'
            OriginalTextRow = '| RQ-011 | 原生 string：A-01 CaseId 后接一个 ASCII space | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'FULL_ENTRY_LITERAL_RECORDS '
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-012'
            OriginalTextRow = '| RQ-012 | 原生 string：空串 | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = ''
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-013'
            OriginalTextRow = '| RQ-013 | 原生 string：UNKNOWN_CASE | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'UNKNOWN_CASE'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-014'
            OriginalTextRow = '| RQ-014 | 原生 string：DRIVER_ALREADY_USED | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = 'DRIVER_ALREADY_USED'
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-015'
            OriginalTextRow = '| RQ-015 | null | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = $null
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-016'
            OriginalTextRow = '| RQ-016 | 原生 bool：false | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = $false
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-017'
            OriginalTextRow = '| RQ-017 | 原生 int：1 | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = [int]1
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RQ-018'
            OriginalTextRow = '| RQ-018 | 普通原生 object[]，一个元素为 A-01 CaseId 的原生 string | false |'
            FunctionName = 'Test-DSP004RequestedCaseText'
            ParameterOrder = [string[]]@('CaseId')
            Parameters = [ordered]@{
                CaseId = [object[]]@('FULL_ENTRY_LITERAL_RECORDS')
            }
            ExpectedOutputKind = 'SINGLE_BOOLEAN'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = $false
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-001'
            OriginalTextRow = '| D-001 | null | NATIVE_BYTES_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = $null
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'NATIVE_BYTES_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-002'
            OriginalTextRow = '| D-002 | 原生 string：空串 | NATIVE_BYTES_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = ''
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'NATIVE_BYTES_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-003'
            OriginalTextRow = '| D-003 | 原生 int[]：一个 int 0（不是 byte[]） | NATIVE_BYTES_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = [int[]]@([int]0)
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'NATIVE_BYTES_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-004'
            OriginalTextRow = '| D-004 | 原生 byte[]：长度 0 | EXACT_DRIVER_LENGTH_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = [byte[]]::new(0)
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'EXACT_DRIVER_LENGTH_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-005'
            OriginalTextRow = '| D-005 | 原生 byte[]：20176 个 byte 0 | EXACT_DRIVER_LENGTH_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = [byte[]]::new(20176)
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'EXACT_DRIVER_LENGTH_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-006'
            OriginalTextRow = '| D-006 | 原生 byte[]：20178 个 byte 0 | EXACT_DRIVER_LENGTH_REQUIRED | 无 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = [byte[]]::new(20178)
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'EXACT_DRIVER_LENGTH_REQUIRED'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'D-007'
            OriginalTextRow = '| D-007 | 原生 byte[]：20177 个 byte 0 | FIXED_DRIVER_SHA_MISMATCH，仅预置条件满足后才可使用此预期 | 未来准备端独立摘要须先确认该合成数据不等于 K 的完整 DriverSha256；不得用受测函数回填。本批次未合成/计算该摘要；该 fixture 前置仍 UNBOUND / NOT_RUN，不虚报已确认。 |'
            FunctionName = 'Test-DSP004DriverBytesInMemory'
            ParameterOrder = [string[]]@('Payload')
            Parameters = [ordered]@{
                Payload = [byte[]]::new(20177)
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FIXED_DRIVER_SHA_MISMATCH'
                Authority = 'NOT ESTABLISHED'
                SourceAdmission = 'NOT ESTABLISHED'
                FrozenHandoff = 'NOT IMPLEMENTED'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@('UNBOUND: SEPARATELY AUTHORIZED INDEPENDENT PREPARER MUST VERIFY NATIVE BYTE ARRAY, LENGTH 20177, ALL ZERO BYTES AND DIGEST MISMATCH AGAINST 6405563F9A39B39F8E63D4330C497A76C99B38F4FE4662B0A6E310F355B69210 ON THIS SAME PRIVATE INPUT BEFORE DUT CALL; FAILURE OR UNKNOWN STOPS BATCH; DO NOT SUBSTITUTE FIXTURE')
        }
        [pscustomobject]@{
            Id = 'F-001'
            OriginalTextRow = '| F-001 | FRAME(T-001) | A-01 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-002'
            OriginalTextRow = '| F-002 | FRAME(T-002) | A-01 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-003'
            OriginalTextRow = '| F-003 | FRAME(T-003) | A-01 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-004'
            OriginalTextRow = '| F-004 | FRAME(T-004) | A-02 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 79, 67, 67, 85, 80, 73, 69, 68, 95, 83, 76, 79, 84, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 80, 82, 69, 67, 79, 78, 68, 73, 84, 73, 79, 78, 95, 82, 69, 70, 85, 83, 65, 76, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_OCCUPIED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-005'
            OriginalTextRow = '| F-005 | FRAME(T-005) | A-02 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 79, 67, 67, 85, 80, 73, 69, 68, 95, 83, 76, 79, 84, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 80, 82, 69, 67, 79, 78, 68, 73, 84, 73, 79, 78, 95, 82, 69, 70, 85, 83, 65, 76, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_OCCUPIED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-006'
            OriginalTextRow = '| F-006 | FRAME(T-006) | A-02 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 79, 67, 67, 85, 80, 73, 69, 68, 95, 83, 76, 79, 84, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 80, 82, 69, 67, 79, 78, 68, 73, 84, 73, 79, 78, 95, 82, 69, 70, 85, 83, 65, 76, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_OCCUPIED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-007'
            OriginalTextRow = '| F-007 | FRAME(T-007) | A-03 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 83, 72, 65, 95, 82, 69, 70, 85, 83, 65, 76, 124, 78, 79, 78, 95, 65, 83, 83, 69, 84, 95, 80, 82, 73, 86, 65, 84, 69, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'HELPER_SYNTHETIC_SHA_REFUSAL'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-008'
            OriginalTextRow = '| F-008 | FRAME(T-008) | A-03 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 83, 72, 65, 95, 82, 69, 70, 85, 83, 65, 76, 124, 78, 79, 78, 95, 65, 83, 83, 69, 84, 95, 80, 82, 73, 86, 65, 84, 69, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_SYNTHETIC_SHA_REFUSAL'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-009'
            OriginalTextRow = '| F-009 | FRAME(T-009) | A-03 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 83, 72, 65, 95, 82, 69, 70, 85, 83, 65, 76, 124, 78, 79, 78, 95, 65, 83, 83, 69, 84, 95, 80, 82, 73, 86, 65, 84, 69, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_SYNTHETIC_SHA_REFUSAL'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-010'
            OriginalTextRow = '| F-010 | FRAME(T-010) | A-04 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 79, 87, 78, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'HELPER_CLEAN_OWNED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-011'
            OriginalTextRow = '| F-011 | FRAME(T-011) | A-04 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 79, 87, 78, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_OWNED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-012'
            OriginalTextRow = '| F-012 | FRAME(T-012) | A-04 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 79, 87, 78, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_OWNED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-013'
            OriginalTextRow = '| F-013 | FRAME(T-013) | A-05 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 77, 73, 83, 83, 73, 78, 71, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'HELPER_CLEAN_MISSING_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-014'
            OriginalTextRow = '| F-014 | FRAME(T-014) | A-05 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 77, 73, 83, 83, 73, 78, 71, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_MISSING_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-015'
            OriginalTextRow = '| F-015 | FRAME(T-015) | A-05 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 77, 73, 83, 83, 73, 78, 71, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_MISSING_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-016'
            OriginalTextRow = '| F-016 | FRAME(T-016) | A-06 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 82, 69, 80, 76, 65, 67, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'HELPER_CLEAN_REPLACED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-017'
            OriginalTextRow = '| F-017 | FRAME(T-017) | A-06 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 82, 69, 80, 76, 65, 67, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_REPLACED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-018'
            OriginalTextRow = '| F-018 | FRAME(T-018) | A-06 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 82, 69, 80, 76, 65, 67, 69, 68, 95, 83, 76, 79, 84, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_REPLACED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-019'
            OriginalTextRow = '| F-019 | FRAME(T-019) | A-07 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 84, 65, 66, 76, 69, 95, 73, 68, 69, 78, 84, 73, 84, 89, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'HELPER_CLEAN_TABLE_IDENTITY'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-020'
            OriginalTextRow = '| F-020 | FRAME(T-020) | A-07 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 84, 65, 66, 76, 69, 95, 73, 68, 69, 78, 84, 73, 84, 89, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_TABLE_IDENTITY'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-021'
            OriginalTextRow = '| F-021 | FRAME(T-021) | A-07 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 72, 69, 76, 80, 69, 82, 95, 67, 76, 69, 65, 78, 95, 84, 65, 66, 76, 69, 95, 73, 68, 69, 78, 84, 73, 84, 89, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 76, 69, 65, 78, 85, 80, 95, 72, 69, 76, 80, 69, 82, 95, 80, 82, 79, 66, 69, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'HELPER_CLEAN_TABLE_IDENTITY'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-022'
            OriginalTextRow = '| F-022 | FRAME(T-022) | A-08 | F-ALLOW | END_CASE | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 67, 65, 82, 82, 73, 69, 82, 95, 82, 69, 70, 69, 82, 69, 78, 67, 69, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 65, 82, 82, 73, 69, 82, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'END_CASE'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-023'
            OriginalTextRow = '| F-023 | FRAME(T-023) | A-08 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 67, 65, 82, 82, 73, 69, 82, 95, 82, 69, 70, 69, 82, 69, 78, 67, 69, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 65, 82, 82, 73, 69, 82, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-024'
            OriginalTextRow = '| F-024 | FRAME(T-024) | A-08 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 67, 65, 82, 82, 73, 69, 82, 95, 82, 69, 70, 69, 82, 69, 78, 67, 69, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 83, 89, 78, 84, 72, 69, 84, 73, 67, 95, 67, 65, 82, 82, 73, 69, 82, 95, 67, 79, 78, 83, 84, 82, 85, 67, 84, 73, 79, 78, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-025'
            OriginalTextRow = '| F-025 | FRAME(T-025) | A-01 | F-ALLOW | STOP_BATCH | true |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 68, 82, 73, 86, 69, 82, 95, 65, 76, 82, 69, 65, 68, 89, 95, 85, 83, 69, 68, 124, 78, 79, 95, 78, 69, 87, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $true
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-026'
            OriginalTextRow = '| F-026 | FRAME(T-026) | A-01 | F-ALLOW | STOP_BATCH | true |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 85, 78, 66, 79, 85, 78, 68, 95, 67, 65, 83, 69, 124, 78, 79, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $true
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-027'
            OriginalTextRow = '| F-027 | FRAME(T-002)，仅把 Observation NOT_RUN 改为 INCOMPLETE（字节即 FRAME(T-003)） | A-01 | F-ALLOW | STOP_BATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 73, 78, 67, 79, 77, 80, 76, 69, 84, 69, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-028'
            OriginalTextRow = '| F-028 | FRAME(T-025) | A-08 | F-ALLOW | STOP_BATCH | true |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 68, 82, 73, 86, 69, 82, 95, 65, 76, 82, 69, 65, 68, 89, 95, 85, 83, 69, 68, 124, 78, 79, 95, 78, 69, 87, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $true
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-029'
            OriginalTextRow = '| F-029 | FRAME(T-026) | A-08 | F-ALLOW | STOP_BATCH | true |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 85, 78, 66, 79, 85, 78, 68, 95, 67, 65, 83, 69, 124, 78, 79, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'CARRIER_REFERENCE_CONSTRUCTION'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'ALLOWLISTED_FRAME_TEXT_ONLY'
                RecordedAction = 'STOP_BATCH'
                ProtectionRecord = $true
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-030'
            OriginalTextRow = '| F-030 | FRAME(T-001) | A-02 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_OCCUPIED_SLOT'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-031'
            OriginalTextRow = '| F-031 | FRAME(T-001) | 原生 string DRIVER_ALREADY_USED | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'DRIVER_ALREADY_USED'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-032'
            OriginalTextRow = '| F-032 | FRAME(T-025) | 原生 string UNBOUND_CASE | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 68, 82, 73, 86, 69, 82, 95, 65, 76, 82, 69, 65, 68, 89, 95, 85, 83, 69, 68, 124, 78, 79, 95, 78, 69, 87, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'UNBOUND_CASE'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-033'
            OriginalTextRow = '| F-033 | FRAME(T-025) | null | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 68, 82, 73, 86, 69, 82, 95, 65, 76, 82, 69, 65, 68, 89, 95, 85, 83, 69, 68, 124, 78, 79, 95, 78, 69, 87, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = $null
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-034'
            OriginalTextRow = '| F-034 | FRAME(T-001) | 原生 int 1 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = [int]1
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-035'
            OriginalTextRow = '| F-035 | 原生 string：T-001 对应完整帧文本含末尾 LF（不是 byte[]） | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = ('DSP004-STATUS-V1|FULL_ENTRY_LITERAL_RECORDS|FULL_ENTRY_LOCAL_OBSERVATION|LOCAL_ASSERTIONS_OBSERVED|END_CASE' + [char]10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-036'
            OriginalTextRow = '| F-036 | null | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = $null
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-037'
            OriginalTextRow = '| F-037 | 原生 object[]，仅一个元素为原生 int 10（不是 byte[]） | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [object[]]@([int]10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-038'
            OriginalTextRow = '| F-038 | 原生 byte[]：长度 0 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]::new(0)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-039'
            OriginalTextRow = '| F-039 | 原生 byte[]：256 个 ASCII A（byte65）再一个 LF（byte10），共257 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-040'
            OriginalTextRow = '| F-040 | 原生 byte[]：仅 LF（byte10），长度1 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-041'
            OriginalTextRow = '| F-041 | FRAME(T-001) 删去末尾唯一 LF | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-042'
            OriginalTextRow = '| F-042 | FRAME(T-001) 末尾 LF 替换成 CR、LF（byte13、10） | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 13, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-043'
            OriginalTextRow = '| F-043 | FRAME(T-001) 前置 UTF-8 BOM 三字节239、187、191 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(239, 187, 191, 68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-044'
            OriginalTextRow = '| F-044 | FRAME(T-001) 首 byte68 改为 byte128 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(128, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-045'
            OriginalTextRow = '| F-045 | FRAME(T-001) 首 byte68 改为 byte0 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(0, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-046'
            OriginalTextRow = '| F-046 | FRAME(T-001) 首 byte68 改为 ASCII space byte32 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(32, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-047'
            OriginalTextRow = '| F-047 | FRAME(T-001) 首 byte68 改为 tab byte9 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(9, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-048'
            OriginalTextRow = '| F-048 | FRAME(T-001) 与 FRAME(T-001) 顺序拼接，无其他字节 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10, 68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-049'
            OriginalTextRow = '| F-049 | FRAME(T-001) 后追加 ASCII X byte88 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10, 88)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-050'
            OriginalTextRow = '| F-050 | FRAME(T-001) 在末尾 LF 前插入 ASCII X byte88 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 88, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-051'
            OriginalTextRow = '| F-051 | FRAME(T-001) 在首 byte 后插入 LF byte10 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 10, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-052'
            OriginalTextRow = '| F-052 | FRAME(T-001) marker 中 DSP004 改为 dsp004，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(100, 115, 112, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-053'
            OriginalTextRow = '| F-053 | FRAME(T-001) CaseId 改为 full_entry_literal_records，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 102, 117, 108, 108, 95, 101, 110, 116, 114, 121, 95, 108, 105, 116, 101, 114, 97, 108, 95, 114, 101, 99, 111, 114, 100, 115, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-054'
            OriginalTextRow = '| F-054 | FRAME(T-001) Level 改为 FULL_ENTRY_PRECONDITION_REFUSAL，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 80, 82, 69, 67, 79, 78, 68, 73, 84, 73, 79, 78, 95, 82, 69, 70, 85, 83, 65, 76, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-055'
            OriginalTextRow = '| F-055 | FRAME(T-001) Observation 改为 EXPECTED_REFUSAL_OBSERVED，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 69, 88, 80, 69, 67, 84, 69, 68, 95, 82, 69, 70, 85, 83, 65, 76, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-056'
            OriginalTextRow = '| F-056 | FRAME(T-001) Action END_CASE 改为 STOP_BATCH，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 83, 84, 79, 80, 95, 66, 65, 84, 67, 72, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-057'
            OriginalTextRow = '| F-057 | FRAME(T-002) Action STOP_BATCH 改为 END_CASE，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 78, 79, 84, 95, 82, 85, 78, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-058'
            OriginalTextRow = '| F-058 | FRAME(T-001) 删除 Level 及紧随 Level 的分隔符，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-059'
            OriginalTextRow = '| F-059 | FRAME(T-001) 在末尾 LF 前追加竖线及 EXTRA | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 124, 69, 88, 84, 82, 65, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-060'
            OriginalTextRow = '| F-060 | FRAME(T-001) 在 marker 后的单个竖线处增加一个竖线 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-061'
            OriginalTextRow = '| F-061 | FRAME(T-001) Action 改为 end_case，其余不变 | A-01 | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 101, 110, 100, 95, 99, 97, 115, 101, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS'
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'F-062'
            OriginalTextRow = '| F-062 | FRAME(T-001) | 原生 string：A-01 CaseId 后接一个 ASCII space | F-REJECT | NO_MATCH | false |'
            FunctionName = 'Test-DSP004FrameBytesInMemory'
            ParameterOrder = [string[]]@('Payload', 'RequestedCase')
            Parameters = [ordered]@{
                Payload = [byte[]]@(68, 83, 80, 48, 48, 52, 45, 83, 84, 65, 84, 85, 83, 45, 86, 49, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 73, 84, 69, 82, 65, 76, 95, 82, 69, 67, 79, 82, 68, 83, 124, 70, 85, 76, 76, 95, 69, 78, 84, 82, 89, 95, 76, 79, 67, 65, 76, 95, 79, 66, 83, 69, 82, 86, 65, 84, 73, 79, 78, 124, 76, 79, 67, 65, 76, 95, 65, 83, 83, 69, 82, 84, 73, 79, 78, 83, 95, 79, 66, 83, 69, 82, 86, 69, 68, 124, 69, 78, 68, 95, 67, 65, 83, 69, 10)
                RequestedCase = 'FULL_ENTRY_LITERAL_RECORDS '
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                TextCheck = 'FRAME_REJECTED'
                RecordedAction = 'NO_MATCH'
                ProtectionRecord = $false
                Qualification = 'IN-MEMORY TEXT CHECK ONLY - NOT AUTHENTICATED'
                PeerEof = 'NOT OBSERVED'
                TaskSettlement = 'NOT OBSERVED'
                ProcessExit = 'NOT OBSERVED'
                Deadline = 'NOT OBSERVED'
                Authority = 'NOT ESTABLISHED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-001'
            OriginalTextRow = '| RD-001 | STDOUT | 0 | 1 | S-N | 1 | false | false | R-BODY | 1 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_BODY_BYTES_ONLY - SHORT_READ_IS_NOT_EOF'
                ReportedBodyBytesAfter = [int]1
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-002'
            OriginalTextRow = '| RD-002 | STDOUT | 0 | 4 | S-N | 2 | false | false | R-BODY | 2 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]4
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]2
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_BODY_BYTES_ONLY - SHORT_READ_IS_NOT_EOF'
                ReportedBodyBytesAfter = [int]2
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-003'
            OriginalTextRow = '| RD-003 | STDOUT | 255 | 1 | S-N | 1 | false | false | R-BODY | 256 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]255
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_BODY_BYTES_ONLY - SHORT_READ_IS_NOT_EOF'
                ReportedBodyBytesAfter = [int]256
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-004'
            OriginalTextRow = '| RD-004 | STDOUT | 256 | 1 | S-N | 0 | false | false | R-ZERO | 256 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]256
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_POSITIVE_NORMAL_READ_ZERO_ONLY'
                ReportedBodyBytesAfter = [int]256
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-005'
            OriginalTextRow = '| RD-005 | STDOUT | 0 | 1 | S-N | 0 | false | false | R-ZERO | 0 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_POSITIVE_NORMAL_READ_ZERO_ONLY'
                ReportedBodyBytesAfter = [int]0
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-006'
            OriginalTextRow = '| RD-006 | STDERR | 0 | 1 | S-N | 0 | false | false | R-ZERO | 0 | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDERR'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_POSITIVE_NORMAL_READ_ZERO_ONLY'
                ReportedBodyBytesAfter = [int]0
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-007'
            OriginalTextRow = '| RD-007 | STDOUT | 256 | 1 | S-N | 1 | false | false | R-DETECT | null | R-PRESENT |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]256
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-008'
            OriginalTextRow = '| RD-008 | STDOUT | 255 | 2 | S-N | 2 | false | false | R-DETECT | null | R-PRESENT |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]255
                RequestedCount = [int]2
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]2
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-009'
            OriginalTextRow = '| RD-009 | STDOUT | 0 | 257 | S-N | 257 | false | false | R-DETECT | null | R-PRESENT |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]257
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]257
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-010'
            OriginalTextRow = '| RD-010 | STDERR | 0 | 1 | S-N | 1 | false | false | R-DETECT | null | R-PRESENT |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDERR'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_DETECTION_BYTE - REJECT_OUTPUT'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'PRESENT - NEVER PUBLISH OR CONTINUE DRAINING'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-011'
            OriginalTextRow = '| RD-011 | STDOUT | 0 | 1 | S-P | -1 | false | false | R-PENDING | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'PENDING'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'ORIGINAL_READ_PENDING - NO EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-012'
            OriginalTextRow = '| RD-012 | STDOUT | 0 | 1 | S-F | -1 | false | false | R-FAIL | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'FAULTED'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_READ_FAILURE - NO EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-013'
            OriginalTextRow = '| RD-013 | STDOUT | 0 | 1 | S-C | -1 | false | false | R-FAIL | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'CANCELED'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_READ_FAILURE - NO EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-014'
            OriginalTextRow = '| RD-014 | STDOUT | 0 | 1 | S-S | -1 | false | false | R-FAIL | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'SYNCHRONOUS_FAILURE'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_READ_FAILURE - NO EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-015'
            OriginalTextRow = '| RD-015 | STDOUT | 0 | 1 | S-N | 0 | true | false | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $true
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-016'
            OriginalTextRow = '| RD-016 | STDOUT | 0 | 1 | S-N | 1 | false | true | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-017'
            OriginalTextRow = '| RD-017 | STDOUT | 0 | 1 | S-N | 1 | true | true | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $true
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-018'
            OriginalTextRow = '| RD-018 | STDOUT | 0 | 1 | S-P | -1 | false | true | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'PENDING'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-019'
            OriginalTextRow = '| RD-019 | STDOUT | 0 | 1 | S-F | -1 | true | false | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'FAULTED'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $true
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-020'
            OriginalTextRow = '| RD-020 | STDOUT | 256 | 1 | S-N | 1 | false | true | R-STOP | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]256
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_OR_LOCAL_CLOSE - NO NORMAL_EOF_INFERENCE'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-021'
            OriginalTextRow = '| RD-021 | stdout | 0 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'stdout'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-022'
            OriginalTextRow = '| RD-022 | OTHER | 0 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'OTHER'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-023'
            OriginalTextRow = '| RD-023 | null | 0 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = $null
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-024'
            OriginalTextRow = '| RD-024 | STDOUT | -1 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]-1
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-025'
            OriginalTextRow = '| RD-025 | STDOUT | 257 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]257
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-026'
            OriginalTextRow = '| RD-026 | STDERR | 1 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDERR'
                BodyBytesBefore = [int]1
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-027'
            OriginalTextRow = '| RD-027 | STDOUT | 0 | 0 | S-N | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]0
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-028'
            OriginalTextRow = '| RD-028 | STDOUT | 0 | -1 | S-N | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]-1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-029'
            OriginalTextRow = '| RD-029 | STDOUT | 256 | 2 | S-N | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]256
                RequestedCount = [int]2
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-030'
            OriginalTextRow = '| RD-030 | STDERR | 0 | 2 | S-N | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDERR'
                BodyBytesBefore = [int]0
                RequestedCount = [int]2
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-031'
            OriginalTextRow = '| RD-031 | STDOUT | 0 | 258 | S-N | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]258
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-032'
            OriginalTextRow = '| RD-032 | STDOUT | 0 | 1 | UNKNOWN | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'UNKNOWN'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-033'
            OriginalTextRow = '| RD-033 | STDOUT | 0 | 1 | ran_to_completion | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'ran_to_completion'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-034'
            OriginalTextRow = '| RD-034 | STDOUT | 0 | 1 | S-N | -1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]-1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-035'
            OriginalTextRow = '| RD-035 | STDOUT | 0 | 1 | S-N | 2 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]2
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-036'
            OriginalTextRow = '| RD-036 | STDOUT | 0 | 1 | S-P | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'PENDING'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-037'
            OriginalTextRow = '| RD-037 | STDOUT | 0 | 1 | S-F | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'FAULTED'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-038'
            OriginalTextRow = '| RD-038 | STDOUT | 0 | 1 | S-C | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'CANCELED'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-039'
            OriginalTextRow = '| RD-039 | STDOUT | 0 | 1 | S-S | 0 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'SYNCHRONOUS_FAILURE'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-040'
            OriginalTextRow = '| RD-040 | STDOUT | string:0 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = '0'
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-041'
            OriginalTextRow = '| RD-041 | STDOUT | 0 | string:1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = '1'
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-042'
            OriginalTextRow = '| RD-042 | STDOUT | 0 | 1 | S-N | string:1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = '1'
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-043'
            OriginalTextRow = '| RD-043 | STDOUT | 0 | 1 | null | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = $null
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-044'
            OriginalTextRow = '| RD-044 | STDOUT | 0 | 1 | S-N | 1 | int:0 | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = [int]0
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-045'
            OriginalTextRow = '| RD-045 | STDOUT | 0 | 1 | S-N | 1 | false | int:0 | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = [int]0
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-046'
            OriginalTextRow = '| RD-046 | int:0 | 0 | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = [int]0
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-047'
            OriginalTextRow = '| RD-047 | STDOUT | null | 1 | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = $null
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-048'
            OriginalTextRow = '| RD-048 | STDOUT | 0 | null | S-N | 1 | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = $null
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-049'
            OriginalTextRow = '| RD-049 | STDOUT | 0 | 1 | S-N | null | false | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = $null
                ReadEndLocallyClosed = $false
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-050'
            OriginalTextRow = '| RD-050 | STDOUT | 0 | 0 | S-N | 0 | false | true | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]0
                OriginalTaskState = 'RAN_TO_COMPLETION'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $false
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-051'
            OriginalTextRow = '| RD-051 | STDOUT | 0 | 1 | UNKNOWN | 1 | true | false | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'UNKNOWN'
                ReturnedCount = [int]1
                ReadEndLocallyClosed = $true
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'RD-052'
            OriginalTextRow = '| RD-052 | STDOUT | 0 | 1 | S-F | 0 | true | true | R-INVALID | null | R-NOTCLASS |'
            FunctionName = 'Get-DSP004ReadObservationClassification'
            ParameterOrder = [string[]]@('Channel', 'BodyBytesBefore', 'RequestedCount', 'OriginalTaskState', 'ReturnedCount', 'ReadEndLocallyClosed', 'StopLatched')
            Parameters = [ordered]@{
                Channel = 'STDOUT'
                BodyBytesBefore = [int]0
                RequestedCount = [int]1
                OriginalTaskState = 'FAULTED'
                ReturnedCount = [int]0
                ReadEndLocallyClosed = $true
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_READ_RECORD'
                ReportedBodyBytesAfter = $null
                DetectionByte = 'NOT CLASSIFIED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ActualPeerEof = 'NOT OBSERVED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-001'
            OriginalTextRow = '| WR-001 | 0 | 20177 | S-N | ENDED | false | W-NORMAL | W-NOCOUNT |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_FULL_RANGE_TASK_NORMAL_ONLY'
                ActualPartialProgress = 'NO BYTE COUNT - CHILD RECEIPT REMAINS UNVERIFIED'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-002'
            OriginalTextRow = '| WR-002 | 0 | 20177 | S-N | PENDING | false | W-NORMAL | W-NOCOUNT |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'PENDING'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_FULL_RANGE_TASK_NORMAL_ONLY'
                ActualPartialProgress = 'NO BYTE COUNT - CHILD RECEIPT REMAINS UNVERIFIED'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-003'
            OriginalTextRow = '| WR-003 | 0 | 20177 | S-P | ENDED | false | W-PENDING | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'PENDING'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'ORIGINAL_WRITE_PENDING - NO NORMAL_INPUT_CLOSE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-004'
            OriginalTextRow = '| WR-004 | 0 | 20177 | S-P | PENDING | false | W-PENDING | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'PENDING'
                WaitState = 'PENDING'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'ORIGINAL_WRITE_PENDING - NO NORMAL_INPUT_CLOSE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-005'
            OriginalTextRow = '| WR-005 | 0 | 20177 | S-F | ENDED | false | W-FAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'FAULTED'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-006'
            OriginalTextRow = '| WR-006 | 0 | 20177 | S-C | ENDED | false | W-FAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'CANCELED'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-007'
            OriginalTextRow = '| WR-007 | 0 | 20177 | S-S | ENDED | false | W-FAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'SYNCHRONOUS_FAILURE'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-008'
            OriginalTextRow = '| WR-008 | 0 | 20177 | S-N | TIMED_OUT | false | W-WAITFAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'TIMED_OUT'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-009'
            OriginalTextRow = '| WR-009 | 0 | 20177 | S-N | CANCELED | false | W-WAITFAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'CANCELED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-010'
            OriginalTextRow = '| WR-010 | 0 | 20177 | S-N | FAULTED | false | W-WAITFAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'FAULTED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-011'
            OriginalTextRow = '| WR-011 | 0 | 20177 | S-P | TIMED_OUT | false | W-WAITFAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'PENDING'
                WaitState = 'TIMED_OUT'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-012'
            OriginalTextRow = '| WR-012 | 0 | 20177 | S-F | TIMED_OUT | false | W-WAITFAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'FAULTED'
                WaitState = 'TIMED_OUT'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'WAIT_FAILED - ORIGINAL_TASK_SETTLEMENT_SEPARATE'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-013'
            OriginalTextRow = '| WR-013 | 0 | 20177 | S-S | PENDING | false | W-FAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'SYNCHRONOUS_FAILURE'
                WaitState = 'PENDING'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-014'
            OriginalTextRow = '| WR-014 | 0 | 20177 | S-N | ENDED | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-015'
            OriginalTextRow = '| WR-015 | 0 | 20177 | S-N | TIMED_OUT | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'TIMED_OUT'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-016'
            OriginalTextRow = '| WR-016 | 0 | 20177 | S-P | ENDED | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'PENDING'
                WaitState = 'ENDED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-017'
            OriginalTextRow = '| WR-017 | 0 | 20177 | S-F | CANCELED | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'FAULTED'
                WaitState = 'CANCELED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-018'
            OriginalTextRow = '| WR-018 | 0 | 20177 | S-S | FAULTED | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'SYNCHRONOUS_FAILURE'
                WaitState = 'FAULTED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-019'
            OriginalTextRow = '| WR-019 | 0 | 20177 | S-N | CANCELED | true | W-STOP | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'CANCELED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'STOP_LATCHED - LATE_COMPLETION_CANNOT_RESTORE_RESULT'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-020'
            OriginalTextRow = '| WR-020 | 0 | 20177 | S-C | PENDING | false | W-FAIL | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'CANCELED'
                WaitState = 'PENDING'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'REPORTED_WRITE_FAILURE - PARTIAL_PROGRESS_UNKNOWN'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-021'
            OriginalTextRow = '| WR-021 | 1 | 20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]1
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-022'
            OriginalTextRow = '| WR-022 | -1 | 20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]-1
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-023'
            OriginalTextRow = '| WR-023 | 0 | 0 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]0
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-024'
            OriginalTextRow = '| WR-024 | 0 | 20176 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20176
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-025'
            OriginalTextRow = '| WR-025 | 0 | 20178 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20178
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-026'
            OriginalTextRow = '| WR-026 | string:0 | 20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = '0'
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-027'
            OriginalTextRow = '| WR-027 | 0 | string:20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = '20177'
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-028'
            OriginalTextRow = '| WR-028 | 0 | 20177 | UNKNOWN | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'UNKNOWN'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-029'
            OriginalTextRow = '| WR-029 | 0 | 20177 | ran_to_completion | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'ran_to_completion'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-030'
            OriginalTextRow = '| WR-030 | 0 | 20177 | null | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = $null
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-031'
            OriginalTextRow = '| WR-031 | 0 | 20177 | S-N | UNKNOWN | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'UNKNOWN'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-032'
            OriginalTextRow = '| WR-032 | 0 | 20177 | S-N | ended | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ended'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-033'
            OriginalTextRow = '| WR-033 | 0 | 20177 | S-N | null | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = $null
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-034'
            OriginalTextRow = '| WR-034 | 0 | 20177 | S-N | ENDED | int:0 | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = [int]0
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-035'
            OriginalTextRow = '| WR-035 | 1 | 20177 | S-N | ENDED | true | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]1
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-036'
            OriginalTextRow = '| WR-036 | 0 | 20176 | S-N | TIMED_OUT | true | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20176
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'TIMED_OUT'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-037'
            OriginalTextRow = '| WR-037 | 0 | 20177 | UNKNOWN | FAULTED | true | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'UNKNOWN'
                WaitState = 'FAULTED'
                StopLatched = $true
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-038'
            OriginalTextRow = '| WR-038 | 0 | 20177 | S-N | ENDED | null | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $null
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-039'
            OriginalTextRow = '| WR-039 | null | 20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = $null
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-040'
            OriginalTextRow = '| WR-040 | 0 | null | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = $null
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-041'
            OriginalTextRow = '| WR-041 | 0 | 20177 | int:0 | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = [int]0
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-042'
            OriginalTextRow = '| WR-042 | 0 | 20177 | S-N | int:0 | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = [int]0
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-043'
            OriginalTextRow = '| WR-043 | 0 | int64:20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [int]0
                RequestedCount = [long]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
        [pscustomobject]@{
            Id = 'WR-044'
            OriginalTextRow = '| WR-044 | int64:0 | 20177 | S-N | ENDED | false | W-INVALID | W-UNKNOWN |'
            FunctionName = 'Get-DSP004WriteObservationClassification'
            ParameterOrder = [string[]]@('RequestedOffset', 'RequestedCount', 'OriginalTaskState', 'WaitState', 'StopLatched')
            Parameters = [ordered]@{
                RequestedOffset = [long]0
                RequestedCount = [int]20177
                OriginalTaskState = 'RAN_TO_COMPLETION'
                WaitState = 'ENDED'
                StopLatched = $false
            }
            ExpectedOutputKind = 'SINGLE_PSCUSTOMOBJECT'
            ExpectedOutputCountPerCall = [int]1
            ExpectedValuePerCall = [ordered]@{
                Classification = 'INVALID_REPORTED_WRITE_RECORD'
                ActualPartialProgress = 'UNKNOWN'
                WriteByteCount = 'NOT RETURNED BY INTERFACE'
                ChildLengthEofShaVerification = 'NOT OBSERVED'
                InputClose = 'NOT PERFORMED'
                AutomaticResend = 'PROHIBITED'
                Qualification = 'REPORTED OBSERVATIONS ONLY - NOT INDEPENDENTLY VERIFIED'
                ResourceOwnership = 'NOT IMPLEMENTED'
                CaseCompletion = 'NOT ESTABLISHED'
            }
            InvocationCount = [int]1
            MutationsBetweenCalls = [object[]]@()
            IdentityAssertions = [string[]]@()
            Preconditions = [string[]]@()
        }
    )
    # One container prevents the plan's item/parameter arrays being emitted
    # as pipeline items here. This is NOT a solution to DUT capture semantics.
    [pscustomobject]@{
        Qualification = 'CONSTRUCTION SOURCE CANDIDATE ONLY - NOT EXECUTION READY'
        ControllerSha256 = '891311B08078692C7D012EC5A3C80AFEC255A2B4E6E55BC9AD001B67CC6B47FB'
        CatalogSha256 = '4BAED6E284C92A2403117C72CFBF419BD2B6FB478A55697CA2229201C8FB149E'
        Items = $dspItems
        CaseReference = $dspCaseReference
        TupleReference = $dspTupleReference
        FixedReference = $dspFixedReference
        CaptureComparison = 'UNBOUND - NOT IMPLEMENTED'
        TrustedLoad = 'UNBOUND - NOT IMPLEMENTED'
        D007Preparation = 'UNBOUND - NOT PERFORMED'
        OutsideStop = 'UNBOUND - NOT IMPLEMENTED'
    }
}
