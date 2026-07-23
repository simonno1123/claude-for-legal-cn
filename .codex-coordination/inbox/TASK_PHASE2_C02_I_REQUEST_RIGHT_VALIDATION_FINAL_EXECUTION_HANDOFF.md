# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_FINAL_EXECUTION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Validation Final Execution Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal` / Request Right Foundation Validation

---

## 1. Task Purpose

本 Handoff 用于授权启动：
`C02-I Request Right Validation Final Execution`

本阶段授权对三起案件的已绑定物理文件进行扫描与请求权基础 Layer 1-3 拆解，以验证法学推理框架。本阶段为 **只读验证执行**，不授权修改任何既有代码或 Skill。

---

## 2. Governance Position

```text
C02-I Validation Execution Correction (CLOSED / DONE)
        ↓
C02-I Validation Final Execution (This Task, AUTHORIZED)
        ↓
C02-II Implementation (NOT AUTHORIZED)
```

No file under `litigation-legal/` may be created or modified.

---

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-I Corrected Material Import Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST.md`
- Required SHA-256: `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C`

### 3.2 C02-I Validation Execution Correction Handoff
- Path: `.codex-coordination/inbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION_CORRECTION_HANDOFF.md`
- Required SHA-256: `0ABFBD3938F05C00714C38D2ACF8C2A507F0C91355FBB8734A01556B43CE8358`

### 3.3 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

---

## 4. Execution Scope and Rules

- **Allowed**: Read verified input materials located in authorized workspace paths; execute Layer 1-3 request-right mapping for CASE-A, CASE-B, and CASE-C; log findings and missing items.
- **Prohibited**: Overwriting or updating Skill files under `litigation-legal/` or Agent files; making final merits predictions or automated court decisions.

---

## 5. Authorized Outputs

The executor is authorized to create/overwrite exactly **2 files**:

### Output A: Request-Right Validation Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md`

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
