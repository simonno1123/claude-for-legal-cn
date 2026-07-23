# TASK_PHASE2_C02_I_CASE_INPUT_BINDING_CORRECTION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Input Governance Correction Handoff

GOVERNANCE LAYER: Input Asset Authorization

TARGET: C02-I Case Input Binding and Manifesting

IMPLEMENTATION: NOT AUTHORIZED

VALIDATION EXECUTION: BLOCKED

SKILL / AGENT / CODE MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C02-I Case Input Binding Correction**.

The objective is to execute a Correction Cycle to repair the four governance defects identified during the audit of the initial Case Input Binding closeout:
- **Defect-001**: Align actual physical Result hash with coordination Review/Decision bindings.
- **Defect-002**: Align the count of items in the Manifest and the Result for CASE-B (5 items) and CASE-C (4 items).
- **Defect-003**: Populate missing fields (`path`, `type`, `access_scope`, `validation_boundary`) for all missing files in the Manifest.
- **Defect-004**: Correct Git working tree status description in the review and results coordination.

This phase is **read-only and documentation-only**. No actual editing of skill prompts, rewriting agent definitions, or modifying code is authorized.

## 2. Governance Position

```text
C02-I Case Input Binding (REJECTED FOR CORRECTION)
        ↓
C02-I Case Input Binding Correction (This Task, Read-Only Repair)
        ↓
C02-I Validation Execution (BLOCKED)
```

No file under `litigation-legal/` may be modified during this stage.

## 3. Fixed Baseline Inputs

Before execution, the executor must verify that the following baselines exist in the repository and match their designated hashes:

### 3.1 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

### 3.2 C02-I Validation Design Handoff
- Path: `.codex-coordination/inbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_PLAN_HANDOFF.md`
- Required SHA-256: `FB5CBF4EC5A0089E6B3467C9DBB8DCE17299E4AC821B43A8D0FA67131315C429`

## 4. Correction Scope

### Authorized
- Update `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_MANIFEST.md` to add the missing items and fields;
- Update `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_RESULT.md` to align the counts, manifest mappings, and Git status definitions.

### Prohibited
- Modifying any Skill prompt or code under `litigation-legal/` or `agents/`;
- Creating validation specifications or starting request-right analysis.

## 5. Authorized Outputs

The executor is authorized to overwrite/update exactly **2 files**:
1. `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_MANIFEST.md`
2. `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_RESULT.md`

## 6. Acceptance Criteria

- **AC-CORRECT-001 — Hash Chain alignment**: Actual Output A and B hashes must match final review and decision records byte-for-byte.
- **AC-CORRECT-002 — Manifest Completeness**: Manifest contains 4 items for CASE-A, 5 items for CASE-B, and 4 items for CASE-C, with all required fields mapped as `NOT_FOUND` / `UNKNOWN` / `NONE` / `NOT_AVAILABLE`.
- **AC-CORRECT-003 — Git Status Clarified**: Working tree is noted as `NON-CLEAN` due to pre-existing authorized modifications, and repository checks pass.
- **AC-CORRECT-004 — No Implementation drift**: No Skills or Agent parameters are modified.
