# DSP-004 FA-06 剩余 LIMITED 登记候选 REV1

本文件是路径 B 下的 FA-06 剩余 LIMITED 登记候选。它只列出库内已经写明的依赖、启动、隔离或 LIMITED 条目。它不处置任何一条，不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。`DSP004-FA-06` 仍是 `未建立充分前提`。本登记不把它改成完成。

## 1. 形成基准

| 项目 | 本登记的事实 |
| --- | --- |
| 形成时 `HEAD` | `2a9636f45aa12bcfd9edefb045f6e764b6acfc29` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV5.md` |
| 前一增量说明 SHA-256 | `C2F5B4BDF7B637D53E05C806E5BD967450EBFA8BB5BB69909EF4EE80A4B0178B`（5729 字节） |
| 前一增量 JSON SHA-256 | `32527B68DAA54A5763473AF4488DA19653778B5A85BE41CF585FE7C4BFC902ED`（4678 字节） |
| 机器可读登记 | `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` |
| 该登记 SHA-256 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` |
| 该登记字节 | 38377 |
| 受测模块导入或执行 | 未进行 |
| `identity_gate` 调用 | 未进行 |
| Fixture 或场景运行器 | 未运行 |
| 历史虚拟环境或工具缓存 | 未读取 |
| 商业 P0 | 未执行，未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次只用本机对点名文件做字节散列，并读取已经写明的条目标题。没有导入捕获候选、合同模块、场景运行器或受测模块。没有执行 Fixture。没有创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。该路径在本工作区不存在。

## 2. 一行怎么定

先散列、再阅读。点名来源按授权顺序核对：Plan V2、V2.1、V2.2，两文件缺失记录，可信导入有限修订提案，两份 `V003_LIMITED_*`，RDM-DSP-002 有限主体设计。然后只在 `docs/phase2/route-b/` 与 `validation/route_b_c03/wp_008/` 里补上已经分条写出的依赖、启动、隔离或 LIMITED 条目。

同一来源内保持原表顺序。不按字母重排，不把静态核对里的四项提及顺序插到正文之前。不新编条目号。不把任一条标成已处置、已豁免或已关闭。

证据状态只用这三字，并且都不是处置：

| 状态 | 含义 |
| --- | --- |
| `EVIDENCE_PRESENT_UNACCEPTED` | 条目原文在库，该证据没有被接受为 FA-06 的完成或处置 |
| `EVIDENCE_ABSENT` | 来源写明所需证据、文件或观察不存在；本登记不补造 |
| `REQUIRES_RUNTIME_ROOT` | 来源写明没有运行根就不能定位或证明；本登记不读取历史虚拟环境或工具缓存 |

登记 61 行。`EVIDENCE_PRESENT_UNACCEPTED` 35 行，`EVIDENCE_ABSENT` 16 行，`REQUIRES_RUNTIME_ROOT` 10 行。`Disposed` 全部为 false。

下列点名文件已散列、已阅读，没有 LIMITED 条目，所以不入行：

| 路径 | 字节 | SHA-256 | 不入行的原因 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_VENV_TWO_FILE_ABSENCE_REV1.md` | 2536 | `8272F12D37A625455B9CC80962C504285D47E67794BB2CAC750E9684A6B72AAE` | 没有 LIMITED 条目。两路径不存在仍只属于 FA-02，不改写成依赖处置。 |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_VENV_TWO_FILE_ABSENCE_REV1.json` | 1965 | `D8142F5B8CFF55BE0AE26F652A7A09D86BC2E6172DC592D62D9230260A115E97` | 没有 LIMITED 条目。两路径不存在仍只属于 FA-02，不改写成依赖处置。 |

`validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_STATIC_CHECK.md` 已散列。它点名的四项 LIMITED 是 `C03-WP008-V3-RQ-021`、`C03-WP008-V3-G-017`、`C03-WP008-RDM-V2-RQ-018`、`C03-WP008-RDM-V2-G-014`。这四项的标题已经写在 V3.2 与 Plan V2.2 里，下面各记一次。静态核对不另增第五项。

只写“全部 LIMITED 保留”而没有单独条目的文件不入行。可信导入提案里的 `LR-06` 至 `LR-12` 仍在原表，主题是输入绑定和比较分离；本登记不把它们改写成依赖条目，也不处置它们。Plan 的 `RDM-V2-01` 至 `RDM-V2-05`、V-003 静态核对第 5 节的其余未完成行、以及 RDM-DSP-002 的其余审查问题，同样留在原处，不处置。

来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 只提供已经写下的 `RUNTIME_ROOT` 单元格。本登记不是该 SHA 的第二份设计复核。

## 3. 登记

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_CANDIDATE.md`

36436 字节，`F3C3DCA20F5FC0AB22A38F61B5A6C2EE9B437AD949C18E93E27CB0D550AF0B4C`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Current materialization authority` | CONVERSATION-LEVEL PROJECT OWNER “授权” FOR LIMITED DESIGN REVISION CANDIDATES | LIMITED DESIGN REVISION CANDIDATES | `EVIDENCE_PRESENT_UNACCEPTED` |
| `RDM-V2-06` | Authorize static Manifest generation with accepted input, harness, runtime roots and origin-policy evidence | NOT AUTHORIZED | `REQUIRES_RUNTIME_ROOT` |
| `RDM-V2-07` | Generate one new Manifest candidate and compute its file SHA | NOT AUTHORIZED / BLOCKED | `EVIDENCE_ABSENT` |
| `RDM-V2-08` | Review exact file/operation/input closure and obtain detached fixed-SHA acceptance | NOT AUTHORIZED / NOT ESTABLISHED | `EVIDENCE_ABSENT` |
| `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority | BLOCKED | `REQUIRES_RUNTIME_ROOT` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_1_CANDIDATE.md`

38995 字节，`07FD553F641CF52EF54FABFCFAD448CC2D432C8A0279082E6DB899EB8C900910`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Prior joint review disposition` | LIMITED CLARIFICATION REQUIRED — DESIGN ACCEPTANCE / INPUT ADMISSION SEQUENCING; NO ACCEPTANCE | NO ACCEPTANCE | `EVIDENCE_PRESENT_UNACCEPTED` |
| `RDM-V2-06` | Authorize static Manifest generation with accepted input, harness, runtime roots and origin-policy evidence | NOT AUTHORIZED | `REQUIRES_RUNTIME_ROOT` |
| `RDM-V2-07` | Generate one new Manifest candidate and compute its file SHA | NOT AUTHORIZED / BLOCKED | `EVIDENCE_ABSENT` |
| `RDM-V2-08` | Review exact file/operation/input closure and obtain detached fixed-SHA acceptance | NOT AUTHORIZED / NOT ESTABLISHED | `EVIDENCE_ABSENT` |
| `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority | BLOCKED | `REQUIRES_RUNTIME_ROOT` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md`

54703 字节，`6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Latest joint review of V3.1 / V2.1` | LIMITED — B-01 PREPARATION ROOT BINDING / B-02 UNIQUE BYTE ENCODING; CONVERSATION-LEVEL REVIEW, NO REVIEW FILE OR HASH ASSERTED | NO REVIEW FILE OR HASH ASSERTED | `EVIDENCE_PRESENT_UNACCEPTED` |
| `RDM-V2-06` | Before generation, separately authorize and accept exact preparation root-binding sources and the complete typed encoding/array-order policy; then authorize static Manifest generation with accepted input, harness, environment and origin-policy evidence | NOT AUTHORIZED / ROOT AND ENCODING PREREQUISITES NOT ESTABLISHED BY THIS DOCUMENT | `REQUIRES_RUNTIME_ROOT` |
| `RDM-V2-07` | Generate one new Manifest candidate and compute its file SHA | NOT AUTHORIZED / BLOCKED | `EVIDENCE_ABSENT` |
| `RDM-V2-08` | Review exact file/operation/input closure and obtain detached fixed-SHA acceptance | NOT AUTHORIZED / NOT ESTABLISHED | `EVIDENCE_ABSENT` |
| `RDM-V2-09` | Establish separately accepted environment/startup/network assurances and exact run authority; reference and recheck the already accepted preparation root bindings and completed Manifest, not create the root source retroactively | BLOCKED | `REQUIRES_RUNTIME_ROOT` |
| `C03-WP008-RDM-V2-RQ-018` | Has materialization remained document-only, without a Manifest, harness, input binding or evidence? | Twenty-five DESIGN-REQUIREMENT criteria for a later authorized review | `EVIDENCE_PRESENT_UNACCEPTED` |
| `C03-WP008-RDM-V2-G-014` | No Manifest, concrete input, harness, execution or evidence materialized | no PASS is asserted | `EVIDENCE_PRESENT_UNACCEPTED` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_TRUSTED_IMPORT_AND_INPUT_BINDING_LIMITED_REVISION_PROPOSAL.md`

27557 字节，`AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `TI-001` | harness 与 subject 源码继续禁止任意 `eval`、`exec`、动态模块名、用户可控加载器、路径发现及未登记依赖；不增加通用动态执行接口。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-002` | 正常字面量导入必须同时绑定模块名、规范路径、文件 SHA、loader 类别、来源父模块及导入阶段；built-in/frozen 模块绑定精确解释器身份与其类别，不能以缺少文件为由任意放行。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-003` | 静态 AST 解析只针对已绑定的 harness/subject 文本；只生成语法树，不执行解析对象。解释器为解析或正常导入产生的事件须与任意代码输入分开判定。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-004` | `dataclasses` 内部方法生成只能作为精确来源的窄例外候选：固定标准库 SHA、已审查的内部调用路径、已绑定类声明及字段定义、受控生成内容与命名空间、限定导入阶段。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-005` | 不能仅凭模块名称、路径前缀、调用栈文本、`co_filename`、`<string>` 或事件名授予例外；这些标记不能单独证明代码来源。未能建立来源证据则阻断。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-006` | fixture、输入绑定数据、CLI 或环境输入不得控制模块名、源码片段、字段定义、默认工厂、注解表达式或生成命名空间。受控生成代码不能来自运行中的场景数据。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-007` | 未列明的标准库动态行为不得顺带放行。递归依赖需要同样的精确归因；无法静态界定的路径保持阻断，而不是扩大到整个 Lib、site-packages 或目录。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `TI-008` | 所有阶段继续禁止网络、子进程、任意文件访问及权限扩展；可信导入例外只解释必要导入/生成行为，不增加上述能力。 | 待审议设计，尚未成为新的执行规则 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `T0` | 环境与启动身份 | 无对应可核实来源或文件替换防护时阻断；本轮不建设该环境。 | `EVIDENCE_ABSENT` |
| `T1` | 最小可信 bootstrap | 未登记导入、未绑定 loader 或保护初始化失败时停止。 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `T2` | preflight | 身份、来源、输入或策略缺失时停止，不能进入 T3。 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `T3` | 受控 subject 导入 | 意外导入、代码生成或来源不清时停止，场景仍为 NOT RUN。 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `T4` | 场景调用 | 出现未批准的延迟导入或动态行为即停止，不能临时扩张白名单。 | `EVIDENCE_PRESENT_UNACCEPTED` |
| `LR-01` | 仅涉及可信导入与具体输入绑定；没有修改 subject 或创建运行产物。 | PENDING REVIEW | `EVIDENCE_PRESENT_UNACCEPTED` |
| `LR-02` | 启动依赖、AST 解析、正常导入、dataclass 内部生成、任意代码执行相互区分。 | PENDING REVIEW | `EVIDENCE_PRESENT_UNACCEPTED` |
| `LR-03` | 导入例外固定到文件/解释器身份、来源、内容和阶段；不依赖可伪造标签单独判信任。 | PENDING REVIEW | `EVIDENCE_PRESENT_UNACCEPTED` |
| `LR-04` | 无保护预导入不能绕过约束；T0/bootstrap 的信任根和未覆盖风险明确。 | PENDING REVIEW | `EVIDENCE_PRESENT_UNACCEPTED` |
| `LR-05` | audit hook 不被宣称为独立沙箱；网络/环境隔离仍为独立必要条件。 | PENDING REVIEW | `EVIDENCE_PRESENT_UNACCEPTED` |

### `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_DRAFT.md`

17452 字节，`9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `V-003 有限比较规则草案` | PROPOSED_NOT_REVIEWED_NOT_ACCEPTED | 静态自检不等于独立审查、规则接受、输入准入、执行或限制项关闭 | `EVIDENCE_PRESENT_UNACCEPTED` |

### `validation/route_b_c03/wp_008/V003_LIMITED_COMPARISON_RULE_STATIC_CHECK.md`

14449 字节，`A46CCD928EE8CC4EB46D6BEBCBCF7CF53176EF2BF6ACC1116BDCDFBB9309A1D5`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Python 导入、编译、构造与场景执行` | NOT RUN IN THIS TASK | 无实际返回值、异常或分支到达证据 | `EVIDENCE_ABSENT` |
| `Harness、完整依赖与执行方案` | NOT APPROVED BY THIS TASK | 仍需既定独立准入与执行授权 | `EVIDENCE_ABSENT` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL.md`

19838 字节，`85D7A4029D9667EFF7922CEDAA19570A7C6A68F36C2D6A66401F291B5F135A24`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Artifact type` | LIMITED SUBJECT DESIGN PROPOSAL ONLY | LIMITED SUBJECT DESIGN PROPOSAL ONLY | `EVIDENCE_PRESENT_UNACCEPTED` |
| `DSP002-RQ-018` | Are Harness, Manifest, evidence and Python execution excluded? | Proposal Review Questions | `EVIDENCE_PRESENT_UNACCEPTED` |
| `DSP002-G-018` | No source, binding, Harness, Manifest, evidence or execution materialized | Proposal Acceptance Gates | `EVIDENCE_ABSENT` |
| `RDM-DSP-002` | OPEN — PROPOSED LIMITED DESIGN ROUTE ONLY | MATERIALIZED — REVIEW NOT AUTHORIZED / NOT PERFORMED | `EVIDENCE_PRESENT_UNACCEPTED` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_OWNER_DECISION_PACKET_REV1.md`

8630 字节，`9B0A3C048E479B714083952E76CF6620A2AE046EA23D2CC95192D967CF5A6736`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `DSP004-FA-06` | 导入闭包、两侧调用身份和检查到使用的保护未建立。运行依赖 Manifest 仍不存在。 | 依赖与隔离 LIMITED 全部保留，不创建 PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json。 | `EVIDENCE_ABSENT` |
| `DSP004-R-06` | 引用/冻结语义、完整解析、导入闭包、T0 / PE / OS 证据和检查到使用的防替换依据仍缺。 | 保持 LIMITED；私有子进程和模块槽位删除不等于生产可信装载。 | `EVIDENCE_ABSENT` |
| `DSP004-R-07` | Owner 尚未写明哪些停止与清理 LIMITED 可以保留。同步读取、启动、Kill、Close、Dispose 和后代清理都未证明。 | 保留全部既有停止与清理 LIMITED，不宣告零 I/O、零残留或物理硬停止。 | `EVIDENCE_PRESENT_UNACCEPTED` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_REMAINING_WORK_HANDOFF_REV1.md`

14774 字节，`538283D7E48520B56B90ACA42A705A43AFEA468AF6DE8B7A46AE34636A3805AA`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `DSP004-R-06` | 依赖与跨进程完整性 | 保持 LIMITED；私有 -I -S -B 子进程及模块槽位删除不等于生产可信装载 | `EVIDENCE_ABSENT` |
| `DSP004-R-07` | 实际停止与清理限制处置 | 保留原有有限结论与真实失败，不宣称零 I/O、零残留或全部资源结清 | `EVIDENCE_PRESENT_UNACCEPTED` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md`

21257 字节，`57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `RUNTIME_ROOT` | 完整依赖来源、闭包或检查到使用保护 | 不能据此认定 | `REQUIRES_RUNTIME_ROOT` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_1_CANDIDATE.md`

49702 字节，`3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Prior joint review disposition` | LIMITED CLARIFICATION REQUIRED — B-01 / NB-01; NO ACCEPTANCE | NO ACCEPTANCE | `EVIDENCE_PRESENT_UNACCEPTED` |

### `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md`

54109 字节，`87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `Latest joint review of V3.1 / V2.1` | LIMITED — B-01 PREPARATION ROOT BINDING / B-02 UNIQUE BYTE ENCODING; CONVERSATION-LEVEL REVIEW, NO REVIEW FILE OR HASH ASSERTED | NO REVIEW FILE OR HASH ASSERTED | `EVIDENCE_PRESENT_UNACCEPTED` |
| `C03-WP008-V3-RQ-021` | Does this materialization create only design candidates, not a harness, input data, Manifest, attestation or execution evidence? | These are DESIGN-REQUIREMENT criteria only | `EVIDENCE_PRESENT_UNACCEPTED` |
| `C03-WP008-V3-G-017` | No execution artifact or concrete input materialized by this design revision | none is a current PASS | `EVIDENCE_PRESENT_UNACCEPTED` |

### `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/README.md`

5952 字节，`BBAD8F847687531313C42F188AFDB24A2B9DAF645D9D7BDD6CFEFC06F19A0F64`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `保留 LIMITED` | 完整依赖来源、检查到使用期间保护、未观察调度和同步原生调用、host 强制终止后的原生错误对象持久性、完整 189 项计划、D-007 业务来源路径、业务正向 SHA 分支、正式来源准入和后续集成/部署。 | 不得把本地合成补充覆盖算作这些限制的自动解除 | `EVIDENCE_PRESENT_UNACCEPTED` |

### `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/RESUMPTION_RESULT.md`

7419 字节，`2705BBDF9AAFC580DF6AE09EC51BC887011D54496E1296A8C243B367BAA8658A`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `LIMITED / 未覆盖` | 完整依赖来源与检查到使用保护、未观察调度、同步原生调用、强制死亡后的错误对象持久性、完整 189 项计划、D-007 业务路径与正向业务 SHA 分支均保留 LIMITED / 未覆盖 | 不借本次合成场景自动解除 | `EVIDENCE_PRESENT_UNACCEPTED` |

### `validation/route_b_c03/wp_008/dsp004_execution_batch_rev1/attempt_02_result.json`

50434 字节，`967B146EA3DECC79106DE191D83C79934BF16CDB8161B6230DBB8EECCF53D148`。

| 条目 | 标题 | 来源所写状态 | 证据状态 |
| --- | --- | --- | --- |
| `FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE` | FULL_DEPENDENCY_PROVENANCE_AND_CHECK_TO_USE | remaining_limited | `REQUIRES_RUNTIME_ROOT` |
| `UNOBSERVED_OS_SCHEDULES_AND_NATIVE_SYNCHRONOUS_CALLS` | UNOBSERVED_OS_SCHEDULES_AND_NATIVE_SYNCHRONOUS_CALLS | remaining_limited | `EVIDENCE_ABSENT` |
| `DURABLE_NATIVE_ERROR_PRESERVATION_AFTER_HOST_DEATH` | DURABLE_NATIVE_ERROR_PRESERVATION_AFTER_HOST_DEATH | remaining_limited | `EVIDENCE_ABSENT` |
| `FULL_189_INPUT_PLAN_AND_D007_BUSINESS_SOURCE_PATH` | FULL_189_INPUT_PLAN_AND_D007_BUSINESS_SOURCE_PATH | remaining_limited | `EVIDENCE_PRESENT_UNACCEPTED` |
| `FORMAL_SOURCE_ADMISSION_ACCEPTANCE_INTEGRATION_DEPLOYMENT` | FORMAL_SOURCE_ADMISSION_ACCEPTANCE_INTEGRATION_DEPLOYMENT | remaining_limited | `EVIDENCE_ABSENT` |
| `full_dependency_provenance` | LIMITED | runtime_after | `REQUIRES_RUNTIME_ROOT` |
| `full_dependency_provenance` | LIMITED | runtime_before | `REQUIRES_RUNTIME_ROOT` |

## 4. 本登记故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 与 B-02 保持 `OPEN`。
- 不把 `DSP004-FA-06` 标成完成。它仍是 `未建立充分前提`。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不改商业 P0。
- 三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。
- REV1 点名的七个 `DSP_004_CAPTURE_RESULT_*` 仍是 `NOT_SELECTED` / `NOT_ADMITTED`。本登记不装载它们，也不挑选它们。

## 5. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 哪些依赖、启动、隔离、停止与清理 LIMITED 可以保留
- 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权和已经绑定的捕获入口
- 是否对两个 REV3 SHA 作固定 SHA 接受
- 是否对四项保留的 LIMITED 审查项作消除或继续保留
- Manifest、正式运行和 DSP-004 关闭

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。
