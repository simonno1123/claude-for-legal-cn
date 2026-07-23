# TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_CONFIRMATION_PREPARATION_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_CONFIRMATION_PREPARATION_DESIGN |
| Authorization | **CONFIRMATION PREPARATION DESIGN ONLY** |
| Real Confirmation Record | **NOT CREATED / NOT AUTHORIZED** |
| Human Confirmation Collection | **NOT AUTHORIZED** |
| CASE-A-AM-001 | **DRAFT / NON-EXECUTABLE / UNCHANGED** |
| Manifest Activation | **NOT AUTHORIZED** |
| Physical Evidence Acquisition | **BLOCKED** |
| Date | 2026-07-23 |

This specification defines how future human confirmations may be represented, validated, corrected, revoked, audited, and used as one prerequisite for a later activation request. It does not create a real confirmation record, identify a real confirmer, activate a Manifest, or authorize physical action.

## 1. Purpose and Governance Separation

The Confirmation Preparation layer controls the future transition:

```text
CASE-A-AM-001 DRAFT
        ↓
Confirmation Control Model
        ↓
Future Attributable Human Confirmation Records
        ↓
Activation Eligibility Assessment
```

The following objects remain distinct:

```text
Confirmation Preparation Design
        ≠ Human Confirmation Collection
        ≠ Confirmation Decision
        ≠ Manifest Amendment
        ≠ Manifest Activation
        ≠ Physical Evidence Acquisition
```

Core rules:

- Preparation defines structure and validation only.
- AI/Codex cannot be the confirmer or infer a human decision.
- Confirmation completeness does not authorize execution.
- Activation eligibility does not equal activation.
- Activation does not itself perform physical acquisition.

## 2. Fixed Input Binding

| Input | Path | SHA-256 | Role |
|---|---|---|---|
| Confirmation & Activation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_CONFIRMATION_ACTIVATION_HANDOFF.md` | `566EA6E06319C162FE17BBA83FD8717C0A860B25C76C2A0012FB4D2AD5C934BC` | Defines confirmation-preparation-only scope, C1–C6 gates, and activation separation |
| Instance Creation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_SPEC.md` | `59747CAFB05A527D8FE6A0B2E01D4750A085E430BAA965B39F7A818C40572443` | Contains `CASE-A-AM-001` as a non-executable DRAFT |
| Instance Creation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_ACTION_MANIFEST_INSTANCE_CREATION_RESULT.md` | `1CA194A74F53986E11C9EDDC4638A4382BDC5FEF6A5EBC2FF278167505CE4D8F` | Confirms `AMI-D-001` through `AMI-D-006` and zero material operation |

All future confirmation work must recompute these inputs. Any missing or mismatched identity yields `BLOCKED`.

## 3. Scope and Non-Goals

### 3.1 Authorized Design Scope

This specification defines:

- Confirmation Record Schema;
- Authorized Human Actor Model;
- confirmation evidence and authority requirements;
- matter, source, and access confirmation rules;
- activation eligibility criteria;
- revocation, correction, and supersession rules;
- audit trail requirements;
- CASE-A protection and CASE-C identity-first controls;
- validation and stop conditions.

### 3.2 Prohibited Scope

This task does not:

```text
Create a Real Confirmation Record
Name or Authorize a Real Person
Collect a Human Decision
Populate a Real Confirmation Time
Bind a Real Case File or Local Path
Search, Inspect, Read, Copy, Move, or Hash Material
Update an Evidence Registry
Amend CASE-A-AM-001
Activate a Manifest or Action
Perform OCR or Extraction
Modify Database, MCP, Agent, Skill, Workflow, Runtime Schema, or Code
Interpret Evidence or Form Facts / Legal Facts
Assess Liability, Request Rights, Strategy, or Outcome
```

## 4. Confirmation Record Schema

The following is a schema definition only. Every concrete value remains absent or pending.

```yaml
confirmation_record:
  confirmation_id: "required immutable identifier"
  version: "required immutable version"
  status: PENDING

  manifest_binding:
    manifest_id: CASE-A-AM-001
    manifest_version: v0.1-draft
    instance_creation_spec_sha256: 59747CAFB05A527D8FE6A0B2E01D4750A085E430BAA965B39F7A818C40572443
    target_item_id: "CASE-A-AM-001-E01..E04 or MANIFEST"

  confirmation_type: "MATTER_CONFIRMATION | SOURCE_CONFIRMATION | ACCESS_AUTHORIZATION | IDENTITY_CONFIRMATION"

  confirmed_item:
    object_type: "MATTER | EVIDENCE_ITEM | IDENTITY"
    object_id: PENDING
    proposed_value: PENDING
    decision_scope: PENDING

  confirmer:
    actor_id: null
    actor_role: null
    authority_basis_reference: null
    independence_or_conflict_note: null

  confirmation_time: null

  confirmation_evidence:
    evidence_reference: null
    evidence_reference_type: null
    reference_scope: null
    case_material_accessed_by_codex: false
    verification_status: NOT_PERFORMED

  access_decision:
    requested_scope:
      - NO_ACCESS
    granted_scope:
      - NO_ACCESS
    no_copy: true
    no_move: true
    no_upload: true
    no_external_contact: true

  decision:
    value: PENDING
    limitations: null
    reason_summary: null

  audit:
    created_by: null
    created_at: null
    prior_record_id: null
    supersedes_record_id: null
    revocation_target_id: null
    audit_note: null
```

### 4.1 Confirmation Types

| Type | Purpose | Cannot Decide |
|---|---|---|
| `MATTER_CONFIRMATION` | Bind symbolic `CASE-A` to an attributable stable matter identity | Case merits, facts, liability, request rights |
| `SOURCE_CONFIRMATION` | Record a human decision about the declared source and authority basis for one item | Authenticity, admissibility, truth, legal effect |
| `ACCESS_AUTHORIZATION` | Record exact permitted access scope and prohibitions for one item | Whether an operation should be executed or what it proves |
| `IDENTITY_CONFIRMATION` | Record a qualified human identity decision where identity-first controls apply | Automatic entity or historical-matter equivalence |

### 4.2 Status Vocabulary

```text
PENDING
CONFIRMED
REJECTED
REVOKED
SUPERSEDED
CORRECTION_PENDING
```

No other status is permitted. `CONFIRMED` is not an execution state.

## 5. Authorized Human Actor Model

### 5.1 Role Vocabulary

The design recognizes role classes only:

```text
CLIENT_REPRESENTATIVE
ATTORNEY
COURT_AUTHORITY
INTERNAL_REVIEWER
PROJECT_OWNER
```

No person is designated or authorized by this design.

### 5.2 Role Capability Matrix

| Role | Potential Confirmation Scope | Required Additional Basis |
|---|---|---|
| `CLIENT_REPRESENTATIVE` | Client-supplied matter/source declarations within authorized representation | Client authority and scope reference |
| `ATTORNEY` | Matter scope, legal-access constraints, and review of confirmation completeness | Engagement/matter responsibility and conflict review |
| `COURT_AUTHORITY` | Court-origin/source declaration within official scope | Official authority and document/source reference |
| `INTERNAL_REVIEWER` | Process, audit, and internal custody confirmation | Assigned review responsibility and independence note |
| `PROJECT_OWNER` | Governance approval and activation decision | Exact artifact SHA and decision scope |

The role matrix does not grant authority. A future record must include an actual actor ID, role, authority basis, scope, timestamp, limitations, and conflict note.

### 5.3 Prohibited Actor Substitution

The following are invalid:

```text
AI/Codex as confirmer
Role label without actual actor identity
Actor identity without authority basis
Silence or non-response as confirmation
Filename, metadata, or context as human confirmation
Project Owner design approval as source or access confirmation
```

## 6. Confirmation Evidence Requirements

Confirmation evidence is evidence of the human decision and authority—not proof of a case fact.

Every future record must identify:

1. the exact decision object and scope;
2. the actor and role;
3. the authority basis reference;
4. the decision timestamp;
5. the decision value;
6. limitations, uncertainty, and conflicts;
7. the referenced supporting record identity, if any;
8. who created and reviewed the confirmation record.

Rules:

- Codex cannot access a referenced case-material file during confirmation preparation;
- a reference may be recorded only as human-supplied metadata under a later authorization;
- absence of a reference is explicit and cannot be hidden;
- a confirmation record does not determine authenticity, admissibility, proof strength, or a Legal Fact;
- conflicting confirmations remain unresolved and block eligibility.

## 7. Matter, Source, and Access Models

### 7.1 Matter Confirmation

Future requirements:

```yaml
matter_confirmation:
  manifest_id: CASE-A-AM-001
  symbolic_matter_id: CASE-A
  stable_matter_id: "human supplied"
  decision: CONFIRMED
  confirmer: "attributable actor"
  authority_basis: "required"
  scope: "required"
  limitations: "required; may be NONE"
```

No similarity, narrative, or model output may substitute for this record.

### 7.2 Per-Item Source Confirmation

Each item `E01` through `E04` requires an independent record. A decision for one item cannot be inherited by another.

Controlled source values:

```text
court
client
public_registry
opponent
self_provided
PENDING_CONFIRMATION
```

### 7.3 Per-Item Access Authorization

Controlled scopes:

```text
NO_ACCESS
METADATA_ONLY
READ_ONLY
HASH_REGISTER_ONLY
REGISTER_ONLY
```

Normalization rule:

```text
HASH_ONLY → HASH_REGISTER_ONLY
```

Rules:

- default and current scope is `NO_ACCESS`;
- `READ_ONLY`, `HASH_REGISTER_ONLY`, and `REGISTER_ONLY` are candidate scope labels until expressly granted by a separate human decision and later activation;
- scope is per item and cannot be inherited;
- `NO_COPY`, `NO_MOVE`, `NO_UPLOAD`, and `NO_EXTERNAL_CONTACT` remain mandatory;
- confirmation of scope does not execute that scope.

## 8. Activation Eligibility Model

Activation eligibility requires all gates. Eligibility produces only a reviewable candidate state.

### Gate A — Matter Confirmation

Required:

- exact Manifest binding;
- stable matter ID;
- attributable authorized human;
- authority basis, scope, timestamp, and limitations;
- no unresolved conflict.

Failure: `INELIGIBLE — MATTER CONFIRMATION`.

### Gate B — Per-Item Source Confirmation

Required for every action candidate:

- controlled source value;
- source identity and authority basis;
- attributable confirmation record;
- no source conflict.

Failure affects the item and cannot be cured by another item's record.

### Gate C — Per-Item Access Scope Confirmation

Required:

- exact controlled scope;
- exact prohibitions;
- attributable decision;
- exact path only if supplied under a later authorized collection task;
- no scope/path conflict.

Failure: item remains `NO_ACCESS`.

### Gate D — Separate Execution Authorization

Required after Gates A–C:

- amended Manifest candidate with new version and SHA-256;
- Architecture Review bound to that exact SHA;
- separate Project Owner activation decision;
- exact activated action IDs and scope;
- stop conditions and closeout requirements.

Gate D cannot be passed by a Confirmation Record or this design.

### 8.1 Eligibility State

```yaml
activation_eligibility:
  matter_gate: PENDING
  source_gates: PENDING
  access_gates: PENDING
  conflict_gate: PENDING
  eligible_for_activation_request: false
  activation_authorized: false
```

## 9. Revocation, Correction, and Supersession

### 9.1 Revocation

A revocation must:

- reference the exact confirmation ID and version;
- identify the authorized revoking actor and authority basis;
- record time, reason, scope, and limitations;
- set the target to `REVOKED` without deleting history;
- invalidate any dependent activation eligibility;
- trigger re-review of any amended Manifest or activation request.

Revocation does not erase an execution record. If an action was already separately executed, governance must preserve the historical record and escalate remediation.

### 9.2 Correction

Corrections are append-only:

```text
Original Record
        ↓
CORRECTION_PENDING
        ↓
New Corrected Record Version
        ↓
Architecture / Human Review as Required
        ↓
Original Marked SUPERSEDED
```

The original record is not overwritten. A correction cannot broaden scope silently.

### 9.3 Supersession

The new record must bind the prior record, state the exact changes, preserve unchanged limitations, and receive the same or stronger authority review required for the changed fields.

## 10. Audit Trail Requirements

The audit trail is append-only and must capture:

| Event | Required Data |
|---|---|
| Record created | record ID/version, creator, timestamp, input artifact hashes |
| Confirmation requested | object, scope, requested actor role, request status |
| Decision supplied | actor, authority basis, decision, timestamp, limitations, evidence reference metadata |
| Review completed | reviewer, scope, outcome, timestamp, reviewed record SHA |
| Correction proposed | target record, field-level change summary, reason, proposer |
| Revocation issued | target record, authority basis, scope, reason, timestamp |
| Supersession completed | old/new IDs and hashes, effective relationship |
| Eligibility evaluated | Gate A–D status, blockers, evaluator, timestamp |

Audit requirements:

- physical confirmation artifacts must later receive their own SHA-256;
- the audit chain must reference exact versions, not mutable labels;
- no event may be backdated or inferred by Codex;
- missing event data yields `PENDING` or `BLOCKED`;
- deletion or silent overwrite is prohibited.

## 11. CASE-A-AM-001 Protection

This design does not modify the embedded DRAFT. Its state remains:

```yaml
manifest_id: CASE-A-AM-001
status: DRAFT
executable: false
matter_binding: PENDING_HUMAN_CONFIRMATION
source: PENDING_CONFIRMATION
local_path: PENDING_CONFIRMATION
access_scope: PENDING_CONFIRMATION
authorized_action: []
execution_authorization: NOT_GRANTED
```

The current four items remain only candidates:

| Item | Category | Confirmation State | Access State |
|---|---|---|---|
| `CASE-A-AM-001-E01` | `contract` | `PENDING` | `NO_ACCESS` |
| `CASE-A-AM-001-E02` | `payment` | `PENDING` | `NO_ACCESS` |
| `CASE-A-AM-001-E03` | `communication` | `PENDING` | `NO_ACCESS` |
| `CASE-A-AM-001-E04` | `corporate_record` | `PENDING` | `NO_ACCESS` |

No value is promoted to `CONFIRMED`, and no action is activated by this design.

## 12. CASE-C Identity-First Control

The Confirmation Schema must support:

```yaml
identity_confirmation:
  symbolic_case_adapter: CASE-C
  subject: UNKNOWN
  confirmation_required: true
  status: PENDING
  model_population_allowed: false
```

Prohibited:

```text
Model fills a historical subject name
Similar name → same entity
Historical directory → same matter
Identity confirmation → automatic Legal Fact
Identity confirmation → automatic activation
```

CASE-C remains `BLOCKED / IDENTITY FIRST` until a separate authorized human-confirmation chain is complete.

## 13. Validation and Stop Conditions

### 13.1 Schema Validation

- required fields must exist;
- missing values use controlled `PENDING`/`UNKNOWN`/`NOT_PERFORMED` states;
- no concrete person or real material is inserted by this design;
- actor roles use the controlled vocabulary;
- confirmation types and statuses use closed vocabularies;
- case-material access flags remain false;
- `activation_authorized` remains false.

### 13.2 Mandatory Stop Conditions

Stop and remain `BLOCKED` when:

- a bound input hash mismatches;
- an actor identity or authority basis is missing;
- matter or source identity is ambiguous;
- scope or limitations are incomplete;
- records conflict;
- a confirmation is inferred or AI-generated;
- a real path or file operation is requested;
- activation is requested without amended Manifest review and separate Project Owner decision;
- legal reasoning or evidence interpretation is requested.

## 14. Acceptance Criteria

### AMCP-D-001 — Confirmation Handoff Binding

PASS when the Spec binds the exact Confirmation & Activation Handoff and Instance Creation Spec/Result SHA-256 values.

### AMCP-D-002 — Schema Only, No Real Confirmation

PASS when only schemas, role classes, criteria, and workflows are created and no confirmation record is populated.

### AMCP-D-003 — No Fabricated Actor, Time, or Authority

PASS when no person, confirmation time, authority basis, source decision, or access grant is invented.

### AMCP-D-004 — Preparation Is Not Activation

PASS when confirmation preparation and completeness yield only eligibility assessment and cannot activate a Manifest or action.

### AMCP-D-005 — Activation Is Not Physical Acquisition

PASS when activation remains a separate scoped decision and no file operation or acquisition occurs in this task.

### AMCP-D-006 — CASE-A-AM-001 Remains DRAFT

PASS when `CASE-A-AM-001` remains non-executable, all confirmations remain pending, and `authorized_action` stays empty.

## 15. Current Governance State

```text
Confirmation Preparation Spec:
CREATED — PENDING ARCHITECTURE REVIEW

Real Confirmation Records:
0

Human Confirmation Collection:
NOT AUTHORIZED

CASE-A-AM-001:
DRAFT / NON-EXECUTABLE / UNCHANGED

Activation Eligibility:
false / PENDING ALL GATES

Manifest Activation:
NOT AUTHORIZED

Physical Evidence Acquisition:
BLOCKED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN
```

The next recipient is the **Architecture Coordinator (ChatGPT)** for Confirmation Preparation Design Review. Adoption of this design cannot collect confirmations, amend the Manifest, activate actions, or authorize acquisition.
