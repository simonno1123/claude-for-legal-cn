# Project Owner Decision — RDM-DSP-002 Authority-Comparison Reachability Proposal Acceptance

## 1. Decision Control

| Field | Value |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Lifecycle item | `RDM-DSP-002` |
| Decision authority | `Project Owner — SOLE POSITIVE AUTHORITY` |
| Human identity requirement | Stable Project Owner role is sufficient; no real-person identity is required or recorded |
| Decision | `PROPOSAL ACCEPTED — DESIGN-TEXT SCOPE ONLY` |
| Record state at materialization | `MATERIALIZED — DECISION-RECORD REVIEW NOT AUTHORIZED / NOT PERFORMED` |
| Activation semantics | `CAPABILITY_ONLY` |
| Subject revision | `NOT AUTHORIZED / NOT CREATED` |
| Input admission / execution | `NOT AUTHORIZED / NOT ESTABLISHED` |
| Automatic downstream transition | `BLOCKED` |

This record durably materializes the conversation-level Project Owner decision
accepting the limited design route. It does not implement the design, resolve
the source limitation or authorize a revised subject.

## 2. Bound Proposal and Review

| Asset | Path | SHA-256 | Recorded status |
| --- | --- | --- | --- |
| Accepted proposal | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL.md` | `85D7A4029D9667EFF7922CEDAA19570A7C6A68F36C2D6A66401F291B5F135A24` | `ACCEPTED — DESIGN-TEXT SCOPE ONLY` |
| Internal design review | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_008_RDM_DSP_002_AUTHORITY_COMPARISON_REACHABILITY_LIMITED_SUBJECT_DESIGN_PROPOSAL_REVIEW.md` | `73FF239F13E688544D83C1130568D1511F559B065C2FF81E7BD7E8BA1EB558E1` | `PASS — GRADE A`; 20/20 questions, 20/20 gates, zero defects |
| Current subject | `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A` | `UNCHANGED / LIMITATION PRESENT` |
| Current input binding | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | `UNCHANGED / NOT ADMITTED` |

The source and input-binding rows record the fixed identities to which the
accepted design responds. They are not accepted revised assets and were not
modified by this decision.

## 3. Accepted Design Outcome

The Project Owner accepts the following design-level outcome:

1. The existing three-part authority-reference comparison is to be relocated
   before the existing unconditional `ELIGIBLE_FOR_MAPPING` return in a future,
   separately authorized revision candidate.
2. All earlier capability, domain, packet, isolation, scope, input-set and
   output-boundary checks retain their current order and exact outputs.
3. A mismatch in any of the three existing comparisons retains the exact raw
   result `BLOCKED — AUTHORITY BINDING FAILURE`.
4. The all-match path retains the exact eligibility result
   `ELIGIBLE — SEPARATE MATTER INVOCATION AUTHORITY STILL REQUIRED`.
5. Reference equality remains metadata consistency only. It does not establish
   authentic, current or sufficient authority and does not permit execution.
6. The future revised input binding must separately cover the constructor
   failure, three reference-mismatch variants and one all-match control.
7. The proposed future rule `CR-002-AUTHORITY-BINDING-FAILURE` remains
   unmaterialized, unreviewed and unaccepted.
8. All changed source and input-binding bytes require new SHAs, new reviews and
   separate Project Owner decisions; old evidence cannot transfer.

## 4. Decision Effect and Remaining Closure Requirements

| Item | Effect of this decision |
| --- | --- |
| Limited source-design route | `ACCEPTED` |
| Proposal and review lineage | `BOUND` |
| Exact future source revision | `REQUIRES SEPARATE AUTHORIZATION` |
| Revised subject candidate | `NOT CREATED` |
| Revised subject review and acceptance | `NOT ESTABLISHED` |
| Revised Scenario Input Binding | `NOT CREATED` |
| Future gate comparison rule | `NOT MATERIALIZED / NOT REVIEWED / NOT ACCEPTED` |
| `RDM-DSP-002` | `OPEN — DESIGN ROUTE ACCEPTED / SOURCE LIMITATION NOT RESOLVED` |

`RDM-DSP-002` may be closed only after the exact revised subject, static
reachability review, revised input binding and required comparison contract are
separately materialized, reviewed, accepted and SHA-bound.

## 5. Explicit Non-Authorizations

| Activity or asset | State |
| --- | --- |
| Review and fixed-SHA acceptance of this newly materialized decision record | `NOT AUTHORIZED / NOT PERFORMED` |
| Modification of `identity_gate.py` or any source | `NOT AUTHORIZED` |
| Scenario Input Binding or fixture modification | `NOT AUTHORIZED` |
| New comparison-rule materialization or acceptance | `NOT AUTHORIZED` |
| Python import, test, subject call or validation execution | `NOT AUTHORIZED / NOT RUN` |
| Harness, Runtime Dependency Manifest or evidence creation | `NOT AUTHORIZED / NOT CREATED` |
| Input admission or C03 readiness decision | `NOT AUTHORIZED / NOT READY` |
| Route A, OCR, case-material or legal processing | `NOT AUTHORIZED` |
| Provider, model, network, API, Connector or MCP invocation | `NOT AUTHORIZED` |
| Independent ACOS source-project access or modification | `NOT AUTHORIZED` |
| Git stage, commit, branch, merge, push or remote operation | `NOT AUTHORIZED` |
| Automatic downstream transition | `BLOCKED` |

## 6. Decision-Record Review Questions

| ID | Question |
| --- | --- |
| `DSP002-DEC-RQ-001` | Does the record bind the exact accepted proposal SHA? |
| `DSP002-DEC-RQ-002` | Does the record bind the exact internal-review SHA and accurate result counts? |
| `DSP002-DEC-RQ-003` | Is the decision limited to acceptance of the design-text route? |
| `DSP002-DEC-RQ-004` | Is the minimal comparison-block relocation accurately recorded? |
| `DSP002-DEC-RQ-005` | Are all earlier checks and exact outputs preserved? |
| `DSP002-DEC-RQ-006` | Is reference equality kept distinct from positive authority? |
| `DSP002-DEC-RQ-007` | Are all five future V-002 variants retained? |
| `DSP002-DEC-RQ-008` | Is the future gate comparison rule expressly unaccepted? |
| `DSP002-DEC-RQ-009` | Are new SHAs and non-transfer of stale evidence required? |
| `DSP002-DEC-RQ-010` | Does `RDM-DSP-002` remain open until implementation and re-binding prerequisites pass? |
| `DSP002-DEC-RQ-011` | Are V-003 and other disposition items unaffected? |
| `DSP002-DEC-RQ-012` | Are execution, Git and independent ACOS actions excluded? |

## 7. Decision-Record Acceptance Gates

| ID | Gate |
| --- | --- |
| `DSP002-DEC-G-001` | Proposal identity and SHA exact |
| `DSP002-DEC-G-002` | Review identity, SHA and counts exact |
| `DSP002-DEC-G-003` | Project Owner design-text acceptance accurately recorded |
| `DSP002-DEC-G-004` | Minimal future source change fixed without implementation |
| `DSP002-DEC-G-005` | Earlier fail-closed ordering and raw outputs preserved |
| `DSP002-DEC-G-006` | Reference consistency does not become authority validation |
| `DSP002-DEC-G-007` | Five future V-002 variants preserved |
| `DSP002-DEC-G-008` | New comparison rule remains uncreated and unaccepted |
| `DSP002-DEC-G-009` | New identities and no stale-evidence transfer required |
| `DSP002-DEC-G-010` | `RDM-DSP-002` remains open pending full closure evidence |
| `DSP002-DEC-G-011` | Other disposition items remain open and unaffected |
| `DSP002-DEC-G-012` | No source, execution, Git or independent ACOS authority |

## 8. Resulting State

```text
RDM-DSP-002 Limited Subject Design Proposal:
ACCEPTED — DESIGN-TEXT SCOPE ONLY

Proposal Internal Review:
PASS — GRADE A

Decision Record:
MATERIALIZED — FIXED-SHA REVIEW NOT AUTHORIZED / NOT PERFORMED

RDM-DSP-002:
OPEN — DESIGN ROUTE ACCEPTED / SOURCE LIMITATION NOT RESOLVED

Current identity_gate.py / Current Scenario Input Binding:
UNCHANGED / NOT EXECUTED / NOT ADMITTED

Revised Subject / Revised Binding / New Comparison Rule:
NOT AUTHORIZED / NOT CREATED / NOT ACCEPTED

Harness / Manifest / Evidence / Python Execution:
NOT AUTHORIZED / NOT CREATED / NOT RUN

C03 Readiness / Automatic Downstream Transition:
NOT READY / BLOCKED
```
