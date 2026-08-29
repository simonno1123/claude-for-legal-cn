# TASK_PHASE2_ROUTE_A_OCR_CAPABILITY_REUSE_ASSESSMENT

## 1. Record Status

| Field | Value |
|---|---|
| Project | `claude-for-legal-cn` |
| Route | `Phase 2 / Route A` |
| Artifact type | Existing-capability inventory and reuse-first fit-gap assessment |
| Assessment mode | `READ-ONLY / DESIGN AND INVENTORY ONLY` |
| Material access | `NOT AUTHORIZED / NOT PERFORMED` |
| OCR execution | `NOT AUTHORIZED / NOT PERFORMED` |
| Provider selection | `NOT AUTHORIZED / NOT PERFORMED` |
| Implementation | `NOT AUTHORIZED / NOT PERFORMED` |

This artifact records the capabilities visible in the current repository and local Codex workspace runtime. It does not make those runtime dependencies part of the project, authorize their production use, or establish that an unobserved desktop application or enterprise service is unavailable.

## 2. Bound Route A Baselines

| Baseline | SHA-256 | Verification |
|---|---|---|
| `TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` | Exact local byte match |
| `TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_SPEC.md` | `8DBDD4F438BC05DCCA3BAFB6CE4572A4E0FDEDAC1A8303002292CEB6FEC367AB` | Exact local byte match |
| `TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_SPEC.md` | `257ED2A1E16879F9EB50723D91652F7D7C5688C88D586DE6288D8E1888F8512B` | Exact local byte match |

The assessment preserves the existing Route A rule that native text, OCR output, extracted evidence candidates, source-verified fact candidates, and Legal Fact candidates are distinct states.

## 3. Objective and Boundaries

### 3.1 Objective

Determine whether existing repository or local workspace capabilities can satisfy all or part of the Route A text/OCR preparation requirements before any new engine, provider, connector, or implementation is considered.

### 3.2 Non-Goals

This assessment does not:

- inspect, search for, open, copy, hash, transform, OCR, or interpret case materials;
- install, download, configure, benchmark, invoke, or select an OCR engine or external provider;
- create a production dependency, API, MCP server, Connector, Agent, Skill, workflow, database, queue, RAG system, or runtime schema;
- determine evidence authenticity, admissibility, credibility, weight, sufficiency, legal facts, claims, defenses, strategy, or outcome;
- activate `CASE-A-AM-001` or satisfy its pending human matter, source, or access confirmations;
- infer permission to process material from the presence of a tool.

## 4. Read-Only Inventory Method

The assessment used only:

1. repository-wide text search for existing OCR engines, OCR libraries, integrations, and declared capability boundaries;
2. exact command discovery for common local OCR and document-processing executables;
3. package-presence and version checks in the bundled Codex workspace Python runtime;
4. exact baseline SHA-256 verification for the three bound Route A specifications.

No test document, screenshot, PDF, image, spreadsheet, message export, real matter, or synthetic OCR corpus was processed.

## 5. Existing Capability Inventory

| Capability | Observed technology | Observed version/state | Reuse assessment | Qualification |
|---|---|---|---|---|
| Native PDF text parsing | `pypdf` | `6.10.0` | Candidate for later controlled reuse | Bundled workspace dependency; not a repository-declared production dependency |
| PDF text/table and layout inspection | `pdfplumber` | `0.11.9` | Candidate for later controlled reuse | Useful for native text and layout-aware inspection; not OCR |
| PDF metadata and structural inspection | Poppler `pdfinfo` | `26.05.0` | Candidate for later controlled reuse | Inspection only; does not recognize image text |
| PDF page rasterization | Poppler `pdftoppm` | `26.05.0` | Candidate for later controlled reuse | Can prepare page images for a later authorized OCR step; not OCR |
| Image loading and preprocessing | Pillow | `12.3.0` | Candidate for later controlled reuse | Preprocessing capability only; no text recognition |
| Tesseract OCR engine | `tesseract` | Not discoverable in the assessed command environment | Capability gap | Absence is limited to the assessed environment and method |
| OCRmyPDF | `ocrmypdf` | Not discoverable | Capability gap | No searchable-PDF OCR pipeline established |
| PaddleOCR | `paddleocr` | Not discoverable | Capability gap | No Chinese-oriented OCR engine established |
| EasyOCR | `easyocr` | Not discoverable | Capability gap | No OCR engine established |
| Repository OCR integration | Repository code/configuration | Not found | Capability gap | Repository currently documents OCR boundaries but contains no production OCR integration |
| Cloud or commercial OCR provider | Provider/API/Connector configuration | Not established | Intentionally unselected | External transfer and provider use require separate authorization |
| Desktop or enterprise OCR application outside the assessed command/repository view | User or organization environment | Not independently established | `UNKNOWN — HUMAN CONFIRMATION REQUIRED` | Must not be treated as absent or authorized without attributable confirmation |

## 6. Fit-Gap Assessment

| Route A requirement | Existing capability | State | Gap or limitation |
|---|---|---|---|
| Detect native text and inspect PDF structure | `pypdf`, `pdfplumber`, `pdfinfo` | `PARTIALLY AVAILABLE` | Requires a separately authorized, versioned processing wrapper and validation procedure before operational use |
| Render image-only or incomplete pages | `pdftoppm`, Pillow | `PARTIALLY AVAILABLE` | Produces images only; no recognition or human-review record |
| Recognize simplified/traditional Chinese printed text | None established | `GAP` | OCR engine and controlled benchmark not established |
| Preserve page and region locators | Libraries can expose page/image structure | `DESIGN-POSSIBLE / NOT IMPLEMENTED` | No governed locator-output contract has been implemented |
| Preserve tables, columns, signs, units, and merged cells | `pdfplumber` may assist native PDFs | `PARTIAL` | Image-table OCR and structural verification are not established |
| Handle stamps, signatures, handwriting, faint scans, and multi-column layouts | None established | `GAP` | Must preserve images and uncertainty; automated authenticity conclusions remain prohibited |
| Produce confidence and uncertain-span metadata | None established | `GAP` | Confidence cannot substitute for human source comparison |
| Preserve processing version and correction lineage | Route A design defines the requirement | `DESIGN COMPLETE / RUNTIME ABSENT` | No processing ledger or correction workflow exists |
| Enforce matter isolation and permitted purpose | Route A design defines the requirement | `DESIGN COMPLETE / RUNTIME ABSENT` | Tool presence alone does not enforce access or isolation |
| Human document comparison | Governance gate defined | `PROCESS DEFINED / EXECUTION UNAUTHORIZED` | No reviewer, source, scope, or material authorization is bound |
| Qualified-lawyer Legal Fact review | Governance gate defined | `PROCESS DEFINED / EXECUTION UNAUTHORIZED` | OCR output cannot bypass this gate |
| Local/offline processing for protected material | No OCR engine established | `NOT READY` | External transfer is prohibited unless separately classified and authorized |

## 7. Reuse-First Decision Order

Every later material-processing decision must follow this order:

1. **Identity and authority first** — confirm the matter, source, exact object, permitted purpose, access scope, and accountable human decision.
2. **Native text first** — use verified embedded text when it covers the substantive page/region scope; do not run OCR merely because OCR is available.
3. **Existing parser and renderer reuse** — prefer the already available native-text, structure-inspection, and rasterization capabilities where they satisfy the exact authorized task.
4. **Existing approved local OCR confirmation** — ask the Project Owner or authorized environment owner whether an approved local/enterprise OCR capability already exists; bind its identity, version, data path, and authorization before use.
5. **Manual route where proportionate** — use approved manual transcription/review for limited or unsupported regions when it is safer and more proportionate than introducing a new technical dependency.
6. **Gap-only technology evaluation** — evaluate an additional local OCR engine only for requirements not met by existing capabilities, using a non-case or expressly authorized test corpus.
7. **External provider last** — consider cloud or external-provider OCR only after local options fail and a separate data-classification, transfer, confidentiality, retention, and provider authorization is approved.
8. **Implementation remains separate** — a technology fit decision does not authorize installation, integration, production use, case-material processing, or downstream legal analysis.

## 8. Candidate Evaluation Gates for a Later Authorization

Any later OCR candidate assessment must measure, without preselecting a product:

- Chinese printed-text accuracy, including names, amounts, dates, account numbers, and legal article numbers;
- page/region locator stability and reproducibility;
- multi-column, table, merged-cell, header/footer, footnote, stamp, signature, and handwriting behavior;
- image-only, hybrid, faint, skewed, rotated, corrupted, encrypted, and unsupported inputs;
- preservation of native and OCR outputs as separate, versioned artifacts;
- uncertain-span representation and correction history;
- offline/local processing availability and outbound-data behavior;
- logging, retention, deletion, revocation, and matter-isolation controls;
- human comparison workflow and reviewer attribution;
- licensing, maintenance, portability, and operational support burden.

The benchmark must not use real matter material unless a separate exact-object authorization has established the matter, source, access, privacy, confidentiality, and review boundaries.

## 9. Assessment Determination

```text
Reuse-First Principle:
SATISFIED AT ASSESSMENT LEVEL

Existing Native-Text / Inspection / Rasterization Capability:
PARTIALLY AVAILABLE

Existing OCR Recognition Engine:
NOT ESTABLISHED IN THE ASSESSED ENVIRONMENT

OCR Provider or Product Selection:
NOT PERFORMED

OCR Operational Readiness:
BLOCKED — RECOGNITION ENGINE, BENCHMARK, AUTHORITY, AND MATERIAL BINDING NOT ESTABLISHED

Route A Material Acquisition:
BLOCKED — EXTERNAL HUMAN CONFIRMATIONS REMAIN MISSING

Route A OCR Execution:
NOT AUTHORIZED

Implementation / Runtime:
NOT AUTHORIZED
```

The current design does not violate the agreement to prefer existing technology. It explicitly avoids premature replacement or procurement and identifies reusable native-text and preprocessing capabilities. The principle is not operationally complete until an authorized human confirms any additional existing local/enterprise OCR capability and a separate controlled fit assessment is approved.

## 10. Next Eligible Governance Action

The next eligible action is one of the following, each requiring separate Project Owner authorization:

1. collect an attributable confirmation identifying an already approved local or enterprise OCR capability; or
2. materialize a closed-form OCR candidate shortlist and benchmark design using non-case or separately authorized material.

Neither option authorizes OCR execution, software installation, external transfer, provider invocation, case-material access, Manifest activation, or legal analysis.
