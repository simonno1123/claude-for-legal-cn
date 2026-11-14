# C03 Tier B 确切案件授权包：CASE-D 单次关口检查（草稿）

| 字段 | 值 |
| --- | --- |
| 包编号／版本 | `C03-TB-CASE-D-001` / R1 |
| 案件 | CASE-D（代号）。真实案件信息、案卷文件名和文件 SHA 只保存在所有者本机的私有文件夹，不写入本仓库 |
| 发起 | 所有者 2026-11-14 选择"只做一次关口检查" |
| 起草 | Claude（记录人） |
| 依据 | 计划 §3.2、§5；激活语义决定 §2；激活决定 `C03-CP-D-015`；B 类移交项处置及决定 `C03-CP-D-016`；依据时效范围修订；R3 关口设计；V8-A |
| 状态 | **草稿**。在 GitHub PR 上交 Codex 评审后，由所有者作出本包的执行授权决定。本文件本身不授权任何执行 |

## 一、确切操作

| 项目 | 内容 |
| --- | --- |
| 操作 | 在所有者本机调用 `C03Capability.evaluate_transition` **一次**（`scripts/phase2_runtime/route_b_c03/capability.py`） |
| `operation` 取值 | `GATE_CHECK_ONCE` |
| `purpose` 取值 | `PIPELINE_VERIFICATION_ON_REAL_MATTER` |
| 输入 | 只有引用和元数据（见第二节）。该函数不打开任何被引用的文件，不读取案卷内容 |
| 输出 | 一条 `TransitionDetermination`（控制判定＋关口判定）。`execution_authorized` 恒为 `False` |
| 不做的事 | 不生成候选；不调用 Provider（端口为 `NullProviderPort`，本次不调用 `submit_provider_reference`）；不做映射；不产生任何法律内容；不对外发送；不改动案卷 |
| 输出的使用 | 判定结果只写入本机审计记录，并向所有者报告。不作任何下游使用；因此本次不产生需要 AR-B-010 逐项授权的输出。以后若要以该判定为基础做任何进一步动作，须另行提交授权包 |
| 结果预期 | 不预设结果。各输入如实填写后，得到 `ELIGIBLE_FOR_MAPPING`（理由码"ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED"）、`BLOCKED` 或 `REJECTED` 都是有效结果，照实记录。不为了得到某一结果而修改输入重跑 |

## 二、输入的确定

所有取值在运行前由记录人在所有者本机填入一份"运行输入单"（私有，不入库），所有者逐项过目后才运行。填法如下：

| 对象 | 字段 | 取值来源 |
| --- | --- | --- |
| 能力配置 | `capability_id` / `capability_version` | `C03` / `V7`（E-015 R3 §二所绑定的版本） |
| | `implementation_sha256` | 对 E-015 R3 §2.1 所列 10 个 V7 实现文件，按路径排序，逐行写"路径＋制表符＋SHA-256＋换行"（UTF-8），对该文本取 SHA-256。运行开始时在本机重算，各文件 SHA 须与 E-015 R3 逐一相符（处置 B-09），否则停止 |
| | `configuration_sha256` | `NONE`（没有单独的配置文件） |
| | `activation_decision_reference` | `C03-CP-D-015` |
| | `state` | `ENABLED_CAPABILITY_ONLY`。运行开始时核对：主分支上的激活决定仍是 `C03-CP-D-015` 且绑定文件 SHA 未变；否则停止，不构造调用输入，记一条拒绝事件 |
| 预期身份 | 全部字段 | 与能力配置及信封取值各自独立地从同一来源文件抄录（先填预期，再填配置和信封，不互相复制） |
| 信封 | `route` 等五个域字段 | 按第二节之二的固定基线填写，不得在运行时另选取值 |
| | `matter_id` / `matter_version` | `CASE-D` / 私有目录中案件材料清单的版本号 |
| | `actor_reference` / `role` | `REVIEWER-01` / 合格复核人（R3 的 M、I 记录） |
| | `matter_authorization_reference` | AR-B-002/004 与 AR-B-003 关闭决定的编号 |
| | `authority_reference` | 依据时效包（AR-B-006，CASE-D）的编号及核对日 |
| | `input_set_sha256` | 见下"输入集" |
| | `requested_output_scope` | 仅 `C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE` |
| | `prohibited_output_scope` | 法律结论、对外文书、任何其他候选类别 |
| | `execution_authorization_reference` | 所有者对本包作出的执行授权决定的编号 |
| | `audit_correlation_id` | 本次运行编号（处置 B-02） |
| | `input_artifact_references` | 见下"输入集" |
| 授权包引用 | `packet_id` / `packet_version` / `packet_sha256` | 本文件的编号、版本、合并后的 SHA-256 |
| | `matter_id`、`matter_version`、`actor_reference`、`purpose`、`operation`、`input_set_sha256`、`output_class` | 按本包取值填写，不从信封复制 |
| | `decision_reference` | 所有者对本包的执行授权决定编号 |
| | `valid_from` / `valid_until` | 见第四节 |
| | `revocation_state` / `state` | 运行开始时由所有者当场确认本包未撤回、未失效：确认则 `RevocationState.CLEAR` / `PacketState.ACCEPTED`。无法确认或已撤回的，停止，不构造调用输入，记一条拒绝事件（`PacketState` 没有“未知”取值，不得硬填） |
| 调用参数 | `validity_confirmed` | 第四节三项时刻核对全部通过才为 `True`，否则 `False` |
| | `kill` / `revocation` / `control_state_known` | 所有者当场确认没有叫停或撤回，则为 `None` / `None` / `True`；无法确认的，按上一行停止 |
| | `subject_scope` | `CASE-D` |
| | `evaluated_at` | 调用时的 UTC 时刻，取自本机时钟，并由所有者对照另一时间来源确认 |

### 二之二、域身份固定基线

| 字段 | 固定取值 | 出处 |
| --- | --- | --- |
| `route` | `Route-B` | Route B 执行域适配规范 §6 信封定义 |
| `domain_id` | `C03-ENFORCEMENT-ADVERSARIAL-DESIGN` | C03 执行对抗域规范（`TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC.md`） |
| `domain_version` | `1.0` | 同上 |
| `adapter_contract_version` | `v1.0` | 执行域适配规范文件自身的版本号。该规范没有给这个字段单独赋值 |
| `route_version` | `1.0` | **没有任何已采纳文件给出取值**，由本包为本次运行固定 |

局限：后两项此前没有已采纳的赋值，是本包为本次运行指定的；关口对这两项的相等比较因此只能证明填写一致，不能证明符合某个更早的已采纳身份。所有者授权本包即确认这两个取值；以后的授权包沿用，变更须另行决定。预期身份与信封都只能填本表取值，任何一项与本表不符即停止。

**输入集。** 只包含两类已经过人工关口的材料的引用，不含案卷原件：

1. 候选 v2（CASE-D / ENF-01 冲突与信息缺口登记），已经 R3 复核，处置 APPROVE；
2. 该候选对应的 R3 复核记录集（V8-A 校验结果为 `PRE_USE_RECORDS_COMPLETE` 的那一套）。

每个引用按 `ArtifactReference` 填写：`readiness_state`、`validation_state` 只在 R3 记录和 V8-A 校验结果确实支持时才填 `READY`、`VALIDATED`；`human_review_reference` 填对应 R 记录的编号。`input_set_sha256` 的算法同 `implementation_sha256`（按引用编号排序的"编号＋制表符＋SHA-256＋换行"文本的 SHA-256），在本机计算，只存私有目录。

## 三、Tier B 七项条件（计划 §3.2）

| 条件 | 满足方式 | 状态 |
| --- | --- | --- |
| Route A 的确认、访问与就绪权限 | AR-B-002、AR-B-004 关闭决定 | 已关闭（带局限） |
| 确切案件与行为人绑定 | AR-B-003 关闭决定；R3 的 M、I 记录 | 已关闭（带局限） |
| 确切证据的身份、来源、出处与就绪状态 | AR-B-004；本次输入集只引用已复核的候选 v2 及其记录，不引入新证据 | 已关闭（带局限） |
| 现行有效的法律依据 | 依据时效包（AR-B-006，CASE-D），核对日＋30 日，截止 2026-12-08T00:00+08:00。运行开始时须仍在有效期内 | 运行时核对 |
| 有范围的合格复核人角色与复核包 | R3 关口设计（已采纳）；REVIEWER-01 | 已具备 |
| 针对本操作的执行授权 | 所有者对本包的决定（新的独立决定链：本包起草 → Codex 评审 → 所有者决定） | **待决定** |
| 人工复核之后对确切输出的单独下游决定 | 本次输出不作下游使用（第一节）；候选 v2 此前的逐项授权已用尽，不因本次运行恢复 | 不适用于本次；以后另行申请 |

## 四、时刻与有效期

- **记录链有效截止**（R3 §9.2）：从输入集中那份确切的 R 记录取得 C5 期限清单及其状态，取“依据核对日＋30 日”与每一项适用的 C5 期限中的最早者。任何一项 C5 期限状态为“未知”的，本次不得运行。就现有记录，依据时效截止为 2026-12-08T00:00+08:00；C5 各项以私有目录中 R 记录为准，运行开始时由所有者逐项过目确认。
- `valid_from`：所有者作出执行授权决定的时刻。
- `valid_until`：取下列两者中较早者——①`valid_from` 之后 7 日；②上述记录链有效截止。
- 截止的含义：到达截止时刻的那一瞬间起即不再有效（`valid_from ≤ 时刻 < valid_until`，与 `identity_gate.py` 的比较一致）。
- 允许运行时长：10 分钟。运行截止时刻＝开始时刻＋10 分钟。
- 按处置 B-04，在开始时、结果返回时、结果写入审计记录并报告之前，各核对一次精确时刻（含时区），三项都要成立：未到运行截止；在 `valid_from` 与 `valid_until` 之间；未到记录链有效截止。任一项不成立或无法确认，本次运行进入 `QUARANTINED — INCOMPLETE`，结果不得使用。

## 五、执行控制

本次运行完全按 B 类移交项处置（`TASK_PHASE2_ROUTE_B_C03_TIER_B_CARRYOVER_DISPOSITION.md`）执行：只在所有者本机前台运行；不接外部 Provider；一次授权只跑一次，不重试；所有者在场并可随时叫停；逐事件写本机审计记录；叫停或中断后按该文件第五节收尾。

处置 B-10 的适用：本次不发生转换或映射，B-10 所指的"首次转换结果复核"不在本次触发，留待第一次实际发生转换的运行。

运行步骤：

1. 所有者确认开始；记录人查审计记录，确认本包没有已用的运行编号（B-02），生成运行编号。
2. 环境与绑定文件 SHA 比对（B-09）。
3. 第一次时刻核对（B-04）。
4. 记录人填运行输入单，所有者逐项过目。
5. 调用一次 `evaluate_transition`。
6. 第二次时刻核对；记录判定结果。
7. 第三次时刻核对；写入审计记录并闭合；向所有者报告。

任何一步失败，运行即结束，不重试（B-03）。

## 六、本包不产生的效果

- 不改变调用关口关闭的状态；判定为 `ELIGIBLE_FOR_MAPPING` 也不授权映射、候选生成或任何执行。
- 不构成长期授权；本包用一次即用尽。
- 不授权读取案卷原件，不授权任何对外行为。
- 不关闭、不改变任何阻断项或局限；E-014 §六的全部局限照旧。

## 七、公开与私有的划分

本文件只含结构和规则。运行输入单、输入集清单、各 SHA、审计记录和运行结果只保存在所有者本机私有文件夹。运行后在仓库中只记一份脱敏的结果记录：运行编号、判定状态与理由码、三次时刻核对是否通过、结束方式。

## 八、请所有者决定

是否授权按本包对 CASE-D 执行一次关口检查。授权决定的时刻即 `valid_from`。
