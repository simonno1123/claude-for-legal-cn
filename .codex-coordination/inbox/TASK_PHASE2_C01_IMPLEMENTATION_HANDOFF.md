# TASK_PHASE2_C01_IMPLEMENTATION_HANDOFF

STATUS: **DRAFT — PROJECT OWNER REVIEW REQUIRED (WITH CONDITIONS)**

TYPE: Track C Implementation Authorization Request

MODE: IMPLEMENTATION HANDOFF DESIGN

VERSION: v0.2

TARGET MODULE: `litigation-legal`

IMPLEMENTATION: **NOT AUTHORIZED**

## Dependency

This Handoff depends on:

```text
TASK_PHASE2_C01_BASELINE_DECISION
Status: ACCEPTED
```

Canonical dependency:

`.codex-coordination/decisions/TASK_PHASE2_C01_BASELINE_DECISION.md`

---

## 1. Task Identity

### Task Name

C01 Litigation Reasoning Framework Implementation Handoff

### Parent Task

`TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN`

### Approved Baseline

`TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2`

### SHA-256

`67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5`

---

## 2. Objective

Translate the approved C01 Design Baseline into executable implementation phase definitions.

The implementation goal is to enhance litigation reasoning within the `litigation-legal` module via localized Skill and Agent instructions, without altering global system structures or external provider dependencies.

---

## 3. Architecture Position

```text
Existing Domain Plugin Architecture
        ↓
litigation-legal Plugin
        ↓
Existing Litigation Workflow
        ↓
C01 Implementation
        ↓
Skill / Agent Enhancement
```

Explicitly forbidden:

- Creating a new system layer or plugin
- Top-level `methodology/` or `legal-reasoning-core/` directories
- Any global legal reasoning core

---

## 4. Implementation Scope

The authorized scope for the implementation phase covers:

### 4.1 Existing Skill Enhancement
Enhance litigation-legal skills to support:
- Legal issue identification (争议焦点识别)
- Request-right basis analysis (请求权基础分析)
- Element decomposition (要件拆解)
- Proof mapping (证明责任与证据映射)
- Defense / Rebuttal analysis (抗辩与再抗辩分析)

### 4.2 Agent Prompt Enhancement
Optimize:
- Agent instructions
- Analysis workflows
- Output schemas

### 4.3 Output Contract Enhancement
Introduce lawyer analysis output schema:
```yaml
analysis:
  matter:
  issues:
  claims:
  elements:
  proof:
  defenses:
  review_status:
```

---

## 5. Explicit Exclusions

The implementation phase is strictly prohibited from creating or editing:

### 5.1 Data Assets
- Legal databases (法规库)
- Case/Experience databases (案例经验库)
- Knowledge graphs (知识图谱)

### 5.2 Autonomous Decisions
- Automatic claim selection (自动选择请求权)
- Autonomous litigation strategy generation (自动生成诉讼策略)
- Automated win-rate/adjudication predictions (胜诉概率预测)

### 5.3 External Capabilities
- MCP modification or addition of new tools
- External Provider integrations (real APIs)
- Automated monitoring or scheduling

### 5.4 Cross-Border or Multi-Plugin modifications
- Modifying `corporate-legal`, `commercial-legal`, `employment-legal`, etc.
- Multi-plugin shared methodology layers.

### 5.5 Schema Modification Constraints (PO Condition 1)
- **Runtime Schema Modifications**: Any modification to runtime validation schemas, framework schemas, or MCP configurations is strictly prohibited.
- **Rule**: Any runtime schema modification requires separate explicit authorization.

---

## 6. Implementation Phases (PO Condition 2)

The execution must be divided into three sequential steps, preserving strict separation of engineering mapping from code modifications:

### Phase C01-I — Design Translation (Engineering Mapping Only)
Translate the baseline design specifications into concrete code/prompt modification proposals.
- **Constraints**: This phase is strictly limited to documentation and mapping. **No implementation code, Skill files, or Agent instruction modifications are authorized.**
- **Deliverable**: Implementation Design Spec (Markdown)
- **Path**: `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN.md`

### Phase C01-II — Skill / Agent Enhancement
Implement the approved prompt, instruction, and local workflow changes based on the prioritized implementation deliverables.
- **Constraints**: Implementation must proceed strictly under the frozen priority order (see Section 7).

### Phase C01-III — Validation
Verify the changes using the validation cases defined in the design baseline (买卖合同主体争议, 公司人格否认, 执行衍生责任).
- **Deliverable**: Validation Report with proof-mapping chain logs.

---

## 7. Prioritized Implementation Deliverables (PO Condition 2)

The implementation deliverables are frozen into prioritized stages to prevent unguided implementation:

### 7.1 C01-II Priority Deliverables (Core Analysis Structure)
These must be implemented first, directly corresponding to elements, claims, proof, and defenses:

| Deliverable ID | Name | Canonical Path |
|---|---|---|
| D2 | Request Right Analysis Schema | `docs/phase2/track-c/TASK_PHASE2_C01_REQUEST_RIGHT_ANALYSIS_SCHEMA.md` |
| D3 | Element-Proof Model Spec | `docs/phase2/track-c/TASK_PHASE2_C01_PROOF_MODEL_SPEC.md` |
| D4 | Defense / Rebuttal Model Spec | `docs/phase2/track-c/TASK_PHASE2_C01_DEFENSE_REBUTTAL_MODEL.md` |

### 7.2 Post-C01-II Deliverables (General Framework & Verification)
These are deferred to validation and coordination stages:

| Deliverable ID | Name | Canonical Path |
|---|---|---|
| D1 | Litigation Reasoning Framework Spec | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_SPEC.md` |
| D5 | Validation Protocol | `docs/phase2/track-c/TASK_PHASE2_C01_VALIDATION_PROTOCOL.md` |
| D6 | Human Review Gate Spec | `docs/phase2/track-c/TASK_PHASE2_C01_HUMAN_REVIEW_SPEC.md` |

No runtime script, executable CLI, database connector, or external endpoint may be delivered.

---

## 8. Acceptance Criteria

### AC-IMP-001 — Baseline Traceability
Implementation must trace back to C01 Design Baseline v0.2 with matching SHA-256.

### AC-IMP-002 — In-plugin Confinement
All implementation changes must reside strictly within `litigation-legal/` (excluding documentation). No global folders are created.

### AC-IMP-003 — Zero External dependencies
No legal database, case database, or commercial API is integrated.

### AC-IMP-004 — Human-in-the-loop Preservation
The output must maintain the Candidate -> Review -> Approved -> Applied state machine, enforcing manual confirmation before strategy output.

### AC-IMP-005 — Non-deterministic Analysis
The enhanced skill must correctly represent gaps, confidence metrics, and missing evidence instead of outputting over-confident opinions.

### AC-IMP-006 — Governance and CI compliance
The code changes must pass all default lints and CI verification checks (e.g. `scripts/lint-tool-scope.py`).

### AC-IMP-007 — Priority and Schema Constraints (PO Conditions)
- No runtime schema modification was performed without separate, explicit authorization.
- Deliverables were created strictly in accordance with the priority sequence: C01-I Engineering Mapping first; C01-II D2/D3/D4 next; D1/D5/D6 post-C01-II.

---

## 9. Approval Flow

```text
C01 v0.2 Baseline Approved
        ↓
Implementation Handoff Draft (v0.2 with PO Conditions)
        ↓
Project Owner Review & Approval
        ↓
Codex Implementation Task Creation
        ↓
Execution of Phase C01-I (Translation Spec - No code)
        ↓
Project Owner Approval of Translation Spec
        ↓
Execution of Phase C01-II (Enhancement - D2/D3/D4 Priority)
        ↓
Execution of Phase C01-III (Validation)
        ↓
Acceptance Review
```

---

## 10. Current Status

```text
Phase 2 Track C
TASK_PHASE2_C01

Design: APPROVED (v0.2 Baseline Adopted)
Implementation Handoff: REVIEWED (With PO Conditions)
Implementation Authorization: PENDING
Code / Skill / Agent Modification: NOT AUTHORIZED
```
