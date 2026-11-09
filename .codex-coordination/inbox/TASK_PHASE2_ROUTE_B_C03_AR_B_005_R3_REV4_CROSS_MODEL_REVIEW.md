# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV4_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

Codex reviewed AR-B-005 design R3 revision 3 (SHA-256 `8D65B5D22209CC3E77A0504829246DF9A09AA8A0249B68A4A768D666B540B642`) and returned FAIL with five blocking findings, G-01 to G-05. The result is archived at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV3_CROSS_MODEL_REVIEW_RESULT.md`.

On 2026-11-09 the Project Owner chose to **split** the work.

- **R3** now contains only the procedural rules that the reviewer carries out by hand.
- **Code enforcement (V8)** moves to a separate design, `C03-GATE-ENFORCEMENT-V8`, which will be reviewed separately. That covers signatures, trusted time, anti-replay, trust roots, the closed input contract and the reason codes.
- R3 §十 now only lists the known requirements carried over to V8, which include G-02 and G-05.

Revision 4 is at the same path.

## 4. Goal

Review `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` (revision 4) **as a procedural design that a human executes without code enforcement**.

- Do not fail it because V8 does not yet exist. §十 and §十三 item 2 state openly that, until V8 runs, the procedural rules have no code enforcement.
- Do fail it if a procedural rule is ambiguous, circular, or unexecutable by a careful lawyer.
- Do fail it if a rule relaxes R2.
- Do fail it if a bypass exists that a diligent reviewer following the text would not catch.

References: all three earlier review results; the adopted R2 and its adoption decision; plan §7.5 and §7.10; WP-007 §16.

Answer:

1. Are G-01, G-03 and G-04, and N-01 and N-02, resolved at the procedural level? Answer RESOLVED, PARTIALLY RESOLVED or NOT RESOLVED, with line references.
2. Are the procedural parts of G-02 (§9.4 and the Q record in §9.6) and of G-05 (§十一) adequate for a human-executed process?
3. Is the §十 hand-over list complete enough to start the V8 design? It does not need to be a contract yet.
4. Does any Annex A counterexample (A-01 to A-48) fail to be blocked by the rule it cites? Can you construct a new fictional counterexample that a diligent reviewer following revision 4 would not catch?
5. Did revision 4 introduce any new problem? In particular:
   - any relaxation of R2;
   - any expansion of C03's permitted outputs or audiences;
   - a split that hides a gap R2 relied on.

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV4_CROSS_MODEL_REVIEW_RESULT.md`.

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
