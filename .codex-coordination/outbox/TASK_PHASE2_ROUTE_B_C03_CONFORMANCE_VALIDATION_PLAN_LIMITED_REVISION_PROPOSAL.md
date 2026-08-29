# TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_PLAN_LIMITED_REVISION_PROPOSAL

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **LIMITED REVISION PROPOSAL — MATERIALIZED / NOT ADOPTED** |
| Route | Phase 2 / Route B |
| Domain | `C03-ENFORCEMENT-ADVERSARIAL-DESIGN` |
| Proposal Scope | `C03-CVP-F-001` only |
| Source Plan | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_PLAN.md` |
| Source Plan SHA-256 | `C105CD45CF0A8CF9B2F9C2A49615E05C609B34764D2CCC81AC74430C991DF060` |
| Internal Plan Review | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_PLAN_REVIEW.md` |
| Internal Review SHA-256 | `B26E8E5B35E02E5E2A7B449ABAC0EC429B6EFF7CE9B2F9DB8FF3A73DF91E8DB9` |
| C03 Domain Profile Spec | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC.md` |
| C03 Profile SHA-256 | `35C3F7E905D2D171301114C6AAF28DF4BCCC2609ADF528A466EC3661D4F44559` |
| Source Plan Modification | **NOT AUTHORIZED / NOT PERFORMED** |
| Revised Plan Candidate | **NOT AUTHORIZED / NOT CREATED** |
| Validation Execution | **NOT AUTHORIZED / NOT PERFORMED** |

This Proposal addresses only the closed-outcome vocabulary contradiction
identified as `C03-CVP-F-001`. It proposes a finite textual correction but
does not revise or supersede the Source Plan, adopt the correction, create a
fixture, execute validation, activate C03, or authorize implementation.

## 1. Fixed Input Verification

| Input | Bound SHA-256 | Recomputed result |
|---|---|---|
| Source Plan | `C105CD45CF0A8CF9B2F9C2A49615E05C609B34764D2CCC81AC74430C991DF060` | **MATCH** |
| Internal Plan Review | `B26E8E5B35E02E5E2A7B449ABAC0EC429B6EFF7CE9B2F9DB8FF3A73DF91E8DB9` | **MATCH** |
| Adopted C03 Domain Profile Spec | `35C3F7E905D2D171301114C6AAF28DF4BCCC2609ADF528A466EC3661D4F44559` | **MATCH** |

```text
Fixed Inputs:
3 / 3 MATCH

Baseline Drift:
0
```

## 2. Authorized Finding

### `C03-CVP-F-001` — Closed Outcome Vocabulary Contradiction

The Source Plan declares the following validation-review determinations:

```text
PASS
LIMITED
FAIL
BLOCKED
NOT EVALUABLE
QUARANTINED
```

The closed-form scenario matrix separately records expected C03 contract
responses. Eleven rows use `REJECTED`, and one row uses `KEEP BLOCKED`.
Those responses are not defined as validation-review determinations in the
Source Plan.

The apparent conflict is a taxonomy collision rather than evidence that the
twelve protective responses are substantively wrong. The adopted C03 Profile
uses `BLOCKED`, `REJECTED`, `QUARANTINED`, and `KEEP BLOCKED` as design-time
operational protection semantics. They describe what the C03 contract must do
with an input or candidate. They do not describe what a later reviewer must
decide about Plan conformance.

## 3. Revision Objective

The proposed revision has one finite objective:

```text
Separate validation-review determinations from expected operational protective
responses so that each axis is closed, independently defined, and never used
as a substitute for the other.
```

The revision must:

1. preserve the six existing validation-review determinations;
2. preserve all 28 scenario meanings;
3. preserve the adopted C03 Profile responses, including `REJECTED` and
   `KEEP BLOCKED`;
4. prevent a protective response from being reported as a review
   determination;
5. prevent a review determination from triggering an operational response;
6. preserve all current Fail-Closed boundaries; and
7. leave every unrelated Plan section unchanged.

## 4. Options Considered

| Option | Description | Determination | Reason |
|---|---|---|---|
| A | Add `REJECTED` and `KEEP BLOCKED` directly to the validation-review determination vocabulary | **NOT RECOMMENDED** | It merges reviewer conclusions with target-contract protection semantics and recreates the category error. |
| B | Replace every `REJECTED` and `KEEP BLOCKED` scenario response with an existing review determination | **NOT RECOMMENDED** | It weakens fidelity to the adopted C03 Profile and removes the distinction among protective responses. |
| C | Keep two separately closed axes and relabel the scenario column as operational | **RECOMMENDED** | It preserves source fidelity, eliminates semantic collision, and maintains governance-stage separation. |

## 5. Proposed Two-Axis Semantic Contract

### 5.1 Axis 1 — Validation-Review Determinations

These values are available only to a later, separately authorized reviewer
assessing conformity between fixed text and the Plan.

| Review determination | Meaning | Authority effect |
|---|---|---|
| `PASS` | The reviewed control conforms exactly to the fixed validation requirement | Advisory only; no activation or execution |
| `LIMITED` | The reviewed control exists with a disclosed non-blocking limitation | No activation; Project Owner decides whether revision is required |
| `FAIL` | The reviewed control is absent, contradicted, or materially weakened | Validation Result cannot be accepted |
| `BLOCKED` | Required identity, authority, baseline, scope, or input for the review is unavailable | Stop the affected and dependent review checks |
| `NOT EVALUABLE` | Fixed text is insufficient for a determination | Remain explicit; never convert to PASS |
| `QUARANTINED` | Conflict, pollution, or integrity defect prevents safe reliance on the reviewed material | No reuse until separately resolved and rebound |

### 5.2 Axis 2 — Expected Operational Protective Responses

These values describe the expected behavior of the fixed C03 design contract.
They are not validation-review determinations and do not prove that an
implementation exists or behaves as designed.

| Protective response | Meaning | Upstream or downstream effect |
|---|---|---|
| `PASS` | The abstract input path satisfies the specific design contract and may produce only the bounded candidate behavior stated in the scenario | No automatic adoption, activation, filing, execution, or implementation |
| `BLOCKED` | A required precondition is unavailable, invalid, stale, or unauthorized | Stop affected and dependent contract processing; no upstream write |
| `REJECTED` | The supplied input or requested output violates a mandatory contract boundary | Reject the affected path; no upstream write and no silent fallback |
| `QUARANTINED` | A conflict, integrity defect, or unsafe reliance condition requires isolation | Isolate the affected material; no reuse until separately resolved |
| `KEEP BLOCKED` | A previously blocked state must remain blocked because its release condition has not been satisfied | Preserve the blocked state; no implicit approval or downstream transition |

### 5.3 Non-Interchangeability Rules

```text
Operational Protective Response != Validation-Review Determination

Expected Operational Response != Observed Implementation Behavior

Validation PASS != Operational Activation

Operational PASS != Plan Review PASS

Operational BLOCKED / REJECTED / QUARANTINED / KEEP BLOCKED
must not be entered into a Review Determination column.

Review FAIL / LIMITED / NOT EVALUABLE
must not be used as an operational state transition.
```

A later validation reviewer must first compare the fixed target text against
the scenario's expected operational protective response and then independently
record one Axis 1 determination. No scenario pre-populates that determination.

## 6. Exact Proposed Change Set

| Change ID | Source Plan location | Exact proposed action | Unchanged boundary |
|---|---|---|---|
| `C03-CVP-CR-001` | Section 5 heading | Rename to `Validation-Review Determinations and Operational Protective Responses` | No outcome or response is activated |
| `C03-CVP-CR-002` | Section 5 current table | Place the existing six values under subsection `5.1 Axis 1 — Validation-Review Determinations`; retain their meanings | Six review determinations remain unchanged |
| `C03-CVP-CR-003` | New Section 5.2 | Add the five-value operational response table from this Proposal | Profile behavior remains design-only and non-executable |
| `C03-CVP-CR-004` | New Section 5.3 | Add the non-interchangeability rules from this Proposal | No automatic cross-axis mapping |
| `C03-CVP-CR-005` | Section 9 matrix header | Replace `Expected contract outcome` with `Expected operational protective response` | All 28 scenario descriptions and response cells remain verbatim |
| `C03-CVP-CR-006` | Section 9 closing note | State that each response is Axis 2 only and never predetermines Axis 1 | Scenarios remain unexecuted design checks |
| `C03-CVP-CR-007` | `C03-CVP-RQ-004` | Replace with a question testing whether both axes are separately closed and non-interchangeable | Review remains read-only and advisory |
| `C03-CVP-CR-008` | `C03-CVP-RQ-008` | Replace `expected contract outcome` with `expected operational protective response` | Scenario count remains 28 |
| `C03-CVP-CR-009` | `C03-CVP-DG-004` | Require six closed review determinations, five closed protective responses, and explicit non-interchangeability | No additional governance authority |
| `C03-CVP-CR-010` | `C03-CVP-DG-008` | Require 28 scenarios with explicit Axis 2 protective responses and no prefilled Axis 1 result | No fixture or validation execution |

No deletion, reordering, or semantic weakening of the 28 scenario rows is
proposed.

## 7. Twelve-Row Finding Resolution Matrix

| Scenario | Existing response | Proposed axis qualification | Textual treatment |
|---|---|---|---|
| `C03-VS-008` | `REJECTED — ISOLATION FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-009` | `REJECTED — ISOLATION FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-014` | `REJECTED — MAPPING CONTRACT FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-015` | `REJECTED — MAPPING CONTRACT FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-018` | `REJECTED — OUTPUT BOUNDARY FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-019` | `REJECTED — OUTPUT BOUNDARY FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-021` | `REJECTED — WRITE-SET VIOLATION` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-023` | `KEEP BLOCKED — HUMAN GATE FAILURE` | Axis 2 persistent operational protective response | Preserve verbatim |
| `C03-VS-025` | `REJECTED — ROUTE A BOUNDARY FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-026` | `REJECTED — FACT GOVERNANCE FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-027` | `REJECTED — JURISDICTION ALIGNMENT FAILURE` | Axis 2 operational protective response | Preserve verbatim |
| `C03-VS-028` | `REJECTED — CASE AUTHORITY HIERARCHY FAILURE` | Axis 2 operational protective response | Preserve verbatim |

```text
Affected Scenario Rows:
12

Scenario Response Text Changed:
0

Scenario Meaning Changed:
0

Axis Qualification Added:
12
```

The remaining sixteen scenario rows also become expressly governed by the
Axis 2 column heading, but their response text does not require correction.

## 8. Proposed Exact Replacement Text

### 8.1 Replacement for `C03-CVP-RQ-004`

```text
Are the validation-review determinations and operational protective responses
separately closed, independently defined, and expressly non-interchangeable?
```

### 8.2 Replacement for `C03-CVP-RQ-008`

```text
Does every scenario have one explicit expected operational protective response
without pre-populating a validation-review determination?
```

### 8.3 Replacement PASS Condition for `C03-CVP-DG-004`

```text
The six validation-review determinations and five operational protective
responses are separately closed, and non-interchangeability is explicit.
```

### 8.4 Replacement PASS Condition for `C03-CVP-DG-008`

```text
Twenty-eight closed-form scenarios have explicit expected operational
protective responses and no prefilled validation-review determination.
```

## 9. Preservation Matrix

| Plan control | Preservation determination |
|---|---|
| Eight fixed baselines | **UNCHANGED** |
| Validation objective | **UNCHANGED** |
| Manual document-conformance mode | **UNCHANGED** |
| Role and authority separation | **UNCHANGED** |
| Eleven validation layers | **UNCHANGED** |
| Twelve evidence classes | **UNCHANGED** |
| Abstract fixture rules | **UNCHANGED** |
| Twenty-eight scenario meanings | **UNCHANGED** |
| LRG-00 through LRG-05 | **UNCHANGED** |
| China-law alignment | **UNCHANGED** |
| Defect taxonomy | **UNCHANGED** |
| Remaining eighteen Plan Review Questions | **UNCHANGED** |
| Remaining thirteen Acceptance Gates | **UNCHANGED** |
| Future output contract | **UNCHANGED** |
| Current and next governance state | **UNCHANGED** |
| Route A / OCR prohibition | **UNCHANGED** |
| ACOS project separation | **UNCHANGED** |
| Implementation and production prohibition | **UNCHANGED** |

## 10. Proposal Review Questions

| ID | Proposal review question |
|---|---|
| `C03-CVP-LRP-RQ-001` | Are the Source Plan, Internal Review, and adopted C03 Profile exact-SHA bound? |
| `C03-CVP-LRP-RQ-002` | Is the Proposal limited to `C03-CVP-F-001`? |
| `C03-CVP-LRP-RQ-003` | Does the Proposal correctly distinguish a reviewer determination from a target-contract response? |
| `C03-CVP-LRP-RQ-004` | Are all six validation-review determinations retained without semantic weakening? |
| `C03-CVP-LRP-RQ-005` | Are the five operational protective responses finite and independently defined? |
| `C03-CVP-LRP-RQ-006` | Is cross-axis substitution expressly prohibited? |
| `C03-CVP-LRP-RQ-007` | Are all eleven `REJECTED` rows preserved and qualified? |
| `C03-CVP-LRP-RQ-008` | Is the one `KEEP BLOCKED` row preserved and qualified? |
| `C03-CVP-LRP-RQ-009` | Are all 28 scenario meanings preserved? |
| `C03-CVP-LRP-RQ-010` | Does the exact change set avoid unrelated Plan modification? |
| `C03-CVP-LRP-RQ-011` | Do the revised RQ-004 and RQ-008 questions test the two-axis contract? |
| `C03-CVP-LRP-RQ-012` | Do the revised DG-004 and DG-008 conditions close the original finding? |
| `C03-CVP-LRP-RQ-013` | Are validation, activation, implementation, and Project Owner authority still separated? |
| `C03-CVP-LRP-RQ-014` | Are Route A, OCR, case-material, and ACOS boundaries unchanged? |
| `C03-CVP-LRP-RQ-015` | Does the Proposal avoid creating or claiming a revised Plan candidate? |

## 11. Proposal Acceptance Gates

| Gate | PASS condition |
|---|---|
| `C03-CVP-LRP-DG-001` — Input Binding | Three exact fixed inputs are recorded and matched |
| `C03-CVP-LRP-DG-002` — Single-Finding Scope | Only `C03-CVP-F-001` is addressed |
| `C03-CVP-LRP-DG-003` — Axis Separation | Review determinations and protective responses are separately defined |
| `C03-CVP-LRP-DG-004` — Review Vocabulary | Six Axis 1 values remain closed and unchanged |
| `C03-CVP-LRP-DG-005` — Protective Vocabulary | Five Axis 2 values are finite and source-fidelity preserving |
| `C03-CVP-LRP-DG-006` — Non-Interchangeability | Cross-axis substitution and automatic transition are prohibited |
| `C03-CVP-LRP-DG-007` — Twelve-Row Fidelity | Eleven `REJECTED` rows and one `KEEP BLOCKED` row are preserved verbatim |
| `C03-CVP-LRP-DG-008` — Scenario Preservation | All 28 scenario meanings remain unchanged |
| `C03-CVP-LRP-DG-009` — Exact Change Control | Ten finite revision actions are identified |
| `C03-CVP-LRP-DG-010` — Governance Separation | Proposal, revision, review, adoption, execution, and activation remain separate |
| `C03-CVP-LRP-DG-011` — Project Boundary | Route A, OCR, case materials, and ACOS remain outside scope |
| `C03-CVP-LRP-DG-012` — Non-Materialization | No Source Plan edit, candidate, fixture, result, code, or runtime is created |

## 12. Defect and Limitation Register

| Category | Count | Status |
|---|---:|---|
| Unresolved authorized finding | 0 | **PROPOSED RESOLUTION DEFINED — NOT ADOPTED** |
| Out-of-scope Plan change | 0 | **CLEAR** |
| Scenario meaning drift | 0 | **CLEAR** |
| Protective-response weakening | 0 | **CLEAR** |
| Cross-axis semantic collision | 0 | **CLEAR IN PROPOSED DESIGN** |
| Baseline or SHA drift | 0 | **CLEAR** |
| China-law alignment drift | 0 | **CLEAR** |
| Route A / OCR boundary drift | 0 | **CLEAR** |
| ACOS project-boundary drift | 0 | **CLEAR** |
| Implementation pollution | 0 | **CLEAR** |

The original finding remains governing against the Source Plan until a later
authorized proposal review, Project Owner proposal decision, revised-candidate
materialization, and revised-candidate review are completed. This Proposal
does not close `C03-CVP-F-001` by itself.

## 13. Materialization Boundary

```text
Source Plan Modification:
NO

Revised Plan Candidate:
NO

Proposal Adoption:
NO

Fixture or Evidence Instance:
NO

Validation Execution or Result:
NO

Case-Material Access / OCR / Legal Analysis:
NO

External Model / Provider / API / Connector / MCP:
NO

Agent / Skill / Schema / Code / Test / Runtime / Deployment:
NO

Route A State Change:
NO

ACOS Source-Project Change:
NO

Git Commit / Push / Branch / Merge:
NO
```

## 14. Current and Next Governance State

```text
Source Validation Plan:
UNCHANGED — INTERNAL PLAN REVIEW FAILED

Authorized Finding:
C03-CVP-F-001 — OPEN

Limited Revision Proposal:
MATERIALIZED — PENDING INTERNAL PROPOSAL REVIEW

Revised Plan Candidate:
NOT AUTHORIZED / NOT CREATED

Project Owner Plan Adoption:
NOT READY / NOT AUTHORIZED

Validation Fixture Creation / Execution:
NOT AUTHORIZED

C03 Activation:
NOT AUTHORIZED

Route A Material Processing / OCR:
NOT AUTHORIZED

Implementation / Production:
NOT AUTHORIZED
```

Required next sequence:

```text
Limited Revision Proposal
        ↓
Internal Proposal Review
        ↓
Project Owner Proposal Decision
        ↓
Revised Plan Candidate Materialization
        ↓
Revised Candidate Internal Plan Review
```

No step transitions automatically.
