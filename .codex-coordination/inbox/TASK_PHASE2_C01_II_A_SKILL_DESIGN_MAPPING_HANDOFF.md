# TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_HANDOFF

STATUS: **DRAFT v0.2 — PENDING PROJECT OWNER REVIEW**

TYPE: Track C Implementation Design Handoff

GOVERNANCE LAYER: Task Design / Authorization

TARGET MODULE: `litigation-legal`

C01-II-A PLANNING EXECUTION: READY FOR AUTHORIZATION

C01-II-B IMPLEMENTATION EXECUTION: NOT AUTHORIZED

CODE / SKILL / AGENT MODIFICATION: NOT AUTHORIZED

## 1. Task Objective

This Handoff Task governs the execution of **Phase C01-II-A — Skill Design Mapping**.

The objective is to analyze the structural mapping between the approved C01 Litigation Reasoning Framework and the existing `litigation-legal` Skill/Agent architecture, producing a detailed engineering mapping spec.

This is a **documentation-only planning task**. No runtime changes, prompt modifications, executable schemas, or code updates are authorized.

## 2. Dependency Verification (Fixed Baselines)

Before executing C01-II-A, the executor must verify that the following canonical baselines exist in the repository and match their designated hashes:

### 2.1 Governance Architecture Decisions
- **Phase 2 Scope Decision**: `DECISION_PHASE2_SCOPE_RECLASSIFICATION`
  - *Required State*: `ACCEPTED` (recorded in `.codex-coordination/decisions/`)
- **Phase 2 Architecture Acceptance Retry-1**: `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md`
  - *Required State*: `ACCEPTED`

### 2.2 Design Baselines
- **C01 Design Baseline v0.2**: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
  - *Required SHA-256*: `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5`

### 2.3 Phase C01-I Specification and Decisions
- **C01-I Implementation Spec**: `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md`
  - *Required SHA-256*: `0274AB2C7542083BFBDFF98F00E7143F7D45927EEEED5675BF28BF6631A862C7`
- **C01-I Specification Review**: `.codex-coordination/reviews/TASK_PHASE2_C01_I_SPEC_REVIEW.md`
  - *Required State*: `ACCEPTED`
- **C01-I Spec Decision**: `.codex-coordination/decisions/TASK_PHASE2_C01_I_SPEC_DECISION.md`
  - *Required State*: `ACCEPTED`

## 3. Task Position

```text
Existing litigation-legal Plugin
        ↓
Existing Skill Architecture (24 total assets)
        ↓
C01-II-A Mapping Analysis (This Task)
        ↓
Future C01-II-B Implementation Proposal (Blocked)
```

### Strict Prohibitions:
Execution of C01-II-A is strictly prohibited from modifying:
- Plugin descriptors, manifests, or `.mcp.json` configs.
- Any skill code, instructions, or prompts under `litigation-legal/skills/`.
- Any agent instructions under `litigation-legal/agents/`.
- Runtime validation schemas, database layers, or CLI scripts.
- Working matter workspaces or history logs.

## 4. Analysis Scope

The analysis must perform a detailed, read-only mapping of the C01 Reasoning Model onto the existing `litigation-legal` codebase:

### 4.1 Skill Inventory Scope
Inspect all **24 assets** within the `litigation-legal` plugin:
- **18 Canonical Skills**: `brief-section-drafter`, `chronology`, `claim-chart`, `cold-start-interview`, `confidential-evidence-review`, `court-order-triage`, `demand-draft`, `demand-intake`, `demand-received`, `evidence-preservation`, `matter-briefing`, `matter-close`, `matter-intake`, `matter-update`, `matter-workspace`, `oc-status`, `portfolio-status`, `witness-trial-prep`.
- **4 Compatibility Aliases**: `deposition-prep`, `legal-hold`, `privilege-log-review`, `subpoena-triage`.
- **1 Deprecated Skill**: `customize`.
- **1 Agent**: `docket-watcher.md`.

For each asset, the analysis must determine its coverage relative to C01 concepts (Matter, Issue, Claim, Element, Fact, Proof, Evidence, Defense/Rebuttal, Human Review).

### 4.2 Compatibility and Deprecation Handling
The specification must explicitly define:
- How compatibility aliases will route to canonical skills without acquiring independent C01 ownership.
- Whether the deprecated skill requires compatibility mappings or is scheduled for deprecation.
- **Rule**: Deleting, renaming, or modifying any alias or deprecated file is strictly prohibited during this task.

### 4.3 C01 Capability Mapping
Map C01 capabilities onto target Skills/Agents:
- **Request Right Analysis**: Mapped across `Matter`, `Issue`, `Claim`, and `Element` concepts.
- **Proof Analysis**: Mapped across `Element`, `Fact`, `Burden`, and `Evidence` concepts.
- **Defense Analysis**: Mapped across `Claim`, `Defense`, and `Rebuttal` concepts.

## 5. Required Output Documents

Execution of C01-II-A is authorized to create exactly **2 files** in the specified paths. No additional files may be generated:

### Output A: Design Artifact
- **Path**: `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`
- **Purpose**: Defines the skill architecture mapping (M01), capability boundary matrix (M02), input/output contract draft (M03), human review integration mapping (M04), and implementation boundary report (M05).

### Output B: Execution Result
- **Path**: `.codex-coordination/outbox/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_RESULT.md`
- **Purpose**: Documents dependency verification hashes, AC status, Git status checks, and validation results.

## 6. Human Review Control Pattern

The specification must model human control according to the following pattern:

```text
Candidate Analysis (AI generated)
        ↓
Qualified Human Review (Manual gate)
        ↓
Approval Decision (Lawyer confirmed)
        ↓
Optional Application (Downstream use)
```

This pattern is a **governance control guideline** for design and contracts. It must not be described as an implemented runtime state machine, as D6 remains ungenerated and unauthorized.

## 7. Output Contract

Execution of this task must conform strictly to the following path limits:

- **Allowed Paths**:
  - `docs/phase2/track-c/` (only for Output A)
  - `.codex-coordination/outbox/` (only for Output B)
- **Forbidden Paths**:
  - `litigation-legal/` (no code, prompt, or local workspace change)
  - `skills/` or `agents/` (no editing skill/agent instructions)
  - `plugins/` or `mcp/` (no plugin manifest or MCP config editing)
  - `runtime/` (no runtime validation schemas)

## 8. Technical and Git Validation

Before returning a final Result, the executor must perform the following validation checks:

### 8.1 Git Status Check
Verify that no codebase or runtime files have been staged or modified:
- `git status` output shows no modifications under `litigation-legal/`.
- Staging area must be completely empty of staged changes (`No staged changes`).
- Pre-existing untracked/ignored governance files in `.codex-coordination` are preserved and remain unmodified.

### 8.2 Technical Linting
Execute the following verification:
```bash
git diff --check
```
Record the result as `PASS` or `FAIL` in the outbox Result file.

## 9. Explicit Exclusions

The following features remain strictly **NOT AUTHORIZED**:
- Creating, editing, or generating D1-D6 specifications.
- Creating a Global Legal Reasoning Core, `legal-reasoning-core/` directory, or parallel methodology frameworks.
- MCP modifications, connector expansion, or external API provider integrations.
- Automated legal opinions, automated litigation strategy engines, or automatic claim selection.

## 10. Result Binding Requirements

The output Result file `.codex-coordination/outbox/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_RESULT.md` must programmatically bind:
- The SHA-256 hash of this `TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_HANDOFF_v0.2` document.
- The SHA-256 hash of the generated Design Specification `TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md`.
- Explicit verification results confirming:
  - `Zero Skill Modifications`
  - `Zero Agent Modifications`
  - `Zero Workflow Modifications`
  - `Zero Schema/MCP Modifications`
  - `Zero Implementation Code Output`

## 11. Handoff Acceptance Criteria

### AC-C01-II-A-001 — Fixed Inputs Bound
Recomputes and verifies the exact SHA-256 of C01 v0.2, C01-I Spec, and coordinate reviews/decisions. Mismatches return BLOCKED.

### AC-C01-II-A-002 — Phase Separation
Explicitly limits C01-II-A to documentation-only planning and marks C01-II-B/C as NOT AUTHORIZED.

### AC-C01-II-A-003 — Asset Inventory Completeness
Enforces full inventory analysis of all 24 litigation assets, including aliases and deprecated paths.

### AC-C01-II-A-004 — Exclusions Complete
Prohibits code edits, MCP extensions, parallel methodology directories, runtime schemas, and automated adjudication.

### AC-C01-II-A-005 — Human Control Modeling
Incorporates the Human Review Control Pattern, preserving candidate status for all outputs.

### AC-C01-II-A-006 — Output Path Integrity
Verifies that only the 2 authorized file paths under `docs/` and `outbox/` are created or modified.

### AC-C01-II-A-007 — Technical Validation Compliance
Requires `git diff --check` and empty Git staging verification prior to closeout.

## 12. Current State

```text
Phase 2 Track C — TASK_PHASE2_C01

Design Baseline: APPROVED (v0.2 Baseline Adopted)
C01-I Implementation Design: APPROVED AND CLOSED
C01-II Handoff: APPROVED
C01-II-A Handoff: DRAFT v0.2 (This File)
C01-II-A Execution: NOT STARTED / BLOCKED
C01-II-B Skill / Agent Modification: NOT AUTHORIZED
Code Modification: NOT AUTHORIZED
```

## 13. Next Action

Submit this Handoff Draft v0.2 to Project Owner Review. If approved, Codex is authorized to execute Phase C01-II-A and produce the two output documents specified in Section 5. No implementation or code changes may proceed.
