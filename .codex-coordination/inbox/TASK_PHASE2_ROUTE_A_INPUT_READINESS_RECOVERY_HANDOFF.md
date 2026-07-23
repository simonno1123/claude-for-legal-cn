# TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT v1.0 — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY |
| Task Type | Evidence Input Readiness Recovery Design |
| Route | Phase 2 / Route A |
| Requested Authorization | **DESIGN ONLY** |
| Design Execution | **NOT AUTHORIZED BY MATERIALIZATION** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

Materialization of this Handoff creates the physical authorization-request artifact and fixes its proposed input and output identities. It does not authorize creation of the Recovery Spec or Result. Design execution requires file-level Architecture Review and a Project Owner decision bound to this physical Handoff SHA-256.

## 1. Task Objective

Design an Input Readiness Recovery control layer between physical evidence and the already adopted Route A Evidence Infrastructure Design.

The design question is:

> How should missing, inaccessible, identity-ambiguous, text-unready, OCR-dependent, or human-unverified material be recovered to a controlled readiness state without generating evidence content or legal reasoning?

Target relationship:

```text
Physical Evidence or Explicit Material Gap
        ↓
Evidence Recovery Registry
        ↓
Material Acquisition Map
        ↓
Identity Recovery Gate
        ↓
Text / OCR Readiness Classification
        ↓
Document and Matter Human Review
        ↓
Analysis-Ready Candidate Input
        ↓
Separately governed legal reasoning
```

The task closes a design gap only. It does not restore files, perform acquisition, execute OCR, verify evidence, create a runtime registry, or authorize legal analysis.

## 2. Fixed Baseline Binding

Before any design execution, Codex must recompute and exactly match every SHA-256 below. A missing or mismatched artifact yields `BLOCKED` and prohibits Recovery Spec/Result creation.

### 2.1 Canonical Governance Pattern

| Artifact | Path | SHA-256 |
|---|---|---|
| LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` |

Mandatory invariant:

```text
Raw Evidence
        ↓
Extracted Evidence Candidate
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Candidate
        ↓
Request Right Candidate
        ↓
Qualified Human Decision
```

No recovery state may bypass LRG-00, LRG-01, LRG-02, LRG-04, or LRG-05.

### 2.2 Route A Evidence Infrastructure Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` |
| Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md` | `DF22B914C0F92073E41B5126DAE5AE7CBE1C442CBCE99798A0488BDE3B97EAFD` |

The Recovery design may extend documentation for physical-input recovery controls. It may not modify, reinterpret, or replace the Route A Evidence Object, lifecycle, review gates, Analysis-Ready Manifest, or implementation boundary.

### 2.3 Route A Design Validation

| Artifact | Path | SHA-256 |
|---|---|---|
| Validation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_HANDOFF.md` | `E55B25CB94D6F5E35D199D575EE8CDF708DA79F89D4CEEC12C2CF88B2070AE27` |
| Validation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md` | `8DBDD4F438BC05DCCA3BAFB6CE4572A4E0FDEDAC1A8303002292CEB6FEC367AB` |
| Validation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md` | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` |

Frozen validation conclusion:

```text
Route A design compatibility:
SUPPORTED

Current material readiness:
CASE-A  PARTIAL / LEGAL REASONING BLOCKED
CASE-B  BLOCKED
CASE-C  BLOCKED

Route A implementation:
NOT AUTHORIZED
```

This task must preserve the distinction between a validated design and unavailable physical inputs.

## 3. Design Scope

### 3.1 Evidence Recovery Registry

Define a documentation-level recovery record containing at minimum:

```text
recovery_id
matter_id
evidence_category
expected_document_id and version
expected path/object reference
expected hash and size
current location/access state
current hash state
source or custodian candidate
acquisition authority and method candidate
file/document type
text-layer state
OCR-readiness class
human-review state
identity ambiguity
blocking reasons
recovery action
responsible human owner
target state
correction/supersession lineage
audit references
```

This is a conceptual documentation contract, not a runtime schema or database.

### 3.2 Material Acquisition Map

Define a traceable planning map:

```text
Required Evidence Category
        ↓
Current Availability and Identity State
        ↓
Approved Source / Custodian Candidate
        ↓
Authorized Recovery Action
        ↓
Verification and Human Review Requirements
        ↓
Expected Recovery State or Explicit Blocker
```

The map may propose documentation-level actions such as locate, request authorized copy, rebind path, recompute hash, register per-child files, obtain better scan/export, classify OCR need, assign review, or confirm matter identity. It may not perform those actions or contact any person or system.

### 3.3 Identity Recovery Gate

Design independent identity checks:

```text
File / Byte Identity
        ↓
Source / Acquisition Identity
        ↓
Matter Identity
        ↓
Entity / Party Attribution
        ↓
Qualified Human Confirmation
```

Mandatory constraints:

- filename, directory, path, party label, matter label, or similar wording is not identity proof;
- a matching hash establishes same-byte identity only;
- a directory-level `Bound Multiple` record cannot replace per-child identities;
- restored bytes do not inherit old access, review, or readiness automatically;
- CASE-C label drift must remain blocked until the qualified matter owner confirms the matter ID, scope, and intended use;
- absence at an approved path does not prove that material does not exist elsewhere.

### 3.4 OCR and Text Readiness Classification

Define provider-neutral classification only:

```text
TEXT_AVAILABLE_COMPLETE
TEXT_AVAILABLE_PARTIAL
OCR_REQUIRED
IMAGE_ONLY
HYBRID_TEXT_IMAGE
UNREADABLE_OR_CORRUPT
MANUAL_REVIEW_REQUIRED
HUMAN_REVIEW_REQUIRED
NOT_APPLICABLE
```

Classification must identify page, region, sheet, range, message, attachment, or other applicable source-unit scope. It must not run OCR, transcribe content, choose an engine, or convert OCR confidence into fact support.

### 3.5 Recovery State Model

Define controlled recovery progression without collapsing independent states:

```text
MISSING / UNKNOWN
        ↓
LOCATED
        ↓
ACCESS_AUTHORIZED
        ↓
ACCESSIBLE
        ↓
FILE_IDENTITY_VERIFIED
        ↓
MATTER_AND_SOURCE_IDENTITY_CONFIRMED
        ↓
TEXT_ROUTE_CLASSIFIED
        ↓
TEXT_OR_OCR_OUTPUT_HUMAN_VERIFIED
        ↓
DOCUMENT_REVIEW_COMPLETED
        ↓
LEGAL_FACT_REVIEW_COMPLETED
        ↓
ANALYSIS_READY FOR RECORDED SCOPE
```

At any stage:

```text
BLOCKED | DENIED | QUARANTINED | REJECTED | SUPERSEDED | REVOKED
```

`LOCATED`, `ACCESSIBLE`, `HASH_VERIFIED`, `TEXT_READY`, or `HUMAN_VERIFIED` alone never means evidence authenticity, admissibility, truth, Legal Fact support, or request-right support.

### 3.6 Human Review Boundary

The design must preserve separate decisions for:

1. recovery authority and permitted source acquisition;
2. matter and entity identity;
3. file identity and version;
4. extraction/OCR fidelity;
5. evidence use, confidentiality, and scope;
6. Legal Fact promotion and legal reasoning.

Silence, missing review, a technical status, or a prior approval for another version/scope is never current approval.

## 4. CASE-A/B/C Recovery Design Profiles

The profiles below are input-recovery planning identifiers only. They do not authorize new case-fact extraction or legal analysis.

### 4.1 CASE-A — Commercial Transaction Materials

Recovery categories:

- transaction bill/account workbook;
- company/public-record PDF;
- WeChat or other correspondence records;
- payment vouchers.

Frozen state:

```text
1 of 4 categories accessible and hash-matched
3 of 4 categories unavailable
Infrastructure descriptor: PARTIAL
Affected legal reasoning: BLOCKED
```

The design must specify re-location/rebinding, spreadsheet structure preservation, correspondence completeness/source controls, payment-source acquisition planning, and both human review gates. The accessible public-record PDF cannot substitute for the three unavailable categories.

### 4.2 CASE-B — Litigation and Corporate Records

Recovery categories:

- judgment/court document;
- bank-flow or financial record;
- corporate registration records;
- shareholder records;
- enforcement materials.

Frozen state:

```text
0 of 5 categories accessible
Prior corporate-record directory entry lacked current per-child identity
Infrastructure descriptor: BLOCKED
```

The design must require per-file registration, current hashes, source/custodian records, text/OCR classification, and explicit rejection of prior counts or filenames as current evidence.

### 4.3 CASE-C — Property, Cost, and Enforcement-Derivative Materials

Recovery categories:

- fee-detail workbook;
- property/asset registration;
- enforcement records/logs;
- derivative-litigation materials.

Frozen state:

```text
0 of 4 categories accessible
Current “康尔达” validation label and frozen matter label require reconciliation
Infrastructure descriptor: BLOCKED
```

The design must require matter-identity confirmation before acquisition or use, preserve spreadsheet structure, and prohibit any substitution of fee material for property, enforcement, transaction, or derivative-litigation sources.

## 5. Required Recovery Scenarios

The Design Spec must address at minimum:

| Scenario | Required design response |
|---|---|
| File missing at approved path | Preserve expected identity, identify authorized locate/request action, remain `BLOCKED` |
| File located at a new path | Verify authority, recompute hash and size, record new locator/version; do not inherit readiness |
| Same filename, different bytes | Create new version or quarantine mismatch; invalidate dependent records |
| Same bytes, different source | Preserve separate acquisition/source/use record and matter authorization |
| Directory restored | Register every relied-upon child file separately |
| Text-complete PDF | Classify native-text route; extraction and human review still required |
| Partial/hybrid PDF | Classify exact missing regions for OCR/manual route |
| Scan/image/table/message | Preserve layout/sequence/region structure and human-verification requirements |
| OCR unavailable or unreliable | Record recovery blocker or approved manual path; do not invent text |
| Matter/entity label conflict | Stop before acquisition/use until qualified-human identity confirmation |
| Access revoked or scope changed | Reopen recovery and invalidate dependent readiness |
| New adverse/conflicting source | Reopen bundle and Legal Fact review before analytical use |

## 6. Required Spec Structure

The Recovery Spec, if separately authorized, must contain:

1. document control and exact input hashes;
2. objective, non-goals, and controlled terminology;
3. Evidence Recovery Registry;
4. Material Acquisition Map;
5. Identity Recovery Gate;
6. OCR/text-readiness classification;
7. recovery lifecycle, blockers, corrections, and supersession;
8. CASE-A/B/C recovery mappings;
9. human review and matter-isolation controls;
10. Governance Pattern and Route A conformance;
11. acceptance-criteria assessment;
12. implementation boundary and next governance action.

## 7. Authorized Outputs

Only after Architecture Review and a Project Owner decision bound to this physical Handoff SHA may Codex create exactly two files.

### Output A — Recovery Design Spec

```text
docs/phase2/route-a/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC.md
```

### Output B — Recovery Design Result

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_RESULT.md
```

Materialization of this Handoff does not authorize either output.

## 8. Acceptance Criteria

### INPUT-RECOVERY-001 — Evidence Recovery Registry Complete

PASS when the design covers identity, source, location, access, hash, type, text/OCR, reviews, blockers, actions, ownership, target state, and lineage without defining a runtime schema.

### INPUT-RECOVERY-002 — Material Acquisition Map Complete

PASS when every frozen CASE-A/B/C category maps from current availability through an authorized human-owned recovery action to an explicit expected state or blocker.

### INPUT-RECOVERY-003 — OCR Need Classification Complete

PASS when native, partial, hybrid, image-only, unreadable, table/message, OCR-required, and manual/human-review cases are classified without OCR execution or provider selection.

### INPUT-RECOVERY-004 — Identity Ambiguity Isolated

PASS when file, source, matter, and entity identity remain separate and label/path/hash similarities cannot authorize cross-matter or analytical use.

### INPUT-RECOVERY-005 — No Legal Reasoning Generated

PASS when the design contains no evidence-validity, Legal Fact, request-right, burden, strategy, outcome, or probability conclusion.

### INPUT-RECOVERY-006 — Zero Implementation Pollution

PASS when only the two authorized documentation outputs are created during a later authorized execution and no code, Skill, Agent, MCP, Workflow, runtime schema, OCR, database, RAG, or deployment asset changes.

## 9. Strict Forbidden Scope

```text
OCR Implementation or Execution: NOT AUTHORIZED
OCR Engine Development or Selection: NOT AUTHORIZED
Database / Object Store Construction: NOT AUTHORIZED
MCP Integration: NOT AUTHORIZED
Agent Development or Modification: NOT AUTHORIZED
Skill Modification: NOT AUTHORIZED
Workflow Modification: NOT AUTHORIZED
Runtime Schema Modification: NOT AUTHORIZED
Code / Test Script Creation or Modification: NOT AUTHORIZED
RAG / Vector Store: NOT AUTHORIZED
Production Pipeline or Deployment: NOT AUTHORIZED
Legal Reasoning Generation: NOT AUTHORIZED
Route A Implementation: NOT AUTHORIZED
Route B: FROZEN / NOT AUTHORIZED
```

Also prohibited:

- contacting custodians, parties, courts, providers, or external systems;
- copying, moving, renaming, reconstructing, or generating case materials;
- reading new substantive case content;
- running OCR, extraction, transcription, or file conversion;
- determining authenticity, admissibility, credibility, weight, or sufficiency;
- producing Legal Facts, request rights, burdens, defenses, strategies, outcomes, or probabilities;
- modifying canonical Governance Pattern, Route A Design, or Route A Validation assets;
- git add, commit, tag, push, release, or publication.

## 10. Required Result Record

The later Result must record:

- this Handoff and every input hash;
- Recovery Spec hash;
- each acceptance criterion and supporting section;
- CASE-A/B/C recovery-design summary;
- unresolved physical, identity, access, OCR, and human-review gaps;
- exact created/modified file list;
- zero implementation/runtime drift confirmation;
- `git diff --check`, staging, and working-tree state;
- next governance recipient and implementation status.

## 11. Repository and Git Boundary

Execution must preserve all existing user changes and the dirty worktree. It may not clean, reset, reformat, rename, stage, or overwrite unrelated files.

Required later checks:

```text
git diff --check: PASS
Staging Area: EMPTY
New or modified files under litigation-legal/: 0
git add / commit / tag / push / release: NOT PERFORMED
```

## 12. Governance Chain

```text
Recovery Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator File-Level Review
        ↓
Project Owner Decision Bound to Physical SHA
        ↓
Only if approved:
Codex Recovery Design Execution
        ↓
Recovery Spec + Result + SHA-256
        ↓
Architecture Review
        ↓
Project Owner Closeout Decision
```

No stage in this chain authorizes Route A implementation unless a new implementation Handoff is separately approved.

## 13. Current Governance State

```text
Canonical Governance Pattern:
ACTIVE

Route A Evidence Infrastructure Design:
CLOSED

Route A Design Validation:
CLOSED

Route A Input Readiness Recovery Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Recovery Design Execution:
NOT AUTHORIZED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient after materialization is the **Architecture Coordinator (ChatGPT)** for review of the exact physical Handoff SHA-256.
