# TASK_010_CORPORATE_WRAPPER_REVIEW — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_010 REVIEW
# 决策时间：2026-07-09

---

## 决策

**ACCEPTED_WITH_CONDITIONS**

`corporate-legal` 的 wrapper 结构审计与职责发现核验通过，但必须限期整改两项细节冲突/缺口。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-10 | corporate-legal wrapper | Pending Review | **Valid (有条件通过，待完成微调)** |

---

## 限制与整改条件

1. **修正冷启动文件冲突表述**：
   - 目标文件：`corporate-legal/skills/cold-start-interview/SKILL.md`
   - 修改 L159 的 `- 不得另设 customize 配置入口；...`，改为 `- 不得另设配置存储源；公司画像（company_profile）必须统一保存在插件的根配置文件中，其自定义更新可通过 /corporate-legal:customize 入口提出建议并由用户确认。`
2. **CLAUDE.md 注入 "No Silent Supplementation" 独立条款**：
   - 目标文件：`corporate-legal/CLAUDE.md`
   - 在 L68 上方或合适位置，新加一级标题：
     ```markdown
     ## No Silent Supplementation

     1. 禁止在未核验法条、注册登记口径或具体章程规则的前提下，自行编造或默认填充事实。
     2. 确有必要提供参考示例时，必须在文本中明确标注 `[待核验]` 或 `[示例建议]`。
     ```

---

## 下一步

本 TASK 关闭，状态更新为 ACCEPTED_WITH_CONDITIONS。

**→ ChatGPT** 基于本 DECISION 生成下一步执行任务书：

```
TASK_011_CORPORATE_ALIGNMENT_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS: corporate-legal/CLAUDE.md, corporate-legal/skills/cold-start-interview/SKILL.md
FORBIDDEN ACTIONS: 修改其他模块、引入美国法概念、新增非本任务指定的文件
REQUIRED OUTPUT ARTIFACT: TASK_011_CORPORATE_ALIGNMENT_EDIT_RESULT.md
```
