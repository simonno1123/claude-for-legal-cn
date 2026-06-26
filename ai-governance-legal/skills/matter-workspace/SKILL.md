---
name: matter-workspace
description: >
  以 AI 系统、使用场景、供应商或备案专项为单位建立中国 AI 治理工作台。
argument-hint: "[系统/场景/供应商/专项名称]"
---

# /matter-workspace

## 强制规则

- 工作台只组织材料和状态，不自动上线、备案、提交、签约或关闭事项。
- 默认按 AI 系统/使用场景建档，不使用多客户律所 matter 隔离模型。

## 输出格式

```markdown
# AI 治理工作台

## 基本信息
- 项目：
- AI 类型：
- Owner：
- 状态：

## 材料索引
| 材料 | 版本 | 来源 | 状态 |
|---|---|---|---|

## 风险与动作
| 风险 | 等级 | 动作 | Owner | 截止 |
|---|---|---|---|---|

## 关联命令
- `/ai-governance-legal:use-case-triage`
- `/ai-governance-legal:aia-generation`
- `/ai-governance-legal:vendor-ai-review`
- `/ai-governance-legal:policy-monitor`
```
