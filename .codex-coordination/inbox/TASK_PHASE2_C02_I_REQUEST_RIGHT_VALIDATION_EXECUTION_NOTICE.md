# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION_NOTICE

STATUS: **EXECUTION NOTICE ISSUED — PENDING CODEX EXECUTOR START**

TYPE: Track C Validation Execution Notice

FROM: Architecture Coordinator

TO: Codex Executor

TASK: `TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION`

## 1. Authorization Basis

### Final Execution Handoff

- Path: `.codex-coordination/inbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_FINAL_EXECUTION_HANDOFF.md`
- SHA-256: `F4E830148FFF96F105DE8030D5120CCD542CD55D637CFAE6AA772FAFB3E23564`

### Architecture Review

- Path: `.codex-coordination/reviews/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_FINAL_EXECUTION_HANDOFF_REVIEW.md`
- SHA-256: `FF71AC25C4FC4CB4E07FA13A29B38230D642D685D7F38DF2FCFB93F25311A5A8`
- Result: `PASS`

### Project Owner Decision

- Path: `.codex-coordination/decisions/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_FINAL_EXECUTION_HANDOFF_DECISION.md`
- SHA-256: `63BD152F430901927CD7F811EB7E157378723BED99AFB4B78EFD05063256C2A4`
- Decision: `ACCEPTED`

The obsolete draft SHA `381B0AE3EB954ACF53C7D8E6559E155E3EDBEBE97A123EB31B651A2DAA7E1768` is not an execution authorization source.

## 2. Execution Authorization

Codex Executor is authorized, in a subsequent execution step, to start:

`TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_EXECUTION`

Execution mode: **READ-ONLY VALIDATION**.

The executor may:

- Verify all inputs bound by the Final Execution Handoff;
- Read only case materials within the approved manifest paths and access scope;
- Separate facts from candidate legal facts;
- Identify candidate request rights without reaching final legal conclusions;
- Decompose constituent elements;
- Map candidate burden-of-proof positions and evidence requirements;
- Record conflicts, missing facts, inaccessible materials, and evidence gaps;
- Preserve qualified-lawyer review as the final decision authority.

## 3. Authorized Outputs

Execution may create or update exactly two files:

1. `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md`
2. `.codex-coordination/outbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_RESULT.md`

No `TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_REPORT.md` output is authorized.

## 4. Restrictions

- No Skill modification;
- No Agent modification;
- No code modification;
- No architecture expansion;
- No plugin, MCP, workflow, runtime-schema, database, or system-configuration modification;
- No modification under `litigation-legal/`;
- No automatic legal conclusion or adjudication;
- No merits prediction or win-rate estimate;
- No inferred, reconstructed, or fabricated case facts;
- No C02-II or later implementation work;
- No Git staging, commit, tag, push, or release.

## 5. Materialization Boundary

This materialization step creates this Execution Notice only. It does not read case-file contents and does not create either authorized validation output.

Codex Executor must return this Notice's physical SHA-256 and Git validation status before beginning the separate validation execution step.

## 6. Governance Transition

```text
Final Execution Handoff
        ↓
Architecture Review PASS
        ↓
Project Owner Decision ACCEPTED
        ↓
Execution Notice ISSUED
        ↓
Codex Executor START PENDING
```
