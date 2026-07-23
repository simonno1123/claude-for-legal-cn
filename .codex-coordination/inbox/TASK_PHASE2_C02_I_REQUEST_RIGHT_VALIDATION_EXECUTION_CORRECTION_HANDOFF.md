# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION_CORRECTION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Validation Execution Correction Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal` / Request Right Foundation Validation

---

## 1. Task Purpose

本 Handoff 用于授权启动：
`C02-I Request Right Validation Execution Correction`

目标是修复在执行授权阶段由于哈希漂移导致的偏差：
- 隔离非法的历史错误执行对象 `35A908D9EA9C42A8...`；
- 重新对齐并绑定最新的物理执行 Handoff `4DE57A1DD1896E2FACAF1A4521B7E5B9663F9CC3D4EE9DCBD0D20C26114ADA7C` 的哈希作为基线；
- 规范 Output A (`TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md`) 和 Output B 的控制契约。

本阶段为 **只读纠错**，不授权修改任何既有代码或 Skill，亦不启动实际分析。

---

## 2. Governance Position

```text
C02-I Validation Execution (REJECTED FOR DRIFT)
        ↓
C02-I Validation Execution Correction (This Task, AUTHORIZED)
        ↓
C02-I Validation Execution (READY once correction closes)
```

No file under `litigation-legal/` may be created or modified.

---

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-I Case Material Import Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST.md`
- Required SHA-256: `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C`

### 3.2 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

---

## 4. Execution Scope and Rules

- **Allowed**: Read verified input materials located in authorized workspace paths; register and update correction manifest details.
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

- **AC-CORRECT-001**: Align Handoff/Result hashes byte-for-byte.
- **AC-CORRECT-002**: Clean baseline mapping; no drift.
- **AC-CORRECT-003**: Zero prompt changes or code regressions under `litigation-legal/`.
- **AC-CORRECT-004**: `git diff --check` passes and staging remains empty.
