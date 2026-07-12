# TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_013 REVIEW
# 决策时间：2026-07-09

---

## 决策

**ACCEPTED**

`managed-agent-cookbooks` 与 `external_plugins` 的对齐编辑通过验收，移出有条件通过状态。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-11 | managed-agent-cookbooks | Valid (有条件通过) | **Valid (完全通过)** |
| A-12 | external_plugins/cocounsel-legal | Valid (有条件通过) | **Valid (完全通过)** |

---

## Commit 建议

建议进行以下 staging 和 commit：

```bash
git add managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml \
        external_plugins/cocounsel-legal/skills/deep-research/SKILL.md \
        external_plugins/README.md
git commit -m "fix(cookbooks): clean box residue and isolate cocounsel with warning"
```

---

## 下一步

托管配方与外部插件的治理生命周期全部闭环。

**→ ChatGPT** 整理状态，并在 `inbox/` 中下发 Phase 2 模块（法学生或法律诊所）的中国化升级任务书。

---

## 流程文件完整性

```
inbox/    TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT.md          ✅
outbox/   TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT_RESULT.md   ✅
reviews/  TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT_REVIEW.md   ✅
decisions/ TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT_DECISION.md  ✅
```

TASK_013 流程物理闭环。
