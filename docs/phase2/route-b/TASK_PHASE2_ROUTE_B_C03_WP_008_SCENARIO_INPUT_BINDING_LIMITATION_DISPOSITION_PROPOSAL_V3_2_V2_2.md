# Route B C03 WP-008 — V3.2/V2.2 输入绑定限制项处置提案

## 1. 身份、范围与效力

| 字段 | 记录 |
| --- | --- |
| 项目 | `claude-for-legal-cn`，不涉及独立 ACOS 源项目 |
| 生命周期位置 | `RDM-V2-04` 限制项逐项处置准备；不是最终输入准入 |
| 产出性质 | `PROPOSAL ONLY — NOT AN OWNER DISPOSITION OR INDEPENDENT REVIEW` |
| 固定候选 | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE_V2.json` |
| 候选 SHA-256 | `A8AB66D73513B81DBBED5CB56952EEA72C2CE0DB950D521BB49ED0A3D5073430` |
| 候选状态 | `MATERIALIZED — NOT INDEPENDENTLY REVIEWED / NOT ACCEPTED / NOT ADMITTED` |
| 缺省保护路线 | 所有尚无逐项 Project Owner 决定的限制继续 `HOLD`；默认路线不是签署决定 |
| 输入准入、Harness、Manifest、执行 | `NOT AUTHORIZED / NOT ESTABLISHED` |

本提案依据 Project Owner 对“有限修正时序措辞、生成新 SHA 并编制绑定新版设计对的逐项处置提案”的对话级授权编制。它不推定授权时间戳，不替 Project Owner 选择各项路线，不把旧 SHA 的审查、决定或运行证据移植到新候选。

## 2. 精确来源及旧方案隔离

| 来源 | SHA-256 | 本提案使用边界 |
| --- | --- | --- |
| Execution Package V3.2 | `87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD` | 对话级有限采纳的设计依据；4 项 LIMITED 中的 V3.2 两项仍保留 |
| Manifest Preparation Plan V2.2 | `6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA` | `RDM-V2-04` 的处置—复审—准入顺序；V2.2 两项 LIMITED 仍保留 |
| 前一 V3.2/V2.2 输入候选 | `2E27CC27059016BB7BDC6A680BBBED34579B717AD932757EA3FEC00DD025FECC` | 只读有限修订来源；原文件不改，原审查/准入状态不转移 |
| 历史限制项方案 | `ACABF4368E1D5DC968F9EAD6569A6578108AF9B9E0926A1C94326EE498D040CE` | 仅借用 `RDM-DSP-001`–`013` 路由编号；该方案绑定 V3.1/V2.1 和旧输入，旧事实/状态不可直接作为本轮决定 |
| V-002 源码替换记录 | `BF5934EBBBE63065B79DCAB27AFE05733078994851EAD4FB0A28ADC2572873AD` | 记录局部合成回归；不是新版输入或全 WP-008 验证 |
| V-003 规则设计来源 | `9A856FCC23FEAC15A32CB7CD68BF3A33B33801B6D3947AB646CB6FD2AD7E08C9` | 规则及独立输出契约的设计文本；形成时草案状态保留，后续对话级接受不等于候选准入 |
| 五条比较规则接受决定记录 | `5EAAC6DF5F7C5C6BAE31804486C59FCCD7E810DD389C94C87AB84165FD4CC8F6` | 五条规则的设计文本范围接受，不覆盖新输入候选 |
| 上述决定记录的内部审查 | `0EA48E3EDBAFD6565FC668BC4119DC51C078EB63D6D5CD83AF9E40E239E8B8AB` | 对旧决定记录的 PASS，不能充当新版候选独立审查 |

有限修订只把上一候选的 `BEFORE RDM-V2-04` 改为 `BEFORE FINAL INPUT ADMISSION WITHIN RDM-V2-04`，并更新必要候选身份、授权来源和修订来源。新版候选仍保留 15 个场景、28 个原输入变体、10 个源码身份、15 个 fixture 身份，以及全部原始输入、预期、规则和观察限制。此处记录的是编制方静态比对，不是独立候选审查。

## 3. 候选处置语义

| 路线 | 如获逐项授权后的含义 | 不能推得的结论 |
| --- | --- | --- |
| `GOVERNANCE_BINDING_REQUIRED` | 单独形成、审查并接受 V3.2/V2.2 固定 SHA 的脱离式采纳绑定 | 不让旧 V3.1/V2.1 记录自动转用 |
| `CURRENT_SOURCE_RECONCILIATION_REQUIRED` | 复核当前源码、可达入口、固定输入/规则及替换记录的相互一致性 | 局部合成回归不等于正式 WP-008 通过 |
| `BINDING_REVIEW_REQUIRED` | 独立审查新候选原始输入、类型、规则引用和原始要求覆盖 | 不自动接受任何不完整场景或生成执行证据 |
| `LIMITED_DESIGN_REQUIRED` | 对明确缺失的机制或观察面另签精确设计授权 | 不自动授权源码、测试或运行变更 |
| `CONTINUED_HOLD` | 保留原始要求及阻断；受影响场景不得计入完整覆盖 | 不构成豁免、范围缩小、PASS 或缺陷关闭 |

若 Project Owner 后续不为某项明确选择路线，该项默认 `CONTINUED_HOLD`。即使已选择路线，在其所需材料、独立审查及另行接受前，路线也不构成解决。凡改变源码、fixture、输入值、比较规则、观察面或设计身份，均须重新绑定新 SHA，不能补写旧候选后保留其原 SHA。

## 4. 十三项逐项候选路线

| ID | 本轮可核对状态 | 建议的非生效路线与后续证据 |
| --- | --- | --- |
| `RDM-DSP-001` | V3.2/V2.2 仅有对话级有限设计采纳；新设计对的脱离式绑定记录未形成。旧 V3.1/V2.1 记录不能转用。 | `GOVERNANCE_BINDING_REQUIRED`；固定新设计对 SHA、原审查限定与 4 项 LIMITED，单独形成、审查、接受绑定记录；此前最终准入 HOLD。 |
| `RDM-DSP-002` | 历史不可达问题已有源码替换及局部合成回归记录；当前五变体绑定、新候选和正式全覆盖仍未独立审查或准入，不能按旧方案继续声称“当前源码尚未修复”。 | `CURRENT_SOURCE_RECONCILIATION_REQUIRED` + `BINDING_REVIEW_REQUIRED`；核对当前源码 SHA、可达调用与四字段原生输出、五变体、原 fixture；不能以旧源码结论或局部回归关闭本项。未完成前 HOLD。 |
| `RDM-DSP-003` | V-003 规则/输出契约已有对话级设计接受并被保留在候选数据中；其新版绑定及三变体尚未独立审查/准入。旧方案的“尚无已接受规则设计”是形成时快照。 | `BINDING_REVIEW_REQUIRED`；逐项核对三个单字段错配、原生四字段输出与 fixture 抽象分离，禁止把 `BLOCKED` 直接重标为运行时 `BLOCKED_STALE`；未完成前 HOLD。 |
| `RDM-DSP-004` | V-004 仅部分可观察；项目、会话、供应商边界没有完整现有观察入口。 | `CONTINUED_HOLD`，或另签 `LIMITED_DESIGN_REQUIRED`；逐边界建立真实可达输入/观察合同后重新绑定。 |
| `RDM-DSP-005` | V-006 缺少去重存储、重放检测或副作用观察机制。 | `CONTINUED_HOLD`，或另签幂等/重放控制设计；不能将元数据构造当作重复调用证明。 |
| `RDM-DSP-006` | V-008 缺少被接受的时钟、计时器、截止/迟到结果和终止观察。 | `CONTINUED_HOLD`，或另签超时控制设计；时间标签不是实际计时证据。 |
| `RDM-DSP-007` | V-009 缺少撤销收据边界及收据前后行为观察。 | `CONTINUED_HOLD`，或另签收据/传播边界设计；给定状态拒绝不证明传播。 |
| `RDM-DSP-008` | V-010 缺少外部 kill 信号、传播/执行及自我解除防护的观察机制。 | `CONTINUED_HOLD`，或另签 kill 边界设计；输入标志不证明外部强制执行。 |
| `RDM-DSP-009` | V-011 缺少回滚资格、授权、恢复及恢复后状态验证机制。 | `CONTINUED_HOLD`，或另签回滚设计；回滚引用数据不是回滚执行。 |
| `RDM-DSP-010` | V-012 缺少独立完整性检测、链校验、隔离及释放门禁。 | `CONTINUED_HOLD`，或另签完整性链设计；调用方提供 `MISMATCH` 不等于检测。 |
| `RDM-DSP-011` | V-013 无独立依赖/供应商不可用观察面；现有拒绝输出不能改称“不可用”。 | `CONTINUED_HOLD`，或另签不可用状态设计；不进行真实网络或故障注入。 |
| `RDM-DSP-012` | V-015 无针对法律/下游分类请求的类型有效拒绝入口。 | `CONTINUED_HOLD`，或另签非法律推理的分类边界设计；不接入真实事项或自动法律结论。 |
| `RDM-DSP-013` | 五条原比较规则已有独立设计审查、Project Owner 接受记录及该记录的内部审查；历史设计文本范围的关闭不等于新版候选准入。 | 保留五条规则原有设计接受，不重复要求重审不变文本；对新候选仍须 `BINDING_REVIEW_REQUIRED`，核对规则与输入/原始预期逐项一致，不转移旧候选审查证据。 |

表内历史形成时状态只用于解释来源，不推翻后来已记录的有限设计决定。上述路线均为建议；本文件不替 Project Owner 对十三项逐项签署决定。

## 5. 顺序、准入门禁与当前结论

1. 先取得新 V3.2/V2.2 设计对的脱离式绑定；旧方案和旧准入不能迁移。
2. 由 Project Owner 逐项决定 `RDM-DSP-002`–`012` 的继续 HOLD 或另行有限设计路线；`001`、`013` 按上表核对其不同的治理/设计边界。
3. 如任何原始输入、规则、源码、fixture、观察面或设计身份改变，先物化新候选并重新审查；不得暗改当前固定 SHA。
4. 仅在逐项限制得到必要处置、完整原始要求均有可达且可审查的绑定时，才可另行启动独立固定 SHA 候选审查与 Project Owner 最终输入准入决定。`CONTINUED_HOLD` 不会使不完整要求变完整。
5. Harness、Manifest、环境/网络证明与实际运行均在更下游，仍需各自明确授权。

当前新版候选记录 11/15 场景存在 `unbound_requirements`，15/15 场景保留 `coverage_limitations`；其中若干状态文案是形成时快照，需在独立审查时与后续决定核对，不能直接照抄为当前失效或已解决结论。V3.2/V2.2 联合审查的 4 项 LIMITED 保留。静态身份匹配不证明完整可观察性，也不证明工作区内绝无未枚举资产。

```text
DISPOSITION PROPOSAL: MATERIALIZED — NON-OPERATIVE
PER-ITEM PROJECT OWNER DISPOSITIONS: NOT ISSUED BY THIS PROPOSAL
NEW CANDIDATE INDEPENDENT REVIEW: NOT PERFORMED
FINAL INPUT ADMISSION: NOT ESTABLISHED
RDM-V2-04: IN PREPARATION / FAIL-CLOSED
PYTHON, HARNESS, MANIFEST, NETWORK, FORMAL EVIDENCE: NOT AUTHORIZED
```
