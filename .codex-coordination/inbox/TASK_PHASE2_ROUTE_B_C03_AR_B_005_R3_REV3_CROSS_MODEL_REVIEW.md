# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV3_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

Codex reviewed AR-B-005 design R3 revision 2 (SHA-256 `EF370CBBCDA52D3A7A6F6D9E6322263EB99DFA8504F2A4929F46795D7EA6E625`) and returned FAIL. That review raised five blocking findings (F-01 to F-05) and two non-blocking findings (NB-01, NB-02). The result is archived at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV2_CROSS_MODEL_REVIEW_RESULT.md`. The first-round result is still at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_CROSS_MODEL_REVIEW_RESULT.md`.

Claude has revised the draft as R3 revision 3, at the same path as before. The main changes are:

- an immutable review-input manifest M with a one-way chain of appended records (§三);
- a closed allowed-use table (§四);
- an egress chain E → S → X (§七);
- a validity cutoff for both tiers, plus positive reconfirmation in event P (§九);
- a closed V8 contract with signatures (§十);
- an external-facts handoff contract (§十一);
- a single sampling algorithm (§十二).

Section 十四 maps every finding from both rounds to the change that addresses it. Annex A contains 36 fictional counterexamples: A-01 to A-19, corrected after round 2, and A-20 to A-36, which are new.

## 4. Goal

Re-review `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` (revision 3). Use as your references both earlier review results, the adopted R2 and its adoption decision, plan §7.5 and §7.10, WP-007 §16, and `isolation.py` / `contracts.py`.

Answer:

1. Is each of F-01 to F-05, NB-01 and NB-02 resolved? For each one, give RESOLVED, PARTIALLY RESOLVED or NOT RESOLVED, with line references. Re-assess the round-1 items that were still open (B-01, B-03, B-04, B-06, NB1).
2. Does any Annex A counterexample fail to be blocked by the rule it cites? Can you construct a new fictional counterexample that bypasses revision 3?
3. Did revision 3 introduce any new problem? In particular:
   - any relaxation of R2;
   - any expansion of C03's permitted outputs or audiences;
   - any internal inconsistency between the reason codes and the rules.
4. Item 5 of §十五 notes that client records are now required by no allowed use, which is narrower than the owner's original direction. Is that consistent with R2 §八 and B-05?
5. Is the §十 V8 contract implementable as pure functions? Is the §十一 handoff contract complete enough to start V8 implementation once the owner adopts the design?

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV3_CROSS_MODEL_REVIEW_RESULT.md`.

## 6. Forbidden Actions

1. Do not modify any other file.
2. Do not adopt, close or authorize anything; the Project Owner decides.
3. This repository is public. Do not add any real case material to it.

## 7. Output

Write the result file in Chinese. It must contain:

- a verdict: PASS, PASS WITH NOTES or FAIL;
- a per-finding resolution table;
- any new BLOCKING findings, NON-BLOCKING findings and notes, each with line references;
- a statement that the review is a cross-model review by Codex and is not a human or legal review.
