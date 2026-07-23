# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_PLAN_HANDOFF

STATUS: **APPROVED — PENDING CODEX EXECUTION**

TYPE: Track C Architecture Design Handoff

GOVERNANCE LAYER: Task Authorization Request

TARGET: Request Right Foundation Intelligence

MODULE: `litigation-legal`

C02-I VALIDATION DESIGN: AUTHORIZED (READ-ONLY)

SKILL / AGENT / CODE MODIFICATION: NOT AUTHORIZED

## 1. Task Definition

### 1.1 Task Name
C02-I Request Right Foundation Validation Design

### 1.2 Purpose
Establish a validation framework driven by request-right foundation theory on top of the C01 Litigation Reasoning grid. The objective is to verify if the current system can map the transition:
`Evidence -> Fact -> Legal Fact -> Request Right -> Element -> Proof Requirement -> Evidence Gap`

This stage is **read-only and documentation-only**. No actual editing of skill prompts, rewriting agent definitions, or modifying code is authorized.

## 2. Governance Position

```text
C01 Litigation Reasoning Framework (CLOSED / DONE)
        ↓
C02 Request Right Foundation
  └─ C02-I Validation Design (This Task, Read-Only)
        ↓
C03 Execution Intelligence
```

C02 does not replace C01. While C01 answers "What facts are documented in the materials?", C02 answers "What request-right structures do these facts map to?"

## 3. Theoretical Foundation

C02 is anchored in the Request-Right Foundation theory (请求权基础理论):
1. **Request-Right Primacy**: Case analysis must start from candidate request-rights, not evidence categories or general facts.
2. **Three-Layer Transformation**:
   - *Layer 1 (Fact)*: Raw business/interactive actions (e.g., sending an order).
   - *Layer 2 (Legal Fact)*: Contextualized legal actions (e.g., representation behaviors).
   - *Layer 3 (Element)*: Statutory requirements (e.g., contract formation elements).

## 4. Verification Scope (Three Core Cases)

- **CASE-A: Muxi Shoes Sales Contract Dispute (C02-CASE-A-001)**
  - *Focus*: Transaction facts -> Sales price request-right -> Agency authority dispute mapping.
- **CASE-B: Subofang Corporate Veil Piercing (C02-CASE-B-001)**
  - *Focus*: Creditor request-right -> Company insolvency -> Corporate veil piercing.
- **CASE-C: Zhang Chengqi Enforcement Derivative Dispute (C02-CASE-C-001)**
  - *Focus*: Enforcement debt -> Asset property right dispute -> New request-right generation.

## 5. Fixed Baseline Inputs

The executor must verify the active identities of all prior baselines and the 9 modified files before validation:

### 5.1 Prior Baselines
- **C01 Design Baseline v0.2**: `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`
  - *Required SHA-256*: `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784`
- **C01-II-B-3 Validation Spec**: `docs/phase2/track-c/TASK_PHASE2_C01_II_B_3_VALIDATION_SPEC.md`
  - *Required SHA-256*: `724FC07FE29142017FC25FB2D9863B88B8DD7A05C71EF48D0AA7968B7F279E0F`

### 5.2 Active 9 Skill Baselines
- `claim-chart/references/element-templates.md`: `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D`
- `matter-intake/SKILL.md`: `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18`
- `chronology/SKILL.md`: `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2`
- `claim-chart/SKILL.md`: `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B`
- `matter-update/SKILL.md`: `DD4EED89B01DAC18CBB567C26EF089DEB6E0BB42CE15A5EA38AC0A82D8712E30`
- `matter-briefing/SKILL.md`: `967C982389BD61888986FAB83B74B42E8D67935C5AD0A380D287731D2EFF517E`
- `brief-section-drafter/SKILL.md`: `53CEFB16B6A0F5CFC6C95BCFB80F936BAE28B3CC283C1FC980883E595019B8A1`
- `evidence-preservation/SKILL.md`: `295A6F738BA7A6D7E87695DB8CEE49BE2AF77226A8915DB531695CA5130188F9`
- `confidential-evidence-review/SKILL.md`: `828A5F25C25D96FF9BA0BB5B1F654A21EA4A49CF9103D33D55FEECCCC0EE5E77`

## 6. Authorized Outputs

Codex is authorized to create exactly **2 documentation files**:

### Output A: Request-Right Validation Spec
- **Path**: `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md`
- **Content**: Modeling rules, case pack information, test criteria, and output templates.

### Output B: Execution Result
- **Path**: `.codex-coordination/outbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_RESULT.md`
- **Content**: Execution record, output SHA-256, and validation status checks.

## 7. Explicit Exclusions

- Modifying any file under `litigation-legal/` or `agents/`;
- Modifying manifests, MCP configs, Plugin registers, or CLAUDE.md;
- Creating D1-D6;
- Staging, committing, pushing, or releasing changes.

## 8. Acceptance Criteria

- **AC-C02-I-001**: Request-right must serve as the primary entry point for analysis.
- **AC-C02-I-002**: Differentiate `Evidence -> Fact -> Legal Fact -> Element`.
- **AC-B3-003**: Prohibit automated claim selection, factual supplements, or outcome predictions.
- **AC-B3-004**: Complete validation tracing for Muxi, Subofang, and Zhang Chengqi cases.
- **AC-B3-005**: Human review priority remains preserved.
- **AC-B3-006**: `git diff --check` passes, staging remains empty, and only the two designated outputs are created.
