# TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-IV Evidence Input Readiness Design |
| Version | v1.0 design execution artifact |
| Execution date | 2026-07-20 |
| Mode | Documentation-only design |
| Status | **DONE — DESIGN ONLY** |
| Handoff SHA-256 | `59BCD1151CFFA0E871B752B7BAA9809C712C918D8A6488D2DDBA9F13542214D2` |
| Execution authority | Project Owner `ACCEPTED` decision in the current coordination record |
| C02-III Validation Enhancement Spec SHA-256 | `96C1532A2B448C4B3DB0A2926172CC7374B02E42DDF61B714295E534B4A74DFD` |
| C02-III Validation Enhancement Result SHA-256 | `AF534A372D4B4824F4F402485691372D8081B4D430302DC9E3B2B0D89A9ED226` |

This artifact defines an Evidence Input Readiness design for the `litigation-legal` domain. It is not an executable schema, runtime state machine, OCR pipeline, database design, automation implementation, evidence-authenticity determination, legal opinion, or request-right merits analysis.

## 1. Purpose and Non-Goals

C02-IV defines the admission controls that must be satisfied before case material may support fact extraction and request-right validation:

```text
Evidence Material
        ↓
Identity and Access Verification
        ↓
Text / OCR Readiness
        ↓
Source-Bounded Extraction
        ↓
Human Source Verification
        ↓
Legal Fact Candidate Review
        ↓
Request Right Validation
```

The design addresses the C02-I and C02-III findings that a request-right model cannot be reliably exercised where paths drift, hashes cannot be reproduced, text layers are unavailable, OCR output is unverified, or required materials are incomplete.

Non-goals:

- implementing OCR, parsers, storage, databases, queues, workflow engines, or interfaces;
- modifying Skills, Agents, code, MCP, Workflow, CLAUDE.md, or runtime schemas;
- declaring a document authentic, admissible, complete, credible, or sufficient;
- generating case facts from labels, filenames, inventories, or missing materials;
- selecting a request right, litigation strategy, case outcome, or success probability;
- replacing the judgment of a qualified lawyer.

## 2. Design Principles

1. **Byte identity before content use**: a material must have a stable identity and verified byte hash before extraction output may be relied upon.
2. **Path is a locator, not identity**: storage paths may drift; path, object reference, version, and hash must remain distinguishable.
3. **Text presence is not extraction accuracy**: an embedded text layer may be partial, malformed, misordered, or detached from the page layout.
4. **OCR output is a candidate transcription**: OCR never becomes a verified fact or legal fact automatically.
5. **Source verification is not truth adjudication**: human confirmation that extracted text matches a source does not decide authenticity, admissibility, credibility, or probative weight.
6. **Facts remain layered**: Raw Evidence, Extracted Evidence Candidate, Source-Verified Fact, and Legal Fact Candidate are independent objects with traceable transitions.
7. **Required gaps block analysis**: missing or unverified required inputs produce `BLOCKED`; the system does not compensate with inference.
8. **Case isolation**: a material may be used only within its approved matter and access scope unless separately authorized.
9. **Correction is append-only in meaning**: replacement, re-extraction, and review reversal create traceable versions; they do not silently overwrite provenance.
10. **Human control**: a qualified lawyer retains final authority over legal relevance, request-right use, burden positions, and downstream application.

## 3. Evidence Material Registry

### 3.1 Registry Record

The following is a conceptual documentation contract, not a runtime schema.

| Field | Purpose | Required readiness rule |
|---|---|---|
| `evidence_id` | Stable evidence-level identifier | Immutable after registration |
| `case_id` | Bound matter/case identifier | Must match the approved analysis scope |
| `document_id` | Stable document/version identifier | Required; a replacement receives a new version identity |
| `original_filename` | Original source filename | Preserved exactly where available |
| `storage_reference` | Approved path or object reference | Must resolve at readiness check time |
| `storage_version` | Version, generation, or snapshot reference | Required where the source can change in place |
| `sha256` | Byte-level identity | Must be present and independently recomputed |
| `byte_size` | File-size cross-check | Must match the registered version |
| `document_type` | PDF, image, spreadsheet, message export, audio, etc. | Must be recognized or marked `UNKNOWN` |
| `source_description` | Custodian, system, person, or acquisition source | Must preserve attribution and uncertainty |
| `received_at` | Receipt time | Required for audit chronology |
| `registered_at` | Registry-entry time | Required |
| `registered_by` | Human or approved service that registered the material | Required |
| `access_scope` | Case, team, confidentiality, and permitted-use boundary | Must authorize the intended validation use |
| `access_status` | Current accessibility state | Must be `ACCESSIBLE` for readiness |
| `hash_status` | Integrity-verification state | Must be `VERIFIED` for readiness |
| `text_layer_status` | Machine-readable text coverage | Must be verified or routed to OCR/manual transcription |
| `ocr_status` | OCR need and verification state | If required, must reach `HUMAN_VERIFIED` |
| `extraction_status` | Source-bounded extraction state | Must reach `HUMAN_VERIFIED` |
| `human_review_status` | Required source and legal-use review state | Must reach the review level required by the gate |
| `readiness_status` | Input-gate result | `ANALYSIS_READY` or `BLOCKED` only |
| `blocking_reasons` | Explicit missing prerequisites | Required whenever status is `BLOCKED` |
| `supersedes` / `superseded_by` | Version lineage | Required after replacement |
| `correction_history` | Extraction/review corrections | Append-only record |
| `limitations` | Missing pages, illegibility, truncation, format or source caveats | Must be visible downstream |

### 3.2 Registry Identity Invariants

- The same `evidence_id` may not point to different byte content without a new document/version record.
- A matching filename or path does not substitute for a matching hash.
- A matching hash confirms byte identity only; it does not confirm authenticity or legal effect.
- A directory-level label such as `Bound Multiple` is not sufficient for analysis readiness. Each relied-upon child file requires its own document ID, path/object reference, hash, type, and processing status.
- A missing file remains `BLOCKED`; an old hash in a manifest does not make the file accessible.
- Any hash mismatch, source replacement, access-scope change, or processing correction invalidates the prior readiness determination until re-review.

## 4. Independent Status Dimensions

Readiness must not be represented by one overloaded lifecycle value. The Registry records independent dimensions and derives a gate result from them.

### 4.1 Access Status

| Value | Meaning |
|---|---|
| `UNKNOWN` | Accessibility has not been checked |
| `ACCESSIBLE` | The registered material can be opened within the approved scope |
| `MISSING` | The registered path/object does not resolve |
| `DENIED` | The material exists but current access is not authorized |
| `CORRUPT` | The file cannot be read as its declared type |
| `QUARANTINED` | Use is suspended because of integrity, security, or scope concerns |

Only `ACCESSIBLE` may proceed.

### 4.2 Hash Status

| Value | Meaning |
|---|---|
| `NOT_COMPUTED` | No approved byte hash exists |
| `REGISTERED_ONLY` | A prior hash is recorded but has not been recomputed in the current readiness check |
| `VERIFIED` | Current bytes match the registered SHA-256 |
| `MISMATCH` | Current bytes differ from the registered identity |
| `NOT_AVAILABLE` | Bytes are inaccessible, so identity cannot be verified |

Only `VERIFIED` may proceed.

### 4.3 Text Layer Status

| Value | Meaning |
|---|---|
| `UNKNOWN` | Coverage not checked |
| `AVAILABLE_COMPLETE` | Usable text exists for all substantive pages/regions in scope |
| `AVAILABLE_PARTIAL` | Some substantive pages/regions lack usable text or have layout loss |
| `UNAVAILABLE` | No usable text layer exists |
| `NOT_APPLICABLE` | The format is not expected to contain a text layer |

`AVAILABLE_COMPLETE` still requires extraction verification. `AVAILABLE_PARTIAL`, `UNAVAILABLE`, or an image-only format routes the affected scope to OCR or approved manual transcription.

### 4.4 OCR Status

| Value | Meaning | May proceed? |
|---|---|---|
| `NOT_REQUIRED` | Verified text/source access is adequate for the declared scope | Yes, subject to extraction review |
| `REQUIRED` | OCR is needed for one or more substantive regions | No |
| `COMPLETED_UNVERIFIED` | OCR output exists but has not been checked against the image | No |
| `HUMAN_VERIFIED` | OCR output was checked against identified image regions by an authorized reviewer | Yes, for the verified scope only |
| `FAILED` | OCR output is unusable or materially unreliable | No |
| `NOT_AVAILABLE` | OCR cannot be performed or accessed | No where OCR is required |

### 4.5 Extraction Status

| Value | Meaning |
|---|---|
| `NOT_STARTED` | No source-bounded extraction exists |
| `EXTRACTED_UNVERIFIED` | Candidate text/data was extracted but not checked against the source |
| `HUMAN_VERIFIED` | Extraction and locators were checked against the source for the approved scope |
| `REJECTED` | The extraction was found unreliable or out of scope |
| `SUPERSEDED` | A later reviewed extraction replaces this version |

### 4.6 Human Review Status

| Value | Meaning |
|---|---|
| `NOT_REQUIRED` | Only where the approved policy explicitly permits no human verification; never sufficient for creating a Legal Fact Candidate |
| `REQUIRED` | A reviewer must be assigned |
| `PENDING` | Review is assigned or underway |
| `SOURCE_VERIFIED` | Extraction matches the identified source and locator within stated limits |
| `LAWYER_APPROVED_FOR_ANALYSIS` | A qualified lawyer approved the source-verified material for the stated legal-analysis scope |
| `REJECTED` | The material or extraction may not be used for the stated scope |
| `REVOKED` | Earlier approval was withdrawn after correction, new conflict, or scope change |

## 5. Material Lifecycle and Transition Controls

The lifecycle is a documentation-level control model:

```text
RECEIVED
        ↓
REGISTERED
        ↓
IDENTITY_VERIFIED
        ↓
PROCESSING_ROUTE_SELECTED
        ↓
TEXT_EXTRACTED / OCR_COMPLETED_UNVERIFIED
        ↓
SOURCE_VERIFIED
        ↓
LAWYER_APPROVED_FOR_ANALYSIS
        ↓
ANALYSIS_READY
```

At any step, the material may enter `BLOCKED`, `QUARANTINED`, `REJECTED`, or `SUPERSEDED` with an explicit reason.

| Transition | Required conditions | Required record | Blocking examples |
|---|---|---|---|
| Received → Registered | Case identity, source, filename/type, receipt time, approved storage reference | Registry record and access scope | Unknown case, prohibited source, missing storage reference |
| Registered → Identity Verified | File accessible; SHA-256 and size recomputed | Hash result, verifier, verification time | Missing file, hash mismatch, unreadable file |
| Identity Verified → Route Selected | Type and page/region coverage inspected | Text-layer assessment and OCR/manual route | Unsupported or corrupt format, unclear substantive scope |
| Route Selected → Extracted | Embedded text or OCR/manual transcription generated with locators | Extraction version, method, page/region coverage | Extraction failure, incomplete pages, lost tables |
| Extracted → Source Verified | Human comparison to the source completed | Reviewer identity, review scope, corrections, limitations | OCR/transcription error, missing source page, unresolved layout |
| Source Verified → Lawyer Approved | Qualified lawyer confirms permitted analytical use and remaining caveats | Approval scope, date, unresolved conflicts | Wrong matter, privilege/confidentiality concern, insufficient provenance |
| Lawyer Approved → Analysis Ready | All required document- and bundle-level gates pass | Readiness decision and reason | Missing required material, stale hash, later correction |

### 5.1 Reopening Triggers

An `ANALYSIS_READY` record returns to `BLOCKED` when any of the following occurs:

- the file at the storage reference changes or disappears;
- the registered and recomputed hashes no longer match;
- a replacement or higher-quality version is received;
- a text/OCR/extraction correction changes a relied-upon proposition;
- a reviewer revokes approval or identifies a material omission;
- confidentiality, privilege, personal-information, or case-scope restrictions change;
- the downstream analysis scope expands beyond the reviewed pages, fields, or purpose.

## 6. OCR and Text-Layer Readiness

### 6.1 Coverage Assessment

Text readiness must be assessed at page, sheet, region, or message-range level as appropriate. A non-empty document-level character count is insufficient. The assessment records:

- total and substantive page/region count;
- pages/regions with usable embedded text;
- pages/regions requiring OCR or manual transcription;
- tables, forms, stamps, signatures, handwriting, images, footnotes, headers, and annotations that may not survive extraction;
- ordering, column, cell, merged-region, formula, date, currency, decimal, and sign conventions;
- password, encryption, corruption, truncation, or unsupported-format issues.

### 6.2 OCR Risk Catalogue

| Risk | Example consequence | Required control |
|---|---|---|
| Character substitution | Party name, amount, date, account or article number changes | Human comparison at the exact image locator |
| Omission | A negation, qualifier, seal, handwritten note, or footnote disappears | Page/region coverage checklist |
| Reading-order error | Multi-column text or conversation sequence is reordered | Layout-aware comparison and chronological review |
| Table reconstruction error | Rows, columns, totals, debit/credit, or counterparties are misaligned | Cell/row-level verification against the image or native workbook |
| Page association error | Text is linked to the wrong page or attachment | Stable page/image locator and document hash |
| Low-quality image | Faint text or compression artifacts create uncertain output | Mark uncertain spans and require re-scan or manual transcription |
| Language/encoding error | Chinese names, uncommon characters, symbols, or punctuation change | Reviewer correction with original image retained |
| Stamp/signature misreading | Apparent seal/signature content is invented or missed | Treat as image evidence; no automated authenticity conclusion |

### 6.3 Mandatory OCR Boundary

This path is prohibited:

```text
OCR Output
        ↓
Legal Fact
```

The only permissible design path is:

```text
Raw Image Evidence
        ↓
OCR Candidate Transcription
        ↓
Human Source Verification
        ↓
Source-Verified Fact Candidate
        ↓
Qualified Lawyer Review
        ↓
Legal Fact Candidate
```

Human verification applies only to transcription fidelity and stated source attribution. It does not decide whether the underlying statement is true or legally sufficient.

## 7. Evidence Confidence Layers

### 7.1 Layer Definitions

| Layer | Definition | What it does not establish |
|---|---|---|
| Raw Evidence | The registered file/object and its preserved bytes, metadata, source, and access scope | Authenticity, admissibility, completeness, truth, or relevance |
| Extracted Evidence Candidate | Machine- or human-produced text/data linked to a source locator and method | Accurate transcription until verified; truth or legal meaning |
| Source-Verified Fact Candidate | A proposition whose transcription/normalization was checked against the identified source | Objective truth, credibility, proof sufficiency, or legal consequence |
| Legal Fact Candidate | A lawyer-reviewable characterization mapped to a legal question or constituent element | Judicial fact, final request right, burden decision, or outcome |

The phrase “Verified Fact” in the Handoff is implemented as **Source-Verified Fact Candidate** to prevent the review of transcription fidelity from being misread as a finding of truth.

### 7.2 Source-Verified Fact Record

A source-verified candidate must retain:

- evidence ID and exact document version;
- page/sheet/cell/message/time/region locator;
- source actor or record origin, including `UNKNOWN` where necessary;
- verbatim or source-faithful extracted text/data;
- normalized proposition, with transformations separately explained;
- extraction method and version;
- reviewer identity, review date, and reviewed scope;
- ambiguity, illegibility, missing context, counter-source, and conflict markers;
- correction/supersession history;
- permitted analytical scope and access restrictions.

### 7.3 Legal Fact Promotion Rule

A Source-Verified Fact Candidate may become input to a Legal Fact Candidate only when:

1. the document is `ANALYSIS_READY` for the relevant scope;
2. the source locator and transformation rationale are preserved;
3. supporting, adverse, and conflicting sources remain visible;
4. a qualified lawyer reviews legal relevance, current authority, and uncertainty;
5. the result remains labelled a candidate and not a judicial fact.

## 8. Evidence Input Gate

### 8.1 Document-Level Gate

A document is `ANALYSIS_READY` only if all applicable conditions are satisfied:

| Gate | Required condition |
|---|---|
| Identity | Stable evidence/document IDs; current byte hash equals the registered SHA-256 |
| Access | Material is accessible and use is permitted for the stated case and purpose |
| Coverage | All substantive pages/regions needed for the scope have a verified text or transcription route |
| OCR | If required, OCR output is `HUMAN_VERIFIED` for the relied-upon scope |
| Extraction | Source-bounded extraction is `HUMAN_VERIFIED` with locators and limitations |
| Human review | Qualified reviewer approval is complete for the requested analytical use |
| Version | The material and extraction are current, not superseded, revoked, or stale |
| Isolation | No cross-case or unauthorized-person disclosure is required for use |

If any applicable condition fails, the document is `BLOCKED`.

### 8.2 Case-Bundle Gate

Document readiness does not imply matter readiness. Before request-right validation begins, a qualified lawyer or approved case plan identifies which evidence categories are `required_for_analysis` for the declared scope.

The case bundle is `ANALYSIS_READY` only when:

- every required material category has at least one analysis-ready source, or an explicitly approved reason why the category is not required;
- party identity, procedural posture, requested legal effect, and current scope are confirmed;
- source conflicts and known missing categories are visible;
- evidence access complies with case isolation and confidentiality constraints;
- no required gap is hidden by an optional or unrelated document.

Missing optional material remains visible but does not automatically block the whole bundle. Missing required material always blocks the affected request-right validation scope.

### 8.3 Blocking Reason Codes

| Code | Meaning |
|---|---|
| `FILE_MISSING` | Required file/object cannot be resolved |
| `ACCESS_DENIED` | Current access scope does not permit use |
| `HASH_MISSING` | No registered SHA-256 exists |
| `HASH_MISMATCH` | Current bytes differ from the registered identity |
| `FORMAT_UNREADABLE` | File is corrupt, encrypted, or unsupported |
| `TEXT_COVERAGE_INCOMPLETE` | Required substantive regions lack usable text |
| `OCR_REQUIRED` | OCR/manual transcription is required but incomplete |
| `OCR_UNVERIFIED` | OCR output exists without human comparison |
| `EXTRACTION_UNVERIFIED` | Extracted content lacks source verification |
| `HUMAN_REVIEW_PENDING` | Required reviewer approval is incomplete |
| `SOURCE_CONFLICT_UNRESOLVED` | Material conflict is not recorded or reviewed |
| `SCOPE_NOT_AUTHORIZED` | Intended case/purpose exceeds approved use |
| `VERSION_SUPERSEDED` | A newer or corrected version invalidates this record |

### 8.4 Gate Decision Matrix

| Situation | Document result | Case-bundle effect |
|---|---|---|
| Required file missing | `BLOCKED` | Affected validation scope blocked |
| Hash mismatch | `BLOCKED` and quarantine/rebind required | Affected scope blocked |
| Complete embedded text but extraction unverified | `BLOCKED` | No downstream fact use |
| OCR completed but not human-verified | `BLOCKED` | No downstream fact use |
| OCR human-verified only for selected pages | Ready only for that recorded scope | Other required regions remain blocked |
| Source extraction verified but lawyer review pending | `BLOCKED` for legal analysis | No Legal Fact Candidate promotion |
| Optional file missing; all required inputs ready | Optional item remains a visible gap | Bundle may be ready for the declared limited scope |
| Required inputs ready and lawyer approves scope | `ANALYSIS_READY` | Request-right validation may begin within that scope |

## 9. Downstream Contract to Request-Right Validation

C02-II/C02-III may consume only:

1. Registry records with `readiness_status = ANALYSIS_READY` for the declared case and purpose;
2. Source-Verified Fact Candidates with stable source locators and current document hashes;
3. explicit limitations, conflicts, adverse sources, and blocking reasons;
4. the lawyer-approved scope and review identity.

Downstream systems must not consume:

- raw OCR output;
- unverified extraction;
- inaccessible file labels or prior summaries as evidence;
- directory counts without per-file identity;
- source-verified text as an automatic Legal Fact;
- ready documents from another case without separate authorization.

The downstream result remains:

```text
Evidence Input
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Candidate
        ↓
Element Fact Candidate
        ↓
Request Right Candidate
        ↓
Qualified Lawyer Decision
```

## 10. Human Review Gate

### 10.1 Review Levels

| Review level | Reviewer responsibility |
|---|---|
| Registry review | Confirm identity, source, storage reference, hash, type, access scope, and version |
| Extraction review | Compare text/data to exact source regions; record errors, gaps, and corrections |
| Evidence-use review | Confirm confidentiality, case isolation, purpose, and known authenticity/admissibility/completeness questions |
| Legal-analysis review | Qualified lawyer assesses relevance, current authority, element mapping, conflicts, defenses, and permitted use |

One approval may not silently stand in for another. The final Legal Fact Candidate requires qualified-lawyer review even where transcription was verified by another authorized reviewer.

### 10.2 Minimum Review Checklist

- correct case, party, document, version, hash, and source;
- source locator is reproducible;
- extracted text/data matches the source for the reviewed scope;
- omitted, illegible, handwritten, stamped, tabular, or image-only regions are recorded;
- dates, amounts, names, account identifiers, signs, units, and sequence are checked;
- attribution distinguishes a source statement from an objective event;
- adverse, conflicting, or superseding material remains visible;
- confidentiality, personal-information, trade-secret, and privilege-like concerns are flagged for human legal review without automated determination;
- the intended downstream use stays within the approved scope;
- no authenticity, admissibility, credibility, probative-weight, or outcome conclusion is implied by readiness.

## 11. Case Isolation, Confidentiality, and Auditability

### 11.1 Case Isolation

- Every material is bound to a `case_id` and approved access scope.
- Cross-case reuse is blocked unless a separate legal and access review authorizes it.
- A shared person, company, filename, or source system does not authorize cross-matter transfer.
- Registry searches and generated indexes must preserve matter-level restrictions in any later implementation.

### 11.2 Confidentiality Boundary

Input readiness records may flag sensitivity and handling restrictions, but the design does not automatically decide legal privilege, state-secret status, trade-secret status, or admissibility. Those determinations remain with qualified humans under applicable China Mainland law and case-specific obligations.

### 11.3 Audit Record

Every later implementation must preserve an auditable sequence of:

```text
Receipt
→ Registration
→ Hash Verification
→ Processing Route
→ Extraction Version
→ Human Corrections
→ Source Verification
→ Lawyer Approval Scope
→ Readiness Decision
→ Revocation / Supersession, if any
```

## 12. Validation Scenarios

| Scenario | Expected design behavior | Result |
|---|---|---|
| V01 — File listed in an old manifest but missing now | Recheck path/object; mark `FILE_MISSING`; block use | PASS |
| V02 — Same filename, different bytes | Mark `HASH_MISMATCH`; do not inherit prior readiness | PASS |
| V03 — PDF has embedded text on only some substantive pages | Mark `AVAILABLE_PARTIAL`; route missing regions to OCR/manual review | PASS |
| V04 — OCR output exists without human comparison | Mark `OCR_UNVERIFIED`; block extraction promotion | PASS |
| V05 — OCR text was reviewed but authenticity is disputed | Allow source-fidelity record only; preserve authenticity question; lawyer review required | PASS |
| V06 — Spreadsheet text is readable but cell relationships were lost | Block affected extraction until sheet/cell structure is verified | PASS |
| V07 — Reviewer corrects an extracted amount | Create correction/version trace; invalidate dependent readiness and analysis | PASS |
| V08 — Required material missing while optional material exists | Block affected scope; do not substitute optional evidence | PASS |
| V09 — Material is ready in another case | Block cross-case use without separate authorization | PASS |
| V10 — All required materials and reviews pass | Mark only the approved scope `ANALYSIS_READY` | PASS |

## 13. C02-I / C02-III Problem Closure Mapping

| Observed problem | C02-IV design control | Design-level closure | Physical problem solved? |
|---|---|---|---|
| Path drift and inaccessible WPS materials | Stable document/version identity plus current accessibility recheck | YES | NO |
| Prior hash recorded but current bytes unavailable | Separate `REGISTERED_ONLY`, `VERIFIED`, and `NOT_AVAILABLE` states | YES | NO |
| Directory-level binding without per-file hashes | Per-child document identity invariant | YES | NO |
| Partial or absent PDF text layers | Page/region coverage status and OCR/manual routing | YES | NO |
| OCR output could be mistaken for fact | OCR candidate → human verification → source-verified fact boundary | YES | Not applicable until implemented |
| Source-verified text could be mistaken for legal fact | Independent qualified-lawyer promotion gate | YES | Not applicable until used |
| One accessible document amid a materially incomplete case | Required-category case-bundle gate | YES | NO |
| Missing facts were at risk of being inferred | Explicit blocking reasons and no-substitution rule | YES | YES as a governance rule |
| Cross-case evidence leakage risk | Case ID, access scope, and separate reuse authorization | YES | Not implemented |

C02-IV closes the **design gap**. It does not restore missing files, perform OCR, verify extraction, populate a database, or make current CASE-A/B/C analysis-ready.

## 14. Current Readiness Snapshot

Using the accepted C02-III results as the frozen factual basis:

| Case | Current verified availability | Design-gate determination | Reason |
|---|---|---|---|
| CASE-A | 1 of 4 categories accessible and hash-verified | `BLOCKED` | Required transaction, communication, account, and payment inputs remain unavailable; complete human-review approval is not recorded |
| CASE-B | 0 of 5 categories accessible | `BLOCKED` | No source can pass identity, text/OCR, extraction, or human-review gates |
| CASE-C | 0 of 4 categories accessible | `BLOCKED` | Required enforcement, property, and derivative-litigation inputs remain unavailable |

This snapshot is not a new case analysis. It demonstrates the proposed gate against the accepted C02-III registry findings.

## 15. Acceptance Criteria Assessment

| AC | Status | Design evidence |
|---|---|---|
| AC-C02-IV-001 — Describe the complete material lifecycle | **PASS** | Sections 3–5 define registration, identity, routing, extraction, review, readiness, reopening, and supersession |
| AC-C02-IV-002 — Distinguish Raw Evidence and Verified Fact | **PASS** | Section 7 separates four layers and narrows “Verified Fact” to a Source-Verified Fact Candidate |
| AC-C02-IV-003 — Identify unverified OCR risk | **PASS** | Section 6 defines page/region coverage, OCR states, risk catalogue, and mandatory human comparison |
| AC-C02-IV-004 — Block incomplete input from request-right validation | **PASS** | Section 8 provides document- and case-bundle gates, blocking codes, and a decision matrix |
| AC-C02-IV-005 — Preserve Human Review Gate | **PASS** | Section 10 separates registry, extraction, evidence-use, and qualified-lawyer review |
| AC-C02-IV-006 — Zero code and zero Skill modification | **PASS** | This task creates documentation outputs only; repository verification is recorded in the Result |

## 16. Preconditions for Any Future Implementation

Implementation remains **NOT AUTHORIZED**. A future implementation request would require a separate reviewed Handoff that binds at minimum:

- authoritative Registry ownership and storage/version semantics;
- permitted file types, maximum sizes, corruption and encryption handling;
- approved hash, OCR, extraction, and page/region coverage methods;
- reviewer roles, competence, assignment, and approval/revocation rules;
- confidentiality, personal-information, trade-secret, retention, deletion, and case-isolation controls;
- correction, supersession, audit-log, and downstream invalidation behavior;
- a test corpus including Chinese names, amounts, dates, tables, seals, signatures, handwriting, partial text layers, and low-quality scans;
- failure, rollback, and manual-fallback procedures;
- confirmation that no readiness flag becomes an authenticity, admissibility, credibility, proof-sufficiency, merits, or outcome conclusion.

No provider, OCR engine, database, queue, schema, workflow, or production architecture is selected by this design.

## 17. Final Design Determination

```text
C02-IV Input Readiness Design:
DONE — DESIGN ONLY

Design acceptance criteria:
6 / 6 PASS

Current case-material readiness:
CASE-A BLOCKED
CASE-B BLOCKED
CASE-C BLOCKED

Implementation:
NOT AUTHORIZED
```

The design supplies a stable conceptual boundary between evidence receipt and request-right validation. It resolves the governance-model gap identified in C02-I/C02-III while correctly leaving the existing physical material gaps unresolved. The next governance step is Architecture Coordinator review of this Spec and the corresponding Result, followed by a Project Owner closeout decision.
