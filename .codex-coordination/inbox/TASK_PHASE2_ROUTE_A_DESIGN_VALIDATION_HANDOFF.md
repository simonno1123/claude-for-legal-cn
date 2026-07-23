# TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION |
| Task Type | Evidence Infrastructure Architecture Design Validation |
| Route | Phase 2 / Route A |
| Execution Mode | **READ-ONLY DESIGN VALIDATION** |
| Execution | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

Materialization of this Handoff establishes the proposed validation task and input identities only. It does not authorize Validation Spec/Result creation, case-merits analysis, OCR execution, evidence processing, or implementation.

## 1. Validation Objective

Validate whether the Route A Evidence Infrastructure Design can safely and consistently represent complex legal-practice evidence inputs while preserving the canonical Evidence → Fact Candidate → Source-Verified Fact Candidate → Legal Fact Candidate boundary.

The validation object is:

```text
Route A Evidence Infrastructure Design v1.0
```

It is not:

```text
OCR engine validation
Database validation
MCP validation
Agent validation
Workflow validation
Production performance testing
Case merits analysis
```

Core question:

> Can the design register, state-map, review, gate, audit, and safely block the complex document categories encountered in lawyer work without inventing facts or bypassing qualified-human control?

## 2. Fixed Baseline Binding

Before any validation execution, Codex must recompute and exactly match every required hash below. A missing or mismatched artifact yields `BLOCKED` and prohibits output creation.

### 2.1 Input 001 — Route A Evidence Infrastructure Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Design Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_HANDOFF.md` | `9E40FC833135C8C7B5CE9B97A689D4335F10827A242A97424D20880B249831A3` |
| Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` |
| Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md` | `DF22B914C0F92073E41B5126DAE5AE7CBE1C442CBCE99798A0488BDE3B97EAFD` |

The current coordination instruction states that Route A Design is closed. At Handoff preparation time, no separately materialized Route A Design Review/Decision file was found in the repository. Validation execution therefore binds the physical Handoff/Spec/Result identities above and still requires this Validation Handoff's own Architecture Review and Project Owner decision before execution.

Validation focus:

- Evidence Object completeness;
- component responsibilities and trust zones;
- lifecycle and independent status dimensions;
- native-text/OCR/hybrid/spreadsheet/message/manual routes;
- Document Review and Legal Fact Review gates;
- matter-level Analysis-Ready Manifest;
- audit, correction, supersession, and invalidation behavior.

### 2.2 Input 002 — LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 Canonical

| Artifact | Path | SHA-256 |
|---|---|---|
| Canonical Governance Pattern | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` |
| Pattern Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_GOVERNANCE_C01_LEGAL_REASONING_PATTERN_ADOPTION_DECISION.md` | `A275B101843D4DDEC82715AC4857C2DEBB576292FDF29481D38FE069F88E1CD2` |

Mandatory boundary:

```text
Raw Evidence
        ↓
Extracted Evidence Candidate
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Candidate
        ↓
Separately governed legal reasoning
```

The validation must verify conformance with LRG-00, LRG-01, LRG-02, LRG-04, and LRG-05. It may not modify or reinterpret the canonical Pattern.

### 2.3 Input 003 — C02-IV Input Readiness Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Input Readiness Design Spec | `docs/phase2/track-c/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_SPEC.md` | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` |
| Input Readiness Design Result | `.codex-coordination/outbox/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_RESULT.md` | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` |
| Architecture Review | `.codex-coordination/reviews/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_REVIEW.md` | `46A1F6CAD52A2F73421804AED701D1AEC8214B37C55040148E1611C3A3DE5402` |
| Project Owner Decision | `.codex-coordination/decisions/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_DECISION.md` | `4ACEAECA570721CF6A1B2B0882D0D2068B51CFF7B88BB876CA0F8554F2EF4478` |

Validation focus:

- Evidence Registry identity and provenance;
- independent access/hash/text/OCR/extraction/review/readiness states;
- document and case-bundle gates;
- source-verification and qualified-lawyer review separation;
- correction, supersession, and blocked controls.

### 2.4 Frozen Case-Material Governance Inputs

These inputs define the previously verified availability/gap state. They do not authorize new case facts or merits analysis.

| Artifact | Path | SHA-256 |
|---|---|---|
| C02-I Case Material Import Manifest | `docs/phase2/track-c/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_MANIFEST.md` | `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C` |
| C02-I Case Material Import Result | `.codex-coordination/outbox/TASK_PHASE2_C02_I_CASE_MATERIAL_IMPORT_RESULT.md` | `2269DE1DF06037851B10C5299F0DD0192C44AC7BE010702CD940253562DAEA05` |
| C02-III Validation Enhancement Spec | `docs/phase2/track-c/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_SPEC.md` | `96C1532A2B448C4B3DB0A2926172CC7374B02E42DDF61B714295E534B4A74DFD` |
| C02-III Validation Enhancement Result | `.codex-coordination/outbox/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_RESULT.md` | `AF534A372D4B4824F4F402485691372D8081B4D430302DC9E3B2B0D89A9ED226` |

The validation may recheck only file existence, byte hash, file type, and text/OCR readiness at already approved paths where access is available. It may not extract new substantive case facts, assess evidence validity, or analyze claims.

## 3. Validation Semantics

### 3.1 What Counts as Compatibility

A case profile is compatible when the design can:

- represent each material category as an Evidence Object or explicit missing object;
- map identity, source, access, hash, file type, text/OCR, extraction, and review states;
- select a conceptual processing route without running it;
- identify missing/partial/blocked conditions;
- prevent unsafe promotion to fact or Legal Fact;
- produce a matter-level readiness decision and human-readable blockers;
- preserve matter isolation and audit/invalidation lineage.

Compatibility does not require that all materials exist or become `READY`. Correctly returning `BLOCKED` for a missing critical input is a successful safe-design behavior.

### 3.2 Infrastructure and Legal-Reasoning States

Infrastructure descriptors:

```text
READY
PARTIAL
BLOCKED
```

Canonical legal-reasoning states:

```text
SUPPORTED
UNKNOWN
BLOCKED
```

The validation must confirm that `PARTIAL` never becomes partial proof, partial merits support, probability, or authorization to bypass a critical gap.

### 3.3 Prohibited Validation Conclusions

The validation may not conclude:

- that a source statement is true because it is registered or extracted;
- that a matching hash proves authenticity or admissibility;
- that OCR confidence proves fact accuracy;
- that a case has a viable request right, likely outcome, or recommended strategy;
- that missing material does not exist;
- that a design pass authorizes implementation.

## 4. Case Validation Profiles

### 4.1 CASE-A — Commercial Transaction Material Profile

Matter label: 沐希鞋业案件. The label is a validation identifier only, not evidence.

Bound material categories from the frozen governance inputs:

- transaction bill/account workbook;
- company/public-record PDF;
- WeChat or other correspondence records;
- payment vouchers.

Frozen C02-III availability:

```text
Accessible and hash-verified categories: 1 / 4
Unavailable/missing categories: 3 / 4
```

Validation objectives:

- map spreadsheet, PDF, message/screenshot, and payment-record categories into Evidence Objects;
- test native-text, image/OCR, spreadsheet/table, and missing-source routes;
- verify that the accessible public-record PDF cannot substitute for transaction materials;
- verify `PARTIAL` infrastructure readiness while affected request-right reasoning remains `BLOCKED`;
- verify Document Review and Legal Fact Review remain separate.

No transaction fact, amount, party attribution, delivery, payment, or request-right conclusion may be generated.

### 4.2 CASE-B — Litigation and Corporate Record Profile

Matter label: 塑博坊相关案件. The label is a validation identifier only.

Bound material categories:

- judgment/court-document PDF;
- corporate registration records;
- shareholder records;
- bank-flow or financial records;
- enforcement-related materials.

Frozen C02-III availability:

```text
Accessible categories: 0 / 5
```

Validation objectives:

- represent court documents, corporate-record collections, spreadsheets/images, and enforcement materials without directory-level identity ambiguity;
- require per-file identity where a collection's child files are relied upon;
- verify missing/path-drift behavior and safe invalidation of earlier registered hashes;
- verify that no OCR, extraction, corporate-liability, shareholder-liability, or evidence conclusion is inferred from filenames or prior counts;
- verify matter gate `BLOCKED` and explicit remediation requirements.

### 4.3 CASE-C — Property, Cost, and Enforcement-Derivative Profile

Matter label: 康尔达相关案件. The label is a validation identifier only.

Bound material categories:

- fee-detail spreadsheet;
- transaction materials;
- property/asset records;
- enforcement records;
- derivative-claim materials.

Frozen C02-III availability:

```text
Accessible categories: 0 / 4 recorded required categories
```

Validation objectives:

- test structured table/range requirements and file-unavailable behavior;
- verify that a fee workbook cannot substitute for property, enforcement, or derivative-claim sources;
- map missing material to explicit Evidence Objects/gaps and a blocked Analysis-Ready Manifest;
- prohibit property ownership, asset transfer, enforcement path, derivative request right, or priority inference.

## 5. Validation Procedure

### Step 0 — Identity and Authorization Check

- recompute all bound artifact hashes;
- verify the physical Validation Handoff identity;
- confirm outputs are absent;
- record pre-execution `litigation-legal` status and staging state;
- stop on mismatch.

### Step 1 — Material Registration Mapping

For each case material category, create a documentation-only validation row containing:

```text
evidence_id candidate
matter_id
document/category identity
source description
approved path/object reference
expected and current hash state
file type
access scope/status
text/OCR/extraction/review status
lifecycle state
blocking reasons
```

No runtime registry or database is created.

### Step 2 — Document State Mapping

Validate the design's independent dimensions and lifecycle transitions:

```text
RECEIVED
REGISTERED
HASH_VERIFIED
TEXT_ASSESSED
PROCESSING_ROUTE_SELECTED
EXTRACTED_UNVERIFIED
DOCUMENT_HUMAN_REVIEWED
SOURCE_VERIFIED
LEGAL_FACT_REVIEWED
ANALYSIS_READY
```

Missing, denied, corrupt, mismatched, unverified, rejected, or superseded conditions must map to an explicit safe state rather than a skipped transition.

### Step 3 — OCR Boundary Scenarios

Use conceptual/scenario-level validation for:

- scan-only PDF;
- hybrid PDF with partial text;
- image-based bank-flow/table record;
- WeChat screenshot or incomplete conversation image;
- stamp/signature/handwriting region;
- low-quality or conflicting OCR output.

Expected invariant:

```text
OCR Result
≠ Source-Verified Fact Candidate
≠ Legal Fact Candidate
```

The validation must not run OCR or create extracted case content.

### Step 4 — Matter Input Gate Scenarios

Validate:

- one ready file with critical missing categories;
- all files inaccessible;
- prior manifest hash with current file missing;
- filename/path match with hash mismatch;
- optional material missing while all declared critical inputs are ready;
- new adverse/conflicting material after readiness;
- scope or access authorization change.

Expected output is a scope-specific `READY`, `PARTIAL`, or `BLOCKED` infrastructure descriptor plus explicit legal-reasoning consequences.

### Step 5 — Human Gate Scenarios

Verify at minimum:

#### Document Review Gate

- OCR/transcription fidelity;
- extraction completeness and source locators;
- table/message sequence and missing regions;
- corrections and limitations.

#### Legal Fact Review Gate

- matter/purpose/access scope;
- source/provenance and unresolved authenticity/admissibility questions;
- fact transformation rationale;
- adverse/conflicting material;
- qualified-lawyer authorization for analytical use.

The first gate cannot silently satisfy the second.

### Step 6 — Audit and Invalidation Scenarios

Verify that changed bytes, corrected extraction, superseding files, new conflicts, revoked access, or review reversal identify and block dependent manifests and downstream candidates pending re-review.

### Step 7 — Matter Isolation Test

Verify that identical filenames, hashes, parties, or source systems across matters do not authorize cross-matter reuse without a separate use record and approval.

### Step 8 — Boundary and Git Verification

- confirm only the two authorized documentation outputs exist;
- confirm no file under `litigation-legal/` changed by execution;
- run `git diff --check`;
- confirm staging remains empty;
- perform no git publication action.

## 6. Required Validation Spec Structure

The Validation Spec must include:

1. document control and exact input hashes;
2. validation method and non-goals;
3. case-neutral pass/fail semantics;
4. CASE-A/B/C material-registration mapping;
5. lifecycle coverage matrix;
6. OCR isolation scenarios;
7. Document Review and Legal Fact Review gate scenarios;
8. Matter Input Gate decisions and blockers;
9. audit, invalidation, and case-isolation scenarios;
10. Governance Pattern and C02-IV conformance matrix;
11. acceptance-criteria assessment;
12. implementation boundary and next governance action.

## 7. Authorized Outputs

After separate Project Owner validation-execution approval, Codex may create exactly two files.

### Output A — Validation Spec

```text
docs/phase2/route-a/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md
```

### Output B — Validation Result

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md
```

Materialization of this Handoff does not authorize either output.

## 8. Strict Forbidden Scope

```text
Implementation: NOT AUTHORIZED
OCR Integration or Execution: NOT AUTHORIZED
Database / Object Store: NOT AUTHORIZED
MCP: NOT AUTHORIZED
Agent: NOT AUTHORIZED
Skill: NOT AUTHORIZED
Workflow: NOT AUTHORIZED
Code / Test Scripts: NOT AUTHORIZED
Runtime Schema: NOT AUTHORIZED
RAG / Vector Store: NOT AUTHORIZED
Production Deployment: NOT AUTHORIZED
Route B: FROZEN / NOT AUTHORIZED
```

Also prohibited:

- new substantive case-fact extraction;
- evidence authenticity/admissibility/credibility/weight/sufficiency conclusions;
- request-right, burden, strategy, outcome, or probability conclusions;
- generated or reconstructed missing evidence;
- modification of Route A Design, C02-IV, or canonical Governance Pattern assets;
- git add, commit, tag, push, release, or publication.

## 9. Acceptance Criteria

The statuses below are pass conditions to be evaluated during authorized validation; they are not pre-awarded by this Handoff.

### ROUTE-A-VAL-001 — Evidence Registry Mapping

PASS when all required case material categories can be represented as traceable Evidence Objects or explicit missing/blocked records without inventing identity, content, or facts.

### ROUTE-A-VAL-002 — Lifecycle Coverage

PASS when native, OCR, hybrid, table, message/image, missing, mismatched, corrected, and superseded scenarios map to traceable states with no prohibited jump.

### ROUTE-A-VAL-003 — OCR Boundary Isolation

PASS when every OCR scenario remains an extraction candidate until Document Review and Legal Fact Review, and no confidence/processing state becomes legal support.

### ROUTE-A-VAL-004 — Input Gate Blocking

PASS when missing or unverified critical inputs produce scope-specific `BLOCKED`, while `PARTIAL` remains an infrastructure descriptor that cannot authorize affected legal reasoning.

### ROUTE-A-VAL-005 — CASE-A/B/C Compatibility

PASS when all three material profiles can be safely mapped, routed, reviewed, or blocked. Full material availability and successful case analysis are not required and must not be claimed.

### ROUTE-A-VAL-006 — Zero Implementation Drift

PASS when only the two authorized documentation outputs are created and there is zero code, Skill, Agent, Workflow, MCP, schema, OCR, database, RAG, deployment, or `litigation-legal` drift.

## 10. Required Result Record

The Result, if later authorized, must record:

- Validation Handoff and all input hashes;
- Validation Spec hash;
- each AC status and supporting section/scenario;
- per-case compatibility versus material-readiness distinction;
- any blocked validation scope or design defect;
- exact created/modified file list;
- zero implementation/runtime drift confirmation;
- `git diff --check`, staging, and working-tree state;
- next recipient and implementation status.

## 11. Repository and Git Boundary

Execution must preserve all existing user changes and the dirty worktree. It may not clean, reset, reformat, rename, stage, or overwrite unrelated files.

Required checks:

```text
git diff --check: PASS
Staging Area: EMPTY
New or modified files under litigation-legal/: 0
git add / commit / tag / push / release: NOT PERFORMED
```

## 12. Governance Chain

```text
Route A Design Validation Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator Review
        ↓
Project Owner Validation-Execution Decision
        ↓
Only if approved:
Codex Design Validation Execution
        ↓
Validation Spec + Result + SHA-256
        ↓
Architecture Validation Review
        ↓
Project Owner Validation Closeout Decision
        ↓
Only under a new Handoff:
Decision whether any Route A implementation planning may begin
```

## 13. Current Governance State

```text
Canonical Governance Pattern:
ACTIVE

Route A Design Spec / Result:
PHYSICALLY BOUND

Route A Design Validation Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Route A Validation Execution:
NOT AUTHORIZED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient after materialization is the **Architecture Coordinator (ChatGPT)** for file-level review of the exact physical Validation Handoff SHA-256.
