# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV5_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

Codex reviewed AR-B-005 design R3 revision 4 (SHA-256 `22F6412A11A6D766113BBBD73DF3BAC0CD1C4AABC8E8A8E3417C1F771244BE60`) as a human-executed procedural design. The verdict was FAIL, with three procedural blocking findings (H-01 to H-03) and three non-blocking findings (N-01 to N-03). The result is archived at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV4_CROSS_MODEL_REVIEW_RESULT.md`.

Revision 5 is at the same path. It makes the following changes:

- It adds a pre-review declaration record I, which carries the R2 E-006 signature collected before the review starts (§3.1, §3.2).
- It rewrites Q as an item-by-item comparison check. Q is now required at three points: at application, at authorization and before use (§9.6).
- It adds a private stop-point index H, together with a lookup that must happen before sending (§6.5). It also clarifies that a stop raised in the current round can be cleared on the same M (§6.4).
- It clarifies N-01 to N-03 (§4.4, §7.4, §十二).

Section 14.3 maps each round-4 finding to the change that addresses it. Annex A adds counterexamples A-49 to A-55.

## 4. Goal

Review `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` (revision 5). Use the same standard as round 4: treat it as a procedural design executed by a human, without code enforcement. Do not fail it because V8, digital signatures or trusted time do not exist yet. Do fail it for ambiguous, circular or unexecutable procedural rules, for any relaxation of R2, or for any bypass that a diligent reviewer following the text would not catch.

Answer the following:

1. Are H-01, H-02, H-03 and N-01 to N-03 resolved? Answer RESOLVED, PARTIALLY RESOLVED or NOT RESOLVED for each, with line references.
2. Can a careful lawyer actually carry out the new records I, Q (at three points) and H? Is any of them circular or contradictory?
3. Does any Annex A counterexample (A-01 to A-55) fail to be blocked by the rule it cites? Can you construct a new fictional counterexample that a diligent reviewer following revision 5 would not catch?
4. Did revision 5 introduce any new problem, such as a relaxation of R2 or an expansion of C03's permitted outputs or audiences?

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV5_CROSS_MODEL_REVIEW_RESULT.md`.

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
