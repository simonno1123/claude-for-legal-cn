# Project Owner Decision — Route B C03 WP-008 Comparison-Rule Acceptance

## 1. Decision Control

| Field | Value |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Lifecycle item | `RDM-DSP-013 — DETACHED_RULE_REVIEW_REQUIRED` |
| Decision authority | `Project Owner — SOLE POSITIVE AUTHORITY` |
| Human identity requirement | Stable Project Owner role is sufficient; no real-person identity is required or recorded |
| Decision | `FIVE COMPARISON RULES ACCEPTED — DESIGN-TEXT SCOPE ONLY` |
| Record state at materialization | `MATERIALIZED — DECISION-RECORD REVIEW NOT AUTHORIZED / NOT PERFORMED` |
| Activation semantics | `CAPABILITY_ONLY` |
| Input admission | `NOT AUTHORIZED / NOT ESTABLISHED` |
| Python / subject / fixture execution | `NOT AUTHORIZED / NOT RUN` |
| Automatic downstream transition | `BLOCKED` |

This record durably materializes the conversation-level Project Owner decision
accepting the five independently reviewed comparison rules identified below.
It neither edits the fixed input binding nor changes the embedded
`PROPOSED_NOT_ACCEPTED` text in that already-hashed candidate. The detached
record provides later decision lineage without rewriting historical bytes.

This decision record must receive a separate fixed-SHA read-only review before
`RDM-DSP-013` can be marked fully closed for final input-admission purposes.

## 2. Bound Assets and Review Lineage

| ID | Asset | SHA-256 | Binding effect |
| --- | --- | --- | --- |
| `CR-DEC-SRC-001` | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | Exact candidate containing the five rule definitions, stimuli and fixture abstractions |
| `CR-DEC-SRC-002` | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_SCENARIO_INPUT_BINDING_COMPARISON_RULES_INTERNAL_REVIEW.md` | `90D7FD7E330FDD776CB82FF26EE6E1F35944D52F15E0BE9BF1248AA14C5D5180` | Independent internal review: `5 / 5 PASS`, `12 / 12` questions, `12 / 12` gates, zero review defects |
| `CR-DEC-SRC-003` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_SCENARIO_INPUT_BINDING_LIMITATION_DISPOSITION_PROPOSAL.md` | `ACABF4368E1D5DC968F9EAD6569A6578108AF9B9E0926A1C94326EE498D040CE` | Accepted disposition design defining the `RDM-DSP-013` route and rule-review boundary |

The review is a design-text determination only. It did not execute any source,
fixture, adapter or scenario and did not independently establish runtime output.

## 3. Accepted Comparison Rules

| Rule ID | Exact raw requirement | Accepted fixture abstraction | Acceptance scope | Preserved limitation |
| --- | --- | --- | --- | --- |
| `CR-001-RAW-GATE-TO-ABSTRACT-ORACLE` | State `BLOCKED`; reason `BLOCKED — TIER B AUTHORITY REQUIRED` | State `BLOCKED`; reason class `MISSING_MATTER_BOUND_AUTHORITY` | Accept the mapping for the V-001 missing-packet gate only | No assertion that real authority is absent; no authority validation or execution authority |
| `CR-002-CONSTRUCTOR-FAILURE` | Exception `ValueError`; message `matter_authorization_reference must be a non-empty explicit value` | State `BLOCKED`; reason class `AUTHORITY_OR_IDENTITY_FAILURE` | Accept the constructor-level mapping only | The final matter/execution/decision-reference comparison remains unreachable; full V-002 remains HOLD |
| `CR-005-PROHIBITED-KEY-EXCEPTION` | Exception `IsolationViolation`; message `QUARANTINED — CONTENT FIELD PROHIBITED: credential_reference_present` | State `BLOCKED_QUARANTINED`; reason class `PROHIBITED_CONTENT_CLASSIFICATION` | Accept the exact top-level prohibited-key mapping only | No nested-object, value-content or other disclosure-channel coverage |
| `CR-007-RETRY-ELIGIBILITY` | State `RETRY_ELIGIBILITY_PENDING`; reason `RETRY ELIGIBLE — EXECUTION NOT AUTHORIZED`; next attempt `1` | State `RETRY_ELIGIBILITY_PENDING`; reason class `ELIGIBILITY_ONLY_EXECUTION_UNAUTHORIZED` | Accept the eligibility-only mapping | No retry, delay, scheduler, deadline measurement or side effect is authorized or established |
| `CR-014-PROHIBITED-NAMESPACE-EXCEPTION` | Exception `IsolationViolation`; message prefix `REJECTED — PROHIBITED WRITE:` | State `BLOCKED`; reason class `PROHIBITED_WRITE_TARGET` | Accept the mapping for the exact non-empty `acos_source_project` and `route_a` namespace metadata inputs | No filesystem, Git, remote ACL, stage, commit, branch, push or external-write denial is executed or established |

For all five rules, raw observations and fixture abstractions remain separate,
and `post_hoc_change: PROHIBITED` remains binding. Acceptance does not permit a
Harness to rewrite raw values, reason text or exception identity after a call.

## 4. Decision Effect

The Project Owner decision establishes only the following:

1. Each of the five named comparison rules is accepted independently at the
   design-text level for its exact fixed input, raw requirement, fixture
   abstraction and stated limitation.
2. The independent internal review bound at SHA-256
   `90D7FD7E330FDD776CB82FF26EE6E1F35944D52F15E0BE9BF1248AA14C5D5180`
   is adopted as the review lineage supporting this decision.
3. No aggregate runtime PASS is created. Any future execution must preserve the
   raw result and compare it under the accepted rule without post-hoc repair.
4. Any change to a rule, adapter, stimulus, observation surface, subject,
   fixture or expected abstraction requires a revised input-binding candidate,
   a new SHA, a new review and a new Project Owner decision.
5. The fixed candidate retains its original materialization-state text. This
   detached decision does not alter or retroactively restate the candidate.

## 5. Explicit Exclusions and Preserved Holds

| Item | State after this decision |
| --- | --- |
| Review and fixed-SHA acceptance of this decision record | `NOT AUTHORIZED / NOT PERFORMED` |
| Full closure of `RDM-DSP-013` | `PENDING DECISION-RECORD REVIEW` |
| V-003 raw `BLOCKED` to `BLOCKED_STALE` mapping | `NOT DESIGNED / NOT REVIEWED / NOT ACCEPTED` |
| V-002 final authority comparison | `UNREACHABLE / CONTINUED HOLD` |
| `RDM-DSP-002` through `RDM-DSP-012` | `OPEN / UNAFFECTED` |
| Scenario Input Binding final admission | `NOT AUTHORIZED / NOT ESTABLISHED` |
| Input-binding, fixture, subject or source modification | `NOT AUTHORIZED` |
| Harness materialization or source acceptance | `NOT AUTHORIZED` |
| Runtime Dependency Manifest generation or acceptance | `NOT AUTHORIZED` |
| Evidence directory, evidence files or aggregate result | `NOT AUTHORIZED / NOT CREATED` |
| Python import, subject call, fixture execution or validation | `NOT AUTHORIZED / NOT RUN` |
| Route A, OCR, case-material or legal processing | `NOT AUTHORIZED` |
| Provider, model, network, API, Connector or MCP invocation | `NOT AUTHORIZED` |
| Independent ACOS source-project access or modification | `NOT AUTHORIZED` |
| Git stage, commit, branch, merge, push or remote action | `NOT AUTHORIZED` |
| C03 readiness | `NOT READY` |
| Automatic downstream transition | `BLOCKED` |

## 6. Decision-Record Review Questions

| ID | Question |
| --- | --- |
| `RDM-CRD-RQ-001` | Does the record bind the exact Scenario Input Binding SHA? |
| `RDM-CRD-RQ-002` | Does the record bind the exact independent internal review SHA and its correct result counts? |
| `RDM-CRD-RQ-003` | Are the five accepted rule IDs complete and free of additions? |
| `RDM-CRD-RQ-004` | Are each rule's raw requirement and fixture abstraction recorded separately? |
| `RDM-CRD-RQ-005` | Is CR-001 limited to the missing-packet gate without a real-authority inference? |
| `RDM-CRD-RQ-006` | Is CR-002 limited to the constructor failure while the unreachable comparison remains HOLD? |
| `RDM-CRD-RQ-007` | Is CR-005 limited to the exact top-level key? |
| `RDM-CRD-RQ-008` | Is CR-007 limited to eligibility rather than retry or time enforcement? |
| `RDM-CRD-RQ-009` | Is CR-014 limited to namespace metadata rather than actual write denial? |
| `RDM-CRD-RQ-010` | Is the missing V-003 rule excluded without inference or transfer? |
| `RDM-CRD-RQ-011` | Are all other disposition blockers and admission requirements preserved? |
| `RDM-CRD-RQ-012` | Are execution, evidence, Git and independent ACOS actions excluded? |

## 7. Decision-Record Acceptance Gates

| ID | Gate |
| --- | --- |
| `RDM-CRD-G-001` | Fixed input-binding identity and SHA exact |
| `RDM-CRD-G-002` | Fixed review-record identity, SHA and counts exact |
| `RDM-CRD-G-003` | Five and only five rule candidates accepted |
| `RDM-CRD-G-004` | Five independent acceptance scopes and limitations present |
| `RDM-CRD-G-005` | Raw requirements and fixture abstractions remain separate |
| `RDM-CRD-G-006` | Post-hoc changes remain prohibited |
| `RDM-CRD-G-007` | V-002 unreachable comparison remains HOLD |
| `RDM-CRD-G-008` | V-003 comparison rule remains absent and unaccepted |
| `RDM-CRD-G-009` | Other disposition items remain open and unaffected |
| `RDM-CRD-G-010` | Input admission and execution remain unauthorized |
| `RDM-CRD-G-011` | Changed bytes require new binding, review and decision |
| `RDM-CRD-G-012` | Git and independent ACOS boundaries preserved; automatic transition blocked |

## 8. Resulting State

```text
Five Existing Comparison Rules:
ACCEPTED BY PROJECT OWNER — DESIGN-TEXT SCOPE ONLY

Detached Internal Rule Review:
PASS — GRADE A / 5 OF 5 RULE DETERMINATIONS PASS

Decision Record:
MATERIALIZED — FIXED-SHA REVIEW NOT AUTHORIZED / NOT PERFORMED

RDM-DSP-013:
PENDING DECISION-RECORD REVIEW

V-003 Comparison Rule:
NOT DESIGNED / NOT REVIEWED / NOT ACCEPTED

RDM-DSP-002 THROUGH RDM-DSP-012:
OPEN / UNAFFECTED

Scenario Input Binding Admission / Harness / Manifest / Evidence / Execution:
NOT AUTHORIZED / NOT ESTABLISHED / NOT CREATED / NOT RUN

C03 Readiness / Automatic Downstream Transition:
NOT READY / BLOCKED
```
