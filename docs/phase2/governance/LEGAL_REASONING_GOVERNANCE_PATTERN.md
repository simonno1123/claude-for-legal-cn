# LEGAL_REASONING_GOVERNANCE_PATTERN

## 0. Document Control

| Field | Value |
|---|---|
| Pattern | LEGAL_REASONING_GOVERNANCE_PATTERN |
| Version | v1.0 Canonical |
| Status | **ADOPTED — CANONICAL GOVERNANCE ASSET** |
| Type | Architecture Governance Pattern |
| Source Handoff | `TASK_PHASE2_GOVERNANCE_C01_LEGAL_REASONING_PATTERN_EXTRACTION_HANDOFF.md` |
| Source Handoff SHA-256 | `2FB33555DBF2AFD32A145AC7FD491526BE62AD981763DBA27A60385280D04182` |
| Adoption Date | 2026-07-22 |
| Mode | Documentation-only governance pattern |
| Implementation | **NOT AUTHORIZED** |

### 0.1 Bound Source Artifacts

| Stage | Artifact | SHA-256 |
|---|---|---|
| C02-I | Request Right Validation Spec | `FD51E092DC8C4DA3A06BC9FB711D80CEA958E3DE6B6288EE1DB4490A4C6CD94C` |
| C02-I | Request Right Validation Result | `F0003635F051D9CA89956EBC624F7EE8B285D7A5D8202D85B88C4EBF1664A7B7` |
| C02-II | Request Right Framework Design Spec | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` |
| C02-II | Request Right Framework Design Result | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` |
| C02-III | Request Right Validation Enhancement Spec | `96C1532A2B448C4B3DB0A2926172CC7374B02E42DDF61B714295E534B4A74DFD` |
| C02-III | Request Right Validation Enhancement Result | `AF534A372D4B4824F4F402485691372D8081B4D430302DC9E3B2B0D89A9ED226` |
| C02-IV | Input Readiness Design Spec | `1CDA2E655395CA89B1762A65C9DCAA4DF82CC626C8AC8209234118B5230ACB51` |
| C02-IV | Input Readiness Design Result | `F2F1F30AECCABCAB392D267F78FF08D8EC055B3A1DB8CF6E781EFDF361D66ED0` |

C02-I is closed as a governance stage, but its substantive result remains `BLOCKED — PARTIAL VALIDATION ONLY`. C02-III was completed with material gaps. This Pattern preserves those limitations; it does not reinterpret design closure as successful real-case validation.

## 1. Pattern Overview

### 1.1 Intent

The Legal Reasoning Governance Pattern defines reusable controls for admitting matters and evidence into machine-assisted legal analysis, transforming source material into reviewable fact candidates, structuring legal-reasoning candidates, preserving uncertainty, and reserving legal judgment for qualified humans.

It is designed for legal-AI systems that assist with civil, commercial, litigation, arbitration, enforcement, investigation, or related legal work. A domain may adapt its legal concepts, evidence categories, authority sources, and review checklists, but it may not weaken the Pattern's boundary, traceability, validation, or human-decision requirements.

### 1.2 Pattern Objective

```text
Authorized Matter and Scope
        ↓
Analysis-Ready Evidence
        ↓
Source-Verified Fact Candidates
        ↓
Legal Fact and Element Candidates
        ↓
Request Right / Legal Position Candidates
        ↓
Controlled Validation States
        ↓
Qualified Human Decision
```

### 1.3 Non-Goals

This Pattern does not:

- create a global legal-reasoning runtime, database, knowledge graph, RAG system, OCR pipeline, workflow, Skill, Agent, MCP, or production service;
- prescribe a software schema, vendor, model, provider, storage platform, or user interface;
- determine evidence authenticity, admissibility, credibility, probative weight, or proof sufficiency;
- generate a final legal opinion, select a request right, choose litigation strategy, predict adjudication, or calculate success probability;
- replace statutes, judicial interpretations, evidence rules, professional duties, or qualified-lawyer judgment;
- treat China Mainland cases as common-law precedent;
- authorize Route A, Route B, or any other downstream route.

### 1.4 Pattern Composition

```text
LRG-00 Boundary Governance
        ↓
LRG-01 Evidence Governance
        ↓
LRG-02 Fact Governance
        ↓
LRG-03 Legal Reasoning Governance
        ↓
LRG-04 Validation Governance
        ↓
LRG-05 Human Decision Governance
```

The six layers are cumulative. A downstream layer may not bypass or repair a failed upstream gate through inference.

## 2. Governance Principles

1. **Authority before analysis**: a matter, user, purpose, and material set must be authorized before processing.
2. **Boundary before capability**: the system must know what it may read, for which matter, for which purpose, and what it must not do.
3. **Identity before content use**: byte identity, source, access scope, and version must be established before extracted content may be relied upon.
4. **Evidence is not fact**: a document or source statement is not automatically true, complete, relevant, or attributable to every party.
5. **Source verification is not truth adjudication**: checking transcription fidelity does not establish authenticity, credibility, admissibility, weight, or legal sufficiency.
6. **Legal facts remain candidates**: machine-assisted characterization never becomes a judicial fact or final legal determination by status alone.
7. **Candidate-only reasoning**: rules, elements, burdens, request rights, defenses, rebuttals, and outcomes remain candidates until qualified review.
8. **Traceability is mandatory**: every candidate proposition must link to a source, locator, transformation rationale, current authority where applicable, and review state.
9. **Gaps are first-class outputs**: missing sources, uncertainty, adverse facts, conflicts, inaccessible evidence, and unresolved authority remain visible.
10. **Stop rather than synthesize**: a required missing or unverified prerequisite produces `BLOCKED`; labels and prior summaries never fill the gap.
11. **Adversarial completeness**: supporting and adverse facts, defenses, rebuttals, competing explanations, and burden uncertainty must remain available to review.
12. **Current-law control**: substantive legal use requires current statutes, judicial interpretations, evidence rules, effective dates, and approved authority sources.
13. **Matter isolation**: one matter's evidence and analysis do not authorize use in another matter.
14. **Human decision supremacy**: a qualified lawyer controls legal judgment, request-right selection, advice, strategy, and application.
15. **Reversible governance**: source replacement, hash drift, correction, revoked access, or new conflict invalidates dependent readiness and analysis.

## 3. Pattern Architecture and Layer Contract

| Layer | Receives | Produces | Mandatory stop condition |
|---|---|---|---|
| LRG-00 Boundary | Matter request, actor, purpose, source scope | Authorized analysis envelope | Missing authority, scope, case identity, or permitted purpose |
| LRG-01 Evidence | Authorized source material | Registered, identity-verified, analysis-ready evidence or explicit gaps | Missing file, denied access, hash failure, incomplete processing or review |
| LRG-02 Fact | Analysis-ready evidence | Source-verified fact and Legal Fact candidates | Missing locator, unverified extraction, ambiguity hidden, or unsupported transformation |
| LRG-03 Legal Reasoning | Questions, Legal Fact candidates, current authority | Rule, element, proof, evidence-gap, request-right, defense, and rebuttal candidates | Missing authority, critical element/fact, unresolved scope, or required human decision |
| LRG-04 Validation | Candidate objects and trace records | `SUPPORTED`, `UNKNOWN`, or `BLOCKED` with reasons | Any attempt to use outcome-like states or hide a critical gap |
| LRG-05 Human Decision | Complete trace, limitations, conflicts, candidates | Human approval, revision, rejection, or deferred decision | Missing qualified reviewer, incomplete disclosure, or unauthorized intended use |

Layer outputs are contracts for review, not executable interfaces. Any later runtime representation requires separate architecture and Project Owner authorization.

## 4. LRG-00 — Boundary Governance

### 4.1 Purpose

Boundary Governance defines whether a matter and its materials may enter analysis and fixes the scope that all later layers must respect.

### 4.2 Matter Boundary Record

The conceptual boundary record contains:

| Dimension | Required content |
|---|---|
| Matter identity | Stable matter/case ID and approved name/reference |
| Client/represented position | Confirmed or explicitly `UNKNOWN` |
| Parties and roles | Candidate identities, roles, and unresolved attribution |
| Procedural posture | Pre-action, litigation, arbitration, enforcement, investigation, or other approved context |
| Requested purpose | The bounded analytical question or deliverable |
| Jurisdiction | Applicable jurisdiction candidate and review requirement |
| Authorized actors | Users, reviewers, teams, and service roles allowed to access or process |
| Evidence scope | Approved sources, locations, custodians, and excluded categories |
| Use restrictions | Confidentiality, personal information, trade-secret, privilege-like, export, retention, or contractual limits |
| Time boundary | Relevant and authorized source periods |
| Output boundary | Permitted candidate outputs and expressly prohibited conclusions |
| Review owner | Qualified human responsible for approval and scope changes |

### 4.3 Boundary Admission Gate

A matter may enter evidence processing only when:

- the matter ID and intended purpose are explicit;
- the requesting actor and processing role are authorized;
- the evidence scope and permitted use are defined;
- matter isolation and access controls can be maintained;
- required professional and confidentiality review is assigned;
- prohibited outputs and stop conditions are visible.

If any required condition is missing, the result is `BLOCKED` before content analysis.

### 4.4 Boundary Invariants

- A case name, cause-of-action label, party name, folder name, or filename is metadata, not evidence.
- Permission to locate a file is not permission to analyze or disclose its content.
- Permission for one purpose does not authorize a broader purpose.
- Permission for one matter does not authorize cross-matter reuse.
- A scope expansion requires a new or amended human authorization and re-evaluation of downstream readiness.
- The system must preserve which facts and sources were outside scope; it must not imply that absence means nonexistence.

### 4.5 Boundary Stop and Reopen Conditions

Stop analysis when:

- matter identity, client position, party attribution, jurisdiction, or procedural posture becomes materially uncertain;
- access authorization expires or is revoked;
- a source appears to belong to another matter or unauthorized person;
- requested output changes from structure/gap support to advice, strategy, outcome, or another prohibited use;
- confidentiality or professional-responsibility concerns require human decision.

Reopen only after the qualified boundary owner documents the new scope and any required reprocessing.

## 5. LRG-01 — Evidence Governance

### 5.1 Purpose

Evidence Governance establishes source identity, access, processing readiness, limitations, and review lineage before a material can support any fact candidate.

### 5.2 Minimum Evidence Object

| Field group | Required dimensions |
|---|---|
| Identity | Evidence ID, matter ID, document/version ID, original filename, document type |
| Source | Custodian/system/person, acquisition description, receipt time, attribution uncertainty |
| Storage | Approved path/object reference, storage version, byte size |
| Integrity | Registered SHA-256, recomputed hash status, verifier and verification time |
| Access | Current accessibility, permitted matter/purpose, confidentiality restrictions |
| Processing | Text-layer coverage, OCR/manual route, extraction version, page/sheet/message/region coverage |
| Review | Source-fidelity reviewer, qualified-lawyer review, scope, dates, decisions |
| Limitations | Missing pages, illegibility, truncation, layout loss, ambiguity, conflicting or superseding sources |
| Lifecycle | Received, registered, identity verified, processed, reviewed, analysis ready, blocked, rejected, superseded |
| Lineage | Supersedes/superseded-by, correction history, downstream invalidation references |

### 5.3 Evidence Status Dimensions

Statuses are independent; they must not be collapsed into one ambiguous “processed” flag.

| Dimension | Illustrative controlled values |
|---|---|
| Access | `UNKNOWN`, `ACCESSIBLE`, `MISSING`, `DENIED`, `CORRUPT`, `QUARANTINED` |
| Hash | `NOT_COMPUTED`, `REGISTERED_ONLY`, `VERIFIED`, `MISMATCH`, `NOT_AVAILABLE` |
| Text layer | `UNKNOWN`, `AVAILABLE_COMPLETE`, `AVAILABLE_PARTIAL`, `UNAVAILABLE`, `NOT_APPLICABLE` |
| OCR | `NOT_REQUIRED`, `REQUIRED`, `COMPLETED_UNVERIFIED`, `HUMAN_VERIFIED`, `FAILED`, `NOT_AVAILABLE` |
| Extraction | `NOT_STARTED`, `EXTRACTED_UNVERIFIED`, `HUMAN_VERIFIED`, `REJECTED`, `SUPERSEDED` |
| Human review | `REQUIRED`, `PENDING`, `SOURCE_VERIFIED`, `LAWYER_APPROVED_FOR_ANALYSIS`, `REJECTED`, `REVOKED` |
| Readiness | `ANALYSIS_READY`, `BLOCKED` |

These are conceptual governance states, not a runtime schema or workflow.

### 5.4 Evidence Lifecycle

```text
RECEIVED
        ↓
REGISTERED
        ↓
IDENTITY_VERIFIED
        ↓
PROCESSING_ROUTE_SELECTED
        ↓
TEXT_EXTRACTED / OCR_COMPLETED_UNVERIFIED
        ↓
SOURCE_VERIFIED
        ↓
LAWYER_APPROVED_FOR_ANALYSIS
        ↓
ANALYSIS_READY
```

At every stage, the object may enter `BLOCKED`, `QUARANTINED`, `REJECTED`, or `SUPERSEDED` with an explicit reason.

### 5.5 Evidence Invariants

- Hash equality establishes byte identity only.
- A path or filename does not establish byte identity.
- A directory count or `Bound Multiple` label cannot replace per-file identity where individual files support analysis.
- Embedded text does not establish complete or accurate extraction.
- OCR output remains a candidate transcription until checked against the image at stable locators.
- Human source verification confirms transcription fidelity and attribution within the reviewed scope; it does not establish truth or legal sufficiency.
- Missing required material blocks the affected scope and is never replaced with generated content.
- Any changed bytes, corrected extraction, revoked access, new conflict, or superseding source invalidates dependent readiness.

### 5.6 Evidence Input Gate

An evidence object is `ANALYSIS_READY` only when:

1. matter and purpose are authorized;
2. the file/object is accessible and current;
3. the recomputed SHA-256 matches the registered identity;
4. all substantive regions required for the declared scope have usable, reviewed text or transcription;
5. OCR, if required, is human-verified;
6. extraction is source-verified with reproducible locators;
7. access, confidentiality, and case-isolation controls permit use;
8. qualified-lawyer review approves the analytical scope;
9. the record is not superseded, revoked, or stale.

The case bundle is ready only when all material categories identified as required for the declared analysis satisfy the gate or are expressly determined not required by an authorized human. Optional gaps remain visible.

## 6. LRG-02 — Fact Governance

### 6.1 Purpose

Fact Governance prevents source material, extraction output, and legal characterization from collapsing into a single unreviewed “fact.”

### 6.2 Fact Generation Chain

```text
Raw Evidence
        ↓
Extracted Evidence Candidate
        ↓
Source-Verified Fact Candidate
        ↓
Legal Fact Candidate
```

| Layer | Definition | Does not establish |
|---|---|---|
| Raw Evidence | Registered source bytes/object, provenance, metadata, and access scope | Authenticity, truth, admissibility, completeness, relevance |
| Extracted Evidence Candidate | Machine- or human-produced text/data linked to an exact source locator and method | Accurate transcription, truth, or legal meaning |
| Source-Verified Fact Candidate | A source statement or normalized proposition checked against the identified source and locator | Objective truth, credibility, proof sufficiency, or legal consequence |
| Legal Fact Candidate | A lawyer-reviewable characterization proposed as relevant to a legal issue or element | Judicial fact, final legal position, or outcome |

The term “Verified Fact” must be understood as **Source-Verified Fact Candidate**, never as an automated finding of truth.

### 6.3 Transformation Record

Every proposed transformation retains:

- evidence and document/version IDs;
- exact page, sheet/cell, message/time, audio interval, or image-region locator;
- source actor or origin, including `UNKNOWN` where unresolved;
- source-faithful text/data and extraction method/version;
- normalized proposition and transformation rationale;
- event time, document time, receipt time, extraction time, and review time where relevant;
- counter-source, adverse-source, ambiguity, illegibility, missing-context, and conflict markers;
- reviewer identity, reviewed scope, corrections, and limitations;
- linked Legal Issue, element, proof requirement, and Request Right candidates;
- current validation state and blocking reasons.

### 6.4 Transformation Rules

- Preserve the original source or a reproducible locator; do not overwrite it with legal characterization.
- Attribute statements to the speaker, author, system, or record instead of presenting them as objective truth.
- Separate direct source content from normalization, inference, and legal relevance.
- Do not infer event completion from a draft, invoice, registration entry, template, or uncorroborated statement without recording the limited proposition.
- Do not infer nonexistence from an empty search result or unavailable file.
- Do not aggregate conflicting sources into a single cleaned fact; preserve the conflict.
- Do not infer evidence weight or legal outcome from document count, OCR confidence, extraction confidence, or model confidence.
- Any correction to relied-upon extraction invalidates dependent Legal Fact and reasoning candidates until re-review.

### 6.5 OCR Boundary

This shortcut is prohibited:

```text
OCR Output → Legal Fact
```

Required path:

```text
Raw Image Evidence
        ↓
OCR Candidate Transcription
        ↓
Human Source Verification
        ↓
Source-Verified Fact Candidate
        ↓
Qualified Lawyer Review
        ↓
Legal Fact Candidate
```

### 6.6 Fact Promotion Stop Conditions

Stop before Legal Fact promotion when:

- source identity, version, access, or locator is unresolved;
- extraction/OCR is incomplete or unverified;
- material context, attribution, date, amount, unit, sequence, or actor is ambiguous;
- a known conflicting source is absent from the review package;
- legal relevance requires current authority or a lawyer decision not yet obtained;
- use would exceed the authorized matter or purpose.

## 7. LRG-03 — Legal Reasoning Governance

### 7.1 Purpose

Legal Reasoning Governance structures candidate analysis without converting machine assistance into legal judgment.

### 7.2 Candidate Analysis Chain

```text
Legal Issue / Question
        ↓
Rule / Legal Basis Candidate
        ↓
Constituent Element Candidate
        ↓
Required Fact / Proof Requirement
        ↓
Evidence Mapping / Gap
        ↓
Request Right / Legal Position Candidate
        ↓
Defense / Rebuttal / Conflict
        ↓
Qualified Lawyer Review
```

The chain may be iterated in both directions for gap analysis, but no iteration may bypass source traceability, input readiness, or human decision.

### 7.3 Legal Issue / Question

A Legal Issue or Question identifies the bounded legal uncertainty to be examined. It must link to:

- matter and procedural scope;
- requested legal effect or analytical purpose;
- relevant parties/roles as candidates;
- facts and sources that prompted the question;
- unresolved factual, authority, or professional questions;
- review owner.

### 7.4 Rule / Legal Basis Candidate

A rule candidate records:

- authority type and exact citation;
- official or approved source;
- text verification status;
- effective dates and retrieval/review date;
- jurisdiction and applicability rationale;
- conflicts, amendments, hierarchy, and unresolved interpretation;
- human-review requirement.

No rule is treated as current merely because it appears in a template, prior matter, model memory, or extracted document. China Mainland cases may inform similar-case reasoning but do not operate as common-law precedent and do not replace statutes or judicial interpretations.

### 7.5 Constituent Element and Required Fact

Each element candidate links to:

- one or more rule candidates;
- required fact candidates;
- burden/proof candidates and current authority;
- supporting, adverse, and conflicting evidence;
- evidence requirements and gaps;
- defenses and rebuttals;
- validation state and blocking reasons.

Element templates remain reviewable and updateable. They may not encode a case outcome as permanent doctrine.

### 7.6 Proof Requirement and Evidence Mapping

The mapping distinguishes:

```text
Element
        ↓
Required Fact
        ↓
Evidence Requirement
        ↓
Analysis-Ready Evidence Reference
        ↓
Supporting / Adverse / Conflicting Mapping
        ↓
Gap or Review Requirement
```

The mapping must not conflate:

- evidentiary burden, burden of persuasion, production responsibility, and procedural consequence;
- evidence availability with authenticity or admissibility;
- evidence count with proof strength;
- source support with ultimate proof or likely success.

Burden and proof positions remain candidates until current authority and a qualified lawyer confirm them.

### 7.7 Request Right / Legal Position Candidate

A candidate records the requested legal effect or proposed legal position, parties, procedural posture, rule candidates, elements, fact/evidence mappings, defenses, gaps, relationships to alternatives, and review state.

Candidates may be cumulative, alternative, mutually exclusive, prerequisite-linked, or unresolved. The system may describe those relationships but may not rank candidates by predicted success or silently choose one.

### 7.8 Defense, Rebuttal, and Conflict

Every candidate path must provide symmetric space for:

- denial and alternative factual explanations;
- defenses and exceptions;
- procedural objections;
- adverse evidence;
- rebuttal candidates;
- unresolved source and authority conflicts;
- remaining gaps after rebuttal.

A client assertion or initial theory must not suppress adverse material.

### 7.9 Reasoning Stop Conditions

The system stops or returns `BLOCKED` when:

- a critical element lacks an analysis-ready source or approved gap disposition;
- current legal authority is missing, stale, inaccessible, or materially disputed;
- party identity, requested legal effect, procedural posture, or jurisdiction is unresolved;
- a burden allocation requires human legal judgment;
- evidence processing or source verification is incomplete;
- an adverse/conflicting source is known but unavailable for review;
- the next step would select strategy, give final advice, predict outcome, or exceed authorization.

## 8. LRG-04 — Validation Governance

### 8.1 Controlled States

Only three reasoning states are allowed:

| State | Meaning | Prohibited interpretation |
|---|---|---|
| `SUPPORTED` | Analysis-ready evidence currently supports a candidate proposition within stated source, authority, scope, and review limits | Not true, proved, admissible, sufficient, likely to prevail, or approved for final use |
| `UNKNOWN` | Available inputs or review are insufficient to assess support | Not rejected, disproved, or unlikely |
| `BLOCKED` | A required source, identity, authority, fact, access condition, processing step, conflict review, or human decision is missing | Not a merits rejection or loss conclusion |

The following are prohibited as reasoning states:

```text
WIN
LOSE
SUCCESS_RATE
MERITS_SCORE
AUTOMATIC_APPROVAL
MODEL_CONFIDENCE_AS_PROOF
```

### 8.2 State Assignment Rules

- States attach to a specific candidate proposition and declared scope, not to the matter as an undifferentiated whole.
- `SUPPORTED` requires source traceability and completion of all applicable upstream gates.
- If a critical prerequisite is missing, the affected candidate is `BLOCKED` even if other elements are supported.
- Noncritical uncertainty remains `UNKNOWN` and visible.
- Partial support is represented by element-level states and gaps, not a probability or outcome score.
- Aggregate status may not hide a blocked critical element.
- A human may revise or reject a state, but the reason and source lineage must remain auditable.

### 8.3 State Propagation

| Upstream event | Required downstream effect |
|---|---|
| Evidence hash mismatch or missing file | Dependent fact and reasoning candidates become `BLOCKED` |
| Extraction/OCR correction | Dependent candidates reopen for review |
| Source superseded | Prior support is marked stale; dependent states are recalculated only after review |
| Authority amendment or expiry | Rule and dependent element/request-right candidates become `UNKNOWN` or `BLOCKED` pending verification |
| Access revoked | Dependent analysis cannot be newly used; scope and retention decisions require human review |
| New adverse or conflicting source | Existing state reopens; conflict must be visible before human decision |

### 8.4 Validation Record

Each state decision preserves:

- candidate object and scope;
- supporting and adverse source references;
- rule/authority references and effective-date checks;
- gate results;
- blocking or unknown reasons;
- reviewer identity and decision date;
- limitations and required next actions;
- version and downstream invalidation history.

## 9. LRG-05 — Human Decision Governance

### 9.1 Responsibility Boundary

| Machine-assisted functions | Qualified human/lawyer responsibilities |
|---|---|
| Register and structure authorized materials | Approve matter, purpose, access, and professional boundary |
| Compute and compare byte identities | Decide authenticity/admissibility questions and appropriate evidentiary use |
| Produce text/OCR/extraction candidates | Verify source fidelity, corrections, and review scope |
| Link source statements to fact candidates | Decide whether and how a source may support a factual position |
| Propose Legal Fact, issue, rule, element, burden, and evidence mappings | Verify current law, legal relevance, burden, defenses, and competing interpretations |
| Identify missing sources, conflicts, and risks | Decide whether gaps can be accepted, remediated, or require stopping |
| Draft request-right and defense/rebuttal candidates | Select, revise, reject, or defer legal positions |
| Preserve traceability and review records | Give legal advice, choose litigation strategy, approve filings, and apply conclusions |

### 9.2 Human Decision Gate

```text
Machine-Assisted Candidate Package
        ↓
Source and Processing Verification
        ↓
Boundary / Confidentiality Review
        ↓
Current Authority and Legal Analysis Review
        ↓
Qualified Lawyer Decision
        ↓
Approve / Revise / Reject / Defer
        ↓
Optional Authorized Application
```

The gate is a governance control pattern, not a runtime workflow or automatic state machine.

### 9.3 Minimum Decision Package

The lawyer must receive:

- matter and purpose boundary;
- source identities, hashes, access scope, versions, and processing limitations;
- source-verified fact candidates with exact locators;
- Legal Fact transformations and rationales;
- current authority candidates and effective-date verification;
- element, burden, proof, and evidence mappings;
- supporting, adverse, conflicting, missing, and inaccessible material;
- defenses, rebuttals, alternative request rights, and unresolved relationships;
- validation states and stop reasons;
- explicit notice of what the machine did not verify or decide.

### 9.4 Human Decision Invariants

- Silence or failure to review is never approval.
- A source-fidelity reviewer does not automatically approve legal relevance.
- A lawyer's approval is limited to the recorded matter, scope, sources, version, and purpose.
- A material correction or new adverse source reopens the decision.
- Machine-generated language may not obscure that the legal decision belongs to the lawyer.

## 10. Domain Adapter Extension Model

### 10.1 Core and Adapter Separation

```text
LEGAL_REASONING_GOVERNANCE_PATTERN
        ↓ mandatory controls
Domain Adapter
        ↓ domain-specific concepts
Route Profile
        ↓ separately authorized use
Implementation, only if separately approved
```

The governance core defines mandatory controls. A Domain Adapter supplies domain-specific legal concepts without modifying the core.

### 10.2 Domain Adapter Contract

A proposed adapter may define:

- jurisdiction and professional context;
- matter and procedural-posture taxonomy;
- official/approved authority sources and freshness checks;
- domain-specific Legal Issues and rule types;
- request-right, defense, remedy, or legal-position templates;
- element and required-fact templates;
- evidence categories and source-locator conventions;
- burden/proof candidate types;
- domain-specific adverse facts, conflicts, defenses, and rebuttals;
- qualified-review roles and checklists;
- route-specific input/output descriptions.

### 10.3 Adapter Constraints

An adapter must not:

- weaken LRG-00 matter authorization or case isolation;
- accept evidence that fails LRG-01 readiness;
- collapse LRG-02 source, extraction, fact, and Legal Fact layers;
- bypass LRG-03 authority, element, proof, defense, or gap controls;
- introduce validation states outside LRG-04 without a separately approved governance revision;
- replace or automate LRG-05 qualified-human decision;
- create a global methodology that supersedes the approved domain architecture;
- embed case outcomes, obsolete law, or unreviewed model knowledge as permanent rules.

### 10.4 Adapter Conformance Record

Every adapter proposal must map each mandatory LRG control to its domain implementation concept, identify deviations, bind its source authorities and versions, and receive Architecture Review plus Project Owner approval before use.

## 11. Route A / Route B Compatibility

### 11.1 Route-Neutral Extension Slots

This Pattern does not assume what Route A or Route B will do. Each route is an opaque, separately governed profile until its own Handoff defines purpose, scope, inputs, outputs, risks, and authorization.

Stable extension slots:

| Extension slot | Mandatory route declaration |
|---|---|
| Matter profile | Authorized matter types, actors, purposes, and exclusions |
| Evidence profile | Required categories, readiness requirements, source and locator conventions |
| Fact profile | Permitted extraction/normalization, verification roles, and transformation limits |
| Legal reasoning profile | Questions, authority sources, element/proof models, defenses, and stop conditions |
| Validation profile | Application of `SUPPORTED`, `UNKNOWN`, and `BLOCKED` |
| Human decision profile | Reviewer qualifications, decision package, approvals, and prohibited automation |
| Output profile | Candidate artifacts, disclosure labels, retention, and downstream-use boundary |

### 11.2 Shared Route Requirements

Both Route A and Route B must:

- inherit LRG-00 through LRG-05 without weakening them;
- bind case/matter identity and prevent unauthorized cross-matter use;
- consume only analysis-ready evidence for substantive reasoning;
- preserve exact source and authority traceability;
- retain gaps, adverse material, defenses, rebuttals, and unresolved conflicts;
- use only controlled validation states;
- stop when a critical prerequisite is blocked;
- reserve legal judgment, advice, strategy, and application for qualified humans;
- obtain separate design, implementation, and validation authorization.

### 11.3 Compatibility Matrix

| Control | Route A | Route B | May route override? |
|---|---|---|---|
| Matter authorization and case isolation | Mandatory | Mandatory | No |
| Evidence identity and readiness | Mandatory | Mandatory | No |
| Source → extraction → fact → Legal Fact separation | Mandatory | Mandatory | No |
| Current authority and element/proof trace | Mandatory where legal reasoning occurs | Mandatory where legal reasoning occurs | No |
| `SUPPORTED` / `UNKNOWN` / `BLOCKED` | Mandatory | Mandatory | No |
| Human Decision Gate | Mandatory | Mandatory | No |
| Route-specific evidence categories | Adapter-defined | Adapter-defined | Yes, within core controls |
| Route-specific candidate outputs | Adapter-defined | Adapter-defined | Yes, subject to authorization |
| Runtime architecture or provider | Not defined | Not defined | Requires separate approval |

Compatibility does not constitute route authorization.

## 12. Audit, Versioning, and Change Governance

### 12.1 Minimum Audit Chain

```text
Matter Authorization
→ Evidence Receipt and Registration
→ Hash and Access Verification
→ Processing Route and Extraction Version
→ Source Verification and Corrections
→ Legal Fact Transformation
→ Rule / Element / Proof / Evidence Mapping
→ Validation State
→ Qualified Human Decision
→ Optional Authorized Use
→ Revocation / Supersession / Reopening, if any
```

### 12.2 Version Rules

- Source bytes, extraction, fact transformations, authority checks, candidate analysis, and human decisions each have distinct versions.
- A later version never silently rewrites earlier provenance.
- Downstream artifacts record the exact versions used.
- A correction identifies affected dependent artifacts and reopens them where material.
- A canonical pattern, adapter, or route profile requires a separate adoption decision.

### 12.3 Governance Change Classes

| Change | Required governance action |
|---|---|
| Editorial clarification with no semantic change | Documented review according to repository policy |
| State semantics or mandatory gate change | Architecture Review and Project Owner decision |
| New domain adapter | Adapter Handoff, conformance review, and approval |
| New Route A/B profile | Route-specific Handoff and approval |
| Runtime implementation | Separate implementation design, authorization, validation, and deployment controls |
| Relaxation of human decision or input readiness | Prohibited without explicit governance revision and Project Owner approval |

## 13. Failure Modes and Prohibited Shortcuts

| Anti-pattern | Governance response |
|---|---|
| “The file was previously listed, so it is available” | Recheck access and byte identity; otherwise `BLOCKED` |
| “OCR confidence is high, so the content is correct” | Require source-region human verification |
| “Hash matches, so the evidence is authentic/admissible” | Record byte identity only; retain legal review questions |
| “The case label implies the request right” | Require source-backed facts, current authority, elements, and review |
| “Most elements are supported, so success is likely” | Preserve element states and critical blockers; prohibit probability inference |
| “No contrary document was found, so no defense exists” | Record search/access limits and `UNKNOWN`; do not infer nonexistence |
| “A prior matter used this rule, so it is current” | Re-verify official source, effective dates, applicability, and conflicts |
| “The model selected the best route” | Present candidates and relationships; qualified lawyer selects or rejects |
| “Human review occurred somewhere in the workflow” | Require named reviewer, scope, source/version, decision, date, and limitations |
| “Route-specific speed requires bypassing the core gate” | Reject route conformance |

## 14. Pattern Validation Scenarios

| ID | Scenario | Expected governance behavior | Result |
|---|---|---|---|
| P01 | Matter purpose is undefined | LRG-00 blocks before evidence processing | PASS |
| P02 | File path resolves but hash differs | LRG-01 marks mismatch and invalidates dependent analysis | PASS |
| P03 | OCR output is unreviewed | LRG-01/LRG-02 block fact promotion | PASS |
| P04 | Extraction matches source but source statement may be false | Record Source-Verified Fact Candidate only; truth remains unresolved | PASS |
| P05 | Rule text lacks effective-date verification | LRG-03 blocks dependent element/request-right conclusion | PASS |
| P06 | Supporting and adverse sources conflict | Preserve both and reopen validation/human review | PASS |
| P07 | One critical element lacks evidence | Candidate remains `BLOCKED`; no outcome score | PASS |
| P08 | Lawyer approves a limited source scope | Approval applies only to that scope and version | PASS |
| P09 | Route A proposes cross-case reuse | LRG-00/01 require separate authorization; otherwise block | PASS |
| P10 | Route B proposes automated final advice | LRG-05 rejects route conformance | PASS |

## 15. Acceptance Criteria

| ID | Status | Verification |
|---|---|---|
| `GOV-C01-001` — Pattern independent from specific cases | **PASS** | Core controls use matter-neutral identities, gates, candidates, and reviewer roles; no case fact or outcome is embedded |
| `GOV-C01-002` — Covers C02-I to C02-IV | **PASS** | Input/blocked controls, request-right model, material-gap validation, and input-readiness lifecycle are bound and abstracted |
| `GOV-C01-003` — Maintains Evidence–Fact–Law chain | **PASS** | LRG-01 through LRG-03 preserve evidence identity, extraction, source verification, Legal Fact, element/proof, and request-right traceability |
| `GOV-C01-004` — Maintains Human Review Boundary | **PASS** | LRG-05 reserves legal judgment, advice, selection, strategy, and application for qualified humans |
| `GOV-C01-005` — No implementation pollution | **PASS** | Pattern is documentation-only and selects no code, Skill, Agent, Workflow, MCP, OCR, database, RAG, provider, or runtime schema |
| `GOV-C01-006` — Supports Route A/B extension | **PASS** | Route-neutral extension slots and mandatory conformance controls are defined without authorizing or implementing either route |

## 16. Adoption and Current Governance Status

```text
LEGAL_REASONING_GOVERNANCE_PATTERN v1.0 Canonical:
ADOPTED

Pattern Extraction:
DONE — CANONICAL GOVERNANCE ASSET

Acceptance Criteria Check:
6 / 6 PASS

Architecture Pattern Review:
PASS (Grade A)

Project Owner Adoption Decision:
ACCEPTED (SHA: 95199F93877966458A29EFD6ABF6F83459C62AC7D59E5402825FB5B662B2C724)

Canonical Governance Asset:
ADOPTED

Route A / Route B:
NOT AUTHORIZED

Implementation:
NOT AUTHORIZED
```
