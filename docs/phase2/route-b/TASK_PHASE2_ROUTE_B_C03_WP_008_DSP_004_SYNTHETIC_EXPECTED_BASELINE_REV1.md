# DSP-004 合成预期基线候选 — REV1

## 1. 资产类型与授权效力

| 项目 | 形成时记录 |
| --- | --- |
| Project | claude-for-legal-cn-phase2.5 |
| Scenario | C03-TA-V-004 |
| Asset Type | MARKDOWN SYNTHETIC EXPECTED BASELINE CANDIDATE ONLY |
| Candidate Document Version | REV1 |
| Materialization State | MATERIALIZED — CANDIDATE ONLY |
| Candidate Review | NOT AUTHORIZED / NOT COMPLETED |
| Candidate Acceptance | NOT ESTABLISHED |
| Source Admission | NOT AUTHORIZED / NOT ESTABLISHED |
| Source Binding | NOT ESTABLISHED |

唯一物化授权对象是本文件。Project Owner 在对话中明确确认“授权预期基线候选物化”，对应授权文本 writing block `96481`。

该授权只允许形成三项合成预期引用的 Markdown 候选、静态完整性检查及物化后 SHA-256 计算，不授权候选审查、接受、来源准入、实际捕获或运行。

本文件中的状态描述候选形成时的边界。未来的审查、接受或准入决定不得通过改写本文追溯建立，须以独立、明确且固定 SHA 的决定记录确认。

## 2. 固定设计依据与载体身份

### 2.1 两项物理基线

Preparation Record:
`C:\Users\Administrator\Documents\claude-for-legal-cn-phase2.5\docs\phase2\route-b\TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_DESIGN_RECORD_REV1.md`

SHA-256:
`DB39150AE0428A452B2BEBE958A4B7DD91F4DE8A3790B0BC374FAEA4693868F4`

Acceptance Decision Archive:
`C:\Users\Administrator\Documents\claude-for-legal-cn-phase2.5\.codex-coordination\decisions\TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PREPARATION_RECORD_ACCEPTANCE_DECISION.md`

SHA-256:
`F45ED18D9E314B84F7A6A724F5C96DF1C9030C9102C29432A19A4DC4CD680FDE`

两项 SHA 绑定其物理文件字节身份；引用这些基线不重新裁定其治理效力，也不使本候选自动接受。

### 2.2 会话层设计依据

- “DSP-004 六侧合成来源规格与职责映射 — REV1”，writing block `59382`；Project Owner 已明确确认“采纳来源规格 REV1”，效力仅为会话层设计文本。
- “DSP-004 合成来源绑定与受控捕获合同设计草案 — REV2 有限澄清”，writing block `50736`；仅其第 5 节有限澄清已获采纳，其余章节不因本候选取得整体接受。
- 原 REV3 的精确原生类型、旧拒绝保留、事项与 actor 区分及判定优先级继续保留。

以上会话正文没有因本文件产生各自的物理文件 SHA，不以本文件摘要替代会话正文身份。

### 2.3 本候选载体

Carrier:
`C:\Users\Administrator\Documents\claude-for-legal-cn-phase2.5\docs\phase2\route-b\TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SYNTHETIC_EXPECTED_BASELINE_REV1.md`

本候选拟由三项预期侧角色共用这一 Markdown 载体。载体身份取物化完成后本文件全部 UTF-8 字节的 SHA-256；摘要只在外部会话回执中记录，不内嵌本文件，也不计算排除字段后的替代摘要。

每项角色须结合本文件摘要及第 3 节的独立记录定位才能描述对应候选。共用载体摘要不证明角色可信、来源准入或引用值匹配；不得把三个引用字符串的摘要当作载体身份。

本候选是人可读的来源准备文档，不是可执行 Schema、当前门禁参数、已实例化原生对象或输入文件。禁止据此自动读取拟议属性、生成调用或回填观察。

## 3. 三项预期来源候选

### 3.1 Project 预期来源候选

| Field | Candidate Record |
| --- | --- |
| Source Role | SRC004-E-PROJECT |
| Candidate Source Identity | DSP004-EXPECTED-PROJECT-V1 |
| Candidate Record Version | REV1 — DOCUMENT CANDIDATE VERSION ONLY |
| Expected Reference | SYNTHETIC-PROJECT-001 |
| Producer Responsibility | BASELINE_PREPARER — 本次文档由 Codex Executor 物化；不据此宣称来源可信 |
| Materialization Authority | Project Owner 对本文件的单次物化授权；不含来源接受或准入 |
| Record Locator | 本文件第 3.1 节，Field = Expected Reference 的唯一表格行 |
| Proposed Logical Location | baseline.project_reference — 逻辑候选，当前接口未实现 |
| Candidate Applicability | C03-TA-V-004 的合成 Project 预期引用；具体变体、调用及输入快照使用绑定尚未建立 |
| Carrier SHA Binding | 本文件全字节 SHA 在外部会话回执中绑定；本文不内嵌 |
| Source Qualification | CANDIDATE RECORD ONLY — NOT REVIEWED / NOT ACCEPTED / NOT ADMITTED |

### 3.2 Session 预期来源候选

| Field | Candidate Record |
| --- | --- |
| Source Role | SRC004-E-SESSION |
| Candidate Source Identity | DSP004-EXPECTED-SESSION-V1 |
| Candidate Record Version | REV1 — DOCUMENT CANDIDATE VERSION ONLY |
| Expected Reference | SYNTHETIC-SESSION-001 |
| Producer Responsibility | BASELINE_PREPARER — 本次文档由 Codex Executor 物化；不据此宣称来源可信 |
| Materialization Authority | Project Owner 对本文件的单次物化授权；不含来源接受或准入 |
| Record Locator | 本文件第 3.2 节，Field = Expected Reference 的唯一表格行 |
| Proposed Logical Location | baseline.session_reference — 逻辑候选，当前接口未实现 |
| Candidate Applicability | C03-TA-V-004 的合成 Session 预期引用；具体变体、调用及输入快照使用绑定尚未建立 |
| Carrier SHA Binding | 本文件全字节 SHA 在外部会话回执中绑定；本文不内嵌 |
| Source Qualification | CANDIDATE RECORD ONLY — NOT REVIEWED / NOT ACCEPTED / NOT ADMITTED |

### 3.3 Provider 预期来源候选

| Field | Candidate Record |
| --- | --- |
| Source Role | SRC004-E-PROVIDER |
| Candidate Source Identity | DSP004-EXPECTED-PROVIDER-V1 |
| Candidate Record Version | REV1 — DOCUMENT CANDIDATE VERSION ONLY |
| Expected Reference | SYNTHETIC-PROVIDER-001 |
| Producer Responsibility | BASELINE_PREPARER — 本次文档由 Codex Executor 物化；不据此宣称来源可信 |
| Materialization Authority | Project Owner 对本文件的单次物化授权；不含来源接受或准入 |
| Record Locator | 本文件第 3.3 节，Field = Expected Reference 的唯一表格行 |
| Proposed Logical Location | baseline.provider_reference — 逻辑候选，当前接口未实现 |
| Candidate Applicability | C03-TA-V-004 的合成 Provider 预期引用；具体变体、调用及输入快照使用绑定尚未建立 |
| Carrier SHA Binding | 本文件全字节 SHA 在外部会话回执中绑定；本文不内嵌 |
| Source Qualification | CANDIDATE RECORD ONLY — NOT REVIEWED / NOT ACCEPTED / NOT ADMITTED |

三项引用仅为合成预期值，不包含真实事项、个人信息、凭据、Token、文件路径或外部地址。上文的载体路径仅用于资产定位，不是边界引用值。

候选身份和文档版本已被写入候选记录，不表示其已被认定为可信来源。不得将候选身份直接填入未来原生观察对象来自证 `MATCH` 或 `MISMATCH`。

## 4. 职责、冻结与使用范围

本次 Codex Executor 的物化职责仅是忠实记录获准的三项预期引用及其候选说明，不承担来源准入、运行观察或 Project Owner 决策职责；不要求记录真实人物信息。

本候选物化后不由本轮继续修改。任何内容变更均须另行授权、产生新 SHA 并重新确认其适用范围。

未来若接受并冻结本候选，待审调用不得改写预期基线。调用刺激可按另行获准变体准备，但不得反向改变预期值，也不得以预期值回填实际捕获记录。

三项单错配、全匹配对照和原始四边界联合条件仍分别保留。具体使用绑定须另行指定相应变体、调用尝试及输入快照；本文件不定义或准入这些输入。

## 5. 尚未建立的绑定与实际侧边界

| 项目 | 本候选完成的记录 | 仍未建立的效力 |
| --- | --- | --- |
| 预期侧身份与版本 | 三项候选身份及 REV1 文档版本 | 可信来源认定及来源准入 |
| 载体 SHA | 由物化后外部会话回执计算和固定 | 单凭摘要不能证明授权充分、来源可信或引用值匹配 |
| 产生者与授权依据 | 文档物化职责和单次物化授权 | 运行产生者资格、捕获授权及输入使用授权 |
| 取值位置 | 三条文档内唯一定位与拟议逻辑位置 | 原生接口实现、受控读取与可运行取值规则 |
| 适用范围 | C03-TA-V-004 合成预期引用范围 | 各变体、调用尝试及输入快照的具体使用绑定 |
| 实际侧来源 | 本文件不创建实际侧记录 | 三项实际来源身份、版本、观察、SHA 及准入全部未建立 |

实际侧继续区分事前捕获资格与事后单次观察记录绑定。不能把本文件、调用刺激或相同的关联字符串当作实际观察来源；不能为尚未产生的观察提前填写 SHA。

整体执行未获准时保持 `NOT_RUN`，不生成观察。未来获准调用中的 `UNBOUND / SOURCE_UNBOUND`、`UNBOUND / INVALID_REFERENCE_TYPE`、`NOT_EVALUATED / PRIOR_DENIAL` 及 `CONSTRUCTION_FAILURE` 分界继续遵循已采纳的 REV2 第 5 节和原 REV3，不由本候选改变。

事项 ID、事项版本及 actor 不合并处理。NullProvider 禁止调用、保护性拒绝、元数据匹配或空写入声明均不证明真实隔离、零 I/O、零披露或无状态复用。

## 6. 后续前置条件

本候选的固定 SHA 只为后续独立、精确范围的决定提供字节身份。候选只读复核、接受、来源准入、具体输入使用绑定、捕获合同、代码实施及运行执行仍须各自明确授权，不因物化自动触发。

未来来源认定须同时核对来源身份、版本、完整 SHA、产生者职责、授权依据、取值位置及适用范围，不得以候选记录“字段已填写”代替条件满足。

本文件不输出候选审查 PASS、零缺陷声明、总体隐私或安全结论，也不接受或准入完整输入。

## 7. 形成时保留状态与操作边界

| 项目 | 保留状态 |
| --- | --- |
| Synthetic Expected Baseline | MATERIALIZED — CANDIDATE ONLY |
| Six-Side Source Binding | UNBOUND — NOT ESTABLISHED |
| Actual Capture | NO OBSERVATION PRODUCED |
| Runnable Comparison Rule | NOT ACCEPTED |
| Input Candidate | PARTIAL_OBSERVABLE / NOT_RUN |
| DSP-004 | OPEN / HOLD |
| B-01 / B-02 | OPEN |
| Automatic Downstream Transition | NOT AUTHORIZED |

本轮仅物化本文件，不另建状态台账、回执文件或接受归档。除获准的本文件静态完整性检查与 SHA 计算外，不生成或修改调用刺激、实际侧来源、捕获记录、具体 Schema、代码、配置、输入或 Fixture；不运行 Python、Harness、测试或场景；不调用真实供应商，不处理真实事项、个人信息或凭据；不访问或修改独立 ACOS 或其他项目，不执行 Git 操作。
