# TASK_014_LAW_STUDENT_UPGRADE — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_014 REVIEW
# 决策时间：2026-07-09

---

## 决策

**REJECTED**

`law-student` 模块目前的中国化深度和架构配置违反了根级 Parity 原则，其有状态学习工作流及学术诚信护栏基本丢失。状态设定为 **Invalid（待整改）**。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-13 | law-student | Phase-2 (未激活/隐藏) | **Invalid (待整改重构)** |

---

## 整改与重构核心任务书（TASK_015）要求

### 🔴 结构性重构 (P0)
1. **物理目录移动**：将 `phase-2/law-student/` 目录下的所有文件物理移动（Move）至根目录顶级路径 `law-student/` 下。
2. **注册插件入口**：在 `.claude-plugin/marketplace.json` 中追加 `law-student` 插件的本地路径配置，使其具备根级命令发现能力。

### 🔴 核心职责恢复 (P0/P1)
1. **学术诚信护栏重建**：重写 `CLAUDE.md`、`README.md`、`legal-writing.md` 和 `irac-practice.md`，确立只提供框架性逻辑建议、**绝对禁止代写**的强硬原则。
2. **苏格拉底互动工作流**：在 `socratic-drill.md` 与 `cold-call-prep.md` 中重建 Ask-Wait-Pushback 的提问式反馈交互。
3. **有状态学习环持久化**：重写 `study-plan` 与 `session`，建立本地 `study-plan.yaml` 与 `session_history` 持久化读写流程。

### 🟡 中国法深度填充 (P1)
1. 将 `bar-prep-questions` 的美国法考核对接为**中国国家统一法律职业资格考试（法考）**的科目考纲、客观题干扰项解析与主观题答题逻辑。
2. 将 `case-brief` 的 Case Method 改造为**中国民商事/刑事“案例研习”规范**（包含请求权基础、争点、要件证明与裁判要旨）。
3. 将 `outline-builder` 的知识大纲对接为**中国成文法与司法解释体系**。

---

## 下一步

本 TASK 不关闭，标记为 REJECTED。

**→ ChatGPT** 整理本 Decision 结论，并在 `inbox/` 目录中下发微调与物理移动的具体执行任务书：

```
TASK_015_LAW_STUDENT_UPGRADE_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS:
  - phase-2/law-student/** (for migration source)
  - law-student/** (for target files creation/overwrites)
  - .claude-plugin/marketplace.json (for registering the plugin)
FORBIDDEN ACTIONS: 修改其他非本任务相关的插件、删除中国法既有成文法概念、越权提交 git commit
REQUIRED OUTPUT ARTIFACT: TASK_015_LAW_STUDENT_UPGRADE_EDIT_RESULT.md
```
