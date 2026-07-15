# Evidence Workflow Architecture

## Status And Scope

This document defines the Evidence Workflow contract for Matter Workspace. It
is an architecture definition only. It does not provide a workflow engine,
Agent orchestration, document parser, OCR pipeline, legal-analysis algorithm,
external data connector, or user interface.

The workflow prepares a structurally valid Evidence record for later use by
human-controlled legal research and strategy processes. Reaching the final
stage does not establish authenticity, admissibility, evidentiary weight, or a
legal conclusion.

The terms `MUST`, `MUST NOT`, `SHOULD`, and `MAY` describe requirements for a
future implementation of this contract.

## Schema Contract

The workflow consumes and produces records conforming to
`core/matter-workspace/schema/evidence.yaml`. It uses the following existing
Evidence fields without redefining them:

- `id`, `matter_slug`, `title`, `evidence_type`, and `metadata` identify the
  Evidence record;
- `source`, `acquisition`, and `chain_of_custody` preserve provenance and
  acquisition information;
- `classification` records the business routing category;
- `fact_refs` and `issue_refs` record graph membership;
- `fact_relationships` and `issue_relationships` record typed graph edges;
- `authenticity`, `relevance`, and `admissibility` keep separate review
  dimensions;
- `status` records Evidence lifecycle state;
- `human_review` records the required professional review gate.

Workflow-control state is distinct from Evidence lifecycle state. A future
runtime MAY persist workflow-control state in a separately reviewed contract,
but MUST NOT add undeclared properties to an Evidence record.

## Lifecycle

```text
Evidence Intake
      |
      v
Normalization
      |
      v
Classification
      |
      v
Relationship Resolution
      |-- Fact Linking
      `-- Issue Linking
      |
      v
Evidence Review
      |
      v
Analysis Ready
```

Fact Linking and Issue Linking are parallel responsibilities inside
Relationship Resolution. An implementation MUST NOT require Fact Linking to
finish before Issue Linking begins, or the reverse. Both operate on a graph in
which one Evidence record may connect to multiple Facts and Issues.

## Workflow Control State

Each Evidence item moves through one `current_stage` value:

```text
evidence_intake
normalization
classification
relationship_resolution
evidence_review
analysis_ready
```

Every non-terminal stage has one control status:

```text
pending
in_progress
awaiting_human_review
completed
blocked
```

These values define workflow control only. They are not additional values for
the Evidence Schema `status` field.

A future control record MUST bind to exactly one `evidence_id` and SHOULD
retain an append-only transition history containing the prior stage, next
stage, actor, timestamp, reason, and human override reference. This document
does not authorize creation of that persistence format.

## Stage Contracts

### 1. Evidence Intake

Input:

- a human-submitted Evidence description or local source reference;
- the target `matter_slug`;
- available provider, holder, acquisition, and confidentiality information.

Output:

- an Intake Record bound to a stable Evidence `id` and Matter;
- recorded provenance without invented or silently supplemented facts;
- Evidence lifecycle `status` set to `received` when intake is accepted.

Completion conditions:

- the Matter and Evidence identifiers are valid;
- source and acquisition fields distinguish known values from unknown values;
- a human accepts any correction to the submitted description or provenance.

The stage MUST NOT inspect image layers, perform OCR, extract bank
transactions, parse chat histories, or retrieve external data.

### 2. Normalization

Input:

- the completed Intake Record;
- the Evidence Schema contract.

Output:

- a Schema-conformant Evidence record;
- normalized dates, identifiers, local references, and metadata;
- an explicit record of unresolved fields rather than guessed content.

Completion conditions:

- YAML and Schema validation pass;
- normalization does not change substantive source meaning;
- any material correction has passed the Intake correction gate.

During this stage, Evidence lifecycle `status` SHOULD be `reviewing`.

### 3. Classification

Input:

- the normalized Evidence record;
- its legal-form `evidence_type` and available metadata.

Output:

- one supported `classification` value;
- any human correction and its reason recorded by the future control layer.

Supported classifications are:

```text
contract
payment
communication
corporate
court_document
property
identity
other
```

Completion conditions:

- classification is valid under the Evidence Schema;
- uncertain material is classified as `other`, not forced into a more specific
  class;
- an automated suggestion remains editable and may be rejected by a human.

### 4. Relationship Resolution

Input:

- the classified Evidence record;
- existing Matter Fact and Issue identifiers.

Output:

- `fact_refs` and `issue_refs` containing the selected graph nodes;
- optional typed `fact_relationships` and `issue_relationships` explaining the
  edge semantics;
- explicit unresolved-link notes in the future control layer.

Completion conditions:

- every selected target exists in the same Matter;
- links do not cross Matter confidentiality boundaries;
- Fact and Issue links are independently reviewable;
- an empty link set is accepted explicitly rather than treated as an implicit
  success.

A relationship suggestion MUST NOT create a new Fact or Issue silently. The
workflow MAY request a separately authorized record-creation process.

### 5. Evidence Review

Input:

- the Evidence record after relationship resolution;
- source reliability and acquisition information;
- authenticity, relevance, and admissibility review dimensions;
- relationship-review outcomes.

Output:

- completed review dimensions with unresolved challenges preserved;
- a populated `human_review` object;
- Evidence lifecycle `status` set to `verified` only after approval, or
  `disputed` when a material challenge remains.

Completion conditions:

- the final Human Review Gate has an identified reviewer or remains `pending`;
- no review dimension is converted into an automatic legal conclusion;
- disagreement, missing provenance, or unlawful-acquisition concerns remain
  visible and block Analysis Ready when material.

### 6. Analysis Ready

Input:

- the reviewed Evidence record and completed workflow-control history.

Output:

- a stable reference that downstream Strategy or Research processes may read;
- no filing, sending, notification, legal opinion, or legal-effect action.

Entry conditions:

1. The Evidence record passes Schema validation.
2. Normalization and Classification are completed.
3. Relationship Resolution is completed, including explicit acceptance of any
   empty link set.
4. Evidence Review is completed.
5. `human_review.required` is `true` and `human_review.status` is `approved`.
6. Evidence lifecycle `status` is `verified`.
7. No material block or unresolved dispute remains.

Downstream consumers MUST recheck these conditions. The label Analysis Ready
does not authorize autonomous legal analysis or reliance without professional
review.

## Human Review Gates

The workflow contains four human-controlled gates:

| Gate | Trigger | Human authority |
|---|---|---|
| Intake correction | Submitted content or provenance is materially changed | Accept, revise, or reject the correction |
| Classification correction | A proposed class is uncertain or disputed | Select a supported class or `other` |
| Relationship correction | A Fact or Issue edge is proposed, removed, or disputed | Accept, revise, reject, or leave unresolved |
| Final review | Evidence is proposed for Analysis Ready | Approve, reject, or return to an earlier stage |

No automated component may bypass a gate, mark its own output approved, or
replace an existing human decision. A human override MUST identify what was
overridden and invalidate affected downstream stage completions until they are
reviewed again.

## Transition Rules

1. A stage may advance only after its completion conditions are satisfied.
2. A `blocked` stage cannot advance until the blocking reason is resolved or a
   human records an authorized disposition.
3. Fact Linking and Issue Linking may run in either order or concurrently, but
   Relationship Resolution completes only after both have a recorded outcome.
4. A correction may return an item to an earlier stage. All dependent later
   stages then become `pending` and require re-review.
5. `disputed` Evidence cannot enter Analysis Ready.
6. `archived` Evidence is outside the active workflow until a separately
   authorized reopen action restores it.
7. Analysis Ready is terminal for one workflow revision. A substantive change
   creates a new revision and reopens the earliest affected stage.
8. Every transition and human override SHOULD be append-only and attributable.

## Evidence Status Mapping

The current Evidence Schema preserves legacy status values. New workflow
implementations SHOULD use the following mapping:

| Workflow condition | Evidence `status` |
|---|---|
| Intake accepted | `received` |
| Normalization through Evidence Review | `reviewing` |
| Final review approved | `verified` |
| Material challenge unresolved | `disputed` |
| Removed from active handling | `archived` |

Legacy records remain valid. Their status MUST be interpreted without silently
rewriting the record; migration requires a separate reviewed task.

## Failure And Recovery

- Invalid YAML or Schema data blocks Normalization and returns the item for a
  scoped correction.
- Missing provenance remains explicit and blocks final approval when material.
- Unsupported classification input is rejected; uncertainty uses `other` with
  a human-readable note.
- Missing Fact or Issue targets block the affected relationship outcome and do
  not cause target creation.
- Conflicting links or review dimensions move the item to human review.
- Recovery MUST preserve the original submitted material and transition
  history. It MUST NOT rewrite source material automatically.

## Operational Boundary

This architecture does not authorize:

- OCR, PDF image-layer processing, bank-flow analysis, or chat parsing;
- NLP classification or relationship algorithms;
- Agent orchestration or a Workflow Engine;
- MCP, legal database, court-system, WPS, or enterprise integration;
- UI development;
- automatic legal opinions, evidentiary-weight decisions, filings, notices, or
  other legal-effect actions.

Any such capability requires its own bounded TASK, implementation contract,
tests, and human-review design.

## Validation Checklist

A future implementation conforms to this definition only when:

1. all six stages and their transition states are represented;
2. stage input and output contracts map to the accepted Evidence Schema;
3. Fact and Issue linking are graph-oriented and independently reviewable;
4. all four Human Review Gates are enforceable;
5. blocked, disputed, correction, revision, and archive behavior are tested;
6. existing Matter Workspace validation and project regression continue to
   pass;
7. no excluded integration or autonomous legal behavior is introduced.
