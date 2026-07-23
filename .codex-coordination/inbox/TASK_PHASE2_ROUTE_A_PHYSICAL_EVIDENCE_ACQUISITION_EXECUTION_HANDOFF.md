# TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_HANDOFF

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DRAFT v1.0 — PENDING ARCHITECTURE REVIEW** |
| Task ID | TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION |
| Task Type | Controlled Physical Evidence Intake and Registration Authorization Request |
| Route | Phase 2 / Route A |
| Execution | **NOT AUTHORIZED BY MATERIALIZATION** |
| External Acquisition / Contact | **NOT AUTHORIZED** |
| OCR / Extraction / Legal Analysis | **NOT AUTHORIZED** |
| Implementation | **NOT AUTHORIZED** |
| Route B | **FROZEN / NOT AUTHORIZED** |

Materialization of this Handoff creates the physical execution-authorization request only. It does not authorize the Execution Spec/Result, physical material collection, external communication, file scanning, file copying, OCR, evidence assessment, legal reasoning, or implementation. Execution requires Architecture Review and a Project Owner decision bound to this physical Handoff SHA-256.

## 1. Task Objective

Convert the adopted Physical Evidence Acquisition Design into a fail-closed execution protocol for registering materials that an authorized human has explicitly confirmed and made available within an exact approved matter, source, purpose, path/object, and access scope.

```text
Adopted Acquisition Design
        ↓
Human Target and Authority Confirmation
        ↓
Exact Action Manifest
        ↓
Controlled Receipt / Local Intake Record
        ↓
Evidence Registry and Hash Update
        ↓
Human Verification Records
        ↓
Input Readiness Re-evaluation
        ↓
READY / PARTIAL / BLOCKED
```

The task does not authorize Codex to cause a third party to produce material. “Material Collection Record” means recording a material already delivered or placed by an authorized human; it is not authority to contact, request, download, or collect from an external source.

## 2. Fixed Baseline Binding

Before any later execution, Codex must recompute and exactly match every required SHA-256. A missing or mismatched artifact yields `BLOCKED` and prohibits Execution Spec/Result creation.

### 2.1 Canonical Governance Pattern

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

OCR, hash, file availability, and human transcription cannot become legal support without the separately governed LRG-00 through LRG-05 chain.

### 2.2 Route A Evidence Infrastructure

| Artifact | Path | SHA-256 |
|---|---|---|
| Evidence Infrastructure Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_EVIDENCE_INFRASTRUCTURE_DESIGN_SPEC.md` | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` |

### 2.3 Route A Design Validation

| Artifact | Path | SHA-256 |
|---|---|---|
| Design Validation Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_DESIGN_VALIDATION_RESULT.md` | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` |

### 2.4 Input Readiness Recovery

| Artifact | Path | SHA-256 |
|---|---|---|
| Input Readiness Recovery Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_INPUT_READINESS_RECOVERY_SPEC.md` | `6A9847DE0ABBC6641F904B69B328D6A2DDE6D76B331276521B99935F31AB3CF0` |

### 2.5 Physical Evidence Acquisition Design

| Artifact | Path | SHA-256 |
|---|---|---|
| Acquisition Design Handoff | `.codex-coordination/inbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_HANDOFF.md` | `906D8062C5463DC38116FE6BC3C176C8E310551A605CBADADE34A2B11D28FE77` |
| Acquisition Design Spec | `docs/phase2/route-a/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_SPEC.md` | `257ED2A1E16879F9EB50723D91652F7D7C5688C88D586DE6288D8E1888F8512B` |
| Acquisition Design Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_RESULT.md` | `D21A6563CC43374C52B89BD9D371F05B31A126681C2061A14FDDF1E1E4DBF71E` |

The Execution task may apply these controls but may not modify or reinterpret any frozen baseline.

## 3. Execution Model and Activation Gates

### 3.1 Gate E0 — Artifact and Repository Verification

- recompute every bound input hash;
- confirm only the two authorized outputs are absent or explicitly approved for update;
- record pre-execution `litigation-legal` status and staging;
- stop on mismatch.

### 3.2 Gate E1 — Human Target Confirmation

Before any material-specific operation, an attributable qualified human must provide:

```text
matter_id
material category ID
category requiredness and analysis purpose
source/custodian identity or explicit uncertainty
source authority decision
approved local path/object reference
permitted actor and access scope
permitted operation
confidentiality/personal-information limits
review owner
```

Codex may record this decision. It may not invent, infer, or self-approve it.

### 3.3 Gate E2 — Exact Action Manifest

Every executable item requires an action row containing:

```text
action_id
approved acquisition-plan ID
matter_id
category ID
exact input path/object
expected filename/type/version/hash if known
approved operation
read scope
write target, if any
authority decision reference
human approver and date
stop conditions
```

No wildcard, broad directory, unresolved environment variable, inferred source, or numeric category shorthand may define an action target.

### 3.4 Gate E3 — Controlled Local Intake

Only materials already provided or placed by an authorized human at an exact approved local path may be registered. Permissible later operations, if explicitly approved per action row, are limited to:

- existence and file-type check;
- read access needed to compute byte size and SHA-256;
- creation of a documentation-only receipt/registry entry;
- comparison with a previously registered hash;
- recording a human-provided source, matter, entity, and review decision;
- readiness re-evaluation using frozen rules.

This Handoff does not authorize moving, copying, downloading, uploading, converting, parsing, OCR, transcription, or substantive content reading.

### 3.5 Gate E4 — Identity, Review, and Readiness

```text
File / Version Identity
        ↓
Source / Acquisition Identity
        ↓
Matter Identity
        ↓
Entity / Party Attribution
        ↓
Text / OCR Readiness Classification
        ↓
Human Source-Fidelity Decision
        ↓
Qualified-Lawyer Legal-Use Decision
        ↓
Case-Bundle Readiness Decision
```

Codex may register an actual human decision and its scope. It may not manufacture a “Human Verified” record or substitute its own assessment.

## 4. Category Identity and Count Reconciliation

The current instruction refers to “7 candidate materials” but lists nine descriptive items. The adopted Acquisition Spec contains:

- four frozen CASE-A profile categories;
- seven newly proposed CASE-A candidate categories;
- eleven CASE-A planning rows total, identified as `A-P01` through `A-P11`.

Therefore:

```text
Authoritative execution identity:
A-P01 through A-P11

Numeric shorthand “7” or list count “9”:
NOT AN EXECUTABLE TARGET
```

Every category must be referenced by its exact ID and basis:

| ID | Category basis | Category |
|---|---|---|
| A-P01 | Frozen profile | Corporate/public registration |
| A-P02 | Current-instruction candidate | Legal-representative information |
| A-P03 | Current-instruction candidate | Business-person identity/authority |
| A-P04 | Current-instruction candidate | Contract/agreement |
| A-P05 | Current-instruction candidate | Orders/instructions |
| A-P06 | Frozen profile | Reconciliation/account workbook |
| A-P07 | Frozen profile | WeChat/communication record |
| A-P08 | Current-instruction candidate | Delivery/receipt material |
| A-P09 | Current-instruction candidate | Bank-flow record |
| A-P10 | Current-instruction candidate | Digital/WeChat payment record |
| A-P11 | Frozen profile | Payment vouchers/other payment source |

The seven newly proposed rows remain candidates until a qualified human confirms requiredness, source, authority, and purpose. Confirmation does not prove the material exists or is legally sufficient.

## 5. Authorized Execution Scope After Separate Approval

Approval of this Handoff may authorize only the following governed record operations, and only for action-manifest rows that satisfy every activation gate:

### 5.1 Material Collection Record

Record receipt of material already supplied or placed by an authorized human, including source declaration, acquisition authority reference, receipt time, local locator, type, version, and limitations.

It does not authorize Codex to contact or collect from an external source.

### 5.2 Evidence Status Update

Update documentation-only status for an exact evidence/document/version record:

```text
MISSING
LOCATED_UNVERIFIED
ACCESSIBLE
HASH_VERIFIED
TEXT_STATUS_UNKNOWN
HUMAN_REVIEW_PENDING
PARTIAL
BLOCKED
```

No status may be advanced beyond the evidence available and the recorded human decisions.

### 5.3 Source Confirmation Record

Register a source/custodian decision supplied by an authorized human, including uncertainty and scope. Codex cannot independently confirm legal source authenticity, authority, or attribution.

### 5.4 Hash Registration

Compute and register byte size and SHA-256 only for an exact approved local file. Hash confirms same-byte identity only.

### 5.5 Human Verification Record

Register a decision actually made by a named authorized human with date, reviewed scope, source locators, limitations, corrections, and decision type. No AI-generated or implied approval is permitted.

### 5.6 Input Readiness Re-evaluation

Apply the adopted Route A criteria to determine:

```text
READY
PARTIAL
BLOCKED
```

`READY` requires all applicable document, human, identity, access, conflict, and case-bundle gates. It is not a conclusion about authenticity, admissibility, proof sufficiency, request rights, or outcome.

## 6. CASE-A Execution Scope

### 6.1 Target Confirmation

The first permissible execution step is to obtain attributable human decisions for the exact A-P01 through A-P11 rows. The seven candidate rows must not be promoted in bulk.

For each row, record:

- required, optional, candidate, rejected, or deferred status;
- bounded analysis purpose;
- exact source and authority decision;
- approved local path if material is already provided;
- permitted registry/hash/review operation;
- continuing blocker.

### 6.2 Status Progression

```text
CANDIDATE / MISSING / UNKNOWN
        ↓
HUMAN TARGET CONFIRMED
        ↓
MATERIAL ALREADY PROVIDED AT APPROVED PATH
        ↓
RECEIPT REGISTERED
        ↓
FILE IDENTITY VERIFIED
        ↓
TEXT / OCR NEED CLASSIFIED
        ↓
HUMAN REVIEW RECORDS REGISTERED
        ↓
CASE-BUNDLE RE-EVALUATED
```

If material is not already provided under exact authority, the row remains `BLOCKED`; Codex does not seek it externally.

### 6.3 Non-Substitution

Corporate/public material cannot substitute for contract, order, reconciliation, communication, delivery, bank-flow, digital-payment, or other payment sources. Recovery of one row cannot release the bundle gate.

## 7. CASE-B Execution Scope

Exact frozen row identities are `B-P01` through `B-P05` in the adopted Acquisition Spec.

Before any local intake:

1. confirm stable matter ID and entity/source candidates;
2. confirm the category, purpose, authority owner, and exact approved local path;
3. reject filenames, historical directories, counts, or fuzzy labels as binding proof;
4. require per-file actions for every relied-upon corporate-record child;
5. stop if the source collection cannot be resolved to exact child identities.

```text
File Existence Observation
        ≠ Matter Binding
        ≠ Source Authenticity
        ≠ Legal Relevance
```

## 8. CASE-C Execution Scope

Exact frozen row identities are `C-P01` through `C-P04` in the adopted Acquisition Spec.

Mandatory order:

```text
Historical Material Reference
        ↓
Document / Source Identity Review
        ↓
Matter Identity Confirmation
        ↓
Entity / Party Attribution Confirmation
        ↓
Purpose and Access Approval
        ↓
Qualified Human Binding Approval
        ↓
Only then: exact local intake action may be authorized
```

Any failure or missing human decision yields:

```text
BLOCKED
```

The current “康尔达” label, frozen `C02-CASE-C-001 / 张成棋执行衍生案件` label, and historical filename cannot be automatically merged.

## 9. Execution Registry Record

The Execution Spec, if authorized, must define a documentation-only record with at least:

```text
execution_id
action_id
acquisition_plan_id
matter_id and identity decision
category ID and category basis
requiredness and analysis purpose
exact local path/object
declared and detected file type
source/custodian decision reference
authority owner and decision reference
receipt actor/time/method
expected and actual byte size
expected and actual SHA-256
access status
file/source/matter/entity identity statuses
text/OCR readiness class
document review decision reference
legal review decision reference
readiness result
blocking reasons
limitations
correction/supersession/invalidation lineage
audit references
```

This record is not a database or runtime schema.

## 10. Exception and Stop Handling

| Condition | Required response |
|---|---|
| No physical Project Owner decision bound to this Handoff SHA | Stop before outputs |
| Missing/mismatched baseline | `BLOCKED`; create no execution outputs unless a later authority explicitly defines blocked-result behavior |
| Category referenced only by count or prose | `BLOCKED`; resolve exact ID |
| No named human authority decision | `BLOCKED`; no material action |
| Path absent or broad/unresolved | `BLOCKED`; do not search beyond approved target |
| Path exists but access not approved | `DENIED/BLOCKED` |
| Hash mismatch | Quarantine observation or new-version proposal; no inherited status |
| Source/matter/entity conflict | `BLOCKED`; preserve alternatives and escalate to human owner |
| OCR or text extraction needed | Record classification only; do not process |
| Human review missing | `HUMAN_REVIEW_PENDING/BLOCKED` |
| New adverse/conflicting material | Reopen dependent review and readiness |
| Any requested legal conclusion | Stop and return boundary violation |

## 11. Authorized Future Outputs

Only after Architecture Review and a Project Owner decision bound to this physical Handoff SHA may Codex create exactly two files.

### Output A — Execution Spec

```text
docs/phase2/route-a/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_SPEC.md
```

The Spec must define the execution process, exact category identities, action-manifest requirements, human decision points, state transitions, exceptions, and the current executable/non-executable row set.

### Output B — Execution Result

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_A_PHYSICAL_EVIDENCE_ACQUISITION_EXECUTION_RESULT.md
```

The Result must record materials actually provided and registered, files not provided, blocked reasons, hashes computed under exact authority, human decisions actually supplied, readiness outcomes, and zero boundary drift. If no per-item action satisfies every gate, the truthful execution result is `BLOCKED / NO MATERIAL ACTION PERFORMED`.

Materialization of this Handoff does not authorize either output.

## 12. Acceptance Criteria

### PEE-001 — All Executed Sources Registered

PASS when every action actually performed has an exact category ID, local path, source/custodian record, authority decision, receipt record, actor, scope, and audit reference. Unexecuted rows remain explicit.

### PEE-002 — Evidence Lifecycle Conformance

PASS when every received material follows the adopted Route A intake, identity, text/OCR classification, human review, and bundle-gate sequence without shortcut.

### PEE-003 — Identity-Risk Materials Isolated

PASS when unresolved file/source/matter/entity/category conflicts remain `BLOCKED`, especially CASE-B fuzzy binding and CASE-C identity-first controls.

### PEE-004 — No Unverified Fact Enters Legal Fact

PASS when no file, hash, OCR/text state, source statement, or AI output is promoted to a Legal Fact or support state without the required human chain.

### PEE-005 — Human Review Gate Effective

PASS when every recorded human decision corresponds to a real named reviewer record and scope; absent review remains pending/blocked and is never fabricated.

### PEE-006 — Zero Code and Architecture Drift

PASS when only the two authorized documentation outputs are created and no code, Skill, Agent, MCP, Workflow, runtime schema, OCR, database, RAG, deployment, or canonical architecture asset changes.

## 13. Strict Forbidden Scope

```text
External Contact or Third-Party Request: NOT AUTHORIZED
Court / Bank / Registry / Platform Application or Request: NOT AUTHORIZED
Broad Filesystem Search or Discovery: NOT AUTHORIZED
File Copy / Move / Download / Upload / Conversion: NOT AUTHORIZED
New Substantive Case-Content Reading: NOT AUTHORIZED
OCR Processing or Transcription: NOT AUTHORIZED
Automatic Extraction: NOT AUTHORIZED
Database / Storage Construction: NOT AUTHORIZED
MCP Integration: NOT AUTHORIZED
Agent Development or Modification: NOT AUTHORIZED
Skill Modification: NOT AUTHORIZED
Workflow Modification: NOT AUTHORIZED
Runtime Schema Modification: NOT AUTHORIZED
Code or Test Script Creation: NOT AUTHORIZED
RAG / Vector Store: NOT AUTHORIZED
Production Deployment: NOT AUTHORIZED
Legal Analysis or Request-Right Evaluation: NOT AUTHORIZED
Route A Implementation: NOT AUTHORIZED
Route B: FROZEN / NOT AUTHORIZED
```

Also prohibited:

- recording an inferred, AI-generated, or silent “human approval”;
- treating a current instruction, category list, or numeric count as a qualified-human material-necessity decision;
- treating path, filename, same hash, or same entity name as matter/source binding;
- modifying canonical Governance Pattern, Route A Design, Validation, Recovery, or Acquisition Design assets;
- git add, commit, tag, push, release, or publication.

## 14. Required Result and Repository Checks

The future Result must record:

- this Handoff and every input hash;
- Execution Spec hash;
- exact action-manifest rows and whether each gate passed;
- actual materials provided/registered versus not provided;
- exact byte hashes computed and authority references;
- human records actually supplied versus pending;
- CASE-A/B/C readiness outcomes and blockers;
- PEE-001 through PEE-006 evidence;
- exact created/modified file list;
- zero implementation/runtime drift;
- `git diff --check`, staging, and working-tree state;
- next governance recipient.

Required checks:

```text
git diff --check: PASS
Staging Area: EMPTY
New or modified files under litigation-legal/: 0
git add / commit / tag / push / release: NOT PERFORMED
```

## 15. Governance Chain

```text
Execution Handoff Materialization
        ↓
Physical Handoff SHA-256
        ↓
Architecture Coordinator File-Level Review
        ↓
Project Owner Decision Bound to Physical SHA
        ↓
Only if approved:
Codex Execution Spec + Action-Gate Evaluation
        ↓
Only for exact rows satisfying every gate:
Controlled Local Intake / Registry / Hash Record
        ↓
Execution Result
        ↓
Architecture Review
        ↓
Project Owner Execution Closeout Decision
```

If no exact row satisfies every gate, execution closes truthfully as `BLOCKED / NO MATERIAL ACTION PERFORMED`.

## 16. Current Governance State

```text
Canonical Governance Pattern:
ACTIVE

Route A Evidence Infrastructure Design:
CLOSED

Route A Design Validation:
CLOSED

Route A Input Readiness Recovery:
CLOSED

Route A Physical Evidence Acquisition Design:
PHYSICALLY BOUND

Physical Evidence Acquisition Execution Handoff:
DRAFT v1.0 — MATERIALIZED FOR REVIEW

Physical Evidence Acquisition Execution:
NOT AUTHORIZED

Route A Implementation:
NOT AUTHORIZED

Route B:
FROZEN / NOT AUTHORIZED
```

The next governance recipient after materialization is the **Architecture Coordinator (ChatGPT)** for review of the exact physical Handoff SHA-256.
