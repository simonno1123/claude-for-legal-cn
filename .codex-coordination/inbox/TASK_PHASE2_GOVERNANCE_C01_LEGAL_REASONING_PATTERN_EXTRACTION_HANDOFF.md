# TASK_PHASE2_GOVERNANCE_C01_LEGAL_REASONING_PATTERN_EXTRACTION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Status | **DRAFT v1.0** |
| Execution Mode | **DESIGN ONLY** |
| Authorization | **PENDING PROJECT OWNER DECISION** |
| Task Type | Architecture Governance Pattern Extraction |
| Track | Phase 2 Governance / C01 |
| Source Domain | Phase 2 Track C / C02 Request Right Foundation |
| Execution | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |

Materialization of this Handoff records a proposed task boundary only. It does not authorize Pattern Extraction, creation of the authorized output, or any implementation activity.

## 1. Objective

Abstract the staged outcomes of Phase 2 Track C / C02 Request Right Foundation into a reviewable architecture-governance pattern:

```text
LEGAL_REASONING_GOVERNANCE_PATTERN v1.0
```

The proposed pattern is intended to describe reusable governance controls for later legal-AI design work while remaining independent of the facts, parties, documents, or outcomes of any specific case.

This task extracts governance structure. It does not create a global legal-reasoning runtime, change the C01/C02 methodology, implement evidence processing, or authorize a downstream route.

## 2. Fixed Input Baseline Binding

Before any extraction execution, Codex must recompute and exactly match every hash below.

### 2.1 C02-I — Request Right Validation

| Artifact | Path | SHA-256 |
|---|---|---|
| Validation Spec | `docs/phase2/track-c/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC.md` | `FD51E092DC8C4DA3A06BC9FB711D80CEA958E3DE6B6288EE1DB4490A4C6CD94C` |
| Validation Result | `.codex-coordination/outbox/TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_RESULT.md` | `F0003635F051D9CA89956EBC624F7EE8B285D7A5D8202D85B88C4EBF1664A7B7` |

Governance stage status:

```text
CLOSED / DONE
```

Substantive validation result retained without reinterpretation:

```text
BLOCKED — PARTIAL VALIDATION ONLY
```

Permitted pattern inputs:

- input-boundary controls;
- controlled validation states;
- blocked conditions and reasoning-stop behavior;
- separation of evidence, source statement, fact candidate, and legal conclusion.

### 2.2 C02-II — Request Right Framework Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Design Spec | `docs/phase2/track-c/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_SPEC.md` | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` |
| Design Result | `.codex-coordination/outbox/TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_RESULT.md` | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` |

Status:

```text
CLOSED / DONE — DESIGN ONLY
```

Permitted pattern inputs:

- Request Right Candidate model;
- Legal Basis and constituent-element mapping;
- required-fact and burden-candidate interfaces;
- Evidence Requirement mapping;
- Human Review Gate and candidate-only semantics.

### 2.3 C02-III — Request Right Validation Enhancement

| Artifact | Path | SHA-256 |
|---|---|---|
| Validation Enhancement Spec | `docs/phase2/track-c/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_SPEC.md` | `96C1532A2B448C4B3DB0A2926172CC7374B02E42DDF61B714295E534B4A74DFD` |
| Validation Enhancement Result | `.codex-coordination/outbox/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_RESULT.md` | `AF534A372D4B4824F4F402485691372D8081B4D430302DC9E3B2B0D89A9ED226` |

Status:

```text
CLOSED / DONE — COMPLETED WITH MATERIAL GAPS
```

Permitted pattern inputs:

- model-fit validation controls;
- material-gap representation;
- source/fact/legal-fact separation;
- reasoning-stop conditions;
- candidate-only use and qualified-lawyer control.

### 2.4 C02-IV — Input Readiness Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Input Readiness Design Spec | `docs/phase2/track-c/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_SPEC.md` | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` |
| Input Readiness Design Result | `.codex-coordination/outbox/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_RESULT.md` | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` |

Status:

```text
CLOSED / DONE — DESIGN ONLY
```

Permitted pattern inputs:

- Evidence Material Registry;
- document identity, access, text/OCR, extraction, and review states;
- Evidence lifecycle and input-admission gate;
- source-verification and qualified-lawyer review boundaries;
- case isolation, correction, supersession, and blocked controls.

## 3. Authorized Extraction Scope

If and only if this Handoff is approved through Architecture Review and a Project Owner decision, Codex may perform documentation-only pattern extraction that:

1. identifies governance controls common to C02-I through C02-IV;
2. normalizes the evidence–fact–law trace without changing the approved source methodologies;
3. records stop conditions and controlled states;
4. distinguishes machine-assisted structuring from qualified-lawyer judgment;
5. provides non-executable extension interfaces for later separately authorized routes;
6. preserves uncertainty, adverse material, source identity, and human review.

The extraction may not state that incomplete C02-I/C02-III validation succeeded. Design closure, validation completeness, input readiness, and implementation readiness must remain distinct.

## 4. Sole Authorized Output

After separate approval, execution may create exactly one file:

```text
docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN_DRAFT.md
```

Required identity:

```text
Artifact: LEGAL_REASONING_GOVERNANCE_PATTERN
Version: v1.0 Draft
Status: DRAFT — PENDING ARCHITECTURE REVIEW
Type: Architecture Governance Pattern
```

No Review, Decision, implementation file, schema, Skill, Agent, code, or additional output is authorized by this Handoff.

## 5. Required Pattern Structure

### LRG-00 — Boundary Governance

Define the authorization and readiness conditions under which a case, material set, declared analytical scope, and user/reviewer role may enter legal analysis.

The section must include:

- matter/case binding;
- access and permitted-use scope;
- required-input completeness;
- stop conditions;
- case isolation;
- prohibition on using a label, filename, missing document, or prior summary as evidence.

### LRG-01 — Evidence Governance

Define the minimum Evidence Object governance dimensions:

```text
Identity
Source
Hash
Lifecycle
Access Status
Text / OCR Status
Extraction Status
Review Status
Limitations
Version / Supersession
```

The section must state that byte identity does not establish authenticity, admissibility, credibility, probative weight, or proof sufficiency.

### LRG-02 — Fact Governance

Define and preserve the layered fact-generation chain:

```text
Raw Evidence
        ↓
Extracted Evidence Candidate
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Candidate
```

The section must prohibit direct promotion from OCR/extraction output to Legal Fact and must distinguish source-fidelity verification from a finding that the proposition is true.

### LRG-03 — Legal Reasoning Governance

Define the candidate-only analysis chain:

```text
Legal Issue / Question
        ↓
Rule / Legal Basis Candidate
        ↓
Constituent Element
        ↓
Required Fact / Proof Requirement
        ↓
Evidence Mapping / Gap
        ↓
Request Right Candidate
        ↓
Defense / Rebuttal / Conflict
        ↓
Qualified Lawyer Review
```

The section must preserve current-authority verification, adverse facts, defenses, rebuttals, burden uncertainty, and prohibition on automatic selection or outcome prediction.

### LRG-04 — Validation Governance

Use only the controlled reasoning states:

```text
SUPPORTED
UNKNOWN
BLOCKED
```

Required semantics:

- `SUPPORTED` means a verified source currently supports a candidate proposition within stated limits; it does not mean proved, true, admissible, sufficient, or likely to prevail;
- `UNKNOWN` means the available inputs or review are insufficient to assess support;
- `BLOCKED` means a required source, identity, authority, fact, access condition, processing step, or human decision is missing.

No `WIN`, `LOSE`, success-rate, confidence score, or automated merits state is permitted.

### LRG-05 — Human Decision Governance

Define the division of responsibility.

Machine-assisted functions may include:

- information registration and structuring;
- source-bounded extraction candidates;
- fact/element/evidence mapping candidates;
- evidence-gap, conflict, and risk flags;
- traceability and review-support records.

Qualified human/lawyer responsibilities include:

- source and extraction verification;
- evidence-use authorization and confidentiality review;
- legal relevance and current-authority verification;
- Legal Fact, element, burden, defense, and Request Right judgments;
- request-right selection, legal advice, and litigation strategy;
- approval, revision, rejection, and optional application.

The Human Review Gate is a governance control pattern, not a runtime workflow or automatic approval state machine.

## 6. Route A / Route B Extension Requirement

The Draft must support later Route A/Route B extension by defining stable governance interfaces rather than implementing either route.

It must:

- identify which boundary, evidence, fact, reasoning, validation, and human-decision controls are mandatory for any route;
- identify route-specific inputs and outputs as future extension points;
- prevent a route from bypassing input readiness, controlled states, case isolation, or qualified-lawyer review;
- avoid selecting, naming, or implementing a particular OCR, database, RAG, workflow, Agent, Skill, or provider architecture.

Route A/Route B execution and implementation remain separately reviewable and separately authorizable.

## 7. Forbidden Scope

This task does not authorize:

```text
Skill modification
Agent modification
Workflow modification
Code modification
MCP modification
CLAUDE.md modification
Runtime schema modification
OCR implementation
Database implementation
RAG implementation
Automation implementation
Production deployment
```

It also prohibits:

- creation of a global legal-reasoning runtime or parallel methodology framework;
- real-case merits analysis or new fact extraction;
- evidence authenticity, admissibility, credibility, weight, or sufficiency conclusions;
- automatic legal opinions, request-right selection, strategy recommendations, adjudication predictions, or success probabilities;
- treating China Mainland cases as common-law precedent;
- modifying or superseding C01/C02 source artifacts.

## 8. Acceptance Criteria

| ID | Criterion |
|---|---|
| `GOV-C01-001` | Pattern is independent from specific cases, parties, files, and outcomes |
| `GOV-C01-002` | Pattern covers and accurately binds the C02-I through C02-IV governance contributions |
| `GOV-C01-003` | Pattern preserves the Evidence → Extracted Evidence → Source-Verified Fact → Legal Fact → element/request-right chain |
| `GOV-C01-004` | Pattern preserves qualified human review and lawyer decision authority |
| `GOV-C01-005` | Pattern introduces no implementation, runtime, Skill, Agent, Workflow, MCP, OCR, database, or RAG pollution |
| `GOV-C01-006` | Pattern exposes bounded Route A/Route B extension interfaces without authorizing or implementing either route |

## 9. Repository and Git Boundary

Execution, if later authorized, must:

- create only the sole authorized Draft;
- preserve all existing user changes and the dirty worktree;
- introduce no file change under `litigation-legal/`;
- leave the staging area empty;
- pass `git diff --check`;
- perform no `git add`, commit, tag, push, release, or publication.

## 10. Governance Chain

```text
Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator Review
        ↓
Project Owner Decision
        ↓
Only if approved:
Codex Pattern Extraction
        ↓
Pattern Draft + SHA-256
        ↓
Architecture Pattern Review
        ↓
Project Owner Adoption Decision
        ↓
Canonical Governance Asset, only if separately adopted
```

## 11. Current State

```text
Phase 2 Track C / C02 Request Right Foundation:
COMPLETE AS GOVERNANCE INPUT

Route C:
Legal Reasoning Governance Pattern Extraction

Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Authorization:
PENDING PROJECT OWNER DECISION

Pattern Extraction:
NOT STARTED

Pattern Draft:
NOT CREATED

Implementation:
NOT AUTHORIZED
```

The next handoff recipient after materialization is the **Architecture Coordinator (ChatGPT)** for file-level review of the exact physical Handoff SHA-256.
