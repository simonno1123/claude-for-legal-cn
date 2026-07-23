# TASK_PHASE2_C01_II_B_IMPLEMENTATION_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Implementation Authorization Request

GOVERNANCE LAYER: Handoff / Authorization Request

TARGET MODULE: `litigation-legal`

C01-II-B-1 IMPLEMENTATION DESIGN: AUTHORIZED

C01-II-B-2 SKILL / AGENT MODIFICATION: NOT AUTHORIZED

C01-II-B-3 VALIDATION EXECUTION: NOT AUTHORIZED

CODE MODIFICATION: NOT AUTHORIZED

## 1. Task Purpose

This Handoff authorizes execution of **C01-II-B-1 — Implementation Design**.

The objective is to translate the adopted C01-II-A Skill Design Mapping into
concrete modification specifications for existing `litigation-legal` assets.

This phase produces:

- Modification scope design;
- Skill/Agent adjustment proposals (diff-level text specifications);
- Risk assessment;
- Rollback plan;
- Validation plan.

This phase does not modify any file under `litigation-legal/`.

## 2. Governance Position

```text
Phase 2 Track C
        ↓
TASK_PHASE2_C01
        ↓
C01 Design Baseline (APPROVED)
        ↓
C01-I Engineering Design (CLOSED)
        ↓
C01-II-A Skill Design Mapping (CLOSED / ADOPTED)
        ↓
C01-II-B-1 Implementation Design (This Task)
```

C01-II-B-1 does not alter the above architecture chain.

## 3. Fixed Input Binding

Before execution, the executor must verify that the following baselines exist
and match their designated hashes:

### 3.1 C01 Design Baseline v0.2

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
- Required SHA-256: `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5`

### 3.2 C01-I Implementation Design Specification

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md`
- Required SHA-256: `0274AB2C7542083BFBDFF98F00E7143F7D45927EEEED5675BF28BF6631A862C7`

### 3.3 C01-II-A Skill Design Mapping

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`
- Required SHA-256: `ACBCCB077EB3EE7193C0AC031C23950FC9EF31FE43A44A3D5EB07ABC96474115`

### 3.4 Governance Decisions

- Phase 2 Scope Decision: `DECISION_PHASE2_SCOPE_RECLASSIFICATION` (ACCEPTED)
- Phase 2 Architecture Acceptance: `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md` (ACCEPTED)
- C01-II-A Mapping Decision: `.codex-coordination/decisions/TASK_PHASE2_C01_II_A_MAPPING_DECISION.md` (ACCEPTED)

## 4. Current Authorization

### Authorized

C01-II-B-1 Implementation Design only. This permits:

- Evaluating which Skills require modification and the minimum necessary scope;
- Producing an ordered file modification list with exact paths;
- Designing Prompt/Instruction adjustment proposals as diff-level text blocks;
- Designing Agent contract adjustment proposals;
- Producing a test/validation plan for the subsequent C01-II-B-3 phase;
- Producing a rollback plan.

### Not Authorized

The following remain strictly prohibited:

- C01-II-B-2 Skill / Agent Modification (actual file editing);
- C01-II-B-3 Validation Execution;
- Modifying any file under `litigation-legal/`;
- Modifying any Plugin, Marketplace, MCP, Workflow, or Runtime file.

## 5. Modification Boundary

### Minimum Change Surface Principle

The executor must not propose wholesale rewriting of `litigation-legal`. The
design must follow:

```text
C01-II-A Mapping (adopted baseline)
        ↓
Identify Minimal Required Assets
        ↓
Design Change Proposal (diff-level)
```

Only assets identified in C01-II-A Section 7.1 (Candidate C01-II-B Change
Points) are eligible for modification design. Assets not listed there must not
appear in the modification proposal.

## 6. Candidate Modification Areas

Based on C01-II-A Mapping Section 3.2 and Section 7.1:

### Matter Layer

- `matter-workspace/SKILL.md` — Matter identity and analysis reference
- `matter-intake/SKILL.md` — Issue/Question/Claim initialization

### Claim Analysis Layer

- `claim-chart/SKILL.md` — Central analytical mapping (Claim, Request Right,
  Element, Proof, Evidence, Defense/Rebuttal)
- `claim-chart/references/element-templates.md` — Governance/freshness metadata

### Fact Layer

- `chronology/SKILL.md` — Legal Fact candidate references and provenance

### Lifecycle and Consumer Layer

- `matter-update/SKILL.md` — Reopen/invalidation notice
- `matter-briefing/SKILL.md` — Candidate/review/adverse/gap status
- `brief-section-drafter/SKILL.md` — Approved analysis references
- `witness-trial-prep/SKILL.md` — Reviewed Proof/Evidence references

### Evidence Specialist Layer

- Evidence-related canonical Skills — Reviewed Evidence references and gaps

### Agent Layer

- `agents/docket-watcher.md` — Procedural candidate references (requires
  separate Agent authorization)

### System-Level

- `litigation-legal/CLAUDE.md` — Distributed gates alignment (requires broad
  system-behavior review)

These are design candidates only. They are not authorized modification targets.

## 7. Explicit Exclusions

This Handoff prohibits:

- Creating `methodology/`, `legal-reasoning-core/`, or any parallel framework
  directory;
- Creating legal databases, case repositories, experience databases, or
  knowledge graphs;
- MCP modifications, provider integrations, or API expansions;
- Automated claim selection, litigation strategy generation, legal opinion
  generation, or adjudication prediction;
- D1-D6 generation or substitution;
- Global Legal Reasoning Core of any form.

## 8. C01-II-B-1 Authorized Outputs

Upon approval, Codex is authorized to generate exactly **2 files**:

### Output A: Implementation Design Spec

- Path: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md`
- Required content:
  - Baseline verification results;
  - Target asset analysis with exact file paths;
  - Proposed modifications as diff-level text blocks;
  - Risk assessment;
  - Rollback plan;
  - Validation plan for future C01-II-B-3.

### Output B: Execution Result

- Path: `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN_RESULT.md`
- Required content:
  - Input hash verification;
  - Scope verification;
  - Git validation (`git diff --check`, empty staging);
  - Zero-modification confirmation;
  - Authorization boundary check results.

## 9. Acceptance Criteria

### AC-C01-II-B-001 — Fixed Inputs Bound

Recomputes and verifies the exact SHA-256 of C01 v0.2 Design Baseline, C01-I
Spec, and C01-II-A Mapping. Mismatches return BLOCKED.

### AC-C01-II-B-002 — Design Only Output

Confirms that only design documentation is produced. No implementation code,
skill prompt edits, or agent modifications exist in the output.

### AC-C01-II-B-003 — Mapping-Based Scope

All proposed modifications trace to C01-II-A Mapping Section 7.1 candidate
change points. No out-of-scope assets appear.

### AC-C01-II-B-004 — No New Methodology Architecture

No parallel methodology framework, global reasoning core, or legal-reasoning
directory is proposed or created.

### AC-C01-II-B-005 — No Database or External Capability

No legal databases, knowledge graphs, MCP extensions, or automated adjudication
capabilities are proposed.

### AC-C01-II-B-006 — Human Review Preserved

The Human Review Control Pattern (Candidate → Qualified Review → Approval →
Optional Application) is preserved in all proposed modifications.

### AC-C01-II-B-007 — Technical Validation Compliance

Requires `git diff --check` PASS and empty Git staging area prior to closeout.

## 10. Result Binding Requirements

The output Result file must bind:

- The SHA-256 hash of this Handoff document;
- The SHA-256 hash of the generated Implementation Design Spec;
- Explicit verification confirming:
  - Zero Skill Modifications;
  - Zero Agent Modifications;
  - Zero Workflow Modifications;
  - Zero Schema/MCP Modifications;
  - Zero Implementation Code Output.

## 11. Current State

```text
Phase 2 Track C — TASK_PHASE2_C01

Design Baseline: APPROVED (v0.2 Baseline Adopted)
C01-I: APPROVED AND CLOSED
C01-II-A: CLOSED / DONE (Adopted)
C01-II-B Handoff: APPROVED (This File)
C01-II-B-1 Implementation Design: AUTHORIZED — PENDING EXECUTION
C01-II-B-2 Skill / Agent Modification: NOT AUTHORIZED
C01-II-B-3 Validation Execution: NOT AUTHORIZED
Code Modification: NOT AUTHORIZED
```

## 12. Next Action

With this Handoff approved, Codex is authorized to execute Phase C01-II-B-1 and
produce the two output documents specified in Section 8. No implementation
changes, skill modifications, or code edits may proceed.
