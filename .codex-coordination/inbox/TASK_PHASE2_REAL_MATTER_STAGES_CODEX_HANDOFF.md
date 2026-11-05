# Codex Task

## 1. Task ID

TASK_PHASE2_REAL_MATTER_STAGES_CODEX_HANDOFF

## 2. Status

READY — SCOPE HANDOFF (each stage still needs its own owner authorization before execution)

## 3. Background

Project Owner decision (2026-11-05, recorded by Claude as recorder only): every stage of claude-for-legal-cn that needs **real case material** is handed to Codex, because the Codex environment holds a large body of real cases that can be used. Claude sessions continue to handle work that needs no real case material (synthetic validation, design, review, plugin content).

State at handoff:
- C03 Tier A (platform) blockers AR-B-007, AR-B-008 and AR-B-009 are CLOSED (AR-B-008 with limitations): `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_TIER_A_CLOSURE_DECISION.json`. 3 of 10 C03 blockers are closed; C03 is NOT active and downstream stays BLOCKED.
- Route A input readiness: CASE-A PARTIAL / LEGAL REASONING BLOCKED; CASE-B BLOCKED; CASE-C BLOCKED (`docs/phase2/route-a/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC.md`).

## 4. Stages handed to Codex

| Stage | Blocker / item | Governing document |
|---|---|---|
| Route A real-matter input and evidence | CASE-A/B/C readiness; physical evidence acquisition; action-manifest confirmations | `docs/phase2/route-a/` |
| C03 matter-bound blockers | AR-B-002 Route A readiness; AR-B-003 matter and actor identity; AR-B-004 evidence readiness and provenance; AR-B-005 qualified-human review gate (matter packet); AR-B-006 China-law authority freshness | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN.md` §7.2–7.6 |
| C03 per-output authority | AR-B-010 downstream candidate authority | same plan §7.10 |
| C03 activation | AR-B-001 activation authorization (final positive authority; after the above and a new readiness review) | same plan §7.1 |
| Integration-stage items handed over by the AR-B-008 closure | runtime timers, signal propagation, persistence, real dependencies, project/session/provider isolation, wiring the remaining evaluators at their transitions | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_AR_B_008_CLOSURE_EVIDENCE_PACKET_REV2.md` §二, §五 |

The Final Readiness Review authorization request (C03-TA-D-017) can be prepared by either side; it needs a separate owner decision.

## 5. Hard constraints

1. **This repository is PUBLIC on GitHub.** No real case material may be committed, pushed, quoted or attached to any issue or pull request. This covers party names, ID numbers, case numbers, addresses, amounts tied to a real matter, document images, OCR text and file hashes that would identify a real document. Keep real material in Codex's private store only. Commit to this repository only redacted, synthetic or aggregate results, plus records that point to private evidence by an opaque reference.
2. Each stage starts only after a separate Project Owner authorization naming that stage. This handoff authorizes no execution.
3. The accepted C03 implementation is bound at the SHAs in the Tier A closure decision. Any change to `scripts/phase2_runtime/route_b_c03/**` reopens AR-B-007/008/009 under their withdrawal conditions and must be routed back for review.
4. Human confirmation gates in `CHINA_LOCALIZATION_STATUS.md` (sending opinions, filing, signing, data transfer and similar) are unchanged. No legal-consequence action is executed.
5. Results go to `.codex-coordination/outbox/` as `*_RESULT.md`, with input SHA verification as in earlier results.

## 6. Forbidden Actions

1. Do not commit or push real case material (see 5.1).
2. Do not activate C03 or lift any downstream block.
3. Do not modify the accepted C03 subject files without a routed review.
4. Do not treat this handoff as authorization to execute any stage.
