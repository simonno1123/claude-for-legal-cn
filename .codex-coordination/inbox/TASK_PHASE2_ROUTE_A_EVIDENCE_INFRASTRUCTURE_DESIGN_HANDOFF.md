# TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN |
| Task Type | Evidence Infrastructure Architecture Design |
| Route | Phase 2 / Route A |
| Target Domain | `litigation-legal` evidence-input boundary |
| Execution Mode | **DESIGN ONLY** |
| Execution | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

Materialization of this Handoff establishes a proposed design task and its input identities only. It does not authorize creation of the Design Spec/Result or any OCR, document-AI, database, workflow, MCP, Skill, Agent, code, or production asset.

## 1. Task Position and Objective

Route A converts the accepted C02-IV Input Readiness Design and the canonical LRG-01/LRG-02 governance controls into a reviewable **Evidence Infrastructure physical architecture design**.

The design objective is to define an Evidence Infrastructure Layer whose responsibility is:

> ensure that data admitted to legal reasoning has traceable identity, source, processing lineage, review status, access boundary, and an explicit readiness decision.

The task is architecture design, not:

```text
OCR Development
Document AI Implementation
MCP Integration
Evidence Database Construction
Production Deployment
```

The design must remain independent from the merits, facts, parties, or outcomes of any specific case. Real-case references may appear only as validation profiles or failure scenarios without substantive analysis.

## 2. Fixed Input Baseline Binding

Before any design execution, Codex must recompute and exactly match every required input hash below. Any mismatch, missing artifact, ambiguous identity, or superseding governance decision yields `BLOCKED` and prohibits output creation.

### 2.1 Input 001 — LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 Canonical

| Artifact | Path | SHA-256 |
|---|---|---|
| Canonical Governance Pattern | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` |
| Pattern Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_GOVERNANCE_C01_LEGAL_REASONING_PATTERN_ADOPTION_DECISION.md` | `A275B101843D4DDEC82715AC4857C2DEBB576292FDF29481D38FE069F88E1CD2` |

Status:

```text
v1.0 CANONICAL — ADOPTED
```

Binding purpose:

- LRG-00 matter, purpose, access, and isolation boundary;
- LRG-01 Evidence Object identity, source, hash, lifecycle, processing, review, and readiness governance;
- LRG-02 Raw Evidence → Extracted Evidence Candidate → Source-Verified Fact Candidate → Legal Fact Candidate separation;
- LRG-04 controlled legal-reasoning states (`SUPPORTED`, `UNKNOWN`, `BLOCKED`);
- LRG-05 qualified-human decision boundary;
- Route Adapter conformance and prohibition on bypassing the governance core.

The Route A design may instantiate physical architecture concepts for LRG-01/LRG-02 but may not amend, supersede, relax, or reinterpret the canonical Pattern.

### 2.2 Input 002 — C02-IV Input Readiness Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Input Readiness Design Spec | `docs/phase2/track-c/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_SPEC.md` | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` |
| Input Readiness Design Result | `.codex-coordination/outbox/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_RESULT.md` | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` |
| Architecture Review | `.codex-coordination/reviews/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_REVIEW.md` | `46A1F6CAD52A2F73421804AED701D1AEC8214B37C55040148E1611C3A3DE5402` |
| Project Owner Decision | `.codex-coordination/decisions/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_DECISION.md` | `4ACEAECA570721CF6A1B2B0882D0D2068B51CFF7B88BB876CA0F8554F2EF4478` |

Status:

```text
CLOSED / DONE — DESIGN ONLY
```

Binding purpose:

- Evidence Material Registry fields and identity invariants;
- independent access, hash, text-layer, OCR, extraction, review, and readiness states;
- document and case-bundle admission gates;
- correction, supersession, audit, and downstream invalidation requirements;
- source-verification and qualified-lawyer review boundaries.

The C02-IV Decision's original hold on implementation remains effective. This Route A Handoff seeks architecture-design review only and does not authorize implementation.

### 2.3 Input 003 — External Advisory Review

| Artifact | Path | SHA-256 |
|---|---|---|
| External Advisory Review Report | `.codex-coordination/outbox/TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW_REPORT.md` | `F091FB8A53415F6DE152942A5144BE797F28BB2833C4EBE3A433CBFD4E592F77` |
| Architecture Coordinator Assessment | `.codex-coordination/reviews/TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW_ASSESSMENT.md` | `26B2B0BBF82FEBF2E1CDFDD90159E5F3B4399CCB645E2ABCB1FD33A1685D2719` |
| External Advisory Closeout / Route Decision | `.codex-coordination/decisions/TASK_PHASE2_GOVERNANCE_EXTERNAL_ADVISORY_REVIEW_CLOSEOUT_DECISION.md` | `2F575AA6EA40DA192B7847DCB94864F4CA2F7D0F970CDCC6E145FA4A5305713D` |

Status:

```text
EXTERNAL ADVISORY: CLOSED / ACCEPTED
ROUTE A: UNFROZEN FOR DESIGN HANDOFF
```

Binding purpose:

- records the independent pressure-test conclusion that the canonical Pattern has no critical structural defect;
- records the adopted advisory finding that evidence input readiness and physical text/OCR availability are the current primary bottleneck;
- records the Project Owner decision authorizing Route A Handoff preparation, not implementation;
- preserves advisory notes as design considerations rather than unreviewed runtime requirements.

External advisory content has no independent execution authority. Only the bound Architecture assessment and Project Owner decision give it governance effect.

## 3. Route A Design Principles

1. **Governance-conformant physical design**: components and interfaces must map explicitly to LRG-00/LRG-01/LRG-02/LRG-04/LRG-05.
2. **Identity before extraction**: no processing result may be trusted before matter scope, source, version, access, and hash checks.
3. **Independent status dimensions**: access, integrity, text availability, OCR, extraction, human review, and readiness must not collapse into a single ambiguous state.
4. **OCR is transcription infrastructure**: OCR produces candidate extracted evidence, never a Legal Fact.
5. **Source verification is not evidence adjudication**: human comparison confirms fidelity only and does not decide authenticity, admissibility, credibility, weight, or sufficiency.
6. **Document readiness and matter readiness differ**: one ready file does not make a case bundle ready.
7. **Required gaps block affected analysis**: the infrastructure must not “complete” missing inputs with model inference.
8. **Matter isolation and access control**: cross-matter use requires separate authorization.
9. **Versioned and reversible**: replacements, corrected OCR/extraction, hash drift, access changes, and revoked review invalidate dependent readiness.
10. **Provider-neutral design**: the Spec may define responsibilities and interfaces but may not select a database, OCR engine, model, vendor, MCP server, queue, or cloud architecture.

## 4. Authorized Design Scope

If and only if this Handoff receives Architecture Review and Project Owner approval, Codex may produce documentation-only architecture design covering A-01 through A-06.

### A-01 — Evidence Object Design

Define a unified conceptual Evidence Object. At minimum it must include:

```yaml
EvidenceObject:
  evidence_id:
  matter_id:
  document_id:
  document_version:
  source_type:
  source_description:
  original_filename:
  storage_reference:
  byte_size:
  sha256:
  file_format:
  access_scope:
  access_status:
  hash_status:
  text_layer_status:
  ocr_status:
  extraction_status:
  source_review_status:
  lawyer_review_status:
  readiness_status:
  blocking_reasons:
  limitations:
  supersedes:
  superseded_by:
  correction_history:
```

The final Spec must state:

```text
Hash Verified
≠
Evidence Authentic
≠
Evidence Admissible
≠
Fact Proved
```

The YAML is illustrative documentation only. It is not an authorized runtime schema.

### A-02 — Document Lifecycle Design

Define a conceptual lifecycle and its physical component responsibilities:

```text
RECEIVED
        ↓
REGISTERED
        ↓
HASH_VERIFIED
        ↓
PROCESSING_ROUTE_SELECTED
        ├─ TEXT_EXTRACTION
        └─ OCR / MANUAL TRANSCRIPTION
        ↓
EXTRACTED_UNVERIFIED
        ↓
SOURCE_HUMAN_REVIEWED
        ↓
LAWYER_APPROVED_FOR_ANALYSIS
        ↓
ANALYSIS_READY
```

At any point, the document may enter `BLOCKED`, `QUARANTINED`, `REJECTED`, or `SUPERSEDED` with an explicit reason.

The design must identify:

- transition preconditions and prohibited jumps;
- component of record for each state;
- audit event and responsible role;
- correction and reprocessing behavior;
- downstream invalidation after changed bytes, extraction corrections, new conflicts, revoked access, or supersession;
- native-text, OCR, spreadsheet, image, message-export, audio, and unsupported-format branches at a conceptual level.

### A-03 — OCR Boundary Design

Place OCR strictly between original evidence and candidate extraction:

```text
Evidence Object / Original File
        ↓
OCR Processing Boundary
        ↓
Candidate Extracted Evidence
        ↓
Human Source Verification
        ↓
Source-Verified Fact Candidate
        ↓
Qualified Lawyer Review
        ↓
Legal Fact Candidate
```

The design must:

- distinguish page/region coverage from document-level OCR completion;
- record model/tool version, processing time, language, page/region locators, and limitations without selecting a provider;
- represent unrecognized, low-quality, handwritten, stamped, tabular, multi-column, and partial-text regions;
- prevent OCR confidence from being used as truth, authenticity, proof strength, legal support, or outcome probability;
- require human correction lineage and revalidation of dependent outputs;
- prohibit `OCR_COMPLETED → Legal Fact` and `OCR confidence → SUPPORTED` shortcuts.

### A-04 — Text Layer Governance

Define text-readiness semantics compatible with C02-IV:

| Presentation label | Required canonical meaning |
|---|---|
| `NO_TEXT_LAYER` | `text_layer_status = UNAVAILABLE`; OCR/manual route required for substantive regions |
| `TEXT_AVAILABLE` | `AVAILABLE_COMPLETE` or explicitly scoped `AVAILABLE_PARTIAL`; extraction review still required |
| `OCR_REQUIRED` | OCR/manual processing required; not analysis-ready |
| `OCR_COMPLETED` | Candidate output exists but remains unverified |
| `OCR_VERIFIED` | OCR output was human-compared for stated pages/regions; does not establish truth |

The Spec must not create conflicting duplicate state semantics. It must preserve the canonical independent status dimensions from C02-IV and explain any presentation aliases.

### A-05 — Matter Input Gate

Define a case/matter-level admission architecture:

```text
Authorized Matter and Purpose
        ↓
Required Evidence Profile / Registry
        ↓
Document-Level Readiness Checks
        ↓
Case-Bundle Completeness and Scope Review
        ↓
Qualified Human Authorization
        ↓
Analysis-Ready Manifest
```

Infrastructure readiness descriptors may be:

| Descriptor | Meaning | Legal-reasoning effect |
|---|---|---|
| `READY` | All required evidence and reviews for the declared limited scope pass | Downstream reasoning may start within that scope |
| `PARTIAL` | Some evidence is ready, but one or more declared scopes or optional/required categories remain incomplete | Does not itself authorize reasoning; each affected required gap remains `BLOCKED` |
| `BLOCKED` | A critical required input, identity, access, processing, review, or human decision is missing | Downstream legal reasoning prohibited for the affected scope |

`READY / PARTIAL / BLOCKED` are infrastructure-readiness descriptors. They do not replace LRG-04's legal-reasoning states `SUPPORTED / UNKNOWN / BLOCKED`, and `PARTIAL` may never be converted into partial merits support, a confidence score, or permission to bypass a critical gap.

### A-06 — Physical Architecture and Trust Boundaries

Define provider-neutral logical/physical responsibilities and trust boundaries for later review. The design may name conceptual components such as:

- Intake Boundary;
- Evidence Registry of Record;
- Immutable/Versioned Evidence Store abstraction;
- Integrity Verification service boundary;
- Text/OCR Processing Workspace;
- Extraction Candidate Store;
- Human Source-Review Workbench/Queue abstraction;
- Qualified-Lawyer Approval Gate;
- Analysis-Ready Manifest/View;
- Audit and Invalidation Ledger;
- Matter/Access Policy Boundary.

For every conceptual component, the Spec must define:

- responsibility and non-responsibility;
- trusted and untrusted inputs;
- produced records and lineage;
- access/matter boundary;
- failure and blocked behavior;
- human role;
- audit events;
- downstream invalidation behavior.

The design may provide diagrams, tables, conceptual contracts, failure modes, nonfunctional requirements, and validation protocols. It may not create executable schemas, migrations, APIs, code, test scripts, infrastructure-as-code, database DDL, MCP definitions, or workflow implementation.

## 5. Required Design Topics

The Design Spec must include:

1. architecture overview and non-goals;
2. mapping to LRG-00, LRG-01, LRG-02, LRG-04, and LRG-05;
3. Evidence Object and version/provenance model;
4. physical component responsibility model and trust boundaries;
5. native-text/OCR/manual/spreadsheet/image processing routes;
6. document lifecycle and invalidation/reprocessing rules;
7. page/region-level text/OCR coverage and human correction lineage;
8. document-level and matter-level readiness gates;
9. access control, matter isolation, confidentiality, retention, and audit requirements at design level;
10. source-verification versus legal-review separation;
11. failure modes and stop conditions;
12. real-case validation profile showing how previously missing/partial materials remain blocked without analyzing merits;
13. implementation prerequisites, risk register, and later-stage validation plan;
14. explicit confirmation that no implementation or provider selection occurred.

## 6. Authorized Outputs

After separate Project Owner execution approval, Codex may create exactly two documentation files.

### Output A — Evidence Infrastructure Design Spec

```text
docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md
```

### Output B — Evidence Infrastructure Design Result

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md
```

No other file is authorized. Materialization of this Handoff does not authorize either output.

## 7. Strict Forbidden Scope

This task does not authorize:

```text
Code modification
Skill modification
Agent modification
Workflow modification
MCP integration or configuration
CLAUDE.md modification
Runtime schema modification
OCR pipeline implementation
Document AI implementation
Evidence database construction
Object-storage implementation
RAG implementation
API implementation
Automation implementation
Production deployment
```

It also prohibits:

- real-case merits analysis, new fact extraction, or request-right selection;
- evidence authenticity, admissibility, credibility, weight, or sufficiency conclusions;
- automated legal opinion, strategy, outcome prediction, or success probability;
- modification of the canonical Governance Pattern or C02-IV artifacts;
- activation or design execution of Route B;
- git add, commit, tag, push, release, or publication.

## 8. Acceptance Criteria

### ROUTE-A-001 — Complete Evidence Object

The design defines identity, matter binding, source, version, hash, format, access, processing, review, readiness, limitations, correction, and supersession dimensions without treating a hash as evidence validity.

### ROUTE-A-002 — OCR / Legal Fact Isolation

The design prevents OCR or unverified extraction from becoming a Source-Verified Fact or Legal Fact without required human gates and traceable correction lineage.

### ROUTE-A-003 — C02-IV Input Gate Conformance

The design preserves independent status dimensions, document-level readiness, case-bundle readiness, required-gap blocking, and qualified-human authorization.

### ROUTE-A-004 — LRG-01 / LRG-02 Conformance

The design maps all infrastructure components and data transitions to canonical Evidence and Fact Governance without weakening LRG-00, LRG-04, or LRG-05.

### ROUTE-A-005 — No Implementation Pollution

The task creates documentation only and introduces no code, Skill, Agent, Workflow, MCP, schema, OCR, database, RAG, automation, or deployment asset.

### ROUTE-A-006 — Real-Case Revalidation Readiness

The design provides a reusable validation profile that can later register, process, review, gate, and audit real case materials while preserving missing/partial inputs as explicit blockers. It does not claim that current cases are analysis-ready.

## 9. Required Result Record

If execution is later authorized, the Result must record:

- exact Handoff and all input hashes;
- Spec hash;
- ROUTE-A-001 through ROUTE-A-006 status and evidence;
- files created/modified;
- confirmation of zero `litigation-legal`, Skill, Agent, Workflow, MCP, and code drift;
- `git diff --check` result;
- staging state;
- working-tree preservation;
- implementation status and next governance recipient.

## 10. Repository and Git Boundary

Execution must preserve all existing user changes and the dirty worktree. It may not clean, reset, reformat, rename, or stage unrelated files.

Required final checks:

```text
git diff --check: PASS
Staging Area: EMPTY
New or modified files under litigation-legal/: 0
git add / commit / tag / push / release: NOT PERFORMED
```

## 11. Governance Chain

```text
Route A Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator Review
        ↓
Project Owner Design-Execution Decision
        ↓
Only if approved:
Codex Evidence Infrastructure Design Execution
        ↓
Design Spec + Result + SHA-256
        ↓
Architecture Design Review
        ↓
Project Owner Design Closeout Decision
        ↓
Only under a new Handoff:
Decision whether to authorize any OCR / Evidence Infrastructure implementation
```

## 12. Current Governance State

```text
Canonical Governance Pattern:
v1.0 ADOPTED

C02-IV Input Readiness Design:
CLOSED / DONE

External Advisory Review:
CLOSED / ACCEPTED

Route A:
UNFROZEN FOR DESIGN HANDOFF

Route A Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Route A Design Execution:
NOT AUTHORIZED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient after Handoff materialization is the **Architecture Coordinator (ChatGPT)** for file-level review of the exact physical Handoff SHA-256.
