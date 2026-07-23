# TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Route | Phase 2 / Route A |
| Design | Evidence Infrastructure Design v1.0 |
| Version | v1.0 design execution artifact |
| Status | **DONE — DESIGN ONLY** |
| Execution date | 2026-07-22 |
| Approved Handoff SHA-256 | `9E40FC833135C8C7B5CE9B97A689D4335F10827A242A97424D20880B249831A3` |
| Canonical Governance Pattern SHA-256 | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` |
| C02-IV Input Readiness Spec SHA-256 | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` |
| C02-IV Input Readiness Result SHA-256 | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` |
| External Advisory Report SHA-256 | `F091FB8A53415F6DE152942A5144BE797F28BB2833C4EBE3A433CBFD4E592F77` |
| Mode | Documentation-only physical architecture design |
| Implementation | **NOT AUTHORIZED** |

This specification defines provider-neutral physical responsibilities, trust boundaries, conceptual records, state transitions, and review gates for an Evidence Infrastructure Layer. It is not an executable schema, API, database, OCR service, MCP definition, workflow, Skill, Agent, code package, infrastructure-as-code artifact, or production deployment plan.

## 1. Evidence Infrastructure Objective

### 1.1 Design Objective

The Evidence Infrastructure Layer ensures that any material admitted to legal reasoning has:

- a stable matter and evidence identity;
- a traceable source and version;
- independently verified byte identity;
- explicit access and confidentiality scope;
- page/region/sheet/message-level text or OCR coverage;
- versioned extraction and correction history;
- documented human source review;
- an explicit document- and matter-level readiness decision;
- audit and invalidation lineage.

Relationship to the canonical Governance Pattern:

```text
LEGAL_REASONING_GOVERNANCE_PATTERN v1.0
        │
        ├── LRG-00 Boundary Governance
        ├── LRG-01 Evidence Governance
        ├── LRG-02 Fact Governance
        ├── LRG-04 Validation Governance
        └── LRG-05 Human Decision Governance
                │
                ↓
Evidence Infrastructure Layer
                │
                ↓
Analysis-Ready Evidence Manifest
                │
                ↓
Separately governed legal reasoning
```

### 1.2 Problems Addressed

- files previously listed in a manifest are no longer accessible;
- the same path may contain changed bytes;
- directories are bound without per-file identities;
- PDFs contain image-only, partial, malformed, or absent text layers;
- OCR quality varies by page, table, stamp, signature, handwriting, and layout;
- OCR/extraction output may be mistaken for a fact;
- one readable document may mask an incomplete matter bundle;
- corrections or replacements may not invalidate dependent analysis;
- human source review and lawyer legal review may be conflated.

### 1.3 Non-Goals

This layer does not:

- decide legal issues, request rights, burdens, defenses, or litigation strategy;
- determine evidence authenticity, admissibility, credibility, weight, or sufficiency;
- generate a final legal opinion, merits conclusion, adjudication prediction, or success probability;
- select an OCR engine, model, database, vector store, object store, queue, MCP server, cloud, or vendor;
- implement extraction, OCR, storage, access control, workflow, RAG, or automation;
- make any existing CASE-A/B/C bundle analysis-ready merely by describing the architecture.

## 2. Governance Alignment

| Governance control | Infrastructure responsibility | Infrastructure must not do |
|---|---|---|
| LRG-00 Boundary | Bind matter, purpose, actor, access scope, evidence scope, isolation, and review owner | Expand purpose, cross matters, or infer permission from possession |
| LRG-01 Evidence | Register identity/source/version, verify bytes, assess text/OCR, preserve lifecycle and review lineage | Treat hash or processing completion as evidence validity |
| LRG-02 Fact | Produce source-located extraction candidates and source-review records | Promote OCR/extraction directly to Legal Fact |
| LRG-04 Validation | Emit readiness and blocking records; preserve downstream `BLOCKED` triggers | Produce merits scores or replace legal-reasoning states |
| LRG-05 Human Decision | Provide Document Review and Legal Fact Review gates with attributable decisions | Auto-approve sources, facts, request rights, or legal use |

Canonical invariants:

```text
Hash Verified
≠ Evidence Authentic
≠ Evidence Admissible
≠ Fact Proved
≠ Legal Fact Established
≠ Request Right Supported
```

## 3. Physical Architecture Overview

### 3.1 Conceptual Component Map

```text
Authorized Matter / Actor / Purpose
                │
                ↓
[C01] Matter & Access Boundary
                │
                ↓
[C02] Evidence Intake Gateway
                │
       ┌────────┴────────┐
       ↓                 ↓
[C03] Registry       [C04] Versioned Evidence Store
  of Record              (Original Bytes)
       │                 │
       └────────┬────────┘
                ↓
[C05] Integrity Verification Boundary
                │
                ↓
[C06] Text Readiness Assessor / Processing Router
       ┌────────┼───────────┬────────────┐
       ↓        ↓           ↓            ↓
 Native Text   OCR      Spreadsheet   Manual/Other
       └────────┼───────────┴────────────┘
                ↓
[C07] Extraction Candidate Workspace
                │
                ↓
[C08] Document Review Gate
                │
                ↓
[C09] Source-Verified Candidate Register
                │
                ↓
[C10] Legal Fact Review Gate
                │
                ↓
[C11] Analysis-Ready Manifest
                │
                ↓
Separately authorized Legal Reasoning Layer

Cross-cutting:
[C12] Audit / Correction / Supersession / Invalidation Ledger
[C13] Matter Isolation / Confidentiality / Retention Policy Boundary
```

Component labels are conceptual design identifiers. They do not prescribe services, processes, databases, or deployment topology.

### 3.2 Component Responsibilities and Trust Boundaries

| ID | Component | Accepts | Produces | Trust boundary / blocked behavior |
|---|---|---|---|---|
| C01 | Matter & Access Boundary | Matter request, actor, purpose, permitted sources | Authorized intake envelope | Blocks unknown matter, unauthorized actor/purpose, cross-matter use, or missing review owner |
| C02 | Evidence Intake Gateway | Files/objects and source declaration inside envelope | Receipt event and untrusted intake reference | Treats all content as untrusted; does not parse into facts |
| C03 | Registry of Record | Receipt event, source metadata, matter binding | Stable evidence/document/version record | Rejects missing matter/source/identity fields; no content-validity claim |
| C04 | Versioned Evidence Store abstraction | Original bytes/objects | Immutable-addressed or version-addressed original reference | Preserves bytes and version lineage; does not imply authenticity |
| C05 | Integrity Verification Boundary | Registered hash/size and current bytes | Hash result, size result, verifier/time | Mismatch/missing bytes cause quarantine and downstream invalidation |
| C06 | Text Readiness Assessor / Router | Identity-verified material | Page/region coverage map and processing route | Partial/nontext regions remain explicit; never assumes document-level completeness |
| C07 | Extraction Candidate Workspace | Original reference and approved route | Versioned extraction candidates with locators/method | Outputs remain unverified and isolated from legal reasoning |
| C08 | Document Review Gate | Source and extraction candidates | Source-fidelity decision, corrections, limitations | Missing/failed review blocks promotion; no legal relevance decision |
| C09 | Source-Verified Candidate Register | Human-reviewed extraction | Source-verified fact candidates and lineage | “Verified” means source fidelity only; truth/admissibility unresolved |
| C10 | Legal Fact Review Gate | Source-verified candidates and approved analytical purpose | Lawyer decision on promotion/use scope | Qualified lawyer required; no automatic Legal Fact promotion |
| C11 | Analysis-Ready Manifest | Ready documents, required-evidence profile, review decisions | Scope-bound manifest or blocked report | One ready document cannot mask missing required categories |
| C12 | Audit / Invalidation Ledger | Events from all components | Append-only conceptual history and dependency invalidations | Changed source/review reopens dependent readiness and analysis |
| C13 | Policy Boundary | Matter/access/confidentiality/retention rules | Enforced scope decisions and review flags | Denied/revoked scope blocks processing/use; no automated privilege conclusion |

### 3.3 Trust Zones

| Zone | Contents | Default trust |
|---|---|---|
| Z0 — External / Untrusted | Received files, uploads, messages, scans, external media, user descriptions | Untrusted |
| Z1 — Registered Original | Matter-bound, versioned original reference with source metadata | Identity pending until verified |
| Z2 — Identity Verified | Bytes and registered hash match within approved scope | Same-file identity only |
| Z3 — Processing Candidate | Native extraction, OCR, transcription, table reconstruction | Unverified candidate output |
| Z4 — Source Verified | Human-compared extraction and source-located proposition | Fidelity within reviewed scope only |
| Z5 — Lawyer Approved Input | Qualified-lawyer-approved source-verified candidate | Permitted for stated analytical scope, not a final legal conclusion |

No direct data path may jump from Z0–Z3 to the legal-reasoning layer.

## 4. Evidence Object Model

### 4.1 Conceptual Evidence Object

```yaml
EvidenceObject:
  evidence_id: stable evidence identity
  matter_id: authorized matter identity
  document_id: stable document identity
  document_version: immutable or versioned revision identity
  evidence_category: matter-profile category
  source_type: person | system | institution | device | public_record | other
  source_description: attributed source and acquisition context
  original_filename: exact original name where available
  storage_reference: approved locator or object reference
  byte_size: current version size
  sha256: registered byte identity
  file_type: detected and declared format
  received_at: receipt time
  registered_at: registration time
  registered_by: accountable actor
  access_scope: matter, actor, purpose, and handling restrictions
  access_status: independent access state
  hash_status: independent integrity state
  text_layer_status: page/region text coverage state
  ocr_status: independent OCR state
  extraction_status: independent extraction state
  document_review_status: source-fidelity review state
  legal_review_status: qualified-lawyer use decision
  readiness_status: READY | PARTIAL | BLOCKED descriptor
  blocking_reasons: explicit prerequisite gaps
  source_locators: page/sheet/cell/message/time/region map
  extraction_versions: candidate-output lineage
  linked_fact_candidates: source-verified candidate references only
  limitations: missing, ambiguous, illegible, truncated, or out-of-scope regions
  supersedes: prior document/version identity
  superseded_by: replacement identity
  correction_history: reviewer-attributed corrections
  audit_references: lifecycle and invalidation events
```

This YAML is illustrative documentation, not a runtime schema.

### 4.2 Identity Rules

- `evidence_id` identifies the evidence record; `document_id` and `document_version` identify its material versions.
- A changed byte sequence creates a new version identity and cannot silently inherit readiness.
- Path, filename, size, timestamp, and hash are separate observations.
- SHA-256 is mandatory for byte-identity verification but is not a conclusion about content origin or legal validity.
- Directory-level registration may describe a collection, but every relied-upon child file requires its own identity and processing states.
- A copy with the same hash may share byte identity while retaining a distinct source/acquisition record.
- Duplicate bytes do not automatically merge access scope, source attribution, or matter authorization.

### 4.3 Source and Provenance Model

The source record distinguishes:

- who or what supplied the material;
- from which system/device/institution it was acquired;
- when and by whom it was received;
- whether it is original, export, copy, screenshot, scan, printout, transcription, or derived file;
- known acquisition steps and unresolved gaps;
- matter and permitted-use scope;
- any associated parent/attachment/container relationship.

Infrastructure records provenance candidates. Qualified humans decide authenticity, admissibility, and evidentiary use.

### 4.4 Linked Facts Boundary

`linked_fact_candidates` may reference only Source-Verified Fact Candidates with exact source locators and review lineage. The Evidence Object must never contain an unreviewed Legal Fact or final merits label.

## 5. Independent State Models

### 5.1 Access Status

```text
UNKNOWN
ACCESSIBLE
MISSING
DENIED
CORRUPT
QUARANTINED
```

Only `ACCESSIBLE` may proceed to identity and processing checks.

### 5.2 Hash Status

```text
NOT_COMPUTED
REGISTERED_ONLY
VERIFIED
MISMATCH
NOT_AVAILABLE
```

Only `VERIFIED` establishes same-byte identity for the current version.

### 5.3 Text Layer Status

Canonical states:

```text
UNKNOWN
AVAILABLE_COMPLETE
AVAILABLE_PARTIAL
UNAVAILABLE
NOT_APPLICABLE
```

Presentation aliases:

| Alias | Canonical mapping | Consequence |
|---|---|---|
| `NO_TEXT` | `UNAVAILABLE` | OCR/manual processing required for substantive regions |
| `TEXT_AVAILABLE` | `AVAILABLE_COMPLETE`, or explicitly scoped `AVAILABLE_PARTIAL` | Extraction and source review still required |
| `OCR_PENDING` | `ocr_status = REQUIRED` | Not analysis-ready |
| `OCR_COMPLETED` | `COMPLETED_UNVERIFIED` | Candidate output only |
| `OCR_VERIFIED` | `HUMAN_VERIFIED` for recorded pages/regions | Fidelity verified only; legal review still required |

Aliases must not create duplicate or conflicting status semantics.

### 5.4 OCR Status

```text
NOT_REQUIRED
REQUIRED
COMPLETED_UNVERIFIED
HUMAN_VERIFIED
FAILED
NOT_AVAILABLE
SUPERSEDED
```

### 5.5 Extraction Status

```text
NOT_STARTED
EXTRACTED_UNVERIFIED
HUMAN_VERIFIED
REJECTED
SUPERSEDED
```

### 5.6 Review Statuses

Document Review Gate:

```text
REQUIRED
PENDING
SOURCE_VERIFIED
REJECTED
REVOKED
```

Legal Fact Review Gate:

```text
REQUIRED
PENDING
LAWYER_APPROVED_FOR_ANALYSIS
REJECTED
REVOKED
```

### 5.7 Readiness Descriptors

| Descriptor | Infrastructure meaning | Downstream effect |
|---|---|---|
| `READY` | All required document- and bundle-level gates for the declared scope pass | Legal reasoning may start only within the approved scope |
| `PARTIAL` | Some materials/scopes are ready while other categories or scopes remain incomplete | No critical required gap is waived; affected legal reasoning remains `BLOCKED` |
| `BLOCKED` | A critical identity, access, processing, review, completeness, or human-decision condition fails | Downstream legal reasoning prohibited for the affected scope |

These infrastructure descriptors do not replace LRG-04 states `SUPPORTED`, `UNKNOWN`, and `BLOCKED`. `PARTIAL` is not partial proof, partial merits support, or a confidence score.

## 6. Evidence Lifecycle Design

### 6.1 Lifecycle

```text
RECEIVED
        ↓
REGISTERED
        ↓
HASH_VERIFIED
        ↓
TEXT_ASSESSED
        ↓
PROCESSING_ROUTE_SELECTED
        ├─ NATIVE_TEXT
        ├─ OCR
        ├─ SPREADSHEET/TABLE
        ├─ MESSAGE/IMAGE
        └─ MANUAL/OTHER
        ↓
EXTRACTED_UNVERIFIED
        ↓
DOCUMENT_HUMAN_REVIEWED
        ↓
SOURCE_VERIFIED
        ↓
LEGAL_FACT_REVIEWED
        ↓
ANALYSIS_READY
```

At any state:

```text
BLOCKED | QUARANTINED | REJECTED | SUPERSEDED
```

### 6.2 Transition Matrix

| From → To | Preconditions | Recorded output | Prohibited shortcut |
|---|---|---|---|
| Received → Registered | Matter/purpose/source/access scope identified | Receipt and registry record | Received → Analysis Ready |
| Registered → Hash Verified | Accessible bytes; current SHA-256 and size recomputed | Integrity event | Path match → Hash Verified |
| Hash Verified → Text Assessed | File format readable; substantive scope identified | Page/region/sheet coverage map | Nonempty text → Complete coverage |
| Text Assessed → Route Selected | Native/OCR/table/manual needs explicit | Processing plan/version | OCR by default without assessment |
| Route Selected → Extracted Unverified | Candidate extraction linked to exact source/version and locators | Candidate extraction version | Extraction → Fact |
| Extracted → Document Reviewed | Human compares candidate to source regions | Review, corrections, limitations | OCR completed → Source Verified |
| Document Reviewed → Source Verified | Reviewed scope and correction lineage complete | Source-verified candidate references | Source Verified → Legal Fact automatically |
| Source Verified → Legal Fact Reviewed | Qualified lawyer reviews purpose, relevance, conflicts, and permitted use | Approval/rejection and scope | Technical reviewer → Legal approval |
| Legal Fact Reviewed → Analysis Ready | All required document and matter-bundle gates pass | Analysis-Ready Manifest | One ready file → Matter Ready |

### 6.3 Reprocessing and Invalidation

The following events revoke or reopen dependent readiness:

- file missing, denied, corrupt, or quarantined;
- hash mismatch or changed bytes;
- replacement, higher-quality copy, or superseding source;
- OCR/extraction correction affecting relied-upon text/data;
- newly identified omitted page, table, message, attachment, or region;
- review rejection, revocation, or scope reduction;
- new adverse/conflicting material;
- matter purpose, party scope, jurisdiction, or legal-analysis scope change;
- retention, confidentiality, or access rule change.

The Audit/Invalidation Ledger must identify every dependent extraction, Source-Verified Fact Candidate, Legal Fact Candidate, Analysis-Ready Manifest, and downstream analysis requiring re-review.

## 7. Text and OCR Governance

### 7.1 Text Readiness Assessment

Assessment occurs at the smallest practical source unit:

- PDF/image: page and region;
- spreadsheet: workbook, sheet, range/cell, formula/displayed-value context;
- message export: conversation, message ID, timestamp, sender, attachment;
- audio/video: time interval and channel;
- archive/container: child object;
- mixed document: each substantive embedded object.

Required observations:

- total and substantive page/region count;
- usable native-text coverage;
- missing, image-only, illegible, encrypted, corrupted, or unsupported regions;
- table, column, merged-cell, header/footer, footnote, annotation, stamp, signature, handwriting, and attachment coverage;
- ordering and relationship information needed to interpret extracted values.

### 7.2 Processing Routes

#### Native-Text Route

Use when verified native text covers the declared substantive scope. Native text still enters `EXTRACTED_UNVERIFIED` and requires source comparison, especially for reading order, tables, encoding, invisible text, or layout-dependent meaning.

#### OCR Route

Use for image-only or unreadable regions. The route records provider-neutral processing metadata, page/region locators, language, processing version, output version, and limitations. It does not select a provider or define an API.

#### Hybrid Route

Use when native text is partial. Preserve native and OCR outputs separately, identify which source regions each covers, and prevent duplicate/conflicting text from being silently merged.

#### Spreadsheet/Table Route

Preserve workbook/sheet/range identity, displayed values, formulas where relevant, merged cells, headers, units, debit/credit signs, dates, currencies, and row/column relationships. A flattened text dump is not sufficient when structure carries meaning.

#### Message/Image Route

Preserve sender/source attribution, timestamp, sequence, thread/context, attachment linkage, screenshot boundaries, truncation, edits/deletions if observable, and acquisition limitations. A screenshot is not automatically a complete conversation record.

#### Manual/Unsupported Route

If automated processing is unavailable or unreliable, record the blocked condition and approved manual transcription/review scope. Manual transcription has the same provenance, locator, review, and correction requirements.

### 7.3 OCR Risk Controls

| Risk | Required design control |
|---|---|
| Character substitution in names, amounts, dates, accounts, or article numbers | Exact source-region human comparison and correction lineage |
| Missing negation, qualifier, footnote, stamp, or handwritten note | Page/region completeness checklist |
| Multi-column or message-order error | Layout/sequence-aware review |
| Table row/column misalignment | Structural verification against image/native workbook |
| Wrong page/attachment association | Stable document-version and source locator |
| Low-quality or faint scan | Mark uncertain spans; require better source or manual review |
| Seal/signature misreading | Preserve as image evidence; no automated authenticity claim |
| High OCR confidence masking error | Confidence may prioritize review only; it cannot establish truth or support |

### 7.4 Mandatory Isolation Rule

```text
OCR Output
        ↓
Extracted Evidence Candidate
        ↓
Document Human Review
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Review
        ↓
Legal Fact Candidate
```

No technical OCR or extraction state may directly assign LRG-04 `SUPPORTED` to a legal proposition.

## 8. Evidence Verification Model

### 8.1 Three Independent Questions

| Gate | Question answered | Evidence considered | Responsible decision | Does not answer |
|---|---|---|---|---|
| File Identity Gate | “Are these the registered bytes/version?” | SHA-256, size, storage/version metadata | Integrity verifier | Source authenticity or truth |
| Evidence Source/Content Review | “Does the extraction match this source, and what is known about provenance/limitations?” | Original, acquisition record, locators, extraction, corrections | Document reviewer; legal specialist where needed | Legal Fact or proof sufficiency |
| Legal Fact Review | “May this source-verified candidate enter legal analysis for this matter/scope?” | Source record, fact candidate, conflicts, purpose, current law context | Qualified lawyer | Final merits or outcome |

### 8.2 Separation Invariant

```text
File Identity
        ↓ does not imply
Evidence Authenticity / Admissibility / Credibility
        ↓ does not imply
Legal Fact
        ↓ does not imply
Request Right or Outcome
```

Infrastructure records the decisions and their scope; it does not make substantive legal determinations.

### 8.3 Source-Verified Fact Candidate Contract

Every candidate made available to Legal Fact Review contains:

- evidence/document/version identity and current hash;
- exact source locator;
- source actor/origin and attribution uncertainty;
- source-faithful extracted text/data;
- normalization, if any, separately recorded;
- extraction method/version;
- human reviewer, date, and reviewed scope;
- corrections and supersession lineage;
- ambiguity, missing context, adverse/conflicting sources, and limitations;
- permitted matter and analytical purpose.

## 9. Matter Input Gate

### 9.1 Gate Flow

```text
Matter and Purpose Authorization
        ↓
Required Evidence Profile
        ↓
Evidence Registry Query
        ↓
Per-Document Identity / Processing / Review Gate
        ↓
Required-Category and Conflict Check
        ↓
Qualified Human Matter Authorization
        ↓
Analysis-Ready Manifest or Blocked Report
```

### 9.2 Required Evidence Profile

For each declared analytical scope, the profile records:

- required and optional evidence categories;
- acceptable source types and alternatives;
- minimum source/coverage requirements;
- confidentiality/access restrictions;
- document-review requirements;
- lawyer-review requirements;
- conflict/adverse-source expectations;
- stop conditions;
- responsible human approver.

The profile is a reviewable plan, not an automated statement of what evidence is legally sufficient.

### 9.3 Readiness Decision

#### READY

All critical required categories, document gates, known conflicts, access conditions, and human approvals pass for the recorded limited scope.

#### PARTIAL

Some materials or subscopes pass, while other categories/subscopes remain incomplete. The manifest explicitly separates ready and blocked scopes. `PARTIAL` never authorizes reasoning across a missing critical prerequisite.

#### BLOCKED

At least one critical required identity, access, processing, source-review, conflict-review, or lawyer-approval condition fails.

When blocked, the infrastructure may produce:

- missing-source and inaccessible-source lists;
- required page/region/text/OCR work;
- review and correction tasks;
- provenance or source-quality gaps;
- requests for supplemental evidence or authorized collection;
- a machine-readable and human-readable blocked report.

It may not produce:

- a final request-right judgment;
- a legal merits conclusion;
- a litigation strategy decision;
- an outcome or success prediction;
- generated facts to fill the gap.

### 9.4 Analysis-Ready Manifest

The conceptual manifest contains:

- matter, purpose, jurisdiction candidate, and scope;
- approved actor/reviewer identities;
- required evidence profile version;
- exact ready evidence/document versions and hashes;
- source-locator and extraction versions;
- Document Review and Legal Fact Review decisions;
- excluded, optional, missing, adverse, conflicting, and superseded materials;
- readiness result and blocking reasons;
- issue time, expiry/recheck condition, and invalidation links.

The manifest is not a factual finding, evidence ruling, legal opinion, or permission to exceed the stated scope.

## 10. Human Review Gates

### 10.1 Document Review Gate

Purpose: confirm extraction fidelity and completeness for the declared source scope.

Minimum checks:

- correct evidence/document/version and hash;
- source locator reproducibility;
- page/region/sheet/message coverage;
- names, amounts, dates, identifiers, signs, units, sequence, and layout;
- OCR/transcription errors and uncertain spans;
- missing pages, attachments, context, tables, stamps, signatures, or handwriting;
- correction history and reviewer attribution;
- known provenance and acquisition limitations.

Output:

```text
SOURCE_VERIFIED | REJECTED | PENDING | REVOKED
```

This gate does not approve legal relevance or truth.

### 10.2 Legal Fact Review Gate

Purpose: decide whether a Source-Verified Fact Candidate may enter legal analysis for the recorded matter and purpose.

Minimum checks:

- matter, parties, procedural posture, purpose, and access scope;
- source attribution and known authenticity/admissibility/completeness questions;
- adverse/conflicting material and missing context;
- proposed normalization and Legal Fact transformation rationale;
- current legal-authority needs and professional constraints;
- limitation of use and any required re-review trigger.

Output:

```text
LAWYER_APPROVED_FOR_ANALYSIS | REJECTED | PENDING | REVOKED
```

This gate does not automatically approve a request right, strategy, filing, or final advice.

### 10.3 Separation of Duties

The architecture records review role and scope separately. The same person may perform multiple roles only if later policy authorizes it and the distinct decisions remain explicit. An omitted review is never implied approval.

## 11. Audit, Correction, Supersession, and Invalidation

### 11.1 Minimum Audit Events

```text
Matter authorization
Evidence receipt
Registry creation
Storage/version assignment
Hash verification
Text assessment
Processing route selection
Extraction creation
OCR/manual correction
Document review
Source-verified candidate creation
Legal Fact review
Manifest readiness decision
Downstream consumption reference
Revocation / supersession / invalidation
```

Every event identifies actor/role, time, matter, evidence/document/version, action, prior/new state, reason, and affected scope.

### 11.2 Correction Rules

- Corrections create a new extraction/review version; they do not silently overwrite prior output.
- The original source and prior candidate remain traceable according to retention policy.
- A material correction identifies dependent source-verified facts, Legal Fact candidates, manifests, and analyses.
- Dependent objects reopen to `BLOCKED` or pending review until revalidated.
- Reviewer disagreement is preserved; it is not averaged into a confidence score.

### 11.3 Supersession Rules

- New file bytes produce a new document version and hash verification.
- A higher-quality scan may supersede processing output but does not automatically supersede source/provenance questions.
- A later export or duplicate copy does not automatically replace an original source record.
- Superseded records cannot remain silently analysis-ready.

## 12. Matter Isolation, Confidentiality, and Retention

### 12.1 Matter Isolation

- Every object and processing artifact inherits a matter ID and permitted purpose.
- Search, review, extraction, and manifest construction must respect the same boundary in any later implementation.
- Cross-matter reuse requires separate authorization and produces a distinct use record.
- Shared parties, filenames, hashes, custodians, or source systems do not authorize reuse.

### 12.2 Confidentiality and Sensitive Material

The design records handling restrictions and required legal review. It does not automatically determine privilege, trade-secret status, state-secret status, personal-information legality, confidentiality obligations, or admissibility.

### 12.3 Retention and Deletion Design Requirement

Any later implementation must define source retention, derived-output retention, legal hold, reviewer decisions, correction history, deletion authorization, secure disposal, and audit preservation. This Spec does not select retention periods or implement deletion.

## 13. Failure Modes and Safe Behavior

| Failure | Safe behavior |
|---|---|
| File missing or access denied | `BLOCKED`; preserve registered identity and gap; no extraction |
| Hash mismatch | Quarantine current bytes; create mismatch event; invalidate dependent readiness |
| Corrupt/encrypted/unsupported file | `BLOCKED`; request approved alternate source or manual path |
| Partial text layer | Route missing substantive regions to OCR/manual review; do not claim complete extraction |
| OCR failure or low-quality output | Retain uncertain spans and `BLOCKED`; do not repair by model invention |
| Table/message sequence lost | Reject affected extraction until structural review |
| Reviewer unavailable | Keep `PENDING`/`BLOCKED`; no implicit approval |
| Conflicting reviewer decisions | Preserve both and escalate to designated human authority |
| New adverse source | Reopen dependent manifest and Legal Fact review |
| Matter/access scope changes | Reauthorize and re-evaluate affected artifacts |
| Audit/invalidation event cannot be recorded | Fail closed; do not issue Analysis-Ready Manifest |

## 14. Nonfunctional Design Requirements

These requirements guide later design review; they are not implementation commitments.

| Quality | Requirement |
|---|---|
| Traceability | Every downstream candidate resolves to exact evidence/document/extraction/review versions |
| Determinism | Same bytes and policy inputs produce reproducible identity/coverage observations, subject to tool-version recording |
| Fail-closed safety | Missing critical state, audit, review, or scope information blocks readiness |
| Idempotent registration | Repeated intake does not create ambiguous identities; duplicate-byte/source distinctions remain explicit |
| Version awareness | Replacements/corrections do not silently inherit readiness |
| Explainability | Every blocked/partial/ready result has human-readable reasons and affected scope |
| Observability | Lifecycle, review, failure, and invalidation events are inspectable without exposing unauthorized matter content |
| Security | Least-privilege, matter isolation, encryption, secrets, and incident controls require later implementation design |
| Portability | Provider-specific OCR/storage/database details remain outside the governance contract |
| Human usability | Review packages expose source image/text side-by-side conceptually, locators, corrections, and limitations |

## 15. Interface Contracts

### 15.1 Intake Contract

Requires matter authorization, actor/purpose, source declaration, original material/reference, access scope, and handling restrictions. Produces a receipt event, not evidence validity.

### 15.2 Processing Contract

Requires identity-verified material and an approved processing route. Produces versioned extraction candidates and coverage metadata, not facts.

### 15.3 Document Review Contract

Requires original source access, extraction version, locator map, and reviewer authorization. Produces source-fidelity decision, corrections, and limitations.

### 15.4 Legal Fact Review Contract

Requires source-verified candidate, matter/purpose, conflicts, and review authority. Produces a limited legal-analysis-use decision, not final advice.

### 15.5 Downstream Legal Reasoning Contract

Provides only:

- Analysis-Ready Manifest for a declared scope;
- approved evidence/document/extraction/review versions;
- source-verified candidates and locators;
- adverse/conflicting/missing/blocked records;
- limitations and invalidation hooks.

The legal-reasoning layer must use LRG-04 states and LRG-05 Human Decision Governance independently.

## 16. Real-Case Revalidation Profile

Route A must later support revalidation without embedding case facts into the infrastructure design.

### 16.1 Profile Inputs

- approved case/matter ID and purpose;
- required evidence profile;
- per-file paths/object references and SHA-256 hashes;
- page/region/sheet/message coverage;
- extraction versions;
- Document Review decisions;
- Legal Fact Review decisions;
- missing/adverse/conflicting materials.

### 16.2 Frozen C02-III Availability Demonstration

The accepted C02-III snapshot may be used only to demonstrate gate behavior:

| Validation profile | Frozen availability | Expected infrastructure decision |
|---|---|---|
| CASE-A profile | 1 of 4 categories accessible and hash-verified | `PARTIAL` at infrastructure level; request-right validation remains `BLOCKED` for missing critical transaction materials |
| CASE-B profile | 0 of 5 categories accessible | `BLOCKED` |
| CASE-C profile | 0 of 4 categories accessible | `BLOCKED` |

The demonstration does not read new case content, extract facts, decide authenticity, or make a merits assessment.

### 16.3 Revalidation Success Conditions

The design can carry a future real-case rerun when:

- each relied-upon file has a stable identity and current hash;
- text/OCR coverage is recorded at source-unit level;
- extraction is human-verified;
- required source/provenance limitations remain visible;
- required categories and known conflicts are reviewed;
- a qualified lawyer approves the limited analysis-ready manifest;
- invalidation and audit hooks are testable;
- no blocked gap is replaced by generated facts.

## 17. Implementation Boundary and Preconditions

### 17.1 Explicitly Excluded

```text
OCR engine/provider selection
OCR execution
MCP integration
Database or object-store selection
Database schema/DDL
Vector database or RAG
API or event schema implementation
Workflow engine
Queue/job system
Skill or Agent changes
Code or test scripts
Infrastructure as code
Production deployment
```

### 17.2 Preconditions for a Future Implementation Handoff

A separate Project Owner-approved implementation Handoff would need to bind:

1. the adopted Route A Design Spec and Review/Decision hashes;
2. exact implementation components and file whitelist;
3. provider/security/privacy/data-residency assessment;
4. runtime schemas and migration governance;
5. access-control and matter-isolation enforcement design;
6. supported file types and processing limits;
7. OCR/extraction quality baselines and China-language test corpus;
8. reviewer roles, workbench behavior, and audit evidence;
9. failure, retry, manual fallback, rollback, revocation, and deletion procedures;
10. validation plan proving no OCR-to-Legal-Fact shortcut and no legal outcome automation.

No such implementation authorization exists.

## 18. Risk Register

| Risk | Design mitigation | Residual decision owner |
|---|---|---|
| Hash interpreted as authenticity | Three-gate verification separation and explicit labels | Qualified lawyer/evidence reviewer |
| OCR output treated as fact | Candidate workspace isolation plus Document Review Gate | Document reviewer |
| Source-verified text treated as Legal Fact | Legal Fact Review Gate | Qualified lawyer |
| Partial case bundle released | Required-evidence profile and scope-bound manifest | Matter review owner |
| Cross-matter leakage | Matter/access boundary and separate-use record | Access/confidentiality owner |
| Silent correction drift | Versioned corrections and dependency invalidation | Registry/audit owner |
| Provider-specific lock-in | Provider-neutral responsibilities and contracts | Future Architecture Review |
| Technical confidence becomes merits score | Prohibit confidence-to-LRG-state mapping | Governance owner |
| Review bottleneck encourages bypass | Fail closed; explicit pending/blocked status | Project Owner / operations design |
| Missing audit event | No Analysis-Ready Manifest | Infrastructure governance owner |

## 19. Acceptance Criteria Assessment

| ID | Status | Design evidence |
|---|---|---|
| `ROUTE-A-001` — Evidence Object complete | **PASS** | Section 4 defines identity, matter, source, version, hash, type, access, processing, reviews, readiness, limitations, correction, and supersession |
| `ROUTE-A-002` — Lifecycle traceable / OCR isolated from Legal Fact | **PASS** | Sections 6–8 define transitions, prohibit jumps, isolate extraction candidates, and separate three verification questions |
| `ROUTE-A-003` — Supports C02-IV Input Gate | **PASS** | Sections 5 and 9 preserve independent states, document gate, case-bundle gate, required gaps, and qualified authorization |
| `ROUTE-A-004` — Supports LRG-01/LRG-02 | **PASS** | Sections 2–3 map components/trust zones to canonical Evidence and Fact Governance while retaining LRG-00/04/05 |
| `ROUTE-A-005` — No implementation | **PASS** | Provider-neutral documentation only; Section 17 explicitly excludes all implementation assets |
| `ROUTE-A-006` — Can carry real-case revalidation | **PASS** | Section 16 defines a reusable profile, frozen gap demonstration, and future success conditions without merits analysis |

## 20. Final Design Status

```text
Route A Evidence Infrastructure Design:
DONE — DESIGN ONLY

Acceptance Criteria:
6 / 6 PASS

Architecture Review:
PENDING

Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient is the **Architecture Coordinator (ChatGPT)** for review of this Spec and the corresponding Result. Only a separate Project Owner closeout and later implementation Handoff may authorize technical implementation.
