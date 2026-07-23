# TASK_PHASE2_ROUTE_A_EXTERNAL_HUMAN_INPUT_RECOVERY_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | `v1.0` |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | `TASK_PHASE2_ROUTE_A_EXTERNAL_HUMAN_INPUT_RECOVERY_DESIGN` |
| Authorization | **EXTERNAL HUMAN INPUT RECOVERY DESIGN ONLY** |
| Handoff | `TASK_PHASE2_ROUTE_A_EXTERNAL_HUMAN_INPUT_RECOVERY_HANDOFF.md` |
| Handoff SHA-256 | `099C0025C3744FD360A4935F6623DE46C4A6BF66FC2CC73778C1C47AB9DB4CBE` |
| Date | `2026-07-23` |

This specification defines a safe recovery interface for future external human
input. It does not identify or contact a human, send a request, receive an
input, create a Confirmation Record or Bundle, amend a Manifest, authorize an
action, or access physical evidence.

## 1. Purpose

The Confirmation Collection phase completed with no valid confirmation input:

```text
MATTER_CONFIRMATION:
0 of 1

SOURCE_CONFIRMATION:
0 of 4

ACCESS_AUTHORIZATION:
0 of 4

VALID CONFIRMATION RECORDS:
0

CONFIRMATION BUNDLE:
NOT CREATED
```

The recovery design governs the transition from a known input gap to a future,
separately authorized opportunity for an attributable human to supply input.

```text
Known Human-Input Gap

        ↓

Recovery Request Candidate

        ↓

Separately Authorized Submission Channel

        ↓

External Human Input Candidate

        ↓

Identity / Authority / Scope / Integrity Verification

        ↓

Recovery Completion Candidate

        ↓

Separate Confirmation Eligibility Review
```

Recovery completion does not create a substantive confirmation and does not
activate `CASE-A-AM-001`.

## 2. Governing Principles

### 2.1 Recovery Is Not Fabrication

The system may describe what information is missing and how a future input
would be evaluated. It may not invent:

- an actor or identity;
- a relationship or authority basis;
- a scope or limitation;
- a submission time or channel event;
- an answer, approval, rejection, or revocation;
- a source, local path, material fact, or confirmation record.

### 2.2 Request Design Is Not Contact

An interface, schema, or request template is a design asset.

```text
Request Interface Defined
≠
Request Authorized
≠
Request Sent
≠
Person Contacted
```

No contact discovery, public search, email, message, calendar event, provider
call, or external outreach is part of this design.

### 2.3 Input Is Not Confirmation

An incoming statement is a candidate input until its provenance, identity,
authority, scope, integrity, and audit record pass review.

```text
Input Received
≠
Input Verified
≠
Confirmation Accepted
≠
Bundle Created
≠
Manifest Activated
```

### 2.4 Confirmation Is Not Execution

Even a future accepted confirmation cannot itself authorize file access,
hashing, registration, copying, OCR, acquisition, legal analysis, or any other
Manifest action.

## 3. Fixed Baseline

| Asset | SHA-256 | Verification requirement |
|---|---|---|
| External Human Input Recovery Handoff | `099C0025C3744FD360A4935F6623DE46C4A6BF66FC2CC73778C1C47AB9DB4CBE` | Exact match |
| Confirmation Collection Handoff | `0B8AC04165EAC43F0E31F015FB31F5C669B2BC236DB740DFACFCE8F4F1CD2B14` | Exact match |
| Confirmation Collection Spec | `35E01BFAC61DCBDE2649A28EC441154702C37E76E9A585E6DFD6FA10464621BB` | Exact match |
| Confirmation Collection Result | `7BD22F6AE2C40A8430891360758AFB0677FF17FF03949EED31E0952E4BC24A96` | Exact match |
| Confirmation Preparation Spec | `AB9195CC58EDA92AE62126C746269EE83F6A0E51350192817DBD82AE5B84DFBE` | Exact match |
| Instance Creation Spec | `59747CAFB05A527D8FE6A0B2E01D4750A085E430BAA965B39F7A818C40572443` | Exact match |

A mismatch produces `BLOCKED — BASELINE IDENTITY FAILURE`. Silent rebinding
is prohibited.

## 4. Missing-Input Register

Each requirement is an isolated target. A response for one target cannot be
generalized to another.

| Recovery target | Input type | Required | Received | Current state |
|---|---|---:|---:|---|
| `CASE-A-AM-001` | `MATTER_CONFIRMATION` | 1 | 0 | `MISSING` |
| `CASE-A-AM-001-E01` | `SOURCE_CONFIRMATION` | 1 | 0 | `MISSING` |
| `CASE-A-AM-001-E02` | `SOURCE_CONFIRMATION` | 1 | 0 | `MISSING` |
| `CASE-A-AM-001-E03` | `SOURCE_CONFIRMATION` | 1 | 0 | `MISSING` |
| `CASE-A-AM-001-E04` | `SOURCE_CONFIRMATION` | 1 | 0 | `MISSING` |
| `CASE-A-AM-001-E01` | `ACCESS_AUTHORIZATION` | 1 | 0 | `MISSING / NO_ACCESS` |
| `CASE-A-AM-001-E02` | `ACCESS_AUTHORIZATION` | 1 | 0 | `MISSING / NO_ACCESS` |
| `CASE-A-AM-001-E03` | `ACCESS_AUTHORIZATION` | 1 | 0 | `MISSING / NO_ACCESS` |
| `CASE-A-AM-001-E04` | `ACCESS_AUTHORIZATION` | 1 | 0 | `MISSING / NO_ACCESS` |

```text
TOTAL REQUIRED INPUT TARGETS:
9

TOTAL RECEIVED:
0

CURRENT RECOVERY OUTCOME:
NOT STARTED — DESIGN ONLY
```

## 5. External Human Input Request Model

The model separates four objects.

### 5.1 Recovery Need

A record that identifies a missing input and its target. It contains no real
human identity and grants no permission.

### 5.2 Request Candidate

A reviewable, unsent request description containing:

- one recovery need;
- an abstract eligible role class;
- requested information;
- expressly excluded scope;
- proposed channel class;
- required authority evidence;
- required audit fields.

Its state is always `DRAFT / NOT_SENT` until a separate authorization exists.

### 5.3 Submission Envelope

A future wrapper for externally supplied input. It records provenance and
preserves the original external statement without treating it as verified.

### 5.4 Recovery Assessment

A future verification outcome that records gate results. Its maximum output is
`ELIGIBLE_FOR_CONFIRMATION_REVIEW`.

It cannot output `CONFIRMED`, `ACTIVE`, `EXECUTABLE`, or
`ACQUISITION_AUTHORIZED`.

## 6. Recovery Need Schema

```yaml
external_human_input_recovery_need:
  recovery_id:
  manifest_id: CASE-A-AM-001
  target_id:
  missing_input_type:
    enum:
      - MATTER_CONFIRMATION
      - SOURCE_CONFIRMATION
      - ACCESS_AUTHORIZATION
  current_state: MISSING
  eligible_role_classes:
    - CLIENT_REPRESENTATIVE
    - ATTORNEY
    - INTERNAL_REVIEWER
    - PROJECT_OWNER
    - COURT_AUTHORITY
  actual_actor:
    state: NOT_IDENTIFIED
    value: null
  authority_basis:
    state: NOT_PROVIDED
    value: null
  requested_scope:
  prohibited_scope:
  proposed_channel:
    state: NOT_SELECTED
    value: null
  request_state: NOT_DRAFTED
  submission_state: NOT_RECEIVED
  verification_state: NOT_STARTED
  recovery_state: GAP_IDENTIFIED
```

Role classes are eligibility categories only.

```text
ROLE CLASS
≠
REAL ACTOR
≠
VERIFIED AUTHORITY
```

## 7. Request Candidate Schema

```yaml
external_human_input_request_candidate:
  request_candidate_id:
  recovery_id:
  manifest_id: CASE-A-AM-001
  target_id:
  requested_input_type:
  question_text:
  requested_scope:
  prohibited_scope:
  eligible_role_class:
  actual_recipient: null
  authority_evidence_required: true
  proposed_channel_class:
  channel_authorization:
    state: NOT_AUTHORIZED
    reference: null
  transmission:
    state: NOT_SENT
    timestamp: null
  status: DRAFT
```

Permitted `proposed_channel_class` values:

```text
AUTHORIZED_USER_INPUT
APPROVED_ATTACHMENT
APPROVED_CANONICAL_COORDINATION_ARTIFACT
SEPARATELY_AUTHORIZED_COMMUNICATION_WORKFLOW
```

This design does not select or use any channel. A channel class does not
authorize communication.

## 8. Submission Envelope Schema

This schema applies only if a later, separately authorized process receives
real external input.

```yaml
external_human_input_submission:
  submission_id:
  request_candidate_id:
  recovery_id:
  received_via:
  received_at:
  original_input_reference:
  original_input_preserved:
  supplied_actor_identity:
    name:
    role:
    organization:
    identity_reference:
    verification_source:
  supplied_authority:
    authority_basis_reference:
    permitted_confirmation_type:
    permitted_target:
    limitations:
    validity_period:
  supplied_scope:
    included:
    excluded:
  supplied_statement:
  integrity_reference:
  status: UNVERIFIED_INPUT
```

Every supplied field must originate from attributable external input. The
system must not complete a missing field from context or inference.

## 9. Human Identity Input Gate

Purpose: determine who supplied the input.

Required:

1. an attributable identity reference;
2. a declared role and organization, if applicable;
3. a reviewable verification source;
4. a link between the actor and the submission event.

Outcomes:

```text
PASS
PENDING
REJECTED
CONFLICT
```

The following cannot pass the gate:

- a model-generated identity;
- a name inferred from a case file or filename;
- an unverified historical association;
- a role label without an attributable actor;
- a governance approver presumed to be a matter confirmer.

## 10. Authority Scope Gate

Identity and authority are separate.

The gate must verify:

1. the authority basis;
2. the confirmation type covered;
3. the exact target covered;
4. limitations and exclusions;
5. validity period, revocation, or supersession;
6. whether a second reviewer is required.

Authority is target-specific:

```text
Matter Association Authority
≠
Source Confirmation Authority
≠
Evidence Access Authority
≠
Execution Authority
```

A lawyer, representative, employee, owner, or Project Owner role does not
automatically pass this gate.

## 11. Submission Boundary

### 11.1 Permitted Future Intake

A separately authorized process may receive:

- explicit user-provided text;
- an explicitly attached, attributable record;
- an approved canonical coordination artifact;
- a response produced through a separately authorized communication workflow.

### 11.2 Prohibited Intake

The system must not:

- search directories, case materials, public sources, contacts, email, chat,
  or calendars to locate a confirmer;
- infer contact details;
- send a request without explicit communication authorization;
- treat silence as consent;
- treat a Project Owner governance decision as matter, source, or access
  confirmation;
- extract confirmation from unrelated historical text;
- convert a partial response into broader scope.

### 11.3 Non-Response

Non-response preserves:

```text
INPUT:
MISSING

RECOVERY:
PENDING / BLOCKED

CONFIRMATION:
NOT RECEIVED

ACTIVATION:
INELIGIBLE
```

## 12. Input Integrity Gate

This gate asks whether the submitted input is complete, attributable,
preserved, and unchanged within its authorized intake process. It does not
decide whether the underlying case fact or evidence is true.

Required checks:

1. original input is preserved or referenced;
2. received time and authorized channel are recorded;
3. target and scope are unambiguous;
4. identity and authority references are present;
5. amendments and corrections are append-only;
6. conflicts are exposed rather than reconciled by inference.

```text
INPUT INTEGRITY VERIFIED
≠
EVIDENCE AUTHENTICITY
≠
LEGAL FACT
```

Permitted outcomes:

```text
PASS
INCOMPLETE
CONFLICT
SUPERSEDED
REVOKED
REJECTED
```

## 13. Audit Record

```yaml
human_input_recovery_audit_record:
  audit_id:
  recovery_id:
  request_candidate_id:
  submission_id:
  event_type:
    enum:
      - GAP_RECORDED
      - REQUEST_CANDIDATE_CREATED
      - REQUEST_REVIEWED
      - REQUEST_AUTHORIZED
      - REQUEST_SENT
      - INPUT_RECEIVED
      - IDENTITY_CHECKED
      - AUTHORITY_CHECKED
      - SCOPE_CHECKED
      - INTEGRITY_CHECKED
      - CORRECTION_RECEIVED
      - INPUT_REVOKED
      - RECOVERY_ASSESSED
  actor_reference:
  actor_role:
  authority_reference:
  event_time:
  authorized_channel:
  original_input_reference:
  target_id:
  scope:
  limitations:
  prior_state:
  new_state:
  reviewer_reference:
  review_result:
  immutable_history_required: true
```

Events that did not occur must not be populated. This design creates no audit
event instance.

## 14. Recovery State Model

### 14.1 Primary States

```text
GAP_IDENTIFIED

        ↓

REQUEST_CANDIDATE_DRAFTED

        ↓

REQUEST_REVIEWED

        ↓

REQUEST_AUTHORIZED

        ↓

AWAITING_EXTERNAL_INPUT

        ↓

INPUT_RECEIVED_UNVERIFIED

        ↓

IDENTITY_VERIFIED

        ↓

AUTHORITY_VERIFIED

        ↓

SCOPE_VERIFIED

        ↓

INTEGRITY_VERIFIED

        ↓

RECOVERY_COMPLETION_CANDIDATE

        ↓

ELIGIBLE_FOR_CONFIRMATION_REVIEW
```

### 14.2 Blocking and Terminal Branches

```text
NO_AUTHORIZED_CHANNEL
NO_RESPONSE
IDENTITY_PENDING
IDENTITY_REJECTED
AUTHORITY_PENDING
AUTHORITY_REJECTED
SCOPE_INCOMPLETE
INPUT_INCOMPLETE
INPUT_CONFLICT
INPUT_REVOKED
INPUT_SUPERSEDED
RECOVERY_BLOCKED
```

No state automatically transitions to `CONFIRMED`, `ACTIVE`, `EXECUTABLE`, or
`ANALYSIS_READY`.

### 14.3 Current State

This design does not execute the state machine.

```text
Actual Recovery State:
GAP_IDENTIFIED

Request Candidate Instances:
0

Requests Sent:
0

External Inputs Received:
0

Recovery Completed:
NO
```

## 15. Recovery Completion Gate

Recovery is complete for one target only when:

1. a real external submission exists;
2. identity passes;
3. authority passes for the exact input type and target;
4. scope is explicit;
5. integrity passes;
6. the audit chain is complete;
7. there is no unresolved conflict, revocation, or supersession.

The gate output is:

```text
ELIGIBLE_FOR_CONFIRMATION_REVIEW
```

It is never:

```text
CONFIRMED
CONFIRMATION_BUNDLE_CREATED
ACTIVATION_APPROVED
EXECUTABLE
PHYSICAL_ACQUISITION_AUTHORIZED
```

Partial recovery remains target-specific. Passing one of nine targets cannot
complete any other target.

## 16. Correction, Revocation, and Conflict

### Correction

A correction must reference the original submission and create a new version.
Silent overwrite is prohibited.

### Revocation

A revocation must preserve the original record, identify the revoking actor and
authority basis, record scope and time, and invalidate dependent eligibility.

### Conflict

Conflicting inputs remain concurrently visible. The system must set
`INPUT_CONFLICT` and require human review; it may not choose a preferred input.

### Expiry

Time-limited authority or input becomes `AUTHORITY_PENDING` or
`RECOVERY_BLOCKED` upon expiry. It is not silently extended.

## 17. CASE-A-AM-001 Preservation

The existing embedded Manifest draft is not modified.

```yaml
manifest_id: CASE-A-AM-001
status: DRAFT
executable: false
matter_binding: PENDING_HUMAN_CONFIRMATION
source_confirmations:
  CASE-A-AM-001-E01: PENDING
  CASE-A-AM-001-E02: PENDING
  CASE-A-AM-001-E03: PENDING
  CASE-A-AM-001-E04: PENDING
local_paths:
  CASE-A-AM-001-E01: PENDING_CONFIRMATION
  CASE-A-AM-001-E02: PENDING_CONFIRMATION
  CASE-A-AM-001-E03: PENDING_CONFIRMATION
  CASE-A-AM-001-E04: PENDING_CONFIRMATION
access:
  CASE-A-AM-001-E01: NO_ACCESS
  CASE-A-AM-001-E02: NO_ACCESS
  CASE-A-AM-001-E03: NO_ACCESS
  CASE-A-AM-001-E04: NO_ACCESS
authorized_actions: []
execution_authorization: NOT_GRANTED
```

No field is promoted, filled, or reinterpreted by this design.

## 18. CASE-C Identity-First Isolation

CASE-C remains:

```yaml
case: CASE-C
identity_status: IDENTITY_FIRST
subject: UNKNOWN
binding_status: BLOCKED
```

A future recovery submission may supply an identity-confirmation candidate.
It cannot itself bind a historical entity or create a case relationship.

```text
External Input Recovery
≠
Historical Entity Match
```

## 19. Interfaces to Later Governance Stages

### 19.1 Recovery Request Authorization Interface

Consumes a `Request Candidate`. Produces only `AUTHORIZED_TO_SEND` or
`NOT_AUTHORIZED`. It does not send the request.

### 19.2 External Submission Intake Interface

Consumes externally supplied input through an authorized channel. Produces an
`UNVERIFIED_INPUT` envelope.

### 19.3 Recovery Verification Interface

Runs identity, authority, scope, integrity, and audit checks. Produces a
target-specific Recovery Assessment.

### 19.4 Confirmation Eligibility Interface

Consumes a passed Recovery Assessment. Produces only an eligibility candidate
for a separately governed confirmation review.

### 19.5 Activation Interface

Not part of this design and not authorized.

## 20. Explicit Boundary

```text
Real Human Identification:
NOT PERFORMED

Contact Search or Inference:
NOT PERFORMED

External Outreach:
NOT PERFORMED

Request Transmission:
NOT PERFORMED

External Human Input Received:
0

Confirmation Record:
NOT CREATED

Confirmation Bundle:
NOT CREATED

CASE-A-AM-001 Amendment:
NOT PERFORMED

Manifest Activation:
NOT AUTHORIZED

Directory / Case-Material Search:
NOT PERFORMED

File Read / Copy / Move / Hash:
NOT PERFORMED

Evidence Registry Update:
NOT PERFORMED

Physical Evidence Acquisition:
BLOCKED

OCR / Extraction:
NOT PERFORMED

Database / MCP / Agent / Skill / Workflow / Code:
NOT MODIFIED

Evidence Evaluation / Fact Extraction / Legal Reasoning:
NOT PERFORMED
```

## 21. Acceptance Criteria

### EHIR-D-001 — Handoff Binding Integrity

PASS when the exact Handoff and fixed upstream hashes are bound and verified.

### EHIR-D-002 — Recovery Is Not Fabrication

PASS when no actor, authority, time, scope, source, input, or confirmation is
invented.

### EHIR-D-003 — No External Contact Automation

PASS when the design defines interfaces and channels without searching,
selecting, contacting, messaging, or notifying an external party.

### EHIR-D-004 — Draft Preservation

PASS when `CASE-A-AM-001` remains DRAFT, non-executable, unchanged, and has no
authorized action.

### EHIR-D-005 — Activation Isolation

PASS when the maximum recovery output is
`ELIGIBLE_FOR_CONFIRMATION_REVIEW` and no activation state or decision is
created.

### EHIR-D-006 — Physical Access Isolation

PASS when no case-material operation, Registry update, OCR, implementation, or
legal reasoning occurs.

## 22. Required Next Governance State

After this Spec and its Result are produced:

```text
Codex Design Result

        ↓

Architecture Coordinator Design Review

        ↓

Project Owner Decision
```

Even an accepted design does not authorize a recovery request or human-input
collection. Those actions require a separate Handoff, review, decision, and
explicit channel authorization.

```text
External Human Input Recovery Design:
DESIGN OUTPUT — PENDING REVIEW

Actual Human Input Recovery:
NOT AUTHORIZED / NOT STARTED

Confirmation Collection:
CLOSED WITH NO CONFIRMATIONS

CASE-A-AM-001:
DRAFT / NON-EXECUTABLE / UNCHANGED

Confirmation Bundle:
NOT CREATED

Manifest Activation:
NOT AUTHORIZED

Physical Evidence Acquisition:
BLOCKED
```

Next recipient: **Architecture Coordinator (ChatGPT)**.
