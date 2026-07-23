# TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | `v1.0` |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Task | `TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_DESIGN` |
| Authorization | **EXECUTION DOMAIN ADAPTER DESIGN ONLY** |
| Handoff | `TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_HANDOFF.md` |
| Handoff SHA-256 | `0A1980EEEAA384067FB7EE37C3D00364A34E763BBAD49CA57FC2D468E1A9194F` |
| Concrete Domain | `NOT SELECTED` |
| Implementation | `NOT AUTHORIZED` |
| Date | `2026-07-23` |

The Project Owner's current coordination decision authorizes exactly:

```text
TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_SPEC.md
TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_RESULT.md
```

These physical names supersede only the prospective filename examples in
Handoff Section 14. The design-only scope and every prohibition remain
unchanged.

## 1. Purpose

Route B defines a governed contract layer between approved upstream artifacts
and a separately authorized execution domain.

```text
LRG Governance Controls

        ↓

Governed Input Envelope

        ↓

Execution Domain Adapter

        ↓

Domain Request / Response Candidates

        ↓

Validation and Qualified Human Review

        ↓

Optional Separately Authorized Use
```

The Adapter translates structures. It does not decide facts, law, strategy, or
outcomes, and it does not execute a domain operation in this phase.

## 2. Fixed Baseline

| Baseline | SHA-256 | Status required |
|---|---|---|
| Route B Handoff | `0A1980EEEAA384067FB7EE37C3D00364A34E763BBAD49CA57FC2D468E1A9194F` | Exact match |
| Canonical LRG v1.0 | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | Exact match |
| Route A Evidence Infrastructure Design Spec | `E163B0F53B7ADB38CB236FCA64A228C2032B6074CCB4EBB083C95DCC29A33892` | Exact match |
| Route A Design Validation Result | `15991C562DB9EA8C67CFB46781AB9C73CBA1CBA4E8D772B8FCCA47F3FB43B901` | Exact match |
| Route A External Human Input Recovery Spec | `5F04DFB5C2B01E90A7B3B92A3A312427415997BDA11C6BCCD17DA92DBEB3EDA6` | Exact match |
| Route A External Human Input Recovery Result | `586EB08F4813D97A8717F76C0DD06FCE3111E80EC36472F7CB0BB97CF7D5D063` | Exact match |

Any mismatch produces:

```text
BLOCKED — BASELINE IDENTITY FAILURE
```

Silent rebinding is prohibited.

## 3. Architectural Position

### 3.1 Layer Separation

```text
Route A — Evidence Control Layer
  Owns evidence identity, readiness, recovery, and acquisition controls

Canonical LRG — Legal Reasoning Governance Layer
  Owns mandatory matter, evidence, fact, reasoning, validation, and human-decision controls

Route B — Execution Domain Adapter Layer
  Owns bounded contract mapping and isolation for a separately authorized execution domain
```

Route B is neither a replacement for Route A nor a legal reasoning engine.

### 3.2 Non-Ownership

Route B does not own and cannot mutate:

- Evidence Registry identity or lifecycle state;
- evidence readiness or verification state;
- Matter identity, authorization, or decision state;
- source, extraction, Fact, or Legal Fact records;
- rule, issue, element, proof, request-right, defense, or gap records;
- qualified-human decisions;
- Route A Manifest status or authorized actions;
- the canonical LRG.

### 3.3 Current Concrete Domain

```text
domain_id:
PENDING_DOMAIN_SELECTION

domain_status:
NOT BOUND

domain_execution:
NOT AUTHORIZED
```

This Spec defines the reusable adapter contract. A concrete domain requires a
separate domain profile, conformance review, Project Owner approval,
implementation authorization, and validation.

## 4. Core Design Invariants

| ID | Invariant |
|---|---|
| `RBI-01` | Every request is bound to one route, domain version, matter, purpose, actor scope, and authorization set |
| `RBI-02` | Unknown, missing, stale, conflicting, or out-of-contract data fails closed |
| `RBI-03` | Mapping is explicit and traceable; the Adapter may not infer missing facts, authority, identity, scope, or intent |
| `RBI-04` | Adapter outputs are candidates, never evidence status, Legal Facts, legal decisions, or executed actions |
| `RBI-05` | Route B's upstream write-set is always empty |
| `RBI-06` | A domain failure cannot mutate Evidence, Matter, Legal Reasoning, or Human Decision state |
| `RBI-07` | Human review is mandatory before any downstream use |
| `RBI-08` | Design approval does not authorize implementation or execution |

## 5. Domain Profile Contract

A future concrete domain must publish a finite, versioned profile:

```yaml
execution_domain_profile:
  domain_id:
  name:
  version:
  purpose:
  jurisdiction_or_professional_context:
  authorized_matter_types:
  authorized_actor_roles:
  permitted_operations:
  prohibited_operations:
  input_profile:
    accepted_input_types:
    required_artifact_states:
    required_authorizations:
    matter_isolation_rules:
  output_profile:
    candidate_output_types:
    prohibited_output_types:
    disclosure_labels:
    retention_rules:
    downstream_use_boundary:
  dependency_profile:
    declared_dependencies:
    provider_status: NOT_SELECTED
  human_review_profile:
    required: true
    reviewer_qualification:
    review_checklist:
  failure_profile:
  conformance_profile:
    canonical_lrg_sha:
    control_mapping:
  status: DESIGN_ONLY
```

### 5.1 Domain Boundary Rules

A domain is valid only when:

1. its purpose is finite;
2. every operation is enumerated;
3. inputs and outputs are enumerated;
4. prohibited operations and outputs are explicit;
5. dependencies and provider assumptions are disclosed;
6. matter and actor scope are explicit;
7. review qualifications are defined;
8. the LRG conformance record has no unresolved deviation.

Broad terms such as `all legal work`, `all matters`, `any material`, or
`general execution` are invalid.

## 6. Governed Input Envelope

```yaml
governed_input_envelope:
  envelope_id:
  route: Route-B
  route_version:
  domain_id:
  domain_version:
  adapter_contract_version:
  matter:
    matter_id:
    matter_version:
    matter_authorization_reference:
    cross_matter_use: false
  actor:
    actor_reference:
    role:
    authority_reference:
  purpose:
  operation:
  input_artifacts:
    - artifact_id:
      artifact_type:
      artifact_version:
      artifact_sha256:
      source_reference:
      readiness_state:
      validation_state:
      human_review_reference:
  requested_output_scope:
  prohibited_output_scope:
  execution_authorization:
    reference:
    state:
    valid_from:
    valid_until:
  audit_correlation_id:
```

### 6.1 Input Preconditions

The Adapter contract accepts an input only if:

- route, domain, and contract versions match;
- matter identity and authorization are exact;
- actor authority covers the operation and target;
- each referenced artifact exists in an allowed state;
- evidence-dependent operations use only the readiness state allowed by the
  domain profile;
- purpose and requested output are within scope;
- no unresolved critical `BLOCKED` state exists;
- required human decisions are present and version-bound;
- any future execution authorization is separate, current, and operation
  specific.

### 6.2 Reference Is Not Access

An artifact reference records identity and provenance. It does not grant the
Adapter permission to open, read, copy, hash, transform, transmit, or register
the referenced material.

## 7. Mapping Contract

The Mapping Contract provides a deterministic, reviewable relationship between
the governed input and a domain request candidate.

```yaml
mapping_contract:
  mapping_contract_id:
  version:
  domain_id:
  domain_version:
  input_schema_version:
  output_schema_version:
  rules:
    - rule_id:
      source_path:
      target_path:
      transformation_type:
        enum:
          - DIRECT_COPY
          - ENUMERATION_MAP
          - FORMAT_NORMALIZATION
          - EXPLICIT_OMISSION
      allowed_source_states:
      null_policy:
      conflict_policy:
      provenance_required: true
      human_review_required:
  prohibited_transformations:
    - FACT_INFERENCE
    - AUTHORITY_INFERENCE
    - IDENTITY_INFERENCE
    - SCOPE_EXPANSION
    - LEGAL_CONCLUSION
    - SILENT_DEFAULT
  conformance_state: DESIGN_ONLY
```

### 7.1 Permitted Transformations

- exact field copy;
- controlled enumeration mapping;
- lossless formatting normalization;
- explicit omission of a field the domain does not accept.

### 7.2 Prohibited Transformations

- filling a missing value from context;
- deriving authority from role;
- deriving matter identity from a filename or historical association;
- promoting Evidence, extraction, or a Fact candidate to a Legal Fact;
- converting uncertainty into a positive value;
- weakening a `BLOCKED` state;
- broadening purpose, actor, matter, operation, or output scope;
- creating a legal conclusion, priority, strategy, score, or prediction.

### 7.3 Null, Gap, and Conflict Policy

```text
Required value missing:
BLOCKED — REQUIRED INPUT MISSING

Optional value missing:
EXPLICIT NULL + SOURCE TRACE

Conflicting values:
PRESERVE ALL + BLOCK OR HUMAN REVIEW

Unknown value:
UNKNOWN

Stale version:
BLOCKED — VERSION FAILURE
```

No silent default is permitted.

## 8. Adapter Request Candidate

```yaml
adapter_request_candidate:
  candidate_id:
  source_envelope_id:
  mapping_contract_id:
  mapping_contract_version:
  domain_id:
  domain_version:
  operation:
  mapped_parameters:
  field_trace:
    - target_path:
      source_path:
      source_artifact:
      source_version:
      mapping_rule_id:
  omitted_fields:
  unresolved_gaps:
  conflicts:
  authorization_check:
  matter_isolation_check:
  readiness_check:
  lrg_conformance_check:
  human_review_required: true
  status:
    enum:
      - BLOCKED
      - REJECTED
      - MAPPING_CANDIDATE
      - ELIGIBLE_FOR_EXECUTION_AUTHORIZATION_REVIEW
```

The maximum state produced by this design is
`ELIGIBLE_FOR_EXECUTION_AUTHORIZATION_REVIEW`.

It is not `AUTHORIZED`, `SENT`, `EXECUTED`, or `COMPLETED`.

## 9. Domain Response Envelope

If a later implementation and execution are separately authorized, the raw
domain response must first enter an isolation envelope:

```yaml
domain_response_envelope:
  response_id:
  request_candidate_id:
  domain_id:
  domain_version:
  provider_reference:
  response_received_at:
  raw_response_reference:
  completeness_state:
  transport_state:
  domain_error:
  response_integrity_reference:
  status: UNVALIDATED_DOMAIN_RESPONSE
```

Receipt of a response is not evidence, a fact, a legal result, an approved
output, or proof of execution success.

## 10. Adapter Output Candidate

```yaml
adapter_output_candidate:
  output_candidate_id:
  response_id:
  domain_id:
  domain_version:
  output_type:
  normalized_candidate:
  source_trace:
  mapping_trace:
  validation_findings:
  unresolved_gaps:
  adverse_or_conflicting_material:
  warnings:
  prohibited_downstream_uses:
  human_review:
    required: true
    state: PENDING
  downstream_authorization:
    state: NOT_AUTHORIZED
  status:
    enum:
      - CANDIDATE
      - BLOCKED
      - REJECTED
      - QUARANTINED
```

Every candidate must carry:

```text
DOMAIN ADAPTER CANDIDATE
NOT A LEGAL DECISION
NOT EXECUTED
DOWNSTREAM USE NOT AUTHORIZED
```

## 11. State Isolation Protocol

### 11.1 Namespace Separation

```text
Upstream Governance Namespace:
READ-ONLY REFERENCES

Route B Adapter Namespace:
REQUEST / MAPPING / RESPONSE / OUTPUT CANDIDATES

Execution Domain Namespace:
SEPARATELY AUTHORIZED EXTERNAL STATE
```

### 11.2 Read-Set and Write-Set

```yaml
adapter_transaction_boundary:
  upstream_read_set:
    - exact_versioned_references_only
  upstream_write_set: []
  route_b_write_set:
    - adapter_request_candidate
    - domain_response_envelope
    - adapter_output_candidate
    - adapter_failure_record
    - adapter_audit_record
  external_domain_write_set:
    state: NOT_AUTHORIZED
```

The empty upstream write-set is invariant.

### 11.3 No Reverse Propagation

Route B may not propagate a domain result backward into:

- Evidence status or readiness;
- Matter status or decision;
- Fact or Legal Fact;
- request-right support status;
- legal authority status;
- a human approval;
- Route A activation or acquisition state.

Any future upstream update requires a new, separately authorized upstream
review process using an explicit candidate artifact.

## 12. Triple Failure Isolation

### 12.1 Execution Domain Failure ≠ Evidence Status Mutation

```text
Domain error, timeout, or invalid response

        ↓

Route B Failure Record

        X

Evidence Registry or Readiness Change
```

Evidence identity, lifecycle, extraction, verification, and readiness remain
unchanged.

### 12.2 Execution Domain Failure ≠ Matter Decision Mutation

An adapter failure cannot change:

- matter authorization;
- matter priority;
- claim or request-right selection;
- litigation strategy;
- lawyer decision;
- execution or acquisition eligibility.

### 12.3 Execution Domain Failure ≠ Legal Reasoning Mutation

An adapter failure or response cannot rewrite:

- issues, rules, elements, or proof requirements;
- source authority or freshness;
- Facts or Legal Facts;
- support, adverse material, defenses, rebuttals, or gaps;
- `SUPPORTED`, `UNKNOWN`, or `BLOCKED` reasoning states.

## 13. Failure Taxonomy and Barrier

```yaml
adapter_failure_record:
  failure_id:
  request_or_response_id:
  failure_class:
  detected_at_stage:
  affected_route_b_objects:
  protected_upstream_objects:
  retry_eligibility:
  human_review_required:
  recovery_action_candidate:
  state:
```

| Failure | Required result | Retry | Upstream mutation |
|---|---|---|---|
| Missing required input | `BLOCKED — INPUT GAP` | After corrected input and review | None |
| Evidence not ready | `BLOCKED — READINESS FAILURE` | After separate Route A state change | None |
| Permission missing or expired | `BLOCKED — AUTHORIZATION FAILURE` | After new authorization | None |
| Matter/route mismatch | `REJECTED — ISOLATION FAILURE` | New valid envelope required | None |
| Version or provenance mismatch | `BLOCKED — IDENTITY FAILURE` | Rebind through governance | None |
| External dependency unavailable | `FAILED — DOMAIN UNAVAILABLE` | Review required | None |
| Timeout or partial response | `QUARANTINED — INCOMPLETE` | Review required | None |
| Invalid/out-of-contract output | `REJECTED / QUARANTINED` | Corrected domain profile or response | None |
| Conflicting outputs | Preserve conflict; `HUMAN REVIEW REQUIRED` | No automatic selection | None |
| Legal-decision automation detected | `REJECTED — GOVERNANCE VIOLATION` | No automatic retry | None |

### 13.1 Fail-Closed Rule

When the Adapter cannot prove that a request or output is within contract, it
must produce `BLOCKED`, `REJECTED`, or `QUARANTINED`.

It must never reinterpret failure as success.

### 13.2 Retry and Idempotency

The future contract must require:

- an idempotency key bound to request, domain, version, matter, and operation;
- no automatic retry without an applicable policy and authorization;
- every retry linked to the prior attempt;
- partial responses quarantined;
- no duplicate upstream effect;
- no fallback to a broader provider, operation, or scope.

This Design does not implement retry or idempotency.

## 14. LRG Governance Mapping

| LRG control | Route B control | Conformance |
|---|---|---|
| `LRG-00` Boundary Governance | Exact matter, purpose, actor, route, domain, operation, and authorization binding | **MANDATORY / NO OVERRIDE** |
| `LRG-01` Evidence Governance | Readiness-aware references; no Evidence Registry or lifecycle mutation | **MANDATORY / NO OVERRIDE** |
| `LRG-02` Fact Governance | Preserve source → extraction → Fact → Legal Fact separation; prohibit promotion by mapping | **MANDATORY / NO OVERRIDE** |
| `LRG-03` Legal Reasoning Governance | Preserve issue/rule/element/proof/gap trace; Adapter cannot originate legal judgment | **MANDATORY / NO OVERRIDE** |
| `LRG-04` Validation Governance | Preserve `SUPPORTED`, `UNKNOWN`, `BLOCKED`; critical blockers stop processing | **MANDATORY / NO OVERRIDE** |
| `LRG-05` Human Decision Governance | Qualified-human review required; candidate output cannot self-approve or self-execute | **MANDATORY / NO OVERRIDE** |

## 15. Human Decision Gate

The Adapter may prepare a review package containing:

- the exact input envelope;
- the mapping contract and rules used;
- field-level source traces;
- omitted inputs and unresolved gaps;
- raw response reference;
- normalized candidate;
- failures, warnings, conflicts, and adverse material;
- prohibited uses;
- version and audit references.

The qualified human reviewer decides whether to:

```text
REJECT
REQUEST CORRECTION
KEEP BLOCKED
APPROVE A CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP
```

Human approval is scoped and version-specific. It is not implementation,
provider, production, legal-opinion, or execution authorization unless a
separate decision expressly says so.

## 16. Audit and Version Contract

```yaml
adapter_audit_record:
  audit_id:
  correlation_id:
  route: Route-B
  adapter_contract_version:
  mapping_contract_version:
  domain_id:
  domain_version:
  matter_id:
  actor_reference:
  authorization_references:
  input_artifact_references:
  input_versions:
  state_transition:
  mapping_trace_reference:
  response_reference:
  failure_reference:
  output_candidate_reference:
  human_review_reference:
  downstream_authorization_reference:
  created_at:
  supersedes:
```

Rules:

- version changes never silently rewrite prior artifacts;
- correction and supersession are append-only;
- domain, mapping, and input versions are bound independently;
- every downstream candidate references exact upstream versions;
- an invalidated source reopens dependent Route B candidates without mutating
  the source.

No real audit instance is created by this Design.

## 17. Route A Preservation

The following states remain fixed:

```yaml
CASE-A-AM-001:
  status: DRAFT
  executable: false
  authorized_actions: []

confirmation_bundle:
  state: NOT_CREATED

manifest_activation:
  state: NOT_AUTHORIZED

physical_evidence_acquisition:
  state: BLOCKED

external_human_inputs_received:
  count: 0
```

Route B does not provide an alternate path around Route A's human-input,
identity, source, access, readiness, or activation gates.

## 18. Design-Time Conformance Scenarios

| Scenario | Expected contract result |
|---|---|
| Missing domain profile | `BLOCKED — DOMAIN NOT BOUND` |
| Valid domain but no matter authorization | `BLOCKED — AUTHORIZATION FAILURE` |
| Route A Manifest is DRAFT | Reject as execution authority |
| Evidence reference is not analysis-ready | `BLOCKED — READINESS FAILURE` |
| Mapping rule requires an inferred fact | Reject mapping rule |
| Domain output conflicts with upstream data | Preserve conflict and quarantine output |
| External system timeout | Create Route B failure candidate only |
| Domain response claims a final legal conclusion | Reject as governance violation |
| One matter references another matter's artifact | `REJECTED — ISOLATION FAILURE` |
| Human approves a limited candidate | Approval remains limited to exact candidate/version and separate next step |

## 19. Design Acceptance Criteria

### RB-D-001 — Baseline Binding

PASS when the Handoff, canonical LRG, and all Route A boundary hashes match.

### RB-D-002 — Finite Domain Boundary

PASS when a domain must declare finite purpose, actor, matter, operations,
inputs, outputs, dependencies, exclusions, and human review.

### RB-D-003 — Deterministic Mapping Contract

PASS when mappings are field-traceable and inference, silent defaults, scope
expansion, and legal conclusions are prohibited.

### RB-D-004 — LRG Conformance

PASS when LRG-00 through LRG-05 are fully mapped and cannot be weakened.

### RB-D-005 — Triple Failure Isolation

PASS when domain failure cannot mutate Evidence, Matter Decision, or Legal
Reasoning state.

### RB-D-006 — Route A Preservation

PASS when `CASE-A-AM-001` remains DRAFT/non-executable and all Route A
activation/acquisition blocks remain unchanged.

### RB-D-007 — Human Decision and Output Isolation

PASS when every output remains a candidate pending qualified-human review and
separate downstream authorization.

### RB-D-008 — Zero Implementation Drift

PASS when no API, MCP, Agent, Skill, workflow, database, provider integration,
runtime schema, code, case-material operation, or production execution occurs.

## 20. Explicit Boundary

```text
Concrete Domain Selection:
NOT PERFORMED

Domain Profile Activation:
NOT AUTHORIZED

Case-Material Access:
NOT PERFORMED

Evidence Registry / Matter / Legal Reasoning Mutation:
NOT PERFORMED

API / Provider Integration:
NOT AUTHORIZED

MCP / Agent / Skill / Workflow:
NOT MODIFIED

Database / Runtime Schema:
NOT CREATED

Code:
NOT MODIFIED

Domain Request / Response:
NOT CREATED OR SENT

Production Execution:
NOT AUTHORIZED

Legal Reasoning Generation:
NOT PERFORMED
```

## 21. Required Next Governance State

```text
Codex Design Spec + Result

        ↓

Architecture Coordinator Route B Design Review

        ↓

Project Owner Design Adoption Decision
```

Design adoption would still not authorize implementation, provider selection,
integration, validation execution, or production use.

```text
Route B Handoff:
APPROVED

Route B Adapter Design:
DESIGN OUTPUT — PENDING REVIEW

Concrete Domain:
NOT SELECTED

Implementation:
NOT AUTHORIZED

Production Execution:
NOT AUTHORIZED

Route A:
UNCHANGED / EXECUTION BLOCKED
```

Next recipient: **Architecture Coordinator (ChatGPT)**.
