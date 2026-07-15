# Legal Research Workflow Architecture

## Purpose And Boundary

This document defines an offline, model-independent workflow that connects one
Matter Workspace Issue to a human-reviewed legal-research output. It defines
data contracts and stage responsibilities only. It does not implement legal
database access, source retrieval, Agent orchestration, an LLM chain, legal
analysis, prediction, or automated legal advice.

The workflow uses three independent models:

```text
core/legal-research/schema/research-matter.yaml
core/legal-research/schema/research-source.yaml
core/legal-research/schema/research-output.yaml
```

Every Research Matter carries the `matter_slug` and `issue_ref` of an existing
Matter Workspace Issue. A validator must reject unresolved or cross-Matter
references. The workflow does not modify the Issue object.

## Lifecycle

```text
Issue Identification
        |
        v
Question Framing
        |
        v
Source Collection
        |
        v
Rule Extraction
        |
        v
Case Analysis
        |
        v
Legal Position
        |
        v
Human Review
```

The corresponding Research Matter statuses are:

```text
issue_identified
question_framed
collecting_sources
extracting_rules
analyzing_cases
drafting_position
awaiting_human_review
approved
closed
```

`approved` requires an identified human reviewer and review time. `closed`
records lifecycle closure and does not imply that the research was approved.

## Stage Contracts

### 1. Issue Identification

Input:

- an existing Matter Workspace `matter_slug`;
- an existing Issue `id` in that Matter;
- the Issue question and its known factual boundaries.

Output:

- a stable Research Matter `id`;
- one resolvable `issue_ref`;
- status `issue_identified`.

The stage must not create or rewrite an Issue silently.

### 2. Question Framing

Input:

- the linked Issue;
- jurisdiction and procedural context;
- explicit assumptions and open questions.

Output:

- one bounded `legal_question`;
- PRC jurisdiction metadata;
- a human-reviewable source requirement plan;
- status `question_framed`.

Material reframing requires human confirmation. The question must distinguish
assumed facts from verified Matter facts.

### 3. Source Collection

Input:

- the approved research question;
- source requirements.

Output:

- Research Source records with provenance and verification state;
- status `collecting_sources` while collection remains incomplete.

The architecture recognizes these source types:

| Source type | China-law meaning |
|---|---|
| `law_or_regulation` | Laws, administrative regulations, rules and other normative instruments |
| `judicial_interpretation` | Judicial interpretations and applicable judicial normative materials |
| `guiding_case` | Guiding cases, with their applicable reasoning and limits recorded |
| `adjudicative_case` | Verified adjudicative examples used as non-binding analytical patterns |
| `scholarship` | Secondary academic or professional analysis |

This source layer is abstract. `source_location` is citation metadata, not an
instruction to connect to a provider. No source is treated as verified merely
because metadata is present.

### 4. Rule Extraction

Input:

- collected source records;
- source verification outcomes;
- pinpoint locations.

Output:

- candidate rule propositions linked to source IDs;
- separate verification state for each proposition;
- status `extracting_rules` until primary authority is verified.

The stage must not silently supply a missing rule, effective date, citation or
pinpoint. Secondary sources must not be presented as primary authority.

### 5. Case Analysis

Input:

- verified guiding or adjudicative case sources;
- the Matter Issue and relevant verified facts;
- candidate rules.

Output:

- case-pattern entries with source references and treatment;
- status `analyzing_cases`.

Chinese cases are not treated as common-law precedent by default. Each pattern
must state whether it supports, distinguishes, contradicts or contextualizes a
proposition. Material factual differences remain visible.

### 6. Legal Position

Input:

- verified rules;
- reviewed case patterns;
- explicit unresolved questions and assumptions.

Output:

- draft analysis and legal position in Research Output;
- status `drafting_position` and then `awaiting_human_review`.

A structurally valid output is not an approved legal opinion. The workflow
does not file, send or publish the draft and does not update Strategy directly.

### 7. Human Review

Input:

- the complete Research Matter, sources and Research Output;
- source provenance and verification status;
- unresolved questions and contrary material.

Output:

- `review_status` and `human_review` with matching states;
- Research Matter status `approved` only after human approval;
- an approved output that a separately authorized Strategy process may read.

The reviewer may approve, reject or return the work to an earlier stage. Any
material source, rule or analysis change invalidates downstream approval until
reviewed again.

## Human Review Gates

Human confirmation is required for:

1. material Question Framing changes;
2. primary-source verification and effective-status assessment;
3. selection and treatment of case patterns;
4. the final Legal Position.

No automated component may mark its own output approved, conceal an unverified
source, or convert a structural validation result into a legal conclusion.

## Research Output Contract

Research Output keeps these responsibilities separate:

- `question` preserves the reviewed research question;
- `sources` references collected source records;
- `rules` links every proposition to one or more sources;
- `case_patterns` records comparative patterns without binding-precedent
  assumptions;
- `analysis` and `legal_position` remain nullable until drafted;
- `review_status` and `human_review` control downstream use.

Only an approved output may become Strategy input, and that handoff requires a
separate authorized workflow. Approval does not guarantee legal correctness or
current authority.

## Operational Non-Goals

This foundation does not provide:

- MCP, PKULAW, Wolters Kluwer or any other provider integration;
- automated case or authority retrieval;
- citation completion or source supplementation;
- LLM or Agent execution;
- automatic legal analysis, advice, prediction or drafting;
- modification of Matter Workspace, Evidence Workflow or Evidence Validation.
