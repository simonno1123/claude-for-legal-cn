# TASK_PHASE2_ROUTE_B_C03_ENFORCEMENT_ADVERSARIAL_DOMAIN_PROFILE_SPEC

## Document Control

| Field | Value |
|---|---|
| Version | v1.0 |
| Status | **DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW** |
| Route | Phase 2 / Route B |
| Domain ID | `C03-ENFORCEMENT-ADVERSARIAL-DESIGN` |
| Domain Version | `1.0` |
| Jurisdiction Context | China Mainland |
| Authorization | **DOMAIN PROFILE DESIGN DOCUMENTS ONLY** |
| Domain Activation | **NOT AUTHORIZED** |
| Case-Material Access | **NOT AUTHORIZED / NOT PERFORMED** |
| Implementation / Production | **NOT AUTHORIZED** |

This document defines a finite, non-executable candidate Domain Profile for
structured issue identification and stress-testing in China Mainland civil and
commercial enforcement matters. It is not an enforcement action, legal
opinion, case analysis, court filing, provider selection, implementation, or
production authorization.

## 1. Fixed Design Baselines

| Baseline | Path | SHA-256 | Status |
|---|---|---|---|
| Canonical LRG v1.0 | `docs/phase2/governance/LEGAL_REASONING_GOVERNANCE_PATTERN.md` | `A3CC62153B0CA8D718523257880BC3856AEBCA5760903961B48FFB659BBBED39` | **MATCH** |
| Route B Adapter Spec | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_SPEC.md` | `C23BED2F6128D845D438ED624E399D97F03F628A32FA9F09C3A9FBBF12518C89` | **MATCH** |
| Route B Adapter Result | `.codex-coordination/outbox/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_RESULT.md` | `940D5961A9C82F9C09D1F719991D2F010AC05DD806FD1CDC004CFAF0B01C809F` | **MATCH** |
| Route B Architecture Review | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_DESIGN_REVIEW.md` | `24993891E1CB0FBBF793872C9A42E13E7A5BBF85F919E169FCACB06F52CED4D2` | **MATCH** |
| Route B Adoption Decision | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_EXECUTION_DOMAIN_ADAPTER_DESIGN_ADOPTION_DECISION.md` | `F097CF521FB3A2A917055FC4B0B04FED937167941C83CE36F8B402DC69FB49BE` | **MATCH** |
| China Legal-Term Alignment | `references/us-to-cn-legal-terms.md` | `093A7423BD134F5F32DCA487B20D775CA3341EB99DB4AE65566D12B79F6C6380` | **MATCH** |
| China Case Authority Layer | `references/china-case-authority.md` | `DA5AD4BAD036A3506E217F90740EF1FAEE726B6F872CB7560BE71F60CEDF57BD` | **MATCH** |
| Case Authority Update Interface | `references/case-authority-sources.json` | `9C20891DA062C63BA714ED51C13380F13BA758C6A5B907C005CB488243CE8B91` | **MATCH** |

A mismatch in any design baseline blocks review or later use. No silent
rebinding or transfer of authority is permitted.

## 2. Purpose and Meaning of Adversarial Design

The finite purpose of this Domain Profile is to define how a future,
separately authorized process may:

1. receive version-bound, analysis-ready references;
2. identify competing interpretations, adverse conditions, conflicts, and
   missing inputs relevant to an enforcement-matter review;
3. prepare structured candidates for a qualified China-law professional; and
4. preserve uncertainty, source trace, and downstream-use restrictions.

“Adversarial” means structured challenge and counter-position testing of an
authorized legal-analysis candidate. It does not mean obstruction of judicial
enforcement, concealment or transfer of property, harassment, unauthorized
investigation, circumvention of preservation measures, evasion of obligations,
or assistance with unlawful conduct.

## 3. Explicit Exclusions

This Domain Profile does not authorize or design an operational path to:

- open, copy, hash, transform, upload, transmit, or search case materials;
- locate or investigate a person's assets, accounts, residence, movements, or
  communications;
- contact a court, enforcement authority, party, bank, platform, registry,
  employer, custodian, or other third party;
- prepare or submit an application, objection, lawsuit, investigation request,
  preservation request, enforcement document, or external communication;
- decide whether an enforcement request, objection, additional-party request,
  procedural remedy, or substantive position should be pursued;
- generate final legal advice, litigation strategy, settlement instruction,
  outcome prediction, success probability, risk score, or compliance score;
- treat a case, judgment, model output, OCR output, or historical record as
  automatically true, current, authentic, admissible, or binding; or
- implement an API, MCP, Agent, Skill, workflow, database, queue, schema,
  provider integration, code package, runtime, pilot, or deployment.

## 4. Finite Domain Profile

```yaml
execution_domain_profile:
  domain_id: C03-ENFORCEMENT-ADVERSARIAL-DESIGN
  name: China Mainland Enforcement-Matter Adversarial Review Candidate Domain
  version: "1.0"
  purpose: structured issue identification and counter-position stress-testing for qualified-human review
  jurisdiction_or_professional_context: CHINA_MAINLAND
  authorized_matter_types:
    - CIVIL_ENFORCEMENT_REVIEW_CANDIDATE
    - COMMERCIAL_ENFORCEMENT_REVIEW_CANDIDATE
  authorized_actor_roles:
    - AUTHORIZED_MATTER_PROFESSIONAL
    - QUALIFIED_CHINA_LAWYER_REVIEWER
    - PROJECT_OWNER_DECISION_AUTHORITY
  permitted_operations:
    - VALIDATE_GOVERNED_INPUT_ENVELOPE
    - MAP_EXPLICIT_FIELDS_WITH_TRACE
    - ENUMERATE_CANDIDATE_REVIEW_DIMENSIONS
    - RECORD_ADVERSE_CONDITIONS
    - RECORD_CONFLICTS_AND_INFORMATION_GAPS
    - PREPARE_QUALIFIED_HUMAN_REVIEW_PACKET
  prohibited_operations:
    - CASE_MATERIAL_ACCESS
    - FACT_OR_AUTHORITY_INFERENCE
    - EXTERNAL_ASSET_SEARCH
    - THIRD_PARTY_CONTACT
    - LEGAL_CONCLUSION
    - STRATEGY_OR_FILING_GENERATION
    - OUTCOME_OR_PROBABILITY_PREDICTION
    - DOMAIN_EXECUTION
  dependency_profile:
    declared_dependencies: []
    provider_status: NOT_SELECTED
  status: DESIGN_ONLY
```

The three actor roles are functional governance identifiers. This design does
not require a person's real name. A later authorization must bind a stable
actor reference, role, authority, exact matter, exact operation, and validity
period before any candidate processing can occur.

## 5. Input Profile

### 5.1 Accepted Input Types

Only references already admitted through upstream governance may be described
as candidate inputs:

```text
MATTER_AUTHORITY_REFERENCE
ACTOR_AUTHORITY_REFERENCE
ANALYSIS_READY_EVIDENCE_REFERENCE
SOURCE_VERIFIED_FACT_CANDIDATE_REFERENCE
LEGAL_FACT_REVIEW_REFERENCE
PROCEDURAL_STATE_REFERENCE
CURRENT_NORMATIVE_AUTHORITY_SET_REFERENCE
CURRENT_CASE_AUTHORITY_CHECK_REFERENCE
AUTHORIZED_OUTPUT_SCOPE_REFERENCE
```

An artifact reference is not permission to access the referenced bytes.

### 5.2 Required Artifact States

| Required state | Minimum condition | Failure state |
|---|---|---|
| Matter identity bound | Exact matter ID and version | `BLOCKED — MATTER IDENTITY FAILURE` |
| Actor authority bound | Role, authority reference, operation, and validity scope | `BLOCKED — ACTOR AUTHORITY FAILURE` |
| Evidence readiness bound | Upstream state explicitly permits the requested design-time use | `BLOCKED — READINESS FAILURE` |
| Source and version trace present | Exact artifact ID, version, SHA-256, and source reference | `BLOCKED — PROVENANCE FAILURE` |
| Human review references present | Required upstream human decisions are version-bound | `BLOCKED — HUMAN GATE FAILURE` |
| Normative authority current | Current statutes, judicial interpretations, and mandatory rules are identified at review time | `BLOCKED — AUTHORITY FRESHNESS FAILURE` |
| Case authority qualified | Tier, source, retrieval date, similarity, distinctions, and limitations are recorded when cases are used | `BLOCKED — CASE AUTHORITY QUALIFICATION FAILURE` |
| No critical unresolved conflict | Critical conflicts are resolved or explicitly excluded from requested scope | `BLOCKED — UNRESOLVED CONFLICT` |

### 5.3 Matter Isolation

```yaml
matter_isolation:
  cross_matter_use: false
  inheritance_from_prior_matter: prohibited
  historical_candidate_reuse: prohibited_unless_separately_rebound
  unknown_matter: blocked
  mixed_matter_input: rejected
```

### 5.4 Current Route A Gate

At design materialization, the known Route A state remains:

```text
CASE-A-AM-001:
DRAFT / NON-EXECUTABLE

Valid Human Confirmation Records:
0

Material Processing:
BLOCKED

OCR:
DEFERRED / NOT AUTHORIZED
```

No current Route A material is admitted into C03 by this document.

## 6. Governed Input Envelope Extension

The C03 profile extends, but does not replace, the adopted Route B envelope:

```yaml
c03_governed_input_extension:
  domain_id: C03-ENFORCEMENT-ADVERSARIAL-DESIGN
  domain_version: "1.0"
  matter_reference:
  actor_authority_reference:
  operation: PREPARE_C03_REVIEW_CANDIDATE
  procedural_context_reference:
  legal_fact_review_references: []
  normative_authority_set_reference:
  case_authority_check_reference:
  requested_review_dimensions: []
  requested_output_types: []
  prohibited_output_types: []
  execution_authorization:
    state: NOT_AUTHORIZED
  audit_correlation_id:
```

Empty, unknown, stale, conflicting, unbound, or out-of-profile fields remain
visible. They cannot be silently defaulted or inferred.

## 7. Candidate Review Dimensions

The following are review dimensions, not rules, findings, or conclusions:

| ID | Candidate dimension | Required boundary |
|---|---|---|
| `C03-D01` | Enforceable-instrument identity and recorded scope | Record exact source and version; do not decide enforceability |
| `C03-D02` | Recorded parties, roles, and identity conflicts | No identity inference or additional-party conclusion |
| `C03-D03` | Recorded performance, payment, settlement, or outstanding-obligation states | Preserve conflicts; do not calculate an authoritative balance without reviewed inputs |
| `C03-D04` | Recorded procedural posture and currency | No assumption that a historical status remains current |
| `C03-D05` | Recorded court, territorial, or procedural-competence references | Candidate issue only; qualified lawyer determines legal relevance |
| `C03-D06` | Authorized property-clue references | No active search, tracing, enrichment, or third-party access |
| `C03-D07` | Recorded preservation or enforcement measures | No instruction to initiate, evade, or alter a measure |
| `C03-D08` | Recorded objections, third-party claims, insolvency, or intersecting proceedings | Preserve adverse positions and missing records |
| `C03-D09` | Recorded service, notice, and participation information | No legal-effect conclusion from metadata alone |
| `C03-D10` | Recorded time-related facts and authority-check needs | No limitation or deadline conclusion without current-law review |
| `C03-D11` | Evidence readiness and source gaps | Never promote an extraction or OCR candidate to fact |
| `C03-D12` | Contradictions and adverse material | Adverse material must not be omitted or softened |
| `C03-D13` | Current statutory, judicial-interpretation, and case-authority lookup needs | Authorities must be retrieved and qualified at review time |

## 8. China-Law Authority Interface

China Mainland law is statute-centered. A future C03 review must use current
laws, administrative regulations, judicial interpretations, and mandatory
rules as the primary normative basis.

When adjudication or enforcement practice matters, the review must use
`references/china-case-authority.md` and the update interface in
`references/case-authority-sources.json`.

Required case-authority controls:

- guiding and reference cases calibrate reasoning but are not common-law
  precedent;
- ordinary judgments are samples and cannot be universalized;
- every case reference records source, category, issuing body, case identity,
  retrieval date, similarity, distinctions, usability, and limitations;
- unavailable case text is marked `[case text not retrieved - verify]`; and
- no case may override current statutes or judicial interpretations.

No authority was researched or applied by this design materialization.

## 9. Deterministic Mapping Contract

Permitted mapping classes:

```text
DIRECT_COPY
ENUMERATION_MAP
FORMAT_NORMALIZATION
EXPLICIT_OMISSION
```

Prohibited mapping classes:

```text
FACT_INFERENCE
IDENTITY_INFERENCE
AUTHORITY_INFERENCE
PROCEDURAL_STATE_INFERENCE
SCOPE_EXPANSION
ADVERSE_MATERIAL_SUPPRESSION
LEGAL_CONCLUSION
SILENT_DEFAULT
```

Every mapped field must retain source artifact, source field, source version,
transformation class, target field, omission reason if applicable, and reviewer
status.

## 10. Candidate Output Profile

### 10.1 Permitted Candidate Outputs

```text
C03_ISSUE_MATRIX_CANDIDATE
C03_ADVERSE_CONDITION_REGISTER_CANDIDATE
C03_CONFLICT_AND_INFORMATION_GAP_REGISTER_CANDIDATE
C03_AUTHORITY_CHECK_REQUEST_CANDIDATE
C03_QUALIFIED_HUMAN_REVIEW_PACKET_CANDIDATE
```

Every output must carry:

```text
CANDIDATE — REQUIRES QUALIFIED HUMAN REVIEW
NOT LEGAL ADVICE
NOT AN ENFORCEMENT INSTRUCTION
NOT AUTHORIZED FOR FILING, CONTACT, TRANSFER, OR EXECUTION
```

### 10.2 Prohibited Outputs

```text
FINAL_LEGAL_OPINION
ENFORCEMENT_STRATEGY_OR_TACTIC
COURT_OR_AUTHORITY_SUBMISSION
ASSET_SEARCH_OR_TRACING_INSTRUCTION
ADDITIONAL_PARTY_OR_LIABILITY_CONCLUSION
OBJECTION_OR_REMEDY_CONCLUSION
SETTLEMENT_OR_PAYMENT_INSTRUCTION
OUTCOME_PREDICTION
SUCCESS_PROBABILITY
AUTOMATED_RISK_OR_COMPLIANCE_SCORE
```

### 10.3 Retention and Downstream Boundary

This design creates no candidate instance. A future profile instance must bind
retention, correction, supersession, withdrawal, and deletion rules to the
matter and authorization. No candidate may become a filing, instruction,
decision, or production input without a separate Project Owner authorization.

## 11. Failure and Isolation Profile

| Failure class | Required response | Upstream mutation |
|---|---|---|
| Missing or mismatched domain/version | `BLOCKED — DOMAIN IDENTITY FAILURE` | None |
| Missing matter or actor authority | `BLOCKED — AUTHORIZATION FAILURE` | None |
| Unready evidence reference | `BLOCKED — READINESS FAILURE` | None |
| Stale normative or case authority reference | `BLOCKED — AUTHORITY FRESHNESS FAILURE` | None |
| Cross-matter or mixed-matter input | `REJECTED — ISOLATION FAILURE` | None |
| Mapping requires inference | `REJECTED — MAPPING CONTRACT FAILURE` | None |
| Critical conflict or adverse omission | `QUARANTINED — CONTENT INTEGRITY FAILURE` | None |
| Output claims advice, filing authority, strategy, or outcome | `REJECTED — OUTPUT BOUNDARY FAILURE` | None |
| External dependency requested | `BLOCKED — DEPENDENCY NOT AUTHORIZED` | None |
| Human review absent | `KEEP BLOCKED — HUMAN GATE FAILURE` | None |

```yaml
upstream_write_set: []
route_a_write_set: []
evidence_registry_write_set: []
matter_decision_write_set: []
legal_reasoning_write_set: []
external_domain_write_set:
  state: NOT_AUTHORIZED
```

## 12. LRG-00 Through LRG-05 Mapping

| LRG control | C03 control | Status |
|---|---|---|
| `LRG-00` Boundary Governance | Exact domain, matter, actor, purpose, operation, version, and authority binding | **MANDATORY / NO OVERRIDE** |
| `LRG-01` Evidence Governance | Analysis-ready references only; reference is not access; zero Evidence Registry mutation | **MANDATORY / NO OVERRIDE** |
| `LRG-02` Fact Governance | Preserve source → extraction → Fact → Legal Fact separation; no promotion by mapping | **MANDATORY / NO OVERRIDE** |
| `LRG-03` Legal Reasoning Governance | Candidate dimensions and issue traces only; no originating legal judgment | **MANDATORY / NO OVERRIDE** |
| `LRG-04` Validation Governance | Preserve `SUPPORTED`, `UNKNOWN`, `BLOCKED`, conflict, and adverse conditions | **MANDATORY / NO OVERRIDE** |
| `LRG-05` Human Decision Governance | Qualified-human review plus separate downstream authority | **MANDATORY / NO OVERRIDE** |

## 13. Qualified-Human Review Gate

The future review packet must contain exact input and mapping identities,
source traces, omissions, conflicts, adverse conditions, authority freshness,
prohibited uses, and version references.

Permitted human dispositions:

```text
REJECT
REQUEST CORRECTION
KEEP BLOCKED
APPROVE A SPECIFIC CANDIDATE FOR A SEPARATELY AUTHORIZED NEXT STEP
```

The reviewer role may be represented by a stable governance identifier; a real
name is not required by this design. Approval remains exact-matter,
exact-version, exact-output, and exact-purpose bound.

## 14. Audit and Version Contract

```yaml
c03_audit_record_design:
  audit_id:
  correlation_id:
  domain_id: C03-ENFORCEMENT-ADVERSARIAL-DESIGN
  domain_version: "1.0"
  adapter_contract_version:
  matter_reference:
  actor_authority_reference:
  input_artifact_references: []
  input_versions: []
  mapping_trace_reference:
  gap_and_adverse_register_reference:
  authority_set_reference:
  case_authority_check_reference:
  output_candidate_reference:
  human_review_reference:
  downstream_authorization_reference:
  state_transition:
  supersedes:
```

Corrections and supersessions are append-only. A source invalidation reopens
dependent candidates but cannot silently rewrite the source or prior record.
No audit instance is created by this Spec.

## 15. Design Review Questions

| ID | Design review question |
|---|---|
| `C03-RQ-001` | Are all fixed design baselines present and SHA-bound? |
| `C03-RQ-002` | Is the domain purpose finite and limited to candidate issue identification and stress-testing? |
| `C03-RQ-003` | Is adversarial design expressly separated from obstruction, evasion, harassment, and unlawful conduct? |
| `C03-RQ-004` | Are permitted and prohibited operations exhaustively enumerated? |
| `C03-RQ-005` | Are accepted input types references rather than access grants? |
| `C03-RQ-006` | Do unbound, stale, conflicting, or unready inputs fail closed? |
| `C03-RQ-007` | Is cross-matter reuse prohibited without exact rebinding? |
| `C03-RQ-008` | Are current Route A materials excluded while confirmation and access remain blocked? |
| `C03-RQ-009` | Are candidate dimensions separated from findings, rules, and conclusions? |
| `C03-RQ-010` | Are property-clue references separated from active search or tracing? |
| `C03-RQ-011` | Are time and procedural-state issues prevented from becoming inferred conclusions? |
| `C03-RQ-012` | Are China-law terms used without US discovery or privilege defaults? |
| `C03-RQ-013` | Are statutes and judicial interpretations primary over case references? |
| `C03-RQ-014` | Are guiding, reference, and ordinary cases correctly qualified and updateable? |
| `C03-RQ-015` | Are mapping classes deterministic and field-traceable? |
| `C03-RQ-016` | Are inference, scope expansion, adverse suppression, and silent defaults prohibited? |
| `C03-RQ-017` | Are all permitted outputs labeled as candidates requiring qualified-human review? |
| `C03-RQ-018` | Are advice, strategy, filing, tracing, scoring, and prediction outputs prohibited? |
| `C03-RQ-019` | Is the upstream write set empty across Route A, Evidence, Matter Decision, and Legal Reasoning? |
| `C03-RQ-020` | Are external dependencies and providers unselected? |
| `C03-RQ-021` | Are failure, quarantine, rejection, correction, and retry boundaries explicit? |
| `C03-RQ-022` | Are LRG-00 through LRG-05 mandatory and non-overridable? |
| `C03-RQ-023` | Is qualified-human approval exact-scope and non-executing? |
| `C03-RQ-024` | Are audit, version, correction, supersession, and invalidation rules append-only? |
| `C03-RQ-025` | Is there zero case access, OCR, implementation, provider invocation, and production pollution? |

## 16. Design Acceptance Gates

| Gate | PASS condition |
|---|---|
| `C03-DG-001` — Baseline Integrity | All eight design baselines exist and match exactly |
| `C03-DG-002` — Finite Purpose | Purpose, matters, actors, operations, inputs, outputs, and exclusions are bounded |
| `C03-DG-003` — Lawful Adversarial Meaning | Obstruction, evasion, concealment, harassment, and unauthorized investigation are excluded |
| `C03-DG-004` — Input Authority | Matter, actor, purpose, readiness, source, version, and authority gates are mandatory |
| `C03-DG-005` — Matter Isolation | Cross-matter and historical reuse fail closed without rebinding |
| `C03-DG-006` — Route A Preservation | Current Route A blocked state is not bypassed or modified |
| `C03-DG-007` — China-Law Alignment | China Mainland terminology and statute-centered authority hierarchy are preserved |
| `C03-DG-008` — Case Authority Qualification | Cases remain updateable reasoning references, not precedent or replacement rules |
| `C03-DG-009` — Deterministic Mapping | Field trace exists and inference, silent defaults, and scope expansion are prohibited |
| `C03-DG-010` — Candidate Output Isolation | Outputs cannot claim advice, execution, filing, strategy, prediction, or approval |
| `C03-DG-011` — Triple Failure Isolation | Domain failures cannot mutate Evidence, Matter Decision, or Legal Reasoning |
| `C03-DG-012` — LRG Conformance | LRG-00 through LRG-05 map with no override |
| `C03-DG-013` — Human Decision Gate | Qualified-human review and separate downstream authorization remain mandatory |
| `C03-DG-014` — Version and Audit Integrity | Correction, supersession, withdrawal, and invalidation are traceable and append-only |
| `C03-DG-015` — Zero Implementation Drift | No material access, OCR, provider, code, runtime, integration, or production action occurs |

## 17. Required Next Governance State

```text
C03 Domain Profile Spec + Result
        ↓
Internal Architecture Design Review
        ↓
Project Owner Domain Profile Adoption Decision
```

Even an adopted profile would not authorize case-material access, profile
activation, validation execution, provider selection, implementation, or
production use.

```text
C03 Domain Profile:
DESIGN OUTPUT — PENDING ARCHITECTURE REVIEW

Domain Activation:
NOT AUTHORIZED

Case-Material Access / OCR:
NOT AUTHORIZED

Implementation / Production:
NOT AUTHORIZED
```
