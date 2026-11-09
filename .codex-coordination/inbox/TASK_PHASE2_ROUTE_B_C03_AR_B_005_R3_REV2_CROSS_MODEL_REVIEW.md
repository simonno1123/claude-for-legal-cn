# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV2_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

Codex reviewed AR-B-005 design R3 (revision 1, SHA-256 `113F1EFD81A6C494C6EA2AD3CA74103097F6E5836196E52C1EFFA686296E1CB8`) and returned FAIL with six blocking findings (B-01 to B-06), two non-blocking findings (NB1, NB2) and notes. The result is archived at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_CROSS_MODEL_REVIEW_RESULT.md`.

Claude has revised the draft as R3 revision 2 at the same path. Following that review's recommendation, the revision includes Annex A, which gives fictional counterexamples showing how each of B-01 to B-06 is blocked. Section 十二 maps each finding to the change that addresses it.

## 4. Goal

Re-review `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` (revision 2) against:

- the previous review result (above);
- the adopted R2 and its adoption decision;
- plan §7.5 and §7.10, WP-007 §16.2 and §16.3, and `isolation.py` / `contracts.py`, as in the previous task.

Answer:

1. Is each of B-01 to B-06 resolved? For each one, give RESOLVED, PARTIALLY RESOLVED or NOT RESOLVED, with line references.
2. Are NB1 and NB2 and the notes addressed?
3. Does any Annex A counterexample fail to be blocked by the rule it cites? Can you construct a new fictional counterexample that bypasses revision 2?
4. Did revision 2 introduce any new problem, in particular any relaxation of R2 or any expansion of C03's permitted outputs?
5. Is the §九 V8 contract implementable as pure functions, and is the external-responsibility list complete?

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV2_CROSS_MODEL_REVIEW_RESULT.md`.

## 6. Forbidden Actions

1. Do not modify any other file.
2. Do not adopt, close or authorize anything; the Project Owner decides.
3. This repository is public. Do not add any real case material to it.

## 7. Output

Write the result file in Chinese. It must contain:

- a verdict: PASS, PASS WITH NOTES or FAIL;
- a per-finding resolution table for B-01 to B-06, NB1 and NB2;
- any new BLOCKING findings, NON-BLOCKING findings and notes, each with line references;
- a statement that the review is a cross-model review by Codex and is not a human or legal review.
