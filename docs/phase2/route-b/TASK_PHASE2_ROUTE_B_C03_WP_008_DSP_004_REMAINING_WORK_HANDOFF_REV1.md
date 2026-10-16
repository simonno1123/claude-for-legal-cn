# DSP-004 剩余操作收敛与精确交接 REV1

## 1. 目的、执行范围与当前结论

Project Owner 请求“自动完成 dsp-004 项目的剩余操作”。本文件承接该请求，集中说明已具备的本地技术证据、未满足的正式前提和需要补齐的决策输入；不是 Project Owner 接受决定，不替其签署，不改变任何既有固定 SHA。

本轮只读梳理本项目固定文件和输入元数据，重新核对第 7 节 25 个现有项目文件的长度及 SHA；未新增受测对象执行，未运行 Python、编译 C#、重放原业务场景或开展环境探测。唯一新增文件为本交接文档，未修改已接受资产。

**当前不能宣布 DSP-004 整体完成或 CLOSED。** 现有本地合成证据与真实来源/正式运行前提是不同层级。继续增加同层测试不会产生可信角色、准备根、批准记录或执行权限。因此本次收束到可决定的交接点，不再用新增测试数量代替剩余项处理。

DSP-004 继续 OPEN / HOLD；B-01、B-02 继续 OPEN；全部 LIMITED、旧失败和后续验证记录保留。独立 ACOS 和其他项目未访问、未修改。

## 2. 已有技术成果及其真实单位

以下为固定记录中已有的局部结果，本轮只读核对来源身份，不重新执行或重新证明原断言。所有数字不可相加成为总体覆盖率或项目完成百分比。

| 技术层 | 现有记录结果 | 严格效力边界 |
| --- | --- | --- |
| 本地组合 REV2 | 189 个已记录计划项 ID、2027 个父级检查；RW / PURE / D007 三阶段记录 | 合成本地组合，不是正式运行、来源准入或完整停止保证 |
| 既有六组归档一致性 | 6 组、71 项只读归档核对；缺失原始见证被如实区分 | 不是 71 个新增业务测试，不能补造历史缺失的 child 原始正文 |
| CANON-2 标量 / 十五字段流 | 93 项局部检查、12 个向量 | 不包含完整 Manifest 政策或可信根 |
| CANON-2 结构布局 | 81 项局部检查、12 个向量 | 只接受显式合成合同，不是正式 typed contract / 全数组政策注册表 |
| 双层 detached 一致性 | 106 项局部检查、3 个向量 | 全文与条目聚合一致不是来源、签名、权限或新鲜度证明 |
| 编码 / 布局错误注入 | 2 个原版基线；8 个指定内存错误被发现；10 个原进程记录 | 不计算普遍 mutation score；负例不等于候选通过 |
| 双层绑定错误注入 | 1 个原版基线；8 个指定内存错误被发现；9 个原进程记录 | 保留完整负例快照与输出，不把 wrapper 退出 0 当作变异源码通过 |

这些技术成果可支持下一轮精确审查和决定，但不会自行完成接受、准入、正式验证或 DSP-004 关闭。较早受限源码的会话层接受不自动转移到后续 REV 或新 SHA。

## 3. 输入文件确实存在，但文件名不等于准入

| 对象 | 本轮局部核对事实 | 不能推导的结论 |
| --- | --- | --- |
| validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json | 文件存在；元数据引用 V3.1 Package 与 V2.1 Plan；形成时 candidate_state 为 MATERIALIZED_NOT_REVIEWED_NOT_ADMITTED | 不能仅因名称是固定路径，就当作已准入的 V3.2/V2.2 输入 |
| validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json | 文件存在；元数据引用 V3.2/V2.2；形成时状态为 MATERIALIZED_NOT_FORMALLY_REVIEWED_NOT_ACCEPTED_NOT_ADMITTED | 不能把候选物化、元数据记录或后来局部测试当成最终完整输入准入 |
| validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json | 本次指定路径存在性检查为不存在 | 不创建、填充或签署它；此项也不证明仓库外不存在其他历史资料 |

旧名输入的设计身份为：

- Execution Package V3.1：`3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB`。
- Plan V2.1：`07FD553F641CF52EF54FABFCFAD448CC2D432C8A0279082E6DB899EB8C900910`。

当前准备候选指向：

- Execution Package V3.2：`87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD`。
- Plan V2.2：`6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA`。

本轮对输入文件只做身份、元数据与选定限制字段的局部核对，不声称对整个输入或 Package V3.2 完成新的独立全文审查。Plan V2.2 的形成时状态保留；不能用该旧状态抹除后来的会话层有限设计采纳，也不能反向把有限采纳扩大为输入准入。

## 4. 剩余操作与真正的前置输入

| ID | 剩余事项 | 仍需的精确事实 / 决策 | 在事实或决定齐备前的动作 |
| --- | --- | --- | --- |
| DSP004-R-01 | Project / Session / Provider 六侧来源绑定 | 三类边界各自的预期侧与实际侧：来源记录、身份/版本/SHA、产生者职责、授权依据、位置和适用范围；两侧不能由同一未获信任的调用方同时自填后自证可信 | UNBOUND / HOLD；不回填观察，不将刺激或引用字符串相等当作实际证据 |
| DSP004-R-02 | B-01 准备根与启动信任 | Manifest 生成前已经批准的 PROJECT_ROOT、VENV_ROOT、RUNTIME_ROOT、SYSTEM_ROOT 来源；解析器、大小写/重解析规则、允许读取目的/阶段、完整性基础及剩余限制；缺失事实需单独处置 | OPEN；硬编码路径和文件 SHA 不替代可信根，也不使用未来运行授权追补过去的准备资格 |
| DSP004-R-03 | B-02 正式 typed contract 与完整数组政策 | 每个正式成员、类型、可空性、数值范围和数组路径的明确政策；唯一 ORDERED / SET_SORTED 规则及来源；固定源码/政策版本的独立审查与批准；detached 的外部权威绑定 | OPEN；现有玩具投影不可冒充正式全合同；不得自行补定义后宣布已接受 |
| DSP004-R-04 | 设计与接受记录的最终关联 | 精确 SHA 的既有会话决定及对应记录处置；若已在别处完成，提供本项目路径或完整原文供核对 | 保留已有有限采纳，不重复签发或追溯改写；本轮不推断所有历史决定不存在 |
| DSP004-R-05 | 当前完整输入、比较映射及 Harness | 当前设计对下的完整输入候选与观察限制处置、原生结果/Fixture 映射、精确 Harness 源码与其接受，独立来源与固定调用归属 | 不覆盖旧同名输入，不把 189 项合成检查拼成正式输入准入，不从输入数据导入任意模块/函数 |
| DSP004-R-06 | 依赖与跨进程完整性 | 引用/冻结语义、调用侧/被调用侧身份、完整解析及导入闭包、T0 / PE / OS 证据、检查到使用期间防替换依据 | 保持 LIMITED；私有 -I -S -B 子进程及模块槽位删除不等于生产可信装载 |
| DSP004-R-07 | 实际停止与清理限制处置 | 对同步读取、启动、Kill、Close、Dispose、恶意后代等剩余限制的精确处置；允许保留何种 LIMITED 需由 Owner 明确，不能靠声明证明物理硬停止 | 保留原有有限结论与真实失败，不宣称零 I/O、零残留或全部资源结清 |
| DSP004-R-08 | 最终 Manifest、正式运行及关闭决定 | 按已接受准备来源、合同、输入、Harness 和环境顺序生成/审查/接受 Manifest；其后才是精确范围运行授权、运行证据审查及 Owner 关闭决定 | 未授权来源准入、实际业务捕获、集成或部署；不自动触发任何阶段 |

不要求绑定真实姓名、证件或个人信息。稳定职责身份足够；但“手动操作完成”与“已取得来源/权限/完整性证据”仍是不同事实。Gemini 或其他审查模型也不能替 Owner 批准这些事实。

## 5. 自动化在什么位置停住

下列事项不能由本轮协调执行者自动补签：

1. 将任意候选或政策宣告为 Project Owner 已接受。
2. 发明六侧来源、可信根、批准记录或已完成的独立审查。
3. 在事实缺失时，以合成值、历史结果、文件名或同一调用方重算的散列代替实际来源。
4. 为了“跑通”而默默降低覆盖、放开真实来源、改写接受文件、引入真实案件或接入供应商。

本轮已将剩余项收敛到上述决策/事实边界，而不是继续安排不影响准入结论的重复测试。没有生成正式 Manifest、来源准入记录、Owner 签署记录或正式执行结果。

## 6. 一次性后续指示方式（未签署、非授权）

需要 Owner 确定的不是再回复一遍泛化“授权”，而是**结项范围及缺失事实来源**。可明确选择下列一种路径；本文件不会替 Owner 选择：

### 路径 A：只确认本地合成技术准备阶段交付

仅确认已有本地技术证据可作为阶段交付；全部 LIMITED、DSP-004 OPEN / HOLD、B-01 / B-02 OPEN 继续保留。该确认不等于接受全部未接受候选，不将 DSP-004 整体改为 CLOSED，也不准入来源或授权正式运行。

如选择该路径，应单独明确需要接受的资产与固定 SHA；不能用笼统阶段交付自动接受所有源码或归档。此处不预填“SIGNED”“VERIFIED”或接受状态。

### 路径 B：继续正式验证筹备

提供或指向已批准的六侧来源与可信准备根记录，并明确当前 V3.2/V2.2 设计、政策、输入、Harness 的适用处置。可一次列出本项目路径和 SHA；没有记录的项目明确为待设计/待处置，不用真实案件或凭据填充。

获得准确输入后，可批量进行有范围的准备与审查；新增正式政策候选也仍需对应独立审查及 Owner 决定。本路径不因选择本身自动接受资产、生成 Manifest 或执行真实业务。

两条路径都不需要访问独立 ACOS 项目。若已有合规决定仅存在于会话中，可直接提供完整原文，无须重复签署或创建虚构时间。

## 7. 本轮固定身份清单

下列 25 项在本轮核对时均保持指定字节数与 SHA。身份匹配仅说明文件字节一致；并不表示它们全部已获接受、准入或独立审查。本轮不声称重复完成此前七十项或全仓库的逐文件散列复核。

| 本项目路径 | SHA-256 | bytes |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py` | `532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4` | 8234 |
| `validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py` | `F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87` | 9953 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py` | `32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821` | 5799 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py` | `944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476` | 13142 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_LOCAL_RUN_REV1.ps1` | `20AD3881CB7EAD15930290537AE1921B617909F51D950CC21704C6695D2612E2` | 10172 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_DETACHED_PROJECTION_BINDING_PLAN_REV1.md` | `BC93B49AF201F8E33D04CC477BA7CEA7EF5376CF55F71930B04C984680FE3939` | 6803 |
| `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_REV1_OBSERVED_RESULT.json` | `5F3755FC6CB37BE210710FC8CB0287ABB0EDDAC6CEF550F9A7F557081701B63C` | 10762 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_DETACHED_PROJECTION_BINDING_RESULT_REV1.md` | `CF972802BF1E75C5EFF32AAD04C9DB46F860FD3CE27086562B022655475BF6A4` | 9331 |
| `validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_SENSITIVITY_REV1.ps1` | `70B28D732BCB5FF1B34673E6A23835469FF981D2A15AB719A6960D9A3C225140` | 24249 |
| `validation/route_b_c03/wp_008/RDM_CANON2_BINDING_PREDECLARED_MUTATION_REV1.ps1` | `B2B3BB909BEF11D8E108AFC0ADBE6F1363667E93AA6C41EA4EB1A84FEAE9B524` | 28475 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_BINDING_MUTATION_PLAN_REV1.md` | `3A27572851A291154D09500AE3CD45C4252E0200EFF4C5C6309589F107A2B676` | 6715 |
| `validation/route_b_c03/wp_008/RDM_CANON2_BINDING_MUTATION_REV1_OBSERVED_RESULT.json` | `8718C5FFD58AE45A52C38CC845FE9B78D1441C9B37A636F08EBD2949C9A4570F` | 30700 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_CANON2_BINDING_MUTATION_RESULT_REV1.md` | `C6510FB95B91DCA3ABE52031C270BEE368F971A20D82ADF607A50A99F19045E3` | 8992 |
| `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_RECORD_ACCEPTANCE_DECISION.md` | `F45ED18D9E314B84F7A6A724F5C96DF1C9030C9102C29432A19A4DC4CD680FDE` | 9693 |
| `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_V3_2_V2_2_DESIGN_PAIR_ADOPTION_RECORD.md` | `D52E1485B7D0690720B5051827BDE9B19CB6E4DEAE92564FDFE1188FEB67EEDB` | 5902 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_EVIDENCE_COVERAGE_AND_READINESS_REV1.md` | `C4C49EEAA12A9D725CD1F98DE509988025D272AA59FEBD6F94DEDD332109CEE9` | 14476 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | 68768 |
| `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` | 107849 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md` | `87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD` | 54109 |
| `validation/route_b_c03/wp_008/DSP_004_EVIDENCE_ARCHIVE_RECONCILIATION_REV1.ps1` | `2AF0A8E2902AF838FC5A60DBAE92DA0D47C211A2F1CAC45BA4CEEA6BDF1CD035` | 19604 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_OPERATIONAL_VALIDATION_PLAN.md` | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` | 23939 |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md` | `6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA` | 54703 |
| `validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_REV1_OBSERVED_RESULT.json` | `18F9B9068B319D37B5547339A738A27DB71FE53A350992F7D85E01E1AF81B7B0` | 6370 |
| `validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_REV1_OBSERVED_RESULT.json` | `CE536D6E21163D6C585C6F845F5D49E8F20DE77C30CF4125D2060CEACEB052E1` | 7035 |
| `validation/route_b_c03/wp_008/RDM_CANON2_PREDECLARED_MUTATION_REV1_OBSERVED_RESULT.json` | `C3297E81CF3A69662F045E5C074CF48DA3F390B157A246757695A3A5B7797425` | 44253 |

本文件自身不嵌入自身散列，身份由之后的交付核对及普通阶段备份提交绑定。备份只保存本项目现状，不构成上述任何接受、来源准入、LIMITED 消除或 DSP-004 关闭决定。
