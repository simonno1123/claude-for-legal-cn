# TASK_017_PHASE1_SCOPE_RECLASSIFICATION

STATUS: READY

TO: Codex

MODE: READ ONLY

PROJECT:
/Users/zhang/Documents/claude-for-legal-cn

OBJECTIVE:

对 TASK_016_PHASE1_FINAL_AUDIT 中发现的所有 Blocker / Gap 进行范围重新分类。

本任务不是修复任务。

目标：
根据 claude-for-legal-cn 当前定位：

“中国律师 AI 平台基础能力层”

重新判断各项问题属于：

1. Phase 1 Baseline Recovery 必须闭环事项；
2. Phase 1.5 Legal Workflow Layer 建设事项；
3. Phase 2 Advanced Integration / External Capability事项。

避免机械复制 upstream 能力导致项目范围失控。

---

ALLOWED:

READ ONLY:

- 全项目文件读取
- TASK_016_PHASE1_FINAL_AUDIT_RESULT.md
- TASK_016_PHASE1_FINAL_AUDIT_REVIEW.md
- TASK_016_PHASE1_FINAL_AUDIT_DECISION.md
- CHINA_LOCALIZATION_STATUS.md
- UPSTREAM_MAPPING_MATRIX.md
- PROJECT_USAGE_GUIDE.md
- PHASE_2_ROADMAP.md

---

FORBIDDEN:

- 修改任何项目文件
- 创建修复文件
- git add
- git commit
- 调整目录结构
- 修改 Audit 结果

---

RECLASSIFICATION TARGETS:

请重点审查以下事项：

## B-1 Runtime / CI Drift

包括：

- scripts/localization-regression.py
- scripts/mcp-modules.json
- scripts/generate-mcp-configs.py
- phase-2/law-student
- phase-2/legal-clinic

判断：

是否属于 Phase 1 必须修复。

---

## B-2 Product Legal Responsibilities

包括：

- product-legal launch watcher
- product-legal matter-workspace

判断：

是否属于：

A. 基础法律平台能力

或者：

B. 企业 Legal Operation 扩展能力。

---

## B-3 Employment Expansion

包括：

- expansion-kickoff
- expansion-update
- international-expansion

判断：

是否属于：

A. 中国劳动法律基础能力

或者：

B. 跨境用工 / 出海企业扩展能力。

---

## B-4 IP Matter Workspace

判断：

是否属于：

A. 通用 Matter Workspace 基础设施

或者：

B. IP 专业工作流深化能力。

---

## B-5 Legal Builder Hub

包括：

- skill-installer
- skill-updater
- skill-uninstaller
- auto-updater

判断：

是否属于：

A. 平台运行基础能力

或者：

B. Agent 生态扩展能力。

---

## G 类问题

重新分类：

- 文档路径漂移
- WPS schema
- README状态错误
- Mapping Matrix不同步

判断：

是否属于 Phase 1 Release Candidate 必修项。

---

OUTPUT:

生成：

.codex-coordination/outbox/TASK_017_PHASE1_SCOPE_RECLASSIFICATION_RESULT.md


报告格式：

# TASK_017 Scope Reclassification Result


## Executive Summary


## Phase 1 Mandatory Fixes

|Issue|Reason|Decision|
|-|-|-|


## Phase 1.5 Backlog

|Issue|Reason|Decision|
|-|-|-|


## Phase 2 Deferred Items

|Issue|Reason|Decision|
|-|-|-|


## Recommended Next Step


## Risk Assessment
