# TASK_012_COOKBOOKS_AND_EXTERNAL_PLUGINS_AUDIT — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_012 REVIEW
# 决策时间：2026-07-09

---

## 决策

**ACCEPTED_WITH_CONDITIONS**

托管智能体配方与外部 Vendor 插件的中国化审计通过，必须对已发现的一处 Gap 和两处治理边界进行微调整改。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-11 | managed-agent-cookbooks | Pending Review | **Valid (有条件通过，待完成整改)** |
| A-12 | external_plugins/cocounsel-legal | Pending Review | **Valid (有条件通过，待完成整改)** |

---

## 整改条件与要求

1. **清除 `box` SaaS 示例残留**：
   - 目标文件：`managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`
   - 删除所有 `name: box` 相关的 MCP 挂载与服务器配置（第 29 行和第 33 行）。
2. **CoCounsel 技能级安全护栏写入**：
   - 目标文件：`external_plugins/cocounsel-legal/skills/deep-research/SKILL.md`
   - 在其 `frontmatter` 之下、L10 之前新注入警告文字：
     ```markdown
     > [!WARNING]
     > 本技能属于第三方的 Westlaw / 美国法外部插件。除非用户明确指定进行美国法或 Westlaw 检索，本技能默认不被加载，亦不得作为中华人民共和国大陆地区法律检索的默认手段。中国法域检索请导向 `regulatory-legal` 或根目录 `references/` 规范。
     ```
3. **新增外部插件治理说明**：
   - 目标文件：`external_plugins/README.md` [NEW]
   - 阐明三方 Vendor 插件的非激活和边界隔离政策，避免其影响默认的中国法合规环境。

---

## 下一步

本 TASK 关闭，状态更新为 ACCEPTED_WITH_CONDITIONS。

**→ ChatGPT** 基于本 DECISION 生成下一步执行任务书：

```
TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS:
  - managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml
  - external_plugins/cocounsel-legal/skills/deep-research/SKILL.md
  - external_plugins/README.md
FORBIDDEN ACTIONS: 修改其他模块、删除已有的中国法默认配置、新增非本任务指定的文件
REQUIRED OUTPUT ARTIFACT: TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT_RESULT.md
```
