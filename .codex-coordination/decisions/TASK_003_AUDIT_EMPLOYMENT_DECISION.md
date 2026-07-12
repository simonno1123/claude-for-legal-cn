# TASK_003_AUDIT_EMPLOYMENT — 流程决策
# 决策方：Claude
# 决策依据：TASK_003 REVIEW artifact
# 决策时间：2026-07-04

---

## 决策

**ACCEPTED_WITH_CONDITIONS**

## employment-legal 模块状态更新

Baseline Recovery Review A-01：`Valid` → **Valid（附条件）**

条件清单：

| # | 条件 | 优先级 | 截止 |
|---|------|--------|------|
| C-1 | expansion-kickoff / expansion-update / international-expansion 三个 skill 最终处置裁定（映射 or 保持悬挂） | P2 | v1 Release Candidate 前 |
| C-2 | Connector 命名漂移统一（cold-start 中的 `npc-law-database` vs .mcp.json 中的 `legal-data`） | P3 | v2 MCP 接入时 |

## 不需要修复的项（确认合规）

- CN 新增 3 个 China-law skill（handbook-audit、severance-calculator、social-insurance-audit）：合规，深化同一能力
- matter-workspace 默认关闭：与上游 in-house 默认行为一致
- 外国法引用均为负向约束：合规

## 下一任务

**→ ChatGPT** 生成下一个模块的 Codex TASK 任务书。

建议按 Baseline Recovery Review 队列继续：
- TASK_003 已关闭（employment-legal）
- 下一个应为已 Valid 模块中的下一个按序审计

## 流程文件完整性

```
inbox/    TASK_003 — 由 ChatGPT 生成（本次经用户传递）
outbox/   TASK_003 RESULT — 由 Codex 产出（本次经用户传递）
reviews/  TASK_003 REVIEW — 由 Claude 产出 ✅
decisions/ TASK_003 DECISION — 由 Claude 产出 ✅
```

四个 artifact 齐备，TASK_003 流程闭环。
