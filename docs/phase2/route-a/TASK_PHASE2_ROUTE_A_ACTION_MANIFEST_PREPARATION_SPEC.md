# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_DESIGN |
| Mode | **PREPARATION DESIGN ONLY** |
| Authorization Source | Project Owner decision as conveyed by Architecture Coordinator on 2026-07-23 |
| Action Manifest Instance | **NOT CREATED / NOT AUTHORIZED** |
| Physical Evidence Acquisition Execution | **BLOCKED** |
| Implementation | **NOT AUTHORIZED** |

This document designs the governance process that may later transform an adopted Action Manifest design into a candidate Manifest instance. It does not create that instance, populate a real path, bind real case material, or authorize execution.

## 1. Purpose

The Preparation layer controls the future transition:

```text
Adopted Action Manifest Design
        ↓
Preparation Governance
        ↓
Manifest Instance Candidate
```

Core principle:

```text
Preparation creates a candidate structure.
Preparation does not authorize execution.
```

The Preparation layer must:

- bind the future candidate to exact adopted design assets;
- define which identifiers and categories may be proposed without accessing material;
- keep real source, path, access, and human decisions pending;
- validate schema, action allowlists, identity controls, and fail-closed states;
- require new review and approval before a Manifest instance is created;
- preserve a separate execution activation gate after instance creation.

## 2. Fixed Input Binding

| Input | Path | SHA-256 | Role |
|---|---|---|---|
| Preparation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF.md` | `3E3254C9E800A82B355ABA30DB4B10D1A814DA4B17FD3B3D145718A281EE654C` | Defines preparation-only authorization request and boundaries |
| Action Manifest Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN_SPEC.md` | `B9A4B69012F9EEEF786D730684B208E601934472C9A4562F702DF3650B799ECF` | Defines core schema, three authorization levels, action registry, and state machine |
| Action Manifest Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN_RESULT.md` | `8A46792D81E291316A21E83857BC6B95D134BCC2FBBAE8255A337D5F572F756B` | Confirms `AM-001` through `AM-006` and outstanding execution blockers |
| Physical Evidence Acquisition Execution Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_HANDOFF.md` | `CF3F786204BD647B6D2597F4EA3FD14BAC8713FB7F7CBADE001A390E122CAF4D` | Preserves E0–E4 controls and the execution boundary |

Any future Preparation task must recompute every required hash. Missing or mismatched input yields `BLOCKED` and prohibits candidate-instance creation.

## 3. Scope and Non-Goals

### 3.1 Authorized Design Scope

This design defines:

- the Preparation workflow and state machine;
- the Preparation data model;
- field-source and pending-value rules;
- future Manifest-instance generation requirements;
- the instance-creation gate;
- the fixed action allowlist;
- CASE-A/B/C preparation adapters;
- validation and stop conditions;
- human-review ownership.

### 3.2 Prohibited Scope

This design does not authorize or perform:

```text
Real Manifest Instance Creation
Real Case or Matter Binding
Real Local Path Population
Directory or File Search
File Inspection or Reading
File Copy, Move, Download, Upload, or Conversion
Hash Computation Against Case Material
Evidence Registry Update
Evidence Lifecycle Advancement
OCR or Automatic Extraction
Database, MCP, Agent, Skill, Workflow, Runtime Schema, or Code Change
Evidence Interpretation
Fact or Legal Fact Formation
Request-Right Analysis
Litigation Strategy or Outcome Prediction
```

## 4. Preparation Governance Model

### 4.1 Separation of Objects

The following objects are distinct:

| Object | Purpose | Executable? |
|---|---|---|
| Action Manifest Design | Defines the canonical control model | No |
| Preparation Design | Defines how a candidate may later be prepared | No |
| Preparation Work Record | Records future preparation steps | No |
| Manifest Instance Candidate | Proposed, non-executable instance | No |
| Reviewed Manifest Instance | Exact physical instance accepted by Architecture Review | No |
| Activated Manifest Instance | Exact rows activated by Project Owner decision | Only activated rows |
| Execution Record | Records an actual authorized operation | Not itself authority |

No object inherits authority from the preceding object automatically.

### 4.2 Preparation Ownership

| Decision | Owner |
|---|---|
| Design-model interpretation | Architecture Coordinator |
| Stable matter identifier supply | Qualified human matter owner |
| Requiredness of a candidate category | Qualified lawyer / Project Owner as applicable |
| Source, path, access, and authority confirmation | Attributable authorized human |
| Candidate schema generation | Codex after separate instance-creation authorization |
| Manifest review | Architecture Coordinator |
| Execution activation | Project Owner |
| Legal judgment | Qualified lawyer |

Codex may record an actual supplied decision. It may not manufacture, infer, or silently substitute a human decision.

## 5. Preparation Data Model

The following is a design schema, not a populated record:

```yaml
manifest_preparation:
  preparation_id: "required stable preparation identifier"
  version: "required immutable version"
  state: PREPARATION_DESIGN

  based_on:
    preparation_handoff_path: ".codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_HANDOFF.md"
    preparation_handoff_sha256: "3E3254C9E800A82B355ABA30DB4B10D1A814DA4B17FD3B3D145718A281EE654C"
    action_manifest_design_spec_sha256: "B9A4B69012F9EEEF786D730684B208E601934472C9A4562F702DF3650B799ECF"
    action_manifest_design_result_sha256: "8A46792D81E291316A21E83857BC6B95D134BCC2FBBAE8255A337D5F572F756B"

  matter_binding:
    symbolic_case_adapter: "CASE-A | CASE-B | CASE-C"
    matter_id: PENDING_HUMAN_CONFIRMATION
    binding_source: NOT_AVAILABLE
    identity_status: PENDING

  evidence_scope:
    planning_row_id: "A-P01..A-P11 | B-P01..B-P05 | C-P01..C-P04"
    category: "frozen category label"
    target: CANDIDATE_ONLY
    requiredness: PENDING_HUMAN_CONFIRMATION

  environment_fields:
    source: PENDING_CONFIRMATION
    local_path: PENDING_CONFIRMATION
    access_scope: PENDING_CONFIRMATION
    file_identity: NOT_ACCESSED
    observed_hash: NOT_COMPUTED

  action_scope:
    proposed_action:
      - "zero or more allowlisted proposals"
    authorized_action: []
    prohibited_action:
      - MATERIAL_ACCESS
      - FILE_READ
      - FILE_COPY
      - HASH_OPERATION
      - REGISTRY_UPDATE
      - LEGAL_REASONING

  confirmation:
    required: true
    status: PENDING
    reviewer_id: null
    confirmed_scope: null
    decided_at: null

  validation:
    schema_status: NOT_RUN
    identity_gate: PENDING
    action_allowlist: NOT_RUN
    execution_isolation: REQUIRED
```

### 5.1 Symbolic Case Adapter Is Not a Matter Binding

This design may use `CASE-A`, `CASE-B`, or `CASE-C` as a symbolic adapter identifier. It may not claim that a real matter has been bound.

```yaml
symbolic_case_adapter: CASE-A
matter_id: PENDING_HUMAN_CONFIRMATION
```

Using `CASE-A` in a schema example does not create a case-material association.

### 5.2 Environment Facts Remain Pending

Real source, path, access, file identity, and observed hash are Execution Environment Facts. During Preparation Design they remain:

```yaml
source: PENDING_CONFIRMATION
local_path: PENDING_CONFIRMATION
access_scope: PENDING_CONFIRMATION
file_identity: NOT_ACCESSED
observed_hash: NOT_COMPUTED
```

No path example using `C:\...`, a wildcard, a directory, a URL, or a network share may be inserted into a candidate by this design task.

## 6. Preparation State Machine

```text
PREPARATION_DESIGN
        ↓
PREPARATION_DRAFT
        ↓
ARCHITECTURE_REVIEW
        ↓
PROJECT_OWNER_APPROVAL
        ↓
MANIFEST_INSTANCE_CREATED
        ↓
MANIFEST_INSTANCE_REVIEW
        ↓
EXECUTION_GATE
```

### 6.1 Transition Rules

| Transition | Required Condition |
|---|---|
| `PREPARATION_DESIGN → PREPARATION_DRAFT` | Preparation Design reviewed and adopted; separate draft-preparation authorization issued |
| `PREPARATION_DRAFT → ARCHITECTURE_REVIEW` | Draft schema complete; all unknown environment facts explicitly pending; output SHA frozen |
| `ARCHITECTURE_REVIEW → PROJECT_OWNER_APPROVAL` | Architecture Review PASS bound to exact draft SHA |
| `PROJECT_OWNER_APPROVAL → MANIFEST_INSTANCE_CREATED` | Separate Project Owner instance-creation decision bound to exact reviewed draft |
| `MANIFEST_INSTANCE_CREATED → MANIFEST_INSTANCE_REVIEW` | Physical instance created with immutable version and SHA; no action executed |
| `MANIFEST_INSTANCE_REVIEW → EXECUTION_GATE` | Exact instance passes review; separate activation request may be submitted |

### 6.2 Forbidden Transitions

```text
PREPARATION_DESIGN → MANIFEST_INSTANCE_CREATED
PREPARATION_DESIGN → EXECUTION_GATE
PREPARATION_DRAFT → EXECUTION_GATE
PROJECT_OWNER_APPROVAL → EXECUTED
PENDING/BLOCKED → EXECUTION_READY
```

Architecture acceptance of a design or draft is not an execution decision.

## 7. Manifest Instance Creation Gate

Every gate must pass before a future Manifest instance may be created.

### Gate 1 — Design Asset Binding

Required:

- Action Manifest Design Spec SHA-256;
- Action Manifest Design Result SHA-256;
- Preparation Design Spec SHA-256;
- Preparation Design Result SHA-256;
- approved instance-creation Handoff and Decision identities.

Failure result: `BLOCKED — ARTIFACT IDENTITY`.

### Gate 2 — Matter Scope

Required:

- an attributable human-supplied stable `matter_id`;
- symbolic case adapter;
- explicit matter-binding scope and limitations.

Failure result: `BLOCKED — MATTER IDENTITY`.

### Gate 3 — Evidence Category

Required:

- one frozen planning row ID;
- the canonical category label from the Evidence Model;
- an explicit human requiredness decision for any candidate category.

Failure result: `BLOCKED — CATEGORY CONFIRMATION`.

### Gate 4 — Proposed Action Legality

Only these proposals are valid:

```text
REGISTER_EVIDENCE
HASH_REGISTER
SOURCE_CONFIRM
HUMAN_VERIFY
STATUS_UPDATE
```

At instance-creation time these values remain proposals. `authorized_action` remains empty until a separate Level 2 activation decision.

Failure result: `BLOCKED — ACTION OUTSIDE ALLOWLIST`.

### Gate 5 — Human Confirmation Requirement

The candidate must identify which human decisions are required, who owns them, and what scope must be confirmed. Missing actual decisions remain `PENDING` and cannot be inferred.

Failure result: `BLOCKED — HUMAN CONFIRMATION REQUIRED`.

### Gate 6 — Environment-Fact Isolation

Preparation Design must not populate or validate real paths, inspect sources, or compute material hashes. Those values remain pending until separately authorized and human supplied.

Failure result: `BLOCKED — EXECUTION ENVIRONMENT FACT`.

## 8. Instance Generation Requirements

A future instance-generation task, if separately authorized, must:

1. use one immutable `manifest_id` and version;
2. bind all adopted design and preparation hashes;
3. use only frozen planning-row IDs;
4. distinguish symbolic case adapters from real matter IDs;
5. preserve pending real-world fields without guessing;
6. keep `status: DRAFT`;
7. keep `authorized_action: []`;
8. keep `execution_authorization: NOT_GRANTED`;
9. prohibit all material operations;
10. return the physical instance SHA for review.

It must not set:

```text
APPROVED
EXECUTION_READY
EXECUTED
VERIFIED
ANALYSIS_READY
```

## 9. CASE Adapter Preparation Design

### 9.1 CASE-A

Supported design groups:

```text
Corporate
Contract / Transaction
Payment
Communication / Delivery
```

Only `A-P01` through `A-P11` may appear. The seven current-instruction candidate rows remain individually pending human requiredness confirmation. Preparation cannot perform transaction-fact analysis or infer a contract, debt, agency, delivery, or payment relationship.

### 9.2 CASE-B

```yaml
symbolic_case_adapter: CASE-B
identity_gate: REQUIRED
identity_status: IDENTITY_PENDING
matter_id: PENDING_HUMAN_CONFIRMATION
```

Only `B-P01` through `B-P05` may appear. Filename, directory, entity-string, or historical-location similarity cannot bind material to CASE-B.

### 9.3 CASE-C

```yaml
symbolic_case_adapter: CASE-C
identity_rule: IDENTITY_FIRST
identity_status: BLOCKED
matter_id: PENDING_HUMAN_CONFIRMATION
```

Only `C-P01` through `C-P04` may appear. Similar names cannot establish the same entity or matter. No candidate may leave `BLOCKED` until the separate document, source, matter, entity, and human-binding decisions are actually supplied.

## 10. Validation Rules and Stop Conditions

### 10.1 Schema Validation

- all required design fields must exist;
- unknown values must use controlled pending values, not blanks or guesses;
- hashes must be 64-character uppercase hexadecimal when applicable;
- planning row IDs must belong to the correct case adapter;
- `authorized_action` must be empty in Preparation Design and candidate-generation stages;
- real paths and observed hashes must not be present.

### 10.2 Governance Validation

- every state transition must have a separate authority artifact;
- Architecture Review and Project Owner decisions remain distinct;
- Manifest instance creation and execution activation remain distinct;
- an absent decision yields `BLOCKED`, not implied approval.

### 10.3 Mandatory Stop Conditions

Stop without creating or advancing a Manifest instance when:

- any bound input hash mismatches;
- matter identity is missing or ambiguous;
- category requiredness is unconfirmed;
- a proposed action is outside the allowlist;
- a real source, path, or material operation is requested;
- human confirmation is missing;
- legal reasoning or evidence interpretation is requested;
- a state transition would skip review or approval.

## 11. Human Review Boundary

AI/Codex may design structure and validate syntax. It cannot decide:

- whether a real matter ID is correct;
- whether material belongs to a matter or entity;
- whether a candidate category is legally required;
- whether a source is authentic or authorized;
- whether a path may be accessed;
- whether evidence proves a fact or Legal Fact;
- whether any action should be activated.

Those decisions remain attributable human decisions and must preserve uncertainty, limitations, and conflicts.

## 12. Acceptance Criteria

### AMP-D-001 — Preparation Binds Action Manifest Design

PASS when the Preparation Spec binds the exact Handoff, Action Manifest Design Spec, Action Manifest Design Result, and Execution Handoff identities.

### AMP-D-002 — No Real Manifest Instance

PASS when this task creates no Manifest instance and instance generation requires a new reviewed authorization chain.

### AMP-D-003 — No Real Path or Material Access

PASS when real source, local path, access, file identity, and observed hash remain pending and no search/read/copy/hash operation occurs.

### AMP-D-004 — Identity Gate Preserved

PASS when symbolic adapters and real matter IDs remain distinct, and CASE-B/C retain their identity gates.

### AMP-D-005 — Legal Reasoning Isolation

PASS when Preparation cannot interpret evidence, determine facts, form Legal Facts, analyze request rights, generate strategy, or predict outcomes.

### AMP-D-006 — Preparation Is Not Execution

PASS when design, draft, review, approval, instance creation, instance review, and execution activation remain separate and non-skippable.

## 13. Current Governance State

```text
Preparation Design Spec:
CREATED — PENDING ARCHITECTURE REVIEW

Preparation Design Result:
CREATED WITH THIS TASK

Preparation Draft:
NOT CREATED

Action Manifest Instance:
NOT CREATED / NOT AUTHORIZED

Physical Evidence Acquisition Execution:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next recipient is the **Architecture Coordinator (ChatGPT)** for review of this Spec and the paired Result. Adoption of Preparation Design does not authorize a Manifest instance or execution.
