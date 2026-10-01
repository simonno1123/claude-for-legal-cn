# Route B C03 WP-008 DSP-004 设计准备记录 — REV1

## 1. 记录身份、效力与本次授权

- Project: `claude-for-legal-cn`
- Record: `DSP-004 PREPARATION DESIGN RECORD — REV1`
- Record Type: `DESIGN PREPARATION RECORD ONLY`
- 唯一物化文件：`docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md`
- 新物化文件状态：`MATERIALIZED — RECORD REVIEW / ACCEPTANCE NOT ESTABLISHED`
- 本次检查性质：静态完整性与来源 SHA 比对；不是新的独立复核、运行验证或文件接受。
- 历史三份正文的采纳效力：仅限其各自会话层有限设计正文；不自动转移为本物化记录的接受。
- 可信来源绑定、受控捕获、可运行比较规则接受与整体输入准入：`NOT ESTABLISHED`
- DSP-004：`OPEN / HOLD`；B-01 / B-02：`OPEN`
- 输入候选保留状态：`PARTIAL_OBSERVABLE / NOT_RUN`
- 自动下游转换：`BLOCKED`

### 1.1 本次物化授权依据

本记录仅根据下列会话层授权创建；不将“物化”解释为任何下游接受或运行权。

| 要素 | 会话记录 |
| --- | --- |
| 授权草案 writing block | `41752` |
| 授权草案 turn | `01a0f55c-f7e7-7391-a3e7-983f23c2dc4a` |
| 授权草案 message | `msg_050c32c7e9d0b59a016abdca9db4988198a75cea4a1491fc81` |
| Project Owner 本轮明确指令 | 授权物化上述唯一设计准备文档 |
| 指令 turn | `01a0f67d-c52a-7593-959b-281893be7a97` |
| 唯一输出 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md` |
| 允许操作 | 创建此文档、静态完整性检查、计算 SHA-256 |
| 不允许操作 | 修改现有源码、输入、Fixture；创建运行证据；运行 Python / Harness / 测试 / 场景；真实事项或供应商接入；独立 ACOS 项目操作 |
| 不产生的效力 | 新文件接受、来源绑定、可运行比较规则接受、输入准入、DSP-004 或 B-01 / B-02 关闭、提交、推送或下游阶段启动 |

本次仅访问本项目明确列出的固定来源和本会话记录，不访问或修改独立 ACOS 源项目。本文不记录真实人物信息。

### 1.2 原文保留方法与来源限定

本记录将四层信息分开保存：形成时正文、后来发布的复核结论、Project Owner 会话指令及其有限采纳确认、本次新物化记录。

- 第 3 节展示三份完整形成时正文；不把原文中的 `NOT REVIEWED / NOT ACCEPTED`、未物化、未授权等历史声明改成后来状态。
- 第 4 节保存已发布的独立只读复核结论原文。它们是本会话发布的结论，不冒称独立子审查员完整工作轨迹。
- 第 5 节分开保留采纳决定形成时模板、后来的用户指令和会话确认。模板内 `PENDING` 等字段是形成时快照，不是本轮状态。
- 第 7 节保存 JSON 字符串形式的无损快照。JSON 解码后的字符串保留原始正文的换行、行尾空格及标点；不将其当作物理源文件或独立源文件 SHA。
- 可读展示副本只移除各行行尾空格 / Tab，以满足仓库无行尾空白规则，不删减、翻译、替换或补充正文内容。精确原文以第 7 节解码结果为准。
- 本文中的 turn / message / writing block 标识仅用于本会话定位，不是治理时间戳，也不构成时间链或外部执行事实证明。
- 本文不填造来源身份、版本、捕获结果或运行时间；本文件 SHA 在创建后另行计算并交付，不嵌入自身内容。

## 2. 固定来源身份与 SHA

以下七项是本次静态比对的明确来源。SHA 一致只证明这些本地文件内容与记录的固定值一致，不证明拟议来源已受控绑定、原生合同已实现或场景已运行。

| 来源角色 | 本项目文件 | 固定 SHA-256 |
| --- | --- | --- |
| 当前输入候选 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` |
| 原始四边界联合 Fixture | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/validation/route_b_c03/wp_008/fixtures/C03-TA-V-004.json` | `9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8` |
| 现有原生合同 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/scripts/phase2_runtime/route_b_c03/contracts.py` | `7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4` |
| 现有身份门禁 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/scripts/phase2_runtime/route_b_c03/identity_gate.py` | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` |
| 现有 Provider 端口 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` |
| 现有隔离合同 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` |
| 现有能力合同 | `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5/scripts/phase2_runtime/route_b_c03/capability.py` | `028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5` |

本次未修改以上来源。本文不将历史来源比对扩张为合成来源准入或真实供应商身份验证。

## 3. 三份设计形成时完整正文

下列形成时声明保留原有历史含义。正文中的“文件物化未授权”描述当时边界；本轮只单独授权了本文这一个准备记录，不追溯改变旧授权或旧正文。

### 3.1 原文 A：RDM-DSP-004 会话层边界细化设计 — REV3

| 原文定位 | 标识 |
| --- | --- |
| writing block | `86310` |
| turn | `01a0f05b-876c-75e2-8c3d-6aca7df416af` |
| message | `msg_050c32c7e9d0b59a016abc8235e4788198a9b77d103417533f` |

<!-- DSP004 ORIGINAL A READABLE BEGIN -->
````markdown
# RDM-DSP-004 会话层边界细化设计 — REV3

状态：`REVISED DESIGN CANDIDATE — CONVERSATION ONLY / NOT REVIEWED / NOT ACCEPTED`
对象：`C03-TA-V-004` 的 Project、Session、Provider 三项边界。

绑定输入候选 SHA-256：
`A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`

绑定原始 fixture SHA-256：
`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8`

本版仅固定 REV2 中尚不明确的原生类型、无效引用与构造失败分界，以及旧门禁所有非准入分支的观察规则。REV2 的可信来源缺口、原 fixture 保真、实际效果限度及禁止自动下游转换要求均保留。

## 1. 可信来源仍未绑定

Project、Session、Provider 各需受控的预期引用与本次调用引用。两侧来源身份须分别绑定于同一受审调用，不得由调用方自填两侧值来自证匹配。引用仅使用不含真实事项、个人信息、凭据、Token、路径或外部地址的合成标识，并按原值精确比较，不作裁剪或别名替换。

**现有源码没有这三组已绑定来源。** 来源身份及适用范围另行审查前，对应观察只能为 `UNBOUND`，不得因值恰好相同而记为 `MATCH`。NullProvider 的禁止调用结果不是供应商身份匹配证据。

## 2. 拟议原生类型合同

以下均为**未来实现须另行授权的设计类型**，不是现有源码中已经存在的类或观察。拟议类身份固定归属本项目 `route_b_c03.contracts` 合同层；若未来选择其他归属，须作为设计变更复核。

| 拟议原生类型 | 精确要求 |
| --- | --- |
| `BoundaryKind` | 原生枚举；仅 `PROJECT`、`SESSION`、`PROVIDER` |
| `BoundaryCheckState` | 原生枚举；仅 `MATCH`、`MISMATCH`、`UNBOUND`、`NOT_EVALUATED` |
| `BoundaryCheckCause` | 原生枚举；仅 `EXACT_EQUAL`、`EXACT_UNEQUAL`、`SOURCE_UNBOUND`、`INVALID_REFERENCE_TYPE`、`PRIOR_DENIAL` |
| `BoundaryCheck` | 拟议不可变对象，字段依次为 `boundary: BoundaryKind`、`state: BoundaryCheckState`、`cause: BoundaryCheckCause`、`audit_correlation_id: str`、`expected_source_id: str \| None`、`actual_source_id: str \| None` |
| 三项观察序列 | 原生 `tuple`，长度严格为 3，元素原生类型严格为 `BoundaryCheck`，顺序严格为 `PROJECT → SESSION → PROVIDER` |

`MATCH` 与 `MISMATCH` 必须有两侧各自已受控绑定的非空原生字符串来源身份。来源身份字段本身不能由调用方自我声明为可信。`UNBOUND` 与 `NOT_EVALUATED` 可以用原生 `None` 表示未取得的来源身份；不能以空字符串或 JSON `null` 投影冒充已核验原生对象。

状态和原因必须成对出现：

| 状态 | 允许原因 |
| --- | --- |
| `MATCH` | `EXACT_EQUAL` |
| `MISMATCH` | `EXACT_UNEQUAL` |
| `UNBOUND` | `SOURCE_UNBOUND` 或 `INVALID_REFERENCE_TYPE` |
| `NOT_EVALUATED` | `PRIOR_DENIAL` |

组合门禁拟复用现有 `route_b_c03.contracts.GateDecision` 与 `route_b_c03.contracts.InvocationState` 的原生类身份。其四字段须逐项核验：原生 `InvocationState` 枚举、原生非空 `str` 原因、原生非空 `str` 关联引用、原生空 `tuple` 写入命名空间声明。现有 dataclass 类型注解本身不构成运行时类型核验；JSON 字符串枚举或 `[]` 不可替代这些原生值。

## 3. 无效引用与构造失败的分界

1. 若现有配置、授权包、输入信封或预期身份对象无法构造，或者信封的关联引用无法取得有效原生字符串：记录 `CONSTRUCTION_FAILURE`。**不生成**三项观察序列或 `GateDecision`，也不补写预期结果。
2. 若上述现有对象均有效、关联引用有效，但补充边界的来源尚未受控绑定或缺失：为对应边界生成原生 `UNBOUND / SOURCE_UNBOUND` 观察。
3. 若来源已受控绑定，但捕获到的补充引用不是原生 `str`、为空或仅为空白：在构造补充观察对象**之前**将该原始引用判为无效，为对应边界生成原生 `UNBOUND / INVALID_REFERENCE_TYPE` 观察；不得将它伪装为两侧引用错配。
4. 若补充观察对象本身无法按第 2 节的原生类型合同构造：记录 `CONSTRUCTION_FAILURE`，不输出伪造的三项序列或 `GateDecision`。

第 2、3 项只有在旧门禁分支允许补充观察时才执行；旧门禁先行拒绝的处理按第 4 节确定。

## 4. 旧门禁分支的完整观察规则

先取得现有 `evaluate_identity_gate` 的原生结果。下表穷尽其当前返回分支。旧门禁的状态与原因始终保留，不得被补充检查改成允许。

| 现有分支条件 | 三项边界观察及组合效力 |
| --- | --- |
| Kill 生效 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧 `BLOCKED — KILL ACTIVE` |
| 配置缺失或能力禁用 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧能力未激活拒绝 |
| 能力已撤销 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |
| 能力已失效 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧版本失败拒绝 |
| 五项能力身份任一错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧能力身份拒绝 |
| 路由、域或适配合同身份任一错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧域身份拒绝 |
| Tier B 授权包缺失 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权包缺失拒绝 |
| 授权包状态并非 `ACCEPTED` | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |
| 撤销状态不为 `CLEAR` 或有效性未确认 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |
| 事项 ID、事项版本、操作主体三项中的一项或多项错配 | 必须另按第 5 节逐字段区分。仅当事项 ID 或事项版本错配可被独立核对时，才允许形成三项**附加诊断观察**；旧 `REJECTED — ISOLATION FAILURE` 不变。若仅操作主体错配或逐字段条件不可核对，三项均 `NOT_EVALUATED / PRIOR_DENIAL` |
| 目的或操作错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧范围拒绝 |
| 输入集 SHA 错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧输入集身份拒绝 |
| 输出类别不在请求范围 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧输出边界拒绝 |
| 事项授权、执行授权或包决议引用错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权绑定拒绝 |
| `ELIGIBLE_FOR_MAPPING` | 在第 1、3 节条件下执行三项补充观察，并按第 6 节确定组合结果；全匹配仍不授予执行权 |

上表的附加诊断仅表示**拟议补充检查**可分别观察三项，不表示现有身份门禁执行了这些检查。旧门禁在任何非 `ELIGIBLE_FOR_MAPPING` 分支拒绝时，其原生结果不得被附加诊断覆盖。

## 5. 事项边界的逐字段条件

共用原因 `REJECTED — ISOLATION FAILURE` 可能由以下任一比较触发，不能单凭原因字符串归因：

- `packet.matter_id` 与 `envelope.matter_id`；
- `packet.matter_version` 与 `envelope.matter_version`；
- `packet.actor_reference` 与 `envelope.actor_reference`。

只有两侧字段均可核对时才能记录相应的原值 `MATCH` 或 `MISMATCH`。仅操作主体错配不得充当事项边界错配；事项 ID 或版本至少一项错配，才可作为该边界的**候选证据**。原 fixture 对“事项边界”的最终释义及比较映射仍须单独审查，不能由本设计直接确立。

在旧门禁因事项 ID 或版本错配拒绝后，三项补充观察即使全部得出结果，也只是附加诊断；最终原生 `GateDecision` 保持旧拒绝状态和原因。若三项来源未绑定，如实记录 `UNBOUND`，不得宣称原 fixture 四边界均已受检。

## 6. `ELIGIBLE_FOR_MAPPING` 后的确定性优先级

仅对旧门禁已返回 `ELIGIBLE_FOR_MAPPING`、且现有对象与关联引用有效的情形，按下列**互斥顺序**形成拟议组合结果：

1. 任一项 `UNBOUND / INVALID_REFERENCE_TYPE`：原生 `InvocationState.BLOCKED`，精确原因 `BLOCKED — CONTEXT REFERENCE INVALID`。
2. 否则，任一项 `UNBOUND / SOURCE_UNBOUND`：原生 `InvocationState.BLOCKED`，精确原因 `BLOCKED — CONTEXT SOURCE UNBOUND`。
3. 否则，两项或三项 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — MULTIPLE CONTEXT MISMATCHES`。
4. 否则，仅 Project 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — PROJECT CONTEXT MISMATCH`。
5. 否则，仅 Session 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — SESSION CONTEXT MISMATCH`。
6. 否则，仅 Provider 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — PROVIDER CONTEXT MISMATCH`。
7. 三项均为 `MATCH`：保留旧门禁原生 `ELIGIBLE_FOR_MAPPING` 状态及其完整原因。

有效关联引用原样传递；拟议拒绝的允许写入命名空间字段保持原生空元组。这些原因是未来设计合同，不是现有代码输出。`ELIGIBLE_FOR_MAPPING` 只表示仍需其他授权的元数据阶段结果，不许可映射执行或供应商调用。

## 7. 原 fixture、实际效果与后续门禁

后续输入设计仍须分别固定 Project、Session、Provider 单项错配与三项全匹配对照，使待检条件可达。原 fixture 同时记录事项、项目、会话、供应商四项错配，必须作为单独的联合条件保留；三个单项变体不得替代。任何 `UNBOUND` 或 `NOT_EVALUATED` 项都不得被补写为联合条件已通过。

现有门禁原生 `REJECTED` 与 fixture 的 `BLOCKED_ISOLATED` 是不同层级。原生门禁结果、附加观察、fixture 抽象之间的映射仍是**待单独审查的比较规则候选**。元数据匹配、保护性拒绝及原生空写入元组均不证明零实际 I/O、真实项目/会话/供应商隔离，或不存在跨边界披露与状态复用。

本 REV3 只有会话正文，没有物理文件或文件 SHA；尚未经 REV3 只读审查或 Project Owner 接受。当前输入候选仍为 `PARTIAL_OBSERVABLE / NOT_RUN`，`DSP-004` 继续 `OPEN / HOLD`，整体输入未接受、未准入，B-01/B-02 未关闭。

任何源码、输入、fixture、观察合同或比较规则变化均须新 SHA 和另行审查决定。文件物化、代码修改、Python/Harness/场景执行、真实事项处理及独立 ACOS 项目操作均未授权。
````
<!-- DSP004 ORIGINAL A READABLE END -->

### 3.2 原文 B：DSP-004 可信来源绑定与比较规则草案 — REV1

| 原文定位 | 标识 |
| --- | --- |
| writing block | `96524` |
| turn | `01a0f0ef-40f2-7352-acef-d05f8a7734d4` |
| message | `msg_050c32c7e9d0b59a016abca8881b7c819898f4cb74b19822d4` |

<!-- DSP004 ORIGINAL B READABLE BEGIN -->
````markdown
# DSP-004 可信来源绑定与比较规则草案 — REV1

Status:
PREPARED — NOT REVIEWED / NOT ACCEPTED

Scope:
仅细化已采纳的 DSP-004 REV3 设计，不改变其原生类型、旧门禁优先级或权限边界。

Bound Input Candidate SHA-256:
A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430

Bound Original Fixture SHA-256:
9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8

## 1. 可信来源绑定要求

以下是拟议来源角色，不是已存在或已获准使用的来源资产。

| 边界 | 预期引用来源角色 | 实际引用来源角色 | 当前状态 |
| --- | --- | --- | --- |
| Project | 经独立确认的本项目范围基线 | 本次调用入口捕获的项目引用 | SOURCE UNBOUND |
| Session | 经独立确认的合成会话范围基线 | 本次调用入口捕获的会话引用 | SOURCE UNBOUND |
| Provider | 经独立确认的供应商身份范围基线 | 本次调用入口捕获的供应商引用 | SOURCE UNBOUND |

每侧来源后续均须固定：来源身份、版本、完整 SHA、产生者角色、授权依据、取值位置和适用范围。来源记录必须绑定具体变体及同一受审调用，不能仅凭可能重复的关联字符串证明来源属于该调用。

调用方不得通过自填两侧引用建立可信性。来源身份匹配也不等于边界值匹配；必须先确认来源，再比较实际引用。

现有 NullProvider 的禁止调用结果不能替代 Provider 身份证据。当前没有完整来源绑定，因此不得登记三项边界为 MATCH。

仅使用合成元数据，不引入真实事项、个人信息、凭据、Token、文件路径或外部地址。

## 2. 原生观察比较顺序

拟议规则标识：
CR-004-CONTEXT-BOUNDARY-DRAFT-001

1. 核对固定源码、来源、变体和实际返回的对应关系。
2. 检查 REV3 规定的精确原生类、枚举、字段类型及三项元组顺序。
3. 将预期数据、实际观察、类型来源和比较结论分别保留，禁止把预期值复制成实际观察。
4. 对来源已绑定的有效原生字符串进行逐字符比较，不裁剪、翻译、归一化或替换。
5. JSON 仅可作为可逆展示；字符串枚举和空列表不能替代原生枚举与空元组。
6. 缺失观察、类型失败、异常、无返回或未定义状态均停止受影响的比较，禁止补值后给出通过。

构造失败不生成伪造的观察或门禁结果；已经取得的真实旧拒绝结果仍须保留。

## 3. 分离的比较条件

| 条件 | 拟议比较要求 | 与原始 fixture 的关系 |
| --- | --- | --- |
| Project 单错配 | 旧门禁准入；Project 为 MISMATCH，其余两项 MATCH；组合结果为 REJECTED，原因逐字为 `REJECTED — PROJECT CONTEXT MISMATCH` | 单项控制，不代表四边界联合通过 |
| Session 单错配 | 旧门禁准入；Session 为 MISMATCH，其余两项 MATCH；原因逐字为 `REJECTED — SESSION CONTEXT MISMATCH` | 单项控制 |
| Provider 单错配 | 旧门禁准入；Provider 为 MISMATCH，其余两项 MATCH；原因逐字为 `REJECTED — PROVIDER CONTEXT MISMATCH` | 单项控制 |
| 三项全匹配 | 三项均 MATCH；保留旧门禁准入结果及完整原因 | 正向控制，不授予运行权限 |
| 无效引用或来源未绑定 | 严格沿用 REV3 的 UNBOUND 原因与组合优先级 | 不得映射成联合条件通过 |
| actor 单错配 | 保留旧 isolation 拒绝；三项补充观察为 NOT_EVALUATED | 不得充当事项边界错配 |
| 普通旧门禁拒绝 | 保留原生状态、原因；三项为 NOT_EVALUATED | 不得推断补充边界已检查 |
| 原始四边界联合条件 | 事项 ID 或版本错配须逐字段确认；三项补充边界均有受控来源并实际记录 MISMATCH；保留旧 isolation 拒绝，补充结果仅作诊断 | 单独保留，不以单项结果拼成联合运行证据 |

同一比较中的门禁和补充观察须关联同一变体、同一调用。原因、关联引用及写入命名空间声明均按原生类型和值核对，不接受前缀匹配或原因替换。

## 4. 原始 fixture 映射限制

原始期望保持不变：

- expected_state：BLOCKED_ISOLATED
- expected_reason_class：BOUNDARY_MISMATCH
- expected_permitted_write_set：空集合的原有 JSON 表示
- prohibited_effect：CROSS_BOUNDARY_DISCLOSURE_OR_STATE_REUSE

原生 REJECTED 到 BLOCKED_ISOLATED 仅是待审的分类映射，不改变原生返回。

即使分类映射成立，空写入声明仍只是元数据，不能证明没有实际披露、状态复用或其他 I/O。因此不得据此宣布整个 fixture 通过或实际隔离成立。

## 5. 保留状态

可信来源选择与绑定：
NOT ESTABLISHED

比较规则：
DRAFT — NOT ACCEPTED

DSP-004：
OPEN / HOLD

输入候选：
PARTIAL_OBSERVABLE / NOT_RUN

B-01 / B-02：
OPEN

文件物化、源码或输入修改、Harness、Python、场景执行、正式验证、真实事项处理及独立 ACOS 操作：
NOT AUTHORIZED
````
<!-- DSP004 ORIGINAL B READABLE END -->

### 3.3 原文 C：DSP-004 合成来源与取值位置候选 — REV1

| 原文定位 | 标识 |
| --- | --- |
| writing block | `58127` |
| turn | `01a0f50d-0462-7621-9d01-643e4f6c07d4` |
| message | `msg_050c32c7e9d0b59a016abdb6577a688198a6e0f86c0d7074e9` |

<!-- DSP004 ORIGINAL C READABLE BEGIN -->
````markdown
# DSP-004 合成来源与取值位置候选 — REV1

Status:
DESIGN CANDIDATE — NOT REVIEWED / NOT ACCEPTED

适用范围：
仅本项目 C03-TA-V-004 的合成元数据比较，不接入真实案件、会话服务或供应商。

绑定输入候选 SHA-256：
A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430

绑定原始 Fixture SHA-256：
9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8

## 1. 候选来源选择

拟采用两种分别受控的来源：

- 合成边界基线：保存经审查冻结的预期引用。
- 合成调用帧：保存具体变体拟送入调用入口的引用；实际取值须由受控入口捕获，不能从预期基线回填。

两者尚未物化、审查或准入。调用帧中的预填值是测试刺激，不是运行观察。

## 2. 拟议取值位置

下列位置仅为新设计的逻辑字段，不存在于当前门禁参数或输入对象中，不得据此动态导入或查找属性。

| 边界 | 预期来源角色标识／位置 | 实际来源角色标识／拟捕获位置 |
| --- | --- | --- |
| Project | SRC004-E-PROJECT／baseline.project_reference | SRC004-A-PROJECT／frame.project_reference |
| Session | SRC004-E-SESSION／baseline.session_reference | SRC004-A-SESSION／frame.session_reference |
| Provider | SRC004-E-PROVIDER／baseline.provider_reference | SRC004-A-PROVIDER／frame.provider_reference |

拟议全匹配基线引用：

- Project：SYNTHETIC-PROJECT-001
- Session：SYNTHETIC-SESSION-001
- Provider：SYNTHETIC-PROVIDER-001

这些值仅为设计期望，不是实际捕获记录、可信性证明或真实供应商身份。

## 3. 来源成为可用证据的条件

每侧来源均须另行固定身份、版本、完整 SHA、产生者职责、授权依据、取值位置及适用范围。

必须同时满足：

1. 预期基线已冻结，待审调用不能改写它。
2. 实际引用由受控入口取得，禁止以预期值代替。
3. 来源记录关联具体变体、调用尝试及输入快照；仅关联字符串相同不足以证明同一调用。
4. 捕获合同及其固定代码身份经过审查。
5. 来源身份与引用值分别核验；身份匹配不能代替值比较。
6. 产生者职责声明不等于可信性证明；不要求记录真实人物信息。
7. 缺失任何必要绑定时维持 UNBOUND，不虚构 SHA 或补填来源。

现有门禁不会读取这些新字段。未来补充观察适配须单独授权，不得改变已采纳 REV3 的旧拒绝保留、类型合同和判定优先级。

## 4. 比较范围限制

三项单错配、全匹配对照和原始四边界联合条件分别保留。

现有事项 ID、版本、actor 三条变体不修改；actor 不得替代事项边界。

即使未来合成比较通过，也只能证明受控合成输入的元数据比较符合合同，不能证明真实项目、会话或供应商已经隔离。

Fixture 分类映射、事项边界最终释义和实际禁止效果仍需另审。

## 5. 当前效力

本候选只有会话正文，无物理文件或自身 SHA。

SOURCE BINDING：NOT ESTABLISHED
DSP-004：OPEN / HOLD
输入候选：PARTIAL_OBSERVABLE / NOT_RUN
B-01 / B-02：OPEN

文件物化、源码或输入修改、Python/Harness/场景执行、正式验证、真实事项处理及独立 ACOS 操作：
NOT AUTHORIZED
````
<!-- DSP004 ORIGINAL C READABLE END -->

## 4. 对应独立只读复核结论

本节仅保存已经发布的结论，不启动或重做任何审查。三次复核均为同供应商的新上下文独立内部复核，不是跨供应商外审；每次保留的 `8 PASS / 2 LIMITED` 与正文阻断项 0，不等同于实际来源、实现或运行效果通过。

### 4.1 原文 A 的已发布复核结论

- 发布 turn：`01a0f0dd-7f94-7d42-b648-ab475c506174`
- 发布 message：`msg_050c32c7e9d0b59a016abca589531c8198a59720ecbc74595c`

<!-- DSP004 REVIEW A READABLE BEGIN -->
````markdown
DSP-004 REV3 独立只读复核已完成：`PASS — DESIGN TEXT REVIEW ONLY`，尚未接受。

- 七项来源 SHA：`7/7 MATCH`
- 复核领域：`8 PASS / 2 LIMITED`
- 旧门禁全部14个拒绝分支：完整覆盖
- 原生类型、构造失败分界、逐字段归因及组合优先级：通过
- 设计正文阻断项：0；无需进一步文本修订

两项限制继续保留：可信来源及实际隔离效果尚未验证；原生输出到 fixture 的比较映射尚未接受。

本次是同供应商独立子上下文复核，不是跨供应商外审。未修改文件、运行 Python、执行场景或访问独立 ACOS。

REV3 可提交你作有限设计采纳决定。当前仍保持：`DSP-004 OPEN / HOLD`、输入 `PARTIAL_OBSERVABLE / NOT_RUN`，B-01/B-02 未关闭；实现与正式验证未授权。
````
<!-- DSP004 REVIEW A READABLE END -->

### 4.2 原文 B 的已发布复核结论

- 发布 turn：`01a0f4f8-a82e-74e3-ac64-f421a1feedd5`
- 发布 message：`msg_050c32c7e9d0b59a016abdb28852d08198912ab063c38ed00a`

<!-- DSP004 REVIEW B READABLE BEGIN -->
````markdown
REV1 独立只读复核已完成：

`PASS — PREPARATION DESIGN TEXT REVIEW ONLY`

- 七项来源 SHA：`7/7 MATCH`
- 分领域结果：`8 PASS / 2 LIMITED`
- 正文阻断项：0；无需文本修订
- 与已采纳 REV3 的类型、拒绝保留及判定优先级一致

两项限制继续保留：具体可信来源尚未绑定；fixture 映射及实际隔离效果尚未获确认。

本次为同供应商新上下文独立内部复核，不是跨供应商外审。未修改文件、运行 Python 或执行场景。

REV1 可提交你作“准备设计正文”的有限采纳决定，但尚未接受；DSP-004 仍为 `OPEN / HOLD`，输入准入和运行验证仍未授权。
````
<!-- DSP004 REVIEW B READABLE END -->

### 4.3 原文 C 的已发布复核结论

- 发布 turn：`01a0f518-f527-7180-acf6-1d6ede028c94`
- 发布 message：`msg_050c32c7e9d0b59a016abdb9e24d6081989ad803405ef25b31`

<!-- DSP004 REVIEW C READABLE BEGIN -->
````markdown
《DSP-004 合成来源与取值位置候选 — REV1》独立只读复核已完成：

`PASS — PREPARATION CANDIDATE DESIGN TEXT REVIEW ONLY`

- 七项来源 SHA：`7/7 MATCH`
- 分领域结果：`8 PASS / 2 LIMITED`
- 正文阻断项：0；无需修订

两项限制保留：六个来源角色的实际绑定及受控捕获尚未建立；fixture 最终映射与实际隔离效果尚未确认。

本次是同供应商独立内部复核，不是跨供应商外审。未修改文件或运行程序。

候选可提交你作有限设计采纳决定，但尚未接受。`SOURCE BINDING: NOT ESTABLISHED`，DSP-004 仍为 `OPEN / HOLD`，输入准入及运行验证未授权。
````
<!-- DSP004 REVIEW C READABLE END -->

## 5. 后续会话层有限采纳记录

本节与第 3 节形成时正文严格分开。用户短指令的对象由对应采纳模板或紧邻待采纳正文绑定；本文件不借由物化扩大其效力。

### 5.1 原文 A 的有限采纳

采纳对象：RDM-DSP-004 会话层边界细化设计 — REV3

#### 形成时采纳决定模板

- writing block：`84536`
- turn：`01a0f0e9-234f-7720-9e55-4be031577519`
- message：`msg_050c32c7e9d0b59a016abca64b94348198b42eb4894b52eec9`

下列模板是后来用户指令所指向的决定文本，其形成时待签署字段按原文保留。

<!-- DSP004 DECISION A READABLE BEGIN -->
````markdown
# Project Owner DSP-004 REV3 有限设计采纳决定

Accepted Subject:
RDM-DSP-004 会话层边界细化设计 — REV3

Decision:
ACCEPT — LIMITED DESIGN TEXT ONLY

Record Form:
CONVERSATION-LEVEL ONLY
正文尚未物化，无独立文件 SHA。

Bound Input Candidate SHA-256:
A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430

Bound Original Fixture SHA-256:
9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8

Review Basis:
独立内部只读复核：PASS — REV3 DESIGN TEXT REVIEW ONLY
来源 SHA：7/7 MATCH
分领域结论：8 PASS / 2 LIMITED
设计正文阻断项：0
本复核不是跨供应商外审或运行验证。

Accepted Scope:
仅采纳拟议原生类型、构造失败分界、旧门禁拒绝保留、事项逐字段归因及补充边界判定优先级的设计正文。

Preserved Limitations:
- Project、Session、Provider 的可信来源仍未绑定。
- 原生输出到 fixture 的比较映射尚未接受。
- 实际隔离效果、运行时副作用及零 I/O 未经验证。
- 原始四边界联合 fixture 保留，不得由单项变体替代。
- 历史审查结果不得自动转移至未来修订 SHA。

No Downstream Effect:
本决定不接受或准入整个输入候选，不关闭 DSP-004、B-01 或 B-02。

文件物化、源码修改、输入或 fixture 修改、比较规则接受、Python/Harness 执行、正式验证、真实事项处理及独立 ACOS 项目操作：
NOT AUTHORIZED

Automatic Downstream Transition:
BLOCKED

Project Owner Signature:
PENDING EXPLICIT ACCEPTANCE AND SIGNATURE
````
<!-- DSP004 DECISION A READABLE END -->

#### 后来的 Project Owner 指令

- turn：`01a0f0ee-98e3-7fb1-9eec-305e103d2d59`
- user message：`01a0f0ee-9aca-7821-9a8d-429e59160c4f`

````text
授权采纳
````

#### 对应会话确认

- message：`msg_050c32c7e9d0b59a016abca7a5d3a8819898b909bfbc26f2ef`

<!-- DSP004 ACCEPTANCE A READABLE BEGIN -->
````markdown
已根据你的明确指令，在本会话确认：

`DSP-004 REV3：ACCEPTED — LIMITED DESIGN TEXT ONLY`

仅采纳设计正文，不代表实现、输入准入或验证通过；未物化文件、修改源码或运行 Python。

当前仍保留：

- 三项可信来源绑定、fixture 比较映射及实际隔离效果：待完成。
- DSP-004：`OPEN / HOLD`；B-01/B-02：未关闭。
- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`。
- 实现与正式验证：`NOT AUTHORIZED`。

后续应先处理可信来源绑定和比较规则，不能直接进入运行验证。
````
<!-- DSP004 ACCEPTANCE A READABLE END -->

### 5.2 原文 B 的有限采纳

采纳对象：DSP-004 可信来源绑定与比较规则草案 — REV1

#### 形成时采纳决定模板

- writing block：`40291`
- turn：`01a0f502-4276-7b73-86d8-6c4a0b3fbcc2`
- message：`msg_050c32c7e9d0b59a016abdb40d60508198ad13b05376b9d006`

下列模板是后来用户指令所指向的决定文本，其形成时待签署字段按原文保留。

<!-- DSP004 DECISION B READABLE BEGIN -->
````markdown
# Project Owner DSP-004 REV1 准备设计有限采纳决定

采纳对象：
《DSP-004 可信来源绑定与比较规则草案 — REV1》

决定：
ACCEPT — LIMITED PREPARATION DESIGN TEXT ONLY

记录形式：
仅限本会话；未物化文件，无独立文件 SHA。

绑定输入候选 SHA-256：
A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430

绑定原始 Fixture SHA-256：
9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8

复核依据：
独立内部只读复核 PASS — PREPARATION DESIGN TEXT REVIEW ONLY
七项来源 SHA：7/7 MATCH
分领域结果：8 PASS / 2 LIMITED
正文阻断项：0

采纳范围：
仅采纳拟议来源角色及绑定要求、原生观察比较步骤、单项与联合条件分离原则，以及候选分类映射的限制。

保留限制：
- 不确认具体可信来源已经绑定。
- 不接受可运行比较规则或整个输入候选。
- 不确认事项边界的最终 Fixture 释义。
- 不确认实际隔离、零 I/O 或禁止效果已经验证。
- 已采纳的 DSP-004 REV3 设计保持不变。

状态与权限：
DSP-004：OPEN / HOLD
B-01 / B-02：OPEN
输入候选：PARTIAL_OBSERVABLE / NOT_RUN

文件物化、源码或输入修改、Python/Harness/场景执行、正式验证、真实事项处理及独立 ACOS 项目操作：
NOT AUTHORIZED

自动下游转换：
BLOCKED

Project Owner：
PENDING EXPLICIT ACCEPTANCE AND SIGNATURE
````
<!-- DSP004 DECISION B READABLE END -->

#### 后来的 Project Owner 指令

- turn：`01a0f508-0954-7362-87dd-658342392f99`
- user message：`01a0f508-0bab-7ea2-99ac-7e77ed7ab484`

````text
同意
````

#### 对应会话确认

- message：`msg_050c32c7e9d0b59a016abdb44c47fc819882636a76cb872c9f`

<!-- DSP004 ACCEPTANCE B READABLE BEGIN -->
````markdown
已根据你的“同意”，在本会话确认：

`DSP-004 REV1：ACCEPTED — LIMITED PREPARATION DESIGN TEXT ONLY`

仅采纳准备设计正文，不代表可信来源已绑定、可运行比较规则已接受或输入已准入。

当前保持：

- DSP-004：`OPEN / HOLD`
- B-01/B-02：未关闭
- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`
- 文件物化、代码修改及运行验证：未授权

下一步应先明确三项边界的具体来源及取值位置，再审查比较映射。
````
<!-- DSP004 ACCEPTANCE B READABLE END -->

### 5.3 原文 C 的有限采纳

采纳对象：DSP-004 合成来源与取值位置候选 — REV1

该对象没有另列独立采纳模板；保存对上述候选正文的直接用户接受指令及会话确认，不补造模板、签名或时间。

#### 后来的 Project Owner 指令

- turn：`01a0f551-5262-74f3-8d9b-f323f82286a2`
- user message：`01a0f551-5959-79b2-89c1-656ca1de7ab8`

````text
接受
````

#### 对应会话确认

- message：`msg_050c32c7e9d0b59a016abdc714cec081988ab3893f7f86d5fb`

<!-- DSP004 ACCEPTANCE C READABLE BEGIN -->
````markdown
已在本会话确认接受《DSP-004 合成来源与取值位置候选 — REV1》：

`ACCEPTED — LIMITED PREPARATION DESIGN TEXT ONLY`

仅采纳合成来源方案与拟议取值位置，不代表实际来源已绑定或捕获已完成。

当前保持：

- `SOURCE BINDING: NOT ESTABLISHED`
- DSP-004：`OPEN / HOLD`；B-01/B-02 未关闭
- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`
- 文件物化、代码修改、输入准入及运行验证：未授权

未创建文件或执行程序。
````
<!-- DSP004 ACCEPTANCE C READABLE END -->

## 6. 未完成条件与继续保留的边界

### 6.1 来源角色仍是设计候选

下表仅汇总原文 C 的拟议字段，不创建来源资产、不捕获引用、不计算或虚构这些来源的 SHA。字段是逻辑位置，不是当前门禁已实现的参数。

| 边界 | 预期来源角色 / 位置 | 实际来源角色 / 拟捕获位置 | 实际绑定状态 |
| --- | --- | --- | --- |
| Project | `SRC004-E-PROJECT / baseline.project_reference` | `SRC004-A-PROJECT / frame.project_reference` | `UNBOUND — NOT ESTABLISHED` |
| Session | `SRC004-E-SESSION / baseline.session_reference` | `SRC004-A-SESSION / frame.session_reference` | `UNBOUND — NOT ESTABLISHED` |
| Provider | `SRC004-E-PROVIDER / baseline.provider_reference` | `SRC004-A-PROVIDER / frame.provider_reference` | `UNBOUND — NOT ESTABLISHED` |

合成期望引用、调用帧刺激、实际捕获观察、比较结论必须继续分开；本文不把任何拟议值登记为实际观察。NullProvider 的禁止调用结果不成为 Provider 身份匹配证明。

### 6.2 待完成条件登记

这些是被保留的准备条件，不是本轮新作出的设计缺陷判定或运行观察。

| 条件 | 保留状态 / 限定 | 本文不产生的效力 |
| --- | --- | --- |
| 六侧来源固定绑定 | 身份、版本、完整 SHA、产生者职责、授权依据、位置及适用范围尚未完整绑定 | 不建立可信性，不接受来源 |
| 受控入口捕获 | 合同与固定代码身份仍须另行形成、审查；预填调用帧不是运行观察 | 不生成捕获证据，不动态导入或读取拟议属性 |
| 具体调用归属 | 来源须绑定具体变体、调用尝试、输入快照；关联字符串相同不足为证 | 不把设计候选当作已执行调用 |
| 精确原生类型合同 | 保留 REV3 的类、枚举、None、元组顺序、无效引用及构造失败规则 | 不创建新类或修改现有合同 |
| 可运行比较规则 | `CR-004-CONTEXT-BOUNDARY-DRAFT-001` 仍为待单独审查的候选 | 准备正文采纳不等于可运行规则接受 |
| Fixture 最终释义与映射 | 事项 ID / 版本逐字段归因设计已获会话层有限采纳；事项边界的最终 Fixture 释义仍未确认，原生输出到 Fixture 的可运行比较／映射规则仍未接受 | actor 错配不替代事项边界；不改写原生返回 |
| 单项与联合条件 | 三项单错配、全匹配对照、原始四边界联合条件分别保留 | 不拼接单项观察冒称联合运行证据 |
| 真实隔离与禁止效果 | 实际披露、状态复用、I/O、写入副作用仍未验证 | 空写入声明、匹配或保护性拒绝不证明实际效果 |
| 整体输入与阶段关闭 | 输入仍 `PARTIAL_OBSERVABLE / NOT_RUN`；DSP-004 `OPEN / HOLD`；B-01 / B-02 `OPEN` | 不接受或准入整体输入，不关闭缺口 |
| 新物化记录的独立效力 | 尚无本文件的独立只读复核或 Project Owner 接受 | 不将旧正文采纳自动转成新文件接受 |

### 6.3 本轮操作边界

- 只创建这一份 Markdown 准备记录并进行静态完整性检查及 SHA 计算。
- 不创建合成基线、调用帧、观察合同、运行证据、Fixture 变体或比较规则文件。
- 不修改现有代码、配置、输入或 Fixture，不导入受审 Python，不运行 Python / Harness / 测试 / 场景。
- 不调用真实供应商、不处理真实事项、个人信息或凭据。
- 不访问或修改独立 ACOS 或其他项目。
- 不执行 Git 提交、推送、分支或合并。
- 不关闭 DSP-004、B-01 或 B-02，不启动任何自动下游转换。
- 本文件物化完成后，任何新记录复核、文件接受、来源绑定或运行准备仍须各自独立的明确授权。

## 7. 无损会话快照附录

以下 JSON 保存三份 writing block 正文、采纳决定形成时模板（如有）、已发布复核结论、用户采纳指令及会话确认的精确字符串。

- `original_body` 是 writing block 内部正文，不含框外说明及 writing fence。
- `published_review_text` 是已发布结论整段正文，不是子审查员完整轨迹。
- `formation_decision_template_body` 是当时待签署模板，不能单独建立后来接受。
- `owner_messages[].text` 和 `conversation_confirmation_text` 保留后来指令与确认，不能建立本文件的接受。
- JSON 转义只是存储形式：解码后须逐字符等于所引会话内容，不施加 Unicode、标点、翻译或空白规范化。

<!-- DSP004 LOSSLESS SNAPSHOTS BEGIN -->
```json
{
  "schema": "DSP004_CONVERSATION_SNAPSHOTS_REV1",
  "thread_id": "019f8d76-a85b-71c0-8127-cab64093db9f",
  "records": [
    {
      "key": "A",
      "title": "RDM-DSP-004 会话层边界细化设计 — REV3",
      "original": {
        "turn_id": "01a0f05b-876c-75e2-8c3d-6aca7df416af",
        "message_id": "msg_050c32c7e9d0b59a016abc8235e4788198a9b77d103417533f",
        "writing_block_id": "86310",
        "original_body": "# RDM-DSP-004 会话层边界细化设计 — REV3\n\n状态：`REVISED DESIGN CANDIDATE — CONVERSATION ONLY / NOT REVIEWED / NOT ACCEPTED`  \n对象：`C03-TA-V-004` 的 Project、Session、Provider 三项边界。\n\n绑定输入候选 SHA-256：\n`A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430`\n\n绑定原始 fixture SHA-256：\n`9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8`\n\n本版仅固定 REV2 中尚不明确的原生类型、无效引用与构造失败分界，以及旧门禁所有非准入分支的观察规则。REV2 的可信来源缺口、原 fixture 保真、实际效果限度及禁止自动下游转换要求均保留。\n\n## 1. 可信来源仍未绑定\n\nProject、Session、Provider 各需受控的预期引用与本次调用引用。两侧来源身份须分别绑定于同一受审调用，不得由调用方自填两侧值来自证匹配。引用仅使用不含真实事项、个人信息、凭据、Token、路径或外部地址的合成标识，并按原值精确比较，不作裁剪或别名替换。\n\n**现有源码没有这三组已绑定来源。** 来源身份及适用范围另行审查前，对应观察只能为 `UNBOUND`，不得因值恰好相同而记为 `MATCH`。NullProvider 的禁止调用结果不是供应商身份匹配证据。\n\n## 2. 拟议原生类型合同\n\n以下均为**未来实现须另行授权的设计类型**，不是现有源码中已经存在的类或观察。拟议类身份固定归属本项目 `route_b_c03.contracts` 合同层；若未来选择其他归属，须作为设计变更复核。\n\n| 拟议原生类型 | 精确要求 |\n| --- | --- |\n| `BoundaryKind` | 原生枚举；仅 `PROJECT`、`SESSION`、`PROVIDER` |\n| `BoundaryCheckState` | 原生枚举；仅 `MATCH`、`MISMATCH`、`UNBOUND`、`NOT_EVALUATED` |\n| `BoundaryCheckCause` | 原生枚举；仅 `EXACT_EQUAL`、`EXACT_UNEQUAL`、`SOURCE_UNBOUND`、`INVALID_REFERENCE_TYPE`、`PRIOR_DENIAL` |\n| `BoundaryCheck` | 拟议不可变对象，字段依次为 `boundary: BoundaryKind`、`state: BoundaryCheckState`、`cause: BoundaryCheckCause`、`audit_correlation_id: str`、`expected_source_id: str \\| None`、`actual_source_id: str \\| None` |\n| 三项观察序列 | 原生 `tuple`，长度严格为 3，元素原生类型严格为 `BoundaryCheck`，顺序严格为 `PROJECT → SESSION → PROVIDER` |\n\n`MATCH` 与 `MISMATCH` 必须有两侧各自已受控绑定的非空原生字符串来源身份。来源身份字段本身不能由调用方自我声明为可信。`UNBOUND` 与 `NOT_EVALUATED` 可以用原生 `None` 表示未取得的来源身份；不能以空字符串或 JSON `null` 投影冒充已核验原生对象。\n\n状态和原因必须成对出现：\n\n| 状态 | 允许原因 |\n| --- | --- |\n| `MATCH` | `EXACT_EQUAL` |\n| `MISMATCH` | `EXACT_UNEQUAL` |\n| `UNBOUND` | `SOURCE_UNBOUND` 或 `INVALID_REFERENCE_TYPE` |\n| `NOT_EVALUATED` | `PRIOR_DENIAL` |\n\n组合门禁拟复用现有 `route_b_c03.contracts.GateDecision` 与 `route_b_c03.contracts.InvocationState` 的原生类身份。其四字段须逐项核验：原生 `InvocationState` 枚举、原生非空 `str` 原因、原生非空 `str` 关联引用、原生空 `tuple` 写入命名空间声明。现有 dataclass 类型注解本身不构成运行时类型核验；JSON 字符串枚举或 `[]` 不可替代这些原生值。\n\n## 3. 无效引用与构造失败的分界\n\n1. 若现有配置、授权包、输入信封或预期身份对象无法构造，或者信封的关联引用无法取得有效原生字符串：记录 `CONSTRUCTION_FAILURE`。**不生成**三项观察序列或 `GateDecision`，也不补写预期结果。\n2. 若上述现有对象均有效、关联引用有效，但补充边界的来源尚未受控绑定或缺失：为对应边界生成原生 `UNBOUND / SOURCE_UNBOUND` 观察。\n3. 若来源已受控绑定，但捕获到的补充引用不是原生 `str`、为空或仅为空白：在构造补充观察对象**之前**将该原始引用判为无效，为对应边界生成原生 `UNBOUND / INVALID_REFERENCE_TYPE` 观察；不得将它伪装为两侧引用错配。\n4. 若补充观察对象本身无法按第 2 节的原生类型合同构造：记录 `CONSTRUCTION_FAILURE`，不输出伪造的三项序列或 `GateDecision`。\n\n第 2、3 项只有在旧门禁分支允许补充观察时才执行；旧门禁先行拒绝的处理按第 4 节确定。\n\n## 4. 旧门禁分支的完整观察规则\n\n先取得现有 `evaluate_identity_gate` 的原生结果。下表穷尽其当前返回分支。旧门禁的状态与原因始终保留，不得被补充检查改成允许。\n\n| 现有分支条件 | 三项边界观察及组合效力 |\n| --- | --- |\n| Kill 生效 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧 `BLOCKED — KILL ACTIVE` |\n| 配置缺失或能力禁用 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧能力未激活拒绝 |\n| 能力已撤销 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |\n| 能力已失效 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧版本失败拒绝 |\n| 五项能力身份任一错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧能力身份拒绝 |\n| 路由、域或适配合同身份任一错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧域身份拒绝 |\n| Tier B 授权包缺失 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权包缺失拒绝 |\n| 授权包状态并非 `ACCEPTED` | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |\n| 撤销状态不为 `CLEAR` 或有效性未确认 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权失败拒绝 |\n| 事项 ID、事项版本、操作主体三项中的一项或多项错配 | 必须另按第 5 节逐字段区分。仅当事项 ID 或事项版本错配可被独立核对时，才允许形成三项**附加诊断观察**；旧 `REJECTED — ISOLATION FAILURE` 不变。若仅操作主体错配或逐字段条件不可核对，三项均 `NOT_EVALUATED / PRIOR_DENIAL` |\n| 目的或操作错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧范围拒绝 |\n| 输入集 SHA 错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧输入集身份拒绝 |\n| 输出类别不在请求范围 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧输出边界拒绝 |\n| 事项授权、执行授权或包决议引用错配 | 三项均 `NOT_EVALUATED / PRIOR_DENIAL`；保留旧授权绑定拒绝 |\n| `ELIGIBLE_FOR_MAPPING` | 在第 1、3 节条件下执行三项补充观察，并按第 6 节确定组合结果；全匹配仍不授予执行权 |\n\n上表的附加诊断仅表示**拟议补充检查**可分别观察三项，不表示现有身份门禁执行了这些检查。旧门禁在任何非 `ELIGIBLE_FOR_MAPPING` 分支拒绝时，其原生结果不得被附加诊断覆盖。\n\n## 5. 事项边界的逐字段条件\n\n共用原因 `REJECTED — ISOLATION FAILURE` 可能由以下任一比较触发，不能单凭原因字符串归因：\n\n- `packet.matter_id` 与 `envelope.matter_id`；\n- `packet.matter_version` 与 `envelope.matter_version`；\n- `packet.actor_reference` 与 `envelope.actor_reference`。\n\n只有两侧字段均可核对时才能记录相应的原值 `MATCH` 或 `MISMATCH`。仅操作主体错配不得充当事项边界错配；事项 ID 或版本至少一项错配，才可作为该边界的**候选证据**。原 fixture 对“事项边界”的最终释义及比较映射仍须单独审查，不能由本设计直接确立。\n\n在旧门禁因事项 ID 或版本错配拒绝后，三项补充观察即使全部得出结果，也只是附加诊断；最终原生 `GateDecision` 保持旧拒绝状态和原因。若三项来源未绑定，如实记录 `UNBOUND`，不得宣称原 fixture 四边界均已受检。\n\n## 6. `ELIGIBLE_FOR_MAPPING` 后的确定性优先级\n\n仅对旧门禁已返回 `ELIGIBLE_FOR_MAPPING`、且现有对象与关联引用有效的情形，按下列**互斥顺序**形成拟议组合结果：\n\n1. 任一项 `UNBOUND / INVALID_REFERENCE_TYPE`：原生 `InvocationState.BLOCKED`，精确原因 `BLOCKED — CONTEXT REFERENCE INVALID`。\n2. 否则，任一项 `UNBOUND / SOURCE_UNBOUND`：原生 `InvocationState.BLOCKED`，精确原因 `BLOCKED — CONTEXT SOURCE UNBOUND`。\n3. 否则，两项或三项 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — MULTIPLE CONTEXT MISMATCHES`。\n4. 否则，仅 Project 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — PROJECT CONTEXT MISMATCH`。\n5. 否则，仅 Session 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — SESSION CONTEXT MISMATCH`。\n6. 否则，仅 Provider 为 `MISMATCH`：原生 `InvocationState.REJECTED`，精确原因 `REJECTED — PROVIDER CONTEXT MISMATCH`。\n7. 三项均为 `MATCH`：保留旧门禁原生 `ELIGIBLE_FOR_MAPPING` 状态及其完整原因。\n\n有效关联引用原样传递；拟议拒绝的允许写入命名空间字段保持原生空元组。这些原因是未来设计合同，不是现有代码输出。`ELIGIBLE_FOR_MAPPING` 只表示仍需其他授权的元数据阶段结果，不许可映射执行或供应商调用。\n\n## 7. 原 fixture、实际效果与后续门禁\n\n后续输入设计仍须分别固定 Project、Session、Provider 单项错配与三项全匹配对照，使待检条件可达。原 fixture 同时记录事项、项目、会话、供应商四项错配，必须作为单独的联合条件保留；三个单项变体不得替代。任何 `UNBOUND` 或 `NOT_EVALUATED` 项都不得被补写为联合条件已通过。\n\n现有门禁原生 `REJECTED` 与 fixture 的 `BLOCKED_ISOLATED` 是不同层级。原生门禁结果、附加观察、fixture 抽象之间的映射仍是**待单独审查的比较规则候选**。元数据匹配、保护性拒绝及原生空写入元组均不证明零实际 I/O、真实项目/会话/供应商隔离，或不存在跨边界披露与状态复用。\n\n本 REV3 只有会话正文，没有物理文件或文件 SHA；尚未经 REV3 只读审查或 Project Owner 接受。当前输入候选仍为 `PARTIAL_OBSERVABLE / NOT_RUN`，`DSP-004` 继续 `OPEN / HOLD`，整体输入未接受、未准入，B-01/B-02 未关闭。\n\n任何源码、输入、fixture、观察合同或比较规则变化均须新 SHA 和另行审查决定。文件物化、代码修改、Python/Harness/场景执行、真实事项处理及独立 ACOS 项目操作均未授权。"
      },
      "review": {
        "turn_id": "01a0f0dd-7f94-7d42-b648-ab475c506174",
        "message_id": "msg_050c32c7e9d0b59a016abca589531c8198a59720ecbc74595c",
        "published_review_text": "DSP-004 REV3 独立只读复核已完成：`PASS — DESIGN TEXT REVIEW ONLY`，尚未接受。\n\n- 七项来源 SHA：`7/7 MATCH`\n- 复核领域：`8 PASS / 2 LIMITED`\n- 旧门禁全部14个拒绝分支：完整覆盖\n- 原生类型、构造失败分界、逐字段归因及组合优先级：通过\n- 设计正文阻断项：0；无需进一步文本修订\n\n两项限制继续保留：可信来源及实际隔离效果尚未验证；原生输出到 fixture 的比较映射尚未接受。\n\n本次是同供应商独立子上下文复核，不是跨供应商外审。未修改文件、运行 Python、执行场景或访问独立 ACOS。\n\nREV3 可提交你作有限设计采纳决定。当前仍保持：`DSP-004 OPEN / HOLD`、输入 `PARTIAL_OBSERVABLE / NOT_RUN`，B-01/B-02 未关闭；实现与正式验证未授权。"
      },
      "formation_decision_template": {
        "turn_id": "01a0f0e9-234f-7720-9e55-4be031577519",
        "message_id": "msg_050c32c7e9d0b59a016abca64b94348198b42eb4894b52eec9",
        "writing_block_id": "84536",
        "formation_decision_template_body": "# Project Owner DSP-004 REV3 有限设计采纳决定\n\nAccepted Subject:\nRDM-DSP-004 会话层边界细化设计 — REV3\n\nDecision:\nACCEPT — LIMITED DESIGN TEXT ONLY\n\nRecord Form:\nCONVERSATION-LEVEL ONLY  \n正文尚未物化，无独立文件 SHA。\n\nBound Input Candidate SHA-256:\nA8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430\n\nBound Original Fixture SHA-256:\n9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8\n\nReview Basis:\n独立内部只读复核：PASS — REV3 DESIGN TEXT REVIEW ONLY  \n来源 SHA：7/7 MATCH  \n分领域结论：8 PASS / 2 LIMITED  \n设计正文阻断项：0  \n本复核不是跨供应商外审或运行验证。\n\nAccepted Scope:\n仅采纳拟议原生类型、构造失败分界、旧门禁拒绝保留、事项逐字段归因及补充边界判定优先级的设计正文。\n\nPreserved Limitations:\n- Project、Session、Provider 的可信来源仍未绑定。\n- 原生输出到 fixture 的比较映射尚未接受。\n- 实际隔离效果、运行时副作用及零 I/O 未经验证。\n- 原始四边界联合 fixture 保留，不得由单项变体替代。\n- 历史审查结果不得自动转移至未来修订 SHA。\n\nNo Downstream Effect:\n本决定不接受或准入整个输入候选，不关闭 DSP-004、B-01 或 B-02。\n\n文件物化、源码修改、输入或 fixture 修改、比较规则接受、Python/Harness 执行、正式验证、真实事项处理及独立 ACOS 项目操作：\nNOT AUTHORIZED\n\nAutomatic Downstream Transition:\nBLOCKED\n\nProject Owner Signature:\nPENDING EXPLICIT ACCEPTANCE AND SIGNATURE"
      },
      "acceptance": {
        "turn_id": "01a0f0ee-98e3-7fb1-9eec-305e103d2d59",
        "owner_messages": [
          {
            "message_id": "01a0f0ee-9aca-7821-9a8d-429e59160c4f",
            "text": "授权采纳\n"
          }
        ],
        "message_id": "msg_050c32c7e9d0b59a016abca7a5d3a8819898b909bfbc26f2ef",
        "conversation_confirmation_text": "已根据你的明确指令，在本会话确认：\n\n`DSP-004 REV3：ACCEPTED — LIMITED DESIGN TEXT ONLY`\n\n仅采纳设计正文，不代表实现、输入准入或验证通过；未物化文件、修改源码或运行 Python。\n\n当前仍保留：\n\n- 三项可信来源绑定、fixture 比较映射及实际隔离效果：待完成。\n- DSP-004：`OPEN / HOLD`；B-01/B-02：未关闭。\n- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`。\n- 实现与正式验证：`NOT AUTHORIZED`。\n\n后续应先处理可信来源绑定和比较规则，不能直接进入运行验证。"
      }
    },
    {
      "key": "B",
      "title": "DSP-004 可信来源绑定与比较规则草案 — REV1",
      "original": {
        "turn_id": "01a0f0ef-40f2-7352-acef-d05f8a7734d4",
        "message_id": "msg_050c32c7e9d0b59a016abca8881b7c819898f4cb74b19822d4",
        "writing_block_id": "96524",
        "original_body": "# DSP-004 可信来源绑定与比较规则草案 — REV1\n\nStatus:\nPREPARED — NOT REVIEWED / NOT ACCEPTED\n\nScope:\n仅细化已采纳的 DSP-004 REV3 设计，不改变其原生类型、旧门禁优先级或权限边界。\n\nBound Input Candidate SHA-256:\nA8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430\n\nBound Original Fixture SHA-256:\n9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8\n\n## 1. 可信来源绑定要求\n\n以下是拟议来源角色，不是已存在或已获准使用的来源资产。\n\n| 边界 | 预期引用来源角色 | 实际引用来源角色 | 当前状态 |\n| --- | --- | --- | --- |\n| Project | 经独立确认的本项目范围基线 | 本次调用入口捕获的项目引用 | SOURCE UNBOUND |\n| Session | 经独立确认的合成会话范围基线 | 本次调用入口捕获的会话引用 | SOURCE UNBOUND |\n| Provider | 经独立确认的供应商身份范围基线 | 本次调用入口捕获的供应商引用 | SOURCE UNBOUND |\n\n每侧来源后续均须固定：来源身份、版本、完整 SHA、产生者角色、授权依据、取值位置和适用范围。来源记录必须绑定具体变体及同一受审调用，不能仅凭可能重复的关联字符串证明来源属于该调用。\n\n调用方不得通过自填两侧引用建立可信性。来源身份匹配也不等于边界值匹配；必须先确认来源，再比较实际引用。\n\n现有 NullProvider 的禁止调用结果不能替代 Provider 身份证据。当前没有完整来源绑定，因此不得登记三项边界为 MATCH。\n\n仅使用合成元数据，不引入真实事项、个人信息、凭据、Token、文件路径或外部地址。\n\n## 2. 原生观察比较顺序\n\n拟议规则标识：\nCR-004-CONTEXT-BOUNDARY-DRAFT-001\n\n1. 核对固定源码、来源、变体和实际返回的对应关系。\n2. 检查 REV3 规定的精确原生类、枚举、字段类型及三项元组顺序。\n3. 将预期数据、实际观察、类型来源和比较结论分别保留，禁止把预期值复制成实际观察。\n4. 对来源已绑定的有效原生字符串进行逐字符比较，不裁剪、翻译、归一化或替换。\n5. JSON 仅可作为可逆展示；字符串枚举和空列表不能替代原生枚举与空元组。\n6. 缺失观察、类型失败、异常、无返回或未定义状态均停止受影响的比较，禁止补值后给出通过。\n\n构造失败不生成伪造的观察或门禁结果；已经取得的真实旧拒绝结果仍须保留。\n\n## 3. 分离的比较条件\n\n| 条件 | 拟议比较要求 | 与原始 fixture 的关系 |\n| --- | --- | --- |\n| Project 单错配 | 旧门禁准入；Project 为 MISMATCH，其余两项 MATCH；组合结果为 REJECTED，原因逐字为 `REJECTED — PROJECT CONTEXT MISMATCH` | 单项控制，不代表四边界联合通过 |\n| Session 单错配 | 旧门禁准入；Session 为 MISMATCH，其余两项 MATCH；原因逐字为 `REJECTED — SESSION CONTEXT MISMATCH` | 单项控制 |\n| Provider 单错配 | 旧门禁准入；Provider 为 MISMATCH，其余两项 MATCH；原因逐字为 `REJECTED — PROVIDER CONTEXT MISMATCH` | 单项控制 |\n| 三项全匹配 | 三项均 MATCH；保留旧门禁准入结果及完整原因 | 正向控制，不授予运行权限 |\n| 无效引用或来源未绑定 | 严格沿用 REV3 的 UNBOUND 原因与组合优先级 | 不得映射成联合条件通过 |\n| actor 单错配 | 保留旧 isolation 拒绝；三项补充观察为 NOT_EVALUATED | 不得充当事项边界错配 |\n| 普通旧门禁拒绝 | 保留原生状态、原因；三项为 NOT_EVALUATED | 不得推断补充边界已检查 |\n| 原始四边界联合条件 | 事项 ID 或版本错配须逐字段确认；三项补充边界均有受控来源并实际记录 MISMATCH；保留旧 isolation 拒绝，补充结果仅作诊断 | 单独保留，不以单项结果拼成联合运行证据 |\n\n同一比较中的门禁和补充观察须关联同一变体、同一调用。原因、关联引用及写入命名空间声明均按原生类型和值核对，不接受前缀匹配或原因替换。\n\n## 4. 原始 fixture 映射限制\n\n原始期望保持不变：\n\n- expected_state：BLOCKED_ISOLATED\n- expected_reason_class：BOUNDARY_MISMATCH\n- expected_permitted_write_set：空集合的原有 JSON 表示\n- prohibited_effect：CROSS_BOUNDARY_DISCLOSURE_OR_STATE_REUSE\n\n原生 REJECTED 到 BLOCKED_ISOLATED 仅是待审的分类映射，不改变原生返回。\n\n即使分类映射成立，空写入声明仍只是元数据，不能证明没有实际披露、状态复用或其他 I/O。因此不得据此宣布整个 fixture 通过或实际隔离成立。\n\n## 5. 保留状态\n\n可信来源选择与绑定：\nNOT ESTABLISHED\n\n比较规则：\nDRAFT — NOT ACCEPTED\n\nDSP-004：\nOPEN / HOLD\n\n输入候选：\nPARTIAL_OBSERVABLE / NOT_RUN\n\nB-01 / B-02：\nOPEN\n\n文件物化、源码或输入修改、Harness、Python、场景执行、正式验证、真实事项处理及独立 ACOS 操作：\nNOT AUTHORIZED"
      },
      "review": {
        "turn_id": "01a0f4f8-a82e-74e3-ac64-f421a1feedd5",
        "message_id": "msg_050c32c7e9d0b59a016abdb28852d08198912ab063c38ed00a",
        "published_review_text": "REV1 独立只读复核已完成：\n\n`PASS — PREPARATION DESIGN TEXT REVIEW ONLY`\n\n- 七项来源 SHA：`7/7 MATCH`\n- 分领域结果：`8 PASS / 2 LIMITED`\n- 正文阻断项：0；无需文本修订\n- 与已采纳 REV3 的类型、拒绝保留及判定优先级一致\n\n两项限制继续保留：具体可信来源尚未绑定；fixture 映射及实际隔离效果尚未获确认。\n\n本次为同供应商新上下文独立内部复核，不是跨供应商外审。未修改文件、运行 Python 或执行场景。\n\nREV1 可提交你作“准备设计正文”的有限采纳决定，但尚未接受；DSP-004 仍为 `OPEN / HOLD`，输入准入和运行验证仍未授权。"
      },
      "formation_decision_template": {
        "turn_id": "01a0f502-4276-7b73-86d8-6c4a0b3fbcc2",
        "message_id": "msg_050c32c7e9d0b59a016abdb40d60508198ad13b05376b9d006",
        "writing_block_id": "40291",
        "formation_decision_template_body": "# Project Owner DSP-004 REV1 准备设计有限采纳决定\n\n采纳对象：\n《DSP-004 可信来源绑定与比较规则草案 — REV1》\n\n决定：\nACCEPT — LIMITED PREPARATION DESIGN TEXT ONLY\n\n记录形式：\n仅限本会话；未物化文件，无独立文件 SHA。\n\n绑定输入候选 SHA-256：\nA8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430\n\n绑定原始 Fixture SHA-256：\n9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8\n\n复核依据：\n独立内部只读复核 PASS — PREPARATION DESIGN TEXT REVIEW ONLY  \n七项来源 SHA：7/7 MATCH  \n分领域结果：8 PASS / 2 LIMITED  \n正文阻断项：0\n\n采纳范围：\n仅采纳拟议来源角色及绑定要求、原生观察比较步骤、单项与联合条件分离原则，以及候选分类映射的限制。\n\n保留限制：\n- 不确认具体可信来源已经绑定。\n- 不接受可运行比较规则或整个输入候选。\n- 不确认事项边界的最终 Fixture 释义。\n- 不确认实际隔离、零 I/O 或禁止效果已经验证。\n- 已采纳的 DSP-004 REV3 设计保持不变。\n\n状态与权限：\nDSP-004：OPEN / HOLD  \nB-01 / B-02：OPEN  \n输入候选：PARTIAL_OBSERVABLE / NOT_RUN\n\n文件物化、源码或输入修改、Python/Harness/场景执行、正式验证、真实事项处理及独立 ACOS 项目操作：\nNOT AUTHORIZED\n\n自动下游转换：\nBLOCKED\n\nProject Owner：\nPENDING EXPLICIT ACCEPTANCE AND SIGNATURE"
      },
      "acceptance": {
        "turn_id": "01a0f508-0954-7362-87dd-658342392f99",
        "owner_messages": [
          {
            "message_id": "01a0f508-0bab-7ea2-99ac-7e77ed7ab484",
            "text": "同意\n"
          }
        ],
        "message_id": "msg_050c32c7e9d0b59a016abdb44c47fc819882636a76cb872c9f",
        "conversation_confirmation_text": "已根据你的“同意”，在本会话确认：\n\n`DSP-004 REV1：ACCEPTED — LIMITED PREPARATION DESIGN TEXT ONLY`\n\n仅采纳准备设计正文，不代表可信来源已绑定、可运行比较规则已接受或输入已准入。\n\n当前保持：\n\n- DSP-004：`OPEN / HOLD`\n- B-01/B-02：未关闭\n- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`\n- 文件物化、代码修改及运行验证：未授权\n\n下一步应先明确三项边界的具体来源及取值位置，再审查比较映射。"
      }
    },
    {
      "key": "C",
      "title": "DSP-004 合成来源与取值位置候选 — REV1",
      "original": {
        "turn_id": "01a0f50d-0462-7621-9d01-643e4f6c07d4",
        "message_id": "msg_050c32c7e9d0b59a016abdb6577a688198a6e0f86c0d7074e9",
        "writing_block_id": "58127",
        "original_body": "# DSP-004 合成来源与取值位置候选 — REV1\n\nStatus:\nDESIGN CANDIDATE — NOT REVIEWED / NOT ACCEPTED\n\n适用范围：\n仅本项目 C03-TA-V-004 的合成元数据比较，不接入真实案件、会话服务或供应商。\n\n绑定输入候选 SHA-256：\nA8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430\n\n绑定原始 Fixture SHA-256：\n9DAE8B930EB62CE358605D0FB4CB080FC8F5A3C81CAF946B7C98D48979BE46D8\n\n## 1. 候选来源选择\n\n拟采用两种分别受控的来源：\n\n- 合成边界基线：保存经审查冻结的预期引用。\n- 合成调用帧：保存具体变体拟送入调用入口的引用；实际取值须由受控入口捕获，不能从预期基线回填。\n\n两者尚未物化、审查或准入。调用帧中的预填值是测试刺激，不是运行观察。\n\n## 2. 拟议取值位置\n\n下列位置仅为新设计的逻辑字段，不存在于当前门禁参数或输入对象中，不得据此动态导入或查找属性。\n\n| 边界 | 预期来源角色标识／位置 | 实际来源角色标识／拟捕获位置 |\n| --- | --- | --- |\n| Project | SRC004-E-PROJECT／baseline.project_reference | SRC004-A-PROJECT／frame.project_reference |\n| Session | SRC004-E-SESSION／baseline.session_reference | SRC004-A-SESSION／frame.session_reference |\n| Provider | SRC004-E-PROVIDER／baseline.provider_reference | SRC004-A-PROVIDER／frame.provider_reference |\n\n拟议全匹配基线引用：\n\n- Project：SYNTHETIC-PROJECT-001\n- Session：SYNTHETIC-SESSION-001\n- Provider：SYNTHETIC-PROVIDER-001\n\n这些值仅为设计期望，不是实际捕获记录、可信性证明或真实供应商身份。\n\n## 3. 来源成为可用证据的条件\n\n每侧来源均须另行固定身份、版本、完整 SHA、产生者职责、授权依据、取值位置及适用范围。\n\n必须同时满足：\n\n1. 预期基线已冻结，待审调用不能改写它。\n2. 实际引用由受控入口取得，禁止以预期值代替。\n3. 来源记录关联具体变体、调用尝试及输入快照；仅关联字符串相同不足以证明同一调用。\n4. 捕获合同及其固定代码身份经过审查。\n5. 来源身份与引用值分别核验；身份匹配不能代替值比较。\n6. 产生者职责声明不等于可信性证明；不要求记录真实人物信息。\n7. 缺失任何必要绑定时维持 UNBOUND，不虚构 SHA 或补填来源。\n\n现有门禁不会读取这些新字段。未来补充观察适配须单独授权，不得改变已采纳 REV3 的旧拒绝保留、类型合同和判定优先级。\n\n## 4. 比较范围限制\n\n三项单错配、全匹配对照和原始四边界联合条件分别保留。\n\n现有事项 ID、版本、actor 三条变体不修改；actor 不得替代事项边界。\n\n即使未来合成比较通过，也只能证明受控合成输入的元数据比较符合合同，不能证明真实项目、会话或供应商已经隔离。\n\nFixture 分类映射、事项边界最终释义和实际禁止效果仍需另审。\n\n## 5. 当前效力\n\n本候选只有会话正文，无物理文件或自身 SHA。\n\nSOURCE BINDING：NOT ESTABLISHED  \nDSP-004：OPEN / HOLD  \n输入候选：PARTIAL_OBSERVABLE / NOT_RUN  \nB-01 / B-02：OPEN\n\n文件物化、源码或输入修改、Python/Harness/场景执行、正式验证、真实事项处理及独立 ACOS 操作：\nNOT AUTHORIZED"
      },
      "review": {
        "turn_id": "01a0f518-f527-7180-acf6-1d6ede028c94",
        "message_id": "msg_050c32c7e9d0b59a016abdb9e24d6081989ad803405ef25b31",
        "published_review_text": "《DSP-004 合成来源与取值位置候选 — REV1》独立只读复核已完成：\n\n`PASS — PREPARATION CANDIDATE DESIGN TEXT REVIEW ONLY`\n\n- 七项来源 SHA：`7/7 MATCH`\n- 分领域结果：`8 PASS / 2 LIMITED`\n- 正文阻断项：0；无需修订\n\n两项限制保留：六个来源角色的实际绑定及受控捕获尚未建立；fixture 最终映射与实际隔离效果尚未确认。\n\n本次是同供应商独立内部复核，不是跨供应商外审。未修改文件或运行程序。\n\n候选可提交你作有限设计采纳决定，但尚未接受。`SOURCE BINDING: NOT ESTABLISHED`，DSP-004 仍为 `OPEN / HOLD`，输入准入及运行验证未授权。"
      },
      "formation_decision_template": null,
      "acceptance": {
        "turn_id": "01a0f551-5262-74f3-8d9b-f323f82286a2",
        "owner_messages": [
          {
            "message_id": "01a0f551-5959-79b2-89c1-656ca1de7ab8",
            "text": "接受\n"
          }
        ],
        "message_id": "msg_050c32c7e9d0b59a016abdc714cec081988ab3893f7f86d5fb",
        "conversation_confirmation_text": "已在本会话确认接受《DSP-004 合成来源与取值位置候选 — REV1》：\n\n`ACCEPTED — LIMITED PREPARATION DESIGN TEXT ONLY`\n\n仅采纳合成来源方案与拟议取值位置，不代表实际来源已绑定或捕获已完成。\n\n当前保持：\n\n- `SOURCE BINDING: NOT ESTABLISHED`\n- DSP-004：`OPEN / HOLD`；B-01/B-02 未关闭\n- 输入候选：`PARTIAL_OBSERVABLE / NOT_RUN`\n- 文件物化、代码修改、输入准入及运行验证：未授权\n\n未创建文件或执行程序。"
      }
    }
  ]
}
```
<!-- DSP004 LOSSLESS SNAPSHOTS END -->

## 8. 记录效力收束

三份正文及其后续会话层有限采纳记录被收录于本准备文档；形成时声明未被追溯改写。本物化记录的独立复核、接受与下游权限均未由收录行为建立。

`DESIGN PREPARATION RECORD ONLY — NO RUNTIME EVIDENCE / NO INPUT ADMISSION / NO GAP CLOSURE / NO AUTOMATIC DOWNSTREAM EFFECT`
