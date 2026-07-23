# TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN

STATUS: **REVIEWED BASELINE**

TYPE: Track C Task Design

VERSION: v0.2

MODE: DOCUMENTATION / SPECIFICATION DESIGN

TARGET MODULE: `litigation-legal`

IMPLEMENTATION: **NOT AUTHORIZED**

## Dependency

This Task depends on:

```text
TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION
Status: ACCEPTED
```

Canonical dependency:

`.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md`

## 1. Task Summary

### Task Name

Litigation Reasoning Framework Design

### Track

Track C — Legal Methodology Enhancement

### Target Module

`litigation-legal`

This is a design Task. It defines a reviewable specification baseline for a
future implementation Task; it does not modify the target module.

## 2. Objective

Design an in-domain case-analysis enhancement framework for the existing
`litigation-legal` plugin. The framework should assist licensed lawyers and
reviewers with:

- legal-question identification;
- request-right / claim-basis analysis;
- element decomposition;
- legal-fact organization;
- burden-of-proof analysis;
- evidence mapping;
- defense and rebuttal analysis.

The output is a lawyer-reviewable analysis structure, not an automated legal
opinion or adjudication engine.

## 3. Architecture Position

```text
Existing Domain Plugin Architecture
        ↓
litigation-legal Plugin
        ↓
Existing Litigation Workflow
        ↓
C01 Reasoning Enhancement
        ↓
Future Skill / Agent Enhancement
```

C01 does not create a new system layer, plugin or top-level methodology tree.

Explicitly forbidden:

```text
Global Legal Reasoning Core
methodology/
legal-reasoning-core/
```

Request-right analysis is litigation-domain methodology. It is not a universal
reasoning layer for every legal practice module.

## 4. Problem Statement

The target problem is not merely access to legal information. It is the failure
to organize a dispute according to a lawyer's actual analysis path.

Insufficient path:

```text
Input Facts → Search Law → Output Opinion
```

Required path:

```text
Matter
  ↓
Question
  ↓
Claim / Request Right
  ↓
Element
  ↓
Legal Fact
  ↓
Burden and Standard of Proof
  ↓
Evidence
  ↓
Defense / Rebuttal
  ↓
Human Legal Review
```

C01 defines this path without hard-coding a substantive outcome.

## 5. Core Reasoning Model

### 5.1 Matter

The matter-level context establishes dispute and client posture:

```yaml
matter:
  dispute_type:
  parties:
  procedural_stage:
  client_position:
  objective:
```

Required rules:

- distinguish litigation, arbitration, enforcement and pre-action posture;
- identify the represented party and requested objective;
- do not treat the system as a neutral court decision-maker;
- preserve uncertainty and missing-fact markers.

### 5.2 Question

One matter may contain multiple legal questions. Each Question must be separately
traceable to facts, claims, defenses and authority.

Example:

```text
Q1: 合同是否成立？
Q2: 合同主体是谁？
Q3: 付款义务是否产生并届期？
Q4: 是否存在抗辩或责任限制？
```

### 5.3 Claim

A Claim records the requested legal consequence and its candidate basis.

```yaml
claim:
  requested_relief:
  claim_basis:
  claimant:
  respondent:
  procedural_vehicle:
  authority:
  status: candidate
```

Claims remain candidates until reviewed by a qualified human. The framework must
support alternative, cumulative or mutually exclusive candidate paths without
silently selecting one as final.

### 5.4 Element

Each candidate Claim is decomposed into legally relevant elements.

Example:

```text
Claim: 买卖合同价款请求权

E1 合同成立并对相关主体生效
E2 履行或交付达到付款条件
E3 付款义务届期
E4 对方未履行付款义务
```

Each Element must link to:

- governing authority;
- required facts;
- burden allocation;
- available and missing evidence;
- defenses and rebuttals;
- human-review status.

Element templates must remain updateable and may not encode case outcomes as
permanent doctrine.

## 6. Legal Fact Classification Model

C01 uses a four-level fact model:

```text
Case Fact
    ↓
Event Fact
    ↓
Element Fact
    ↓
Material Fact
```

### Case Fact

A party or source's narrative assertion.

Example: `客户称业务员代表公司交易。`

### Event Fact

A concrete event capable of being placed in time, source and actor context.

Example: `业务员通过微信发送订单。`

### Element Fact

A fact proposition mapped to a candidate legal element.

Example: `公司可能通过业务员作出交易意思表示。`

### Material Fact

An abstracted fact proposition necessary for legal evaluation.

Example: `是否存在可归属于公司的意思表示。`

`Judicial Fact` is excluded from the C01 design baseline because it describes a
court's ultimate finding, not a pre-decision lawyer analysis input. The framework
must not present a candidate Material Fact as a judicially established fact.

## 7. Proof Model

C01 must define the following traceable chain:

```text
Element
  ↓
Required Fact
  ↓
Burden of Proof
  ↓
Applicable Proof Standard / Evaluation Rule
  ↓
Evidence
  ↓
Gap and Confidence Statement
```

Minimum mapping:

| Candidate element | Fact to be proved | Burden candidate | Evidence candidate | Gap |
|---|---|---|---|---|
| 合同成立 | 双方达成合意并可归属于相应主体 | 原告/申请人，待规则核验 | 微信、订单、合同、履行材料 | 授权或追认材料是否完整 |
| 交付完成 | 标的物实际交付且符合约定付款条件 | 原告/申请人，待规则核验 | 物流、签收、验收、对账 | 签收主体及异议记录 |
| 未付款 | 到期债务未履行 | 依主张与证据规则核验 | 流水、对账、催告、回函 | 完整期间流水或抵销材料 |

Burden allocation and proof standards must be derived from current statutes,
judicial interpretations and applicable evidence rules, with authority and date
recorded. They must not be inferred solely from case examples or permanently
hard-coded into prompts.

## 8. Defense / Rebuttal Model

The framework must support adversarial paths:

```text
Claim
  ↓
Defense
  ↓
Defense Element
  ↓
Required Fact / Burden
  ↓
Evidence
  ↓
Rebuttal
  ↓
Sur-rebuttal or Remaining Gap
```

Required perspectives:

- claimant/plaintiff path;
- respondent/defendant defense;
- rebuttal and, when material, further response;
- procedural as well as substantive defenses;
- alternative theories and inconsistent evidence.

The system assists counsel from the stated client position. It does not simulate
a final court judgment or suppress adverse facts.

## 9. Design Deliverables

If this Draft receives Project Owner approval, the design execution Task may
create only the following specification artifacts:

| ID | Deliverable | Proposed path |
|---|---|---|
| D1 | Litigation Reasoning Framework Specification | `docs/PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_SPEC.md` |
| D2 | Request Right Analysis Schema | `docs/PHASE2_C01_REQUEST_RIGHT_ANALYSIS_SCHEMA.md` |
| D3 | Proof Model Specification | `docs/PHASE2_C01_PROOF_MODEL_SPEC.md` |
| D4 | Defense / Rebuttal Model | `docs/PHASE2_C01_DEFENSE_REBUTTAL_MODEL.md` |
| D5 | Validation Protocol | `docs/PHASE2_C01_VALIDATION_PROTOCOL.md` |
| Result | Design execution record | `.codex-coordination/outbox/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_RESULT.md` |

The deliverables are normative design documents, not runtime schemas or code.

## 10. Validation Cases

### CASE-C01-001 — 买卖合同主体争议

Validate:

- party and principal attribution;
- authority, apparent-authority and ratification questions where applicable;
- course of dealing and transaction records;
- element/fact/evidence traceability;
- plaintiff and defendant paths.

### CASE-C01-002 — 公司人格否认

Validate:

- controlling relationship;
- commingling or abuse allegations;
- candidate responsibility path;
- claimant burden and respondent rebuttal;
- separation of allegation, evidence and legal conclusion.

### CASE-C01-003 — 执行衍生责任

Validate:

- procedural stage and available procedural vehicle;
- property clues and responsible-party theory;
- claim/request-right selection;
- burden and evidence gaps;
- separation of enforcement measure from substantive liability.

Each case must include expected structural checks, prohibited shortcuts and a
human-review rubric. Validation does not require a predetermined winning answer.

## 11. Out of Scope

C01 does not build or authorize:

- a legal database;
- a case database or case-experience repository;
- a lawyer experience database;
- a knowledge graph;
- a global Legal Reasoning Core;
- an automated legal-opinion system;
- automatic claim selection or litigation strategy;
- court, arbitration or enforcement-system integration;
- external monitoring or autonomous action.

Legal authorities and case materials continue to use the existing Legal Data MCP
and China Case Authority Layer. Case materials calibrate analysis but do not
replace statutes, judicial interpretations or mandatory rules.

## 12. Permission and Implementation Boundary

### Current Draft Stage

This file may be reviewed and edited as a Task Draft only.

Current authorization does **not** permit creation of D1–D5 or a Design Result.

### After Project Owner Task Approval

The approved Design Task may modify only:

- the five D1–D5 `docs/` paths listed in Section 9;
- `.codex-coordination/outbox/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_RESULT.md`.

### Always Forbidden Under This Task

- any file under `litigation-legal/`;
- any `SKILL.md` or Agent definition;
- any runtime schema, hook, script or test implementation;
- Plugin or Marketplace metadata;
- MCP or connector configuration;
- Phase 1/1.5 assets;
- `PROJECT_SCOPE.md`, `PHASE_2_ROADMAP.md` or Architecture v0.5;
- git add, commit, tag, push or GitHub Release.

Future implementation requires a separate approved Handoff:

`TASK_PHASE2_C01_IMPLEMENTATION_HANDOFF.md`

## 13. Acceptance Criteria

### AC-C01-001 — Request-right Structure

D1/D2 define a traceable Matter → Question → Claim → Element path suitable for
China litigation analysis and alternative candidate claims.

### AC-C01-002 — Element / Proof Mapping

D2/D3 map each Element to required facts, burden, applicable proof rule,
evidence and gaps without hard-coding unverified doctrine.

### AC-C01-003 — Adversarial Analysis

D4 supports defense, defense elements, evidence, rebuttal and remaining gaps from
the stated client position.

### AC-C01-004 — No Database Assets

No legal, case, experience or knowledge-graph database is created or proposed as
a hidden dependency.

### AC-C01-005 — In-domain Implementation Compatibility

The specifications can later be implemented through narrow `litigation-legal`
Skill/Agent enhancement without a parallel methodology architecture.

### AC-C01-006 — Human Review Gate

All claims, facts, burden allocations, evidence evaluations and strategy outputs
remain candidates requiring qualified human legal review.

All six criteria must pass before an Implementation Handoff may be proposed.

## 14. Approval Flow

```text
C01 Design Task Draft
        ↓
Project Owner Review
        ↓
C01 Design Task Approval
        ↓
Codex Design Execution (D1–D5 only)
        ↓
Design Result / Review / Acceptance
        ↓
Separate Implementation Handoff
        ↓
Implementation Review and Acceptance
```

## 15. Current State

```text
Track C
TASK_PHASE2_C01

Design Handoff: Draft Completed
Project Owner Task Approval: Pending
Design Execution: Not Authorized
Implementation: Not Authorized
```

## 16. Next Action

Submit this Draft to Project Owner Review.

If approved, Codex may execute only the D1–D5 documentation design scope and
produce the specified Design Result. Implementation remains blocked until a
later, separately approved `TASK_PHASE2_C01_IMPLEMENTATION_HANDOFF.md`.

After C01 Design Task approval, Track B may separately formalize:

`TASK_PHASE2_B01_MODEL_ADAPTATION_SPECIFICATION_DESIGN.md`
