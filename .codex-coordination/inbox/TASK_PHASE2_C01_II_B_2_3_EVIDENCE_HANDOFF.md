# TASK_PHASE2_C01_II_B_2_3_EVIDENCE_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Implementation Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET MODULE: `litigation-legal`

C01-II-B-2.3-A EVIDENCE TARGET INVENTORY: AUTHORIZED (READ-ONLY)

C01-II-B-2.3-B EVIDENCE SKILL MODIFICATION: NOT AUTHORIZED

CODE / SKILL / AGENT MODIFICATION: NOT AUTHORIZED

## 1. Task Objective

This Handoff authorizes execution of **C01-II-B-2.3-A — Evidence Target Inventory and Scope Binding**.

The objective is to map the C01 Litigation Reasoning Evidence layer onto existing `litigation-legal` skills, perform a read-only inventory, check current file hashes, define boundaries, and present a minimal change whitelist proposal.

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
C01-II-B-1 Design Spec (CLOSED / ADOPTED)
        ↓
C01-II-B-2.1 P1 Core Skill Modification (CLOSED / DONE)
        ↓
C01-II-B-2.2 Lifecycle Modification (CLOSED / DONE)
        ↓
C01-II-B-2.3-A Evidence Target Inventory (This Task, Read-Only)
```

No file under `litigation-legal/` may be modified during this stage.

## 3. Fixed Baseline Inputs

Before execution, the executor must verify that the following baselines exist and match their designated hashes:

### 3.1 C01 Design and Mapping Baselines
- **C01 Design Baseline v0.2**: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
  - *Required SHA-256*: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`
- **C01-II-A Skill Design Mapping**: `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`
  - *Required SHA-256*: `8E52FB0F5DC13DD82B610E351653F11DA16178D6073621C0D773136DA9695870`
- **C01-II-B-1 Design Spec**: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md`
  - *Required SHA-256*: `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E`

### 3.2 C01-II-B-2.2-B Lifecycle Baselines
- **Lifecycle Modification Result (Output A)**: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT.md`
  - *Required SHA-256*: `48F44519B6DF039246E49DE0FFC9DB4BC824CAD5B5227A80D24BAC9DE166BA3D`
- **Result Record (Output B)**: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT_RECORD.md`
  - *Required SHA-256*: `E45C1EF28CFB2A9A80D2925618587122D2B917C92FC68E14E5110B3AFD78EFAB`

## 4. Prior Work Post-change Baseline Binding

The executor must verify that the previously modified Skill files match their post-change hashes exactly. Any modification or drift is a blocking condition.

### 4.1 P1 Core Skill Post-change Hashes
- `claim-chart/references/element-templates.md`: `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D`
- `matter-intake/SKILL.md`: `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18`
- `chronology/SKILL.md`: `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2`
- `claim-chart/SKILL.md`: `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B`

### 4.2 P2 Lifecycle Skill Post-change Hashes
- `matter-update/SKILL.md`: `DD4EED89B01DAC18CBB567C26EF089DEB6E0BB42CE15A5EA38AC0A82D8712E30`
- `matter-briefing/SKILL.md`: `967C982389BD61888986FAB83B74B42E8D67935C5AD0A380D287731D2EFF517E`
- `brief-section-drafter/SKILL.md`: `53CEFB16B6A0F5CFC6C95BCFB80F936BAE28B3CC283C1FC980883E595019B8A1`

## 5. B-2.3-A Scope and Whitelist Criteria

### Candidates for Inventory Analysis
1. `litigation-legal/skills/confidential-evidence-review/SKILL.md`
2. `litigation-legal/skills/evidence-preservation/SKILL.md`
3. `litigation-legal/skills/witness-trial-prep/SKILL.md`
4. `litigation-legal/skills/claim-chart/SKILL.md`

### Authorized
- Read design baselines and post-change Skill files;
- Identify gaps or redundancies in Evidence analytical tracking, confidentiality boundaries, preservation safeguards, and witness prep inputs;
- Document pre-change SHA-256 hashes for candidate evidence target files;
- Propose a minimal change target whitelist and divide files into MODIFY, NO CHANGE, or DEFER;
- Propose acceptance criteria for a potential subsequent B-2.3-B task.

### Not Authorized
- Modifying any Skill, Agent, or file under `litigation-legal/`;
- Modifying Plugin manifests, MCP configs, Workflows, or CLAUDE.md;
- Modifying Runtime validation schemas;
- Creating D1-D6;
- Proposing or creating new database tables or evidence repository files.

## 6. Evidence Design Boundaries (For Future Proposals)

1. **Analytical Mapping Only**: Evidence rules map authenticity, relevance, legality, and probative custody links. They must not calculate credibility scores, automate admissibility findings, or replace lawyer judgment.
2. **P4 Separation**: Agent (`docket-watcher.md`), CLAUDE.md, and workspace persistence layout decisions remain deferred and must not be proposed or applied during B-2.3.
3. **PRC Law Integration**: Proposed evidence rules must align with PRC evidence guidelines (statutory primacy, authentic-carrier preservation, personal information redaction).

## 7. Whitelist Selection Criteria

Target files proposed in B-2.3-A must:
1. Exist in the repository and belong to `litigation-legal`;
2. Already hold evidence-related analytical, preservation, or confidentiality responsibilities;
3. Be upgradable solely via prompt instruction additions (no code/schema change);
4. Avoid duplication with previously modified files unless strictly necessary and documented.

Each whitelist candidate must specify path, current SHA-256, current role, gap, proposed instruction edit, overlap risk, and recommendation status.

## 8. Authorized Outputs

The executor is authorized to create exactly **2 files**:

### Output A: Evidence Target Inventory
- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_3_A_EVIDENCE_TARGET_INVENTORY.md`

### Output B: Execution Result
- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_3_A_EVIDENCE_TARGET_INVENTORY_RESULT.md`

## 9. Acceptance Criteria

- **AC-B23A-001 — Input Integrity**: All design baseline, mapping, design spec, lifecycle modification result, and prior post-change baseline hashes match exactly.
- **AC-B23A-002 — Read-only Boundary**: No files under `litigation-legal/` are altered.
- **AC-B23A-003 — Whitelist Completeness**: Whitelist entries include exact repository path, current hash, role, gap, proposed prompt block, and isolation risk.
- **AC-B23A-004 — Scope Separation**: No Agent, MCP, Workflow, or Runtime Schema edits are proposed.
- **AC-B23A-005 — Human Gate Preservation**: Design matrix enforces the manual review pattern.
- **AC-B23A-006 — Technical Validation**: `git diff --check` and Git status check confirm zero implementation modifications.
- **AC-B23A-007 — Execution Block**: No actual file modifications under B-2.3-B may begin without separate Project Owner approval.

## 10. Blocking Rules

Execution returns `BLOCKED` immediately if:
- Baseline or post-change hashes mismatch;
- In-progress user changes exist that would corrupt target path tracking;
- Evidence scope cannot be isolated from workspace persistence boundaries without runtime schema edits.

## 11. Current State

```text
TASK_PHASE2_C01

C01-II-A: CLOSED / DONE
C01-II-B-1: CLOSED / DONE
C01-II-B-2.1 P1 Core: CLOSED / DONE
C01-II-B-2.2 Lifecycle: CLOSED / DONE
C01-II-B-2.3-A Handoff: APPROVED (This File)
C01-II-B-2.3-A Execution: PENDING CODEX
C01-II-B-2.3-B Modification: NOT AUTHORIZED
```
