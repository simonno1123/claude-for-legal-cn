# TASK_005_REGULATORY_RECOVERY — 流程决策
# 决策方：Claude
# 决策依据：TASK_005 REVIEW artifact
# 决策时间：2026-07-04

---

## 决策

**APPROVED**

Codex Recovery Plan 批准执行，附一项升级：

| 原优先级 | 修改后 | 项目 |
|---------|--------|------|
| P1 | **P0-附属** | `regulatory-legal/CLAUDE.md` 操作护栏恢复（reviewer-note、source-provenance、no-silent-supplement） |

其余 P0/P1/P2 分级维持不变。

---

## 批准的修复范围

### P0（必须完成）

| 步骤 | 文件 | 职责恢复目标 |
|------|------|------------|
| 1 | cold-start-interview/SKILL.md | config persistence + --redo + --check-integrations + policy library index |
| 2 | reg-feed-watcher/SKILL.md | feed pull/classify/materiality/comment-deadline/digest |
| 3 | policy-diff/SKILL.md | requirement extraction + rule-status + policy-mapping + gap-handoff |
| 4 | gap-surfacer/SKILL.md + gaps/SKILL.md | tracker schema + lifecycle + close/accept + due-soon/overdue |
| 5 | comments/SKILL.md | comment-tracker + decision log + deadline + approval gate |
| 6 | policy-redraft/SKILL.md | proposal-only + source-policy protection + non-closure guardrail |
| P0-附属 | CLAUDE.md | 操作护栏恢复 |

### P1（应完成）

| 文件 | 目标 |
|------|------|
| reg-change-monitor.md | 对齐 feed→diff→gap 工作流 |
| matter-workspace/SKILL.md | 可选，恢复 workspace lifecycle |

### P2（后续对齐）

README 文案、source-catalog 结构化、MCP 命名、自动化回归测试。

---

## 约束条件

1. 中国法来源、术语、负向约束必须保留，不得回退
2. 修复后产出新 RESULT，Claude 逐项复核 18 项职责
3. 不得越界修改其他模块或项目治理文档

---

## 下一步

**→ ChatGPT** 基于本 DECISION 生成执行任务书：

```
TASK_006_REGULATORY_RECOVERY_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS: regulatory-legal/**
FORBIDDEN ACTIONS: 修改其他模块、删除中国法内容、新增 MCP 实现
REQUIRED OUTPUT ARTIFACT: TASK_006_REGULATORY_RECOVERY_EDIT_RESULT.md
```

---

## 流程异常转办

`.codex-coordination/` 路径不一致问题（Documents vs Downloads）转交 **ChatGPT** 裁定。

---

## 流程文件完整性

```
inbox/    TASK_005 — 由 ChatGPT 生成（经用户传递）
outbox/   TASK_005 RESULT — 由 Codex 产出（经用户传递）
reviews/  TASK_005 REVIEW — 由 Claude 产出 ✅
decisions/ TASK_005 DECISION — 由 Claude 产出 ✅
```

TASK_005 流程闭环。
