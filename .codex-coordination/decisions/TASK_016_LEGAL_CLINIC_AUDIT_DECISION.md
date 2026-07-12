# TASK_016_LEGAL_CLINIC_AUDIT — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_016 REVIEW
# 决策时间：2026-07-09

---

## 决策

**REJECTED**

`legal-clinic` 模块目前不具备顶级模块的可发现性，且其时效管理（deadlines）和导师审批（supervisor-review-queue）两个最为核心的有状态工作流完全退化，不能保障合规与执业风险控制。状态设定为 **Invalid（待整改重构）**。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-14 | legal-clinic | Phase-2 (未激活/隐藏) | **Invalid (待整改重构)** |

---

## 下一步

本 TASK 不关闭，标记为 REJECTED。

**→ ChatGPT** 整理本 Decision 结论，在 `inbox/` 目录中下发微调与物理移动的执行任务书：

```
TASK_017_LEGAL_CLINIC_UPGRADE_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS:
  - phase-2/legal-clinic/** (for migration source)
  - legal-clinic/** (for target files creation/overwrites)
  - .claude-plugin/marketplace.json (for registering the plugin)
  - PROJECT_USAGE_GUIDE.md (for correcting the law-student and legal-clinic path references)
  - docs/UPSTREAM_MAPPING_MATRIX.md (for correcting the law-student and legal-clinic path references)
FORBIDDEN ACTIONS: 修改其他非本任务相关的模块、删除中国法概念、越权提交 git commit
REQUIRED OUTPUT ARTIFACT: TASK_017_LEGAL_CLINIC_UPGRADE_EDIT_RESULT.md
```

**注意**：为了彻底关闭文档历史残留，在此任务中特批允许并授权 Codex 修改 `PROJECT_USAGE_GUIDE.md` 与 `docs/UPSTREAM_MAPPING_MATRIX.md`，将其中关于 `law-student` 和 `legal-clinic` 的 `phase-2/` 路径全部修正为顶级路径。
