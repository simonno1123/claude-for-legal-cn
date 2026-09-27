# C03 WP-008 RDM-V2-03 V3.2/V2.2 输入绑定候选静态校验记录

## 1. 范围与产出

项目：`claude-for-legal-cn`。本轮依据 Project Owner 对单一 RDM-V2-03 准备授权的对话级确认，仅创建独立输入绑定候选并做编制方静态校验。没有给该授权虚构时间戳、决策文件或独立审查结论。

| 角色 | 路径 | SHA-256 / 状态 |
| --- | --- | --- |
| 唯一新输入绑定候选 | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_V3_2_V2_2_REVISION_CANDIDATE.json` | `2E27CC27059016BB7BDC6A680BBBED34579B717AD932757EA3FEC00DD025FECC`；未审查、未接受、未准入 |
| V3.2 固定设计依据 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_2_CANDIDATE.md` | `87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD` |
| V2.2 固定设计依据 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_2_CANDIDATE.md` | `6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA` |
| 只读准备来源 REV3 | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING_RDM_DSP_002_REVISION_CANDIDATE_REV3.json` | `45AB3117389A22DA9F502319467CE8BDDA731539C3B023BF92D7F0E2D93F0C6B`；旧设计对形成时快照，未准入 |
| 未来唯一固定运行输入路径 | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`；原文件保留，未按新版设计对准入 |

V3.2/V2.2 的对话级有限采纳只允许设计准备；独立审查留下的 4 项 LIMITED 仍保留。本记录不是两份设计的无保留接收、RDM-V2-04 决定或完整输入准入凭证。

## 2. 方法与逐项静态结果

方法包括明示路径的本地只读 SHA-256、JSON 解析、结构/值比较、文本格式检查，以及只读 Git 状态与两文件差异查看；文件复制只为创建上述独立候选。没有导入或运行 Python、被审对象、Harness、场景、Manifest 生成器或网络探针；没有 Git 提交或推送。

| 编号 | 核对内容 | 结果与限定 |
| --- | --- | --- |
| `V32V22-STATIC-01` | 三项固定来源身份 | V3.2、V2.2、REV3 SHA 均与上表相符；历史 V3.1/V2.1 只保存在候选的历史来源字段，不是当前 `design_pair`。 |
| `V32V22-STATIC-02` | JSON 与唯一候选身份 | JSON 解析成功；新绑定 ID/版本为 `C03-WP008-SCENARIO-INPUT-BINDING-V3.2-V2.2-CANDIDATE-005` / `0.5`；新增顶层字段仅为 `v32_v22_preparation_reconciliation`。 |
| `V32V22-STATIC-03` | 核心受保护数据 | 与 REV3 解析值比较，`project`、`activation_semantics`、表示契约、源码/fixture 身份、合成数据声明、适配器、合成对象、比较规则和完整 `scenarios` 共 10 组字段均无值变化。 |
| `V32V22-STATIC-04` | 场景及具体输入数量 | 保留 15 个场景、28 个原有输入变体；未补入新实参，未改原始 fixture 输入状态、original oracle、参数或覆盖值。 |
| `V32V22-STATIC-05` | 受约束的源文件身份 | 候选所列 10 份源码、15 份 fixture 分别计算 SHA，25/25 与候选记录一致；这是当前固定路径文件的完整性核对，不是运行时或未枚举文件的证明。 |
| `V32V22-STATIC-06` | 缺失输入与观察限制 | 11/15 场景保留至少一项 `unbound_requirements`；15/15 场景保留 `coverage_limitations`。缺失机制、不可达比较及禁止效果证明没有被改写为 PASS。 |
| `V32V22-STATIC-07` | 旧准入与新候选隔离 | 固定运行输入文件 SHA 仍为 `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5`。新候选不替代此文件，不是可供 V3.2 运行的备用输入路径。 |
| `V32V22-STATIC-08` | 文本格式与最终候选 SHA | 候选保留末尾换行，无行尾空白；落盘后 SHA 为 `2E27CC27059016BB7BDC6A680BBBED34579B717AD932757EA3FEC00DD025FECC`。 |

上述结果仅覆盖列出的文件、字段和路径；尤其不声称能够证明工作区内绝对不存在其他未枚举资产。V3.2 `RQ-021`、`G-017` 与 V2.2 `RQ-018`、`G-014` 的 LIMITED 条目不因此消除。

## 3. 未解决事项与治理状态

- 候选直接沿用 REV3 的原始数据与限制，并改绑新版设计对；REV3 的审查、授权或证据不自动迁移。本次编制方校验不等于独立候选审查。
- 11 个场景的未绑定要求与 15 个场景的覆盖限制仍须逐项处置；不得以现有调用可执行、状态标签存在或局部合成回归替代完整原始要求的可达观察证明。
- B-01、B-02、RDM-DSP-001、RDM-DSP-002 均未由本轮关闭。完整原始要求覆盖、输入准入、正式验证及 C03 就绪均未建立。
- 下一阶段 RDM-V2-04 需分别授权限制项处置、独立固定 SHA 候选审查与 Project Owner 输入准入决定。若后续处置改变输入、源码、fixture、规则或设计身份，必须重新绑定并重审，不能继承本候选 SHA。
- Harness、Manifest、网络/启动证明、Python 或场景运行、正式证据、Git 提交/推送及独立 ACOS 项目变更均不在本轮授权内。

```text
RDM-V2-03: CANDIDATE PREPARED; AUTHOR STATIC CHECK COMPLETED
RDM-V2-04: NOT AUTHORIZED / NOT COMPLETED
INPUT BINDING: NOT INDEPENDENTLY REVIEWED / NOT ADMITTED
EXECUTION: NOT AUTHORIZED / NOT RUN
AUTOMATIC DOWNSTREAM TRANSITION: BLOCKED
```
