# TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Architecture Design Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal` / Request Right Foundation Design

---

## 1. Task Purpose

本 Handoff 用于授权启动：
`C02-II Request Right Framework Design`

目标是开展请求权基础设计大纲构建：
- 构建事实层 -> 法律事实层 -> 请求权要件层的要素分析体系；
- 限制状态标志（`UNKNOWN` / `SUPPORTED` / `BLOCKED`）；
- 严禁任何 merits prediction 胜诉预测与裁判结论。

本阶段为 **只读设计大纲构建**，不授权修改任何既有代码或 Skill。

---

## 2. Governance Position

```text
C02-I Validation Execution (CLOSED / DONE)
        ↓
C02-II Request Right Design (This Task, AUTHORIZED)
        ↓
C02-II Implementation (NOT AUTHORIZED)
```

No file under `litigation-legal/` may be created or modified.

---

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-I Validation Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md`
- Required SHA-256: `FD51E092DC8C4DA3A06BC9FB711D80CEA958E3DE6B6288EE1DB4490A4C6CD94C`

### 3.2 C02-I Validation Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_RESULT.md`
- Required SHA-256: `F0003635F051D9CA89956EBC624F7EE8B285D7A5D8202D85B88C4EBF1664A7B7`

---

## 4. Design Scope and Rules

- **Allowed**: Draft the request-right element validation schema and structure case-verification interfaces.
- **Prohibited**: Editing Skill prompts, Agents, workflows, or code; estimating merits, outcome probability, or success rates.

---

## 5. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Request-Right Framework Design Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_SPEC.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_RESULT.md`

---

## 6. Acceptance Criteria

- **AC-C02-II-001**: Model prioritizes request-right entries.
- **AC-C02-II-002**: Structures Layer 1-3 mappings logic.
- **AC-C02-II-003**: Restricts status indicators to descriptive variables.
- **AC-C02-II-004**: Prohibit win predictions or automated strategy generation.
- **AC-C02-II-005**: Zero prompt changes or code regressions under `litigation-legal/`.
- **AC-C02-II-006**: `git diff --check` passes and staging remains empty.
