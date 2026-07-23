# TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Route | Phase 2 / Route A |
| Task | Physical Evidence Acquisition Design |
| Version | v1.0 design execution artifact |
| Execution date | 2026-07-22 |
| Status | **DONE — DESIGN ONLY** |
| Approved Handoff SHA-256 | `906D8062C5463DC38116FE6BC3C176C8E310551A605CBADADE34A2B11D28FE77` |
| Execution authority | Project Owner approval in the current coordination record |
| Physical acquisition | **NOT PERFORMED / NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

This specification defines a documentation-only Physical Evidence Acquisition Plan. It does not contact a source, assert entitlement, request or receive records, copy or move files, scan the filesystem, run OCR, read new case content, create a database, or perform legal reasoning.

## 1. Exact Input Binding

All required artifacts were present and byte-identical before output creation.

| Input | Path | Expected and actual SHA-256 | Result |
|---|---|---|---|
| Acquisition Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_HANDOFF.md` | `906D8062C5463DC38116FE6BC3C176C8E310551A605CBADADE34A2B11D28FE77` | PASS |
| Canonical Governance Pattern | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | PASS |
| Route A Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` | PASS |
| Route A Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md` | `DF22B914C0F92073E41B5126DAE5AE7CBE1C442CBCE99798A0488BDE3B97EAFD` | PASS |
| Route A Validation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_HANDOFF.md` | `E55B25CB94D6F5E35D199D575EE8CDF708DA79F89D4CEEC12C2CF88B2070AE27` | PASS |
| Route A Validation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md` | `8DBDD4F438BC05DCCA3BAFB6CE4572A4E0FDEDAC1A8303002292CEB6FEC367AB` | PASS |
| Route A Validation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md` | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` | PASS |
| Input Readiness Recovery Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_HANDOFF.md` | `180A160564CAB3A7E58AFFC92F16F595C0F7C95D342CCE281A042485537BDA75` | PASS |
| Input Readiness Recovery Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC.md` | `6A9847DE0ABBC6641F904B69B328D6A2DDE6D76B331276521B99935F31AB3CF0` | PASS |
| Input Readiness Recovery Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_RESULT.md` | `395B2539E753AACA4E2A0DBDD4AE4276B1C03A92A5CF6CA86D8A4103F4194260` | PASS |

## 2. Objective, Interpretation, and Non-Goals

### 2.1 Objective

Convert the frozen CASE-A/B/C material gaps into explicit, human-owned acquisition plans with named candidate source classes, authority checkpoints, verification packages, and stop conditions.

```text
Existing Evidence Gap
        ↓
Acquisition Plan
        ↓
Qualified-Human Authority Decision
        ↓
Later Material Receipt and Intake
        ↓
Identity / Text / Review Verification
        ↓
Analysis-Ready Decision or BLOCKED
```

### 2.2 Interpretation Rules

- “Acquisition” in this Spec means **acquisition planning**, not execution.
- “Real source” means a named real-world source class or custodian candidate, not a verified accessible source or legal entitlement.
- “Required material” means required only for a recorded, human-approved analysis scope.
- frozen validation categories remain separate from newly proposed candidate categories.
- current status derives from frozen upstream artifacts; no new material scan was performed.
- recovery completion, hash verification, or text readiness never establishes authenticity, admissibility, truth, proof, or legal support.

### 2.3 Non-Goals

This design does not:

- contact a client, party, custodian, bank, court, registry, platform, provider, or authority;
- draft or issue a request, application, investigation order, subpoena-like instrument, authorization letter, or collection instruction;
- determine whether a person has a legal right or procedural route to obtain a record;
- receive, copy, download, upload, move, rename, convert, OCR, transcribe, parse, or inspect new materials;
- determine facts, Legal Facts, request rights, burdens, defenses, strategy, outcomes, or probabilities;
- authorize a database, storage system, MCP, Skill, Agent, Workflow, runtime schema, code, RAG, or deployment.

## 3. Evidence Acquisition Registry

The following is a conceptual design contract, not a runtime schema.

### 3.1 Acquisition Plan Record

```yaml
PhysicalEvidenceAcquisitionPlan:
  acquisition_plan_id: stable planning identity
  recovery_id: link to the Input Readiness Recovery record
  matter_id: approved matter identity or explicit UNKNOWN
  matter_identity_status: independent identity state
  entity_id_candidates: candidate parties, custodians, or source entities
  entity_identity_status: independent attribution state
  evidence_category: material category
  category_basis: FROZEN_PROFILE | CURRENT_INSTRUCTION_CANDIDATE | HUMAN_APPROVED
  requiredness: REQUIRED_FOR_SCOPE | OPTIONAL | CANDIDATE | UNKNOWN
  declared_analysis_scope: bounded human-approved purpose
  current_availability: current frozen availability descriptor
  missing_reason: explicit physical, access, identity, or readiness gap
  expected_document_id: prior identity if any
  expected_version: prior version if any
  expected_sha256: prior byte identity if any
  prior_location: previously approved locator if any
  candidate_source_class: named source/custodian class with uncertainty
  source_identity_status: independent source state
  acquisition_authority_owner: qualified human decision owner
  authority_status: NOT_ASSESSED | PENDING | APPROVED_FOR_PLANNING | REJECTED
  candidate_action: non-executing planning label
  action_status: UNPLANNED | PLANNED | PENDING_AUTHORITY | BLOCKED
  purpose_and_access_limits: matter, actor, time, confidentiality, and use scope
  expected_delivery_format: native file, official copy, export, image, paper, or UNKNOWN
  expected_completeness: source-unit and attachment expectations
  verification_requirements: intake, hash, source, matter, text/OCR, and review checks
  acquisition_owner: accountable human role
  intake_owner: accountable registry/review role
  target_state: next controlled state only
  blockers: explicit stop reasons
  non_substitution_rules: categories this material cannot replace
  correction_and_supersession: version lineage
  audit_references: authority, action, receipt, verification, and review records
```

### 3.2 Registry Rules

- every category has an explicit basis and requiredness status;
- newly proposed categories remain `CANDIDATE` until a qualified human confirms scope and necessity;
- the source class, authority owner, acquisition owner, next state, and blocker are mandatory;
- `UNKNOWN`, `NOT_ASSESSED`, `NOT_AVAILABLE`, and `NO_ACTION_AUTHORIZED` are first-class values;
- a source class does not prove a particular source currently holds the material;
- an approved plan does not authorize execution;
- a received item starts the existing Route A intake lifecycle and does not inherit analysis readiness.

## 4. Planning States and Controlled Transitions

### 4.1 Acquisition Planning States

```text
UNPLANNED
        ↓
GAP_CLASSIFIED
        ↓
SOURCE_CANDIDATE_IDENTIFIED
        ↓
AUTHORITY_REVIEW_PENDING
        ↓
PLAN_APPROVED_FOR_RECORDED_SCOPE
        ↓
EXECUTION_NOT_AUTHORIZED
```

This design task stops at `PLAN_APPROVED_FOR_RECORDED_SCOPE`. It does not authorize any acquisition-operation state.

Future operational states, if separately authorized, would remain distinct:

```text
ACQUISITION_AUTHORIZED
IN_PROGRESS
RECEIVED_PENDING_INTAKE
REGISTERED
HASH_VERIFIED
TEXT_ASSESSED
DOCUMENT_REVIEWED
LEGAL_FACT_REVIEWED
ANALYSIS_READY FOR RECORDED SCOPE
```

### 4.2 Fail-Closed States

```text
BLOCKED
DENIED
CANCELLED
QUARANTINED
REJECTED
REVOKED
SUPERSEDED
```

### 4.3 Prohibited Shortcuts

```text
PLAN_APPROVED → ACQUISITION_EXECUTED
SOURCE_CANDIDATE → ENTITLEMENT_TO_ACQUIRE
RECEIVED → VERIFIED
HASH_VERIFIED → AUTHENTIC
TEXT_AVAILABLE → FACT
OCR_COMPLETED → LEGAL_FACT
ONE_READY_FILE → CASE_READY
SIMILAR_FILENAME_OR_ENTITY → SAME_MATTER
```

## 5. Source, Responsibility, and Authority Matrix

All rows describe source classes and human-owned planning paths. They do not assert actual availability or legal entitlement.

| Material class | Candidate real-world source classes | Authority decision owner | Expected verification package | Initial target state |
|---|---|---|---|---|
| Corporate/public registration | Approved official/public record source, authorized company copy, prior matter custodian | Qualified lawyer plus approved access owner | Current source/time, file/version, acquisition record, hash, scope, review | `RECEIVED_PENDING_INTAKE` |
| Legal-representative or entity-role record | Approved current corporate/public record or authorized source document | Qualified lawyer | Effective date, entity identity, source, currentness, limitations | `SOURCE_IDENTITY_DOCUMENTED` |
| Business-person identity/authority | Authorized employer/client/party record, approved correspondence/source package | Qualified lawyer / matter owner | Person/entity attribution, time, role evidence, source limits, conflict record | `ENTITY_IDENTITY_CANDIDATE_REVIEW` |
| Contract/agreement | Approved party/custodian native copy, authorized archive | Qualified lawyer / matter owner | Complete version, signatures/seals preserved as images, attachments, amendments, source and hash | `FILE_IDENTITY_VERIFIED` |
| Order/instruction | Approved transaction system export, authorized party/custodian copy | Qualified lawyer / matter owner | Order ID, time, parties/source, item/amount fields, attachments, hash and completeness | `FILE_IDENTITY_VERIFIED` |
| Reconciliation/account statement | Approved native workbook/export, authorized party/custodian copy | Qualified lawyer / matter owner | Workbook/sheet/range identity, formulas/display values, units, signs, dates, source, hash | `FILE_IDENTITY_VERIFIED` |
| Communication/WeChat record | Authorized participant/custodian native export or bounded source copy | Qualified lawyer plus privacy/confidentiality owner | Source device/account, participants, sequence, timestamps, attachments, truncation, hash, review scope | `RECEIVED_PENDING_INTAKE` |
| Delivery/receipt material | Approved carrier/warehouse/party/custodian record where category is human-confirmed | Qualified lawyer / matter owner | Record type, source, time, parties, item/quantity fields, signature/image limitations, hash | `RECEIVED_PENDING_INTAKE` |
| Bank-flow record | Authorized account holder or other source only after qualified legal/access approval | Qualified lawyer / approved account-access owner | Native/official record, account/source attribution, period, table structure, version, hash, access limits | `RECEIVED_PENDING_INTAKE` |
| Digital-payment record | Authorized account holder/platform export or other approved source | Qualified lawyer plus privacy/access owner | Account/source attribution, transaction identifiers, time, amount/currency, completeness, hash | `RECEIVED_PENDING_INTAKE` |
| Judgment/court document | Approved official/public source or authorized matter copy | Qualified lawyer | Court/document identity, version, effective/current status requiring legal review, complete pages, hash | `FILE_IDENTITY_VERIFIED` |
| Corporate/shareholder collection | Approved registry/company/court-file source | Qualified lawyer / access owner | Per-child file identity, source date, entity scope, version, hash, completeness | `REGISTERED_PER_CHILD` |
| Enforcement material | Approved court/party/counsel source within authorized matter scope | Qualified lawyer | Procedural/source identity, date/version, full record scope, attachments, hash, limitations | `RECEIVED_PENDING_INTAKE` |
| Property/asset registration | Approved official/party source only after qualified authority decision | Qualified lawyer / access owner | Subject/property identity, source/time/version, permitted use, hash, limitations | `RECEIVED_PENDING_INTAKE` |
| Derivative-litigation material | Approved court/party/counsel source within confirmed matter relationship | Qualified lawyer | Matter linkage, document/source identity, version, complete set, hash, access scope | `RECEIVED_PENDING_INTAKE` |

If an authority owner cannot approve the source or method, the acquisition plan result is `BLOCKED`, not an alternate automated route.

## 6. Intake Verification Requirements

### 6.1 Receipt Package

Every later received item would require:

- approved acquisition-plan ID and authority record;
- matter, purpose, source, custodian, and receiving actor;
- receipt date/time and acquisition method;
- original filename/type and delivered container/attachment relationships;
- current byte size and SHA-256;
- original or copy/export/scan/screenshot/transcription designation;
- access, confidentiality, personal-information, and permitted-use limits;
- expected-versus-received completeness and variance record.

### 6.2 File and Source Identity

```text
Delivered Bytes
        ↓
File / Version Identity
        ↓
Source / Acquisition Identity
        ↓
Matter Identity
        ↓
Entity / Party Attribution
        ↓
Qualified Human Binding Approval
```

Any unknown or failed gate yields `BLOCKED` for the affected scope.

### 6.3 Text and OCR Classification

Every received source requires provider-neutral classification only:

```text
TEXT_AVAILABLE_COMPLETE
TEXT_AVAILABLE_PARTIAL
OCR_REQUIRED
IMAGE_ONLY
HYBRID_TEXT_IMAGE
UNREADABLE_OR_CORRUPT
MANUAL_TRANSCRIPTION_CANDIDATE
HUMAN_REVIEW_REQUIRED
NOT_APPLICABLE
```

This Spec does not run OCR or select a provider.

### 6.4 Human Review

Document Review confirms source fidelity, extraction completeness, locators, corrections, and limitations. A separate qualified-lawyer Legal Fact Review decides limited analytical use. Neither gate establishes final truth, admissibility, proof sufficiency, request rights, or outcome.

## 7. CASE-A Acquisition Package

The matter name “沐希鞋业” is a planning identifier only.

### 7.1 Frozen and Candidate Category Matrix

| ID | Layer | Category | Basis | Frozen current state | Candidate source path | Requiredness | Plan result |
|---|---|---|---|---|---|---|---|
| A-P01 | Subject | Corporate/public registration | Frozen profile | One company-report PDF accessible and hash-matched | Approved current public/official record or authorized matter copy | Required for frozen identity scope only | Preserve identity; source and reviews pending |
| A-P02 | Subject | Legal-representative information | Current-instruction candidate | Not independently bound | Approved current corporate/public record | `CANDIDATE` | Human confirmation required |
| A-P03 | Subject | Business-person identity/authority | Current-instruction candidate | Not independently bound | Authorized employer/client/party records and bounded correspondence | `CANDIDATE` | Human confirmation required |
| A-P04 | Transaction | Contract/agreement | Current-instruction candidate | Not independently bound | Approved party/custodian native copy or archive | `CANDIDATE` | Human confirmation required |
| A-P05 | Transaction | Orders/instructions | Current-instruction candidate | Not independently bound | Approved transaction system/party/custodian source | `CANDIDATE` | Human confirmation required |
| A-P06 | Transaction | Reconciliation/account workbook | Frozen profile | Missing at prior path; expected hash retained | Approved custodian native workbook/export | Required for frozen validation scope | Recovery plan defined; execution unauthorized |
| A-P07 | Transaction | WeChat/communication record | Frozen profile | Not found | Authorized participant/custodian native export or bounded copy | Required for frozen validation scope | Recovery plan defined; execution unauthorized |
| A-P08 | Transaction | Delivery/receipt material | Current-instruction candidate | Not independently bound | Approved carrier/warehouse/party/custodian record | `CANDIDATE` | Human confirmation required |
| A-P09 | Payment | Bank-flow record | Current-instruction candidate | Not independently bound | Authorized account holder/approved source after legal/access review | `CANDIDATE` | Human confirmation required |
| A-P10 | Payment | Digital/WeChat payment record | Current-instruction candidate | Not independently bound | Authorized account holder/platform export or approved source | `CANDIDATE` | Human confirmation required |
| A-P11 | Payment | Payment vouchers/other payment source | Frozen profile | Not found | Authorized holder/source within approved matter scope | Required for frozen validation scope | Recovery plan defined; execution unauthorized |

### 7.2 CASE-A Package Gate

```text
Current frozen infrastructure state:
PARTIAL

New candidate categories:
7 — PENDING QUALIFIED HUMAN CONFIRMATION

Current legal reasoning:
BLOCKED

Physical acquisition:
NOT AUTHORIZED / NOT PERFORMED
```

No corporate record can substitute for transaction, communication, delivery, or payment categories. No category label establishes a transaction fact, performance, breach, amount, payment, or request right.

## 8. CASE-B Acquisition Package

The matter name “塑博坊” is a planning identifier only.

| ID | Category | Frozen state | Candidate source path | Identity/verification requirement | Plan result |
|---|---|---|---|---|---|
| B-P01 | Judgment/court document | Missing at prior path | Approved official/public source or authorized matter copy | Court/document identity, version, complete pages, hash, legal review | Plan defined; execution unauthorized |
| B-P02 | Bank-flow/financial record | Missing at prior path | Authorized account holder/approved source after legal/access review | Source/account/period, table structure, version, hash | Plan defined; execution unauthorized |
| B-P03 | Corporate registration collection | Prior directory unavailable; no current per-child identity | Approved registry/company/court-file source | Per-child path/version/hash/type/source/currentness | Plan defined; execution unauthorized |
| B-P04 | Shareholder record | No independently bound file | Approved registry/company/court-file source | Entity/time/source/version/per-file identity | Plan defined; execution unauthorized |
| B-P05 | Enforcement material | Not found | Approved court/party/counsel source | Matter/procedural/source identity, complete set, version, hash | Plan defined; execution unauthorized |

Before any acquisition operation, a qualified human must confirm the stable matter ID, entity candidates, purpose, approved source scope, and authority owner. Filenames, directory names, historical counts, or similar entity names cannot bind material to the matter.

```text
Current infrastructure state:
BLOCKED

Physical acquisition:
NOT AUTHORIZED / NOT PERFORMED
```

## 9. CASE-C Acquisition Package

The current “康尔达” label, frozen `C02-CASE-C-001 / 张成棋执行衍生案件` label, and a historical filename containing “康尔达” remain unbound metadata observations.

### 9.1 Identity-First Rule

```text
Historical Material Reference
        ↓
Document / Source Identity Review
        ↓
Matter and Entity Identity Review
        ↓
Purpose and Access Review
        ↓
Qualified Human Binding Approval
        ↓
Only then may an acquisition plan be considered authorized
```

### 9.2 Category Matrix

| ID | Category | Frozen state | Candidate source path after identity approval | Plan result |
|---|---|---|---|---|
| C-P01 | Fee-detail workbook | Missing at prior path; expected hash retained | Approved matter custodian native workbook/export | `BLOCKED — IDENTITY FIRST` |
| C-P02 | Property/asset registration | Not found | Approved official/party source after qualified authority review | `BLOCKED — IDENTITY FIRST` |
| C-P03 | Enforcement records/logs | Not found | Approved court/party/counsel source after matter confirmation | `BLOCKED — IDENTITY FIRST` |
| C-P04 | Derivative-litigation materials | Not found | Approved court/party/counsel source after relationship confirmation | `BLOCKED — IDENTITY FIRST` |

```text
Matter identity:
BLOCKED — QUALIFIED HUMAN CONFIRMATION REQUIRED

Current infrastructure state:
BLOCKED

Physical acquisition:
NOT AUTHORIZED / NOT PERFORMED
```

The fee workbook cannot substitute for property, enforcement, transaction, or derivative-litigation sources.

## 10. Missing Evidence and Blocker Classification

| Code | Meaning | Planning response |
|---|---|---|
| `CATEGORY_CONFIRMATION_PENDING` | Newly proposed category not yet human-approved | Keep `CANDIDATE`; no acquisition action |
| `MATTER_IDENTITY_UNKNOWN` | Matter relationship unresolved | Identity review only; affected plan `BLOCKED` |
| `ENTITY_IDENTITY_UNKNOWN` | Party/source role unresolved | Preserve candidates and conflicts |
| `SOURCE_NOT_IDENTIFIED` | No responsible real-world source class confirmed | Assign source-identification owner |
| `AUTHORITY_NOT_ASSESSED` | Acquisition/access authority not reviewed | Qualified-lawyer/access review |
| `FILE_NOT_LOCATED` | Material missing at approved path | Authorized locate/request plan only |
| `ACCESS_DENIED_OR_UNKNOWN` | Current access unavailable or unclear | Human access/scope decision |
| `HASH_NOT_AVAILABLE` | Current bytes unavailable | Verify only after authorized receipt/access |
| `HASH_MISMATCH` | Received bytes differ from expected | Quarantine or register new version |
| `COLLECTION_CHILD_IDENTITY_MISSING` | Directory lacks per-file binding | Register every relied-upon child |
| `TEXT_COVERAGE_UNKNOWN` | Source-unit readiness unassessed | Later text/OCR classification |
| `OCR_REQUIRED_NOT_AUTHORIZED` | OCR needed but outside current authority | Preserve blocker |
| `DOCUMENT_REVIEW_PENDING` | Source fidelity not reviewed | Assign authorized reviewer |
| `LEGAL_REVIEW_PENDING` | Analytical use not approved | Qualified-lawyer review |
| `CRITICAL_CATEGORY_NOT_READY` | Human-confirmed required category fails gate | Matter scope remains `BLOCKED` |

## 11. Analysis-Ready Decision Criteria

The Acquisition Plan may only define, not issue, an Analysis-Ready decision.

### 11.1 Document-Level Criteria

- acquisition authority and receipt are recorded;
- matter, source, entity, purpose, and access scope are human-confirmed;
- exact current bytes/version and SHA-256 are registered;
- all substantive source units have classified text/OCR requirements;
- any later extraction/OCR/transcription is human source-verified;
- Document Review and qualified-lawyer Legal Fact Review pass for the recorded scope;
- no supersession, revocation, conflict, or unresolved identity gap remains.

### 11.2 Case-Bundle Criteria

- a qualified human confirms the required and optional category profile;
- every critical required category has an Analysis-Ready source or an explicit human decision that it is not required;
- non-substitution rules are respected;
- adverse/conflicting/missing materials remain visible;
- matter isolation and confidentiality limits pass;
- an attributable human issues a scope-bound Analysis-Ready Manifest.

### 11.3 Decision States

```text
READY
PARTIAL
BLOCKED
```

`PARTIAL` is an infrastructure descriptor only. It cannot authorize reasoning through a missing critical prerequisite.

## 12. Human Ownership Matrix

| Decision | Accountable role | Prohibited automatic action |
|---|---|---|
| Confirm category and analytical need | Qualified lawyer / matter owner | Treat current instruction as proof of legal necessity |
| Approve source and acquisition path | Qualified lawyer / access owner | Assert entitlement or contact source |
| Approve privacy/confidentiality scope | Qualified legal/confidentiality owner | Infer permission from possession |
| Verify receipt and byte identity | Authorized intake/integrity reviewer | Treat hash as authenticity |
| Confirm matter/entity binding | Qualified matter owner / lawyer | Merge similar names, paths, or hashes |
| Classify text/OCR need | Authorized document reviewer | Run OCR in this phase |
| Verify source fidelity | Document reviewer | Convert transcription into truth |
| Approve Legal Fact use | Qualified lawyer | Auto-promote evidence into Legal Fact |
| Issue matter Analysis-Ready Manifest | Qualified matter review owner | Release matter with hidden critical gaps |

## 13. Audit, Correction, and Invalidation Plan

Minimum conceptual events:

```text
Gap/category registered
Category requiredness decision
Source candidate recorded
Authority owner assigned
Acquisition plan approved/rejected
Future operation separately authorized
Material receipt
Intake/version/hash verification
Matter/entity/source binding decision
Text/OCR classification
Document Review
Legal Fact Review
Bundle readiness decision
Correction / supersession / revocation / invalidation
```

Changed bytes, better copies, corrected extraction, new adverse sources, identity disputes, revoked access, or scope changes reopen every dependent review and readiness decision.

## 14. Governance Conformance

| Control | Design alignment |
|---|---|
| LRG-00 | Matter, purpose, actor, source, authority, access, and isolation precede any acquisition operation |
| LRG-01 | Every plan leads to exact evidence identity, provenance, processing, review, and lineage requirements |
| LRG-02 | Receipt, extraction, Source-Verified Fact Candidate, and Legal Fact Candidate remain separate |
| LRG-04 | Gaps remain `BLOCKED`; planning progress never becomes legal support |
| LRG-05 | Category, authority, binding, source fidelity, and legal-use decisions remain human-owned |
| Route A Design | The plan feeds the existing Evidence Object/intake lifecycle; it does not replace it |
| Route A Validation | Frozen `PARTIAL/BLOCKED` states remain unchanged |
| Input Readiness Recovery | Source/action/owner/target/blocker records implement the adopted recovery design without execution |

## 15. Acceptance Criteria Assessment

| ID | Status | Design evidence |
|---|---|---|
| `PEA-001` — Evidence Recovery Registry complete | **PASS** | Sections 3 and 7–10 cover 13 frozen categories plus 7 separately identified CASE-A candidate categories with explicit basis, state, source, authority, owner, target, blocker, and review requirements |
| `PEA-002` — CASE-A/B/C material gaps classified | **PASS** | CASE-A maps 11 categories, CASE-B 5, CASE-C 4; frozen gaps and newly proposed candidates are visibly separated |
| `PEA-003` — Recovery source and responsibility paths clear | **PASS** | Section 5 binds every material class to a named real-world source class, qualified authority owner, verification package, and next controlled state without asserting availability or entitlement |
| `PEA-004` — Identity Gate effective | **PASS** | Sections 6 and 9 separate document, source, matter, entity, purpose, access, and human approval; CASE-C remains blocked |
| `PEA-005` — No legal reasoning conclusion | **PASS** | No authenticity, admissibility, Fact, Legal Fact, request-right, burden, strategy, outcome, or probability conclusion is generated |
| `PEA-006` — Zero engineering pollution | **PASS** | This execution creates two documentation outputs only; repository and target-module verification is recorded in the Result |

## 16. Risks and Safeguards

| Risk | Safeguard |
|---|---|
| Candidate source mistaken for entitlement | Explicit human authority state and non-execution label |
| Proposed category treated as legally required | Separate `CURRENT_INSTRUCTION_CANDIDATE` and human requiredness decision |
| Official/public material substitutes for transaction proof | Category non-substitution rule |
| Same name/path binds wrong matter | Multi-level identity gate; CASE-C fail-closed |
| Directory/count replaces files | Per-child registration requirement |
| Hash becomes authenticity | Same-byte-only label |
| Receipt becomes readiness | Existing Route A intake/review lifecycle remains mandatory |
| OCR need becomes implementation | Classification only; OCR execution prohibited |
| Acquisition plan becomes external action | Separate future operational authorization required |
| Planning status becomes merits support | Infrastructure and LRG validation states remain independent |

## 17. Explicit Boundary and Next Governance Action

The following were not performed and remain unauthorized:

```text
Physical acquisition or external contact
Request/application/investigation-order drafting or issuance
File copy, move, download, upload, conversion, or new content reading
OCR engine selection, OCR execution, or transcription
Database / storage implementation
MCP integration
Agent or Skill modification
Workflow or runtime-schema modification
Code or test scripts
RAG / vector store
Production pipeline or deployment
Evidence or legal reasoning conclusions
Route A implementation
Route B activation
```

Current transition:

```text
Codex Executor
        ↓
Physical Evidence Acquisition Spec + Result
        ↓
Architecture Coordinator — exact artifact review
        ↓
Project Owner — design closeout decision
```

Any actual material acquisition operation requires a new, separately reviewed Handoff that binds exact sources, actors, files/categories, authority basis, safeguards, outputs, rollback/stop conditions, and validation steps.
