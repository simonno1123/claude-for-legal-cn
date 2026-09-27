# Route B C03 WP-008 RDM-DSP-002 Authority-Comparison Reachability Limited Subject Design Proposal

## 0. Proposal Control

| Field | Value |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Lifecycle item | `RDM-DSP-002` |
| Artifact type | `LIMITED SUBJECT DESIGN PROPOSAL ONLY` |
| Activation semantics | `CAPABILITY_ONLY` |
| Authorized objective | Design the smallest control-flow revision that makes the existing final authority-reference comparison reachable |
| Proposal state | `MATERIALIZED — REVIEW NOT AUTHORIZED / NOT PERFORMED` |
| Subject modification | `NOT AUTHORIZED / NOT PERFORMED` |
| Input-binding or fixture modification | `NOT AUTHORIZED / NOT PERFORMED` |
| Python / subject / fixture execution | `NOT AUTHORIZED / NOT RUN` |
| Input admission | `NOT AUTHORIZED / NOT ESTABLISHED` |
| Git / independent ACOS | `NOT AUTHORIZED / NOT ACCESSED` |

This proposal defines a limited future source-revision path. It is not a patch,
an implementation, a source candidate, an accepted design, a reviewed rule, an
admitted input or execution evidence. `RDM-DSP-002` remains open.

## 1. Fixed Sources

| ID | Fixed source | SHA-256 | Qualification |
| --- | --- | --- | --- |
| `DSP002-SRC-001` | `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A` | Current subject; unchanged and not executed |
| `DSP002-SRC-002` | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | Current input-binding candidate; not admitted or modified |
| `DSP002-SRC-003` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_SCENARIO_INPUT_BINDING_LIMITATION_DISPOSITION_PROPOSAL.md` | `ACABF4368E1D5DC968F9EAD6569A6578108AF9B9E0926A1C94326EE498D040CE` | Accepted disposition design identifying `RDM-DSP-002` |
| `DSP002-SRC-004` | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_008_SCENARIO_INPUT_BINDING_COMPARISON_RULES_ACCEPTANCE_DECISION.md` | `5EAAC6DF5F7C5C6BAE31804486C59FCCD7E810DD389C94C87AB84165FD4CC8F6` | Project Owner acceptance of the five existing comparison rules; does not cover the unreachable branch |
| `DSP002-SRC-005` | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_SCENARIO_INPUT_BINDING_COMPARISON_RULES_ACCEPTANCE_DECISION_REVIEW.md` | `0EA48E3EDBAFD6565FC668BC4119DC51C078EB63D6D5CD83AF9E40E239E8B8AB` | Fixed-SHA record review closing `RDM-DSP-013`; does not resolve `RDM-DSP-002` |

## 2. Current Static Defect

The current `evaluate_identity_gate` control flow contains the following ordered
tail after all earlier capability, domain, packet, isolation, scope, input-set
and output-boundary checks:

| Current order | Existing behavior | Reachability |
| --- | --- | --- |
| `CURRENT-TAIL-01` | Return `ELIGIBLE_FOR_MAPPING` with reason `ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED` | Reachable when all earlier checks pass |
| `CURRENT-TAIL-02` | Compare `envelope.matter_authorization_reference`, `envelope.execution_authorization_reference` and `packet.decision_reference` against the expected references | Unreachable because `CURRENT-TAIL-01` always returns first |
| `CURRENT-TAIL-03` | On any mismatch, return `BLOCKED` with reason `BLOCKED — AUTHORITY BINDING FAILURE` | Unreachable for the same reason |

The defect is control-flow reachability only. This proposal does not claim that
any authorization reference is authentic, current, sufficient or legally
effective. The subject operates on metadata references and must continue to
distinguish reference consistency from positive authority.

## 3. Minimal Future Control-Flow Design

The proposed future source revision is limited to relocating the existing final
authority-reference comparison before the existing unconditional eligibility
return.

| Proposed order | Required future behavior | Change boundary |
| --- | --- | --- |
| `PROPOSED-TAIL-01` | Preserve the existing output-boundary membership check and its exact rejection output | No condition, state or reason-text change |
| `PROPOSED-TAIL-02` | Evaluate the existing three-part authority-reference comparison | Relocate the existing comparison; do not broaden or narrow it |
| `PROPOSED-TAIL-03` | If any of the three comparisons mismatches, return `BLOCKED` with exact reason `BLOCKED — AUTHORITY BINDING FAILURE` | Preserve exact state and reason text |
| `PROPOSED-TAIL-04` | Only if all three comparisons match, return `ELIGIBLE_FOR_MAPPING` with exact reason `ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED` | Preserve exact state and reason text |

No other check may be reordered, removed, combined, weakened or converted from
fail-closed to fall-through behavior. The future revision must not introduce an
`else` branch that hides a missing return, a default value, an inferred
reference, a truthiness shortcut or exception suppression.

## 4. Preserved Check Ordering

The complete future decision order must remain:

| Order | Check family | Existing protective outcome preserved |
| ---: | --- | --- |
| 1 | Kill state | `BLOCKED — KILL ACTIVE` |
| 2 | Missing or disabled capability | `BLOCKED — CAPABILITY NOT ACTIVE` |
| 3 | Revoked capability | `BLOCKED — AUTHORITY FAILURE` |
| 4 | Stale capability | `BLOCKED — VERSION FAILURE` |
| 5 | Capability identity fields | `BLOCKED — CAPABILITY IDENTITY FAILURE` |
| 6 | Route/domain/adapter identity fields | `BLOCKED — DOMAIN IDENTITY FAILURE` |
| 7 | Missing Tier B packet | `BLOCKED — TIER B AUTHORITY REQUIRED` |
| 8 | Packet state | `BLOCKED — AUTHORITY FAILURE` |
| 9 | Packet revocation and supplied validity | `BLOCKED — AUTHORITY FAILURE` |
| 10 | Matter/version/actor isolation | `REJECTED — ISOLATION FAILURE` |
| 11 | Purpose/operation scope | `REJECTED — SCOPE FAILURE` |
| 12 | Input-set identity | `BLOCKED — INPUT SET IDENTITY FAILURE` |
| 13 | Output-class boundary | `REJECTED — OUTPUT BOUNDARY FAILURE` |
| 14 | Matter/execution/decision-reference consistency | `BLOCKED — AUTHORITY BINDING FAILURE` |
| 15 | Eligibility return after every prior check passes | `ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED` |

The new position at order 14 is the latest possible reachable point before the
eligibility return. It therefore preserves every earlier failure precedence.

## 5. Reference-Consistency Semantics

| Reference comparison | Required equality | Mismatch outcome |
| --- | --- | --- |
| Matter authorization reference | `envelope.matter_authorization_reference` equals `expected.matter_authorization_reference` | Exact authority-binding failure |
| Execution authorization reference | `envelope.execution_authorization_reference` equals `expected.execution_authorization_reference` | Exact authority-binding failure |
| Packet decision reference | `packet.decision_reference` equals `expected.execution_authorization_reference` | Exact authority-binding failure |

Equality is a closed metadata-consistency check only. A match must not be
reported as authorization validation, grant existence, current authority,
Project Owner approval or permission to execute. The unchanged eligibility
reason must continue to state that separate matter invocation authority is
required.

## 6. Required Future V-002 Binding Revision

A source change makes the existing input-binding SHA stale for the changed
subject. After a separately reviewed and accepted source candidate exists, a
new Scenario Input Binding candidate must bind the new subject SHA and replace
the current unreachable observation with separately identifiable variants.

| Future variant | Stimulus requirement | Required raw observation | Fixture abstraction boundary |
| --- | --- | --- | --- |
| `V002-BIND-01` | Empty `matter_authorization_reference` supplied to `ExpectedIdentityReference` constructor | Existing exact `ValueError` and message | Constructor-level `AUTHORITY_OR_IDENTITY_FAILURE` only |
| `V002-BIND-02` | All earlier gate checks pass; envelope matter-authorization reference differs from expected | `BLOCKED` / `BLOCKED — AUTHORITY BINDING FAILURE` | V-002 gate-level authority-or-identity failure only |
| `V002-BIND-03` | All earlier gate checks pass; envelope execution-authorization reference differs from expected | Same exact raw state and reason | Same limited gate-level abstraction |
| `V002-BIND-04` | All earlier gate checks pass; packet decision reference differs from expected execution reference | Same exact raw state and reason | Same limited gate-level abstraction |
| `V002-BIND-05` | All earlier gate checks and all three reference comparisons pass | Existing `ELIGIBLE_FOR_MAPPING` state and exact eligibility reason | Control variant only; not authority approval or execution permission |

Each variant must bind every non-target field explicitly so that no earlier
branch masks the intended observation. The three mismatch variants must remain
separate even though they share one raw outcome.

The existing `CR-002-CONSTRUCTOR-FAILURE` remains limited to `V002-BIND-01`.
The future gate variants require a separate proposed comparison rule, suggested
identifier `CR-002-AUTHORITY-BINDING-FAILURE`, with this bounded design:

| Field | Proposed value |
| --- | --- |
| Status | `PROPOSED_NOT_REVIEWED_NOT_ACCEPTED` |
| Raw state | `BLOCKED` |
| Raw reason | `BLOCKED — AUTHORITY BINDING FAILURE` |
| Fixture state | `BLOCKED` |
| Fixture reason class | `AUTHORITY_OR_IDENTITY_FAILURE` |
| Post-hoc change | `PROHIBITED` |
| Scope | V-002 gate-level reference-consistency variants only |

This proposal does not create that rule inside the current binding and does not
accept it. The future rule must receive an independent fixed-SHA review and a
separate Project Owner decision.

## 7. Required Future Static and Regression Verification

No verification is authorized now. A later exact-SHA review package must define
and separately authorize at least the following checks:

| Verification ID | Required future check | Pass condition |
| --- | --- | --- |
| `DSP002-V-001` | Static reachability inspection | The three-part comparison lexically and structurally precedes the eligibility return in the revised function |
| `DSP002-V-002` | Control-flow exit inspection | Every mismatch path returns the exact authority-binding failure and the all-match path reaches the unchanged eligibility return |
| `DSP002-V-003` | Earlier-branch precedence matrix | Orders 1 through 13 retain their current precedence and exact outputs |
| `DSP002-V-004` | Matter-reference mismatch variant | Reaches order 14 and records the exact raw failure without fixture rewriting |
| `DSP002-V-005` | Execution-reference mismatch variant | Reaches order 14 and records the exact raw failure without fixture rewriting |
| `DSP002-V-006` | Packet-decision mismatch variant | Reaches order 14 and records the exact raw failure without fixture rewriting |
| `DSP002-V-007` | All-reference-match control | Reaches the unchanged eligibility return and does not assert authority grant or execution permission |
| `DSP002-V-008` | Constructor regression | Empty required constructor reference retains the existing exact `ValueError` behavior |
| `DSP002-V-009` | State and reason regression | No existing state or reason string changes outside the authorized relocation |
| `DSP002-V-010` | Side-effect boundary | Returned permitted-write set remains empty; no I/O, network, provider or external action is introduced |
| `DSP002-V-011` | Source-diff boundary | Only the exact comparison block relocation and removal of its unreachable old position are present |
| `DSP002-V-012` | Binding lineage | New subject and input-binding SHAs are complete; stale reviews and execution evidence are not transferred |

Static review must precede any future execution authorization. Execution, if
ever separately authorized, must preserve expected, raw observed and comparison
fields independently and must not calculate an aggregate PASS inside a Harness.

## 8. Revision, SHA and Staleness Lifecycle

| Stage | Required future artifact or decision | State now |
| ---: | --- | --- |
| 1 | Fixed-SHA review of this proposal | `NOT AUTHORIZED / NOT PERFORMED` |
| 2 | Project Owner acceptance or rejection of this proposal | `NOT AUTHORIZED / NOT ESTABLISHED` |
| 3 | Exact limited source-revision authorization | `NOT AUTHORIZED` |
| 4 | Revised `identity_gate.py` candidate with new SHA | `NOT CREATED` |
| 5 | Static review and Project Owner acceptance of revised subject | `NOT ESTABLISHED` |
| 6 | Revised Scenario Input Binding candidate with new subject SHA, five V-002 variants and proposed gate comparison rule | `NOT CREATED` |
| 7 | Independent review and Project Owner acceptance of the new comparison rule | `NOT ESTABLISHED` |
| 8 | Fixed-SHA review and admission decision for revised input binding | `NOT ESTABLISHED` |
| 9 | Later Harness, Manifest, evidence and execution decisions | `NOT AUTHORIZED` |

Any changed source or binding byte creates a new identity. Reviews, decisions,
comparison-rule acceptance and evidence bound to the current SHAs do not
automatically transfer. The existing five rules accepted under `RDM-DSP-013`
remain valid only for their unchanged fixed candidate text and do not accept
the new proposed V-002 gate rule.

## 9. Rollback and Withdrawal Boundaries

| Condition | Required protective result |
| --- | --- |
| Proposal rejected, held or withdrawn | Current subject and input binding remain unchanged; `RDM-DSP-002` remains HOLD |
| Future source candidate contains any change beyond the accepted relocation | Reject candidate; no partial adoption |
| Earlier check ordering or output text drifts | Reject candidate and keep current SHA authoritative |
| New branch is still unreachable or can fall through without a decision | Reject candidate |
| Reference equality is represented as authority validation | Reject candidate for semantic overreach |
| Revised binding omits any of the three mismatch variants or the all-match control | Block input admission |
| Comparison rule is absent, unreviewed or unaccepted | Block affected V-002 comparison and input admission |
| Any stale review or evidence is transferred to changed bytes | Reject lineage and require new review |
| Authorization is missing, withdrawn or exhausted | Stop without source, binding, Harness or evidence changes |

Rollback means retaining or restoring the previously accepted fixed source
identity through a separately authorized version-control action. This proposal
does not authorize a Git checkout, reset, revert, commit, branch or push.

## 10. Separation of Roles and Decisions

| Role or decision | Boundary |
| --- | --- |
| Project Owner | Sole positive authority for proposal acceptance, source revision, revised binding, comparison-rule acceptance, admission and execution |
| Internal design reviewer | May assess fixed text; cannot accept, implement or execute it |
| Source materializer | May modify the exact subject only after separate exact-scope authorization; cannot approve own change |
| Input-binding materializer | May bind only an accepted subject SHA under separate authority; cannot infer expected results |
| Validation executor | Not selected or authorized by this proposal |
| Independent evidence reviewer | Not selected or authorized by this proposal |

Stable role identity is sufficient. No real-person identity is required or
recorded.

## 11. Proposal Review Questions

| ID | Question |
| --- | --- |
| `DSP002-RQ-001` | Is the current subject bound to exact path and SHA? |
| `DSP002-RQ-002` | Is the unreachable comparison identified without claiming runtime execution? |
| `DSP002-RQ-003` | Is the proposed source change limited to relocating the existing comparison before the eligibility return? |
| `DSP002-RQ-004` | Are all existing conditions, states and reason strings preserved exactly? |
| `DSP002-RQ-005` | Are checks 1 through 13 kept in their existing order and precedence? |
| `DSP002-RQ-006` | Does a mismatch in any of the three references fail closed before eligibility? |
| `DSP002-RQ-007` | Does the all-match path retain the separate-authority-required eligibility reason? |
| `DSP002-RQ-008` | Is reference equality kept distinct from authority validation or execution permission? |
| `DSP002-RQ-009` | Are constructor rejection and gate-level comparison kept separate? |
| `DSP002-RQ-010` | Are three mismatch variants and one all-match control required? |
| `DSP002-RQ-011` | Is every non-target input required to pass earlier gates so target reachability is observable? |
| `DSP002-RQ-012` | Is a separate proposed gate comparison rule required without modifying the current binding? |
| `DSP002-RQ-013` | Are raw output and fixture abstraction protected from post-hoc rewriting? |
| `DSP002-RQ-014` | Are static review, source acceptance, revised binding and rule acceptance ordered before admission? |
| `DSP002-RQ-015` | Does every changed byte require a new SHA and prevent automatic evidence transfer? |
| `DSP002-RQ-016` | Do rollback and withdrawal retain the current fixed subject unless a separate action is authorized? |
| `DSP002-RQ-017` | Are V-003 and all other disposition items excluded? |
| `DSP002-RQ-018` | Are Harness, Manifest, evidence and Python execution excluded? |
| `DSP002-RQ-019` | Are Git and independent ACOS actions excluded? |
| `DSP002-RQ-020` | Is automatic input admission, blocker closure and C03 transition blocked? |

## 12. Proposal Acceptance Gates

| ID | Gate |
| --- | --- |
| `DSP002-G-001` | Exact subject path and SHA complete |
| `DSP002-G-002` | Exact input-binding, disposition and comparison-rule lineage complete |
| `DSP002-G-003` | Current unconditional-return reachability defect accurately described |
| `DSP002-G-004` | Minimal relocation-only design explicit |
| `DSP002-G-005` | Existing conditions, states and reason strings preserved |
| `DSP002-G-006` | Earlier checks and failure precedence preserved |
| `DSP002-G-007` | Three reference mismatches fail closed before eligibility |
| `DSP002-G-008` | All-match path retains separate-authority-required semantics |
| `DSP002-G-009` | Metadata consistency does not become authority validation |
| `DSP002-G-010` | Constructor and gate observations remain distinct |
| `DSP002-G-011` | Three mismatch variants plus all-match control required |
| `DSP002-G-012` | New proposed gate comparison rule separately identified and unaccepted |
| `DSP002-G-013` | Expected, raw observed and comparison values remain separate |
| `DSP002-G-014` | Static reachability and regression checks complete at design level |
| `DSP002-G-015` | New source and binding SHAs mandatory; stale evidence transfer prohibited |
| `DSP002-G-016` | Rollback and withdrawal boundaries fail closed |
| `DSP002-G-017` | V-003 and other disposition items unaffected |
| `DSP002-G-018` | No source, binding, Harness, Manifest, evidence or execution materialized |
| `DSP002-G-019` | Project, Git and independent ACOS boundaries preserved |
| `DSP002-G-020` | No automatic admission, closure, readiness or downstream transition |

## 13. Resulting State

```text
RDM-DSP-002 Limited Subject Design Proposal:
MATERIALIZED — REVIEW NOT AUTHORIZED / NOT PERFORMED

Current identity_gate.py:
UNCHANGED / NOT EXECUTED

Current Scenario Input Binding:
UNCHANGED / NOT ADMITTED

RDM-DSP-002:
OPEN — PROPOSED LIMITED DESIGN ROUTE ONLY

V-003 / RDM-DSP-003:
NOT DESIGNED BY THIS PROPOSAL / OPEN

RDM-DSP-004 THROUGH RDM-DSP-012:
OPEN / UNAFFECTED

Source Revision / Revised Binding / New Comparison Rule:
NOT AUTHORIZED / NOT CREATED / NOT ACCEPTED

Harness / Manifest / Evidence / Python Execution:
NOT AUTHORIZED / NOT CREATED / NOT RUN

C03 Readiness / Automatic Downstream Transition:
NOT READY / BLOCKED
```
