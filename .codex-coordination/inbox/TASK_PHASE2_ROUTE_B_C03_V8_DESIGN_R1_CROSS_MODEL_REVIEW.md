# Codex Task

## 1. Task ID

TASK_PHASE2_ROUTE_B_C03_V8_DESIGN_R1_CROSS_MODEL_REVIEW

## 2. Status

READY. This task is read-only.

## 3. Background

AR-B-005 gate design R3 (revision 9) was adopted on 2026-11-10. Its §十 hands code enforcement over to a separate design, `C03-GATE-ENFORCEMENT-V8`.

A first L1 trial run under R3 produced findings TF-01 to TF-05, recorded in `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_R3_L1_TRIAL_RUN_AUTHORIZATION.md`. Two of them matter here: manual filling was too heavy, and multi-select questions caused missed items.

Claude has drafted V8 design R1 at `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_V8_GATE_ENFORCEMENT_DESIGN.md`. The design proposes two phases:

- **V8-A:** record contracts, a pure-function validator, a local command-line wrapper, a record builder and tests.
- **V8-B:** signatures, trusted time and anti-replay. These are deferred, with the reasons stated in §九.

## 4. Goal

Review V8 design R1 against:

- adopted R3: `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md`, SHA-256 `1029BD425BDBC10DD641FA4AC6A85A2845E75AD0C17B7FABA1342C3E49C0CFEB`;
- the R3 adoption decision;
- the trial record;
- WP-007 §16;
- the existing code in `scripts/phase2_runtime/route_b_c03/`.

Answer:

1. Does V8-A faithfully encode R3? Look for any rule that is relaxed, missing or added relative to R3.
2. Are the record contracts (§四) and the rule table (§五) complete and internally consistent? Are the reason codes and their ordering unambiguous?
3. Is the core implementable as pure functions? Is the boundary with the wrapper and the record builder clean?
4. Does the record builder keep "AI is never the reviewer"? In particular, can it produce any judgment item on the reviewer's behalf?
5. Is the §六 list of things code cannot do honest and complete?
6. Is deferring V8-B acceptable, given that R3's §十三 limitations stay in force until V8-B exists?
7. Is the test plan (§八) adequate?

Apply the same standard as the R3 rounds 4–9. Do not fail the design solely because V8-B is deferred, since that is disclosed. Do fail it for a relaxation of R3, an ambiguity that would let an implementation pass something R3 blocks, or a builder path that lets AI decide.

## 5. Allowed Scope

- Read anything in the repository.
- Write only `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_V8_DESIGN_R1_CROSS_MODEL_REVIEW_RESULT.md`.

## 6. Forbidden Actions

1. Do not modify any other file.
2. Do not adopt, close or authorize anything; the Project Owner decides.
3. This repository is public. Do not add any real case material to it.

## 7. Output

Write the result file in Chinese. It must contain:

- a verdict: PASS, PASS WITH NOTES or FAIL;
- BLOCKING findings, NON-BLOCKING findings and notes, each with line references;
- a statement that the review is a cross-model review by Codex and is not a human or legal review.
