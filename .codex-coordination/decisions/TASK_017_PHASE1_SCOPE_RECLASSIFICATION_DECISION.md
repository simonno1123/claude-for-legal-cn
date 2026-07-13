# TASK_017_PHASE1_SCOPE_RECLASSIFICATION — 流程决策
# 决策方：Gemini 3.5 Flash (Technical Reviewer & Decision Maker)
# 决策依据：TASK_017 REVIEW
# 决策时间：2026-07-13

---

## 决策

**ACCEPTED_WITH_RECLASSIFICATION**

接受对 `TASK_016` 审计缺陷的 Phase 1 / Phase 1.5 / Phase 2 三层划分。

项目冻结基线定位调整为：“中国执业律师/企业法务 AI 辅助工具基础层（中国法实体对齐 + 基线可运行性对齐）”。

所有被后移至 Phase 1.5 和 Phase 2 的上游悬挂职责不阻塞 Phase 1 Release Candidate 的冻结与发布。但前提是，所有相关模块声明、README、ROADMAP、MAPPING_MATRIX 必须与当前重分类事实完全一致（即消灭任何文字描述冲突和夸大宣称）。

---

## 状态更新与分类账本 (Scope Registry)

| 资产/缺陷 | 所属分类 | v1 RC 是否阻塞 | 修复后所属阶段 |
|---|---|---|---|
| **B-1 (CI 校验与 MCP 源表失败)** | Phase 1 Mandatory | 🚨 **YES (阻塞)** | Phase 1 (将在 TASK_018 修复) |
| **G-3 (命令断链引用)** | Phase 1 Mandatory | 🚨 **YES (阻塞)** | Phase 1 (将在 TASK_018 修复) |
| **G-4a (WPS schema 域名匹配自洽)** | Phase 1 Mandatory | 🚨 **YES (阻塞)** | Phase 1 (将在 TASK_018 修复) |
| **G-5 (文档/元数据/README stale 残留)** | Phase 1 Mandatory | 🚨 **YES (阻塞)** | Phase 1 (将在 TASK_018 修复) |
| **G-1a/G-2a (Agent 元数据元/Workspace 描述真实性)** | Phase 1 Mandatory | 🚨 **YES (阻塞)** | Phase 1 (将在 TASK_018 修复) |
| **B-2 (产品合规监控 & 事项空间状态化)** | Phase 1.5 Legal Workflow | 🟢 NO (不阻塞) | Phase 1.5 (列入后续待办) |
| **B-4 & G-1b (各模块 Workspace 本地持久化隔离)** | Phase 1.5 Legal Workflow | 🟢 NO (不阻塞) | Phase 1.5 (列入后续待办) |
| **B-3 (涉外用工/境外雇佣实质能力开发)** | Phase 2 Integration | 🟢 NO (不阻塞) | Phase 2 (列入后续待办) |
| **B-5 (Legal Builder Hub 物理执行安装/更新/回滚)** | Phase 2 Integration | 🟢 NO (不阻塞) | Phase 2 (列入后续待办) |
| **B-2c / G-4b (外部系统联动与真实云端 Provider 联调)** | Phase 2 Integration | 🟢 NO (不阻塞) | Phase 2 (列入后续待办) |

---

## 下一步

本 TASK 关闭，判定为 **ACCEPTED_WITH_RECLASSIFICATION**。

**→ ChatGPT** 收集本 Scope Decision，正式下发 **`TASK_018_PHASE1_ALIGNMENT_EDIT`** 任务书至 `inbox/` 目录，指示 Codex 仅针对 **Phase 1 Mandatory** 部分执行物理修复，严禁越权开发 1.5 或 2.0 后移能力。

---

## 流程文件完整性

```
inbox/    TASK_017_PHASE1_SCOPE_RECLASSIFICATION.md         ✅
outbox/   TASK_017_PHASE1_SCOPE_RECLASSIFICATION_RESULT.md  ✅
reviews/  TASK_017_PHASE1_SCOPE_RECLASSIFICATION_REVIEW.md  ✅
decisions/ TASK_017_PHASE1_SCOPE_RECLASSIFICATION_DECISION.md ✅
```

TASK_017 流程闭环。
