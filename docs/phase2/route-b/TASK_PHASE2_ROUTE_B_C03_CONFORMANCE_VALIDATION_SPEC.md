# TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **VALIDATION SPEC MATERIALIZED — SPEC REVIEW NOT AUTHORIZED** |
| Route | Phase 2 / Route B |
| Domain | `C03-ENFORCEMENT-ADVERSARIAL-DESIGN` |
| Jurisdiction Context | China Mainland |
| Authorized Scope | **CONFORMANCE VALIDATION SPEC DESIGN ONLY** |
| Fixture Instances | **NOT AUTHORIZED / NOT CREATED** |
| Validation Execution | **NOT AUTHORIZED / NOT PERFORMED** |
| Validation Result | **NOT AUTHORIZED / NOT CREATED** |
| Case-Material Access / OCR | **NOT AUTHORIZED / NOT PERFORMED** |
| C03 Activation | **NOT AUTHORIZED** |
| Implementation / Production | **NOT AUTHORIZED** |

This Spec defines a future, separately authorized method for reviewing fixed
C03 design text against the adopted Route B and validation-plan contracts. It
does not create a fixture or evidence instance, execute validation, evaluate a
real matter, issue a legal or operational verdict, select a provider, activate
C03, or authorize implementation.

## 1. Fixed Governing Inputs

| Governing input | Path | SHA-256 | Status |
|---|---|---|---|
| Governing C03 Conformance Validation Plan | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_PLAN_REVISION_CANDIDATE_V2.md` | `CA73F4872C028945A5FFBFEAACD9B42CE54898BE32E4B5ACA4838CCDB32C4CC4` | **MATCH / ACCEPTED** |
| Plan Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_PLAN_REVISION_CANDIDATE_V2_ADOPTION_DECISION.md` | `085934CC33BD100CA7D3F4729E4E38137541B0CC753EF0F7A54350C4A705458F` | **MATCH / ACCEPTED** |
| C03 Domain Profile Spec | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC.md` | `35C3F7E905D2D171301114C6AAF28DF4BCCC2609ADF528A466EC3661D4F44559` | **MATCH / REVIEW OBJECT** |
| C03 Domain Profile Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_ADOPTION_DECISION.md` | `59A350882A7A157D5CC899AD1C1D9DA88FBEACFF572C2785D4282DBB68AE489E` | **MATCH / ACCEPTED** |
| Route B Adapter Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_DESIGN_ADOPTION_DECISION.md` | `F097CF521FB3A2A917055FC4B0B04FED937167941C83CE36F8B402DC69FB49BE` | **MATCH / ACCEPTED** |

A missing or mismatched governing input produces `BLOCKED — BASELINE IDENTITY
FAILURE`. No asset may be silently rebound, refreshed, or replaced.

## 2. Validation Objective and Non-Objectives

### 2.1 Finite Objective

```text
Determine whether the fixed C03 Domain Profile design text conforms to the
accepted Route B Adapter design, the governing C03 Validation Plan, LRG-00
through LRG-05, China-law alignment controls, matter/access isolation,
candidate-output semantics, and Fail-Closed behavior.
```

### 2.2 Explicit Non-Objectives

The future validation must not determine:

- whether a real enforcement request or legal position is correct;
- whether evidence is authentic, admissible, sufficient, or persuasive;
- whether a court, authority, party, asset, measure, objection, remedy,
  deadline, or procedure exists in a real matter;
- whether an implementation, provider, model, API, MCP, Agent, Skill, runtime,
  or workflow behaves as designed;
- whether C03 should be activated or deployed;
- whether a filing, strategy, prediction, probability, score, or legal advice
  should be issued; or
- whether any legal, enforcement, compliance, safety, or production aggregate
  verdict is established.

## 3. Defined Validation Vocabulary

| Term | Definition |
|---|---|
| Review object | The exact-SHA C03 Domain Profile Spec listed in Section 1 |
| Governing requirement | One exact control in the accepted Validation Plan or bound Route B design lineage |
| Abstract fixture specification | A field-level description of a fictional metadata state; not a populated fixture instance |
| Evidence reference | An identifier for a future review record; reference is not access |
| Target-text evidence | Text directly present in the fixed Review Object |
| Governing-plan evidence | A fixed requirement directly present in the governing Plan |
| Review-instruction metadata | Reviewer, mode, scope, and output constraints supplied by a later authorization |
| Reviewer determination | One Axis 1 conclusion entered after comparing fixed text with a requirement |
| Independently verified system evidence | A locally recomputed identity or SHA check, expressly distinguished from recorded values |
| Operational protective response | One Axis 2 design response expected from the fixed C03 contract |

No term authorizes access to a referenced asset beyond the exact inputs
permitted by a later execution authorization.

## 4. Roles and Authority Separation

| Role | Future design responsibility | Authority not granted |
|---|---|---|
| Internal Architecture Reviewer | Compare fixed design text with this Spec and record Axis 1 determinations | Plan adoption, C03 activation, implementation, or case decision |
| Qualified China-Law Reviewer | Assess terminology and authority-hierarchy fidelity if separately authorized | Automatic legal approval, filing, or execution |
| Independent External Reviewer | Optional advisory review only after separate exact-scope authorization | Governance state, owner decision, or downstream authority |
| Project Owner | Sole positive authority for adopting a Validation Result or authorizing a later stage | Reviewer independence cannot be replaced by owner status |
| Codex Executor | Materialize only exact authorized documentation outputs | Legal decision, operational authority, or external action |

Stable role identifiers are sufficient. Real-person names and identity data are
not required by this Spec.

## 5. Input Admission Contract

| Input class | Mandatory fields | Failure response |
|---|---|---|
| Governing Plan | Asset ID, path, version, SHA-256, adoption-decision SHA | `BLOCKED — PLAN IDENTITY FAILURE` |
| Review Object | Domain ID, domain version, asset ID, SHA-256, adoption-decision SHA | `BLOCKED — REVIEW OBJECT IDENTITY FAILURE` |
| Route B lineage | Adapter decision ID and SHA-256 | `BLOCKED — ROUTE B LINEAGE FAILURE` |
| Review authority | Exact authorization scope, reviewer role, mode, output asset | `BLOCKED — REVIEW AUTHORITY FAILURE` |
| Evidence references | Evidence ID, class, source category, target control, provenance status | `BLOCKED — EVIDENCE CONTRACT FAILURE` |
| Scenario specification | Scenario ID, validation layer, expected Axis 2 response, evidence class | `BLOCKED — SCENARIO CONTRACT FAILURE` |

Unknown, mixed, stale, superseded, unbound, or conflicting inputs remain
blocked or quarantined. No default, inference, enrichment, or cross-matter
substitution is permitted.

## 6. Two-Axis Semantic Contract

### 6.1 Axis 1 — Validation-Review Determinations

| Determination | Required meaning | Downstream effect |
|---|---|---|
| `PASS` | Fixed target text satisfies the exact governing requirement | Advisory record only; no activation |
| `LIMITED` | Control exists with an explicit non-blocking design limitation | No activation; owner decides whether revision is required |
| `FAIL` | Required control is absent, contradicted, or materially weakened | Validation Result cannot be accepted |
| `BLOCKED` | Identity, authority, scope, baseline, or required input is unavailable | Stop the affected and dependent checks |
| `NOT EVALUABLE` | Fixed text is insufficient for the required determination | Remain explicit; never promote to PASS |
| `QUARANTINED` | Conflict, pollution, or integrity defect prevents safe reliance | No reuse until separately resolved and rebound |

### 6.2 Axis 2 — Expected Operational Protective Responses

| Protective response | Required meaning | Upstream or downstream effect |
|---|---|---|
| `PASS` | The abstract input path satisfies the bounded C03 design contract | Candidate behavior only; no adoption, filing, or execution |
| `BLOCKED` | A required contract precondition is unavailable, invalid, stale, or unauthorized | Stop affected processing; empty upstream write set |
| `REJECTED` | Input or requested output violates a mandatory contract boundary | Reject the path; no silent fallback and empty upstream write set |
| `QUARANTINED` | Conflict or integrity defect requires isolation | Isolate; no reuse pending separate resolution |
| `KEEP BLOCKED` | An existing blocked state lacks a valid release condition | Preserve the blocked state; no implicit approval |

### 6.3 Mandatory Separation

```text
Axis 1 != Axis 2

Axis 1 Determination Must Be Independently Recorded:
YES

Axis 2 Response May Prefill Axis 1:
NO

Validation PASS May Activate C03:
NO

Operational PASS May Establish Conformance:
NO

Observed Runtime Behavior:
OUTSIDE THIS SPEC
```

## 7. Validation Layer Contracts

| Layer | Required validation contract | Mandatory evidence |
|---|---|---|
| `C03-CV0` | Recompute and compare exact asset and SHA chain; stop on any mismatch | `C03-VE-001` |
| `C03-CV1` | Verify finite purpose, roles, matter classes, operations, inputs, outputs, exclusions, and dependencies | `C03-VE-002` |
| `C03-CV2` | Verify matter, actor, authority, provenance, readiness, access, and conflict preconditions | `C03-VE-003` |
| `C03-CV3` | Verify same-matter use and reject cross-matter, mixed-matter, stale-version, and silent historical reuse | `C03-VE-004` |
| `C03-CV4` | Verify field-level trace and prohibit inference, silent default, suppression, and scope expansion | `C03-VE-005` |
| `C03-CV5` | Verify candidate-output types, labels, prohibited outputs, and downstream boundary | `C03-VE-006` |
| `C03-CV6` | Verify failure class, protective response, retry condition, quarantine, and empty upstream write set | `C03-VE-007` |
| `C03-CV7` | Verify mandatory, non-overridable LRG-00 through LRG-05 mappings | `C03-VE-008` |
| `C03-CV8` | Verify China-law terminology, normative hierarchy, case-source qualification, and non-precedential use | `C03-VE-009` |
| `C03-CV9` | Verify qualified-human gate, audit, version, correction, supersession, and separate owner authority | `C03-VE-010` |
| `C03-CV10` | Verify separation from Route A, OCR, ACOS, code, runtime, activation, and production | `C03-VE-012` |

`C03-VE-011` applies across every layer as the required defect register.

## 8. Planned Evidence Field Contracts

No evidence instance is created by this Spec.

| Evidence ID | Future record purpose | Mandatory abstract fields |
|---|---|---|
| `C03-VE-001` | Baseline identity report | Asset ID, path, expected SHA, recomputed SHA, match state, verifier category |
| `C03-VE-002` | Profile completeness matrix | Profile element, source section, presence state, reviewer determination, limitation |
| `C03-VE-003` | Input gate matrix | Gate ID, mandatory field, target-text evidence, state, determination, blocker |
| `C03-VE-004` | Matter-isolation matrix | Isolation case, expected response, target-text control, determination, limitation |
| `C03-VE-005` | Mapping trace matrix | Source field, version, allowed transformation, target field, omission state, determination |
| `C03-VE-006` | Candidate-output matrix | Output type, mandatory label, prohibited-output check, downstream boundary, determination |
| `C03-VE-007` | Failure-isolation matrix | Failure class, expected Axis 2 response, retry condition, upstream write set, determination |
| `C03-VE-008` | LRG mapping record | LRG ID, normative source, C03 control, non-override state, determination |
| `C03-VE-009` | China-law alignment record | Term or hierarchy control, source text, qualification, determination, limitation |
| `C03-VE-010` | Human-review and audit record | Reviewer role, checklist, exact scope, version, correction, supersession, decision boundary |
| `C03-VE-011` | Defect register | Defect ID, target/report category, severity, affected control, evidence, disposition |
| `C03-VE-012` | Boundary attestation | Prohibited boundary, accessed state, created state, reviewer basis, determination |

Every future evidence row must identify exactly one source category:

```text
TARGET_TEXT_EVIDENCE
GOVERNING_PLAN_EVIDENCE
REVIEW_INSTRUCTION_METADATA
REVIEWER_DETERMINATION
INDEPENDENTLY_VERIFIED_SYSTEM_EVIDENCE
```

Source categories may be linked but never merged.

## 9. Abstract Fixture Field Contract

The following is a field contract, not a populated fixture:

```yaml
abstract_fixture_specification:
  fixture_id: REQUIRED_SYNTHETIC_IDENTIFIER
  fictional: MUST_EQUAL_TRUE
  contains_real_matter_data: MUST_EQUAL_FALSE
  contains_personal_information: MUST_EQUAL_FALSE
  contains_sensitive_or_confidential_information: MUST_EQUAL_FALSE
  contains_credentials_secrets_keys_or_tokens: MUST_EQUAL_FALSE
  contains_file_path_or_external_locator: MUST_EQUAL_FALSE
  contains_legal_authority_not_in_fixed_sources: MUST_EQUAL_FALSE
  target_validation_layer: REQUIRED_C03_CV_IDENTIFIER
  target_control: REQUIRED_FIXED_CONTROL_IDENTIFIER
  abstract_input_state: REQUIRED_CLOSED_METADATA_STATE
  expected_axis_2_response: REQUIRED_CLOSED_PROTECTIVE_RESPONSE
  future_axis_1_determination: MUST_REMAIN_UNPOPULATED
  expected_upstream_write_set: MUST_EQUAL_EMPTY
  evidence_class: REQUIRED_C03_VE_IDENTIFIER
  limitation: REQUIRED_IF_APPLICABLE
```

Permitted abstract metadata states are limited to:

```text
BOUND
MISSING
MISMATCHED
STALE
UNREADY
CONFLICTING
CROSS_MATTER
MIXED_MATTER
UNAUTHORIZED
```

No case narrative, party, document, property clue, account, amount, deadline,
procedural event, personal information, credential, file path, URL, external
locator, or provider payload may be placed in a fixture.

## 10. Closed-Form Abstract Scenario Specifications

These rows specify future abstract checks only. They are not fixture instances
and contain no actual review determination.

| ID | Layer | Abstract condition | Expected Axis 2 response | Required evidence |
|---|---|---|---|---|
| `C03-VS-001` | `C03-CV0` | All eight fixed baselines match | `PASS` | `C03-VE-001` |
| `C03-VS-002` | `C03-CV0` | C03 Spec SHA differs from adopted SHA | `BLOCKED — BASELINE IDENTITY FAILURE` | `C03-VE-001` |
| `C03-VS-003` | `C03-CV0` | Domain ID or version is missing | `BLOCKED — DOMAIN IDENTITY FAILURE` | `C03-VE-001` |
| `C03-VS-004` | `C03-CV2` | Matter ID is absent or ambiguous | `BLOCKED — MATTER IDENTITY FAILURE` | `C03-VE-003` |
| `C03-VS-005` | `C03-CV2` | Actor role exists but authority reference is absent or expired | `BLOCKED — ACTOR AUTHORITY FAILURE` | `C03-VE-003` |
| `C03-VS-006` | `C03-CV2` | Evidence reference is not in the required readiness state | `BLOCKED — READINESS FAILURE` | `C03-VE-003` |
| `C03-VS-007` | `C03-CV2` | Artifact version or SHA is missing | `BLOCKED — PROVENANCE FAILURE` | `C03-VE-003` |
| `C03-VS-008` | `C03-CV3` | One envelope mixes two matter IDs | `REJECTED — ISOLATION FAILURE` | `C03-VE-004` |
| `C03-VS-009` | `C03-CV3` | Historical candidate is reused without exact rebinding | `REJECTED — ISOLATION FAILURE` | `C03-VE-004` |
| `C03-VS-010` | `C03-CV8` | Normative authority reference is stale or unavailable | `BLOCKED — AUTHORITY FRESHNESS FAILURE` | `C03-VE-009` |
| `C03-VS-011` | `C03-CV8` | A case is cited without source, tier, retrieval date, similarity, or distinctions | `BLOCKED — CASE AUTHORITY QUALIFICATION FAILURE` | `C03-VE-009` |
| `C03-VS-012` | `C03-CV4` | Field is copied directly with complete trace | `PASS — DIRECT_COPY` | `C03-VE-005` |
| `C03-VS-013` | `C03-CV4` | Enumerated value is mapped through an explicit closed mapping | `PASS — ENUMERATION_MAP` | `C03-VE-005` |
| `C03-VS-014` | `C03-CV4` | Missing value would require fact, identity, authority, or procedural inference | `REJECTED — MAPPING CONTRACT FAILURE` | `C03-VE-005` |
| `C03-VS-015` | `C03-CV4` | Missing value is silently defaulted | `REJECTED — MAPPING CONTRACT FAILURE` | `C03-VE-005` |
| `C03-VS-016` | `C03-CV4` | Adverse material is omitted or softened | `QUARANTINED — CONTENT INTEGRITY FAILURE` | `C03-VE-005` |
| `C03-VS-017` | `C03-CV5` | Output is one of five permitted candidate types with all labels | `PASS — CANDIDATE OUTPUT BOUND` | `C03-VE-006` |
| `C03-VS-018` | `C03-CV5` | Output claims final legal advice or an enforcement strategy | `REJECTED — OUTPUT BOUNDARY FAILURE` | `C03-VE-006` |
| `C03-VS-019` | `C03-CV5` | Output contains a court filing or external-contact instruction | `REJECTED — OUTPUT BOUNDARY FAILURE` | `C03-VE-006` |
| `C03-VS-020` | `C03-CV5` | Output requests active asset search, tracing, enrichment, or third-party access | `BLOCKED — PROHIBITED OPERATION` | `C03-VE-006` |
| `C03-VS-021` | `C03-CV6` | Domain failure attempts to mutate Evidence, Matter Decision, or Legal Reasoning | `REJECTED — WRITE-SET VIOLATION` | `C03-VE-007` |
| `C03-VS-022` | `C03-CV6` | Domain response conflicts with upstream state | `QUARANTINED — STATE CONFLICT` | `C03-VE-007` |
| `C03-VS-023` | `C03-CV9` | Qualified-human review is absent | `KEEP BLOCKED — HUMAN GATE FAILURE` | `C03-VE-010` |
| `C03-VS-024` | `C03-CV9` | Human approves one exact candidate and version | `PASS — LIMITED CANDIDATE APPROVAL ONLY` | `C03-VE-010` |
| `C03-VS-025` | `C03-CV10` | Route A DRAFT is presented as processing authority | `REJECTED — ROUTE A BOUNDARY FAILURE` | `C03-VE-012` |
| `C03-VS-026` | `C03-CV10` | OCR output is presented as a verified Fact or Legal Fact | `REJECTED — FACT GOVERNANCE FAILURE` | `C03-VE-012` |
| `C03-VS-027` | `C03-CV8` | US discovery or privilege doctrine is introduced as China-law default | `REJECTED — JURISDICTION ALIGNMENT FAILURE` | `C03-VE-009` |
| `C03-VS-028` | `C03-CV8` | Ordinary judgment is treated as binding precedent or universal rule | `REJECTED — CASE AUTHORITY HIERARCHY FAILURE` | `C03-VE-009` |

A future reviewer must independently enter one Axis 1 determination for every
row. The expected Axis 2 response is a target-design requirement and never a
prefilled review result.

## 11. Future Validation Procedure Design

| Stage | Future design action | Required stop condition |
|---|---|---|
| `C03-CVE-01` | Verify exact authorization and output asset | Missing, expired, withdrawn, or mismatched authority |
| `C03-CVE-02` | Recompute all governing-input SHAs | Any missing or mismatched asset |
| `C03-CVE-03` | Bind Review Object, Plan, mode, scope, and reviewer role | Ambiguous identity, role, mode, or scope |
| `C03-CVE-04` | Admit only authorized fixed-text evidence references | Unknown source category or unauthorized access requirement |
| `C03-CVE-05` | Review CV0 through CV10 in sequence | Blocking result in a prerequisite layer |
| `C03-CVE-06` | Review all 28 scenarios and enter independent Axis 1 determinations | Missing row, prefilled determination, or undefined response |
| `C03-CVE-07` | Complete LRG and China-law alignment records | Missing source qualification or unauthorized legal inference |
| `C03-CVE-08` | Reconcile body findings with Defect Register | Count, category, or severity contradiction |
| `C03-CVE-09` | Produce exact authorized Validation Result only | Output name or scope mismatch |
| `C03-CVE-10` | Hold for separate internal review and owner decision | Any attempted automatic acceptance or activation |

No stage in this table is executable under this Spec materialization.

## 12. LRG Conformance Contract

| LRG control | Mandatory validation | PASS condition |
|---|---|---|
| `LRG-00` | Domain, matter, actor, purpose, operation, version, and authority | Every boundary is exact and Fail-Closed |
| `LRG-01` | Evidence references, readiness, access separation, and write sets | Reference never becomes access; Evidence Registry remains immutable |
| `LRG-02` | Source, extraction, Fact, and Legal Fact transitions | No automatic promotion or inference |
| `LRG-03` | Candidate dimensions and prohibited outputs | C03 cannot originate final legal judgment or strategy |
| `LRG-04` | Adverse, conflict, gap, blocked, and quarantine states | Uncertainty and adverse material remain visible |
| `LRG-05` | Human-review packet and downstream authority | Candidate cannot self-approve or self-execute |

## 13. China-Law Alignment Contract

The future validation must verify that:

1. China Mainland law remains the default context;
2. US discovery, deposition, subpoena, privilege, or work-product doctrines
   are not imported as default rules or protections;
3. statutes, administrative regulations, judicial interpretations, and valid
   mandatory rules remain the primary normative layer;
4. case materials remain updateable through the project authority interface
   when adjudication or enforcement practice matters;
5. guiding and reference cases calibrate reasoning but are not common-law
   precedent;
6. ordinary judgments are samples only and are not universalized; and
7. unavailable authority text is never represented as a verified holding.

No live authority retrieval or current-law determination is authorized by this
Spec.

## 14. Defect, Correction, and Supersession Contract

### 14.1 Target-Design Determinations

```text
TARGET_CONTROL_PARTIAL
TARGET_CONTROL_ABSENT
TARGET_CONTRADICTION
BASELINE_DRIFT
REVIEW_BLOCKER
```

### 14.2 Validation-Report Defects

```text
SCOPE_EXPANSION
UNSUPPORTED_DEFINITION
EVIDENCE_OVERSTATEMENT
SOURCE_QUALIFICATION_DEFECT
TEMPORAL_OR_STATE_OVERREACH
TABLE_OR_COUNT_DRIFT
INTERNAL_CONTRADICTION
IMPLEMENTATION_POLLUTION
```

### 14.3 Integrity Rules

- every body defect must map to exactly one primary Defect Register row;
- affected rows may be counted separately from root causes, but the counting
  method must be explicit;
- zero defects may be stated only when the body and register agree;
- a corrected Result must receive a new asset identity and SHA;
- historical invalid Results remain immutable and non-reusable;
- correction, supersession, withdrawal, and invalidation do not rewrite
  historical states; and
- no Attestation may cure a substantive content defect.

## 15. Future Validation Result Output Contract

The only conceptual Result asset permitted by a later exact authorization is:

```text
.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_C03_CONFORMANCE_VALIDATION_RESULT.md
```

The future Result must contain:

| Required Result section | Minimum content |
|---|---|
| Identity and authorization | Exact Review Object, Plan, Spec, authorization, and output identity |
| SHA verification | Expected and recomputed values with source-category qualification |
| Layer determinations | CV0 through CV10 with independent Axis 1 determinations |
| Evidence records | VE-001 through VE-012 or an explicit blocked/not-evaluable state |
| Scenario determinations | 28 rows with expected Axis 2 response and independent Axis 1 determination |
| LRG record | LRG-00 through LRG-05 determinations |
| China-law alignment | Seven required checks and their source qualification |
| Defect Register | Target-design and report-quality defects kept separate |
| Boundary record | No case material, OCR, provider, code, runtime, ACOS, or production action |
| Completion state | Advisory validation completion only; no activation or implementation authority |

The Result may summarize validation conformance counts. It may not issue an
aggregate legal, enforcement, compliance, safety, or production verdict.

## 16. Non-Executable Governance Transition Matrix

| State | Meaning | Entry requirement | Permitted next state | Automatic transition |
|---|---|---|---|---|
| `C03-CVS0` | Validation object nominated | Exact C03 Review Object named | `C03-CVS1` | **NO** |
| `C03-CVS1` | Authority bound | Exact-scope owner authorization | `C03-CVS2` | **NO** |
| `C03-CVS2` | Identity and SHA bound | Required fixed assets match | `C03-CVS3` | **NO** |
| `C03-CVS3` | Scope, mode, and role bound | Review mode and roles are exact | `C03-CVS4` | **NO** |
| `C03-CVS4` | Abstract fixture specifications ready | Field contracts complete; no instances | `C03-CVS5` | **NO** |
| `C03-CVS5` | Evidence contract ready | VE-001 through VE-012 defined | `C03-CVS6` | **NO** |
| `C03-CVS6` | Validation Spec internally reviewed | Separate read-only Spec Review PASS | `C03-CVS7` | **NO** |
| `C03-CVS7` | Validation Spec adopted | Project Owner fixed-SHA decision | `C03-CVS8` | **NO** |
| `C03-CVS8` | Validation execution authorized | Separate exact-output authorization | `C03-CVS9` | **NO** |
| `C03-CVS9` | Validation Result materialized | All authorized checks completed or blocked | `C03-CVS10` | **NO** |
| `C03-CVS10` | Validation Result reviewed | Separate read-only Result Review | `C03-CVS11` | **NO** |
| `C03-CVS11` | Project Owner Result decision | Explicit accept, reject, or hold decision | Separate activation decision only | **NO** |

This matrix is a non-executable governance contract. It is not a workflow,
state-machine implementation, scheduler, queue, runtime, or automatic router.

## 17. Validation Spec Review Questions

| ID | Spec review question |
|---|---|
| `C03-CVS-RQ-001` | Are all five governing inputs exact-SHA bound? |
| `C03-CVS-RQ-002` | Is the objective limited to fixed design-text conformance? |
| `C03-CVS-RQ-003` | Are legal merits, real-matter conclusions, implementation behavior, and activation excluded? |
| `C03-CVS-RQ-004` | Are review roles and Project Owner authority separated? |
| `C03-CVS-RQ-005` | Does the input contract fail closed for identity, authority, scope, evidence, and scenario defects? |
| `C03-CVS-RQ-006` | Are the six Axis 1 determinations closed and non-operational? |
| `C03-CVS-RQ-007` | Are the five Axis 2 responses closed and non-determinative of review results? |
| `C03-CVS-RQ-008` | Are Axis 1 and Axis 2 expressly non-interchangeable? |
| `C03-CVS-RQ-009` | Do CV0 through CV10 have exact contracts and evidence mappings? |
| `C03-CVS-RQ-010` | Do VE-001 through VE-012 define source-qualified abstract fields without instances? |
| `C03-CVS-RQ-011` | Does the fixture contract exclude all real, personal, confidential, credential, path, and external data? |
| `C03-CVS-RQ-012` | Are all 28 scenarios closed, abstract, and free of prefilled Axis 1 determinations? |
| `C03-CVS-RQ-013` | Are matter isolation, historical reuse, mapping, output, failure, and empty-write-set checks complete? |
| `C03-CVS-RQ-014` | Are LRG-00 through LRG-05 mandatory and non-overridable? |
| `C03-CVS-RQ-015` | Are China-law terminology and authority-hierarchy checks complete? |
| `C03-CVS-RQ-016` | Are target-design and report-quality defects separated and count-consistent? |
| `C03-CVS-RQ-017` | Are correction, supersession, withdrawal, and invalidation immutable and SHA-bound? |
| `C03-CVS-RQ-018` | Is the future Result output exact, finite, and advisory only? |
| `C03-CVS-RQ-019` | Is the transition matrix expressly non-executable with no automatic transition? |
| `C03-CVS-RQ-020` | Are Route A, OCR, case-material, ACOS, implementation, and production boundaries preserved? |

## 18. Validation Spec Acceptance Gates

| Gate | PASS condition |
|---|---|
| `C03-CVS-DG-001` — Governing Input Binding | Five exact governing inputs are recorded and matched |
| `C03-CVS-DG-002` — Finite Validation Objective | Only fixed C03 design-text conformance is specified |
| `C03-CVS-DG-003` — Non-Execution | No fixture, evidence instance, validation, result, code, network, or external tool is created |
| `C03-CVS-DG-004` — Role and Authority Separation | Reviewer, executor, qualified human, external reviewer, and owner roles remain distinct |
| `C03-CVS-DG-005` — Two-Axis Closure | Six Axis 1 and five Axis 2 values are closed and non-interchangeable |
| `C03-CVS-DG-006` — Layer Completeness | CV0 through CV10 have finite contracts and evidence mappings |
| `C03-CVS-DG-007` — Evidence Completeness | VE-001 through VE-012 have source-qualified abstract field contracts |
| `C03-CVS-DG-008` — Fixture Safety | Fixture fields prohibit real, personal, confidential, credential, path, and external data |
| `C03-CVS-DG-009` — Scenario Closure | Twenty-eight abstract scenarios have expected Axis 2 responses and no Axis 1 result |
| `C03-CVS-DG-010` — Isolation and Mapping | Matter, history, provenance, inference, default, suppression, and write sets fail closed |
| `C03-CVS-DG-011` — LRG and China-Law Alignment | Six LRG and seven China-law controls are explicit and non-overridable |
| `C03-CVS-DG-012` — Defect Integrity | Target and report defects are separate, mapped, and count-consistent |
| `C03-CVS-DG-013` — Result Contract | One exact future Result asset and its mandatory sections are defined |
| `C03-CVS-DG-014` — Non-Executable Lifecycle | Twelve governance states have no automatic transition |
| `C03-CVS-DG-015` — Project and Runtime Boundary | Route A, OCR, case material, ACOS, activation, implementation, and production remain unauthorized |

## 19. Materialization Boundary

```text
Validation Spec Modification After Materialization:
NOT AUTHORIZED

Validation Spec Internal Review:
NOT AUTHORIZED

Abstract Fixture Instances:
NOT CREATED / NOT AUTHORIZED

Evidence Instances:
NOT CREATED / NOT AUTHORIZED

Validation Execution:
NOT AUTHORIZED

Validation Result:
NOT CREATED / NOT AUTHORIZED

C03 Activation:
NOT AUTHORIZED

Case-Material Access / OCR / Legal Analysis:
NOT AUTHORIZED

External Model / Provider / Network / API / Connector / MCP:
NOT AUTHORIZED

Agent / Skill / Database / Executable Schema / Code / Test / Runtime:
NOT AUTHORIZED

Route A State Change:
NOT AUTHORIZED

ACOS Source-Project Change:
NOT AUTHORIZED

Git Commit / Push / Branch / Merge:
NOT AUTHORIZED
```

## 20. Current and Next Governance State

```text
Governing C03 Conformance Validation Plan:
ACCEPTED & CLOSED & SHA BOUND

C03 Conformance Validation Spec:
MATERIALIZED — SPEC REVIEW NOT AUTHORIZED

Fixture Creation:
NOT AUTHORIZED

Validation Execution:
NOT AUTHORIZED

Validation Result:
NOT AUTHORIZED / NOT CREATED

C03 Activation:
NOT AUTHORIZED

Route A Material Processing / OCR:
NOT AUTHORIZED

Implementation / Production:
NOT AUTHORIZED
```

The next eligible action is a separate Project Owner authorization for a
read-only internal Validation Spec Review. No step transitions automatically.
