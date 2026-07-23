# TASK_PHASE2_C02_IV_INPUT_READINESS_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v0.1 |
| Status | **DRAFT — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_C02_IV_INPUT_READINESS_HANDOFF |
| Track | Phase 2 Track C |
| Module | `litigation-legal` |
| Type | Input Readiness Design Only |
| Execution | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |

## 1. Previous Baseline Binding

### C02-III Validation Enhancement Spec

- Path: `docs/phase2/track-c/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_SPEC.md`
- SHA-256: `96C1532A2B448C4B3DB0A2926172CC7374B02E42DDF61B714295E534B4A74DFD`

### C02-III Validation Enhancement Result

- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_RESULT.md`
- SHA-256: `AF534A372D4B4824F4F402485691372D8081B4D430302DC9E3B2B0D89A9ED226`

### C02-III Closeout Status

```text
ACCEPTED / CLOSED
```

## 2. C02-IV Objective

C02-IV addresses the input-readiness issue exposed in C02-I and C02-III:

> The request-right model exists, but the evidence inputs have not reached a stable, verifiable state.

This task designs an **Evidence Input Readiness Framework** so that case materials can enter the following controlled path:

```text
Evidence
        ↓
Fact Extraction
        ↓
Legal Fact
        ↓
Request Right Validation
```

The task does not authorize OCR implementation, evidence-system development, or legal analysis of case merits.

## 3. Design Scope

### 3.1 Evidence Material Registry

Design a case-material registration model containing at minimum:

```text
Evidence ID
Case ID
Document ID
Original Filename
Storage Path
SHA-256
Document Type
Source
Access Status
Text Layer Status
OCR Status
Extraction Status
Human Review Status
```

Lifecycle model:

```text
RECEIVED
        ↓
REGISTERED
        ↓
TEXT_AVAILABLE / OCR_REQUIRED
        ↓
OCR_COMPLETED
        ↓
HUMAN_VERIFIED
        ↓
ANALYSIS_READY
```

This lifecycle is a documentation-level design model. It is not a runtime state machine or workflow implementation.

### 3.2 Document Processing Readiness

The design objective is legal-analysis admission control, not OCR technology implementation.

#### Text Layer

```text
AVAILABLE
```

Means that the PDF or other supported document has a usable machine-readable text layer, subject to extraction and human verification.

#### OCR Required

```text
REQUIRED
```

Means that image recognition is necessary before the material can proceed to extraction verification.

#### OCR Verification Boundary

The design must prohibit this path:

```text
OCR Output
        ↓
Legal Fact
```

The required path is:

```text
OCR Output
        ↓
Human Review
        ↓
Verified Evidence Fact
```

### 3.3 Evidence Confidence Model

Design a four-layer structure:

```text
Raw Evidence
        ↓
Extracted Evidence
        ↓
Verified Fact
        ↓
Legal Fact Candidate
```

The purpose is to prevent:

```text
OCR Error
        ↓
Fact Error
        ↓
Request-Right Error
```

The design must preserve source attribution, document location, extraction method, uncertainty, correction history, and human-review identity between layers.

### 3.4 Input Gate

Design an analysis-admission rule.

#### Ready

```text
Material Ready
- Hash Verified
- Extraction Verified
- Required Human Review Completed
```

Only an input satisfying the approved readiness conditions may proceed to request-right validation.

#### Blocked

If any required condition is absent:

```text
File Missing
OR
Hash Missing / Mismatch
OR
Text or OCR Output Unverified
OR
Extraction Unverified
OR
Required Human Review Missing
```

the status is:

```text
BLOCKED
```

and the material must not enter legal reasoning.

## 4. Output Contract

After Architecture Review and a separate Project Owner execution decision, the task may be authorized to create only the following two outputs.

### Output 1 — Input Readiness Design Spec

- Path: `docs/phase2/track-c/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_SPEC.md`
- Intended contents:
  - input model;
  - lifecycle and state definitions;
  - Evidence Material Registry;
  - text/OCR readiness controls;
  - Evidence Input Gate;
  - Human Review Gate.

### Output 2 — Input Readiness Design Result

- Path: `.codex-coordination/outbox/TASK_PHASE2_C02_IV_INPUT_READINESS_DESIGN_RESULT.md`
- Intended contents:
  - design validation result;
  - current input-readiness problems;
  - acceptance-criteria assessment;
  - later-stage recommendations;
  - repository-boundary verification.

This Draft does not authorize creation of either output.

## 5. Strict Boundary

The following actions are prohibited:

```text
Skill Modification
Agent Modification
Code Modification
MCP Modification
Workflow Modification
CLAUDE.md Modification
Runtime Schema Modification
```

The following implementations are also prohibited:

```text
OCR Pipeline Implementation
Database Implementation
Automation Implementation
Evidence System Implementation
```

This task may not generate a legal opinion, determine evidence authenticity or probative weight, predict a case outcome, calculate a success rate, or replace qualified-lawyer judgment.

## 6. Acceptance Criteria

### AC-C02-IV-001 — Material Lifecycle

The design describes the complete lifecycle of case materials from receipt through analysis readiness.

### AC-C02-IV-002 — Layer Separation

The design distinguishes Raw Evidence, Extracted Evidence, Verified Fact, and Legal Fact Candidate.

### AC-C02-IV-003 — OCR Risk

The design identifies and controls the risk of unverified OCR output.

### AC-C02-IV-004 — Input Blocking

The design prevents incomplete or unverified inputs from entering request-right validation.

### AC-C02-IV-005 — Human Review Gate

The design preserves qualified human review before evidence-derived facts may be used in legal analysis.

### AC-C02-IV-006 — Zero Runtime Modification

No code, Skill, Agent, MCP, Workflow, runtime schema, OCR pipeline, database, or automation asset is created or modified.

## 7. Current Governance State

```text
Phase 2 Track C

C01:
CLOSED / DONE

C02-I:
CLOSED / DONE

C02-II:
CLOSED / DONE

C02-III:
CLOSED / DONE

C02-IV:
Handoff: DRAFT v0.1
Architecture Review: PENDING
Project Owner Decision: NOT STARTED
Execution: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
```

## 8. Next Governance Step

```text
Codex Executor
        ↓
Materialized Handoff + SHA-256
        ↓
Architecture Coordinator Review
        ↓
Project Owner Decision
        ↓
Only if separately approved:
C02-IV Design Execution
```

Materialization of this Handoff does not itself authorize Design Spec/Result creation or any implementation activity.
