# TASK_PHASE2_C02_II_REQUEST_RIGHT_FRAMEWORK_DESIGN_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-II Request Right Framework Design |
| Version | v1.0 design execution artifact |
| Mode | Documentation-only design |
| Status | **DONE — DESIGN ONLY** |
| Approved Handoff SHA-256 | `42428EBC5C61A4B5C68B4940273EEEF8BDFE6CEDD0736958FFD1F5E93C64EDD0` |
| Handoff Review SHA-256 | `5A2241ACDDB890B57B7B59ADDFD1675C4E299C84F2C95584C34E819F7A590860` |
| Project Owner Decision SHA-256 | `6813DE519682BC49DB810C870FF3BDE1E6F3D60A6F840110B40386FDE6C012B2` |
| C02-I Validation Spec SHA-256 | `FD51E092DC8C4DA3A06BC9FB711D80CEA958E3DE6B6288EE1DB4490A4C6CD94C` |
| C02-I Validation Result SHA-256 | `F0003635F051D9CA89956EBC624F7EE8B285D7A5D8202D85B88C4EBF1664A7B7` |

This artifact defines a reviewable request-right framework design for the `litigation-legal` domain. It is not a runtime schema, Skill prompt, Agent definition, implementation plan, legal opinion, litigation strategy, or automated adjudication model.

## 1. Design Objective

C02-II inserts a request-right foundation layer into the C01 lawyer-reviewable reasoning path:

```text
Matter
  ↓
Question
  ↓
Request Right Candidate
  ↓
Legal Basis Candidate
  ↓
Constituent Element
  ↓
Required Fact / Element Fact
  ↓
Burden Candidate
  ↓
Evidence Requirement
  ↓
Evidence Reference / Gap
  ↓
Qualified Human Review
```

The design addresses the C02-I finding that facts, legal facts, request-right candidates, elements and evidence requirements need independent traceable layers. C02-I ended `BLOCKED — PARTIAL VALIDATION ONLY`; this specification does not convert that result into a successful case validation or substantive conclusion.

## 2. Design Principles

1. **Request-right entry point**: analysis begins with the requested legal consequence and candidate basis, not with an unstructured search for law.
2. **Candidate-only semantics**: every request right, legal basis, legal fact, element mapping and burden position remains a candidate until qualified human review.
3. **Source traceability**: no fact proposition may exist without a source reference or an explicit missing-source marker.
4. **No inference from labels**: case names, causes of action, filenames and inventory rows are not evidence.
5. **No outcome states**: the model uses only `UNKNOWN`, `SUPPORTED` and `BLOCKED`; it does not use `WIN`, `LOSE`, probability, score or strategy ranking.
6. **Authority freshness**: statutory and case-authority references carry source, effective-date and retrieval metadata and remain updateable.
7. **Adversarial visibility**: supporting facts, adverse facts, defenses, rebuttals and unresolved conflicts remain visible.
8. **In-domain design**: the model belongs within `litigation-legal`; it does not create a global legal-reasoning layer.
9. **Human control**: only a qualified lawyer may approve, reject, select or apply a candidate request right.

## 3. Controlled Validation Status

The only request-right validation values are:

| Status | Meaning | Prohibited interpretation |
|---|---|---|
| `UNKNOWN` | Inputs or review are insufficient to evaluate support | Not a negative merits conclusion |
| `SUPPORTED` | Identified evidence currently supports the candidate proposition, subject to authority and lawyer review | Not proof of truth, admissibility, sufficient proof or likely success |
| `BLOCKED` | A critical source, authority, fact, access condition or human decision is missing | Not rejection of the request right on the merits |

Partial support is represented through per-element coverage and explicit gaps, not through an additional outcome-like status. A candidate may therefore have supported elements and blocked elements while its overall state remains `BLOCKED`.

State assignment is descriptive documentation, not a runtime state machine.

## 4. Core Concept Model

### 4.1 Request Right Candidate

A Request Right Candidate identifies a requested legal consequence and its proposed basis.

```yaml
request_right_candidate:
  id: RR-<matter>-<sequence>
  matter_id: <bound matter identifier>
  question_ids: []
  requested_legal_effect: <candidate relief or consequence>
  claimant_candidate: <party reference or UNKNOWN>
  respondent_candidate: <party reference or UNKNOWN>
  procedural_posture: <litigation/arbitration/enforcement/pre-action>
  legal_basis_candidates: []
  element_ids: []
  relationship_to_other_candidates: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  blocking_reasons: []
  human_review:
    required: true
    reviewer: null
    decision: null
```

The model may record candidates as alternative, cumulative or mutually exclusive. It may not rank them by predicted success or silently choose one.

### 4.2 Legal Basis Candidate

```yaml
legal_basis_candidate:
  id: LB-<sequence>
  request_right_id: <RR id>
  authority_type: statute | regulation | judicial_interpretation | case_reference | other
  citation: <article or authority reference>
  source: <official or approved source>
  effective_from: null
  effective_to: null
  retrieval_date: null
  text_verified: false
  relevance_statement: <candidate explanation>
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  human_review_required: true
```

No legal basis is treated as current merely because it appears in a template. Missing text, effective-date uncertainty or inaccessible authority yields `BLOCKED`.

### 4.3 Constituent Element

```yaml
element:
  id: EL-<request-right>-<sequence>
  request_right_id: <RR id>
  label: <element candidate>
  element_type: constitutive | defense | procedural | other
  legal_basis_ids: []
  required_fact_ids: []
  burden_candidate_ids: []
  evidence_requirement_ids: []
  supporting_evidence_ids: []
  adverse_evidence_ids: []
  conflict_ids: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  blocking_reasons: []
  human_review_required: true
```

Element templates remain updateable and may not encode a case result as permanent doctrine.

## 5. Fact Transformation Model

### 5.1 Layer Definitions

| Layer | Definition | Required trace |
|---|---|---|
| Raw Fact | A source's statement, record entry or extracted datum | Evidence source, location, extraction method and attribution |
| Legal Fact Candidate | A normalized proposition potentially relevant to a legal question | Raw Fact IDs and transformation rationale |
| Element Fact Candidate | A proposition mapped to a specific candidate element | Legal Fact ID, element ID and mapping rationale |
| Claim-Relevant Fact Candidate | A proposition material to support, block or contest a request-right candidate | Element Fact IDs, request-right ID and conflict/gap status |

`Judicial Fact` is excluded. The framework assists pre-decision lawyer analysis and must not describe its candidates as facts found by a court.

### 5.2 Transformation Record

```yaml
fact_transformation:
  id: FT-<sequence>
  source_evidence_id: <evidence id>
  source_locator: <page/sheet/cell/message/time range>
  raw_fact_text: <source-bounded proposition>
  source_actor: <actor or UNKNOWN>
  event_time: <time or UNKNOWN>
  legal_fact_candidate: <normalized proposition>
  element_fact_candidate: <mapped proposition>
  claim_relevant_fact_candidate: <material proposition>
  request_right_ids: []
  element_ids: []
  transformation_rationale: <why each step follows>
  counter_source_ids: []
  conflict_ids: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  human_review_required: true
```

### 5.3 Transformation Controls

- Preserve the original source language or an auditable locator; do not overwrite it with a legal characterization.
- Attribute statements to the source actor instead of presenting them as objective truth.
- Separate event time, document time, extraction time and review time.
- Record ambiguity, contradiction, hearsay-like chains and missing context as gaps.
- Prohibit a direct jump from `Raw Fact` to a final request right.
- Prohibit a direct jump from evidence quantity to evidentiary weight or outcome.

## 6. Element–Fact–Evidence Mapping

### 6.1 Required Fact

```yaml
required_fact:
  id: RF-<element>-<sequence>
  element_id: <EL id>
  proposition: <fact that must be examined>
  fact_candidate_ids: []
  evidence_requirement_ids: []
  conflict_ids: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  blocking_reasons: []
```

### 6.2 Evidence Requirement

```yaml
evidence_requirement:
  id: ER-<required-fact>-<sequence>
  required_fact_id: <RF id>
  evidence_category: <contract/accounting/communication/public-record/etc.>
  purpose: <proposition the evidence may support or contest>
  expected_source: <custodian/system/person or UNKNOWN>
  evidence_reference_ids: []
  authenticity_review_required: true
  admissibility_review_required: true
  completeness_review_required: true
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  blocking_reasons: []
```

### 6.3 Evidence Reference

```yaml
evidence_reference:
  id: EV-<sequence>
  matter_id: <matter id>
  bound_path_or_object_id: <approved reference>
  sha256: <hash or BLOCKED>
  source_locator: <page/sheet/cell/message/time range>
  access_scope: <approved scope>
  extraction_method: <text/OCR/manual/table/etc.>
  source_statement_ids: []
  limitations: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  human_review_required: true
```

`SUPPORTED` means only that the referenced material currently supports the mapped candidate proposition. It does not resolve authenticity, admissibility, completeness, credibility or proof sufficiency.

## 7. Burden and Proof Interface

Burden allocation is a candidate mapping that requires current authority and human confirmation.

```yaml
burden_candidate:
  id: BP-<element>-<sequence>
  element_id: <EL id>
  proposed_bearer: <party reference or UNKNOWN>
  proposition: <fact proposition>
  authority_ids: []
  proof_rule_ids: []
  contrary_position: <alternative allocation or UNKNOWN>
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  blocking_reasons: []
  human_review_required: true
```

Rules:

- Never infer burden allocation solely from an example case.
- Record the current statutory, judicial-interpretation or evidence-rule basis and its date.
- Keep evidentiary burden, burden of persuasion, production responsibility and procedural consequence distinguishable where relevant.
- A missing authority or disputed allocation yields `BLOCKED`.
- No burden mapping authorizes a merits conclusion.

## 8. Defense and Rebuttal Integration

C02-II reuses the C01 adversarial structure rather than creating a parallel model:

```text
Request Right Candidate
  ↓
Claim Element
  ↓
Defense Candidate
  ↓
Defense Element / Required Fact
  ↓
Evidence Requirement
  ↓
Rebuttal Candidate
  ↓
Remaining Conflict or Gap
```

Defense and rebuttal records use the same Fact, Element, Evidence Requirement and controlled-status structures. They may not suppress adverse facts or convert a client position into an assumed conclusion.

## 9. Request Right Relationship Model

```yaml
request_right_relationship:
  from_request_right_id: <RR id>
  to_request_right_id: <RR id>
  relationship_type: alternative | cumulative | mutually_exclusive | prerequisite | unknown
  rationale: <source- and authority-linked explanation>
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  human_review_required: true
```

Relationships describe structure only. They do not rank candidates, recommend litigation strategy or predict which path will prevail.

## 10. Human Review Gate

Every candidate analysis follows:

```text
Machine-assisted Candidate Draft
        ↓
Source and Authority Verification
        ↓
Qualified Lawyer Review
        ↓
Lawyer Approval / Revision / Rejection
        ↓
Optional Application
```

Minimum review checklist:

- client position and requested legal effect confirmed;
- parties and procedural posture confirmed;
- source paths, hashes and access scope verified;
- authority text and effective dates verified;
- every element linked to required facts and evidence needs;
- adverse facts, defenses and conflicts visible;
- missing facts and inaccessible evidence preserved;
- no outcome, probability or automatic strategy field present.

The Human Review Gate is a governance control pattern, not a runtime workflow or state machine.

## 11. Case Validation Interfaces

These interfaces define future validation inputs and outputs. They do not analyze real cases.

### 11.1 CASE-A — Transaction Dispute Interface

Required input categories:

- party and representative identity;
- offer, acceptance, order and contract records;
- delivery, receipt, inspection and objection records;
- price, reconciliation, invoice and payment records;
- defenses, returns, set-off and communications;
- governing authority and procedural posture.

Expected design output:

- candidate contract or alternative request rights;
- element/required-fact/evidence maps;
- attribution and authority gaps;
- human-review checklist.

If transaction records are missing, the interface returns `BLOCKED`; it does not activate a claim from the dispute label.

### 11.2 CASE-B — Judgment, Enforcement and Derivative Responsibility Interface

Required input categories:

- enforceable instrument and underlying obligation;
- enforcement status and unfulfilled amount;
- corporate, shareholder and controlling-person records;
- accounting, fund-flow, asset and related-party transaction records;
- alleged conduct, causation and rebuttal materials;
- current authority for each proposed responsibility route.

Expected design output:

- underlying creditor-right candidate;
- separately modeled derivative responsibility candidates;
- element/evidence/gap mapping for each candidate;
- explicit separation of allegation, evidence and legal conclusion.

If the judgment or corporate/fund-flow record is inaccessible, the affected route returns `BLOCKED`.

### 11.3 CASE-C — Enforcement Anomaly and Derivative Litigation Interface

Required input categories:

- enforceable instrument, parties and enforcement case status;
- asset clue, ownership, transfer time and consideration;
- enforcement rulings and procedural acts;
- proposed third-party or derivative-litigation material;
- evidence for defenses and legitimate transaction explanations;
- current procedural and substantive authority.

Expected design output:

- separate procedural and substantive candidate branches;
- prerequisite and alternative relationships;
- evidence cost described as missing/available work, not success probability;
- blocked branch when a critical record is absent.

## 12. Design Validation Procedure

1. Bind the approved matter, manifest, source paths and SHA-256 values.
2. Register Raw Facts with source locators and actor attribution.
3. Transform Raw Facts into Legal Fact Candidates with written rationale.
4. Propose Request Right Candidates from requested legal effects and verified authority.
5. Decompose each candidate into Constituent Elements.
6. Map Required Facts, burden candidates and Evidence Requirements.
7. Attach supporting, adverse and conflicting evidence references.
8. Assign only `UNKNOWN`, `SUPPORTED` or `BLOCKED`.
9. Record all blocking reasons and missing material.
10. Submit the complete candidate structure to qualified lawyer review.

The procedure stops when a critical source or authority is missing. It does not fill gaps from filenames, case labels, model memory or assumed practice.

## 13. Conceptual Aggregate Record

The following documentation-only example shows composition without defining a runtime schema:

```yaml
request_right_analysis:
  matter_id: <matter id>
  client_position: <position>
  procedural_posture: <posture>
  questions: []
  request_right_candidates: []
  legal_basis_candidates: []
  elements: []
  raw_facts: []
  fact_transformations: []
  required_facts: []
  burden_candidates: []
  evidence_requirements: []
  evidence_references: []
  defenses: []
  rebuttals: []
  conflicts: []
  gaps: []
  validation_status: UNKNOWN | SUPPORTED | BLOCKED
  human_review:
    required: true
    status: BLOCKED
```

## 14. Risks and Controls

| Risk | Control |
|---|---|
| Facts are rewritten as conclusions | Preserve source statement, locator and transformation rationale |
| Claim label drives analysis | Require requested legal effect, authority and element mapping |
| Missing evidence is treated as negative proof | Use `BLOCKED` and explicit gap reasons |
| Evidence volume becomes proof strength | Separate evidence reference from authenticity, admissibility and sufficiency review |
| Stale authority is reused | Require source, effective dates, retrieval date and text verification |
| Candidate becomes strategy recommendation | Prohibit ranking, probability and automatic selection |
| Adverse material is hidden | Maintain supporting, adverse and conflict references |
| Case examples become permanent doctrine | Keep templates updateable and authority-dependent |

## 15. Architecture and Implementation Boundary

This design does not authorize or create:

- any file under `litigation-legal/`;
- any Skill, Agent, command, hook, workflow or runtime schema;
- any code, test script, database or knowledge graph;
- any plugin, marketplace, MCP or connector change;
- any global Legal Reasoning Core;
- any real-case merits analysis;
- any automated legal opinion, strategy, adjudication or success-rate feature.

Future implementation requires a separate Handoff that identifies exact files, pre-change hashes, rollback steps and validation controls.

## 16. Acceptance Criteria Traceability

| AC | Design response | Status |
|---|---|---|
| AC-C02-II-001 — Model prioritizes request-right entries | Sections 1, 4 and 9 define request-right candidates as the analysis entry point | PASS |
| AC-C02-II-002 — Structures Layer 1–3 mapping logic | Sections 5–7 map facts, elements, burden candidates and evidence requirements | PASS |
| AC-C02-II-003 — Restricts status indicators | Section 3 limits validation status to `UNKNOWN`, `SUPPORTED`, `BLOCKED` | PASS |
| AC-C02-II-004 — Prohibits predictions and automated strategy | Sections 2, 9, 10, 14 and 15 prohibit outcome and strategy fields | PASS |
| AC-C02-II-005 — Zero runtime-asset change | Section 15 preserves the documentation-only boundary | PASS |
| AC-C02-II-006 — Git validation | Recorded in the Design Result | PENDING RESULT VERIFICATION |

## 17. Next Governance Step

```text
Codex Design Execution
        ↓
Design Spec + Design Result
        ↓
Architecture Coordinator Review
        ↓
Project Owner Decision
```

C02-II Implementation remains `NOT AUTHORIZED` until a later, separately approved implementation Handoff.
