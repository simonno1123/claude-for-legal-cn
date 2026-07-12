# TASK_004_AUDIT_REGULATORY — 流程决策
# 决策方：Claude
# 决策依据：TASK_004 REVIEW artifact
# 决策时间：2026-07-04

---

## 决策

**REJECTED**

regulatory-legal 模块结构合格，法域内容中国化到位，但**核心职责从有状态工作流退化为静态模板**，不满足 Faithful Port v1 职责等价标准。

---

## 状态更新

Baseline Recovery Review A-06（regulatory-legal）：`Valid` → **Invalid**

CHINA_LOCALIZATION_STATUS.md 第 47 行 `PHASE 1 COMPLETE` 标记：**不准确，待修正**

---

## 需修复项

| 优先级 | Skill | 缺失的核心职责 |
|--------|-------|--------------|
| P0 | gap-surfacer | tracker schema、状态分类、owner 路由、reminder |
| P0 | reg-feed-watcher | feed pull/classify/digest/write |
| P0 | gaps | tracker read/write、close/accept |
| P1 | cold-start-interview | config persistence、--redo、--check-integrations |
| P1 | policy-redraft | source-policy 保护、proposed-file output、non-closure guardrails |
| P1 | comments | comment-tracker、decision log、deadline reminder |
| P2 | policy-diff | rule-status check、source-tag、gap-tracker handoff |

---

## 下一步

本 TASK 不关闭，标记为 REJECTED 等待修复。

修复任务应由 **ChatGPT** 生成，交 **Codex** 执行，完成后产出新 RESULT，由 **Claude** 重新审查。

当前审计队列继续推进下一个模块，不因本模块 REJECTED 而阻塞。

---

## 流程文件完整性

```
inbox/    TASK_004 — 由 ChatGPT 生成（经用户传递）
outbox/   TASK_004 RESULT — 由 Codex 产出（经用户传递）
reviews/  TASK_004 REVIEW — 由 Claude 产出 ✅
decisions/ TASK_004 DECISION — 由 Claude 产出 ✅
```

四个 artifact 齐备，TASK_004 流程闭环（结论：REJECTED，待修复后重开）。
