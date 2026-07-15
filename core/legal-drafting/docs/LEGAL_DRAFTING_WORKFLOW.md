# Legal Drafting Workflow Architecture

## Purpose And Boundary

This document defines a model-independent, human-controlled workflow that
connects an existing Strategy decision record to a traceable legal-document
artifact process. The foundation stores workflow metadata and provenance. It
does not generate document text, legal advice, pleadings or signatures; file
or submit anything; call an LLM or Agent; or connect to an external service.

The workflow uses three independent models:

    core/legal-drafting/schema/draft.yaml
    core/legal-drafting/schema/document-type.yaml
    core/legal-drafting/schema/source-trace.yaml

Each Draft preserves references to a Matter, Strategy, Legal Research Output,
Document Type and Source Trace. The Source Trace makes this chain reviewable:

    Draft
      |
      v
    Strategy
      |
      v
    Research
      |
      v
    Issue
      |
      v
    Evidence
      |
      v
    Fact

Structural validity confirms only that records and references are well formed.
It does not confirm factual accuracy, legal sufficiency or professional
approval.

## Lifecycle

    Draft Request
          |
          v
    Outline
          |
          v
    Drafting
          |
          v
    Legal Review
          |
          v
    Revision
          |
          v
    Approval
          |
          v
    Archive

The corresponding Draft statuses are:

    draft_requested
    outlining
    drafting
    legal_review
    revision_required
    awaiting_approval
    approved
    rejected
    archived

Archived status records lifecycle closure. It does not authorize filing,
sending, signing or reliance.

## Stage Contracts

### 1. Draft Request

Input:

- an existing Matter reference;
- an existing Strategy and Legal Research Output reference;
- a permitted Document Type and documented purpose.

Output:

- a stable Draft ID and revision number;
- status draft_requested;
- a Source Trace record awaiting Human Review.

No document text is generated at this stage.

### 2. Outline

Input:

- the authorized drafting purpose;
- reviewed Strategy and Research records;
- a Source Trace linking relevant Issue, Evidence and Fact records.

Output:

- status outlining;
- a human-controlled outline artifact outside this foundation.

The workflow metadata does not invent facts, authorities or arguments.

### 3. Drafting

Input:

- a human-approved outline;
- verified source materials;
- current instructions and confidentiality controls.

Output:

- status drafting;
- an incremented revision when a new draft artifact is recorded.

Draft content production is outside this architecture and requires separate
authorization.

### 4. Legal Review

Input:

- the current draft artifact;
- the complete Source Trace;
- unresolved factual, evidentiary, research and strategy limitations.

Output:

- status legal_review;
- reviewer comments recorded by the authorized professional;
- either progression to approval or status revision_required.

Schema validation is not Legal Review.

### 5. Revision

Input:

- identified review comments;
- corrected or newly verified source records;
- an authorized revision instruction.

Output:

- an incremented revision;
- preserved history and provenance;
- return to legal_review.

The system must not silently alter facts, authorities or strategy.

### 6. Approval

Input:

- the reviewed draft artifact;
- an approved Source Trace;
- an identified reviewer and review time.

Output:

- matching approval_status and Human Review state;
- status approved or rejected.

Approval is a human act and does not authorize external submission or signing.

### 7. Archive

Input:

- a completed, rejected or superseded drafting record;
- applicable retention and confidentiality controls.

Output:

- status archived;
- preserved provenance and revision history.

Archiving does not erase the Source Trace or review record.

## Document Type Model

The initial abstract categories are:

- litigation: complaint, answer, evidence list and hearing statement;
- legal_analysis: memorandum and opinion report;
- enforcement: enforcement application and investigation request.

Document Type records classify workflow artifacts only. They contain no
template text and provide no automated drafting capability.

## Human Review And Traceability Rules

1. A Draft must resolve to one Matter, Strategy, Research Output, Document Type
   and Source Trace.
2. Strategy, Research, Issue, Evidence and Fact references must stay inside the
   same Matter.
3. Source Trace approval requires an identified reviewer and review time.
4. Draft approval requires an approved Strategy, approved Source Trace,
   identified reviewer and review time.
5. Draft reviewer, approval_status and human_review must describe the same
   review state.
6. A material change to purpose, Strategy, Research, Evidence, Fact or document
   revision invalidates prior approval until a human reviews the change.
7. Structural validation never approves document content or authorizes use.

## Operational Non-Goals

This foundation does not provide:

- automatic drafting, legal-opinion generation or factual modification;
- success prediction, strategy selection or professional judgment;
- electronic signature, court filing, sending or publication;
- Agent, LLM, MCP, database, court-system or external-provider integration;
- automatic modification of Matter, Evidence, Research or Strategy assets.
