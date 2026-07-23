# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_DESIGN |
| Mode | **DESIGN ONLY** |
| Authorization | **PREPARATION FOR ACTION MANIFEST ONLY** |
| Action Manifest Instance | **NOT CREATED / NOT AUTHORIZED** |
| Physical Evidence Acquisition Execution | **BLOCKED** |
| Implementation | **NOT AUTHORIZED** |
| Date | 2026-07-22 |

This specification defines the governance model for a future Action Manifest. It is not an Action Manifest instance, an execution notice, an access grant, a material request, or authority to read, copy, hash, register, move, transform, or assess any evidence.

## 1. Purpose and Scope

### 1.1 Purpose

The Action Manifest is the fail-closed control layer between an approved execution intent and a physical action:

```text
Approved Execution Intent
        ↓
Action Manifest Instance
        ↓
Architecture Review
        ↓
Project Owner Activation Decision
        ↓
Exact Authorized Action Row
        ↓
Physical Action
```

Its purpose is to:

- bind every physical operation to one exact matter, evidence target, source, action, path/object, access scope, and accountable human authority;
- prevent unapproved material access and scope expansion;
- prevent evidence intake from becoming evidence interpretation, fact determination, or legal reasoning;
- preserve a complete, hash-bound authorization and execution record;
- keep missing, ambiguous, or unreviewed inputs blocked.

### 1.2 Non-Goals

The Action Manifest is not responsible for:

- evidence interpretation or authenticity determination;
- fact determination or Legal Fact formation;
- legal qualification or admissibility assessment;
- request-right analysis;
- litigation strategy or outcome prediction;
- OCR, transcription, extraction, conversion, database, MCP, Agent, Skill, Workflow, or code implementation;
- contacting a party, court, bank, registry, platform, custodian, or other external source.

Those activities require separate legal, technical, and execution authority. Nothing in this design grants that authority.

## 2. Fixed Design Inputs

| Input | Path / Identity | SHA-256 | Role |
|---|---|---|---|
| Current design instruction | `C:\Users\Administrator\.codex\attachments\c466f65f-2b7f-47c4-b2d9-b874aba8131b\pasted-text.txt` | `6CA911A6DBB0955057F9C5CA409BD58FB9E14919350B387ED8CC70E1540F9137` | Authorizes design preparation only |
| LRG v1.0 | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | Evidence–Fact–Law and human-decision boundary |
| Physical Evidence Acquisition Execution Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_HANDOFF.md` | `CF3F786204BD647B6D2597F4EA3FD14BAC8713FB7F7CBADE001A390E122CAF4D` | Defines E0–E4 activation gates; materialization alone does not authorize execution |
| Physical Evidence Acquisition Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_SPEC.md` | `257ED2A1E16879F9EB50723D91652F7D7C5688C88D586DE6288D8E1888F8512B` | Defines frozen CASE-A/B/C planning rows and identity controls |
| Physical Evidence Acquisition Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_RESULT.md` | `D21A6563CC43374C52B89BD9D371F05B31A126681C2061A14FDDF1E1E4DBF71E` | Records adopted design validation and unresolved risks |

The execution Handoff remains a physical authorization request pending its required review and decision artifacts. This design does not cure or bypass that missing execution chain.

## 3. Three-Level Authorization Model

### Level 0 — Design Authorization

Current level: **ACTIVE**.

Permitted:

- define the manifest schema;
- define validation rules and the action-type registry;
- define case adapters, identity gates, and state transitions;
- define review and activation boundaries.

Not permitted:

- create a populated Action Manifest instance;
- bind or access a physical material;
- perform an action against a source or path.

### Level 1 — Manifest Preparation Authorization

Current level: **NOT AUTHORIZED**.

When separately authorized, Level 1 may permit:

- creating one manifest instance;
- proposing exact action rows;
- binding an already identified target object and exact local locator;
- requesting attributable human confirmation.

Level 1 cannot authorize material access or execution.

### Level 2 — Execution Authorization

Current level: **NOT AUTHORIZED**.

Level 2 requires all of the following:

1. a physical manifest instance with a frozen SHA-256;
2. Architecture Review of that exact manifest SHA-256;
3. a separate Project Owner Execution Activation Decision bound to that exact SHA-256;
4. an exact action row that passes all E0–E4 gates;
5. a named human confirmation record covering the row's matter, target, source, purpose, path/object, access scope, and action.

Approval of this design specification is not Level 2 authorization.

## 4. Action Manifest Data Model

The following is a design schema, not an instance:

```yaml
action_manifest:
  manifest_id: "required stable identifier"
  version: "required immutable version"
  status: "DRAFT"
  created_by: "attributable human or authorized preparer"
  created_at: "ISO-8601 timestamp"

  authorization_basis:
    execution_handoff_path: "required canonical repository path"
    execution_handoff_sha256: "required 64-hex digest"
    architecture_review_id: null
    architecture_review_sha256: null
    project_owner_decision_id: null
    project_owner_decision_sha256: null
    activation_scope: "PREPARATION_ONLY until separately activated"

  actions:
    - action_id: "required unique row identifier"
      planning_row_id: "A-P01..A-P11, B-P01..B-P05, or C-P01..C-P04"
      matter_id: "required stable matter identifier"
      case_adapter: "CASE-A | CASE-B | CASE-C"
      evidence_category: "required frozen or human-approved category"
      evidence_target: "exact target description"
      source:
        source_class: "required"
        source_identity: "required or BLOCKED"
        source_authority_basis: "required or BLOCKED"
      local_path: "exact approved local file path; no glob or directory-wide scope"
      access_scope: "exact read/metadata/hash/registration scope"
      purpose: "bounded non-legal-analysis purpose"
      authorized_action:
        - "one or more registered action types"
      prohibited_action:
        - "explicit row-specific prohibitions"
      human_confirmation:
        reviewer_id: "required attributable person"
        reviewer_role: "required qualified role"
        confirmed_scope: "required exact row scope"
        decision: "CONFIRMED | REJECTED | PENDING"
        decided_at: "ISO-8601 timestamp or null"
        limitations: "required, may be NONE"
      integrity:
        expected_sha256: null
        observed_sha256: null
        hash_meaning: "BYTE_IDENTITY_ONLY"
      identity_gate:
        required: true
        document_identity: "PENDING"
        source_identity: "PENDING"
        matter_identity: "PENDING"
        entity_identity: "PENDING"
        binding_approval: "PENDING"
      execution_state: "DRAFT"
      execution_record_id: null
```

### 4.1 Requiredness Rules

- Blank required fields are invalid; use an explicit controlled value such as `PENDING`, `NOT_AVAILABLE`, or `BLOCKED` where appropriate.
- `local_path` must identify one exact, authorized local file. Wildcards, broad directories, unresolved variables, network shares, URLs, and inferred locations are invalid.
- A file hash proves byte identity only. It does not prove authenticity, admissibility, relevance, truth, or legal effect.
- A current instruction, filename, directory name, or similar entity name cannot substitute for a human matter-binding decision.
- A missing human decision always remains `PENDING` or `BLOCKED`; it cannot be inferred by AI.

## 5. Four-Dimensional Action Boundary

An action row is a candidate for later activation only when all four dimensions are exact:

| Boundary | Question | Required Fields |
|---|---|---|
| Object | What exact evidence target and matter? | `matter_id`, `planning_row_id`, `evidence_category`, `evidence_target` |
| Source | Where did the target come from? | `source_class`, `source_identity`, `source_authority_basis`, `local_path` |
| Action | What exact operation may occur? | `authorized_action`, `access_scope`, `purpose`, `prohibited_action` |
| Authority | Who approved this row and scope? | `reviewer_id`, `reviewer_role`, `confirmed_scope`, `decision`, `decided_at` |

```text
Exact Object
    + Exact Source
    + Exact Action
    + Attributable Authority
    = Executable Scope Candidate
```

This formula yields only a candidate. Level 2 activation remains separately required.

## 6. Action Type Registry

### 6.1 Registered Action Types

| Action Type | Purpose | Maximum Boundary |
|---|---|---|
| `REGISTER_EVIDENCE` | Register an already human-provided evidence object | Metadata registration for one exact file/object |
| `HASH_REGISTER` | Compute and record byte identity | SHA-256 and byte size for one exact approved local file |
| `SOURCE_CONFIRM` | Record a source decision actually supplied by an authorized human | Record only; Codex does not independently certify authenticity or authority |
| `HUMAN_VERIFY` | Record an actual attributable human review decision | Record the supplied decision, scope, limitations, and timestamp |
| `STATUS_UPDATE` | Update evidence lifecycle/readiness status | Only to the highest state supported by recorded inputs and human decisions |

### 6.2 Prohibited Action Types

The following values are invalid and cannot be activated:

```text
LEGAL_ANALYSIS
EVIDENCE_INTERPRETATION
AUTHENTICITY_DETERMINATION
FACT_MAPPING
LEGAL_FACT_FORMATION
REQUEST_RIGHT_ACTIVATION
STRATEGY_GENERATION
OUTCOME_PREDICTION
OCR_PROCESSING
AUTOMATIC_EXTRACTION
EXTERNAL_COLLECTION
THIRD_PARTY_CONTACT
```

Any requested action outside the registered allowlist requires a new Handoff and separate Project Owner authorization.

## 7. State Machine

```text
DRAFT
  ↓
REVIEW_PENDING
  ↓
APPROVED
  ↓
EXECUTION_READY
  ↓
EXECUTED
  ↓
VERIFIED
  ↓
ARCHIVED
```

### 7.1 Transition Conditions

| Transition | Required Conditions |
|---|---|
| `DRAFT → REVIEW_PENDING` | Schema complete; exact inputs and action rows present; manifest SHA frozen; no blank required fields |
| `REVIEW_PENDING → APPROVED` | Architecture Review PASS bound to the exact manifest SHA |
| `APPROVED → EXECUTION_READY` | Separate Project Owner activation bound to the same manifest SHA and exact action-row scope |
| `EXECUTION_READY → EXECUTED` | All E0–E4 gates pass for the row; operation remains within allowlist and exact path scope |
| `EXECUTED → VERIFIED` | Execution record, observed outcome, hash where authorized, and actual human review are recorded |
| `VERIFIED → ARCHIVED` | Closeout review complete; no unresolved identity, scope, or execution conflict |

### 7.2 Forbidden Transitions

The following transitions are prohibited:

```text
DRAFT → EXECUTION_READY
REVIEW_PENDING → EXECUTED
APPROVED → EXECUTED
PENDING/BLOCKED → VERIFIED
MISSING → ANALYSIS_READY
```

No status may be advanced by assumption, filename similarity, the existence of a hash, or an AI-generated approval.

## 8. Validation Rules

Before a manifest instance can leave `DRAFT`, validation must confirm:

1. **Artifact binding:** Handoff, Review, and Decision identities are present and use valid SHA-256 values.
2. **Row identity:** Every action has a unique `action_id` and one frozen `planning_row_id`.
3. **Exact target:** One exact local path/object is provided; no glob, broad directory, or guessed location is used.
4. **Allowed action:** Every `authorized_action` belongs to the fixed allowlist.
5. **Human authority:** The named reviewer, role, scope, decision, timestamp, and limitations are present.
6. **Identity gate:** Document, source, matter, entity, and binding states are explicit.
7. **No legal reasoning:** Neither schema fields nor action payloads request legal conclusions.
8. **Fail closed:** Any missing, conflicting, or ambiguous field results in `BLOCKED` with no physical action.

## 9. Case Adapter Design

The core manifest contains no case logic. Case adapters add only category and identity controls.

### 9.1 CASE-A Adapter

Allowed planning row IDs are exactly `A-P01` through `A-P11`:

| Row Set | Category Group | Control |
|---|---|---|
| `A-P01`–`A-P03` | Corporate / subject identity | Entity and authority identity required |
| `A-P04`–`A-P08` | Transaction / communication / delivery | Evidence status only; no transaction-fact determination |
| `A-P09`–`A-P11` | Payment | Funds-flow status only; no debt, contract, or agency inference |

The seven current-instruction candidates remain candidates until individually confirmed by a qualified human. They cannot be promoted in bulk.

### 9.2 CASE-B Adapter

Allowed planning row IDs are exactly `B-P01` through `B-P05`.

```yaml
identity_gate:
  required: true
  filename_binding_allowed: false
  matter_binding_requires_human_confirmation: true
```

Document existence and CASE-B attribution are separate decisions. A matching filename, historical directory, or entity string is insufficient.

### 9.3 CASE-C Adapter

Allowed planning row IDs are exactly `C-P01` through `C-P04`.

```yaml
identity_status: BLOCKED
required_sequence:
  - DOCUMENT_IDENTITY
  - SOURCE_IDENTITY
  - MATTER_IDENTITY
  - ENTITY_IDENTITY
  - QUALIFIED_HUMAN_BINDING_APPROVAL
```

Until every required identity decision is supplied, no evidence registration or lifecycle advancement is executable.

## 10. Review, Approval, and Activation Protocol

### 10.1 Design Review

The Architecture Coordinator reviews this design against `AM-001` through `AM-006`. Acceptance of this design authorizes no manifest instance.

### 10.2 Manifest Preparation

If Level 1 is later authorized, Codex may create exactly one manifest instance at a separately authorized path and return its SHA-256. It must not perform any listed action.

### 10.3 Manifest Review

The Architecture Coordinator reviews the exact instance for complete bindings, allowed actions, exact paths, case-adapter compliance, and human confirmations.

### 10.4 Execution Activation

The Project Owner may activate only specified manifest version and action IDs. Unlisted rows remain non-executable.

### 10.5 Execution and Closeout

Codex may execute only activated action IDs, return per-row results, and stop on any mismatch. Architecture Review and Project Owner closeout remain separate.

## 11. Acceptance Criteria

### AM-001 — SHA Binding

PASS when every governance input, manifest version, review, decision, and execution record is bound to an exact physical SHA-256 at its applicable stage.

### AM-002 — Action Scope Control

PASS when every candidate action is limited by exact object, source, action, authority, purpose, path/object, and access scope.

### AM-003 — Material Access Isolation

PASS when design or preparation status cannot trigger file access and Level 2 requires an exact action-row activation.

### AM-004 — Identity Gate

PASS when document, source, matter, entity, and binding approval remain distinct, and CASE-B/C fail closed on ambiguity.

### AM-005 — Legal Reasoning Isolation

PASS when evidence registration, hashing, source records, human records, and status updates cannot create facts, Legal Facts, request rights, strategies, or outcome conclusions.

### AM-006 — Activation Separation

PASS when Architecture approval and Project Owner execution activation are separate transitions and `APPROVED → EXECUTED` is prohibited.

## 12. Risks and Controls

| Risk | Control |
|---|---|
| Local path does not identify the intended file | Exact path plus document/source/matter/entity identity gates; fail closed |
| Human confirmation is inferred or fabricated | Attributable reviewer fields and actual decision record required |
| Hash is treated as proof of authenticity | Fixed `BYTE_IDENTITY_ONLY` meaning |
| Candidate category is treated as legally required | Individual human requiredness decision; no bulk promotion |
| Scope expands during execution | Immutable manifest version and exact activated action IDs |
| Evidence intake drifts into legal analysis | Fixed action allowlist and prohibited action registry |
| Approval is mistaken for execution | Separate `APPROVED` and `EXECUTION_READY` states |

## 13. Current Governance State

```text
Action Manifest Design Spec:
CREATED — PENDING ARCHITECTURE REVIEW

Action Manifest Design Authorization:
LEVEL 0 ONLY

Action Manifest Instance:
NOT CREATED

Manifest Preparation:
NOT AUTHORIZED

Physical Evidence Acquisition Execution:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next recipient is the **Architecture Coordinator (ChatGPT)** for review of this design asset and its exact SHA-256.
