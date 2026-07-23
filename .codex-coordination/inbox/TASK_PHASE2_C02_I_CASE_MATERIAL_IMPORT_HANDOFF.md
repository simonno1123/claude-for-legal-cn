# TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Input Governance Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET: C02-I Request Right Foundation Validation

IMPLEMENTATION: NOT AUTHORIZED

VALIDATION EXECUTION: BLOCKED

SKILL / AGENT / CODE MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C02-I Case Material Import and Binding**.

The objective is to scan the workspace and host machine, identify any files belonging to the Muxi Shoes, Subofang, and Zhang Chengqi cases, register them with their exact paths and SHA-256 hashes, and output an Import Manifest.

This phase is **read-only and documentation-only**. No actual editing of skill prompts, rewriting agent definitions, or modifying code is authorized.

## 2. Governance Position

```text
C02-I Validation Execution (HOLD / BLOCKED)
        ↓
C02-I Case Material Import (This Task, Read-Only Setup)
        ↓
C02-I Validation Execution (READY once materials are bound)
```

No file under `litigation-legal/` may be created or modified.

## 3. Fixed Baseline Inputs

Before execution, the executor must verify:

### 3.1 C02-I Corrected Input Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_MANIFEST.md`
- Required SHA-256: `30D14805E7F9250C52E63B227BD02CA54F763B1E71C41141E3ACBB4E038BAE13`

### 3.2 C02-I Corrected Input Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_RESULT.md`
- Required SHA-256: `47AA406C95B27294328DB1686377AE971CAAEBBD1867B20FAF32AE69E64DE2DB`

### 3.3 C02-I Validation Execution Handoff
- Path: `.codex-coordination/inbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION_HANDOFF.md`
- Required SHA-256: `63E593332E29C6C7F2A1008204CD2B74BBCF223A6FC00E8E0D374713BF49097E`

## 4. Import Scope and Inventory Rules

- **Source Check**: Scan directories and log file parameters (Muxi: 4 items, Subofang: 5 items, Zhang Chengqi: 4 items).
- **Missing Marker**: Pursuant to AC-C02-IMPORT-003, missing files must be explicitly registered as `NOT_FOUND` with `NOT_AVAILABLE` hashes and `NO_READ` boundaries. No virtual mock files or fake case data may be generated.

## 5. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Case Material Import Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_RESULT.md`

## 6. Explicit Exclusions

- Writing or editing Skill files, Agents, workflows, or code;
- Executing actual request-right analysis or producing validation reports.

## 7. Acceptance Criteria

- **AC-C02-IMPORT-001**: Source origins and paths are verified.
- **AC-C02-IMPORT-002**: Material SHA-256 hashes are logged.
- **AC-C02-IMPORT-003**: Gaps are explicitly marked `NOT_FOUND`.
- **AC-C02-IMPORT-004**: No legal analysis or legal opinion is generated.
- **AC-C02-IMPORT-005**: Zero prompt changes or code regressions.
- **AC-C02-IMPORT-006**: `git diff --check` passes and staging remains empty.
