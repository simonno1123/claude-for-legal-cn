# TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT v1.0 — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION |
| Task Type | Physical Evidence Acquisition Planning Design |
| Route | Phase 2 / Route A |
| Requested Authorization | **DESIGN ONLY** |
| Design Execution | **NOT AUTHORIZED BY MATERIALIZATION** |
| Physical Acquisition Execution | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

Materialization of this Handoff creates the physical authorization-request artifact only. It does not authorize the future Spec/Result, locating or acquiring material, contacting any source, copying files, OCR, evidence processing, legal analysis, or implementation. Design execution requires Architecture Review and a Project Owner decision bound to this physical Handoff SHA-256.

## 1. Task Objective

Define a documentation-only plan for moving approved CASE-A/B/C material categories from physical availability gaps toward a controlled evidence-intake state that could later satisfy the existing Route A Analysis-Ready criteria.

```text
Frozen Physical Material Gap
        ↓
Acquisition Planning Registry
        ↓
Human-Approved Source and Authority Path
        ↓
Material Recovery / Intake Plan
        ↓
Identity and Access Verification Plan
        ↓
Text / OCR Readiness Classification Plan
        ↓
Document and Matter Review Plan
        ↓
Candidate Analysis-Ready Criteria
```

The task creates an authorization and control design. It does not perform acquisition or make any material Analysis Ready.

## 2. Problem Statement

The accepted upstream conclusion is:

```text
Reasoning model failure:
NO

Governance design failure:
NO BLOCKING DESIGN DEFECT IDENTIFIED

Current blocking condition:
PHYSICAL EVIDENCE AVAILABILITY / IDENTITY / READINESS GAP
```

Current frozen profile:

```text
CASE-A: 1 of 4 frozen categories accessible and byte-identity matched
CASE-B: 0 of 5 frozen categories accessible
CASE-C: 0 of 4 frozen categories accessible; matter-label identity requires human confirmation
```

This Handoff must not reinterpret design closure as successful real-case validation or physical-input readiness.

## 3. Fixed Baseline Binding

Before any later design execution, Codex must recompute and exactly match every required SHA-256. A missing or mismatched artifact yields `BLOCKED` and prohibits Physical Evidence Acquisition Spec/Result creation.

### 3.1 Canonical Governance Pattern

| Artifact | Path | SHA-256 |
|---|---|---|
| LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` |

Mandatory boundary:

```text
Evidence
        ≠ Fact
        ≠ Legal Fact
        ≠ Request Right
```

No acquisition or readiness state may bypass LRG-00 through LRG-05.

### 3.2 Route A Evidence Infrastructure Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` |
| Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md` | `DF22B914C0F92073E41B5126DAE5AE7CBE1C442CBCE99798A0488BDE3B97EAFD` |

### 3.3 Route A Design Validation

| Artifact | Path | SHA-256 |
|---|---|---|
| Validation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_HANDOFF.md` | `E55B25CB94D6F5E35D199D575EE8CDF708DA79F89D4CEEC12C2CF88B2070AE27` |
| Validation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md` | `8DBDD4F438BC05DCCA3BAFB6CE4572A4E0FDEDAC1A8303002292CEB6FEC367AB` |
| Validation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md` | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` |

### 3.4 Route A Input Readiness Recovery Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Recovery Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_HANDOFF.md` | `180A160564CAB3A7E58AFFC92F16F595C0F7C95D342CCE281A042485537BDA75` |
| Recovery Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC.md` | `6A9847DE0ABBC6641F904B69B328D6A2DDE6D76B331276521B99935F31AB3CF0` |
| Recovery Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_RESULT.md` | `395B2539E753AACA4E2A0DBDD4AE4276B1C03A92A5CF6CA86D8A4103F4194260` |

The later design may operationalize planning detail only. It may not change any frozen baseline, execute a recovery action, or broaden authorized evidence scope.

## 4. Authorized Design Scope

If separately approved, the future design execution may define only:

1. **Evidence Acquisition Planning** — planning objects, actors, authority checkpoints, dependencies, stop conditions, and target states;
2. **Material Recovery Mapping** — category-to-source-candidate-to-action-to-verification planning;
3. **Missing Evidence Registry** — explicit missing/inaccessible/ambiguous records and blockers;
4. **Case Material Inventory** — a documentation-only inventory derived from frozen inputs, without new scanning or content reading;
5. **Analysis-Ready Criteria Definition** — the existing Route A document and case-bundle gates restated as acquisition-plan completion criteria;
6. **Human Ownership and Approval Matrix** — qualified roles for source authority, matter/entity identity, intake, document review, and legal-use review;
7. **Audit and Invalidation Plan** — planned records for acquisition authority, receipt, version, identity, review, correction, and supersession.

The design may label candidate sources and acquisition actions. It may not assert entitlement, issue a request, or perform any action.

## 5. Required Planning Objects

### 5.1 Physical Evidence Acquisition Plan Record

The future Spec must define a conceptual record containing at minimum:

```text
acquisition_plan_id
recovery_id
matter_id and identity status
entity/source candidates and uncertainty
evidence category
required/optional/unknown designation by qualified human
frozen expected document/version/hash if any
current availability and access state
approved source candidate
source authority basis requiring human confirmation
acquisition owner
candidate acquisition action
action status
purpose and access limits
personal-information/confidentiality constraints
expected delivered format and completeness
intake verification package
text/OCR readiness classification requirement
document review requirement
legal review requirement
target state
blocking reasons
correction/supersession lineage
audit references
```

This is a documentation contract, not a runtime schema or database.

### 5.2 Missing Evidence Registry

Every required, optional, or candidate material category must retain:

- the basis for its category designation;
- whether a qualified human has confirmed it as required for a stated scope;
- expected identity and source, if known;
- current physical availability and access;
- unresolved matter/entity/source identity;
- candidate human-owned recovery action or `NO_ACTION_AUTHORIZED`;
- the next permitted state and explicit blocker;
- non-substitution rules.

No blank field may imply `NOT_FOUND`, `NOT_REQUIRED`, `AUTHORIZED`, or `READY`.

### 5.3 Analysis-Ready Completion Package

The plan must not declare a material or matter ready. It must define what a later qualified-human completion package would require:

```text
Approved matter/purpose/source scope
        +
Acquisition authority and receipt record
        +
Exact file/document/version identity and current hash
        +
Per-source-unit text/OCR coverage
        +
Human source-fidelity review
        +
Qualified-lawyer analytical-use approval
        +
Critical-category case-bundle gate
        +
Audit and invalidation hooks
```

## 6. Source and Acquisition Authority Boundary

The planning design must separate:

```text
Candidate Source
        ≠ Lawful Entitlement to Acquire
        ≠ Actual Acquisition
        ≠ Source Authenticity
        ≠ Admissibility
        ≠ Analysis Readiness
```

Candidate source/action labels may include, subject to separate qualified-human authorization:

```text
APPROVED_MATTER_CUSTODIAN_COPY
AUTHORIZED_CLIENT_OR_PARTY_PROVISION
AUTHORIZED_NATIVE_SYSTEM_EXPORT
LAWFULLY_AUTHORIZED_OFFICIAL_COPY
APPROVED_PUBLIC_RECORD_COPY
AUTHORIZED_BETTER_SCAN_OR_NATIVE_FILE
PER_CHILD_COLLECTION_REGISTRATION
NO_ACTION_AUTHORIZED
```

The design must not claim that a court, bank, registry, platform, company, party, or other custodian is legally required or procedurally available to provide a record. Current China Mainland law, procedure, professional duties, confidentiality, personal-information constraints, and matter-specific authority require qualified-lawyer confirmation before any external step.

## 7. CASE-A — 沐希鞋业 Material Recovery Package

The matter name is a validation/planning identifier only.

### 7.1 Frozen Categories

| Category | Frozen state | Planning requirement |
|---|---|---|
| Corporate/public-record evidence | One PDF accessible and hash-matched in frozen validation | Preserve current identity; plan source, Document Review, and legal-use review; prohibit substitution |
| Transaction evidence | Workbook missing at prior path | Plan approved custodian/source, native-format recovery, path/version rebind, current hash, and spreadsheet-structure review |
| Payment evidence | Not found | Plan source/authority confirmation, bounded receipt, per-file identity, and review |
| Communication evidence | Not found | Plan authorized export/copy, sequence/context/attachment completeness, source attribution, and privacy/confidentiality review |

### 7.2 Candidate Delivery Evidence Category

“Delivery Evidence” appears in the current planning instruction but was not a separately bound category in the frozen thirteen-category validation registry. The future design must record it as:

```text
Category status:
CANDIDATE — PENDING QUALIFIED HUMAN CONFIRMATION

Required for analysis:
UNKNOWN

Acquisition action:
NO ACTION AUTHORIZED UNTIL CATEGORY/SCOPE CONFIRMED
```

The system may not infer delivery, non-delivery, performance, breach, or proof needs from the category label.

### 7.3 CASE-A Package Rule

Corporate/public-record evidence cannot substitute for transaction, payment, communication, or any human-confirmed delivery category. Recovery of one item cannot release the case-bundle gate.

## 8. CASE-B — 塑博坊 Material and Identity Recovery

The matter name is a validation/planning identifier only.

Frozen categories:

- judgment/court document;
- bank-flow or financial record;
- corporate registration records;
- shareholder records;
- enforcement materials.

Required planning controls:

1. confirm stable matter ID, purpose, parties/entity candidates, and approved source scope;
2. define a qualified-human owner for every acquisition authority decision;
3. replace directory-level `Bound Multiple` with per-child identities for relied-upon files;
4. record native/OCR/hybrid/table classification requirements without processing;
5. preserve currentness, version, source, and procedural-context uncertainty;
6. prohibit inference of shareholder role, corporate control, liability, enforcement result, or evidentiary weight.

Frozen planning result:

```text
Accessible categories: 0 / 5
Matter/entity confirmation: REQUIRED BY CURRENT HANDOFF
Physical acquisition: NOT AUTHORIZED
Analysis readiness: BLOCKED
```

## 9. CASE-C — 康尔达 / Historical-Matter Identity Gate

The current “康尔达” label, frozen `C02-CASE-C-001 / 张成棋执行衍生案件` label, and historical filename containing “康尔达” are distinct metadata observations.

Required gate:

```text
Document Identity
        ↓
Source Identity
        ↓
Matter Identity
        ↓
Entity / Party Attribution
        ↓
Purpose and Access Scope
        ↓
Qualified Human Binding Approval
```

Before that gate passes, the only permissible planning action is identity reconciliation. No material acquisition, cross-matter reuse, or analysis may be planned as authorized.

Frozen categories:

- fee-detail workbook;
- property/asset registration;
- enforcement records/logs;
- derivative-litigation materials.

Non-substitution rule: a fee workbook cannot substitute for property, enforcement, transaction, or derivative-litigation sources.

## 10. Planned Acquisition and Intake States

The future Spec must keep acquisition planning and infrastructure readiness independent.

Acquisition planning states:

```text
UNPLANNED
PLANNED
PENDING_AUTHORITY
AUTHORIZED_FOR_ACQUISITION
IN_PROGRESS
RECEIVED_PENDING_INTAKE
COMPLETED_FOR_RECORDED_SCOPE
BLOCKED
CANCELLED
SUPERSEDED
```

Evidence infrastructure states remain controlled by the adopted Route A Design:

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

Prohibited shortcuts:

```text
ACQUISITION_PLANNED → MATERIAL_RECEIVED
MATERIAL_RECEIVED → HASH_VERIFIED
HASH_VERIFIED → AUTHENTIC
TEXT_AVAILABLE → FACT
OCR_COMPLETED → LEGAL_FACT
ONE_RECOVERED_ITEM → CASE_READY
SIMILAR_NAME_OR_PATH → SAME_MATTER
```

## 11. Required Future Spec Structure

If approved, the Physical Evidence Acquisition Spec must include:

1. document control and exact input hashes;
2. objective, terminology, non-goals, and authority boundary;
3. Physical Evidence Acquisition Plan Record;
4. Missing Evidence Registry;
5. source/authority/owner/action matrix;
6. CASE-A/B/C recovery packages;
7. identity, intake, text/OCR classification, and human review gates;
8. Analysis-Ready completion criteria;
9. blockers, non-substitution, correction, supersession, and invalidation;
10. audit and matter-isolation plan;
11. acceptance-criteria assessment;
12. explicit non-execution and implementation boundary.

## 12. Authorized Future Outputs

Only after Architecture Review and a Project Owner decision bound to this physical Handoff SHA may Codex create exactly two files.

### Output A — Physical Evidence Acquisition Design Spec

```text
docs/phase2/route-a/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_SPEC.md
```

### Output B — Physical Evidence Acquisition Design Result

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_RESULT.md
```

Materialization of this Handoff does not authorize either output.

## 13. Acceptance Criteria

### PEA-001 — Evidence Recovery Registry Complete

PASS when all frozen and human-confirmed candidate categories have explicit identity, source, authority, owner, action, target, blocker, review, and lineage fields.

### PEA-002 — CASE-A/B/C Material Gaps Classified

PASS when every category is classified as available, missing, inaccessible, identity-ambiguous, authority-pending, processing-unready, review-pending, or ready only within an explicit limited scope without inventing content.

### PEA-003 — Recovery Source and Responsibility Paths Clear

PASS when every candidate source/action has a qualified-human authority owner, limits, required verification package, and next controlled state, while no entitlement or external action is claimed.

### PEA-004 — Identity Gate Effective

PASS when file, source, matter, entity, purpose, and approval remain separate and any failed/unknown level returns `BLOCKED`.

### PEA-005 — No Legal Reasoning Conclusion

PASS when the design generates no evidence-validity, Legal Fact, request-right, burden, strategy, outcome, or probability conclusion.

### PEA-006 — Zero Engineering Pollution

PASS when only the two authorized documentation outputs are created in a later approved design execution and no code, Skill, Agent, MCP, Workflow, runtime schema, OCR, database, RAG, or deployment asset changes.

## 14. Strict Forbidden Scope

```text
Physical Material Acquisition or External Contact: NOT AUTHORIZED
File Copy / Move / Download / Upload / Conversion: NOT AUTHORIZED
New Case Content Reading or Extraction: NOT AUTHORIZED
OCR Engine Development or Selection: NOT AUTHORIZED
OCR Processing or Transcription: NOT AUTHORIZED
Database / Object Store: NOT AUTHORIZED
MCP Integration: NOT AUTHORIZED
Agent Development or Modification: NOT AUTHORIZED
Skill Modification: NOT AUTHORIZED
Workflow Modification: NOT AUTHORIZED
Runtime Schema Modification: NOT AUTHORIZED
Code or Test Script Creation: NOT AUTHORIZED
RAG / Vector Store: NOT AUTHORIZED
Production Deployment: NOT AUTHORIZED
Legal Reasoning Generation: NOT AUTHORIZED
Route A Implementation: NOT AUTHORIZED
Route B: FROZEN / NOT AUTHORIZED
```

Also prohibited:

- representing a candidate source as a lawful entitlement or guaranteed recovery path;
- contacting parties, clients, custodians, banks, courts, registries, platforms, providers, or authorities;
- determining authenticity, admissibility, credibility, weight, or sufficiency;
- inferring facts from names, paths, filenames, counts, category labels, or prior summaries;
- modifying canonical Governance Pattern, Route A Design, Validation, or Recovery assets;
- git add, commit, tag, push, release, or publication.

## 15. Required Future Result Record

The future Result must record:

- this Handoff and all input hashes;
- Physical Evidence Acquisition Spec hash;
- each acceptance criterion and supporting section;
- CASE-A/B/C planning coverage and unresolved gaps;
- any new candidate category and its human-confirmation status;
- exact created/modified file list;
- explicit confirmation that no physical acquisition occurred;
- zero implementation/runtime drift confirmation;
- `git diff --check`, staging, and working-tree state;
- next governance recipient and implementation status.

## 16. Repository and Git Boundary

Execution must preserve all existing user changes and the dirty worktree. It may not clean, reset, reformat, rename, stage, or overwrite unrelated files.

Required future checks:

```text
git diff --check: PASS
Staging Area: EMPTY
New or modified files under litigation-legal/: 0
git add / commit / tag / push / release: NOT PERFORMED
```

## 17. Governance Chain

```text
Physical Evidence Acquisition Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator File-Level Review
        ↓
Project Owner Decision Bound to Physical SHA
        ↓
Only if approved:
Codex Physical Evidence Acquisition Design Execution
        ↓
Design Spec + Result + SHA-256
        ↓
Architecture Review
        ↓
Project Owner Design Closeout Decision
        ↓
Only under a new authorization:
Decision whether any physical acquisition operation may be planned or executed
```

## 18. Current Governance State

```text
Canonical Governance Pattern:
ACTIVE

Route A Evidence Infrastructure Design:
CLOSED

Route A Design Validation:
CLOSED

Route A Input Readiness Recovery Design:
PHYSICALLY BOUND

Physical Evidence Acquisition Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Physical Evidence Acquisition Design Execution:
NOT AUTHORIZED

Physical Acquisition Operation:
NOT AUTHORIZED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient after materialization is the **Architecture Coordinator (ChatGPT)** for review of the exact physical Handoff SHA-256.
