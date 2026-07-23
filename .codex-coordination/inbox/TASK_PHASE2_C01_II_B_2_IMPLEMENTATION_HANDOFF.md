# TASK_PHASE2_C01_II_B_2_IMPLEMENTATION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Implementation Authorization Handoff

GOVERNANCE LAYER: Implementation Authorization Request

TARGET MODULE: `litigation-legal`

C01-II-B-2.1 CORE SKILL MODIFICATION: AUTHORIZED (P1 ONLY)

C01-II-B-2.2 LIFECYCLE / CONSUMER MODIFICATION: NOT AUTHORIZED

C01-II-B-2.3 EVIDENCE SPECIALIST MODIFICATION: NOT AUTHORIZED

C01-II-B-2.4 DEFERRED SURFACES: NOT AUTHORIZED

AGENT MODIFICATION: NOT AUTHORIZED

PLUGIN / MCP / RUNTIME SCHEMA MODIFICATION: NOT AUTHORIZED

## 1. Task Objective

This Handoff authorizes execution of **C01-II-B-2.1 — Core Skill Modification
(P1 Package Only)**.

The objective is to apply the diff-level text proposals from the adopted
C01-II-B-1 Implementation Design (Sections 5.1–5.4) to the four P1 Core files,
enhancing existing `litigation-legal` Skill instructions with C01 Litigation
Reasoning Framework concepts.

This is an **existing Skill enhancement** task. It does not create new
architecture, new Skills, new Agents, or new methodology layers.

## 2. Governance Position

```text
Phase 2 Track C
        ↓
C01 Design Baseline (APPROVED)
        ↓
C01-I Engineering Design (CLOSED)
        ↓
C01-II-A Skill Design Mapping (CLOSED / ADOPTED)
        ↓
C01-II-B-1 Implementation Design (CLOSED / ADOPTED)
        ↓
C01-II-B-2.1 Core Skill Modification — P1 (This Task)
```

## 3. Fixed Baseline Inputs

Before execution, the executor must verify that the following baselines exist
and match their designated hashes. Any mismatch returns BLOCKED.

### 3.1 C01 Design Baseline v0.2

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5`

### 3.2 C01-II-A Skill Design Mapping

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`
- Required SHA-256: `ACBCCB077EB3EE7193C0AC031C23950FC9EF31FE43A44A3D5EB07ABC96474115`

### 3.3 C01-II-B-1 Implementation Design

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md`
- Required SHA-256: `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E`

## 4. Authorization Scope

### Authorized: C01-II-B-2.1 (P1 Core Only)

This Handoff authorizes modification of exactly **4 files** listed in Section 5.
Permitted operations:

- Enhance existing Skill instructions with C01 analysis path guidance;
- Add candidate Request Right / Element / Proof / Legal Fact mapping prompts;
- Add governance metadata and non-authoritative safeguards to element templates;
- Add Human Review reminders and candidate status preservation requirements;
- Preserve all existing functionality and instruction semantics.

### Not Authorized

- Creating new Skills, Agents, directories, or methodology frameworks;
- Deleting or renaming any existing file;
- Modifying any file not listed in Section 5;
- Modifying Plugin manifests, `.mcp.json`, Marketplace metadata;
- Modifying Runtime Schemas, Workflows, or source code;
- Modifying `litigation-legal/CLAUDE.md` or `agents/docket-watcher.md`;
- P2 Lifecycle/Consumer modifications (requires B-2.2 authorization);
- P3 Evidence Specialist modifications (requires B-2.3 authorization);
- P4 Deferred surface modifications (requires separate decisions).

## 5. Exact Target File Inventory (P1 Core)

The executor must verify that each target file matches its pre-change SHA-256
before applying any modification. Mismatch on any file returns BLOCKED for that
file.

| Seq | Target File Path | Pre-change SHA-256 | Bytes | B-1 Design Reference |
|---:|---|---|---:|---|
| 1 | `litigation-legal/skills/claim-chart/references/element-templates.md` | `1EFD953B217290A4310084518CEE06E008631F303F65845677DD9A65EF56E6EA` | 2,918 | Section 5.4 |
| 2 | `litigation-legal/skills/matter-intake/SKILL.md` | `F0FCBBBE233BDFA0D846A3DE78D17FE3C8DD03189B2745DAE3FE235EC70E0C00` | 2,960 | Section 5.1 |
| 3 | `litigation-legal/skills/chronology/SKILL.md` | `927E7E08BBBE2B8ED97595CDBFEA4742E4C6B9D8DC9EFD41D9CE334D433702F2` | 1,489 | Section 5.2 |
| 4 | `litigation-legal/skills/claim-chart/SKILL.md` | `1B130FD98A1E46A3D928ADDC905A37B59B998F0B2EE9E86B81AE07193CFE4DCC` | 1,852 | Section 5.3 |

Modification order follows B-1 Design Section 4.2 dependency sequence:
element-templates → matter-intake → chronology → claim-chart.

No file outside this table may be modified.

## 6. Modification Principles

1. **Additive enhancement only.** Extend existing instructions; do not delete or
   replace current functionality.
2. **Diff traceability.** Every modification must trace to a specific diff block
   in B-1 Design Sections 5.1–5.4.
3. **Candidate semantics.** All AI-generated analysis must be marked as
   candidate output requiring qualified human review.
4. **Provenance preservation.** Facts, authorities, evidence, and legal
   propositions must retain source, freshness, jurisdiction, adverse-material,
   and uncertainty signals.
5. **China-law compliance.** Preserve current-law checking, authority hierarchy,
   territorial and temporal applicability, and qualified-lawyer control
   appropriate to PRC legal work.
6. **No silent automation.** No modification may enable automatic claim
   selection, element satisfaction, evidentiary admissibility findings, filing
   decisions, legal opinions, or judicial-outcome predictions.

## 7. Human Review Boundary

All modifications must preserve the governance control pattern:

```text
Candidate Analysis (AI generated)
        ↓
Qualified Human Review (manual gate)
        ↓
Approval Decision (lawyer confirmed)
        ↓
Optional Application (downstream use)
```

This pattern is a governance guideline. It must not be implemented as a runtime
state machine, D6 substitute, or autonomous workflow transition.

## 8. Explicit Exclusions

This Handoff prohibits:

- Global Legal Reasoning Core, `methodology/`, `legal-reasoning-core/`, or any
  parallel framework;
- Legal databases, case repositories, knowledge graphs, or experience databases;
- MCP modifications, provider integrations, or API expansions;
- Automated claim selection, litigation strategy generation, legal opinion
  generation, or adjudication prediction;
- D1-D6 generation or substitution;
- Runtime state machines or autonomous workflow transitions;
- Any modification to compatibility aliases or the deprecated `customize` Skill.

## 9. Authorized Outputs

Upon execution, Codex must produce exactly **2 governance files** in addition to
the 4 modified P1 files:

### Output A: Implementation Result

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_IMPLEMENTATION_RESULT.md`
- Required content:
  - Baseline verification results;
  - For each modified file: before SHA-256, after SHA-256, modification summary;
  - Diff traceability to B-1 Design sections;
  - Human Review boundary confirmation;
  - Exclusion compliance.

### Output B: Execution Result Record

- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_IMPLEMENTATION_RESULT_RECORD.md`
- Required content:
  - Handoff hash binding;
  - Result hash binding;
  - Git validation (`git diff --check`, staging status);
  - Scope compliance confirmation;
  - AC verification matrix.

## 10. Rollback Plan

If any modification fails validation:

1. Restore the affected file to its pre-change SHA-256 bytes from Section 5.
2. Verify restoration hash matches the pre-change value.
3. Do not use `git reset --hard`, broad checkout, or deletion operations.
4. Record the rollback reason, affected file, and residual risk in the Result.
5. A partial rollback (restoring only failed files) is permitted if independent
   files pass validation individually.

## 11. Acceptance Criteria

### AC-B2-001 — Baseline Integrity
Recomputes and verifies the SHA-256 of all three design baselines (Section 3).
Mismatch returns BLOCKED.

### AC-B2-002 — Pre-change Hash Match
Verifies each P1 target file matches its pre-change SHA-256 (Section 5) before
modification. Mismatch on any file blocks that file's modification.

### AC-B2-003 — Scope Compliance
Confirms that only the 4 files in Section 5 are modified. No other file under
`litigation-legal/` or elsewhere is created, modified, or deleted.

### AC-B2-004 — Diff Traceability
Every modification traces to a specific diff block in B-1 Design Sections
5.1–5.4. No out-of-scope enhancement appears.

### AC-B2-005 — Human Review Preservation
No automatic legal opinion, claim selection, element satisfaction, admissibility
finding, or outcome prediction is introduced.

### AC-B2-006 — Architecture Boundary
No new Skill, Agent, methodology directory, database, MCP config, Plugin
manifest, or Runtime Schema is created.

### AC-B2-007 — Technical Integrity
`git diff --check` returns PASS. Only the 4 P1 files and 2 governance outputs
appear in the working tree changes.

## 12. Current State

```text
Phase 2 Track C — TASK_PHASE2_C01

C01 Design Baseline: APPROVED
C01-I: CLOSED
C01-II-A: CLOSED (Adopted)
C01-II-B-1 Implementation Design: CLOSED (Adopted)
C01-II-B-2 Handoff: APPROVED (This File)
C01-II-B-2.1 Core Skill Modification: AUTHORIZED — PENDING EXECUTION
C01-II-B-2.2 Lifecycle / Consumer: NOT AUTHORIZED
C01-II-B-2.3 Evidence Specialist: NOT AUTHORIZED
C01-II-B-2.4 Deferred: NOT AUTHORIZED
```

## 13. Next Action

With this Handoff approved, Codex is authorized to execute C01-II-B-2.1 by
modifying the 4 P1 Core files in the dependency order specified in Section 5.
Upon completion, Architecture Coordinator reviews the result before Project
Owner final decision.
