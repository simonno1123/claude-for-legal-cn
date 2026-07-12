# TASK_016_LEGAL_CLINIC_AUDIT — 审查报告
# 审查方：Gemini 3.5 Flash (接替 Claude)
# 审查依据：Codex RESULT artifact（TASK_016_LEGAL_CLINIC_AUDIT_RESULT）
# 审查时间：2026-07-09
# 审查模式：READ ONLY（基于 RESULT + 本地文件系统交叉验证）

---

## 一、RESULT 事实核验与诊断

经过在本地工作树及上游基线的交叉对比，确认 Codex 在审计报告中陈述的事实均准确属实：

1. **顶级路径与发现性缺失 (P0 - Blocker)**：
   `legal-clinic` 仍挂载于 `phase-2/` 下，且未载入 `marketplace.json`。这破坏了顶级模块的 Parity 发现性，用户无法在本地使用该插件。
2. **核心业务职责退化 (P0 - Blocker)**：
   本模块的代码量严重退化（仅有 306 行，上游基线为 2662 行，缩水达 **88.5%**）。许多原本具有复杂逻辑的系统退化为静态输出模板：
   - **`deadlines`（时效/举证期限管理）**：退化为静态表格，失去了时效台账（Ledger）的 CRUD 和预警机制，对于法援和法律诊所这类时效极其高危的业务而言存在严重隐患。
   - **`supervisor-review-queue`（指导教师审阅队列）**：退化为静态优先级排序，失去了高校诊所/法援中必须存在的“学生撰写 -> 导师审阅/批准/退回（Approve/Return/Log） -> 对外发送”的流程控制。
   - **`client-intake`（案源接待）**：缺少必要的利益冲突审查、分流 triage 及自动对接 deadlines 环节。
   - **`semester-handoff`（学期交接）**：缺少实际交接备忘录的状态生成与归档。
3. **中国化定位较好，但流于表面**：
   虽然融入了中国法律援助中心、12348 公共法律服务、高校法律诊所等国内实体概念，但因底座工作流被抽干，无法实现实质性的工具链辅导。

**诊断结论：ACTION REQUIRED (拒绝通过，必须重构升级)。**

---

## 二、整改框架建议 (Upgrade Plan)

### 1. 顶级模块提升 (P0)
- 将 `phase-2/legal-clinic` 目录**物理提升（Move）**至顶级插件路径 `legal-clinic/`。
- 在 `.claude-plugin/marketplace.json` 中正式注册 `legal-clinic` 插件。
- 修正 `PROJECT_USAGE_GUIDE.md` 和 `docs/UPSTREAM_MAPPING_MATRIX.md` 中的所有 `phase-2/` 陈旧引用。

### 2. 重建时效与导师审批有状态流 (P0)
- **时效管理 (`deadlines`)**：建立 `deadlines-ledger.yaml` 台账系统，实现客观期限（如上诉期、举证期限、劳动仲裁时效）的增删改查与越期预警。
- **导师审查队列 (`supervisor-review-queue`)**：建立 `review-queue.yaml`，硬化导师审查确认动作（批准发表、发回修改、历史日志记录），并禁止学生角色绕过导师直接对外输出法律文书。

### 3. 深化中国特色法援/诊所流程 (P1)
- **`client-intake`**：对接中国《法律援助法》规定的援助条件初审（经济困难标准、案由范围限制），硬化利益冲突检索流程。
- **`semester-handoff`**：实现包含未结案移交、时效警告和 cohort 概况的交接 memo 自动生成。
- **`cold-start-interview`**：初始化诊所类型（高校诊所/基层法援中心/公共服务热线窗口）、带班老师、学生名单和本地时效库。

---

## 三、审查结论

**REJECTED (ACTION REQUIRED)**

`legal-clinic` 模块目前处于 `Invalid` 状态，必须进行物理重构与有状态升级。

---

## 四、Codex RESULT 质量评估

- **诊断深度**：10/10（能够深刻指出 deadlines 与 review-queue 两个核心有状态流退化对法援安全防线带来的危害）。
- **纪律性**：10/10。
