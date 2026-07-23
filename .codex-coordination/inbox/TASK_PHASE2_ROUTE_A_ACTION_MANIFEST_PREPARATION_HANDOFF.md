# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT v1.0 — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF |
| Phase | Phase 2 Track C |
| Route | Route A |
| Purpose | Action Manifest Preparation Authorization Request |
| Current Authorization | **HANDOFF MATERIALIZATION ONLY** |
| Requested Authorization | **PREPARATION FOR ACTION MANIFEST ONLY** |
| Action Manifest Instance | **NOT CREATED / NOT AUTHORIZED** |
| Physical Evidence Acquisition Execution | **BLOCKED** |
| Implementation | **NOT AUTHORIZED** |

Materialization of this Handoff creates only a governance authorization request. It does not authorize Manifest preparation, creation of any output listed below, material access, file inspection, hashing, evidence registration, execution, or legal reasoning.

## 1. Task Identity and Purpose

```yaml
task_id: TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF
phase: Phase 2 Track C
route: Route A
task_type: Governance Handoff Asset
purpose: Action Manifest Preparation Authorization Request
execution_mode: PREPARATION_ONLY_IF_SEPARATELY_APPROVED
```

The requested future task is to prepare one governance-controlled Action Manifest draft that identifies candidate action rows without performing those actions.

The Handoff is not:

- an Action Manifest instance;
- a material-access grant;
- an execution activation decision;
- an Evidence Registry update;
- implementation authority.

## 2. Background and Governance Position

The upstream control chain is:

```text
LEGAL_REASONING_GOVERNANCE_PATTERN
        ↓
Evidence Infrastructure Design
        ↓
Design Validation
        ↓
Input Readiness Recovery
        ↓
Physical Evidence Acquisition Design
        ↓
Physical Evidence Acquisition Execution Handoff
        ↓
Action Manifest Design
        ↓
THIS PREPARATION HANDOFF
```

The current gap is not evidence-model design, input governance, or execution-protocol design. The current gap is a separately reviewed authorization entry for preparing a non-executable Manifest draft.

The Action Manifest Design defines three authorization levels:

| Level | Name | Current State |
|---|---|---|
| 0 | Design Authorization | **COMPLETE — DESIGN ASSETS EXIST** |
| 1 | Manifest Preparation Authorization | **REQUESTED BY THIS HANDOFF / NOT YET GRANTED** |
| 2 | Execution Authorization | **NOT AUTHORIZED** |

## 3. Fixed Asset Binding

Before any later preparation begins, Codex must recompute and exactly match all three inputs. A missing or mismatched artifact yields `BLOCKED` and prohibits preparation outputs.

| Artifact | Path | SHA-256 |
|---|---|---|
| Physical Evidence Acquisition Execution Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_HANDOFF.md` | `CF3F786204BD647B6D2597F4EA3FD14BAC8713FB7F7CBADE001A390E122CAF4D` |
| Action Manifest Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN_SPEC.md` | `B9A4B69012F9EEEF786D730684B208E601934472C9A4562F702DF3650B799ECF` |
| Action Manifest Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN_RESULT.md` | `8A46792D81E291316A21E83857BC6B95D134BCC2FBBAE8255A337D5F572F756B` |

This Handoff may request application of those controls but may not amend, reinterpret, or supersede them.

## 4. Authorization Request

```yaml
authorization_request:
  requested_phase: ACTION_MANIFEST_PREPARATION
  requested_scope:
    - CREATE_MANIFEST_DRAFT
    - DEFINE_ACTION_ITEM
    - BIND_HUMAN_SUPPLIED_MATTER_IDENTIFIER
    - DEFINE_EVIDENCE_CATEGORY
    - RECORD_PENDING_SOURCE_AND_PATH_FIELDS
    - VALIDATE_DRAFT_SCHEMA
  excluded_scope:
    - MATERIAL_ACCESS
    - DIRECTORY_SEARCH
    - FILE_INSPECTION
    - FILE_READ
    - FILE_COPY
    - FILE_MOVE
    - HASH_OPERATION
    - SOURCE_AUTHENTICITY_DETERMINATION
    - EVIDENCE_REGISTRY_UPDATE
    - STATUS_EXECUTION
    - OCR_OR_EXTRACTION
    - LEGAL_REASONING
```

### 4.1 Permitted Preparation Activity After Separate Approval

If Project Owner approval is later bound to this physical Handoff SHA-256, Codex may only:

1. create the Preparation Spec;
2. create a single Manifest draft using metadata and identifiers explicitly supplied by authorized humans or frozen upstream design rows;
3. record unresolved source, local path, access, and human-confirmation fields as pending;
4. validate draft completeness and fail-closed status;
5. create the Preparation Result.

### 4.2 Preparation Cannot Perform Execution

Preparation cannot:

- discover a file or infer a path;
- open, inspect, read, copy, move, convert, hash, upload, or download material;
- confirm source authenticity, ownership, authority, or case identity;
- register evidence or advance an evidence lifecycle;
- create a Legal Fact, request right, strategy, or conclusion.

## 5. Future Output Contract

Approval of this Handoff may authorize only the following three future outputs:

### Output A — Preparation Spec

```text
docs/phase2/route-a/
TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_SPEC.md
```

Purpose: define the preparation procedure, row-selection rules, pending-field rules, schema validation, and stop conditions.

### Output B — Preparation Result

```text
.codex-coordination/outbox/
TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_RESULT.md
```

Purpose: record input hashes, draft identity, validation outcomes, blockers, Git state, and zero material-access drift.

### Output C — Action Manifest Draft

```text
.codex-coordination/outbox/
TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DRAFT.md
```

The draft must always remain:

```yaml
status: DRAFT
execution_authorization: NOT_GRANTED
```

The following states are prohibited during preparation:

```text
APPROVED
EXECUTION_READY
EXECUTED
VERIFIED
```

No other output is authorized.

## 6. Manifest Draft Contract

The future draft is a governance candidate only and must use the following minimum structure:

```yaml
manifest_instance:
  manifest_id: "required stable draft identifier"
  version: "v0.1-draft"
  status: DRAFT
  matter_id: "human-supplied stable identifier or PENDING_CONFIRMATION"
  case: "CASE-A | CASE-B | CASE-C"
  evidence_category: "frozen planning row category or PENDING_CONFIRMATION"
  planning_row_id: "A-P01..A-P11 | B-P01..B-P05 | C-P01..C-P04"
  source: PENDING_CONFIRMATION
  local_path: PENDING_CONFIRMATION
  access_scope: PENDING_CONFIRMATION
  authorized_action: []
  prohibited_action:
    - MATERIAL_ACCESS
    - FILE_READ
    - FILE_COPY
    - HASH_OPERATION
    - REGISTRY_UPDATE
    - LEGAL_REASONING
  human_confirmation:
    status: PENDING
    reviewer_id: null
    confirmed_scope: null
    decided_at: null
  state: DRAFT
```

### 6.1 Matter and Category Binding

- `matter_id` may be populated only from an attributable human-supplied stable identifier. Otherwise it remains `PENDING_CONFIRMATION`.
- `planning_row_id` must use a frozen ID from the upstream design. A descriptive label or numeric count cannot replace it.
- A current-instruction candidate remains a candidate and cannot be marked required by Codex.

### 6.2 Local Path

During preparation:

```yaml
local_path: PENDING_CONFIRMATION
```

No search, directory enumeration, guessing, or path validation is permitted. A later separately authorized manifest amendment may record an exact human-supplied path, freeze a new manifest SHA-256, and re-enter Architecture Review before any activation decision.

### 6.3 Source

During preparation, `source` remains `PENDING_CONFIRMATION` unless a pre-existing, attributable, human-verified source record is explicitly included in the authorized inputs. Recording that statement does not verify the material or create execution authority.

### 6.4 Authorized Action

During preparation, the list remains empty:

```yaml
authorized_action: []
```

The draft may record proposed action types in a separate non-executable field, but no proposed value becomes an authorized action without a new reviewed manifest version and separate Level 2 activation decision.

## 7. Case and Identity Rules

### 7.1 CASE-A

Only `A-P01` through `A-P11` may be proposed. The seven current-instruction candidate rows remain individually pending qualified-human confirmation and cannot be promoted in bulk.

### 7.2 CASE-B

Only `B-P01` through `B-P05` may be proposed. Matter binding remains pending unless an attributable human supplies the stable matter identity. A matching filename, directory, or entity string is insufficient.

### 7.3 CASE-C

Only `C-P01` through `C-P04` may be proposed. CASE-C remains:

```text
BLOCKED — IDENTITY FIRST
```

Document, source, matter, entity, and qualified-human binding decisions must remain separate and pending until actually supplied.

## 8. Fixed Boundary Rules

```text
No Material Access
No Broad or Targeted Directory Search
No File Inspection or Reading
No Copy, Move, Download, Upload, or Conversion
No Hash Computation or Registration Against Case Material
No Evidence Registry Update
No Evidence Lifecycle Advancement
No OCR or Automatic Extraction
No Database or Storage Construction
No MCP Integration
No Agent Development or Modification
No Skill Modification
No Workflow or Runtime Schema Modification
No Code or Test Script Creation
No Legal Reasoning
No Fact or Legal Fact Formation
No Request-Right Analysis
No Strategy or Outcome Prediction
```

Violation or ambiguity yields `BLOCKED` and no preparation output beyond the truthful Result permitted by a future approval.

## 9. Architecture Review Acceptance Criteria

### AMP-H-001 — SHA Binding

PASS when this Handoff binds the physical Execution Handoff and both Action Manifest Design outputs to exact matching SHA-256 values.

### AMP-H-002 — Authorization Scope

PASS when requested authority is limited to a DRAFT manifest and preparation documents.

### AMP-H-003 — No Material Access

PASS when preparation cannot search, inspect, read, copy, move, hash, register, or update any physical material.

### AMP-H-004 — No Legal Reasoning

PASS when the Handoff prohibits evidence interpretation, fact determination, Legal Fact formation, request-right analysis, strategy, and prediction.

### AMP-H-005 — Identity Gate

PASS when frozen planning-row IDs, human-supplied matter identity, and separate document/source/matter/entity decisions are preserved, with CASE-C blocked.

### AMP-H-006 — Preparation Is Not Execution

PASS when Handoff materialization, preparation approval, Manifest draft creation, Manifest review, and execution activation remain distinct governance transitions.

## 10. Required Governance Sequence

```text
Preparation Handoff Materialized
        ↓
Architecture Coordinator Review
        ↓
Project Owner Preparation Decision
        ↓
Preparation Spec + DRAFT Manifest + Preparation Result
        ↓
Architecture Coordinator Manifest Review
        ↓
Project Owner Level 2 Activation Decision
        ↓
Exact Activated Action Rows Only
```

The following shortcut is prohibited:

```text
Handoff
  ↓
Manifest Draft or Physical Action
```

## 11. Current Governance State

```text
Action Manifest Design:
DESIGN ASSETS CREATED

Action Manifest Preparation Handoff:
MATERIALIZED AFTER THIS TASK — PENDING REVIEW

Manifest Preparation:
NOT AUTHORIZED

Action Manifest Instance:
NOT CREATED

Physical Evidence Acquisition Execution:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next governance recipient is the **Architecture Coordinator (ChatGPT)** for file-level review of this physical Handoff SHA-256. No Preparation output or Manifest draft may be created before that review and a separate Project Owner decision.
