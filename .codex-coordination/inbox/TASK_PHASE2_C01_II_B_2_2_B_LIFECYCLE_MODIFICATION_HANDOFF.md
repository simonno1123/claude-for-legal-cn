# TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

VERSION: v1.0

TYPE: Track C Implementation Authorization Handoff

GOVERNANCE LAYER: Implementation Authorization Request

TARGET MODULE: `litigation-legal`

TASK: C01-II-B-2.2-B Lifecycle Modification

IMPLEMENTATION: AUTHORIZED (3 WHITELISTED FILES ONLY)

C01-II-B-2.3 EVIDENCE SPECIALIST: NOT AUTHORIZED

C01-II-B-2.4 DEFERRED SURFACES: NOT AUTHORIZED

AGENT MODIFICATION: NOT AUTHORIZED

CODE / RUNTIME SCHEMA MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C01-II-B-2.2-B — Lifecycle Skill Modification**.

The objective is to enhance the three whitelisted lifecycle Skills in the `litigation-legal` module with the C01 Litigation Reasoning Lifecycle control model.

This is an **existing Skill prompt instruction enhancement** task. It does not create new Skills, new Agents, new database schemas, or automated workflow state machines.

## 2. Governance Position

```text
C01 Design Baseline
        ↓
C01-II-A Mapping
        ↓
C01-II-B-1 Implementation Design
        ↓
C01-II-B-2.2-A Lifecycle Inventory
        ↓
C01-II-B-2.2-B Lifecycle Modification (This Task, Whitelist Only)
```

No file other than the 3 whitelisted Skills may be modified during this stage.

## 3. Fixed Input Binding

Before execution, the executor must verify that the following baselines exist in the repository and match their designated hashes:

### 3.1 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

### 3.2 C01-II-B Handoff
- Path: `.codex-coordination/inbox/TASK_PHASE2_C01_II_B_IMPLEMENTATION_HANDOFF.md`
- Required SHA-256: `8989E7FCB9026B009F69BA2062C93FBD94337CEC7CB87FBF518E15671DADD623`

### 3.3 C01-II-B-1 Design
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md`
- Required SHA-256: `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E`

### 3.4 C01-II-B-2.2-A Inventory
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_TARGET_INVENTORY.md`
- Required SHA-256: `69936726A64D1A71912DEAA8E9E73CFBAA02077B41E4328F3A1777C324AA4BC5`

### 3.5 C01-II-B-2.2-A Inventory Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_TARGET_INVENTORY_RESULT.md`
- Required SHA-256: `8B46758F2596A3F3415805150A8FB7342CD8387E8D1235A01F4B829E558BDFED`

## 4. P1 Core Baseline Integrity Check

The executor must verify that the 4 previously modified P1 Core files match their post-change hashes exactly. Any modification or drift to P1 Core files is strictly prohibited.

- `claim-chart/references/element-templates.md`: `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D`
- `matter-intake/SKILL.md`: `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18`
- `chronology/SKILL.md`: `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2`
- `claim-chart/SKILL.md`: `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B`

## 5. Whitelisted Target File Inventory

The executor must verify that each target file matches its pre-change SHA-256 before modification. Any mismatch returns `BLOCKED`.

| Target File Path | Pre-change SHA-256 | B-1 Design Reference | Lifecycle Focus |
|---|---|---|---|
| `litigation-legal/skills/matter-update/SKILL.md` | `04FB6C9D3A930C17ACD50957E9FD66A2821FAF5B4FE6FF03012E17EB1F94A2C0` | Section 6.1 | Version mapping & re-review triggers |
| `litigation-legal/skills/matter-briefing/SKILL.md` | `6064D4BFB3AE41F88EDF0D94628131AF6CB8C16EB8EEDD7BC0928EF8212C68B6` | Section 6.2 | Candidate status & gaps presentation |
| `litigation-legal/skills/brief-section-drafter/SKILL.md` | `8FDC03E52A6BA4FF34DAE6890EDBA8A657EF2B455EDBC8C061FD4A0ACC664894` | Section 6.3 | Approved ref matching gate |

No file under `litigation-legal/` other than these three may be modified.

## 6. Modification Objectives

### 6.1 `matter-update`
- **Authorized**: Track current analytical stage, list pending items, identify blocking reasons, supply next actions, and display review status.
- **Prohibited**: Automated workflow state transitions, automatic case closures, or automatic item satisfaction.

### 6.2 `matter-briefing`
- **Authorized**: Summarize current Matter status, reference Issue/Claim/Element analysis, display proof/evidence gaps, and show review gates.
- **Prohibited**: Automated legal outcome prediction, automatic litigation strategy selection, or win-rate calculations.

### 6.3 `brief-section-drafter`
- **Authorized**: Generate draft sections based solely on reviewed inputs, preserve fact status markers, and flag/intercept unreviewed elements.
- **Prohibited**: Auto-generating non-existing facts, auto-satisfying elements, or upgrading candidate analysis to final facts.

## 7. Explicit Exclusions

- Global Legal Reasoning Core, `methodology/`, `legal-reasoning-core/`, or any parallel framework;
- Legal databases, case repositories, knowledge graphs, or experience databases;
- MCP modifications, provider integrations, or API expansions;
- Automated claim selection, litigation strategy generation, legal opinion generation, or adjudication prediction;
- D1-D6 generation or substitution;
- Runtime state machines or autonomous workflow transitions;
- Any modification to compatibility aliases, Agent (`docket-watcher.md`), `CLAUDE.md`, or the deprecated `customize` Skill.

## 8. Phase Separation

The execution must follow three stages:
1. **B-2.2-B-1**: Pre-change Snapshot Verification.
2. **B-2.2-B-2**: Whitelisted Skill Modification.
3. **B-2.2-B-3**: Validation (git validation and scope confirmation).

## 9. Authorized Outputs

Upon execution, Codex is authorized to create exactly **2 files**:

### Output A: Modification Result
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT.md`

### Output B: Result Record
- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT_RECORD.md`

## 10. Acceptance Criteria

- **AC-B22B-001**: Baseline integrity checks for all 5 baselines pass exactly.
- **AC-B22B-002**: Only the three whitelisted Skill files are modified.
- **AC-B22B-003**: Skill frontmatter structures remain unchanged.
- **AC-B22B-004**: No new Skills, Agents, databases, or runtime schemas are created.
- **AC-B22B-005**: Human Review boundary remains preserved.
- **AC-B22B-006**: Technical git diff checks pass and staging area remains empty after closeout.
