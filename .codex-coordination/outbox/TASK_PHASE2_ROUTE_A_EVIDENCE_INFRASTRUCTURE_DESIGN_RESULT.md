# TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT

## 0. Status

```text
Route A Evidence Infrastructure Design:
DONE — DESIGN ONLY

Acceptance Criteria:
6 / 6 PASS

Architecture Review:
PENDING

Implementation:
NOT AUTHORIZED
```

| Field | Value |
|---|---|
| Route | Phase 2 / Route A |
| Executed task | TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN |
| Execution date | 2026-07-22 |
| Mode | Documentation-only physical architecture design |
| Approved Handoff SHA-256 | `9E40FC833135C8C7B5CE9B97A689D4335F10827A242A97424D20880B249831A3` |
| Design Spec SHA-256 | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` |
| Route A implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

## 1. Fixed Input Verification

Every Handoff-bound input was recomputed before execution.

| Input | Required SHA-256 | Actual SHA-256 | Result |
|---|---|---|---|
| Route A Design Handoff | `9E40FC833135C8C7B5CE9B97A689D4335F10827A242A97424D20880B249831A3` | `9E40FC833135C8C7B5CE9B97A689D4335F10827A242A97424D20880B249831A3` | PASS |
| Canonical Governance Pattern | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | PASS |
| Pattern Adoption Decision | `A275B101843D4DDEC82715AC4857C2DEBB576292FDF29481D38FE069F88E1CD2` | `A275B101843D4DDEC82715AC4857C2DEBB576292FDF29481D38FE069F88E1CD2` | PASS |
| C02-IV Input Readiness Spec | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` | PASS |
| C02-IV Input Readiness Result | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` | PASS |
| C02-IV Architecture Review | `46A1F6CAD52A2F73421804AED701D1AEC8214B37C55040148E1611C3A3DE5402` | `46A1F6CAD52A2F73421804AED701D1AEC8214B37C55040148E1611C3A3DE5402` | PASS |
| C02-IV Project Owner Decision | `4ACEAECA570721CF6A1B2B0882D0D2068B51CFF7B88BB876CA0F8554F2EF4478` | `4ACEAECA570721CF6A1B2B0882D0D2068B51CFF7B88BB876CA0F8554F2EF4478` | PASS |
| External Advisory Report | `F091FB8A53415F6DE152942A5144BE797F28BB2833C4EBE3A433CBFD4E592F77` | `F091FB8A53415F6DE152942A5144BE797F28BB2833C4EBE3A433CBFD4E592F77` | PASS |
| Architecture Advisory Assessment | `26B2B0BBF82FEBF2E1CDFDD90159E5F3B4399CCB645E2ABCB1FD33A1685D2719` | `26B2B0BBF82FEBF2E1CDFDD90159E5F3B4399CCB645E2ABCB1FD33A1685D2719` | PASS |
| External Advisory Closeout Decision | `2F575AA6EA40DA192B7847DCB94864F4CA2F7D0F970CDCC6E145FA4A5305713D` | `2F575AA6EA40DA192B7847DCB94864F4CA2F7D0F970CDCC6E145FA4A5305713D` | PASS |

The two authorized Route A outputs were absent before execution, and Git staging was empty.

## 2. Design Completion Summary

### 2.1 Evidence Object

The Spec defines a unified conceptual Evidence Object covering:

- evidence, matter, document, and version identity;
- evidence category, source type, source description, acquisition context, and original filename;
- approved storage reference, byte size, SHA-256, and file type;
- matter/purpose access scope and confidentiality restrictions;
- independent access, hash, text-layer, OCR, extraction, document-review, legal-review, and readiness states;
- page/sheet/cell/message/time/region locators;
- linked Source-Verified Fact Candidates;
- limitations, blocking reasons, corrections, supersession, and audit lineage.

The design explicitly preserves:

```text
Hash Verified
≠ Evidence Authentic
≠ Evidence Admissible
≠ Fact Proved
≠ Legal Fact Established
```

### 2.2 Physical Responsibility Model

Thirteen provider-neutral conceptual responsibilities were defined:

1. Matter & Access Boundary;
2. Evidence Intake Gateway;
3. Registry of Record;
4. Versioned Evidence Store abstraction;
5. Integrity Verification Boundary;
6. Text Readiness Assessor / Processing Router;
7. Extraction Candidate Workspace;
8. Document Review Gate;
9. Source-Verified Candidate Register;
10. Legal Fact Review Gate;
11. Analysis-Ready Manifest;
12. Audit / Correction / Supersession / Invalidation Ledger;
13. Matter Isolation / Confidentiality / Retention Policy Boundary.

Six trust zones prevent untrusted intake, registered originals, identity-verified bytes, processing candidates, source-verified candidates, and lawyer-approved inputs from collapsing into one state.

### 2.3 Lifecycle and Processing Routes

The Spec defines the complete traceable lifecycle:

```text
RECEIVED
→ REGISTERED
→ HASH_VERIFIED
→ TEXT_ASSESSED
→ PROCESSING_ROUTE_SELECTED
→ EXTRACTED_UNVERIFIED
→ DOCUMENT_HUMAN_REVIEWED
→ SOURCE_VERIFIED
→ LEGAL_FACT_REVIEWED
→ ANALYSIS_READY
```

Native-text, OCR, hybrid, spreadsheet/table, message/image, and manual/unsupported routes are described as responsibilities and review boundaries only. No provider, engine, API, schema, or implementation was selected.

### 2.4 OCR / Legal Fact Isolation

The required boundary is:

```text
OCR Candidate
→ Extracted Evidence Candidate
→ Document Human Review
→ Source-Verified Fact Candidate
→ Legal Fact Review
→ Legal Fact Candidate
```

OCR completion and OCR confidence cannot directly produce a fact, LRG-04 support state, request right, or legal conclusion.

### 2.5 Verification Model

Three independent questions and owners are defined:

| Gate | Question | Decision boundary |
|---|---|---|
| File Identity | Are these the registered bytes/version? | Hash/metadata verification only |
| Evidence Source/Content Review | Does extraction match this source, with what provenance and limits? | Source-fidelity review only |
| Legal Fact Review | May the source-verified candidate enter legal analysis for this matter/scope? | Qualified-lawyer use decision |

No gate implies the result of a later gate.

### 2.6 Matter Input Gate

The Spec defines:

- a versioned Required Evidence Profile;
- per-document identity, processing, and review gates;
- required-category, adverse-source, and conflict checks;
- qualified-human matter authorization;
- a scope-bound Analysis-Ready Manifest or Blocked Report.

Infrastructure descriptors `READY`, `PARTIAL`, and `BLOCKED` remain separate from LRG-04 legal-reasoning states. `PARTIAL` never waives a critical required gap or authorizes partial merits reasoning.

### 2.7 Audit and Invalidation

Receipt, registration, hashing, routing, extraction, correction, review, readiness, downstream use, revocation, supersession, and invalidation events are included in the design. File changes, extraction corrections, access changes, new conflicts, or review revocation reopen dependent artifacts rather than silently preserving readiness.

## 3. External Advisory Absorption

The External Advisory finding that evidence/text readiness is the current physical bottleneck was used as a routing rationale, not as execution authority or an implementation specification.

Advisory controls absorbed at design level:

- no OCR output may bypass source and lawyer review;
- legal evaluation remains bound to the canonical reasoning layer and current authority;
- controlled states remain free of probabilities and merits scores;
- domain-specific burden-shift, rebuttal, evidence-exchange, or investigation-order concepts remain later Adapter concerns rather than Evidence Infrastructure truth states;
- Route B remains frozen.

## 4. Real-Case Revalidation Capability

The Design can later carry real-case revalidation by accepting:

- per-file identity and hashes;
- page/region/sheet/message coverage;
- extraction versions and corrections;
- Document Review and Legal Fact Review decisions;
- required evidence profiles;
- missing, adverse, conflicting, and superseded materials;
- scope-bound Analysis-Ready Manifests and invalidation hooks.

The accepted C02-III availability snapshot was used only to test gate behavior:

```text
CASE-A: PARTIAL infrastructure readiness; affected legal reasoning remains BLOCKED
CASE-B: BLOCKED
CASE-C: BLOCKED
```

No new case content was read, no fact was extracted, and no merits conclusion was generated.

## 5. Acceptance Criteria

| ID | Status | Verification |
|---|---|---|
| `ROUTE-A-001` — Evidence Object complete | **PASS** | Complete identity, matter, source, version, hash, format, access, processing, review, readiness, limitation, correction, and supersession model |
| `ROUTE-A-002` — Lifecycle traceable / OCR isolated from Legal Fact | **PASS** | Prohibited jumps, trust zones, two review gates, and OCR-to-candidate-only path are defined |
| `ROUTE-A-003` — C02-IV Input Gate conformance | **PASS** | Independent status dimensions, document and bundle gates, required-gap blocking, and qualified authorization are preserved |
| `ROUTE-A-004` — LRG-01 / LRG-02 conformance | **PASS** | Components and data transitions map to canonical Evidence and Fact Governance without weakening LRG-00/04/05 |
| `ROUTE-A-005` — No implementation pollution | **PASS** | Documentation only; no provider, code, Skill, Agent, Workflow, MCP, schema, database, OCR, RAG, automation, or deployment asset |
| `ROUTE-A-006` — Real-case revalidation readiness | **PASS** | Reusable validation profile and safe blocked behavior are defined without claiming current case readiness |

## 6. Current Problems and Remaining Preconditions

The Design resolves the architecture specification gap. It does not resolve the physical input gap.

Still unresolved:

- inaccessible or missing case materials;
- provider/runtime selection;
- text/OCR execution and measurable quality;
- storage, database, API, workflow, queue, and access-control implementation;
- reviewer workbench and operational staffing;
- China-language validation corpus and performance baselines;
- production security, privacy, retention, deletion, incident, rollback, and recovery controls;
- runtime invalidation of downstream analyses;
- Route B design or execution.

A later implementation Handoff must bind the adopted Design Spec and explicitly whitelist components/files, providers, runtime schemas, validation criteria, security controls, rollback, and production boundaries.

## 7. Repository Boundary Verification

```text
Authorized output files created: 2
Files created or modified under litigation-legal/: 0 by this execution
Skill modification: NO
Agent modification: NO
Code modification: NO
Workflow / MCP / CLAUDE.md modification: NO
Runtime schema modification: NO
OCR / database / RAG / automation implementation: NO
Git staging: EMPTY
git diff --check: PASS
Working tree: NON-CLEAN — pre-existing changes and governance artifacts preserved
git add / commit / tag / push / release: NOT PERFORMED
```

The normalized SHA-256 digest of the sorted `git status --short -- litigation-legal` snapshot contained the same nine pre-existing modified files before and after execution:

`808E2452B161A01B1BF3CA021C07668B5CE82B6AA60A5BD641DA0372D6CE549F`

## 8. Authorized Output List

1. `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md`
   - SHA-256: `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892`
2. `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_RESULT.md`
   - SHA-256: returned externally after final materialization; this Result does not self-bind its own hash.

No other file was created or modified by this execution.

## 9. Governance Transition

```text
Codex Executor
        ↓
Route A Design Spec + Result produced
        ↓
Architecture Coordinator Review
        ↓
Project Owner Design Closeout Decision
        ↓
Only under a new Handoff:
Decision whether to authorize any OCR / Evidence Infrastructure implementation
```

Route A Implementation and Route B remain **NOT AUTHORIZED**.
