# Legal Strategy Workflow Architecture

## Purpose And Boundary

This document defines a model-independent, human-controlled workflow that
connects an approved Legal Research Output to a legal strategy decision record.
It is decision-support architecture only. It does not generate litigation
strategy, predict outcomes, rank options, choose an option, draft legal advice
or pleadings, call an LLM, run an Agent, or connect to an external service.

The workflow uses three independent models:

```text
core/legal-strategy/schema/strategy.yaml
core/legal-strategy/schema/strategy-option.yaml
core/legal-strategy/schema/risk-assessment.yaml
```

Every Strategy carries the `matter_slug` and `issue_ref` of an existing Matter
Workspace Issue and the `research_output_ref` of an existing Legal Research
Output. The workflow reads those references without modifying their records.

## Lifecycle

```text
Research Result
      |
      v
Issue Assessment
      |
      v
Option Generation
      |
      v
Risk Review
      |
      v
Strategy Decision
      |
      v
Human Approval
```

The corresponding Strategy statuses are:

```text
research_result_received
issue_assessed
options_documented
risks_reviewed
decision_pending
awaiting_human_approval
approved
rejected
closed
```

`closed` records lifecycle closure and does not imply approval. A Strategy may
enter `approved` only when Human Approval is approved and a candidate option
has been selected by an identified human decision owner.

## Stage Contracts

### 1. Research Result

Input:

- an existing Matter and Issue reference;
- an existing Legal Research Output reference;
- its source-verification and Human Review state.

Output:

- a stable Strategy `id`;
- status `research_result_received`;
- preserved references to the Matter, Issue and Research Output.

The stage must reject unresolved or cross-Matter references. It must not copy
an unapproved research draft into `legal_position` as an approved conclusion.

### 2. Issue Assessment

Input:

- the linked Issue;
- verified Matter facts and Evidence references;
- the reviewed Legal Research Output;
- the client's authorized objective.

Output:

- one bounded Strategy `objective`;
- an explicit legal-position field, which may remain null;
- status `issue_assessed`.

Assumptions, unresolved evidence and open legal questions remain visible. This
stage does not determine a probability of success.

### 3. Option Generation

Input:

- the assessed Issue and objective;
- constraints identified by counsel;
- available, authorized forms of response.

Output:

- one or more human-authored Strategy Option records;
- advantages, prerequisites and linked risk IDs for each option;
- status `options_documented`.

The term "generation" names a workflow stage, not an automated capability.
No component may invent an option, rank options or mark an option selected.

### 4. Risk Review

Input:

- candidate options;
- verified Evidence and Legal Research Source references;
- procedural and business context supplied by authorized humans.

Output:

- separate legal, evidence, procedural and business Risk records;
- qualitative severity that may remain `unassessed`;
- documented mitigation and review status;
- status `risks_reviewed` when human review is complete.

Risk severity is not a win-rate estimate. Missing inputs must remain explicit
and must not be converted into a numerical prediction.

### 5. Strategy Decision

Input:

- reviewed options and risks;
- current legal position and client objective;
- decision authority.

Output:

- a Recommendation object containing a human-selected option reference,
  rationale and decision owner, or null fields while no decision exists;
- status `decision_pending` and then `awaiting_human_approval`.

The system does not select an option. A null Recommendation is valid and means
that no recommendation has been made.

### 6. Human Approval

Input:

- the complete Strategy, Options and Risks;
- the linked Research Output and unresolved limitations;
- the proposed Recommendation.

Output:

- matching `approval_status` and `human_approval` state;
- an identified reviewer and review time for approval or rejection;
- status `approved` or `rejected` only after the corresponding human action.

Approval authorizes no filing, sending, negotiation or external act. Any such
action requires a separate task and its own professional authorization.

## Human Approval Rules

1. Pending Strategy records must not contain a selected option that is marked
   as approved by the system.
2. An approved Strategy must reference an existing candidate option, identify
   the decision owner, contain a rationale, and record an approving reviewer
   and review time.
3. Every risk linked by an option must resolve to a Risk record in the same
   Strategy and Matter.
4. Material changes to Research Output, options, risks or objective invalidate
   approval until a human reviews the revised record.
5. Structural validation never substitutes for Human Approval.

## Operational Non-Goals

This foundation does not provide:

- automated litigation strategy or option selection;
- success-probability, judgment or recovery prediction;
- legal-opinion, pleading or filing generation;
- Agent, LLM, MCP, database or external-provider integration;
- automatic modification of Matter Workspace, Evidence or Legal Research;
- external communication, filing, negotiation or execution.
