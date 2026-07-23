# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT v1.0 — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF |
| Phase | Phase 2 Track C |
| Route | Route A |
| Purpose | Action Manifest Instance Creation Authorization Request |
| Current Authorization | **HANDOFF MATERIALIZATION ONLY** |
| Requested Authorization | **ACTION MANIFEST INSTANCE CREATION — DESIGNATED DRAFT ONLY** |
| Action Manifest Instance | **NOT CREATED / NOT AUTHORIZED** |
| Physical Evidence Acquisition | **BLOCKED** |
| Implementation | **NOT AUTHORIZED** |

Materialization of this Handoff creates only a governance authorization request. It does not authorize Architecture approval, Manifest-instance creation, real matter or material binding, file access, physical evidence execution, or implementation.

## 1. Task Identity

```yaml
task_id: TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF
phase: Phase 2 Track C
route: Route A
task_type: Governance Handoff Asset
purpose: Action Manifest Instance Creation Authorization Request
requested_output_state: DRAFT
```

The requested future task is to create one non-executable Action Manifest instance draft after this exact physical Handoff has passed Architecture Review and a separate Project Owner decision.

This Handoff is not:

- a Manifest instance;
- an instance-creation decision;
- an execution activation decision;
- a material-access grant;
- an Evidence Registry update;
- Route A implementation authority.

## 2. Fixed Upstream Binding

Before any later instance-creation task begins, Codex must recompute and exactly match all three inputs. Missing or mismatched identity yields `BLOCKED` and prohibits instance creation.

| Artifact | Path | SHA-256 |
|---|---|---|
| Action Manifest Preparation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF.md` | `3E3254C9E800A82B355ABA30DB4B10D1A814DA4B17FD3B3D145718A281EE654C` |
| Action Manifest Preparation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_SPEC.md` | `B622BAAB9D65ED01360F092F4E8B6FF2BD859D9B8C72DE9CD91E3F20F527526F` |
| Action Manifest Preparation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_RESULT.md` | `AC4396496EAA80969994067EE1325E71A667059204191657C4C823B0445E1465` |

This Handoff applies those controls but cannot amend, reinterpret, or supersede them.

## 3. Authorization Request

```yaml
requested_authorization:
  scope: ACTION_MANIFEST_INSTANCE_CREATION_DESIGNATED_DRAFT_ONLY
  permitted_operations:
    - CREATE_MANIFEST_INSTANCE_DRAFT
    - BIND_CONFIRMED_MATTER_ID
    - DEFINE_EVIDENCE_CATEGORY
    - DEFINE_SOURCE_REFERENCE
    - DEFINE_PROPOSED_ACTION_SCOPE
    - REQUEST_HUMAN_CONFIRMATION
    - VALIDATE_DRAFT_SCHEMA
    - RETURN_DRAFT_SHA256
  excluded_operations:
    - READ_FILE
    - SEARCH_DIRECTORY
    - COPY_FILE
    - MOVE_FILE
    - HASH_CASE_FILE
    - OCR_PROCESS
    - REGISTRY_UPDATE
    - FACT_EXTRACTION
    - EVIDENCE_INTERPRETATION
    - LEGAL_ANALYSIS
    - LIABILITY_ASSESSMENT
    - REQUEST_RIGHT_ANALYSIS
    - EXECUTION_ACTIVATION
```

### 3.1 Meaning of Instance Creation

Instance creation means generating a governance document from already authorized metadata and attributable human confirmations. It does not mean discovering, opening, checking, or operating on the referenced material.

### 3.2 No Implied Human Confirmation

Codex may record an actual supplied human decision. It may not infer matter identity, category requiredness, source, access, authority, path, or confirmation from a filename, directory, entity similarity, narrative, or model output.

## 4. Instance Creation Four Gates

All four gates must pass before a future instance draft can be created. A failure yields `BLOCKED` and no instance output.

### Gate 1 — Matter Binding Gate

Required:

```yaml
matter_binding:
  matter_id: "human-supplied stable identifier"
  status: CONFIRMED
  human_confirmation:
    required: true
    reviewer_id: "attributable human identifier"
    confirmed_scope: "exact matter scope"
    decision: CONFIRMED
    decided_at: "ISO-8601 timestamp"
    limitations: "required; may be NONE"
```

Prohibited:

```text
filename similarity → matter binding
directory similarity → matter binding
entity-name similarity → matter binding
historical label → matter binding
```

Failure state:

```text
BLOCKED — MATTER BINDING NOT CONFIRMED
```

### Gate 2 — Evidence Category Gate

The future draft may use only the following controlled category vocabulary:

```text
contract
payment
communication
corporate_record
identity
property
court_document
```

Every category must also bind one exact upstream planning row ID:

```text
CASE-A: A-P01 through A-P11
CASE-B: B-P01 through B-P05
CASE-C: C-P01 through C-P04
```

Prohibited free-form categories include:

```text
important
key_material
relevant_file
other_relevant_material
```

A category label does not establish legal requiredness. Candidate requiredness remains an attributable human decision.

Failure state:

```text
BLOCKED — CATEGORY OUTSIDE CONTROLLED VOCABULARY OR ROW SET
```

### Gate 3 — Source Gate

Allowed source reference values:

```text
court
client
public_registry
opponent
self_provided
PENDING_CONFIRMATION
```

Rules:

- Codex cannot infer source from file contents, filename, metadata, directory, or context.
- `PENDING_CONFIRMATION` is permitted only in a non-executable DRAFT.
- A source label does not establish authenticity, authority, chain of custody, admissibility, or legal effect.
- No source reference authorizes external contact, retrieval, download, or material access.

Failure state:

```text
BLOCKED — SOURCE OUTSIDE CONTROLLED VOCABULARY OR IMPROPERLY INFERRED
```

### Gate 4 — Action Scope Gate

Allowed proposed action values:

```text
HASH_REGISTER
SOURCE_CONFIRM
STATUS_UPDATE
HUMAN_VERIFY
```

During instance creation these remain proposals only:

```yaml
proposed_action:
  - "zero or more allowed values"
authorized_action: []
execution_authorization: NOT_GRANTED
```

Prohibited actions include:

```text
ANALYZE
INFER
CONCLUDE
GENERATE_LEGAL_POSITION
FACT_MAPPING
LEGAL_FACT_FORMATION
REQUEST_RIGHT_ACTIVATION
STRATEGY_GENERATION
OUTCOME_PREDICTION
```

Failure state:

```text
BLOCKED — ACTION OUTSIDE ALLOWLIST
```

## 5. Instance Draft State Lock

The only permitted future instance status is:

```yaml
status: DRAFT
execution_authorization: NOT_GRANTED
authorized_action: []
```

The following states are prohibited during instance creation:

```text
APPROVED
EXECUTABLE
EXECUTION_READY
EXECUTED
VERIFIED
ANALYSIS_READY
```

No path, source, or action proposal changes the DRAFT state or grants authority.

## 6. Future Instance Minimum Contract

If separately authorized, the future instance must use at least:

```yaml
action_manifest_instance:
  manifest_id: "required immutable identifier"
  version: "v0.1-draft"
  status: DRAFT

  authorization_basis:
    instance_creation_handoff_path: ".codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF.md"
    instance_creation_handoff_sha256: "physical SHA frozen after this materialization"
    architecture_review_sha256: "required"
    project_owner_decision_sha256: "required"

  matter_binding:
    matter_id: "required human-confirmed identifier"
    case_adapter: "CASE-A | CASE-B | CASE-C"
    identity_status: "CONFIRMED, except CASE-C remains UNKNOWN/BLOCKED until its special gate passes"
    human_confirmation: "required attributable record"

  evidence_scope:
    planning_row_id: "required frozen row ID"
    category: "required controlled category"
    target_description: "metadata-only description"
    requiredness: "human-confirmed or PENDING_CONFIRMATION"

  source_reference:
    source: "controlled source value"
    confirmation_status: "CONFIRMED | PENDING_CONFIRMATION"

  execution_environment:
    local_path: PENDING_CONFIRMATION
    access_scope: PENDING_CONFIRMATION
    file_identity: NOT_ACCESSED
    observed_hash: NOT_COMPUTED

  action_scope:
    proposed_action: []
    authorized_action: []
    prohibited_action:
      - MATERIAL_ACCESS
      - FILE_READ
      - FILE_COPY
      - HASH_CASE_FILE
      - REGISTRY_UPDATE
      - LEGAL_REASONING

  human_confirmation_request:
    required: true
    requested_scope: "exact unresolved decisions"
    status: PENDING

  execution_authorization: NOT_GRANTED
```

### 6.1 Real Path Isolation

Instance creation does not authorize population or verification of a real path:

```yaml
local_path: PENDING_CONFIRMATION
```

A later separately authorized amendment must bind any exact human-supplied path, freeze a new instance SHA-256, and re-enter review before execution activation can be requested.

### 6.2 No Case-File Hashing

The Handoff may authorize computation of the future governance draft's own SHA-256 after creation. It does not authorize opening or hashing any case-material file. `HASH_REGISTER` remains a non-executable proposal.

## 7. CASE-C Special Control

CASE-C must remain identity-first:

```yaml
CASE-C:
  identity_status: UNKNOWN
  instance_creation_state: BLOCKED
  proposed_identity_confirmation_action:
    type: identity_confirmation_action
    executable: false
```

`identity_confirmation_action` is a governance request marker, not an allowed physical action and must not appear in `authorized_action`.

Required sequence:

```text
Document Identity
        ↓
Source Identity
        ↓
Matter Identity
        ↓
Entity Identity
        ↓
Qualified Human Binding Confirmation
        ↓
Eligible for a new instance-creation request
```

Prohibited:

```text
historical_entity_binding
automatic_relation_confirmation
similar_name → same_entity
legal_fact_generation
```

Until every identity condition is supplied and reviewed, no CASE-C instance draft may be created under this Handoff.

## 8. Future Output Contract

If this Handoff later passes Architecture Review and a Project Owner decision bound to its physical SHA-256, only these future outputs may be created:

### Output A — Action Manifest Instance Draft

```text
.codex-coordination/outbox/
TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_DRAFT.md
```

Required state: `DRAFT / NOT_EXECUTABLE`.

### Output B — Instance Creation Result

```text
.codex-coordination/outbox/
TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_RESULT.md
```

Purpose: record input hashes, gate results, instance SHA if created, blockers, repository checks, and zero material-operation drift.

No other output is authorized.

## 9. Strict Boundary

```text
No Directory Search
No File Discovery or Inspection
No Case-File Read
No Copy, Move, Download, Upload, or Conversion
No Case-File Hashing
No OCR or Automatic Extraction
No Evidence Registry Update
No Evidence Lifecycle Advancement
No Database or Storage Construction
No MCP Integration
No Agent Development or Modification
No Skill Modification
No Workflow or Runtime Schema Modification
No Code or Test Script Creation
No Fact Extraction or Legal Reasoning
No Liability or Request-Right Assessment
No Execution Activation
No Physical Evidence Acquisition
```

Any missing, conflicting, ambiguous, or unauthorized input yields `BLOCKED` and no instance creation.

## 10. Architecture Review Acceptance Criteria

### AMI-H-001 — Matter Binding Control

PASS when a stable matter ID and attributable human confirmation are mandatory, and similarity-based binding is prohibited.

### AMI-H-002 — Evidence Category Control

PASS when categories use the closed vocabulary plus exact frozen planning-row IDs, with no vague free-form category.

### AMI-H-003 — Source Control

PASS when source uses a controlled value or `PENDING_CONFIRMATION`, cannot be model-inferred, and grants no retrieval or authenticity authority.

### AMI-H-004 — Action Scope Control

PASS when only four proposed actions are allowed, `authorized_action` remains empty, and analysis/inference/conclusion actions are prohibited.

### AMI-H-005 — Identity Gate

PASS when document/source/matter/entity/human decisions remain separate and CASE-C stays blocked until its identity sequence completes.

### AMI-H-006 — Instance Creation Is Not Execution

PASS when Handoff materialization, review, Project Owner decision, DRAFT creation, instance review, and execution activation request remain distinct.

## 11. Required Governance Sequence

```text
Instance Creation Handoff Materialized
        ↓
Architecture Coordinator Review
        ↓
Project Owner Instance-Creation Decision
        ↓
Instance DRAFT Creation
        ↓
Instance Review
        ↓
Separate Execution Authorization Request
        ↓
Project Owner Activation Decision
        ↓
Exact Activated Action Rows Only
```

The following shortcuts are prohibited:

```text
Handoff → Instance Draft
Handoff → Physical Action
Instance Draft → Executed
Instance Review → Automatic Activation
```

## 12. Current Governance State

```text
Action Manifest Preparation Design:
DESIGN ASSETS CREATED

Instance Creation Handoff:
MATERIALIZED AFTER THIS TASK — PENDING ARCHITECTURE REVIEW

Action Manifest Instance:
NOT CREATED

Instance Creation Authorization:
NOT GRANTED

Physical Evidence Acquisition:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next recipient is the **Architecture Coordinator (ChatGPT)** for file-level review of this exact physical Handoff SHA-256. No instance or Result may be created before that review and a separate Project Owner decision.
