# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

AR-B-005 is the qualified-human review gate for C03. Its design R2 was adopted on 2026-11-08 and closed with limitations. One of those limitations is a concentration: the project has a single practising lawyer, who is both the reviewer and the downstream authorizer.

All earlier reviews of this design came from the same model family as its author. The Project Owner has asked for design R3 to reduce that concentration, and has asked Codex, a model from a different vendor, to review R3. This review is the first independent cross-model check of the C03 governance designs.

## 4. Goal

Review the draft `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` against the following sources:

- the adopted R2 design: `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET.md`;
- the adoption decision: `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_005_ADOPTION_AND_CLOSURE_DECISION.json`;
- plan §7.5 and §7.10: `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN.md`;
- WP-007 §16.2 and §16.3: `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN.md`;
- the code: `scripts/phase2_runtime/route_b_c03/isolation.py` and `contracts.py`.

The review should answer these questions:

1. Does R3 keep every R2 requirement? Does it keep "AI is never the reviewer"?
2. Are the risk tiers (L1 and L2) well defined and fail-closed? Could an L2 candidate slip into L1?
3. Is the cross-model check limited to advice only?
   - Is the de-identified-packet rule workable?
   - Is the rule on disagreements adequate, in particular for C5, C6 and C7?
4. Is the two-time-point rule meaningful? Can it be gamed?
5. Is the client-confirmation rule consistent with a Chinese lawyer's duties of confidentiality and loyalty to the client? Could it be read as turning the candidate into advice to the client?
6. Is the code-enforcement scope in §八 implementable as pure functions within the current design?
   - The current design has no I/O, no clock and no persistence.
   - Is anything missing or unenforceable?
7. Are the remaining limitations in §九 stated honestly?

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_CROSS_MODEL_REVIEW_RESULT.md`.

## 6. Forbidden Actions

1. Do not modify any other file.
2. Do not adopt, close or authorize anything; the Project Owner decides.
3. This repository is public. Do not add any real case material to it.

## 7. Output

Write the result file in Chinese. It must contain:

- a verdict: PASS, PASS WITH NOTES or FAIL;
- BLOCKING findings, NON-BLOCKING findings and notes, each with line references;
- a statement that the review is a cross-model review by Codex and is not a human or legal review.
