# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV6_CROSS_MODEL_REVIEW

## 2. Status

READY. The task is read-only.

## 3. Background

Codex reviewed AR-B-005 design R3 revision 5 (SHA-256 `57CEB3061F21C17DF9764CFA31EA747CA5FC5EE3F34B43A7E38A4FA8499DDA20`) as a human-executed procedural design. The verdict was FAIL, with two procedural blocking findings (J-01, J-02) and two non-blocking findings (NB-01, NB-02). The result is archived at `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV5_CROSS_MODEL_REVIEW_RESULT.md`.

Revision 6 is at the same path. It makes these changes:

1. **Stop-point index H (§6.5).** H is now append-only and applies to both L1 and L2.
   - Discovery events distinguish model stops from human stops. A human stop binds M, the discovery stage, the original-document location and a discovery record, with X marked "不适用".
   - Clearance events have two types: `FINDING_REFUTED`, which covers the issue for the whole case, and `CORRECTED_IN_CANDIDATE`, which covers that candidate only.
   - The lookup now covers all discovery events and checks whether a clearance covers the current candidate.
2. **Q records (§9.6).** Q1, Q2 and Q3 now have a fixed order and fixed references. Q3 must positively verify that the authorization itself is still valid: not withdrawn, within its own deadline and use count, and an exact match on action and scope.
3. **Restart rule (§3.3).** Work restarts from the earliest invalid record. Two forms of equivalent manual confirmation are defined (§3.1).
4. **Sampling (§十二).** Sampling may not resend the same M's package under any purpose.

Section 14.4 maps the round-5 findings to these changes. Annex A adds A-56 to A-63.

## 4. Goal

Review `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` (revision 6) to the same standard as rounds 4 and 5. Treat it as a procedural design executed by a human, without code enforcement. Do not fail it for the absence of V8, digital signatures or trusted time. Do fail it for ambiguous, circular or unexecutable procedural rules, for any relaxation of R2, or for a bypass that a diligent reviewer following the text would not catch.

Answer:

1. Is each of J-01, J-02, NB-01 and NB-02 resolved? Answer RESOLVED, PARTIALLY RESOLVED or NOT RESOLVED, with line references.
2. Are the H event model and the Q1, Q2 and Q3 sequence executable by a careful lawyer, and free of circularity?
3. Does any Annex A counterexample (A-01 to A-63) fail to be blocked by the rule it cites? Can you construct a new fictional counterexample that a diligent reviewer following revision 6 would not catch?
4. Did revision 6 introduce any new problem?

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_AR_B_005_R3_REV6_CROSS_MODEL_REVIEW_RESULT.md`.

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
