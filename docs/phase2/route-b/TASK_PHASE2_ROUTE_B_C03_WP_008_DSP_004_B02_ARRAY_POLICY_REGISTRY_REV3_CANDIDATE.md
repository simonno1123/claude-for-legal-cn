# DSP-004 B-02 数组政策登记候选 — Combined REV3

## 0. 身份、效力与边界

| 项目 | 候选记录 |
| --- | --- |
| 所属项目 | claude-for-legal-cn / Phase 2 Route B C03 WP-008 / DSP-004 |
| 文档性质 | DOCUMENT-ONLY ARRAY-POLICY REGISTRY CANDIDATE |
| 设计来源 | 会话 REV2（writing 87426）与 REV3 附录（writing 90376）的组合设计 |
| Owner 范围 | 有限采纳组合 REV3；仅授权新增本登记候选与类型合同候选及独立静态复核 |
| 实际登记状态 | 未填入、未准入真实序列来源或数组登记事实；不是可直接用于 Manifest 生成的已接受登记 |
| 复核与接受 | 后续复核结论另行报告，不在形成记录预填 PASS；物化不构成固定 SHA 接受 |
| 保留状态 | DSP-004 OPEN / HOLD；B-01、B-02 OPEN；全部 LIMITED 与历史记录保留 |

配套类型合同：
docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md。
其名称是配套定位，不冒充已接受 ArtifactRef；两份候选完整文件 SHA 仅在写入后
通过分离记录报告，不互嵌未来摘要形成循环。

本候选固定 32 个 Manifest 数组路径模式的设计参数，并说明实际来源绑定的缺口。
没有生成 Manifest、实际来源数据、JSON Schema、编码器、测试向量、独立审查文件、
具体输入或运行结果。不修改已接受文件、189 项清单或唯一候选源码。
不装载、不测试、不探测或变更环境、不准入来源、不实际捕获、不集成或部署；
不涉及独立 ACOS 或其他项目。

### 0.1 文档依据

| 既有设计文件 | 字节数 | SHA-256 |
| --- | --- | --- |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md | 54703 | 6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA |
| docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md | 54109 | 87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD |

这是本次只读文件摘要记录，不证明其全部内容被重新接受，也不准入其指向的其他资产。
本文只有设计政策，不声称已经对真实 Manifest 或物理候选源码做路径覆盖验证。

## 1. 全局政策与比较器

每个实际数组路径在先前接受的完整登记中必须恰好匹配一个政策。
[] 表示类型模式中的数组元素，不是文件系统通配符，不授予搜索、读取或枚举权限。
没有匹配、匹配重叠、类型冲突或无法唯一定位时阻断，禁止使用隐式默认值。
不得从 map 遍历、目录顺序、当前输入顺序、实现默认或期望摘要倒推出政策。

| 名称 | 定义 |
| --- | --- |
| CODEPOINT | 解码后的 Unicode 标量词典序；第一差异码点较小者先；精确前缀先于扩展 |
| NUMERIC | 精确整数数值顺序，不强制转换、舍入或截断 |
| TUPLE | 按列出的完整键逐分量从左至右比较；各分量按其声明类型比较 |
| PHASE_RANK | 仅对应允许的 T1—T4 枚举，以其阶段数值 1—4 排序；不发明新阶段 |
| FILE_KEY | (root_id, relative_path)，分量均用 CODEPOINT |
| ARTIFACT_KEY | (path, locator)，分量均用 CODEPOINT |

SET_SORTED 固定元素类型、完整键及比较器。重复身份、相同排序键或未绑定平局规则
均阻断；不去重、合并、任意打破平局或以完整对象字符串排序兜底。
同一文件身份出现不同长度或 SHA 为冲突；同一证据文件路径不能绑定不同 SHA。
SHA 不是用来把同一身份冲突排序成两个合法成员的平局键。

ORDERED 保持先前固定来源的精确顺序，不作为集合重排。
元素身份重复按每条政策的完整身份键判定；文件引用复用不自动等同于元素重复。
空数组仅在行中允许、且来源与政策明确支持该空集合时成立，不能代替证据或清除 LIMITED。

本表的基数、成员类型和键是设计约束，不是已经检查实际数组并取得通过的记录。

## 2. 32 条路径政策

| Policy ID | Manifest 数组路径模式 | 元素类型 | 基数 | 模式 | 完整身份 / 排序规则 |
| --- | --- | --- | --- | --- | --- |
| AP-001 | root_bindings | RootBinding | 恰好四个不同 RootId | SET_SORTED | root_id，CODEPOINT |
| AP-002 | root_bindings[].read_scope | ReadScope | 至少 1 | SET_SORTED | (file.root_id, file.relative_path, purpose, phase)，各分量 CODEPOINT |
| AP-003 | root_bindings[].integrity_evidence | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-004 | root_bindings[].residual_limitations | Text | 0 或更多 | SET_SORTED | 字符串本身，CODEPOINT |
| AP-005 | runtime_identity.core_libraries | FileRef | 至少 1 | SET_SORTED | FILE_KEY |
| AP-006 | runtime_identity.declared_startup_sequence | StartupStep | 至少 1 | ORDERED | step_id 唯一；ordinal 从 1 连续；完整来源见第 3 节 |
| AP-007 | runtime_identity.startup_prerequisite_evidence | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-008 | runtime_identity.limitations | Text | 0 或更多 | SET_SORTED | 字符串本身，CODEPOINT |
| AP-009 | import_contract.lookup_order | LookupItem | 至少 1 | ORDERED | 按 location.kind 的完整查询身份分支，见第 3 节 |
| AP-010 | import_contract.modules | ModuleRecord | 至少 1 | SET_SORTED | module_name，CODEPOINT |
| AP-011 | import_contract.modules[].read_phases | T1 或 T3 | 1 至 2 | SET_SORTED | PHASE_RANK，阶段不重复 |
| AP-012 | import_contract.modules[].evidence | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-013 | import_contract.denied_modules | 固定拒绝模块字符串 | 全部固定集合且各一次 | SET_SORTED | 模块名，CODEPOINT |
| AP-014 | trusted_operation_contract.operations | OperationRecord | 至少 1 | SET_SORTED | operation_id，CODEPOINT |
| AP-015 | trusted_operation_contract.operations[].read_phases | 对应类别允许的 T1 / T2 / T3 | 至少 1，最多为该类别允许阶段数 | SET_SORTED | PHASE_RANK，阶段不重复 |
| AP-016 | trusted_operation_contract.operations[].declaration_sites | DeclarationSite | 至少 1 | SET_SORTED | declaration_id，CODEPOINT |
| AP-017 | trusted_operation_contract.operations[].enforcement_evidence | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-018 | trusted_operation_contract.operations[].limitations | Text | 0 或更多 | SET_SORTED | 字符串本身，CODEPOINT |
| AP-019 | input_contract.subjects | SubjectBinding | 非空且与固定 subject 目录完全一致 | SET_SORTED | subject_id，CODEPOINT |
| AP-020 | input_contract.fixtures | FixtureBinding | 原 15 项各一次 | ORDERED | scenario_id；固定 001 至 015 来源顺序，见第 3 节 |
| AP-021 | input_contract.scenarios | ScenarioRecord | 原 15 项各一次 | ORDERED | scenario_id；固定 001 至 015 来源顺序，见第 3 节 |
| AP-022 | input_contract.scenarios[].variants | VariantRecord | 非空且精确符合各场景原绑定 | ORDERED | 每个具体场景数组内 variant_id 唯一；原顺序和基数，见第 3 节 |
| AP-023 | input_contract.scenarios[].variants[].limitation_dispositions | ArtifactRef | 0 或更多 | SET_SORTED | ARTIFACT_KEY |
| AP-024 | input_contract.observation_dispositions | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-025 | entries | Entry | 至少 1 | SET_SORTED | (category, root_id, relative_path, entry_id)，CODEPOINT 元组；另独立拒绝 entry_id 及文件身份重复 |
| AP-026 | excluded_sets.denied_modules | 固定拒绝模块字符串 | 与 AP-013 完全一致 | SET_SORTED | 模块名，CODEPOINT |
| AP-027 | excluded_sets.denied_capabilities | 固定拒绝能力字符串 | 全部固定集合且各一次 | SET_SORTED | 能力名，CODEPOINT |
| AP-028 | excluded_sets.rules | ExclusionRule | 覆盖全部排除类别，可附绑定的精确拒绝路径 | SET_SORTED | 先 kind，CATEGORY 再 category；EXACT_PATH 再 root_id、relative_path；均 CODEPOINT |
| AP-029 | closure_evidence.resolution_evidence | ArtifactRef | 至少 1 | SET_SORTED | ARTIFACT_KEY |
| AP-030 | closure_evidence.entry_classification | EntryClassification | 每个 entry 恰好 1 项 | SET_SORTED | entry_id，CODEPOINT |
| AP-031 | closure_evidence.limitations | Text | 0 或更多 | SET_SORTED | 字符串本身，CODEPOINT |
| AP-032 | aggregate_identity.category_counts | CategoryCount | 全部 12 个类别各一次，含计数 0 的类别 | SET_SORTED | category，CODEPOINT |

## 3. 五条 ORDERED 政策的完整参数

### 3.1 实际绑定的共同前置要求

每个具体 ORDERED 路径在先前接受的外部登记中须明确：

| 参数 | 合同要求 |
| --- | --- |
| source_ref_selector | 仅使用下表固定字段选择，不接受任意表达式 |
| sequence_locator_rule | 登记中事先固定的唯一序列定位；不能仅引用整份文档 |
| element_identity_key | 下表规定的完整元素身份键 |
| duplicate_disposition | 下表规定的重复拒绝及引用复用规则 |
| 来源文件身份 | 完整 path、SHA256 及与被选引用的相容证明 |

ArtifactRef 选择器须与所选引用的 path / sha256 一致；序列定位须明确落在
所选引用内容内。FileRef 选择器 input_contract.binding 必须属于 PROJECT_ROOT，
来源 path / sha256 分别等于其 relative_path / sha256。
每个场景的序列定位由事先固定、以 scenario_id 为唯一键的登记行明确给出。
不自动补建，不根据当前读到的内容推断，不执行表达式或通配搜索。
无法唯一定位即阻断。

本候选没有填入这些真实来源值，不能把上述参数名称、候选路径或会话定位当作
实际先前接受的来源记录。未来生成所需的准确登记与政策 SHA 仍须另外绑定。

### 3.2 逐路径参数

| Policy ID | source_ref_selector | sequence_locator_rule | element_identity_key | duplicate_disposition |
| --- | --- | --- | --- | --- |
| AP-006 | runtime_identity.startup_contract | 该 ArtifactRef 内容中由登记固定的完整启动步骤序列 | step_id；另 ordinal 从 1 连续且不重复 | 重复 step_id 或 ordinal 阻断；同一文件在不同步骤出现需来源逐次明确身份、步骤和用途 |
| AP-009 | import_contract.origin_policy | 该 ArtifactRef 内容中由登记固定的完整搜索序列；不拼接各项 basis | ROOT_SELF 分支为 (lookup_kind, root_id, ROOT_SELF)；RELATIVE 分支为 (lookup_kind, root_id, RELATIVE, relative_path) | 完全相同查询身份禁止重复；按已绑定政策处理别名，未决则阻断 |
| AP-020 | manifest_identity.fixture_catalog | 该 ArtifactRef 内容中由登记固定的原 15 项 fixture 序列 | scenario_id | 完整 C03-TA-V-001 至 C03-TA-V-015 各一次且按该固定顺序；缺项、乱序或重复阻断，不排序或补项修复 |
| AP-021 | input_contract.binding | 已绑定文件中由登记固定的场景序列 | scenario_id | 同上：完整 001 至 015 各一次，拒绝缺项、乱序和重复，不重排输入 |
| AP-022 | input_contract.binding | 按每个 scenario_id 唯一固定的该场景原变体序列定位 | variant_id，唯一性范围为当前具体场景数组 | 场景内重复身份阻断；身份、顺序及基数逐项符合来源；不以词典序替代、不跨场景拼接或去重 |

AP-009 两个身份键仅使用已声明分支成员，不为 ROOT_SELF 补一个空的 relative_path。
每项 LookupItem.basis 须与完整来源相容，但不能替代全序列绑定。
AP-022 跨场景标识适用范围继续服从绑定来源，不在此新增全局身份规则。

所有 ORDERED 路径都禁止各自 element_identity_key 重复。
启动序列中同一 FileRef 出现在不同 step_id 不属于元素身份键重复，但须满足
逐次来源证明要求。其他路径是否复用同一文件引用，服从其既有来源及路径政策，
不因本候选自动禁止或放行；引用复用不能豁免 entries 的文件身份唯一性。
启动声明序列不声称已经启动或实际装载。

## 4. 对应六项 REV3 修订的拒绝规则

### 4.1 根归属

AP-001 只有四个不同 RootId。AP-002 每项 file.root_id 必须等于所属 RootBinding.root_id。
其 basis 唯一定位文件身份、purpose、phase 和批准范围，且与父根来源、复核、
Owner 决定相容。跨根依赖引用另一个独立根，不冒充本根读取范围。

### 4.2 文件唯一性与聚合

AP-025 独立拒绝 entry_id 重复、规范文件身份重复及四元组平局。
按已绑定根解析、大小写和重解析政策处理跨根或跨拼写别名。
已证明同一文件重复登记或受影响身份无法确定时阻断，不自动合并或删除。
不同文件仅 SHA 相同不等于同一文件。只有唯一性通过后才赋连续 ordinal、
计算条数、byte_length 总和、类别计数与聚合 SHA。
其他组可以保留一致的重复文件引用，它们不是新增 entry。

### 4.3 ORDERED 来源与适用性

AP-006、009、020、021、022 必须同时满足第 3 节，缺一项都不能因表格已存在而通过。
NOT_APPLICABLE 仅按类型合同指定的 parent / import_name 来源适用条件使用；
未知、缺失或真实标识冲突时阻断，不把哨兵扩展为通用占位。

### 4.4 用途、阶段与装载选择

AP-002 中的用途和阶段由准确 basis 绑定，不从名称推断新的组合。
AP-015 不得越过操作类别的固定阶段限制。
STDLIB_EXTENSION 的 EXTENSION / DLL、SCENARIO_INPUT_BINDING 的 DATA / GOVERNANCE
选择必须在 AP-030 对应分类依据中逐文件唯一确定；不得任意回退。
物化候选不等于实际分类或读取政策已经接受。

### 4.5 排除冲突

AP-028 的 EXACT_PATH 与 entry 指向同一文件或已证明别名时阻断。
CATEGORY 成员关系由明确分类依据和排除政策确定，不只比较类别字符串或猜路径。
成员关系不明时阻断受影响范围。允许 entry 不覆盖排除项，也不以静默删条目修复冲突。
能力分类标记不证明被禁行为已经发生，不授予行为权限。
核验拒绝路径不授权读取、散列、搜索或枚举该路径。

## 5. 覆盖核对与未绑定项

按配套类型合同声明的嵌套结构：

| 顶层组 | 本候选登记的数组政策数 |
| --- | --- |
| manifest_identity | 0 |
| root_bindings | 4 |
| runtime_identity | 4 |
| import_contract | 5 |
| trusted_operation_contract | 5 |
| input_contract | 6 |
| entries | 1 |
| excluded_sets | 3 |
| closure_evidence | 3 |
| aggregate_identity | 1 |
| governance | 0 |
| 合计 | 32 |

这是声明结构的静态对应，不是对实际 Manifest、实际源码或运行时路径的探测。
新增、删除或改变任何实际数组路径都需要准确合同修订与重新复核；
不得借本表将未来结构默认为已经覆盖。

| 尚未由本候选建立的事项 | 保留处理 |
| --- | --- |
| 本物理候选及配套类型合同的固定 SHA 接受 | 另行分离复核及 Owner 处置，不预填接受凭证 |
| 各实际 ORDERED 来源文件、唯一序列定位、逐场景登记行 | 未在本次填入或准入；不以占位字符串替代 SHA 或来源 |
| 四根、大小写、重解析及别名事实 | 需单独准确绑定；本次不探测环境 |
| 准确的具体输入、subject / fixture / variant、观察与可达性处置 | 仍需适用来源及准入；不修改 189 项原清单 |
| 排除类别成员关系和装载分支的实际分类依据 | 缺失或冲突时阻断，不推断 |
| 编码器、生成器和实现是否遵守所有政策 | 未实现或运行验证；本次仅文档静态复核 |
| D-007、可信装载、输出隔离、计时与外侧停止能力 | 未由本候选证明；全部相关 LIMITED 保留 |

来源变化按依赖关系及可证实时间范围评估，不因正常更新自动否定全部历史结果；
历史记录始终保留。发现缺失、未批准重解析或无法解释的绑定差异时保持阻断，
不自动扫描、补源、替换或改写已接受文件。
DSP-004 OPEN / HOLD；B-01、B-02 OPEN。无 Manifest 生成、来源准入、实际捕获或运行资格。
