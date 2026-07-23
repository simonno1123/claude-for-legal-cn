# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **INSTANCE CREATION OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION |
| Authorization | **ACTION MANIFEST INSTANCE CREATION DRAFT ONLY** |
| Designated Draft | `CASE-A-AM-001` |
| Draft Status | **DRAFT / BLOCKED FOR EXECUTION** |
| Physical File Access | **NOT AUTHORIZED / NOT PERFORMED** |
| Physical Evidence Acquisition | **BLOCKED** |
| Implementation | **NOT AUTHORIZED** |
| Date | 2026-07-23 |

This specification contains the designated non-executable `CASE-A-AM-001` Manifest draft. It is one of the two authorized outputs; no separate third Manifest file is created. The draft describes candidate governance actions only and does not bind, inspect, hash, register, interpret, or analyze any real material.

## 1. Purpose and Authority

The task performs the controlled transition:

```text
Generic Manifest Schema
        ↓
Designated Matter-Specific DRAFT
```

It does not perform:

```text
Matter-Specific DRAFT
        ↓
Material Access
        ↓
Execution
```

The current Project Owner instruction authorizes creation of a DRAFT only. Architecture Review, instance approval, execution activation, and physical evidence action remain separate future decisions.

## 2. Fixed Input Binding

| Input | Path | SHA-256 | Role |
|---|---|---|---|
| Instance Creation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF.md` | `4AC712BA996C541B2F402F80A0E1396A05F6E3FAE3D3585235206BE9A88ADC1C` | Defines draft-only scope, four gates, CASE-C isolation, and no-execution boundary |
| Preparation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_SPEC.md` | `B622BAAB9D65ED01360F092F4E8B6FF2BD859D9B8C72DE9CD91E3F20F527526F` | Defines preparation workflow, pending-field rules, instance-creation gates, and case adapters |
| Preparation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_PREPARATION_RESULT.md` | `AC4396496EAA80969994067EE1325E71A667059204191657C4C823B0445E1465` | Confirms `AMP-D-001` through `AMP-D-006` and zero material-access drift |

All three inputs were recomputed and matched before this draft was generated.

## 3. Draft Generation Rules

### 3.1 Permitted Values

- `manifest_id` is the authorized identifier `CASE-A-AM-001`.
- `matter_id: CASE-A` is a governance/symbolic identifier supplied by the current instruction, not a physical-material binding or finding of fact.
- only the four CASE-A categories expressly authorized by the current instruction are included;
- sources, local paths, access scopes, and observed hashes remain pending/not accessed/not computed;
- allowed actions are recorded only as proposals;
- `authorized_action` remains empty;
- `status` remains `DRAFT`;
- human confirmation remains required and pending.

### 3.2 Prohibited Values

The draft cannot contain:

```text
APPROVED
EXECUTABLE
EXECUTION_READY
EXECUTED
VERIFIED
ANALYSIS_READY
```

It cannot state or imply what an evidence item proves, whether it is authentic or admissible, whether liability exists, or what legal position should be taken.

## 4. Four-Gate Model

### Gate 1 — Matter Binding Gate

Required draft fields:

```yaml
matter_id: CASE-A
human_confirmation:
  required: true
  status: PENDING
```

`CASE-A` identifies the authorized adapter and candidate matter label. It does not satisfy final matter binding without an attributable human decision.

Current state:

```text
PENDING — HUMAN MATTER-BINDING CONFIRMATION REQUIRED
```

### Gate 2 — Evidence Category Gate

Closed vocabulary:

```text
contract
payment
communication
corporate_record
identity
property
court_document
```

The designated CASE-A draft uses only:

```text
contract
payment
communication
corporate_record
```

Every item also binds one frozen upstream planning-row ID. Vague labels such as `important`, `key evidence`, or `critical file` are prohibited.

Current state:

```text
PASS — CONTROLLED CATEGORIES AND ROW IDS ONLY
```

### Gate 3 — Source Gate

Controlled values:

```text
court
client
public_registry
opponent
self_provided
PENDING_CONFIRMATION
```

All designated items use:

```yaml
source: PENDING_CONFIRMATION
```

No source is inferred from filename, directory, context, entity name, or model output.

Current state:

```text
DRAFT-PASS — PENDING_CONFIRMATION IS ALLOWED ONLY FOR NON-EXECUTABLE DRAFT
```

### Gate 4 — Action Scope Gate

Allowed action proposals:

```text
HASH_REGISTER
SOURCE_CONFIRM
STATUS_UPDATE
HUMAN_VERIFY
```

Every item preserves:

```yaml
authorized_action: []
execution_authorization: NOT_GRANTED
```

Prohibited actions include `ANALYZE`, `FACT_EXTRACTION`, `LEGAL_EVALUATION`, `LIABILITY_CONFIRMATION`, `INFER`, `CONCLUDE`, and `GENERATE_LEGAL_POSITION`.

Current state:

```text
PASS — PROPOSALS ARE ALLOWLISTED; NO ACTION IS AUTHORIZED
```

## 5. Designated Manifest Instance Draft

The following block is the complete designated governance draft. It is not an execution asset.

```yaml
action_manifest_instance:
  manifest_id: CASE-A-AM-001
  version: v0.1-draft
  status: DRAFT
  executable: false
  execution_authorization: NOT_GRANTED

  authorization_basis:
    instance_creation_handoff_path: .codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_HANDOFF.md
    instance_creation_handoff_sha256: 4AC712BA996C541B2F402F80A0E1396A05F6E3FAE3D3585235206BE9A88ADC1C
    preparation_spec_sha256: B622BAAB9D65ED01360F092F4E8B6FF2BD859D9B8C72DE9CD91E3F20F527526F
    preparation_result_sha256: AC4396496EAA80969994067EE1325E71A667059204191657C4C823B0445E1465
    architecture_review_sha256: PENDING
    project_owner_instance_decision_sha256: PENDING
    execution_activation_decision_sha256: NOT_GRANTED

  matter_binding:
    matter_id: CASE-A
    case: CASE-A
    binding_meaning: SYMBOLIC_GOVERNANCE_IDENTIFIER_ONLY
    binding_status: PENDING_HUMAN_CONFIRMATION
    filename_similarity_binding_allowed: false
    human_confirmation:
      required: true
      status: PENDING
      reviewer_id: null
      confirmed_scope: null
      decided_at: null
      limitations: null

  evidence_items:
    - evidence_item_id: CASE-A-AM-001-E01
      planning_row_id: A-P04
      evidence_category: contract
      target_description: contract_or_agreement_candidate
      source: PENDING_CONFIRMATION
      local_path: PENDING_CONFIRMATION
      access_scope: PENDING_CONFIRMATION
      file_identity: NOT_ACCESSED
      observed_hash: NOT_COMPUTED
      human_confirmation:
        required: true
        status: PENDING
      proposed_action:
        - HASH_REGISTER
        - SOURCE_CONFIRM
        - HUMAN_VERIFY
        - STATUS_UPDATE
      authorized_action: []
      prohibited_action:
        - FILE_READ
        - FILE_COPY
        - FACT_EXTRACTION
        - LEGAL_EVALUATION
        - LIABILITY_CONFIRMATION
      state: DRAFT

    - evidence_item_id: CASE-A-AM-001-E02
      planning_row_id: A-P09
      evidence_category: payment
      target_description: bank_flow_or_payment_candidate
      source: PENDING_CONFIRMATION
      local_path: PENDING_CONFIRMATION
      access_scope: PENDING_CONFIRMATION
      file_identity: NOT_ACCESSED
      observed_hash: NOT_COMPUTED
      human_confirmation:
        required: true
        status: PENDING
      proposed_action:
        - HASH_REGISTER
        - SOURCE_CONFIRM
        - HUMAN_VERIFY
        - STATUS_UPDATE
      authorized_action: []
      prohibited_action:
        - FILE_READ
        - FILE_COPY
        - FACT_EXTRACTION
        - LEGAL_EVALUATION
        - LIABILITY_CONFIRMATION
      state: DRAFT

    - evidence_item_id: CASE-A-AM-001-E03
      planning_row_id: A-P07
      evidence_category: communication
      target_description: communication_record_candidate
      source: PENDING_CONFIRMATION
      local_path: PENDING_CONFIRMATION
      access_scope: PENDING_CONFIRMATION
      file_identity: NOT_ACCESSED
      observed_hash: NOT_COMPUTED
      human_confirmation:
        required: true
        status: PENDING
      proposed_action:
        - HASH_REGISTER
        - SOURCE_CONFIRM
        - HUMAN_VERIFY
        - STATUS_UPDATE
      authorized_action: []
      prohibited_action:
        - FILE_READ
        - FILE_COPY
        - FACT_EXTRACTION
        - LEGAL_EVALUATION
        - LIABILITY_CONFIRMATION
      state: DRAFT

    - evidence_item_id: CASE-A-AM-001-E04
      planning_row_id: A-P01
      evidence_category: corporate_record
      target_description: corporate_registration_candidate
      source: PENDING_CONFIRMATION
      local_path: PENDING_CONFIRMATION
      access_scope: PENDING_CONFIRMATION
      file_identity: NOT_ACCESSED
      observed_hash: NOT_COMPUTED
      human_confirmation:
        required: true
        status: PENDING
      proposed_action:
        - HASH_REGISTER
        - SOURCE_CONFIRM
        - HUMAN_VERIFY
        - STATUS_UPDATE
      authorized_action: []
      prohibited_action:
        - FILE_READ
        - FILE_COPY
        - FACT_EXTRACTION
        - LEGAL_EVALUATION
        - LIABILITY_CONFIRMATION
      state: DRAFT

  instance_gate_summary:
    matter_binding_gate: PENDING
    evidence_category_gate: PASS
    source_gate: DRAFT_PASS_PENDING_CONFIRMATION
    action_scope_gate: PASS_NO_AUTHORIZED_ACTION
    architecture_review: PENDING
    project_owner_instance_approval: PENDING
    execution_gate: BLOCKED
```

## 6. CASE-Specific Controls

### 6.1 CASE-A

The only instance created by this task is the embedded `CASE-A-AM-001` DRAFT above.

It describes candidate governance operations. It does not describe what the material proves and does not assert a contract, payment obligation, communication attribution, corporate identity, agency, debt, delivery, breach, or liability fact.

### 6.2 CASE-B

No CASE-B instance is created.

Future CASE-B drafts must preserve:

```yaml
identity_gate: REQUIRED
identity_status: IDENTITY_PENDING
```

Actual-controller, related-person, and fund-flow labels cannot become identity or liability conclusions.

### 6.3 CASE-C

No CASE-C instance is created.

Future CASE-C work remains:

```yaml
identity_status: IDENTITY_FIRST
instance_creation_state: BLOCKED
```

An `identity_confirmation_action` may be represented only as a non-executable governance request marker. It cannot enter `authorized_action`, bind a historical entity, confirm a relationship, or create a Legal Fact.

## 7. Review and Activation Boundary

The designated draft cannot advance until all separate governance stages complete:

```text
CASE-A-AM-001 DRAFT Created Inside Spec
        ↓
Architecture Coordinator Instance Review
        ↓
Project Owner Instance Approval Decision
        ↓
Separately Authorized Environment-Fact Amendment
        ↓
New Instance Version and SHA
        ↓
New Architecture Review
        ↓
Separate Execution Activation Request
        ↓
Project Owner Activation Decision
```

Review or approval of the current DRAFT cannot activate any proposed action because all real environment fields and human confirmations remain pending.

## 8. Strict Boundary

```text
No Physical File Access
No Directory Search
No File Inspection or Read
No File Copy, Move, Download, Upload, or Conversion
No Case-File Hashing or Hash Registration
No Evidence Registry Update
No OCR or Automatic Extraction
No Database, MCP, Agent, Skill, Workflow, Runtime Schema, Code, or Test Change
No Evidence Interpretation
No Fact or Legal Fact Formation
No Liability or Request-Right Assessment
No Litigation Strategy
No Execution Activation
No Physical Evidence Acquisition
```

Any later request to perform one of these actions requires a separately reviewed and Project Owner-approved Handoff.

## 9. Acceptance Criteria

### AMI-D-001 — Required Asset Binding

PASS when the Spec binds the exact Instance Creation Handoff, Preparation Spec, and Preparation Result hashes.

### AMI-D-002 — Instance Remains a Draft

PASS when `CASE-A-AM-001` is `DRAFT`, non-executable, has no activation decision, and cannot be mistaken for an execution asset.

### AMI-D-003 — Zero Material Operation

PASS when no file is searched, inspected, read, copied, moved, hashed, or registered and no real path is populated.

### AMI-D-004 — Four Gates Preserved

PASS when matter binding, evidence category, source, and action scope are explicit and fail closed.

### AMI-D-005 — CASE-C Identity Isolation

PASS when no CASE-C instance is created and identity-first controls prohibit automatic historical-entity or relationship binding.

### AMI-D-006 — Instance Creation Is Not Acquisition

PASS when creation of a DRAFT cannot authorize evidence collection, registry update, analysis, or any physical action.

## 10. Current Governance State

```text
Instance Creation Spec:
CREATED — PENDING ARCHITECTURE REVIEW

CASE-A-AM-001:
DRAFT / NON-EXECUTABLE / EMBEDDED IN SPEC

Standalone Manifest File:
NOT CREATED

Matter Human Confirmation:
PENDING

Source / Path / Access:
PENDING_CONFIRMATION

Authorized Actions:
NONE

Physical Evidence Acquisition:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next recipient is the **Architecture Coordinator (ChatGPT)** for review of this Spec, embedded DRAFT, and paired Result.
