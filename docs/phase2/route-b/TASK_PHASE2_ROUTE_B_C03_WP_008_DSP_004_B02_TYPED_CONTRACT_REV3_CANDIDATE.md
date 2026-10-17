# DSP-004 B-02 类型合同候选 — Combined REV3

## 0. 身份、形成依据与效力

| 项目 | 候选记录 |
| --- | --- |
| 所属项目 | claude-for-legal-cn / Phase 2 Route B C03 WP-008 / DSP-004 |
| 文档性质 | DOCUMENT-ONLY TYPED CONTRACT CANDIDATE |
| 设计来源 | 会话中的 B-02 合同草案 REV2 全文，加组合 REV3 的 A—F 六项定点修订 |
| 会话定位 | REV2：writing 87426；REV3 附录：writing 90376；这些是会话定位，不是文件 SHA |
| Owner 决定范围 | 有限采纳组合 REV3，仅限设计文本；允许新增本类型合同候选及数组政策登记候选并完成独立静态复核 |
| 物理候选效力 | 新增候选文件；物化不等于该文件已完成固定 SHA 接受 |
| 复核记录 | 后续静态复核结论在会话中另行报告；本形成记录不预填复核 PASS |
| 来源准入 / Manifest / 执行 | NOT AUTHORIZED BY THIS MATERIALIZATION |
| 当前保留边界 | DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 与历史记录保留 |

本候选完整展开组合 REV3 的 Manifest 类型合同，不要求读者猜测被省略的
REV2 成员。原 REV2、原复核记录及 REV3 附录仍保留，未被重写。
本文件不是 JSON Schema、编码器、可装载模块、实际 Manifest 或正式来源登记。
它不绑定、准入或实际读取文内未来合同所引用的来源、根、解释器或业务材料。

### 0.1 固定文档依据

以下是本次物化时对两份既有设计文件进行只读摘要核对的记录，不是来源准入、
运行验证或对其全部设计内容重新接受。

| 文档 | 字节数 | SHA-256 |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md | 54703 | 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md | 54109 | 87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD |

配套候选：
docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md。
此路径只是配套文件定位，不是假造一个已接受的 ArtifactRef。
两份候选的完整文件 SHA 应在完成写入后通过分离记录报告；不将自身或对方的
未来文件 SHA 嵌入形成循环。未来使用须另行接受其准确文件身份。

### 0.2 明确不发生的动作

仅新增两份 Markdown 候选。不修改已接受文件、189 项输入与预期清单、
唯一候选源码、既有准备计划或执行包。不生成 Manifest，不生成实际来源数据、
测试向量、编码器、验证程序或第三份审查文件。
不装载、不测试、不探测或变更环境、不准入来源、不实际捕获、不集成或部署。
不访问独立 ACOS 或其他项目。角色分离无需真实人物信息。

未来 Manifest 也须保留准备计划第 6 节的内容边界：不以时间戳代替身份，
不包含真实凭据、密钥、token、外部定位符、安装指令、运行结果或聚合验证结论。
真实案件材料、受保护内容和可执行输入不因字段可容纳 Text 而获准进入。
局部路径及 SHA 仅是必要身份元数据，不授予访问所指资产的权限。

## 1. 基础类型与封闭规则

### 1.1 基础类型

| 类型 | 精确要求 |
| --- | --- |
| Text | 非空有效 Unicode 标量序列；不裁剪、翻译、修复、规范化或改大小写 |
| Identifier | Text；属于对应先前绑定来源声明的标识集合，不临时创造替代身份 |
| SHA256 | 完整 64 位大写十六进制字符串，字符只可为 0—9、A—F |
| UInt | 精确非负整数，范围从 0 起；不额外发明固定机器字长上限 |
| PositiveInt | 精确正整数，范围从 1 起；不额外发明固定机器字长上限 |
| Boolean | 仅 true 或 false，不使用数字或字符串替代 |
| RelativePath | 经绑定政策确认的规范、保留大小写、使用 / 的相对文件路径 |
| RootId | PROJECT_ROOT、VENV_ROOT、RUNTIME_ROOT、SYSTEM_ROOT |
| ScenarioId | C03-TA-V-001 至 C03-TA-V-015，保留原完整标识 |
| EntryCategory | 第 3.7 节的 12 类闭集 |
| EntryRole | 第 3.7 节的 12 项用途闭集 |
| LoaderKind | SOURCE、EXTENSION、DLL、DATA、CONFIG、EXECUTABLE、GOVERNANCE |

RelativePath 禁止盘符、父目录跳转、空路径段、备用数据流、未解析环境变量、
通配或目录级授权。序列化不能替解析政策修复路径。
未能确定路径、大小写或重解析身份时，受影响范围阻断。

所有对象采用封闭成员集合。表中列出的成员均必填、不得为 null，除非明确的
判别分支本来不含该成员。本文没有可空字段；不允许以 null 补齐缺失字段。
未知成员、类型替代、隐式默认值、未绑定身份或未声明数组路径均阻断。

整数不得接受 Boolean、浮点数、指数、带小数点的数字或数字字符串替代。
所有计算必须精确，处理工具无法保持精度时停止，不截断、舍入或改写数值。
解码后重复的对象键须在解析器覆盖前被拒绝；转义拼写不同但解码相同仍是重复。
空数组只能表达经相应来源及政策明确支持的空集合，不能隐藏缺失证据或清除 LIMITED。

### 1.2 共用对象类型

| 类型 | 封闭成员 |
| --- | --- |
| ArtifactRef | path: RelativePath；sha256: SHA256；locator: Text |
| FileRef | root_id: RootId；relative_path: RelativePath；byte_length: UInt；sha256: SHA256 |
| OriginRef | kind: FILE 或 INTERPRETER；identity: FileRef；symbol: Text；basis: ArtifactRef |
| DeclarationSite | declaration_id: Identifier；kind: FILE_SITE 或 INTERPRETER_SITE；identity: FileRef；locator: Text；basis: ArtifactRef |
| SubjectBinding | subject_id: Identifier；file: FileRef；callable_record: ArtifactRef |
| FixtureBinding | scenario_id: ScenarioId；file: FileRef |
| EntryClassification | entry_id: Identifier；basis: ArtifactRef |
| CategoryCount | category: EntryCategory；count: UInt |

ArtifactRef.path 指向本项目内实际存在、先前固定身份的完整文件；locator 须唯一定位
适用内容，sha256 覆盖完整文件而非摘录。引用存在不等于其内容已被接受。
不能引用未来生成的审查、接受、运行或捕获凭证补齐当前资格。

FileRef 是身份引用，不是读取、装载或执行授权。内建、冻结及解释器内部来源通过
OriginRef 的 INTERPRETER 分支绑定真实解释器，不伪造模块文件或生成代码文件。
FILE_SITE 与 INTERPRETER_SITE 分别指向真实声明文件或解释器声明依据；
调用栈文字、文件名前缀、co_filename、相似名称或 <string> 不单独构成来源证明。

### 1.3 NOT_APPLICABLE 规则

parent 和 import_name 保持字符串类型。只有对应绑定来源明确确认字段不适用时，
才可使用精确值 NOT_APPLICABLE。未知、缺失、未绑定不能转为不适用。
它仅在这两个字段中作为保留哨兵，不扩展到全部 Identifier 字段。
若真实模块或父模块标识与该值冲突，不翻译、转义、改名或推断，阻断该用法，
等待另行合同处理。适用时保留原真实标识，不根据类别或文件名猜测。

## 2. 顶层对象

未来 Manifest 的顶层恰好包含以下 11 组，没有其他成员：

| 成员 | 类型 |
| --- | --- |
| manifest_identity | ManifestIdentity |
| root_bindings | RootBinding 数组 |
| runtime_identity | RuntimeIdentity |
| import_contract | ImportContract |
| trusted_operation_contract | TrustedOperationContract |
| input_contract | InputContract |
| entries | Entry 数组 |
| excluded_sets | ExcludedSets |
| closure_evidence | ClosureEvidence |
| aggregate_identity | AggregateIdentity |
| governance | Governance |

每个数组路径的元素、基数、顺序与重复处理须同时符合配套登记候选。
配套候选列出 32 个路径模式；其固定参数不表示实际来源值已经绑定或准入。

## 3. 嵌套类型

### 3.1 ManifestIdentity

| 成员 | 类型 / 约束 |
| --- | --- |
| manifest_id | Identifier |
| manifest_version | Text，由先前生成授权固定 |
| encoding_version | 固定 WP008-RDM-CANON-2 |
| package | ArtifactRef，适用执行包身份 |
| preparation_plan | ArtifactRef，适用准备计划身份 |
| design_adoption | ArtifactRef，已经完成的相应设计采纳记录 |
| typed_contract | ArtifactRef，生成前已经接受的完整类型合同 |
| array_registry | ArtifactRef，生成前已经接受的完整数组政策登记 |
| input_binding | FileRef，唯一具体输入绑定 |
| harness | FileRef |
| environment_record | ArtifactRef |
| subject_catalog | ArtifactRef |
| fixture_catalog | ArtifactRef |
| generation_authority | ArtifactRef，先于生成活动成立 |

本候选的物化不建立上述实际 ArtifactRef。设计采纳不等于来源准入或运行授权。
不得在未来 Manifest 中填入自身完整文件 SHA、未来审查 SHA 或未来接受 SHA。

### 3.2 RootBinding 与 ReadScope

| RootBinding 成员 | 类型 |
| --- | --- |
| root_id | RootId |
| canonical_directory | Text |
| source_record | ArtifactRef |
| independent_review | ArtifactRef |
| owner_decision | ArtifactRef |
| resolver | OriginRef |
| resolver_version | Text |
| case_policy | ArtifactRef |
| reparse_policy | ArtifactRef |
| read_scope | ReadScope 数组，非空 |
| integrity_evidence | ArtifactRef 数组，非空 |
| residual_limitations | Text 数组，允许经证实的空集合 |

| ReadScope 成员 | 类型 |
| --- | --- |
| file | FileRef |
| purpose | ReadPurpose |
| phase | PREPARATION、T0、T1、T2、T3 或 T4 |
| basis | ArtifactRef |

ReadPurpose 闭集：
STATIC_IDENTITY_CHECK、PREFLIGHT_READ、SOURCE_PARSE、LITERAL_IMPORT、
BOOTSTRAP_LOAD、LITERAL_DATA_READ、FIXTURE_READ、BINDING_READ。
这些是用途分类，不是权限开关；它们属于本有限设计，不是对实际读取的批准。

恰好四个 RootId，各出现一次。每条 ReadScope.file.root_id 必须等于所属
RootBinding.root_id。文件仅在该根已绑定目录身份、大小写及重解析政策下解释。
ReadScope.basis 必须唯一定位完整文件身份、purpose、phase 及该组合的批准范围，
并与该根来源、复核和 Owner 决定相容。其他根权限不能冒充本根权限。
跨根依赖须引用另一个独立根绑定下的合法 FileRef / ReadScope，不能嵌入本根替代。
缺失、冲突或唯一解析失败时阻断受影响绑定；不查找替代根或自动扩权。

目录文字、路径相同或 SHA 相同不能独立建立根可信性。
根绑定不授予目录枚举、递归读取或重解析跟随权限。
不推断新的用途—阶段矩阵；每条实际组合都需要先前准确的批准依据。

### 3.3 RuntimeIdentity 与 StartupStep

| RuntimeIdentity 成员 | 类型 |
| --- | --- |
| implementation_record | Text，保留来源原文 |
| version_record | Text，不从资源版本推导未记录的实际运行版本 |
| architecture_record | Text |
| identity_basis | ArtifactRef |
| environment_acceptance | ArtifactRef |
| validation_launcher | FileRef |
| base_executable_identity | FileRef |
| configuration | FileRef |
| core_libraries | FileRef 数组，非空 |
| declared_startup_sequence | StartupStep 数组，非空 |
| startup_contract | ArtifactRef |
| startup_prerequisite_evidence | ArtifactRef 数组，非空 |
| limitations | Text 数组 |

StartupStep 恰好包含：
step_id: Identifier；ordinal: PositiveInt；file: FileRef；role: EntryRole；
required_by: Identifier；basis: ArtifactRef。

启动序列是已绑定的声明依赖设计，不声称已经启动或实际装载。
step_id 和 ordinal 不重复，ordinal 从 1 连续。不同步骤复用同一文件时，
来源必须逐次明确其身份、步骤和用途，不能用一个步骤推断其他步骤。

base_executable_identity 仅记录身份。若未来实际使用需要装载或执行，而已有
分类及批准不能完整覆盖，必须阻断；不能绕过唯一验证解释器限制。
真实 T0 预进程检查及其后续分离绑定记录不得预写为未来成功事实。

### 3.4 ImportContract、LookupItem 与 ModuleRecord

| ImportContract 成员 | 类型 |
| --- | --- |
| lookup_order | LookupItem 数组，非空 |
| modules | ModuleRecord 数组，非空 |
| denied_modules | 固定拒绝模块集合 |
| socket_guard_origin | OriginRef |
| origin_policy | ArtifactRef |

LookupItem 恰好包含：
lookup_kind: SOURCE_IMPORT / EXTENSION_IMPORT / DLL_DEPENDENCY；
root_id: RootId；location: 下述 Location 分支；basis: ArtifactRef。

Location 只有两个封闭分支：

| kind | 该分支的全部成员 |
| --- | --- |
| ROOT_SELF | kind |
| RELATIVE | kind；relative_path: RelativePath |

| ModuleRecord 成员 | 类型 |
| --- | --- |
| module_name | Identifier |
| parent | Identifier 或按第 1.3 节使用的 NOT_APPLICABLE |
| kind | SOURCE、EXTENSION、BUILTIN 或 FROZEN |
| identity | FileRef |
| loader | OriginRef |
| caller | OriginRef |
| read_phases | T1 / T3 数组 |
| evidence | ArtifactRef 数组，非空 |

SOURCE、EXTENSION 绑定真实文件；BUILTIN、FROZEN 绑定解释器身份。
完整搜索次序绑定到 origin_policy 中唯一序列；不能从各 LookupItem.basis 临时拼接。
各项 basis 仍须与完整来源相容。查询身份键及别名处置见配套登记。

拒绝模块闭集：
ssl、http、urllib、ftplib、smtplib、imaplib、poplib、telnetlib、webbrowser、
subprocess、multiprocessing、ctypes。未列入允许闭包的模块仍默认拒绝。
socket_guard_origin 仅限固定 harness 防护初始化，不授权被审对象联网。

### 3.5 TrustedOperationContract 与 OperationRecord

TrustedOperationContract 恰好包含：
operations: 非空 OperationRecord 数组；default_denied: 固定 true；
policy: ArtifactRef。

| OperationRecord 成员 | 类型 |
| --- | --- |
| operation_id | Identifier |
| operation_class | STATIC_AST_PARSE、NORMAL_LITERAL_IMPORT 或 DATACLASS_INTERNAL_GENERATION |
| origin | OriginRef |
| read_phases | 该类别允许阶段的非空数组 |
| declaration_sites | DeclarationSite 数组，非空 |
| content_policy | ArtifactRef |
| namespace_policy | ArtifactRef |
| input_policy | ArtifactRef |
| enforcement_evidence | ArtifactRef 数组，非空 |
| limitations | Text 数组 |

| 类别 | 允许阶段 | 必须保持的限制 |
| --- | --- | --- |
| STATIC_AST_PARSE | 仅 T2 | 固定源码与解析器，仅产生 AST，不执行目标源码 |
| NORMAL_LITERAL_IMPORT | T1 / T3 | 精确模块、装载器和父调用者；T1 不预装被审对象 |
| DATACLASS_INTERNAL_GENERATION | T1 / T3 | 固定生成器、声明位置、内容及命名空间；fixture、CLI、环境值不得成为执行内容；T1 不预装被审对象 |

三项政策引用均须提供该类别的明确内容限制，不能缺省或泛称“安全”。
每项操作仍须满足以上硬限制；来源允许不能覆盖阶段或能力禁令。
生成代码不建立虚构文件条目或文件 SHA；其他动态操作默认拒绝。
审计钩子与 socket 包装不被表述为防篡改沙箱或外侧环境隔离的证明。

### 3.6 InputContract、ScenarioRecord 与 VariantRecord

| InputContract 成员 | 类型 |
| --- | --- |
| binding | FileRef，唯一具体绑定 |
| admission | ArtifactRef |
| subjects | SubjectBinding 数组，非空且成员与绑定目录完全一致 |
| fixtures | FixtureBinding 数组，恰好原 15 项 |
| scenarios | ScenarioRecord 数组，恰好原 15 项 |
| observation_dispositions | ArtifactRef 数组，非空 |

subject 目录仍受原十个固定 subject 的范围约束；“非空”不允许减少原范围。
固定具体绑定路径仍为
PROJECT_ROOT/validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json。
候选文件或旧设计对的记录不自动迁移为该文件在新设计下的准入。

ScenarioRecord 恰好包含：
scenario_id: ScenarioId；fixture: FileRef；variants: 非空 VariantRecord 数组。

VariantRecord 恰好包含：
variant_id: Identifier；input_locator: Text；expected_locator: Text；
subject_id: Identifier；callable_id: Identifier；observation_policy: ArtifactRef；
limitation_dispositions: ArtifactRef 数组。

场景与 fixture 保持 C03-TA-V-001 至 C03-TA-V-015 的固定顺序。
变体身份、顺序、基数、输入及独立预期须逐项来自已接受绑定。
不重新生成、拆分或补写已采纳的 189 项清单，也不将其直接等同于 189 个可执行变体。
callable_id 仅解析到固定审查过的 harness 映射；数据不能驱动任意导入或分派。
这里只绑定未来观察政策，不填入未来捕获结果或其 SHA。

### 3.7 Entry：严格十五字段

| 成员 | 类型 / 约束 |
| --- | --- |
| ordinal | PositiveInt，规范排序后从 1 连续 |
| entry_id | Identifier，稳定的类别前缀标识且全局唯一 |
| category | EntryCategory |
| root_id | RootId |
| relative_path | RelativePath |
| byte_length | UInt |
| sha256 | SHA256 |
| role | EntryRole |
| required_by | Identifier，绑定依赖记录中的精确 bootstrap / harness / subject / extension / PE / governance 引用 |
| import_name | 精确模块标识或按第 1.3 节使用的 NOT_APPLICABLE |
| loader_kind | LoaderKind |
| read_phase | 非空、升序、逗号连接的 T1—T4 子集；无空格或重复 |
| executable | Boolean |
| network_capable | Boolean，有明确分类依据 |
| reparse_state | DIRECT 或已接受精确重解析映射中的标识 |

| EntryCategory | EntryRole | 允许的装载类型 |
| --- | --- | --- |
| PYTHON_EXECUTABLE | VALIDATION_ENTRYPOINT | EXECUTABLE |
| PYTHON_CONFIG | VALIDATION_ENVIRONMENT_CONFIG | CONFIG |
| CPYTHON_CORE_DLL | CPYTHON_BOOTSTRAP_LIBRARY | DLL |
| STDLIB_SOURCE | APPROVED_STDLIB_SOURCE | SOURCE |
| STDLIB_EXTENSION | APPROVED_STDLIB_EXTENSION | EXTENSION 或 DLL，逐文件唯一绑定 |
| STDLIB_DATA | APPROVED_LITERAL_DATA | DATA |
| OS_RUNTIME_DLL | APPROVED_OS_BOOTSTRAP_LIBRARY | DLL |
| HARNESS_SOURCE | VALIDATION_HARNESS_SOURCE | SOURCE |
| SUBJECT_SOURCE | FIXED_SUBJECT_SOURCE | SOURCE |
| GOVERNANCE_INPUT | PREFLIGHT_GOVERNANCE_INPUT | GOVERNANCE |
| FIXTURE_INPUT | ORIGINAL_SCENARIO_FIXTURE | DATA |
| SCENARIO_INPUT_BINDING | ADMITTED_CONCRETE_INPUT_BINDING | DATA 或 GOVERNANCE，逐文件唯一绑定 |

上述用途枚举及对应关系是有限采纳的设计，不是某个实际文件分类已被接受的证明。
对于两个可选装载分支，EntryClassification.basis 必须唯一定位具体文件、类别、
所选 loader_kind，并与 role、read_phase 及能力分类依据一致。
缺失、冲突或无法定位时阻断，不任选、不回退。

executable=true 仅允许唯一已接受验证解释器。两个布尔标记均不授予执行或联网；
false 也不证明文件没有内部执行能力。T0 不进入 read_phase。
未知、占位、通配、未解析路径、缺失 SHA、推断文件或目录授权不得进入正式 Manifest。

entries 同时独立检查 entry_id、规范文件身份 (root_id, relative_path)、
排序四元组 (category, root_id, relative_path, entry_id) 的唯一性。
不同标识、类别、用途或相同 SHA 不能豁免同一文件重复登记。
按已绑定根解析、大小写与重解析政策处理跨拼写或跨根别名；已证明重复或
受影响身份未决时阻断，不自动合并、去重或静默删除。
不同文件仅内容 SHA 相同不等于相同身份。其他组可以对同一文件作一致引用。

### 3.8 ExcludedSets 与 ExclusionRule

ExcludedSets 恰好包含：
denied_modules: 与 ImportContract 完全相同的集合；
denied_capabilities: 下列固定集合；rules: ExclusionRule 数组；
policy: ArtifactRef。

拒绝能力闭集：
NETWORK_IO、PROCESS_CREATION、DYNAMIC_CODE_OUTSIDE_APPROVED_OPERATIONS、
UNDECLARED_FILE_ACCESS、IMPORT_SEARCH_PATH_MUTATION、GUARD_STATE_MUTATION、
UNREVIEWED_EXTENSION_LOADING、EXTERNAL_TOOL_INVOCATION、TARGET_PRELOAD_IN_T1、
LATE_LOADING_IN_T4。

| ExclusionRule.kind | 该分支的全部成员 |
| --- | --- |
| CATEGORY | kind；category: 下列排除类别；basis: ArtifactRef |
| EXACT_PATH | kind；root_id: RootId；relative_path: RelativePath；basis: ArtifactRef |

排除类别闭集：
SITE_PACKAGES、INSTALLATION_TOOL、DEVELOPMENT_HEADER、UNUSED_TEST_ASSET、
TK_TCL、PACKAGE_METADATA、DOCUMENTATION、BYTECODE、CACHE、UNUSED_ASSET。
rules 须覆盖全部排除类别，可另列经绑定的精确拒绝路径。

EXACT_PATH 与 entry 经绑定根政策解析后为同一文件身份或已证明别名时阻断。
CATEGORY 是否涵盖某 entry，须由绑定分类依据与排除政策明确判定，
不能只比较两套类别名是否相同或根据路径片段猜测；受影响成员关系不明时阻断。
允许 entry 不能覆盖排除规则，也不通过删除条目消解冲突。
被禁模块、能力、阶段与拟允许操作或读取范围交叠时阻断。
能力标记本身不证明被禁操作已发生，也不授予该操作。
核对拒绝路径不要求或授权读取其内容、搜索目录、计算其 SHA 或扩大访问。
依据不足继续阻断；依赖需要和审查声明都不能豁免排除集，-S 要求保留。

### 3.9 ClosureEvidence

| 成员 | 类型 |
| --- | --- |
| static_source_resolver | OriginRef |
| pe_resolver | OriginRef |
| os_resolver | OriginRef |
| origin_policy | ArtifactRef |
| resolution_evidence | ArtifactRef 数组，非空 |
| entry_classification | EntryClassification 数组，每个 entry 恰好一项 |
| unresolved_count | UInt |
| duplicate_count | UInt |
| limitations | Text 数组 |

拟正式使用的 Manifest 要求未解析数和冲突重复数都为 0，但不得删除问题条目取得 0。
仍有未解析项时保留阻断诊断，不生成可正式使用的 Manifest，不虚构文件补齐闭包。
这项要求不是本次物化已取得闭包的声明。

### 3.10 AggregateIdentity

封闭成员：
entry_count: PositiveInt；byte_total: UInt；
category_counts: CategoryCount 数组；entry_aggregate_sha256: SHA256。

12 类均须出现，包括计数为 0 的类别。
entry_count 为规范 entry 条数；byte_total 为 byte_length 的精确总和，
不是 JSON 或聚合字节流长度。类别计数来自同一 entry 集合。
不包含 Manifest 自身完整文件 SHA。

### 3.11 Governance

| 成员 | 类型 / 约束 |
| --- | --- |
| generation_authority | ArtifactRef，与 ManifestIdentity 完全一致 |
| materializer_role | 生成授权中明确绑定的角色 Identifier |
| independent_review_policy | ArtifactRef |
| owner_decision_policy | ArtifactRef |
| independent_review_required | 固定 true |
| owner_acceptance_required | 固定 true |
| execution_grant_in_manifest | 固定 false |

这些是流程要求，不声称已完成审查、接受或运行。
未来针对 Manifest 的复核、Owner 决定及运行凭证须在分离记录中绑定其完整 SHA，
不回填已经固定身份的旧文件。稳定角色身份足够，不要求真人身份资料。

## 4. 跨组拒绝与相容规则

1. 同一文件身份的 SHA 和长度在所有引用中一致；不一致即阻断。
2. 同一证据文件路径不能同时绑定不同 SHA；不同 locator 可以引用同一固定文件。
3. 两处具体输入绑定必须完全一致，并符合第 3.6 节的唯一固定路径。
4. subject、fixture、scenario、variant 逐项符合绑定目录，不能仅数量相等。
5. 每个 scenario.fixture 与原 fixture 表中相应身份一致。
6. 所有 entry 都有唯一分类依据；依赖标识均可准确定位。
7. 文件来源、扩展来源与解释器内部身份不能互相伪装。
8. 排除冲突按第 3.8 节处理，能力分类不能代替行为或权限事实。
9. T1—T4 读取同时满足准确 entry、读取授权和阶段限制；代码操作还需第 3.5 节来源合同。
10. PREPARATION / T0 身份引用不自动成为 T1—T4 读取、装载或执行许可。
11. 根、目录、搜索顺序或重解析映射均不产生目录级读取授权。
12. 唯一性通过后才排序、编号和计算同一 entry 集合的计数及摘要。
13. 全部 LIMITED 保持可定位来源；空数组、缺项或“0”不能清除上游限制。
14. 未来接受、运行或捕获 SHA 不能补齐当前缺口；不使用自身摘要形成循环。
15. 按依赖关系及可证实的时间范围，评估变化对后续使用和相关历史输出的影响。正常版本更新不自动推翻历史结果；历史记录始终保留，不自动废止全部项目成果。

发现缺失、未批准重解析或无法解释的绑定差异时保持阻断；不自动扫描、补源、
替换或改写已接受文件。本文不开展真实历史影响调查，也不撤销历史记录。

## 5. WP008-RDM-CANON-2 字节合同

### 5.1 标量、字符串与键

整数使用十进制 ASCII；本合同仅允许非负整数，不接受加号、前导零、
指数、小数点、负零、分数、NaN 或 Infinity。零仅为 0。
true / false 使用小写。null 在本合同中无允许字段。
数值 token 必须在转换掩盖非法形式前验证。

字符串用 ASCII 双引号包围原 Unicode 标量序列。
U+0022 编码为 \"，U+005C 编码为 \\。
U+0000—U+001F 每个编码为六个 ASCII 字符 \u00xx，十六进制为小写；
不使用 \n、\t 等短转义。其余标量直接输出 UTF-8，包括 /、非 ASCII、
U+2028、U+2029；不使用可选斜线、HTML 或 ASCII-only 转义。
拒绝非法 UTF-8、孤立代理项，不修复、不规范化、不做区域或大小写变换。
规则适用于所有深度的成员名和字符串值。

对象键按解码后 Unicode 码点词典序排列；第一差异码点小者在前，
精确前缀先于其扩展。不能用区域、UTF-16 码元或转义 token 排序替代。
数组仅按已接受且完整绑定的对应政策处理。

### 5.2 完整 JSON 布局

1. UTF-8 无 BOM；格式字符仅 ASCII 空格及 LF，不使用 tab、CR 或 CRLF。
2. 顶层从深度 0 开始。非空对象左花括号后为 LF；每个成员以每层两个空格、
   编码后的键、冒号、一个空格及编码后的值组成。
3. 非空数组左括号后为 LF；每个元素独占起始行，按深度缩进。
   作为值的容器在值所在行起始，再递归应用同一布局。
4. 非末成员或元素后为逗号加 LF；末项只有 LF；右分隔符与其容器深度对齐。
   无格式空行、填充、行尾空格或尾逗号。
5. 空容器恰好为 {} 或 []，内部没有空格或换行。
6. 顶层右花括号后恰好一个 LF，没有其他字节。字符串内控制符始终转义。

### 5.3 十五字段聚合流

顺序严格为：
ordinal、entry_id、category、root_id、relative_path、byte_length、sha256、
role、required_by、import_name、loader_kind、read_phase、executable、
network_capable、reparse_state。

每项按本节规则编码为不含无关空白、无末尾 LF 的单个紧凑 JSON 标量 token。
字符串含双引号，整数与 Boolean 不含双引号。
read_phase 保持整个带引号的逗号连接字符串，不变成数组。
每行恰好十五 token，以十四个原始 0x1F 分隔，末尾恰好一个原始 0x0A；
最后一条也有 LF，无前导分隔符、BOM 或空记录。
按规范 entry 顺序连接后计算 SHA-256。
字符串控制符转义保证值不能注入原始 US 或记录 LF。

### 5.4 分离摘要与拒绝

entry 聚合 SHA 仅覆盖 entries，不认证操作、输入或治理政策。
完整文件 SHA 覆盖全部 11 组及唯一最终 LF。两者均需完整 64 位大写十六进制。
Manifest 自身完整 SHA 仅进入后续分离记录，不进入自身或先前具体输入、harness。
禁止旧编码摘要、旧接受记录自动迁移；不规范化已固定摘要的文件后保留旧凭证。
本合同没有生成编码器或证明跨实现字节一致性。

## 6. 静态复核与后续使用停点

当前 Owner 有限采纳针对组合设计文本，不等于本物理候选及配套候选已经被固定 SHA 接受。
可开展的本批次核对仅限：文档结构、32 路径相容、六项 REV3 修订保真、
来源文件摘要、排版及权限边界。不得运行候选或验证程序来补齐证据。

正式生成前仍需准确的类型合同与数组登记文件身份、独立复核及 Owner 处置，
完整实际来源与根绑定、具体输入准入、harness 和环境及来源政策依据，
并另行获得准确生成授权。本次不建立任何一项尚缺的实际资格。

189 项原清单、原 REV1 / REV2、既有复核、首次失败及后续历史记录均保留。
D-007、可信装载、输出隔离、计时、外侧停止、来源准入和实际捕获能力
未由本文证明。DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 保留。
