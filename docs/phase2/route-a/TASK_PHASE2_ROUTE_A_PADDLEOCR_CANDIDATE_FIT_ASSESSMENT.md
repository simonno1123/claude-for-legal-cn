# TASK_PHASE2_ROUTE_A_PADDLEOCR_CANDIDATE_FIT_ASSESSMENT

## 1. Record Status

| Field | Value |
|---|---|
| Project | `claude-for-legal-cn` |
| Route | `Phase 2 / Route A` |
| Candidate | PaddlePaddle/PaddleOCR |
| Assessment date | `2026-08-28` |
| Assessment mode | `OFFICIAL-DOCUMENTATION REVIEW / LOCAL-COMPATIBILITY CHECK ONLY` |
| Installation | `NOT AUTHORIZED / NOT PERFORMED` |
| Model download | `NOT AUTHORIZED / NOT PERFORMED` |
| OCR execution | `NOT AUTHORIZED / NOT PERFORMED` |
| Case-material access | `NOT AUTHORIZED / NOT PERFORMED` |
| Provider or cloud invocation | `NOT AUTHORIZED / NOT PERFORMED` |
| Implementation | `NOT AUTHORIZED / NOT PERFORMED` |

This assessment evaluates PaddleOCR as a candidate technology. It does not adopt a version, install a dependency, approve a model, create a project integration, or authorize any material-processing operation.

## 2. Bound Existing-Capability Assessment

| Artifact | SHA-256 | Status |
|---|---|---|
| `TASK_PHASE2_ROUTE_A_OCR_CAPABILITY_REUSE_ASSESSMENT.md` | `3AD62830A0DA3CFC0CB08B97B9735690983BBF2FCDF0AA686ACC694483BD00F1` | Exact local byte match before this assessment |

The reuse-first assessment established that native-text parsing, PDF inspection, page rasterization, and image preprocessing are partially available, while no OCR recognition engine is currently established in the assessed environment.

## 3. Official Candidate Identity

| Property | Recorded value | Qualification |
|---|---|---|
| Upstream project | `PaddlePaddle/PaddleOCR` | Official repository: <https://github.com/PaddlePaddle/PaddleOCR> |
| Candidate family | PaddleOCR 3.x | Family only; exact version remains unbound |
| Current official repository release observed at assessment | `3.7.0` | Observation only; not adopted or installed |
| License | Apache License 2.0 | Upstream project license; downstream notice and dependency review remain required if adopted |
| Primary deployment posture considered | Local/offline inference | Hosted API, MCP, and external transfer are outside this assessment |
| Primary pipeline candidate | PP-OCR general OCR | Candidate for printed-text baseline only |
| Conditional structured-document extension | PP-StructureV3 | Candidate only where table/layout requirements justify it |
| Deferred high-complexity option | PaddleOCR-VL | Not part of the minimum viable path; requires separate resource, output, and governance assessment |

Official references used:

- Installation: <https://www.paddleocr.ai/main/en/version3.x/installation.html>
- Quick Start: <https://www.paddleocr.ai/main/en/quick_start.html>
- General OCR pipeline: <https://www.paddleocr.ai/main/en/version3.x/pipeline_usage/OCR.html>
- Upstream repository and license: <https://github.com/PaddlePaddle/PaddleOCR>

No third-party benchmark, promotional comparison, or non-official installation guide is treated as governing evidence in this assessment.

## 4. Official Capability Assessment

| Route A requirement | Officially described PaddleOCR capability | Preliminary fit | Limitation |
|---|---|---|---|
| Chinese printed-text recognition | PP-OCR family supports Chinese and multilingual recognition | `CANDIDATE FIT` | Accuracy on Chinese legal documents has not been locally benchmarked |
| Text detection and recognition coordinates | Official pipeline output includes detection polygons, recognized text, and recognition scores | `CANDIDATE FIT` | Route A page/region locator format and stable output contract remain unimplemented |
| Document orientation and rectification | Official pipeline exposes orientation, unwarping, and text-line orientation controls | `CANDIDATE FIT` | Each option must be version-pinned and recorded; automated correction cannot erase source-image lineage |
| Table and complex-layout handling | PP-StructureV3 provides structured-document processing capabilities | `CONDITIONAL FIT` | Must be added only when ordinary OCR and existing native parsers are insufficient |
| Seal text | Official documentation lists seal text detection/recognition capabilities | `CONDITIONAL FIT` | Recognition cannot establish seal authenticity, authority, or legal effect |
| Handwriting | Upstream describes handwriting/document scenarios and datasets | `UNVERIFIED CANDIDATE` | No Route A benchmark has established usable accuracy; manual verification remains mandatory |
| Local deployment | Official documentation provides local Python and command-line inference paths | `CANDIDATE FIT` | Package, inference engine, models, and download source must be independently pinned |
| CPU inference | Official documentation provides a CPU installation path | `CANDIDATE FIT` | Throughput, memory, and document-size limits are untested locally |
| GPU inference | Official documentation provides GPU paths subject to driver/runtime compatibility | `CONDITIONAL FIT` | Exact PaddlePaddle/CUDA wheel compatibility is not established in this assessment |
| Offline operation | Local models can support offline inference after dependencies and model files are present | `CONDITIONAL FIT` | Initial package/model acquisition and any fallback network behavior require explicit controls |
| Hosted/API operation | Official hosted API is available | `OUT OF SCOPE / PROHIBITED` | Would transfer material outside the local process and requires separate authorization |
| MCP/Agent integration | Upstream ecosystem includes integration options | `OUT OF SCOPE / PROHIBITED` | Route A does not authorize MCP, Agent, Skill, or automatic workflow integration |

## 5. Local Environment Observations

| Environment property | Observed state | Compatibility assessment |
|---|---|---|
| Operating-system kernel | `Microsoft Windows NT 10.0.26100.0` | `SUPPORTED IN PRINCIPLE` — official documentation describes Windows use; exact wheel/runtime validation remains required |
| Architecture | `X64 / AMD64` | `SUPPORTED IN PRINCIPLE` |
| Logical processor count | `8` | Sufficient for a controlled CPU feasibility benchmark; performance not established |
| Processor identifier | `Intel64 Family 6 Model 158 Stepping 10` | CPU feature and optimized-backend compatibility not independently benchmarked |
| Python | `3.12.13` | Within the official documented Python 3.8+ / 3.9+ package ranges; exact dependency resolution remains untested |
| pip | `26.2.1` | Package manager present; installation is not authorized |
| NVIDIA GPU | `GeForce GTX 1660 Ti` | GPU candidate present; GPU use remains optional and unapproved |
| GPU memory | `6144 MiB` | May support selected OCR workloads, but no model-specific capacity conclusion is made without a benchmark |
| NVIDIA driver | `566.36` | Driver observed; exact PaddlePaddle wheel/CUDA compatibility remains unverified |
| PaddleOCR package | Not installed in bundled workspace Python | Installation required before any local inference test |
| PaddlePaddle inference engine | Not installed in bundled workspace Python | Exact engine/version must be selected and pinned separately |
| Existing PDF preprocessing | Poppler, `pypdf`, `pdfplumber`, Pillow available | Reuse before adding duplicate PDF/image preprocessing dependencies |

The Windows, CPU, GPU, and Python observations are environment facts only. They do not establish production suitability, security approval, case-material authority, or a supported project dependency.

## 6. Minimum Viable Reuse-First Technical Path

The lowest-complexity candidate path is:

```text
Exact Source Identity and Access Authorization
        ↓
Native-Text Coverage Assessment
        ↓
Existing pypdf / pdfplumber Route where sufficient
        ↓
Existing Poppler / Pillow page-region preparation where needed
        ↓
Local PaddleOCR General OCR Candidate
        ↓
Versioned JSON/Text + Detection Coordinates + Confidence Metadata
        ↓
Document Human Review against Stable Page/Region Locators
        ↓
Source-Verified Fact Candidate
        ↓
Separate Qualified-Lawyer Legal Fact Review
```

### 6.1 Initial Candidate Profile

| Decision area | Preliminary recommendation |
|---|---|
| Runtime | Separate, isolated local Python environment; do not mutate the project or bundled Codex runtime |
| Inference mode | CPU baseline first for portability and minimum configuration risk |
| OCR pipeline | PP-OCR general OCR only for the first benchmark |
| Version | Pin one exact PaddleOCR release, PaddlePaddle release, model identity, and dependency lock only after compatibility design approval |
| PDF handling | Reuse existing Poppler and native-text libraries; OCR only image-only or missing substantive regions |
| Output | Preserve raw model output, normalized candidate text, polygons/locators, scores, configuration, and hashes separately |
| Network | Deny external material transfer; acquire approved packages/models separately and then test offline |
| Tables/layout | Add PP-StructureV3 only after a table/layout benchmark demonstrates need and acceptable fidelity |
| Seal/signature | Preserve source image and uncertain region; never infer authenticity or authority |
| Handwriting | Default to `HUMAN_REVIEW_REQUIRED` unless a controlled benchmark establishes limited usability |
| PaddleOCR-VL | Deferred; no VLM in the minimum path |

### 6.2 Why This Path Preserves Existing Technology

- It keeps verified native text as the first processing route.
- It reuses the already available PDF parsers, PDF renderer, and image library.
- It adds only the missing recognition function instead of replacing the entire document-processing path.
- It begins with the smallest general-OCR package and CPU baseline rather than the full optional dependency set.
- It defers structured parsing, VLM, MCP, cloud API, and production service layers until a measured gap justifies them.

## 7. Route A Output Contract Requirements

Any later PaddleOCR result must remain an `Extracted Evidence Candidate` and include at least:

```yaml
PaddleOCRCandidateOutput:
  matter_id: separately authorized stable matter identifier
  evidence_object_id: exact registered evidence identity
  source_version_id: exact byte-version identity
  source_sha256: complete source-byte SHA-256
  page_or_region_locator: stable page and polygon/region reference
  native_or_ocr_route: OCR
  paddleocr_package_version: exact pinned version
  inference_engine: exact pinned engine and version
  model_identity: exact model name, version, source, and file hashes
  configuration_identity: exact configuration hash
  execution_environment_identity: approved isolated environment reference
  recognized_text_raw: unmodified engine output
  recognition_score_raw: unmodified engine score
  uncertainty_flags: explicit uncertain spans and structural limitations
  correction_version: append-only correction identity
  human_review_status: PENDING | PARTIAL | VERIFIED | REJECTED
  legal_fact_status: NOT_REVIEWED | LIMITED_APPROVAL | REJECTED
```

The schema above is a documentation-level output contract, not an executable runtime schema.

## 8. Required Data and Security Controls

1. Default to local/offline inference after approved package and model acquisition.
2. Do not use the official hosted API, access tokens, remote file URLs, MCP, or third-party inference services for case material under this candidate path.
3. Disable or block unapproved runtime model downloads and record every approved package/model source and SHA-256.
4. Use a separate environment rather than installing into the repository's validation environment or the bundled Codex workspace runtime.
5. Bind every processing action to exact matter, source, purpose, access, reviewer, version, and retention constraints.
6. Preserve original bytes and images; never overwrite them with processed output.
7. Keep raw OCR, normalized text, corrections, and reviewer decisions separately versioned.
8. Prevent logs, temporary files, caches, or debug images from escaping the matter boundary.
9. Treat scores only as review-prioritization metadata, never as truth, authenticity, or legal support.
10. Fail closed on missing pages, low-quality scans, lost table structure, conflicting output, unknown model identity, or incomplete human review.

## 9. Fit-Gap and Risk Register

| ID | Gap or risk | Current state | Required closure before operational use |
|---|---|---|---|
| `POCR-G01` | Exact PaddleOCR/PaddlePaddle/model versions unbound | `OPEN` | Compatibility design, immutable version pin, source and hashes |
| `POCR-G02` | Package/model download path unapproved | `OPEN` | Separate acquisition authorization and supply-chain verification |
| `POCR-G03` | Python 3.12 dependency resolution untested | `OPEN` | Isolated non-case installation test |
| `POCR-G04` | CPU performance and memory untested | `OPEN` | Controlled synthetic/public benchmark |
| `POCR-G05` | GPU wheel/runtime compatibility untested | `OPEN` | Optional separate GPU compatibility test; not required for CPU baseline |
| `POCR-G06` | Chinese legal-document accuracy untested | `OPEN` | Public/synthetic legal-layout corpus with character and field-level metrics |
| `POCR-G07` | Table/layout fidelity untested | `OPEN` | Separate structural benchmark before PP-StructureV3 adoption |
| `POCR-G08` | Seal/signature/handwriting limitations unmeasured | `OPEN` | Region-specific benchmark and mandatory human-review rules |
| `POCR-G09` | Route A output adapter absent | `OPEN` | Separately reviewed implementation design; no code yet |
| `POCR-G10` | Audit, correction, retention, and cache controls absent | `OPEN` | Processing-ledger and cleanup design before real material |
| `POCR-G11` | Real matter/source/access confirmations absent | `BLOCKING` | Attributable human confirmation and exact-object authorization |
| `POCR-G12` | Legal Fact review execution absent | `BLOCKING` | Separate qualified-lawyer review authorization after source verification |

## 10. Determination

```text
Candidate Technology:
PaddleOCR

Candidate Family Fit:
CONDITIONALLY SUITABLE FOR ROUTE A LOCAL OCR

Recommended Minimum Path:
LOCAL / OFFLINE / GENERAL OCR / CPU BASELINE / NATIVE-TEXT-FIRST

PP-StructureV3:
DEFERRED — ADD ONLY FOR DEMONSTRATED TABLE OR LAYOUT NEED

PaddleOCR-VL:
DEFERRED — NOT PART OF MINIMUM VIABLE PATH

Hosted API / MCP / External Provider:
PROHIBITED IN THIS CANDIDATE PATH

Local Environment Compatibility:
PLAUSIBLE — NOT VERIFIED BY INSTALLATION OR EXECUTION

Reuse-First Principle:
SATISFIED AT CANDIDATE-DESIGN LEVEL

Candidate Adoption:
NOT DECIDED

Installation / Download / Benchmark / OCR Execution:
NOT AUTHORIZED

Case-Material Processing:
NOT AUTHORIZED

Route A Manifest Activation:
BLOCKED

Implementation / Runtime / Legal Analysis:
NOT AUTHORIZED
```

PaddleOCR is a reasonable primary candidate because it can supply the recognition capability missing from the current local tool set without replacing the existing native-text, PDF inspection, page-rendering, and human-review architecture. That conclusion is conditional: it does not establish version compatibility, benchmark quality, operational security, or authority to process real material.

## 11. Next Eligible Governance Action

The next eligible action is materialization of a closed-form PaddleOCR controlled benchmark design covering:

- an isolated environment and immutable dependency/model manifest;
- CPU-first test parameters and optional GPU compatibility branch;
- only public, synthetic, or separately authorized non-case samples;
- Chinese text, amounts, dates, article numbers, tables, layout, stamps, signatures, handwriting, and low-quality images;
- character, field, page/region, structural, and failure-rate measures;
- raw-output preservation, locator validation, correction lineage, and human-review scoring;
- offline/network-denial and temporary-file/cache checks;
- explicit pass, limited, fail, and stop conditions.

The benchmark design itself would not authorize installation, model download, benchmark execution, case-material access, provider invocation, Manifest activation, or implementation.
