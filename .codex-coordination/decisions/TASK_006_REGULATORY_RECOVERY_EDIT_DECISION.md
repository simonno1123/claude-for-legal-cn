# TASK_006_REGULATORY_RECOVERY_EDIT — 流程决策
# 决策方：Claude
# 决策依据：TASK_006 REVIEW artifact
# 决策时间：2026-07-04

---

## 决策

**ACCEPTED**

regulatory-legal 模块修复通过验收。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-06 | regulatory-legal | Invalid（TASK_004 REJECTED） | **Valid** |

CHINA_LOCALIZATION_STATUS.md 第 47 行 `PHASE 1 COMPLETE` 标记：**现在准确**（职责已恢复）。

---

## 关闭条件核验

| 条件 | 结果 |
|------|------|
| 18 项缺失职责全部恢复 | ✅ 18/18 |
| CLAUDE.md 4 项护栏恢复 | ✅ 4/4 |
| 中国法内容无回退 | ✅ |
| JSON 可解析 | ✅ |
| Scope 未越界 | ✅ |

---

## Commit 建议

本次修改可提交，建议 commit message：

```
fix(regulatory-legal): restore stateful workflow responsibilities

Restore 18 upstream responsibilities lost in initial port:
cold-start persistence, feed pull/classify, policy-diff rule-status,
gap tracker lifecycle, comment decision logging, policy-redraft
guardrails, and CLAUDE.md operational gates.

14 files changed, 975 insertions(+), 115 deletions(-)
```

**注意**：worktree 中存在 3 个 corporate-legal 先前修改，commit 时应仅 stage regulatory-legal 文件：

```bash
git add regulatory-legal/
git commit
```

此决策不覆盖 corporate-legal 修改的 commit 权限。

---

## 下一步

TASK_004（regulatory-legal 审计）→ TASK_005（recovery plan）→ TASK_006（recovery edit）链路完整关闭。

**→ ChatGPT** 生成下一个模块的审计任务书，继续队列推进。

---

## 流程文件完整性

```
reviews/  TASK_006 REVIEW  — Claude ✅
decisions/ TASK_006 DECISION — Claude ✅
```

TASK_006 流程闭环。
