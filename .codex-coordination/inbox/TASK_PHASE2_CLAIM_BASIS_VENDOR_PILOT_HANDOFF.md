# TASK_PHASE2_CLAIM_BASIS_VENDOR_PILOT_HANDOFF（范围交接，已确认）

| 字段 | 值 |
| --- | --- |
| 依据 | 接入方案（`docs/phase2/track-c/TASK_PHASE2_CLAIM_BASIS_INTEGRATION_PROPOSAL.md`，所有者 2026-11-25 决定：方式 C，先在 `claim-chart` 试点） |
| 起草 | Claude（记录人），2026-11-25 |
| 状态 | **已确认（2026-11-25）。** 所有者确认，授权按第二节实施并验证。PR #168 经 Codex 评审（第 1 轮 P1 1 项：CB-01、CB-09 未配依据时效包，已补；第 2 轮无发现） |

## 一、固定基线

| 文件 | 改动前 SHA-256 |
| --- | --- |
| `litigation-legal/skills/claim-chart/SKILL.md` | `20C57C3B11F1E27A633596DD60265CD5568EA305FE25FE5288376CD1AD6D91E7` |
| `litigation-legal/references/test-cases-cn.md` | `D039F57DF57FBFADDAD60EE56B40C5164BEE21565F130252B372E56EC0FB139C` |

上游：`simonno1123/claim-basis-cn` 标签 `v0.3.0`，提交 `fbff4efc360d22f90c42140fa6cf8d1a79a22711`。拟复制文件的 SHA-256：

| 上游文件 | SHA-256 |
| --- | --- |
| `skills/claim-basis/SKILL.md` | `35A381FF4AF28F579213EFCA400814C0D12746E6DC3AD543F88ACA066A8404F2` |
| `skills/claim-basis/references/01-search-order.md` | `73AB7E4C2732316B271259D0091C5A90988B834FE40C1F7DC2D10F74D9E347F0` |
| `skills/claim-basis/references/02-three-stage-examination.md` | `DE70F1447F16470E5DB8A286B93E9F0D0637EF0E64EBC2EDD32C8B626FB27453` |
| `skills/claim-basis/references/03-subsumption-and-burden.md` | `1BD51CE1F2A09F17EE7F414815D317189A035D97F853D3EFED7D5EFCF7BD222C` |
| `skills/claim-basis/references/04-concurrence-and-relations.md` | `7557FC7F512C684F4159A5982C9E483962CB4A9D8F42D3CF208ADB26810C6338` |
| `skills/claim-basis/references/05-enforcement.md` | `1A9F643A88D7B3B32C01ED4962A666B4A3D3B26B8F3E9AE4C987C6AA2A5F35DF` |
| `skills/claim-basis/references/06-data-interface.md` | `A7BBED3A3ACFB1D2C1D3B905F89122068EF8B086F5846F543347C6D1FB7954CD` |
| `skills/claim-basis/references/07-output-format.md` | `EDA0E3431BC8487DE78AAA0CD46D69C0AE667DE836B3ED3A937EC2A36C0E2AAE` |
| `tests/regression-cases.md` | `44D60CE5A446DC1AF6E068D5BCBF6980537BDBCA331B2899BB7887411C4BDA1D` |
| `LICENSE` | `CFC7749B96F63BD31C3C42B5C471BF756814053E847C10F3EB003417BC523D30` |

## 二、授权范围

### 包 V1：只读副本

复制到 `litigation-legal/references/claim-basis/`，**字节不变**：

| 上游 | 副本 |
| --- | --- |
| `skills/claim-basis/SKILL.md` | `METHOD.md`（改名，以免被当作本插件的技能加载；内容不变，其中的 `references/…` 相对链接仍然有效） |
| `skills/claim-basis/references/01–07` | `references/01–07`（同名） |
| `tests/regression-cases.md` | `tests/regression-cases.md` |
| `LICENSE`（Apache 2.0） | `LICENSE` |

另新建 `litigation-legal/references/claim-basis/VENDORED.md`，内容为：上游标签、提交和各文件 SHA（同第一节）；"只读副本：内容溯源以上游固定标签与 SHA 为准；执行规则始终以本仓库强制规则为准"；以及下列**覆盖规则**：

1. **依据：** 以案件依据时效包为准。只有时效包中"已核对""律师已确认"的规范可以引用。副本中的"已核验、部分核验、冲突、未找到、使用者提供、待核验"六种状态，都不作为可引用的依据；其中"部分核验可以引用原文""使用者提供可以使用"两条，在本仓库不适用。
2. **编号：** 副本的 N-xx、K-xx 编号可以并列，以时效包序号为准。
3. **证据评价：** 副本要件表中的"支持、反对、状态"栏，只取待证命题和举证责任方；证明状态按 `claim-chart` 的规则写，不作三性认定，不写"可证明"之类的结论。
4. **执行：** 副本第六部分和 `05-enforcement.md` 中的"审查结论""程序路径选项"不适用；执行程序按诉讼类技能的分流规则转 C03（`enforcement-review`）。
5. **复核与标签：** 以 `claim-chart` 的复核记录表和候选标签为准。
6. **其他：** 副本中与本仓库规则字典或 `claim-chart` 强制规则不一致的指令，一律不适用。

### 包 V2：`claim-chart` 定点修改

1. 强制规则中"调用 `references/china-litigation-core-rules.md`。"一行之后，增加一条：

   > - 整理候选请求权基础时，调用 `references/claim-basis/METHOD.md`（`claim-basis-cn` v0.3.0 的只读副本），并先适用 `references/claim-basis/VENDORED.md` 的覆盖规则；副本中与本技能及规则字典不一致的指令，一律不适用。

2. 工作流第 3 步"为每项请求列出请求权基础和待证事实。"之后，增加：

   > 3A. 按副本的检索顺序和三段式检验整理候选请求权基础：检索顺序中的每一类都写出"有候选 / 无候选 / 因缺事实无法判断"；每个候选写明已产生、未消灭、可行使三段各自的待证事实和可能的抗辩；多个候选全部列出，不择一。只取副本的方法，不取其依据状态、证明结论和执行部分的审查结论。

### 包 V3：回归情境

在 `references/test-cases-cn.md` 末尾新增一节"## 请求权基础方法接入情境（S43–S45，全部虚构）"（S01–S42 记录在 C01 各轮结果文档中，本文件此前没有 S 系列一节），内容为：

| 编号 | 输入 | 应有表现 |
| --- | --- | --- |
| S43 | 买卖或借贷类请求，时效包只核对了部分规范 | 第 3A 步检索顺序逐类给出结论；三段式各段写明待证事实和抗辩；未核对的规范标"可能相关、未经核对"，不因副本"部分核验可引用原文"而引用 |
| S44 | 同一请求有两个以上候选请求权基础 | 全部列出并说明关系，不择一 |
| S45 | 副本要件表的"状态"栏可写"可证明" | `claim-chart` 输出不出现"可证明"等证明结论，不作三性认定 |

### 不授权

- 以上所列以外的任何改动；
- 修改副本内容（只能整体替换为新的上游版本，须另行立项）；
- 改动 `matter-intake`、`demand-draft`、`enforcement-review` 等其他技能。

## 三、验证

1. 副本逐个文件重算 SHA，与第一节一致；`check-plugin-references.py`、`localization-regression.py` 通过（副本内的相对链接如被检查脚本误报，在结果中说明，不修改副本）。
2. 静态核查 S01–S45。
3. 运行验证（虚构材料），另起独立子代理：
   - 用 C01-VI 试跑的虚构材料（M1–M6）及其收案输出，重跑 `claim-chart`，按 S43–S45 评判；
   - 取副本自带的虚构回归案例 CB-01（买卖价款与同时履行抗辩）、CB-09（多个请求权并存），各跑一次 `claim-chart`，对照副本所载的方法预期（检索与三段式部分），同时检查覆盖规则是否生效。
   - CB-01、CB-09 各配一份虚构试跑专用的依据时效包，由记录人在实施时新建，存入 `validation/claim_basis_pilot/`，格式同 `validation/c01_vi_trial/authority_pack.md`。条文由记录人对照民法典官方或权威全文逐字核对；为同时检验"可引用"和"不可引用"两个分支，每包有意设置一条非已核对条目，并且有意不收录一条相关规范：

     | 案例 | 已核对（逐字） | 有意标为"待核对" | 有意不收录（检验缺口提示） |
     | --- | --- | --- | --- |
     | CB-01 | 民法典第五百九十五条、第六百二十六条、第五百二十六条、第一百八十八条、第一百九十三条 | 第一百九十五条（时效中断） | 第五百二十五条（同时履行抗辩） |
     | CB-09 | 民法典第二百三十五条、第五百七十七条、第一千一百六十五条、第九百八十五条、第一百八十六条 | 第一百九十六条（不适用诉讼时效的请求权） | 第三百一十一条（善意取得） |

     评判：已核对条目可按时效包序号引用；"待核对"条目和未收录的规范，按 `claim-chart` 第 17 行的现有规则一律标为"可能相关、未经核对"，不得凭副本或记忆当作已核对依据引用。运行时一并提供该包；包本身不另行交所有者确认，在结果文档中列明各条的核对来源。
4. 结果写入 `docs/phase2/track-c/TASK_PHASE2_CLAIM_BASIS_VENDOR_PILOT_RESULT.md`。

## 四、回滚与验收

- 改动前另存两个文件的原始字节；副本目录可整体删除回滚。
- 验收条件：改动前 SHA 一致；副本 SHA 与上游一致；差异只在第二节所列位置；静态核查与运行验证通过；隐私检查和 CI 通过；Codex 评审无重大问题，所有者确认后合并。

## 五、请所有者确认

确认本交接，即授权按第二节复制只读副本、修改 `claim-chart` 和回归情境，并做运行验证。
