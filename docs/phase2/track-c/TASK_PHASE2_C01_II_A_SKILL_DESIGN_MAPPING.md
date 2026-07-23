# TASK_PHASE2_C01-II-A Skill Design Mapping

STATUS: **REVIEW DRAFT — DOCUMENTATION ENGINEERING MAPPING ONLY**

TYPE: Phase 2 Track C — C01-II-A Design Specification

TARGET MODULE: `litigation-legal`

IMPLEMENTATION: **NOT AUTHORIZED**

CODE / SKILL / AGENT / PLUGIN / MCP / WORKFLOW / RUNTIME SCHEMA CHANGES:
**NONE**

## 1. Identity, Provenance and Scope

### 1.1 Governing Handoff

- Path:
  `.codex-coordination/inbox/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING_HANDOFF.md`
- SHA-256:
  `7A7FA9AC41961E12148A655D9941AC58F80CEE08B25C9CB4B0B5BDAE5FC9C733`
- Execution authorization: C01-II-A documentation-only Skill Design Mapping.
- C01-II-B Skill / Agent modification: not authorized.
- Inspection date: 2026-07-18.

The Handoff was copied byte-for-byte from an explicitly approved isolated
workspace source to the canonical repository under separate Project Owner
authorization. The target hash was verified before execution resumed.

### 1.2 Fixed Governance and Design Inputs

| Input | Canonical path | Recomputed SHA-256 / state |
|---|---|---|
| Phase 2 Scope Decision | `.codex-coordination/decisions/DECISION_PHASE2_SCOPE_RECLASSIFICATION.md` | ACCEPTED; `4927BA4E1E8093EE8F09FB8A2B9584FB1DE36A456479D6486E0FC265CA080150` |
| Phase 2 Architecture Decision | `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md` | ACCEPTED; `C5457DAB074CCF3F49C8D8D8A9530FA98366E2581BF9CBBA528261084870833C` |
| C01 v0.2 reviewed baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5` |
| Approved C01-I Specification | `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md` | `0274AB2C7542083BFBDFF98F00E7143F7D45927EEEED5675BF28BF6631A862C7` |
| C01-I Specification Review | `.codex-coordination/reviews/TASK_PHASE2_C01_I_SPEC_REVIEW.md` | PASS and accepted by Decision; `C4EE86A9FB5D37CC4E6CA69E8CECC6C1AC1B47E0012546C6F4F6699B4EC19C98` |
| C01-I Specification Decision | `.codex-coordination/decisions/TASK_PHASE2_C01_I_SPEC_DECISION.md` | ACCEPTED; `113837F4EB4AA3E76020FAAFE6EC08C3DA5C141EF5204D6849CFECE86CA7DF65` |
| Parent C01-II Handoff | `.codex-coordination/inbox/TASK_PHASE2_C01_II_IMPLEMENTATION_HANDOFF.md` | `E50E2151F24852BB7E459591A1E9DA91AEB27D061E2364867BA5738FD866D3E2` |

### 1.3 Scope Rule

This document maps approved legal-methodology concepts to existing assets. It
does not change those assets, create D1-D6, define an executable schema, replace
prompts, or authorize implementation.

The ten concept codes used below are:

| Code | C01 concept |
|---|---|
| M | Matter |
| IQ | Issue / Question |
| C | Claim |
| RR | Request Right |
| EL | Element |
| LF | Legal Fact |
| P | Proof |
| EV | Evidence |
| DR | Defense / Rebuttal |
| HR | Human Review |

Coverage labels are `OWNER CANDIDATE`, `SUPPORTING`, `ADJACENT` and `NONE`.
Concepts omitted from an asset's coverage cell are `NONE` for that asset.

## 2. Existing Architecture Facts

### 2.1 Plugin and Shared Controls

- `litigation-legal/.claude-plugin/plugin.json` identifies the existing China
  litigation plugin as version `1.0.2`.
- `litigation-legal/CLAUDE.md` supplies China-law localization, authority
  freshness, reviewer-note fields and mandatory human confirmation before
  consequential external actions.
- `litigation-legal/.mcp.json` is an existing generated integration boundary. It
  is not changed and is not a C01 contract.
- `litigation-legal/matters/_log.yaml`, `matters/_README.md` and
  `matter-workspace/SKILL.md` provide partial Matter persistence conventions.
  Their documented layouts differ; this Task does not resolve the persistence
  contract.
- `references/china-case-authority.md` requires statutory primacy, authority
  tiers, similarity, distinctions, retrieval dates and freshness warnings.
- `references/us-to-cn-legal-terms.md` prohibits importing US discovery,
  privilege and common-law defaults.
- `claim-chart/references/element-templates.md` is an illustrative source of
  candidate elements and evidence, not current law or an implemented Element
  model.

### 2.2 Asset Classification Count

| Classification | Count | Treatment in C01-II-A |
|---|---:|---|
| Canonical Skills | 18 | Inspect and assign candidate ownership/support roles |
| Compatibility aliases | 4 | Route to canonical replacements; no independent ownership |
| Deprecated Skill | 1 | Preserve redirect; no C01 ownership and no modification |
| Agent | 1 | Procedural-facts-only adjacent role; no legal-methodology ownership |
| **Total** | **24** | Full inventory below |

## 3. M01 — Skill Architecture Mapping

### 3.1 Complete 24-Asset Inventory

For compactness, `skills/...` paths in this table are relative to the
`litigation-legal/` module; their complete repository-relative path is
`litigation-legal/<shown path>`. The Agent row is already shown from the module
root.

| Asset and exact path | Class | Current input and output evidenced by inspection | C01 coverage | Candidate future relationship | Current action |
|---|---|---|---|---|---|
| `skills/brief-section-drafter/SKILL.md` | Canonical | Takes a document type/topic plus reviewed facts, evidence and authority; returns reviewable pleading/arbitration text, evidence correspondence and review points | C, RR, LF, EV, DR, HR — SUPPORTING downstream | Consume only human-approved C01 references; never choose the legal theory | NO CHANGE |
| `skills/chronology/SKILL.md` | Canonical | Takes source materials or matter slug; returns source-bound dated events, parties, evidence IDs, related claims/defenses, proof purposes and gaps | LF — OWNER CANDIDATE; M, IQ, C, P, EV, DR, HR — SUPPORTING | Own candidate Legal Fact/event register and provenance links; never decide Element satisfaction | NO CHANGE |
| `skills/claim-chart/SKILL.md` | Canonical | Takes matter materials/claim summary; returns claim/defense, request-right basis, facts, evidence, three-property review, proof purpose and gaps | C, RR, EL, P, EV, DR — OWNER CANDIDATE; IQ, LF, HR — SUPPORTING | Candidate central analytical mapping owner; ownership is a design recommendation, not implementation | NO CHANGE |
| `skills/cold-start-interview/SKILL.md` | Canonical | Takes user profile/configuration answers; returns `litigation_profile` for forums, evidence sources, preservation and manual gates | M, HR — ADJACENT context | Configure environment-level context only; do not own matter reasoning | NO CHANGE |
| `skills/confidential-evidence-review/SKILL.md` | Canonical | Takes evidence/material packages; returns confidentiality, personal-information, secrecy, redaction and protected-submission recommendations | EV, HR — SUPPORTING specialist | Retain specialist protection ownership; consume reviewed Evidence references only | NO CHANGE |
| `skills/court-order-triage/SKILL.md` | Canonical | Takes court/arbitration/regulatory materials; returns document identity, authority, scope, deadlines, risks and response candidates | M, IQ, LF, EV, HR — ADJACENT | Supply verified procedural candidates to Matter/update flow; no substantive C01 ownership | NO CHANGE |
| `skills/demand-draft/SKILL.md` | Canonical | Takes approved intake; returns a lawyer-reviewable letter/notice draft and send checklist | C, RR, LF, EV, HR — SUPPORTING downstream | Consume approved candidates only; external sending remains separately confirmed | NO CHANGE |
| `skills/demand-intake/SKILL.md` | Canonical | Takes pre-dispute facts; returns parties, facts/evidence, request-right basis, amounts, service, limitation and next-step candidates | M, IQ, C, RR, LF, EV, HR — SUPPORTING upstream | Supply candidates to matter intake; no separate C01 ownership | NO CHANGE |
| `skills/demand-received/SKILL.md` | Canonical | Takes received demands/notices; returns requests, deadlines, fact questions and response options | M, IQ, C, LF, EV, DR, HR — SUPPORTING upstream | Route reviewed disputes into `matter-intake`; preserve opponent position | NO CHANGE |
| `skills/evidence-preservation/SKILL.md` | Canonical | Takes matter/evidence-preservation context; returns retention scope, original-carrier/integrity measures and court/arbitration preservation routes | P, EV, HR — SUPPORTING specialist | Retain evidence-action safeguards; do not own analytical Evidence-to-Element mapping | NO CHANGE |
| `skills/matter-briefing/SKILL.md` | Canonical | Takes matter context; returns procedure, claims/defenses, evidence strength, risk, preservation, settlement and next decisions | M, IQ, C, LF, EV, DR, HR — SUPPORTING presentation | Present reviewed mapping and unresolved gaps without finalizing candidates | NO CHANGE |
| `skills/matter-close/SKILL.md` | Canonical | Takes matter slug and closing materials; returns outcome, costs, residual risks, lessons and ledger-update suggestions | M, LF, HR — ADJACENT lifecycle | Record lifecycle outcome only; no reasoning ownership | NO CHANGE |
| `skills/matter-intake/SKILL.md` | Canonical | Takes new matter/materials; returns procedure, parties, claims/request-right bases, facts, evidence, preservation, service and execution candidates | IQ — OWNER CANDIDATE; M, C, RR, LF, EV, HR — SUPPORTING initializer | Initialize candidates and hand central analysis to `claim-chart`; never make filing decision | NO CHANGE |
| `skills/matter-update/SKILL.md` | Canonical | Takes matter slug/new information; returns event summary, deadline/risk/evidence effects, ledger suggestions and next steps | M, LF, EV, HR — SUPPORTING lifecycle | Generate invalidation/review signals; preserve append-only history | NO CHANGE |
| `skills/matter-workspace/SKILL.md` | Canonical | Takes workspace commands/slug; creates or selects isolated matter context and a narrative/evidence directory layout | M — OWNER CANDIDATE; HR — ADJACENT | Own Matter identity and isolation references; persistence details require later decision | NO CHANGE |
| `skills/oc-status/SKILL.md` | Canonical | Takes matter/portfolio context; returns outside-counsel questions and an unsent email draft | M, IQ, EV, HR — ADJACENT reporting | Supply reviewed counsel status only; no methodology ownership | NO CHANGE |
| `skills/portfolio-status/SKILL.md` | Canonical | Takes portfolio ledger; returns aggregate stage, amount, deadline, preservation, execution and risk views | M, HR — ADJACENT aggregate | Consume reviewed matter status only; never aggregate unreviewed C01 conclusions as fact | NO CHANGE |
| `skills/witness-trial-prep/SKILL.md` | Canonical | Takes person/material context; returns proof subjects, claim/defense links, evidence links, questions and high-risk issues | C, LF, P, EV, DR, HR — SUPPORTING downstream | Consume reviewed Proof/Evidence links; no unsupported fact creation or coaching | NO CHANGE |
| `skills/deposition-prep/SKILL.md` | Compatibility alias | Legacy command duplicates China hearing/witness-prep behavior and points to `witness-trial-prep` | Same routing coverage as canonical target; no ownership | Route to `witness-trial-prep`; do not add C01 fields or independent logic | NO CHANGE |
| `skills/legal-hold/SKILL.md` | Compatibility alias | Legacy command duplicates China evidence-retention/preservation behavior and points to `evidence-preservation` | Same routing coverage as canonical target; no ownership | Route to `evidence-preservation`; no US legal-hold semantics | NO CHANGE |
| `skills/privilege-log-review/SKILL.md` | Compatibility alias | Legacy command duplicates China confidentiality/redaction behavior and points to `confidential-evidence-review` | Same routing coverage as canonical target; no ownership | Route to canonical evidence-confidentiality Skill; no privilege promise | NO CHANGE |
| `skills/subpoena-triage/SKILL.md` | Compatibility alias | Legacy command duplicates China court/investigation-order triage and points to `court-order-triage` | Same routing coverage as canonical target; no ownership | Route to canonical triage Skill; no US subpoena semantics | NO CHANGE |
| `skills/customize/SKILL.md` | Deprecated | Redirects users to `cold-start-interview` and prohibits separate configuration | M, HR — routing only; no ownership | Preserve redirect until separately governed deprecation decision; no C01 mapping fields | NO CHANGE |
| `agents/docket-watcher.md` | Agent | Reads user-provided procedural materials/ledger; returns candidate events and deadlines requiring lawyer/administrator verification; declares `Read` and `Write` tools | M, IQ, LF, HR — ADJACENT | Optional procedural-fact supplier only; any Agent change needs separate express approval | NO CHANGE |

### 3.2 Canonical Concept Ownership Proposal

This is the smallest existing-architecture ownership proposal. It creates no
new Skill, Agent, service or runtime object.

| C01 concept | Primary owner candidate | Initializer / supporting assets | Candidate responsibility boundary | Main overlap resolved by proposal |
|---|---|---|---|---|
| Matter | `matter-workspace` | `matter-intake`, matter ledger/history, `matter-update` | Stable matter identity, isolation and reference context; not legal analysis | Separates workspace ownership from intake analysis |
| Issue / Question | `matter-intake` | `chronology`, `claim-chart`, `court-order-triage` | Create and route candidate legal/procedural questions with source triggers | Intake identifies; central mapping links but does not silently create issues |
| Claim | `claim-chart` | `matter-intake`, `demand-intake`, `demand-received` | Maintain candidate Claim identity, party/procedure/relief links and alternatives | Intake initializes; chart owns continuing analysis |
| Request Right | `claim-chart` | `matter-intake`, `demand-intake`, element templates | Maintain candidate legal basis, authority status, alternatives and Claim relation | Prevents request-right basis from remaining an untraceable text field |
| Element | `claim-chart` | element templates, current authority references | Maintain reviewed Element candidates, authority, required facts and status | Templates seed candidates only; they never satisfy an Element |
| Legal Fact | `chronology` | `claim-chart`, matter history, `matter-update` | Maintain source-bound candidate fact/event records, disputes and adverse markers | Chronology owns facts; chart consumes references rather than duplicating fact text |
| Proof | `claim-chart` | `chronology`, China rules, `witness-trial-prep` | Link Element, fact to prove, burden/proof-rule candidate, Evidence and gap | Witness prep consumes reviewed proof subjects; it does not own burden analysis |
| Evidence | `claim-chart` for analytical index | `evidence-preservation`, `confidential-evidence-review`, chronology | Maintain Evidence-to-fact/Element/proof-purpose links; specialists retain action safeguards | Separates analytical indexing from preservation/confidentiality actions |
| Defense / Rebuttal | `claim-chart` | `matter-intake`, `matter-briefing`, drafting/witness Skills | Maintain opposing position, defense elements, evidence, rebuttal and remaining gap | Presentation/drafting consume reviewed chain rather than generating it |
| Human Review | `litigation-legal/CLAUDE.md` distributed governance | Reviewer-note blocks and consequential-action gates in producing/consuming Skills | Define cross-cutting candidate, provenance and qualified-review requirements | No false single Skill owner and no unapproved D6/runtime state machine |

### 3.3 Ownership Decision Effects

The proposal makes `claim-chart` the central analytical candidate, but not a
global orchestrator. `matter-intake` remains the entry and initializer;
`chronology` remains the fact/provenance owner; specialist evidence Skills retain
their legal safeguards; downstream briefing/drafting/witness Skills remain
consumers. The proposal must be reviewed before any C01-II-B Task can name
implementation paths.

## 4. M02 — Capability Boundary Matrix

| Capability | Current evidence | Classification | Future design direction | Boundary |
|---|---|---|---|---|
| Matter identity and isolation | `matter-workspace`, ledger and matter files | EXISTING / PARTIAL | Stable references between matter context and reviewed analysis | Persistence layout requires decision; no schema now |
| Matter intake and procedural posture | `matter-intake` | EXISTING / PARTIAL | Initialize candidate Questions, Claims, Request Rights, facts and gaps | No automatic filing/procedure decision |
| Source-bound event chronology | `chronology` | EXISTING / PARTIAL | Candidate Legal Fact IDs/classifications and cross-references | No judicial-fact assertion |
| Claim/request/fact/evidence matrix | `claim-chart` | EXISTING / PARTIAL | Candidate central ownership with stable links | No current implementation claim |
| Illustrative Element seeds | `element-templates.md` | EXISTING REFERENCE / PARTIAL | Reviewed, current-authority-linked Element candidates | No hard-coded or self-executing doctrine |
| Evidence three-property review | `claim-chart` and evidence Skills | EXISTING / PARTIAL | Link authenticity, legality, relevance and proof purpose to facts/Elements | No admissibility guarantee |
| Evidence preservation | `evidence-preservation` | EXISTING SPECIALIST | Consume reviewed evidence gaps | Consequential actions require human approval |
| Confidentiality/data safeguards | `confidential-evidence-review` | EXISTING SPECIALIST | Consume reviewed Evidence IDs and risks | No US privilege/disclosure immunity |
| Defense presentation | `claim-chart`, briefing and drafting | EXISTING / PARTIAL | Explicit Defense Element → Evidence → Rebuttal → Gap chain | No automatic strategy or suppression of adverse facts |
| Human review controls | `CLAUDE.md`, reviewer notes, Skill gates | EXISTING / DISTRIBUTED | Harmonized governance fields after separate approval | Not D6 and not a runtime state machine |
| Candidate event/deadline monitoring | `docket-watcher` | EXISTING ADJACENT | Optional verified procedural-reference supply | No legal theory, deadline finalization or calendar action |
| Compatibility routes | four compatibility Skill files | EXISTING ROUTING | Continue routing to canonical Skills | Never independent C01 ownership |
| Deprecated configuration route | `customize` | EXISTING REDIRECT | Preserve until separately approved removal/deprecation plan | No modification in C01-II-A |
| Stable C01 identifiers and cross-links | No complete current carrier | FUTURE ENHANCEMENT | Design in C01-II-B only after path approval | No runtime schema in this document |
| Burden/proof-rule authority linkage | Partial rules and matrices | FUTURE ENHANCEMENT | Current-authority candidate fields and review status | Legal methodology review required |
| Change invalidation/reopen behavior | `matter-update` is append-oriented | FUTURE ENHANCEMENT | Flag reviewed analysis affected by new facts/evidence | No silent recomputation |
| Reviewed downstream consumption | Reviewer gates exist but linkage is informal | FUTURE ENHANCEMENT | Require reviewed mapping references before drafting/presentation | No automatic application |
| Global Legal Reasoning Core | None | EXCLUDED | None | Parallel architecture prohibited |
| New methodology framework/tree | None | EXCLUDED | None | `methodology/` and `legal-reasoning-core/` prohibited |
| Database or knowledge graph | None | EXCLUDED | None | New persistence architecture prohibited |
| Runtime/MCP/workflow schema | Existing unrelated configs only | EXCLUDED | None | No schema or MCP modification |
| External provider integration | Existing placeholders only | EXCLUDED | None | Connector/provider expansion prohibited |
| Automated legal opinion/outcome/strategy | None | EXCLUDED | None | Professional boundary prohibits it |
| D1-D6 generation or substitution | Not generated | EXCLUDED | None in C01-II-A | Remains unauthorized |

## 5. M03 — Input / Output Contract Draft

### 5.1 Contract Status

The following contracts are conceptual Markdown design only. Terms such as
`identifier`, `category` and `status` describe reviewable information, not YAML,
JSON, database, MCP or runtime types. No serialization, API, persistence format
or executable validation rule is defined.

### 5.2 Shared Candidate Envelope

| Information group | Candidate content | Producer obligation | Consumer verification |
|---|---|---|---|
| Matter reference | Stable matter slug/reference, forum, stage, party role | Preserve isolation and source matter | Confirm correct matter and conflict boundary |
| Source reference | File/material, page/message/range, collection/retrieval date | Bind every factual/authority assertion to source | Reject unbound facts or mark source gap |
| Candidate identity | Concept label and local candidate reference | Keep identity stable within reviewed artifact | Do not treat as runtime/global ID |
| Candidate status | Proposed, disputed, adverse, unresolved, reviewed or rejected in prose | Preserve uncertainty and opposing positions | Do not flatten candidate into conclusion |
| Authority reference | Statute/interpretation/case tier, effective/retrieval date, freshness | Use statutory primacy and current verification | Reject stale/unretrieved authority as final basis |
| Review note | Reviewer, scope read, pending issues, decision, conditions and date | Keep human gate explicit | Require qualified decision before consequential use |
| Change notice | New fact/evidence/procedure and potentially affected candidates | Append provenance; do not overwrite history silently | Reopen review when material impact exists |

### 5.3 Conceptual Concept Contracts

| Concept output | Candidate fields | Primary producer | Required verification before use |
|---|---|---|---|
| Matter context | Matter reference, parties, role, procedure, forum, stage, objective, isolation/conflict state | `matter-workspace` with intake support | Correct matter, authorization to read, unresolved objective stated |
| Question register | Question reference/text, procedural/substantive category, source trigger, related claims/defenses, open status | `matter-intake` | Source trigger and lawyer validation; no silent closure |
| Claim register | Candidate relief, parties, procedure, alternatives/cumulative/exclusive relation, source and status | `claim-chart` after intake | User/pleading source, authority candidate and reviewer decision |
| Request Right register | Candidate basis, Claim relation, statutory/interpretive source, effective date, alternatives and uncertainty | `claim-chart` | Current-law verification; illustrative templates cannot be final basis |
| Element register | Candidate Element, parent Request Right, authority, required fact references and review status | `claim-chart` | Qualified legal review; no template-based automatic satisfaction |
| Legal Fact register | Candidate classification, actor/date/event, exact source, disputed/adverse marker and related Element/Claim | `chronology` | Source completeness and distinction from court findings |
| Proof matrix | Element, fact to prove, burden candidate, proof/evaluation-rule candidate, authority, Evidence and gap | `claim-chart` | Current authority, uncertainty and no automated sufficiency conclusion |
| Evidence index | Evidence reference, source/original carrier, authenticity/legality/relevance issues, proof purpose, custody, confidentiality and gap | `claim-chart` with specialist inputs | Source integrity, three-property review and human verification |
| Defense/Rebuttal map | Defense, defense elements, required facts, burden candidate, Evidence, rebuttal, further response and remaining gap | `claim-chart` | Preserve opponent evidence, inconsistent facts and unresolved gaps |
| Human review record | Candidate reference, reviewer, scope, decision, conditions, unresolved issues and date | Distributed producing/consuming assets | Qualified reviewer and consequential-use confirmation |

### 5.4 Cross-Asset Interaction Contracts

| Interaction | Candidate input | Candidate output | Rejection / reopen condition | Boundary |
|---|---|---|---|---|
| `matter-workspace` → `matter-intake` | Matter reference, isolation context, source range | Intake review tied to correct Matter | Cross-matter source, unresolved conflict or missing authority to read | Workspace does no legal analysis |
| `matter-intake` → `chronology` | Candidate Questions/Claims, parties, procedure and source materials | Source-bound event/Legal Fact candidates | Event lacks source or date/actor is materially uncertain | Chronology does not select Claim/Element |
| `matter-intake` + `chronology` → `claim-chart` | Candidate Questions/Claims/Request Rights and Legal Fact/Evidence references | Central candidate analysis matrix | Missing source, unclear party position or unresolved material conflict | Chart remains candidate analysis |
| `claim-chart` → evidence specialists | Reviewed Evidence references, gaps, preservation/confidentiality risks | Safeguard plan/recommendations | Consequential action not approved or data scope excessive | Specialists do not own Element analysis |
| `claim-chart` → `witness-trial-prep` | Reviewed proof subjects, facts, Evidence and Defense links | Reviewable question/preparation plan | Unsupported fact, unreviewed theory or coaching risk | No unsupported answers or facts |
| `claim-chart` → briefing/drafting | Human-reviewed candidate references and unresolved/adverse items | Reviewable summary or draft | Review absent, authority stale or candidate status lost | Consumers cannot choose theory |
| `matter-update` → owners/consumers | New procedure/fact/evidence with provenance and impact | Reopen/invalidation notice | Material change conflicts with reviewed analysis | Append-only; no silent recomputation |
| `docket-watcher` → `matter-update` | User-provided procedural material and ledger context | Candidate event/deadline with basis and `[待复核]` | Authenticity or deadline calculation unverified | Agent has no methodology or action authority |
| compatibility alias → canonical Skill | Legacy command and user material | Route to canonical China-law Skill behavior | Attempt to add alias-only C01 behavior | Alias never owns C01 concept |

## 6. M04 — Human Review Integration Mapping

### 6.1 Governance Control Pattern

```text
Candidate Analysis (AI generated)
        ↓
Qualified Human Review (manual gate)
        ↓
Approval Decision (lawyer confirmed)
        ↓
Optional Application (downstream use)
```

This is a governance control guideline. It is not an implemented runtime state
machine, workflow engine or D6 substitute.

### 6.2 Review Gates by Activity

| Activity | Candidate producer | Minimum review focus | Optional application only after review |
|---|---|---|---|
| Matter setup/intake | workspace and intake Skills | Matter identity, conflict/isolation, forum, limitation, parties, objectives and source range | Initiating further legal analysis |
| Question/Claim/Request Right mapping | intake and `claim-chart` | Party instruction, relief, procedure, current authority, alternatives and adverse positions | Pleading/response theory planning |
| Element/Proof mapping | `claim-chart` | Current-law basis, required facts, burden/proof rule, gaps and contrary authority | Reliance in advocacy or advice |
| Legal Fact mapping | `chronology` | Exact provenance, dispute/adverse status and distinction from judicial findings | Use in chart, briefing or draft |
| Evidence mapping | chart and evidence specialists | Original carrier, authenticity, legality, relevance, confidentiality and preservation | Submission, disclosure or preservation action |
| Defense/Rebuttal mapping | `claim-chart` | Opponent position/evidence, further response, inconsistent facts and residual gap | Litigation strategy or drafting use |
| Procedural event/deadline | triage Skills or `docket-watcher` | Official-source verification, calculation basis and local rule | Formal calendar or procedural action |
| Briefing/drafting | presentation/drafting Skills | Candidate status, current authority, source links, adverse facts and approval scope | External submission, sending or decision |

### 6.3 Human Review Failure Rules

- Missing review does not become implicit approval.
- Review of one concept does not approve all connected concepts.
- New material facts, evidence or authority may reopen a prior decision.
- Rejection or conditions must remain visible to downstream consumers.
- Automated confidence scores cannot replace disclosed reasoning and review.
- Filing, sending, preservation execution, calendar entry, settlement and other
  consequential actions require their existing separate confirmation gates.

## 7. M05 — Implementation Boundary Report

### 7.1 Candidate C01-II-B Change Points — Not Authorized

| Exact existing path | Smallest future change candidate | Dependency / decision | C01-II-A status |
|---|---|---|---|
| `litigation-legal/skills/matter-workspace/SKILL.md` | Carry an approved Matter analysis reference without embedding a runtime schema | Resolve workspace vs `matters/_README.md` persistence convention | NOT PERFORMED |
| `litigation-legal/skills/matter-intake/SKILL.md` | Produce approved candidate Question/Claim/Request Right handoff fields | Confirm initializer vs owner boundary | NOT PERFORMED |
| `litigation-legal/skills/chronology/SKILL.md` | Produce approved Legal Fact candidate references and disputed/adverse markers | Approve fact classifications and provenance contract | NOT PERFORMED |
| `litigation-legal/skills/claim-chart/SKILL.md` | Carry the approved central Claim/Request Right/Element/Proof/Evidence/Defense mapping | Path-specific implementation approval and methodology review | NOT PERFORMED |
| `litigation-legal/skills/claim-chart/references/element-templates.md` | Add separately approved governance/freshness metadata only | Current-authority ownership and anti-hard-coding controls | NOT PERFORMED |
| `litigation-legal/skills/matter-update/SKILL.md` | Emit approved reopen/invalidation notice | Append-only history and persistence decision | NOT PERFORMED |
| `litigation-legal/skills/matter-briefing/SKILL.md` | Preserve candidate/review/adverse/gap status in summaries | Downstream-consumer approval | NOT PERFORMED |
| `litigation-legal/skills/brief-section-drafter/SKILL.md` | Require approved analysis references before drafting | High-risk advocacy review | NOT PERFORMED |
| Evidence-related canonical Skills | Accept reviewed Evidence references and gaps while retaining specialist scope | Data, action and professional review | NOT PERFORMED |
| `litigation-legal/skills/witness-trial-prep/SKILL.md` | Consume approved Proof/Evidence references | Hearing-preparation review | NOT PERFORMED |
| `litigation-legal/agents/docket-watcher.md` | Optionally emit procedural candidate references only | Separate Agent/tool-scope authorization | NOT PERFORMED |
| `litigation-legal/CLAUDE.md` | Align distributed gates only if separately approved | Broad system-behavior and D6 boundary review | NOT PERFORMED |

Compatibility aliases and `customize` are deliberately absent from the change
candidate table. They remain routing/redirect assets and receive no independent
C01 enhancement.

### 7.2 Must Remain Unchanged

Under C01-II-A:

- all files under `litigation-legal/`;
- all 23 Skill definitions and the one Agent definition;
- plugin/Marketplace metadata, `.mcp.json`, connectors and generated configs;
- matter workspace, ledger and history data;
- workflow, runtime, scripts, hooks, tests and schemas;
- C01 design baselines, C01-I artifacts and Phase 2 architecture/scope/roadmap;
- China-law references and illustrative element templates.

### 7.3 Requires Separate Architecture or Project Owner Decision

- the exact C01-II-B file set and allowed line-level behavior changes;
- the canonical persistence location for candidate references;
- any runtime object, serialization, database or knowledge graph;
- any new Skill, Agent, orchestrator or cross-plugin service;
- any Agent tool or behavior change;
- any change to distributed Human Review controls or future D6 relationship;
- any compatibility alias removal or deprecated Skill deletion;
- implementation validation scope and regression cases.

### 7.4 Out of Scope

- Global Legal Reasoning Core or parallel methodology framework;
- D1-D6 creation, substitution or implementation;
- automated legal opinion, outcome prediction, claim selection or strategy;
- MCP/provider/connector expansion;
- external actions, filing, sending, calendar operations or preservation
  execution;
- code, Skill, Agent, Plugin, Workflow or Runtime Schema modification;
- commit, tag, push or release activity.

## 8. Risk Register

| Risk | Trigger | Impact | Design control / later gate |
|---|---|---|---|
| Central-owner overreach | `claim-chart` becomes an implicit orchestrator | High | Keep intake/fact/specialist/consumer boundaries explicit |
| Methodology drift | Existing tables are mistaken for complete C01 implementation | High | Bind future changes to approved design and path-specific review |
| Duplicate facts | Chronology and chart copy fact text independently | High | Chronology candidate ownership; chart consumes references |
| Persistence/schema creep | Stable references become YAML/database design | Critical | Markdown-only contract; architecture decision required |
| Stale doctrine | Element templates are treated as current law | Critical | Candidate-only templates plus current-authority verification |
| Adverse-fact suppression | Client-oriented output hides opponent evidence | Critical | Mandatory disputed/adverse markers and Defense/Rebuttal chain |
| Candidate flattening | Briefing/drafting presents candidates as conclusions | Critical | Human-reviewed references and unresolved-gap preservation |
| Cross-matter leakage | Workspace/matter sources are mixed | Critical | Matter isolation and conflict/source checks |
| Agent overreach | `docket-watcher` tool grant is read as legal authority | Critical | Procedural-facts-only boundary and separate Agent approval |
| Compatibility divergence | Alias gains C01 behavior separate from canonical Skill | High | Routing-only rule and no alias change point |
| Review state-machine invention | Governance pattern is implemented without D6 | High | Explicitly non-runtime M04 and separate decision gate |
| Case-authority misuse | Cases are treated as binding/current without retrieval | High | Statutory primacy, tier, similarity, distinctions and freshness |

## 9. Proposed Acceptance Criteria for a Future C01-II-B Task

These are design recommendations only; they do not authorize C01-II-B.

1. **Exact path authorization:** every modified file is named in an approved
   Task; no wildcard Skill or Agent authorization.
2. **Owner-bound behavior:** Matter, Issue, Claim/Request Right, Element,
   Legal Fact, Proof/Evidence, Defense/Rebuttal and Human Review responsibilities
   match Section 3.2.
3. **No executable schema by implication:** any serialization/runtime contract
   requires its own architecture approval.
4. **Candidate and provenance preservation:** every generated analytical item
   retains source, uncertainty, adverse/disputed status and review state.
5. **China-law authority control:** current statutes/interpretations remain
   primary; cases have tier, similarity, distinction and freshness metadata.
6. **Compatibility safety:** aliases route to canonical Skills and receive no
   divergent C01 logic; deprecated `customize` remains untouched unless
   separately authorized.
7. **Professional gate:** no external or consequential use without qualified
   human approval; M04 is not represented as a runtime state machine.
8. **Regression and isolation:** approved validation covers cross-matter
   leakage, adverse facts, stale authority, evidence gaps and Agent overreach.
9. **Zero unauthorized changes:** complete diff, staging, `git diff --check` and
   exact-path audits pass.

## 10. Open Decisions

| Decision | Recommended default | Required authority before implementation |
|---|---|---|
| Matter persistence contract | Preserve current files; add no C01 persistence until layouts are reconciled | Project Owner / architecture decision |
| Central analysis owner | `claim-chart`, with `matter-intake` initializer and `chronology` fact owner | C01-II-A review and Project Owner decision |
| Request Right / Claim identity | Separate candidate concepts linked in analysis, without runtime serialization | Legal-methodology and architecture review |
| Element authority maintenance | Templates are seeds; current authority and reviewer determine candidates | Legal-methodology review |
| Evidence ownership | Chart owns analytical link; specialist Skills own safeguards/actions | C01-II-A review |
| Human Review ownership | Distributed `CLAUDE.md`/Skill governance, not a new component | System-alignment and future D6 decision |
| Agent role | Adjacent procedural candidate supplier only | Separate Agent authorization |
| C01-II-B change set | Start with the smallest Skill-only paths after decisions above | Separate Implementation Task and Project Owner approval |

## 11. Current State and Next Step

```text
Phase 2 Track C — TASK_PHASE2_C01

C01 Design Baseline: APPROVED
C01-I: APPROVED AND CLOSED
C01-II Parent Handoff: APPROVED
C01-II-A Skill Design Mapping: GENERATED — PENDING ARCHITECTURE REVIEW
C01-II-B Skill / Agent Modification: NOT AUTHORIZED
C01-II-C Validation: NOT AUTHORIZED
D1-D6: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
```

Next step: Architecture Coordinator reviews this exact artifact and its Result.
Project Owner decides whether to accept the ownership and interaction proposal.
No C01-II-B Task or implementation change may proceed before that decision.
