# TASK_PHASE2_C02_I_CASE_INPUT_BINDING_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Input Governance Handoff

GOVERNANCE LAYER: Input Asset Authorization

TARGET: C02-I Request Right Foundation Validation

IMPLEMENTATION: NOT AUTHORIZED

VALIDATION EXECUTION: BLOCKED UNTIL INPUT BINDING COMPLETE

SKILL / AGENT / CODE MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C02-I Case Input Binding and Manifesting**.

The objective is to audit the workspace, identify exact repository paths and SHA-256 hashes of the raw input materials for the three validation cases, and establish a formal Input Binding Manifest.

This phase is **read-only and documentation-only**. No actual editing of skill prompts, rewriting agent definitions, or modifying code is authorized.

## 2. Governance Position

```text
C02-I Request Right Validation Design (APPROVED)
        ↓
C02-I Case Input Binding (This Task, Read-Only)
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

## 4. Binding Case Manifest Requirements

The executor must look up, catalog, and bind the following case files:

### 4.1 CASE-A: Muxi Shoes (C02-CASE-A-001)
- Contract, correspondence, billing, payments, or other transaction files.

### 4.2 CASE-B: Subofang (C02-CASE-B-001)
- Judicial decisions, corporate records, shareholder lists, financial flows, or enforcement docs.

### 4.3 CASE-C: Zhang Chengqi (C02-CASE-C-001)
- Enforcement files, asset clues, property records, or derivative litigation files.

Each entry must list path, SHA-256, type, access scope, and validation boundary.

## 5. Input Boundary

### Allowed
- Read verified input materials located in authorized workspace paths;
- Log file paths, formats, sizes, and hashes.

### Prohibited
- Reading outside the authorized directories;
- Synthesizing mock facts or relying on history contexts to compensate for missing files.

## 6. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Case Input Binding Manifest
- Path: `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_MANIFEST.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_INPUT_BINDING_RESULT.md`

## 7. Acceptance Criteria

- **AC-C02-BIND-001**: Every case records a unique ID.
- **AC-C02-BIND-002**: Every input file lists path and active SHA-256.
- **AC-C02-BIND-003**: Missing material results in a `BLOCKED` status in Output B; no analysis can proceed.
- **AC-C02-BIND-004**: No Skills, Agents, Workflows, or code are created or modified.
- **AC-C02-BIND-005**: `git diff --check` passes and staging remains empty at closeout.
