# TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Route | Phase 2 / Route A |
| Task | Input Readiness Recovery Design |
| Version | v1.0 design execution artifact |
| Execution date | 2026-07-22 |
| Status | **DONE — DESIGN ONLY** |
| Approved Handoff SHA-256 | `180A160564CAB3A7E58AFFC92F16F595C0F7C95D342CCE281A042485537BDA75` |
| Execution authority | Project Owner approval in the current coordination record |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

This specification defines documentation-level recovery controls for missing, inaccessible, identity-ambiguous, text-unready, OCR-dependent, or human-unverified case material. It is not an executable schema, database, OCR service, acquisition action, court request, MCP, Workflow, Skill, Agent, code package, or production pipeline.

## 1. Exact Input Binding

All bound artifacts were present and byte-identical before output creation.

| Input | Path | Expected and actual SHA-256 | Result |
|---|---|---|---|
| Recovery Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_HANDOFF.md` | `180A160564CAB3A7E58AFFC92F16F595C0F7C95D342CCE281A042485537BDA75` | PASS |
| Canonical Governance Pattern | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | PASS |
| Route A Evidence Infrastructure Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` | PASS |
| Route A Evidence Infrastructure Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md` | `DF22B914C0F92073E41B5126DAE5AE7CBE1C442CBCE99798A0488BDE3B97EAFD` | PASS |
| Route A Design Validation Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_HANDOFF.md` | `E55B25CB94D6F5E35D199D575EE8CDF708DA79F89D4CEEC12C2CF88B2070AE27` | PASS |
| Route A Design Validation Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md` | `8DBDD4F438BC05DCCA3BAFB6CE4572A4E0FDEDAC1A8303002292CEB6FEC367AB` | PASS |
| Route A Design Validation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md` | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` | PASS |

Frozen starting point:

```text
Route A design compatibility:
SUPPORTED

Current physical material readiness:
CASE-A  PARTIAL / LEGAL REASONING BLOCKED
CASE-B  BLOCKED
CASE-C  BLOCKED

Route A implementation:
NOT AUTHORIZED
```

## 2. Objective, Principles, and Non-Goals

### 2.1 Objective

The Recovery layer converts an unmanaged material gap into a governed, attributable, and reviewable recovery plan:

```text
Evidence Missing / Inaccessible / Ambiguous / Unready
        ↓
Evidence Recovery Registry
        ↓
Authorized Material Acquisition Map
        ↓
Identity Recovery Gate
        ↓
Text / OCR Readiness Classification
        ↓
Human Verification and Matter Gate
        ↓
Analysis-Ready Candidate Input or Explicit BLOCKED
```

### 2.2 Design Principles

1. **Authority before acquisition**: a recovery action requires an approved matter, purpose, source, actor, and access scope.
2. **Gap before guess**: missing identity, access, content, review, or source remains an explicit blocker.
3. **Path is not identity**: a located path does not prove same bytes, same source, same matter, or permitted use.
4. **Hash is not authenticity**: a matching SHA-256 establishes same-byte identity only.
5. **Recovery is not proof**: located, accessible, text-ready, or human-transcribed material is not thereby authentic, admissible, credible, sufficient, or true.
6. **OCR is not fact**: OCR need and output are processing states, not evidence or legal conclusions.
7. **Independent gates**: file, source, matter, entity, extraction, evidence-use, and Legal Fact decisions remain distinct.
8. **No automatic inheritance**: restored or replaced bytes do not inherit prior review/readiness.
9. **Matter isolation**: recovery for one matter or purpose does not authorize reuse elsewhere.
10. **Qualified-human control**: lawful acquisition, identity reconciliation, evidentiary use, and legal reasoning remain human decisions.

### 2.3 Non-Goals

This design does not:

- locate, request, copy, move, rename, convert, OCR, transcribe, or read new case materials;
- select an OCR engine, database, provider, storage system, API, MCP, Agent, or Workflow;
- determine entitlement to obtain bank, court, corporate, property, communication, or other records;
- determine evidence authenticity, admissibility, credibility, probative weight, or sufficiency;
- generate facts, Legal Facts, request rights, burden positions, strategies, outcomes, or probabilities;
- authorize Route A implementation or Route B.

## 3. Evidence Recovery Registry Model

The following is a conceptual documentation contract, not a runtime schema.

### 3.1 Recovery Object

```yaml
EvidenceRecoveryObject:
  recovery_id: stable recovery-task identity
  matter_id: approved matter identity or explicit UNKNOWN
  matter_label: display label only; never identity proof
  entity_id_candidates: proposed parties/custodians with uncertainty
  evidence_category: required or optional category for a declared scope
  required_for_scope: human-approved required/optional/unknown designation
  expected_evidence_id: prior evidence identity if any
  expected_document_id: prior document identity if any
  expected_version: prior version identity if any
  original_source: known source/custodian and acquisition history
  approved_source_candidates: sources requiring separate authority confirmation
  prior_location: previously approved path/object reference
  current_location: current path/object reference or NOT_LOCATED
  expected_sha256: prior byte identity if any
  actual_sha256: current recomputed identity if accessible
  expected_byte_size: prior size if any
  actual_byte_size: current size if accessible
  document_type: declared/detected type or UNKNOWN
  availability_status: independent availability state
  access_authorization_status: independent authority state
  hash_status: independent integrity state
  matter_identity_status: independent matter-binding state
  entity_identity_status: independent attribution state
  text_status: independent native-text coverage state
  ocr_readiness_class: classification only
  extraction_status: independent extraction state
  document_review_status: source-fidelity review state
  legal_review_status: qualified-lawyer analytical-use state
  recovery_owner: accountable human role
  recovery_action: approved candidate action or NO_ACTION_AUTHORIZED
  action_status: planned/authorized/in-progress/completed/blocked
  target_state: next permitted state, not an automatic transition
  blocking_reasons: explicit prerequisites and stop conditions
  limitations: ambiguity, unavailable regions, source/provenance caveats
  supersedes: prior recovery or document record
  superseded_by: replacement record
  correction_history: attributed append-only corrections
  audit_references: authority, action, verification, and review events
```

### 3.2 Required Registry Rules

- `matter_id`, `evidence_category`, current availability, authority, identity, owner, action, and blocker must never be omitted.
- `UNKNOWN`, `NOT_AVAILABLE`, and `NOT_AUTHORIZED` are valid explicit values; empty fields are not.
- `expected_sha256` and `actual_sha256` remain separate.
- a recovery object may refer to an absent expected document without pretending that the document currently exists;
- directory recovery requires a collection record plus an individual record for every relied-upon child file;
- same-byte copies keep distinct source/acquisition/use records where provenance or authority differs;
- changes, corrections, replacements, and review reversals create new lineage rather than silent overwrite.

## 4. Independent Recovery Status Dimensions

### 4.1 Availability Status

```text
UNKNOWN
MISSING
LOCATED_UNVERIFIED
ACCESSIBLE
DENIED
CORRUPT
QUARANTINED
```

Only `ACCESSIBLE` may proceed to current byte verification.

### 4.2 Access Authorization Status

```text
UNKNOWN
NOT_REQUESTED
PENDING_HUMAN_APPROVAL
AUTHORIZED_FOR_RECOVERY
AUTHORIZED_FOR_REVIEW
DENIED
REVOKED
```

Possession, path visibility, or prior access does not imply current authorization.

### 4.3 Hash Status

```text
NOT_COMPUTED
EXPECTED_ONLY
VERIFIED
MISMATCH
NOT_AVAILABLE
SUPERSEDED
```

`VERIFIED` means the current accessible bytes match the registered identity. It says nothing about source authenticity or legal validity.

### 4.4 Identity Status

File identity:

```text
UNKNOWN
EXPECTED_ONLY
VERIFIED
MISMATCH
SUPERSEDED
```

Matter identity:

```text
UNKNOWN
CANDIDATE
HUMAN_CONFIRMED
REJECTED
REVOKED
```

Entity/source attribution:

```text
UNKNOWN
CANDIDATE
SOURCE_DOCUMENTED
HUMAN_CONFIRMED_FOR_SCOPE
DISPUTED
REJECTED
```

These dimensions cannot be collapsed into a single `IDENTIFIED` flag.

### 4.5 Text and OCR Readiness

Text status:

```text
UNKNOWN
TEXT_AVAILABLE_COMPLETE
TEXT_AVAILABLE_PARTIAL
IMAGE_ONLY
UNREADABLE_OR_CORRUPT
NOT_APPLICABLE
```

OCR/readiness classification:

```text
OCR_NOT_REQUIRED
OCR_REQUIRED
HYBRID_TEXT_IMAGE
MANUAL_TRANSCRIPTION_CANDIDATE
HUMAN_REVIEW_REQUIRED
OCR_UNAVAILABLE
UNCLASSIFIED
```

These are classification states only. This design does not run OCR or prescribe a provider.

### 4.6 Extraction and Human Review

Extraction:

```text
NOT_STARTED
EXTRACTED_UNVERIFIED
HUMAN_SOURCE_VERIFIED
REJECTED
SUPERSEDED
```

Document Review:

```text
REQUIRED
PENDING
SOURCE_VERIFIED
REJECTED
REVOKED
```

Legal Fact Review:

```text
REQUIRED
PENDING
LAWYER_APPROVED_FOR_ANALYSIS
REJECTED
REVOKED
```

One human-review state never silently satisfies another.

### 4.7 Recovery and Readiness Descriptors

Recovery planning state:

```text
UNPLANNED
PLANNED
PENDING_AUTHORIZATION
AUTHORIZED
IN_PROGRESS
RECOVERED_PENDING_VERIFICATION
COMPLETED_FOR_RECORDED_SCOPE
BLOCKED
CANCELLED
SUPERSEDED
```

Infrastructure readiness:

```text
READY
PARTIAL
BLOCKED
```

Legal-reasoning validation remains limited to:

```text
SUPPORTED
UNKNOWN
BLOCKED
```

Recovery completion never assigns `SUPPORTED` to a fact or legal proposition.

## 5. Recovery Lifecycle and Gates

### 5.1 Controlled Lifecycle

```text
MISSING / UNKNOWN
        ↓
RECOVERY PLANNED
        ↓
RECOVERY AUTHORIZED BY QUALIFIED HUMAN
        ↓
LOCATED
        ↓
ACCESS AND PURPOSE AUTHORIZED
        ↓
ACCESSIBLE
        ↓
FILE IDENTITY VERIFIED
        ↓
SOURCE / MATTER / ENTITY IDENTITY REVIEWED
        ↓
TEXT ROUTE CLASSIFIED
        ↓
EXTRACTION OR TRANSCRIPTION HUMAN VERIFIED
        ↓
DOCUMENT REVIEW COMPLETED
        ↓
LEGAL FACT REVIEW COMPLETED
        ↓
CASE-BUNDLE GATE PASSED
        ↓
ANALYSIS READY FOR RECORDED SCOPE
```

At any stage:

```text
BLOCKED | DENIED | QUARANTINED | REJECTED | REVOKED | SUPERSEDED
```

The lifecycle is a governance model, not a runtime state machine.

### 5.2 Transition Matrix

| From → To | Preconditions | Recorded evidence | Fail-closed behavior |
|---|---|---|---|
| Missing/Unknown → Planned | Required category and purpose approved; owner assigned | Gap, scope, candidate source/action | Remain `BLOCKED` if purpose/owner unknown |
| Planned → Authorized | Qualified human confirms lawful source, actor, method, limits | Authorization identity, scope, date, conditions | No acquisition action without approval |
| Authorized → Located | Candidate material found at approved source/location | Locator, source, acquisition event | Location alone remains unverified |
| Located → Accessible | Current actor may open/use bytes for recovery scope | Access decision and restrictions | `DENIED`/`QUARANTINED` on scope failure |
| Accessible → File Identity Verified | Hash and size recomputed; version recorded | Actual hash/size, verifier, time | `MISMATCH` creates new version or quarantine |
| File Verified → Identity Reviewed | Source, matter, and entity relationships reviewed | Separate human decisions and uncertainty | Any failed identity gate yields `BLOCKED` |
| Identity Reviewed → Text Route Classified | File/source-unit coverage assessed | Native/OCR/hybrid/manual classification | Unreadable scope remains explicit |
| Classified → Extraction Human Verified | Later authorized processing output checked against source | Locators, corrections, limitations, reviewer | No direct jump from OCR/text to fact |
| Source Verified → Legal Fact Reviewed | Qualified lawyer reviews purpose, relevance, conflicts, authority needs | Approval/rejection and limited scope | Pending/failed review blocks analytical use |
| Legal Fact Reviewed → Analysis Ready | Every critical case-bundle category and human gate passes | Scope-bound Analysis-Ready Manifest | One ready file cannot mask critical gaps |

### 5.3 Prohibited Shortcuts

```text
MISSING → ANALYSIS_READY
LOCATED → HASH_VERIFIED
HASH_VERIFIED → EVIDENCE_AUTHENTIC
TEXT_AVAILABLE → FACT
OCR_COMPLETED → LEGAL_FACT
HUMAN_TRANSCRIPTION → REQUEST_RIGHT
SIMILAR_FILENAME → SAME_MATTER
SAME_HASH → SAME_SOURCE_OR_USE_AUTHORITY
ONE_READY_FILE → CASE_READY
```

## 6. Material Acquisition Map

### 6.1 Map Contract

| Field | Required content |
|---|---|
| Required category | Human-approved category and declared analytical scope |
| Current state | Availability, authority, identity, text/OCR, and review states |
| Candidate source | Person/system/institution/public record with uncertainty |
| Authority owner | Qualified human who decides whether and how acquisition is lawful |
| Candidate action | Locate, request authorized copy, re-export, rebind, rescan, register child files, classify, or assign review |
| Action limits | Matter, purpose, time, confidentiality, personal-information, and source limits |
| Verification package | Path/object, bytes, hash, size, type, source, acquisition event, and lineage |
| Target state | The next controlled state only, never automatic Analysis Ready |
| Blocker | Missing authority, source, identity, access, bytes, review, or scope |

### 6.2 Candidate Recovery Action Taxonomy

```text
LOCATE_WITHIN_APPROVED_SCOPE
REQUEST_AUTHORIZED_COPY_FROM_APPROVED_CUSTODIAN
OBTAIN_LAWFULLY_AUTHORIZED_OFFICIAL_COPY
REEXPORT_FROM_APPROVED_SOURCE_SYSTEM
REBIND_CURRENT_PATH_OR_OBJECT_VERSION
RECOMPUTE_HASH_AND_SIZE
REGISTER_COLLECTION_CHILD_FILES
OBTAIN_BETTER_SCAN_OR_NATIVE_EXPORT
CLASSIFY_TEXT_AND_OCR_NEED
ASSIGN_DOCUMENT_REVIEW
ASSIGN_QUALIFIED_LAWYER_REVIEW
CONFIRM_MATTER_AND_ENTITY_IDENTITY
NO_ACTION_AUTHORIZED
```

These are candidate planning labels. They do not assert legal entitlement to obtain records and do not authorize contacting custodians, courts, banks, registries, platforms, parties, or providers. The qualified lawyer must confirm the current China Mainland legal basis, procedure, professional duty, personal-information boundary, confidentiality requirement, and matter-specific authority before any acquisition.

## 7. Identity Recovery Gate

### 7.1 Gate Sequence

```text
Document / Byte Identity
        ↓
Source / Acquisition Identity
        ↓
Matter Identity
        ↓
Entity / Party Attribution
        ↓
Purpose and Access Authorization
        ↓
Qualified Human Binding Approval
```

Every gate records `PASS`, `UNKNOWN`, `BLOCKED`, or `REJECTED` plus reviewer, date, sources, scope, and limitations.

### 7.2 Binding Rules

- a name match is only a search clue;
- a path match is only a locator observation;
- a hash match is only same-byte identity;
- a source record may establish who supplied material but not whether its content is true;
- a matter label does not prove that a document belongs to that matter;
- an entity name does not prove party role, control, liability, ownership, or attribution;
- prior approval is limited to its recorded matter, bytes, version, source, actor, purpose, and time;
- conflict or uncertainty remains visible and blocks the affected scope.

### 7.3 CASE-C Identity Drift Control

The current “康尔达” validation label, the frozen `C02-CASE-C-001 / 张成棋执行衍生案件` label, and a historical filename containing “康尔达” are distinct metadata observations. The Recovery Registry must not merge them automatically.

Required resolution package:

1. stable approved `matter_id`;
2. qualified-human explanation of the relationship, if any;
3. identified parties/entities and unresolved roles;
4. permitted purpose and recovery scope;
5. source/custodian and acquisition authority;
6. separate approval for every material use.

Until completed:

```text
Matter Identity: UNKNOWN / BLOCKED
Recovery Action: IDENTITY CONFIRMATION ONLY
Analytical Use: NOT AUTHORIZED
```

## 8. OCR and Text Readiness Layer

### 8.1 Classification Matrix

| Class | Meaning | Next design action | Does not establish |
|---|---|---|---|
| `TEXT_AVAILABLE_COMPLETE` | Usable native text appears to cover all substantive source units for the declared scope | Source-unit extraction and human comparison | Extraction accuracy, truth, or completeness beyond scope |
| `TEXT_AVAILABLE_PARTIAL` | Some substantive units lack usable text or layout | Classify missing units for OCR/manual path | Complete document text |
| `OCR_REQUIRED` | Image-only/unusable regions require OCR in a later authorized phase | Record pages/regions and review requirements | OCR authorization or factual content |
| `IMAGE_ONLY` | Material is an image/screenshot/scan without usable native text | Preserve source image, context, and review plan | Transcribed content or authenticity |
| `HYBRID_TEXT_IMAGE` | Native and image regions coexist | Preserve outputs separately and reconcile conflicts | Silent merged text correctness |
| `UNREADABLE_OR_CORRUPT` | Current source cannot support reliable processing | Seek authorized better source or manual decision | Missing content reconstruction |
| `MANUAL_TRANSCRIPTION_CANDIDATE` | Human transcription may be needed if later authorized | Define locator, double-check, correction, and review controls | Automatic truth or legal meaning |
| `HUMAN_REVIEW_REQUIRED` | Technical classification/output needs human confirmation | Assign authorized reviewer | Approval by silence |
| `NOT_APPLICABLE` | Text/OCR is not relevant to the format or scope | Use an approved format-specific route | Readiness of other gates |

### 8.2 Source-Unit Requirements

- PDF/image: page and region;
- spreadsheet: workbook, sheet, range/cell, formula/displayed value, header/unit/sign context;
- message: export, conversation, message ID, timestamp, sender, sequence, attachment, screenshot boundary;
- court/corporate/property record set: each relied-upon child file;
- mixed file: each substantive embedded object.

### 8.3 Mandatory Boundary

```text
Original Material
        ↓
Text/OCR Need Classification
        ↓
Later Authorized Extraction Candidate
        ↓
Document Human Review
        ↓
Source-Verified Fact Candidate
        ↓
Qualified Lawyer Legal Fact Review
        ↓
Legal Fact Candidate
```

No confidence score, OCR state, or recovery status becomes evidence truth or legal support.

## 9. CASE-A Recovery Map

The matter label is a validation identifier only.

| ID | Required material | Frozen state | Candidate human-owned recovery action | Next target state | Continuing blocker |
|---|---|---|---|---|---|
| A-D01 | Transaction bill/account workbook | Missing at prior path; expected hash recorded | Confirm approved custodian/source; locate or request authorized native copy; rebind path/version; recompute hash; preserve workbook structure | `FILE_IDENTITY_VERIFIED` | Source, access, matter scope, text/table review, and legal review |
| A-D02 | Company/public-record PDF | Accessible and byte-hash matched in frozen validation | Preserve current identity; confirm source/acquisition and purpose; assign Document Review and qualified-lawyer use review | `DOCUMENT_REVIEW_COMPLETED` | Cannot substitute for transaction sources; Legal Fact Review pending |
| A-D03 | WeChat/correspondence records | Not found | Qualified lawyer defines lawful/authorized source and scope; prefer complete native/export context where available; register messages/attachments or bounded screenshots separately | `LOCATED` then `FILE_IDENTITY_VERIFIED` | Completeness, sender attribution, sequence, edits/deletions, personal-information/confidentiality, human review |
| A-D04 | Payment vouchers | Not found | Identify authorized holder/source; obtain only through a matter-approved and legally authorized path; register each file/version | `LOCATED` then `FILE_IDENTITY_VERIFIED` | Account/source attribution, scope, authenticity/admissibility questions, review |

CASE-A recovery determination:

```text
Recovery Registry coverage: COMPLETE AT DESIGN LEVEL
Current infrastructure readiness: PARTIAL
Current legal reasoning: BLOCKED
Automatic acquisition or analysis: NOT AUTHORIZED
```

## 10. CASE-B Recovery Map

The matter label is a validation identifier only.

| ID | Required material | Frozen state | Candidate human-owned recovery action | Next target state | Continuing blocker |
|---|---|---|---|---|---|
| B-D01 | Judgment/court document | Missing at prior path; expected hash recorded | Confirm authorized official/party source; locate or obtain lawful copy; recompute identity | `FILE_IDENTITY_VERIFIED` | Current source/version, text/OCR, human review |
| B-D02 | Bank-flow/financial record | Missing at prior path; expected hash recorded | Qualified lawyer confirms entitlement and approved source; locate/request authorized native record; preserve table structure | `FILE_IDENTITY_VERIFIED` | Access authority, source, table fidelity, review |
| B-D03 | Corporate registration collection | Prior directory unavailable; `Bound Multiple` not per-file identity | Reacquire only from approved source; register every relied-upon child file by path/version/hash/type | `REGISTERED` per child | Child identities, completeness, currentness, review |
| B-D04 | Shareholder records | No independently bound file | Identify authorized official/corporate source; register individual documents and versions | `LOCATED` | Source/role/time scope and human review |
| B-D05 | Enforcement materials | Not found | Qualified lawyer identifies permitted court/party source and scope; request/locate authorized copies | `LOCATED` | Access, completeness, current procedural context, review |

CASE-B recovery determination:

```text
Recovery Registry coverage: COMPLETE AT DESIGN LEVEL
Current infrastructure readiness: BLOCKED
Current legal reasoning: BLOCKED
Prior directory count or filename inference: PROHIBITED
```

## 11. CASE-C Recovery Map

The current and frozen matter labels require qualified-human reconciliation before any acquisition or use.

| ID | Required material | Frozen state | Candidate human-owned recovery action | Next target state | Continuing blocker |
|---|---|---|---|---|---|
| C-D01 | Fee-detail workbook | Missing at prior path; expected hash recorded; matter relationship unresolved | First confirm matter/entity binding; then locate/request authorized native copy; rebind and hash; preserve workbook structure | `MATTER_IDENTITY_HUMAN_CONFIRMED`, then `FILE_IDENTITY_VERIFIED` | Matter identity, source, access, table review, legal review |
| C-D02 | Property/asset registration | Not found | After matter confirmation, qualified lawyer determines lawful official/party source and access basis; register exact version | `LOCATED` | Matter/entity/access authority, currentness, review |
| C-D03 | Enforcement records/logs | Not found | After matter confirmation, identify permitted court/party source and bounded procedural scope | `LOCATED` | Matter identity, source, completeness, review |
| C-D04 | Derivative-litigation materials | Not found | After matter confirmation, identify authorized counsel/court/party source and exact purpose | `LOCATED` | Matter identity, source, scope, legal review |

CASE-C recovery determination:

```text
Recovery Registry coverage: COMPLETE AT DESIGN LEVEL
Current matter identity: BLOCKED / HUMAN CONFIRMATION REQUIRED
Current infrastructure readiness: BLOCKED
Current legal reasoning: BLOCKED
Filename or label auto-binding: PROHIBITED
```

## 12. Blocking and Remediation Codes

| Code | Meaning | Permitted next design action |
|---|---|---|
| `RECOVERY_OWNER_MISSING` | No accountable human owner | Assign owner before planning |
| `RECOVERY_AUTHORITY_MISSING` | Acquisition/use authority not approved | Qualified legal/access review |
| `SOURCE_UNKNOWN` | Source/custodian unresolved | Source identification only |
| `FILE_NOT_LOCATED` | Material not found at approved locations | Authorized locate/request plan |
| `ACCESS_DENIED` | Current actor cannot access/use | Human scope/access decision |
| `HASH_NOT_AVAILABLE` | Bytes inaccessible or hash absent | Obtain authorized bytes, then recompute |
| `HASH_MISMATCH` | Current bytes differ from expected | Quarantine or register new version |
| `MATTER_IDENTITY_UNKNOWN` | Matter binding unresolved | Qualified-human reconciliation |
| `ENTITY_IDENTITY_UNKNOWN` | Party/source attribution unresolved | Preserve candidates and obtain review |
| `COLLECTION_CHILD_IDENTITY_MISSING` | Directory/collection lacks per-file identity | Register relied-upon children |
| `TEXT_COVERAGE_UNKNOWN` | Native-text coverage not classified | Source-unit assessment |
| `OCR_REQUIRED_NOT_AUTHORIZED` | OCR is needed but not authorized | Preserve blocker; request separate authorization if appropriate |
| `OCR_OR_EXTRACTION_UNVERIFIED` | Candidate output lacks source comparison | Document Review Gate |
| `DOCUMENT_REVIEW_PENDING` | Source fidelity not approved | Assign authorized reviewer |
| `LEGAL_REVIEW_PENDING` | Analytical use not approved | Qualified-lawyer review |
| `CRITICAL_CATEGORY_MISSING` | Required bundle category not ready | Keep affected matter scope `BLOCKED` |
| `VERSION_SUPERSEDED` | New/corrected source invalidates old record | Reopen identity and all dependent reviews |

## 13. Human Review and Decision Boundary

| Decision | Responsible human role | Machine-assisted support | Prohibited automation |
|---|---|---|---|
| Recovery purpose and category | Matter owner / qualified lawyer | Display gaps and prior registry | Declare category legally sufficient |
| Acquisition authority and method | Qualified lawyer / approved access owner | Present candidate sources/actions | Assert entitlement or contact source |
| File identity | Authorized integrity verifier | Compute hash/size in later approved phase | Treat hash as authenticity |
| Matter/entity binding | Qualified matter owner / lawyer | Present conflicting labels and source records | Auto-merge similar names/files |
| Text/OCR classification | Authorized document reviewer | Coverage observations in later approved phase | Run OCR or approve output in this design |
| Source fidelity | Document reviewer | Side-by-side source/locator package in later implementation | Convert transcription to truth |
| Evidence/legal use | Qualified lawyer | Present provenance, conflicts, limits, and review status | Determine admissibility, weight, or Legal Fact automatically |
| Analysis readiness | Qualified matter review owner | Produce candidate manifest/blocker list | Release scope with critical gaps |

Silence, tool completion, a confidence score, or a prior review is never current approval.

## 14. Audit, Correction, Supersession, and Invalidation

Minimum conceptual audit events:

```text
Gap registered
Recovery owner assigned
Purpose/scope approved
Candidate source recorded
Recovery action authorized/rejected
Material located
Access decision
Path/object rebound
Hash/size verification
Version/source identity decision
Matter/entity binding decision
Text/OCR classification
Document Review
Legal Fact Review
Bundle readiness decision
Correction / supersession / revocation / invalidation
```

Every event records actor/role, time, matter, source, object/version, prior/new state, reason, scope, and dependent objects.

Reopening triggers include:

- changed or missing bytes;
- new location with unverified version;
- corrected extraction or better scan/export;
- source, matter, or entity identity dispute;
- access/purpose change;
- review rejection or revocation;
- new adverse/conflicting material;
- replacement or superseding record.

Any affected Analysis-Ready Manifest and downstream candidate returns to pending or `BLOCKED` until re-reviewed.

## 15. Governance Conformance

| Control | Recovery design alignment |
|---|---|
| LRG-00 Boundary | Recovery requires matter, purpose, actor, source, use, isolation, and human owner before acquisition |
| LRG-01 Evidence | Registry preserves source, identity, access, hash, processing, review, limitations, and lineage |
| LRG-02 Fact | Recovery/output states cannot become Source-Verified or Legal Fact candidates without separate gates |
| LRG-04 Validation | Critical gaps remain `BLOCKED`; recovery progress never becomes merits support |
| LRG-05 Human Decision | Acquisition, binding, source fidelity, evidentiary use, and legal use remain human decisions |
| Route A Design | Recovery records feed the existing Evidence Object and Analysis-Ready Manifest without replacing them |
| Route A Validation | `PARTIAL/BLOCKED` case results are preserved; safe recovery planning does not reinterpret readiness |

## 16. Acceptance Criteria Assessment

| ID | Status | Design evidence |
|---|---|---|
| `INPUT-RECOVERY-001` — Evidence Recovery Registry complete | **PASS** | Sections 3–4 cover identity, source, location, authority, access, hash, type, text/OCR, reviews, action, owner, blockers, targets, and lineage for all three profiles |
| `INPUT-RECOVERY-002` — Material Acquisition Map complete | **PASS** | Sections 6 and 9–11 map all thirteen frozen categories from current state to human-owned candidate action, next state, and continuing blocker |
| `INPUT-RECOVERY-003` — OCR need classification complete | **PASS** | Section 8 distinguishes native, partial, hybrid, image-only, unreadable, OCR-required, manual, and human-review classes without implementation |
| `INPUT-RECOVERY-004` — Identity ambiguity isolated | **PASS** | Section 7 separates file, source, matter, entity, purpose, and approval; CASE-C remains blocked pending qualified-human confirmation |
| `INPUT-RECOVERY-005` — No legal reasoning generated | **PASS** | The design generates only recovery controls and explicitly preserves Evidence ≠ Fact ≠ Legal Fact ≠ Request Right |
| `INPUT-RECOVERY-006` — Zero implementation pollution | **PASS** | This task creates documentation only; repository and target-module verification is recorded in the Result |

## 17. Risks and Safeguards

| Risk | Safeguard |
|---|---|
| Recovery plan mistaken for collection authority | Separate `PENDING_HUMAN_APPROVAL` and `AUTHORIZED_FOR_RECOVERY`; candidate actions are non-executing |
| Located path treated as identity | Require current bytes, size, hash, version, source, and matter checks |
| Same hash treated as authentic evidence | Label hash as same-byte identity only |
| Similar name binds wrong case/entity | Separate matter/entity gates and qualified-human decision |
| OCR need becomes OCR implementation | Classification only; provider/execution remains prohibited |
| Human transcription becomes fact | Document Review and Legal Fact Review remain separate |
| One recovered item releases incomplete matter | Critical-category case-bundle gate remains fail-closed |
| Official/public record substitutes for transaction evidence | Category non-substitution rule |
| Prior review silently transfers to replacement | New version reopens every dependent review |
| Recovery status becomes merits score | Infrastructure and legal-reasoning states remain separate |

## 18. Implementation Boundary and Next Governance Action

Explicitly excluded:

```text
Material acquisition or external contact
OCR engine/provider selection or execution
Database / object-store implementation
MCP integration
Agent or Skill modification
Workflow or runtime-schema modification
Code or test scripts
RAG / vector store
Production pipeline or deployment
Evidence or legal conclusion generation
Route A implementation
Route B activation
```

Current transition:

```text
Codex Executor
        ↓
Recovery Spec + Result
        ↓
Architecture Coordinator — exact artifact review
        ↓
Project Owner — design closeout decision
```

Any later recovery operation, OCR work, input processing, or Route A implementation requires a new Handoff that binds exact targets, actors, sources, safeguards, and validation criteria.
