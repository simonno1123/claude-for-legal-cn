# TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_IMPLEMENTATION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Implementation Authorization Handoff

GOVERNANCE LAYER: Implementation Authorization Request

TARGET MODULE: `litigation-legal`

C01-II-B-2.2-A LIFECYCLE TARGET INVENTORY: AUTHORIZED (READ-ONLY)

C01-II-B-2.2-B LIFECYCLE SKILL MODIFICATION: NOT AUTHORIZED

CODE / SKILL / AGENT MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C01-II-B-2.2-A — Lifecycle Target Inventory and Scope Binding**.

The objective is to map the C01 Litigation Reasoning Lifecycle onto existing `litigation-legal` skills, perform a read-only inventory, check current file hashes, define boundaries, and present a minimal change whitelist proposal.

This phase is **read-only and documentation-only**. No actual editing of skill prompts, rewriting agent definitions, or modifying code is authorized.

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
C01-II-B-2.1 P1 Core Skill Modification (CLOSED / DONE)
        ↓
C01-II-B-2.2-A Lifecycle Target Inventory (This Task, Read-Only)
```

No file under `litigation-legal/` may be modified during this stage.

## 3. Fixed Baseline Inputs

Before execution, the executor must verify that the following baselines exist and match their designated hashes:

### 3.1 C01 Design Baseline v0.2
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`

### 3.2 C01-I Implementation Design Spec
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md`
- Required SHA-256: `9C123A93D2C348C53A48A7F8526A1913443EFA785FE1691174696102714E3553`

### 3.3 C01-II-A Skill Design Mapping
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`
- Required SHA-256: `8E52FB0F5DC13DD82B610E351653F11DA16178D6073621C0D773136DA9695870`

### 3.4 C01-II-B-1 Implementation Design
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md`
- Required SHA-256: `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E`

### 3.5 C01-II-B-2.1 Implementation Result
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_IMPLEMENTATION_RESULT.md`
- Required SHA-256: `B41815E98949EDFEB16C43818DF67D8885AC12770DBC841BE0310EE920EFA7A0`

### 3.6 C01-II-B-2.1 Result Record
- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_IMPLEMENTATION_RESULT_RECORD.md`
- Required SHA-256: `54A8925B9F0057758CF5028D7D273AEFF57EB8CAD9557ADED981C2DD89AE0E36`

## 4. P1 Core Post-change Baseline Binding

The executor must verify that the P1 Core modified files match their post-change hashes before beginning B-2.2-A. Any drift is a blocking condition.

- `claim-chart/references/element-templates.md`: `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D`
- `matter-intake/SKILL.md`: `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18`
- `chronology/SKILL.md`: `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2`
- `claim-chart/SKILL.md`: `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B`

## 5. B-2.2-A Authorized Scope

### Authorized
- Read C01-II-A Mapping, C01-II-B-1 Design, and the P1 Core post-change baselines;
- Audit existing `litigation-legal` Skills, Agent, and instructions;
- Identify gaps, redundancies, or overlaps in Lifecycle processing;
- Calculate and document pre-change SHA-256 for candidate lifecycle target files;
- Propose a minimal change target whitelist and divide files into MODIFY, NO CHANGE, or DEFER;
- Propose acceptance criteria for a potential subsequent B-2.2-B task.

### Not Authorized
- Modifying any Skill, Agent, or file under `litigation-legal/`;
- Modifying Plugin manifests, MCP configs, Workflows, or CLAUDE.md;
- Modifying Runtime validation schemas;
- Creating D1-D6;
- Modifying any evidence specialist Skills (P3 scope).

## 6. Lifecycle Design Boundaries (For Future Proposals)

1. **Analytical Control Only**: Lifecycle tracks candidate status, input/output gates, and review loops. It must not generate automated transitions, legal opinions, claim selections, or final legal strategies.
2. **Human Control Priority**: Any proposed pattern must enforce manual human review gates before candidate analytical output is applied.
3. **P3 Separation**: No evidence safeguards, custody tracking, or probative admissibility logic may be modified (reserved for B-2.3).
4. **Agent Integration Exclusions**: Agent changes are deferred and must not be proposed or applied during B-2.2.

## 7. Whitelist Selection Criteria

Target files proposed in B-2.2-A must:
1. Exist in the repository and belong to `litigation-legal`;
2. Already hold procedural or analysis lifecycle / briefing responsibilities;
3. Be upgradable solely via prompt instruction additions (no code/schema change);
4. Avoid duplication with P1 Core modified files, P3 Evidence files, or P4 Deferred files.

Each whitelist candidate must be structured in a table specifying path, current SHA-256, current role, gap, proposed instruction edit, overlap risk, and recommendation status.

## 8. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Lifecycle Target Inventory
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_TARGET_INVENTORY.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_TARGET_INVENTORY_RESULT.md`

## 9. Acceptance Criteria

- **AC-B22A-001 — Input Integrity**: All design baseline, mapping, design spec, and P1 post-change baseline hashes match exactly.
- **AC-B22A-002 — Read-only Boundary**: No files under `litigation-legal/` are altered.
- **AC-B22A-003 — Whitelist Completeness**: Whitelist entries include exact repository path, current hash, role, gap, proposed prompt block, and isolation risk.
- **AC-B22A-004 — Scope Separation**: No P3 Evidence, P4 Deferred, Agent, MCP, Workflow, or Runtime Schema edits are proposed.
- **AC-B22A-005 — Human Gate Preservation**: Design matrix enforces the manual review pattern.
- **AC-B22A-006 — Technical Validation**: `git diff --check` and Git status check confirm zero implementation modifications.
- **AC-B22A-007 — Execution Block**: No actual file modifications under B-2.2-B may begin without separate Project Owner approval.

## 10. Blocking Rules

Execution returns `BLOCKED` immediately if:
- Baseline or P1 hashes mismatch;
- In-progress user changes exist that would corrupt target path tracking;
- Lifecycle scope cannot be isolated from specialist evidence or agent rules without runtime schema edits.

## 11. Current State

```text
TASK_PHASE2_C01

C01-II-A: CLOSED / DONE
C01-II-B-1: CLOSED / DONE
C01-II-B-2.1 P1 Core: CLOSED / DONE
C01-II-B-2.2-A Handoff: APPROVED (This File)
C01-II-B-2.2-A Execution: PENDING CODEX
C01-II-B-2.2-B Modification: NOT AUTHORIZED
```
