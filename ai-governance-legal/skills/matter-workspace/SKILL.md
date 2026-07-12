---
name: matter-workspace
description: >
  以 AI 系统、使用场景、供应商或备案专项为单位建立中国 AI 治理工作台；supports new/list/switch/close/none and matter isolation.
argument-hint: "<new | list | switch | close | none> [系统/场景/供应商/专项名称]"
---

# /matter-workspace

## Mandatory Rules

- 工作台只组织材料和状态，不自动上线、备案、提交、签约或关闭事项。
- 默认按 AI 系统/使用场景建档，必要时支持多客户/多项目隔离。
- Do not read across matter folders unless cross-matter context is explicitly enabled and the user asks for it.

## Storage

Matter root:

`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/matters/`

Active matter is recorded in the practice profile under `## Matter Workspaces`.

## Commands

- `new <slug>`: create `matter.md`, `history.md`, `notes.md`, and `outputs/`.
- `list`: list active and archived matters.
- `switch <slug>`: set active matter in the practice profile.
- `close <slug>`: append close entry and move to `_archived/<slug>`.
- `none`: set active matter to practice-level context only.

## New Matter Intake

Collect:

- Project/system/vendor name.
- Matter type: system triage, security assessment, vendor review, filing, content safety incident, policy update, regulatory gap.
- Related AI system IDs.
- Related use-case IDs.
- Owner and approving reviewer.
- Key materials.
- Confidentiality / access restrictions.

## matter.md Template

```markdown
# AI 治理工作台

## 基本信息
- 项目：
- Slug：
- Matter type：
- AI 类型：
- Owner：
- Reviewer：
- 状态：

## 关联状态
- System IDs:
- Use-case IDs:
- Vendor:
- Assessment files:

## 材料索引
| 材料 | 版本 | 来源 | 状态 |
|---|---|---|---|

## 风险与动作
| 风险 | 等级 | 动作 | Owner | 截止 |
|---|---|---|---|---|

## 权限和隔离
```

## Output Format

```markdown
# AI 治理工作台状态

> **复核提示**
> - **来源：** matter workspace / practice profile
> - **读取范围：** [matter files read]
> - **待判断事项：** [active matter / isolation / close]
> - **时效性：** [open actions]
> - **行动前：** no cross-matter read or external action without confirmation
```
