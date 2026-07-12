# TASK_008_AUDIT_AI_GOVERNANCE — 流程决策
# 决策方：Gemini 3.5 Flash (接替 Claude)
# 决策依据：TASK_008 REVIEW
# 决策时间：2026-07-09

---

## 决策

**REJECTED**

`ai-governance-legal` 模块虽然在目录结构上完整且命令可发现，但在职责保留度上严重不足（仅保留了 22.7% 的代码行数）。共有 4 个 High 级别和 4 个 Medium 级别的职责缺失，导致上游的“AI系统全生命周期合规管控”有状态工作流退化为了静态表格模板。

---

## 状态更新

| 编号 | 模块 | 旧状态 | 新状态 |
|------|------|--------|--------|
| A-05 | ai-governance-legal | Valid | **Invalid（被拒绝，待修复）** |

---

## 核心缺失职责清单 (需修复)

### 🔴 High 级别

1. **cold-start-interview**: 缺乏持久化配置写入、--redo 支持、--check-integrations 以及种子文档学习能力。
2. **ai-inventory**: 缺乏 persistent 资产台账 (`ai-systems.yaml`) 的 CRUD 核心操作 (list/add/edit/classify/show) 与下一次审查周期追踪。
3. **aia-generation**: 严重缺失。目前仅作为一个极简的 alias 存根，未能继承上游 impact assessment 模板学习、政策一致性比对 (policy-consistency diff) 等深度行为。
4. **policy-monitor**: 从有状态的运行结果 sweep 扫描和漂移更新，退化为了简单的静态漂移分析报告模板，缺乏 Last policy sweep 状态及 gaps 自动同步。

### 🟡 Medium 级别

5. **use-case-triage**: 缺乏 launch gates 结果的 registry 同步和非律师决策审批门控机制。
6. **vendor-ai-review**: 缺乏已配 playbook 自动比对、provisional 临时处理以及采购红线修改建议流程。
7. **matter-workspace**: 缺乏 workspace 的 new/switch/close 隔离生命周期命令支持。
8. **customize**: 缺少与 cold-start-interview 的 update 机制联动，导致自定义更新机制无法真正运行。

---

## 下一步

本 TASK 不关闭，标记为 REJECTED。

**→ ChatGPT** 基于本 DECISION 生成执行任务书：

```
TASK_009_AI_GOVERNANCE_RECOVERY_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS: ai-governance-legal/**
FORBIDDEN ACTIONS: 修改其他模块、删除中国法内容、新增 MCP 物理实现
REQUIRED OUTPUT ARTIFACT: TASK_009_AI_GOVERNANCE_RECOVERY_EDIT_RESULT.md
```
