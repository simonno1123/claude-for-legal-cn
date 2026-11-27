# TASK_PHASE2_CLAIM_BASIS_ROUTING_HANDOFF（范围交接，已确认）

| 字段 | 值 |
| --- | --- |
| 依据 | `docs/phase2/track-c/TASK_PHASE2_CLAIM_BASIS_OTHER_SKILLS_PROPOSAL.md`（已决定方案 B，PR #176） |
| 起草 | Claude（记录人），2026-11-25 |
| 状态 | **已确认（2026-11-25）。** 所有者确认，授权按第二节实施并复验。PR #177 经 Codex 评审（第 1 轮无发现） |

## 一、固定基线

| 文件 | 改动前 SHA-256 |
| --- | --- |
| `litigation-legal/skills/matter-intake/SKILL.md` | `E30FCB9619784160EA3A507850376768BF7A963C831087F9D95B87FEE698371E` |
| `litigation-legal/skills/demand-draft/SKILL.md` | `38CA05DF81DCFBF7BA41938FBD7AC031834494A01E79FBFEB4057316C347498D` |
| `litigation-legal/references/test-cases-cn.md` | `061D44CA63D127D3698CCD50876577CEFA85D317C962DC6CBC9947068882B0DB` |

## 二、授权范围

### 包 Y1：`matter-intake`

第 5 步"诉请和请求权基础"第二个圆点（"区分委托人目标……待核验问题。"）之后，新增一个圆点：

> - 收案只列材料中明显的候选请求权基础，不做完整检索；完整检索（检索顺序、三段式检验）在 `claim-chart` 第 3A 步进行。本步列出的候选，交接时标明"收案候选，未经第 3A 步检索"。

### 包 Y2：`demand-draft`

起草前卡点中：

> - 合同/侵权/不当得利/缔约过失等请求权基础。

改为：

> - 请求权基础：取自经律师复核的 `claim-chart` 输出（注明所依版本）；没有的，提示先运行 `claim-chart`，不在起草时自行检索或选定请求权基础。

### 包 Y3：回归情境

在 S49 之后追加：

| 编号 | 输入 | 应有表现 |
| --- | --- | --- |
| S50 | 收案材料显示两个以上可能的请求权基础 | `matter-intake` 只列明显候选，标明"收案候选，未经第 3A 步检索"，不展开三段式 |
| S51 | 要求起草律师函，但没有经复核的 `claim-chart` 输出 | `demand-draft` 提示先运行 `claim-chart`，不自行检索或选定请求权基础 |

### 不授权

以上所列以外的任何改动；`enforcement-review` 和只读副本不改。

## 三、验证

1. 静态核查 S50、S51。
2. 运行复验：另起独立子代理，各用一份虚构材料运行一次：
   - `matter-intake`：复用 CB-09 的事实和依据时效包，按 S50 评判；
   - `demand-draft`：复用 CB-01 的事实（不提供 `claim-chart` 输出），按 S51 评判。
3. 结果写入 `docs/phase2/track-c/TASK_PHASE2_CLAIM_BASIS_ROUTING_RESULT.md`。评判前逐行通读输出。

## 四、回滚与验收

- 改动前另存三个文件的原始字节。
- 验收条件：改动前 SHA 一致；差异只在第二节所列位置；静态核查与运行复验通过；隐私检查和 CI 通过；Codex 评审无重大问题，所有者确认后合并。

## 五、请所有者确认

确认本交接，即授权按第二节修改两个技能和回归情境，并做运行复验。
