# Route B C03 WP-008 — Scenario Input Binding Limitation Disposition Proposal

## 1. Asset identity and authority boundary

| Field | Record |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Lifecycle step | `RDM-V2-04 LIMITATION DISPOSITION DESIGN` |
| Artifact type | `DISPOSITION PROPOSAL ONLY` |
| Proposal state | `PROPOSED — NOT REVIEWED / NOT ADOPTED / NON-OPERATIVE` |
| Activation semantics | `CAPABILITY_ONLY` |
| Authorized action | Materialize one proposal that classifies and routes the thirteen recorded input-admission blockers |
| Input admission | `NOT AUTHORIZED / NOT ESTABLISHED` |
| Subject or fixture modification | `NOT AUTHORIZED` |
| Comparison-rule acceptance | `NOT AUTHORIZED` |
| Harness / Manifest / evidence | `NOT AUTHORIZED / NOT CREATED BY THIS PROPOSAL` |
| Python / subject execution | `NOT AUTHORIZED / NOT RUN` |
| Git / independent ACOS | `NOT AUTHORIZED / NOT ACCESSED` |

This proposal is a routing design, not a limitation-resolution decision. It does
not repair code, accept a comparison rule, admit the input binding, reduce the
original fifteen-scenario requirements or establish C03 readiness.

## 2. Fixed sources

| ID | Source | SHA-256 | Qualification |
| --- | --- | --- | --- |
| `DSP-SRC-001` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_TRUSTED_IMPORT_AND_INPUT_BINDING_LIMITED_REVISION_PROPOSAL.md` | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` | Original limited-revision proposal; unchanged |
| `DSP-SRC-002` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_1_CANDIDATE.md` | `3432D99D22AA288668C8D4E2CF58975A794ED545B62EB05FCA9E0B41525AEDDB` | Adopted design source at conversation level; durable detached adoption record still required before use |
| `DSP-SRC-003` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_1_CANDIDATE.md` | `07FD553F641CF52EF54FABFCFAD448CC2D432C8A0279082E6DB899EB8C900910` | Adopted companion design source at conversation level; same qualification |
| `DSP-SRC-004` | `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json` | `92303974B76DFB9C4ECFDBE452EFB4728E0EEB861FFB1D2EDC7660EFFD27EEA5` | RDM-V2-03 candidate; preparation review PASS; not admitted or executed |

The RDM-V2-03 review is a conversation-level read-only review record. It found
no preparation-fidelity defect, while preserving all thirteen admission
blockers. This proposal does not convert that review into a durable acceptance
receipt or final input-admission review.

## 3. Disposition semantics

| Disposition | Exact effect | Effect it does not have |
| --- | --- | --- |
| `GOVERNANCE_BINDING_REQUIRED` | Requires a separately materialized, reviewed and accepted detached source/adoption record | Does not infer historical authority or mutate a source file |
| `DETACHED_RULE_REVIEW_REQUIRED` | Sends fixed proposed comparison text to separate independent review and Project Owner decision | Does not accept the rule or change observed output |
| `REVISED_BINDING_REQUIRED` | Requires a new input-binding candidate and new SHA after a rule ID, argument, adapter or observation contract changes | Does not transfer the current candidate review or admission |
| `LIMITED_SUBJECT_DESIGN_REQUIRED` | Requires separate design authority before any subject/API/control-surface change | Does not authorize code modification or implementation |
| `CONTINUED_HOLD` | Preserves the exact original requirement as unresolved and keeps affected admission/preflight blocked | Does not waive, narrow, pass or close the requirement |

Every Project Owner disposition must select one or more exact routes for the
identified item. Silence, general approval, report quality, candidate fidelity
or a comparison-rule PASS cannot be treated as resolution of a different item.

## 4. Thirteen-item disposition matrix

| ID | Candidate blocker | Current fact | Permitted future disposition choices | Default protective route | Closure evidence required before the blocker can be marked resolved |
| --- | --- | --- | --- | --- | --- |
| `RDM-DSP-001` | Durable detached design-pair adoption receipt is not materialized | V3.1 and Plan V2.1 are bound in the candidate with a conversation-level adoption qualification only | `GOVERNANCE_BINDING_REQUIRED` | Keep final admission blocked | Exact V3.1 and Plan V2.1 SHAs, scope/boundary text, Project Owner decision, independent review lineage and detached record SHA |
| `RDM-DSP-002` | V-002 final authority comparison is unreachable | The authority-reference comparison follows an unconditional return in fixed `identity_gate.py` | `CONTINUED_HOLD` or separately authorized `LIMITED_SUBJECT_DESIGN_REQUIRED`, followed by code/candidate re-binding if later approved | `CONTINUED_HOLD` | Accepted design and exact revised subject SHA; static reachability review; revised input binding and comparison contract; no evidence transfer from the old SHA |
| `RDM-DSP-003` | V-003 raw `BLOCKED` output lacks an accepted mapping to `BLOCKED_STALE` | Three identity mismatch calls are bound, but their raw state and fixture abstraction remain different | `CONTINUED_HOLD` or design/review a new fixed comparison rule, then `REVISED_BINDING_REQUIRED` | `CONTINUED_HOLD` | Independent rule rationale proving no post-hoc relabeling; accepted rule ID; revised binding that names it; fixed-SHA review |
| `RDM-DSP-004` | V-004 lacks project/session/provider observation surfaces | Existing gate exposes matter/version/actor comparisons, not all four fixture boundary classes | `CONTINUED_HOLD` or separately authorized `LIMITED_SUBJECT_DESIGN_REQUIRED` | `CONTINUED_HOLD` | Accepted exact observation-surface design and implementation; separate variants for each original boundary; revised subject and binding SHAs |
| `RDM-DSP-005` | V-006 has no idempotency or duplicate-effect mechanism | `IdempotencyKeyReference` only constructs immutable metadata | `CONTINUED_HOLD` or separately authorized idempotency/replay-control design | `CONTINUED_HOLD` | Accepted mechanism, duplicate-call sequence, fresh-state rule, side-effect observation and exact revised subject/binding identities |
| `RDM-DSP-006` | V-008 has no clock, timer or timeout-enforcement mechanism | `TimeoutPolicyReference` is data only; no accepted clock or late-result observer exists | `CONTINUED_HOLD` or separately authorized timeout-control design | `CONTINUED_HOLD` | Accepted clock/start/deadline provenance, termination observation and late-result rule, with exact revised identities |
| `RDM-DSP-007` | V-009 lacks an accepted revocation receipt boundary | Given-state denial is observable; propagation time and post-receipt no-action are not | `CONTINUED_HOLD` or separately authorized revocation-receipt/propagation design | `CONTINUED_HOLD` | Accepted receipt identity, boundary semantics and before/after observation surface; revised subject/binding identities if code changes |
| `RDM-DSP-008` | V-010 lacks an external kill propagation/enforcement mechanism | Supplied flags and null release decision do not establish an external kill switch | `CONTINUED_HOLD` or separately authorized kill/immutable-release-boundary design | `CONTINUED_HOLD` | Accepted external signal identity, propagation and self-release prevention evidence; exact revised identities |
| `RDM-DSP-009` | V-011 has no rollback evaluator or mechanism | `RollbackReference` is a record contract, not an eligibility or restoration function | `CONTINUED_HOLD` or separately authorized rollback design | `CONTINUED_HOLD` | Accepted eligibility/authority/restoration/post-state design and observation surface; exact revised identities |
| `RDM-DSP-010` | V-012 has no integrity detector or chain verifier | A caller can supply `MISMATCH` and construct an audit candidate, but this is not detection | `CONTINUED_HOLD` or separately authorized integrity-chain design | `CONTINUED_HOLD` | Accepted independently grounded detector/chain/isolation/release design and evidence boundary; exact revised identities |
| `RDM-DSP-011` | V-013 has no unavailable-dependency/provider observation surface | `NullProviderPort` returns `PROVIDER NOT AUTHORIZED`, not unavailable | `CONTINUED_HOLD` or separately authorized unavailable-provider/dependency design | `CONTINUED_HOLD` | Accepted distinct unavailable-state surface and raw-output contract; no network or real fault injection under this proposal |
| `RDM-DSP-012` | V-015 has no legal/downstream classification-denial surface | Type-valid `CandidateClass` members do not represent legal advice or downstream authority | `CONTINUED_HOLD` or separately authorized classification-boundary design | `CONTINUED_HOLD` | Accepted non-legal classification contract and exact denial surface; no legal reasoning, real matter or automatic downstream action |
| `RDM-DSP-013` | Five proposed comparison rules are not reviewed or accepted | Rules for V-001, V-002 constructor, V-005, V-007 and V-014 are embedded as `PROPOSED_NOT_ACCEPTED` | `DETACHED_RULE_REVIEW_REQUIRED`; any changed rule also triggers `REVISED_BINDING_REQUIRED` | Keep every referenced comparison blocked | Exact rule text and candidate SHA, independent per-rule determination, Project Owner acceptance, detached decision SHA and proof that observed/raw values remain separate |

## 5. Rule-review packet boundary

The five existing rule candidates may be reviewed together only if each receives
an independent determination and rationale:

| Rule ID | Scenario | Review question |
| --- | --- | --- |
| `CR-001-RAW-GATE-TO-ABSTRACT-ORACLE` | V-001 | Does raw `BLOCKED — TIER B AUTHORITY REQUIRED` support the fixture reason class without asserting real authority absence? |
| `CR-002-CONSTRUCTOR-FAILURE` | V-002 constructor only | Does the exact `ValueError` support only the constructor-level fixture class, while the unreachable gate comparison remains HOLD? |
| `CR-005-PROHIBITED-KEY-EXCEPTION` | V-005 | Does the exact top-level key exception support only the limited classification mapping without extending to nested/value channels? |
| `CR-007-RETRY-ELIGIBILITY` | V-007 | Does the raw eligibility result support only eligibility, never actual retry/deadline enforcement? |
| `CR-014-PROHIBITED-NAMESPACE-EXCEPTION` | V-014 | Does the pure metadata exception support only the namespace check, never an actual filesystem/Git/remote denial? |

Review of these rules must not supply the missing V-003 mapping. V-003 requires
its own new design and, if adopted, a revised binding candidate. A rule reviewer
cannot edit the candidate, infer a missing rule or accept all rules as a bundle
without five separate determinations.

## 6. Decision ordering and staleness

1. Review and dispose this proposal at its own fixed SHA.
2. Materialize and accept the detached design-pair adoption record required by
   `RDM-DSP-001`.
3. Independently review the five existing comparison rules and obtain a separate
   Project Owner decision; no report grants acceptance by itself.
4. Issue an exact per-item disposition for `RDM-DSP-002` through
   `RDM-DSP-012`: continued HOLD or a separately scoped design route.
5. If any adapter, argument, rule ID, observation surface, subject or fixture
   changes, materialize a new scenario-input-binding candidate with a new SHA.
6. Only a candidate with no unresolved input/observation requirement may enter
   final input-admission review. A HOLD disposition does not make it complete.
7. Harness source authority remains downstream and cannot precede the required
   fixed-SHA input admission. Manifest generation and execution remain later,
   separately authorized stages.

No prior review, decision or evidence automatically transfers to changed bytes.
No future artifact may be hashed into the current candidate after the fact.

## 7. Review questions

| ID | Question |
| --- | --- |
| `RDM-DSP-RQ-001` | Is the proposal bound to the exact four source identities without self-hash or future-artifact circularity? |
| `RDM-DSP-RQ-002` | Are all thirteen candidate blockers represented exactly once? |
| `RDM-DSP-RQ-003` | Are candidate fidelity, limitation disposition, resolution, input admission and execution readiness kept distinct? |
| `RDM-DSP-RQ-004` | Does every continued HOLD preserve the original requirement without waiver or PASS? |
| `RDM-DSP-RQ-005` | Does every source-change route require separate design/code authority and new fixed identities? |
| `RDM-DSP-RQ-006` | Is the unreachable V-002 comparison kept distinct from the observable constructor rejection? |
| `RDM-DSP-RQ-007` | Is V-003 prevented from receiving an inferred or post-hoc comparison mapping? |
| `RDM-DSP-RQ-008` | Are V-004 boundary classes prevented from collapsing into matter/actor coverage? |
| `RDM-DSP-RQ-009` | Is V-006 kept blocked unless an actual duplicate/idempotency observation exists? |
| `RDM-DSP-RQ-010` | Is V-008 kept blocked unless a real accepted temporal observation contract exists? |
| `RDM-DSP-RQ-011` | Are revocation and kill propagation distinguished from supplied state flags? |
| `RDM-DSP-RQ-012` | Are rollback and integrity reference construction distinguished from mechanisms and detection? |
| `RDM-DSP-RQ-013` | Is unavailable-provider behavior kept distinct from provider-not-authorized behavior? |
| `RDM-DSP-RQ-014` | Is the V-015 route non-legal and free of real-matter or downstream authority? |
| `RDM-DSP-RQ-015` | Do the five existing comparison rules require five independent determinations? |
| `RDM-DSP-RQ-016` | Does any changed rule, adapter, input or subject force a revised binding and new review? |
| `RDM-DSP-RQ-017` | Is a durable detached design-pair record required without rewriting historical state? |
| `RDM-DSP-RQ-018` | Are Harness, Manifest, evidence and Python execution kept outside this proposal? |
| `RDM-DSP-RQ-019` | Are Git and independent ACOS kept outside project actions? |
| `RDM-DSP-RQ-020` | Does the ordering prevent automatic admission or downstream transition? |

## 8. Acceptance gates

| ID | Gate |
| --- | --- |
| `RDM-DSP-G-001` | Four fixed source SHAs complete and exact |
| `RDM-DSP-G-002` | Thirteen blockers, thirteen disposition rows, zero omission |
| `RDM-DSP-G-003` | No blocker marked resolved by this proposal |
| `RDM-DSP-G-004` | Continued HOLD has no waiver, narrowing or PASS effect |
| `RDM-DSP-G-005` | Separate authority required for every design/code path |
| `RDM-DSP-G-006` | V-002 constructor and unreachable comparison separated |
| `RDM-DSP-G-007` | V-003 missing rule cannot be inferred |
| `RDM-DSP-G-008` | V-004 multi-boundary coverage not collapsed |
| `RDM-DSP-G-009` | V-006/V-008 absent mechanisms remain blocked |
| `RDM-DSP-G-010` | V-009/V-010 external-control limits remain explicit |
| `RDM-DSP-G-011` | V-011/V-012 construction cannot stand for operation/detection |
| `RDM-DSP-G-012` | V-013 unavailable and unauthorized semantics separated |
| `RDM-DSP-G-013` | V-015 remains non-legal and downstream-blocked |
| `RDM-DSP-G-014` | Five existing rules receive itemized independent review |
| `RDM-DSP-G-015` | Changed bytes require new SHA and no evidence transfer |
| `RDM-DSP-G-016` | Durable adoption record required before final admission |
| `RDM-DSP-G-017` | Final admission prohibited while any required binding remains HOLD/unbound |
| `RDM-DSP-G-018` | Harness/Manifest/evidence/execution remain unauthorized |
| `RDM-DSP-G-019` | Project/ACOS/Git boundary preserved |
| `RDM-DSP-G-020` | No automatic downstream transition |

## 9. Resulting state

```text
RDM-V2-04 Disposition Proposal:
MATERIALIZED — REVIEW NOT AUTHORIZED / NOT PERFORMED

Thirteen Admission Blockers:
ROUTED AS CANDIDATE OPTIONS — NONE RESOLVED

Comparison Rules:
5 PROPOSED / 0 REVIEWED / 0 ACCEPTED

Scenario Input Binding Admission:
NOT AUTHORIZED / NOT ESTABLISHED

New Harness / Runtime Dependency Manifest / Evidence / Execution:
NOT AUTHORIZED / NOT CREATED BY THIS PROPOSAL / NOT RUN

C03 Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```
