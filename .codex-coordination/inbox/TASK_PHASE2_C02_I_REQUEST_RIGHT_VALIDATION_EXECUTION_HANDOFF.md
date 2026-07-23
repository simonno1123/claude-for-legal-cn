# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Validation Execution Authorization Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal` / Request Right Foundation Validation

---

## 1. Task Purpose

本 Handoff 用于授权启动：
`C02-I Request Right Validation Execution`

目标：
基于已完成绑定的真实案件输入，对 C01 法律推理框架与请求权基础理论体系进行首次案件级验证。
验证重点是测试事实、法律事实、请求权基础、构成要件、证据对应关系与缺失事项是否能够形成稳定分析链。

本阶段为 **只读验证执行**，不授权修改任何既有代码或 Skill。

---

## 2. Governance Position

```text
C02-I Case Material Import (CLOSED / DONE)
        ↓
C02-I Validation Execution (This Task, AUTHORIZED)
        ↓
C02-II Implementation (NOT AUTHORIZED)
```

No file under `litigation-legal/` may be created or modified.

---

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-I Case Material Import Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST.md`
- Required SHA-256: `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C`

### 3.2 C02-I Case Material Import Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_RESULT.md`
- Required SHA-256: `2269DE1DF06037851B10C5299F0DD0192C44AC7BE010702CD940253562DAEA05`

### 3.3 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

---

## 4. Execution Scope and Rules

- **Allowed**: Read verified input materials located in authorized workspace paths; execute Layer 1-3 request-right mapping for CASE-A, CASE-B, and CASE-C; log findings and missing items.
- **Prohibited**: Overwriting or updating Skill files under `litigation-legal/` or Agent files; making final merits predictions or automated court decisions.

---

## 5. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Request-Right Validation Report
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_REPORT.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_RESULT.md`

---

## 6. Acceptance Criteria

- **AC-C02-I-VAL-001**: Inputs match binding manifests exactly.
- **AC-C02-I-VAL-002**: Traces the 3-Layer Request-Right Foundation analysis.
- **AC-C02-I-VAL-003**: Differentiates evidence and facts strictly.
- **AC-C02-I-VAL-004**: Prohibit win predictions or automated adjudication.
- **AC-C02-I-VAL-005**: Zero prompt changes or code regressions under `litigation-legal/`.
- **AC-C02-I-VAL-006**: `git diff --check` passes and staging remains empty.
