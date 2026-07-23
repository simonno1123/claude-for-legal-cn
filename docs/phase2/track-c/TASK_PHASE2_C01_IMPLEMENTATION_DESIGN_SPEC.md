# TASK_PHASE2_C01 Implementation Design Specification

STATUS: **REVIEW DRAFT — C01-I DESIGN ONLY**

TYPE: Phase 2 Track C — Design → Engineering Mapping

TARGET MODULE: `litigation-legal`

IMPLEMENTATION: **NOT AUTHORIZED**

CODE / SKILL / AGENT / PLUGIN / MCP / WORKFLOW / RUNTIME SCHEMA CHANGES:
**NONE**

## 1. Identity and Provenance

### 1.1 Authorization

This specification was produced under the explicit Project Owner authorization
issued on 2026-07-18:

```text
Project Owner APPROVED — TASK_PHASE2_C01_I_IMPLEMENTATION_DESIGN

Approved task SHA-256:
8728B6737C7E86F6BE7CE4CE42FC5C3B3A61C9F5DF6CA36CF3EEC84EA451F5C0

Authorized action:
Execute C01-I read-only inventory and engineering mapping.

Sole authorized output:
docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md

Implementation and D1-D6:
NOT AUTHORIZED
```

### 1.2 Fixed Input Identity

| Input | Canonical path | Verified SHA-256 / state |
|---|---|---|
| C01-I approved Task | `.codex-coordination/inbox/TASK_PHASE2_C01_I_IMPLEMENTATION_DESIGN.md` | `8728B6737C7E86F6BE7CE4CE42FC5C3B3A61C9F5DF6CA36CF3EEC84EA451F5C0` |
| C01 v0.2 reviewed baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5` |
| C01 v0.3 formalized design | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.3.md` | `EEB69963715A6A52F37DFF4151DEE8CB0AA314B04E8C936E3CD4866B0ECAD857` |
| C01 Design Revision Result | `.codex-coordination/outbox/TASK_PHASE2_C01_DESIGN_REVISION_RESULT.md` | `F0F275B87D81BBEE99E2AA6F91078B2C523B7D161BA3FFE2E575795397B2F564` |
| Phase 2 Architecture Decision | `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md` | ACCEPTED; SHA-256 `C5457DAB074CCF3F49C8D8D8A9530FA98366E2581BF9CBBA528261084870833C` |

Inspection date: 2026-07-18.

Current plugin identity:

- name: `litigation-legal`;
- version: `1.0.2`;
- architecture: one China-localized domain plugin with 23 Skills, one Agent,
  matter workspace files and shared China-law references;
- implementation authorization: none.

### 1.3 Paths Inspected

Governance and design inputs:

- `AGENTS.md`;
- `.codex-coordination/inbox/TASK_PHASE2_C01_I_IMPLEMENTATION_DESIGN.md`;
- `.codex-coordination/decisions/TASK_PHASE2_000_ARCHITECTURE_ALIGNMENT_ACCEPTANCE_RETRY_1_DECISION.md`;
- `.codex-coordination/outbox/TASK_PHASE2_C01_DESIGN_REVISION_RESULT.md`;
- `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md`;
- `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.3.md`.

Plugin identity, integration and working-context assets:

- `litigation-legal/.claude-plugin/plugin.json`;
- `litigation-legal/.mcp.json`;
- `litigation-legal/README.md`;
- `litigation-legal/CLAUDE.md`;
- `litigation-legal/agents/docket-watcher.md`;
- `litigation-legal/inbound/_README.md`;
- `litigation-legal/demand-letters/_README.md`;
- `litigation-legal/oc-status/_README.md`;
- `litigation-legal/matters/_README.md`;
- `litigation-legal/matters/_log.yaml`.

Plugin legal references:

- `litigation-legal/references/china-litigation-core-rules.md`;
- `litigation-legal/references/test-cases-cn.md`;
- `litigation-legal/skills/claim-chart/references/element-templates.md`.

Repository-level legal references:

- `references/china-case-authority.md`;
- `references/case-authority-sources.json`;
- `references/us-to-cn-legal-terms.md`.

Skill definitions:

- `litigation-legal/skills/brief-section-drafter/SKILL.md`;
- `litigation-legal/skills/chronology/SKILL.md`;
- `litigation-legal/skills/claim-chart/SKILL.md`;
- `litigation-legal/skills/cold-start-interview/SKILL.md`;
- `litigation-legal/skills/confidential-evidence-review/SKILL.md`;
- `litigation-legal/skills/court-order-triage/SKILL.md`;
- `litigation-legal/skills/customize/SKILL.md`;
- `litigation-legal/skills/demand-draft/SKILL.md`;
- `litigation-legal/skills/demand-intake/SKILL.md`;
- `litigation-legal/skills/demand-received/SKILL.md`;
- `litigation-legal/skills/deposition-prep/SKILL.md`;
- `litigation-legal/skills/evidence-preservation/SKILL.md`;
- `litigation-legal/skills/legal-hold/SKILL.md`;
- `litigation-legal/skills/matter-briefing/SKILL.md`;
- `litigation-legal/skills/matter-close/SKILL.md`;
- `litigation-legal/skills/matter-intake/SKILL.md`;
- `litigation-legal/skills/matter-update/SKILL.md`;
- `litigation-legal/skills/matter-workspace/SKILL.md`;
- `litigation-legal/skills/oc-status/SKILL.md`;
- `litigation-legal/skills/portfolio-status/SKILL.md`;
- `litigation-legal/skills/privilege-log-review/SKILL.md`;
- `litigation-legal/skills/subpoena-triage/SKILL.md`;
- `litigation-legal/skills/witness-trial-prep/SKILL.md`.

No inspected path was modified.

## 2. Existing Architecture Inventory

### 2.1 Plugin, Workspace and Reference Layers

| Asset | Current behavior evidenced by inspection | Classification for C01 |
|---|---|---|
| `litigation-legal/.claude-plugin/plugin.json` | Declares plugin `litigation-legal` v1.0.2 for China civil/commercial litigation, arbitration, labor disputes, evidence, chronology and drafting | Canonical identity; MUST REMAIN UNCHANGED |
| `litigation-legal/CLAUDE.md` | Defines China-law system alignment, review-note fields, current-authority checks and mandatory human confirmation before consequential actions | Existing distributed Human Review control |
| `litigation-legal/.mcp.json` | Generated configuration for `legal-data` plus placeholder document, court-docket and arbitration connectors | Existing read-only integration boundary; not a C01 schema or change point under this Task |
| `litigation-legal/matters/_log.yaml` | Ledger for identity, role, forum, status, deadlines, preservation, risk and enforcement | Partial Matter/procedural context; no C01 Question/Claim/Element graph |
| `litigation-legal/matters/_README.md` | Defines `_log.yaml`, narrative `matter.md` and append-only `history.md` ownership | Existing persistence convention; partial C01 carrier |
| `matter-workspace` template | Adds matter summary, parties, procedure, stage, claims/defenses, evidence and preservation directories | Partial Matter carrier; differs from the narrower layout documented in `matters/_README.md` |
| `inbound/_README.md` | Routes incoming letters and procedural documents into triage and matter intake | Optional upstream entry; currently references compatibility command `subpoena-triage` |
| `demand-letters/_README.md` | Routes demand intake/drafting and escalation to `matter-intake` | Optional pre-dispute entry |
| `oc-status/_README.md` | Persists outside-counsel follow-up drafts and describes optional Gmail/scheduling behavior | Adjacent reporting layer; external actions are outside C01 |
| `china-litigation-core-rules.md` | Defines procedure, evidence authenticity/legality/relevance, investigation orders, preservation, hearing, confidentiality and enforcement | Canonical China-law rule reference; dynamic rules still require current verification |
| `element-templates.md` | Provides illustrative claim/defense elements and common evidence for six dispute patterns | Partial Element reference only; not a current Element model or permanent doctrine |
| `test-cases-cn.md` | Contains ten high-pressure China litigation/arbitration regression scenarios | Existing validation seed; not the future D5 artifact |
| `china-case-authority.md` and source JSON | Define authority tiers, freshness and mandatory similarity/distinction/provenance fields | Required authority/provenance boundary |
| `us-to-cn-legal-terms.md` | Prohibits importing US discovery, privilege and common-law defaults | Mandatory localization boundary |

Observed workspace inconsistency: `matter-workspace` describes subdirectories for
evidence, pleadings, preservation, hearing and enforcement, while
`matters/_README.md` documents only `matter.md` and `history.md`. C01-I does not
resolve or modify that inconsistency; future persistence ownership is
`REQUIRES DECISION`.

### 2.2 Skill Inventory

| Skill path | Type | Current purpose | C01 relationship |
|---|---|---|---|
| `skills/brief-section-drafter/SKILL.md` | Canonical | Drafts lawyer-reviewable pleading/brief sections with facts, evidence and authority markers | Downstream consumer of reviewed mappings; must not select claims |
| `skills/chronology/SKILL.md` | Canonical | Source-bound event timeline linked to claims, defenses, issues and proof purposes | Partial Legal Fact carrier |
| `skills/claim-chart/SKILL.md` | Canonical | Maps claims/defenses, legal basis, facts, evidence, proof purpose and gaps | Strongest current C01 mapping candidate; still lacks the full C01 chain |
| `skills/cold-start-interview/SKILL.md` | Canonical | Creates litigation profile for forums, matter types, evidence, preservation and review gates | Context configuration; not matter reasoning |
| `skills/confidential-evidence-review/SKILL.md` | Canonical | Reviews secrecy, personal information and protected submission measures | Specialized Evidence safeguard |
| `skills/court-order-triage/SKILL.md` | Canonical | Triages court, investigation-order, arbitration and regulatory documents | Procedural input; not methodology owner |
| `skills/customize/SKILL.md` | Deprecated | Redirects to `cold-start-interview` | Not a C01 change point |
| `skills/demand-draft/SKILL.md` | Canonical | Drafts demand/notice letters with human confirmation | Optional downstream consumer |
| `skills/demand-intake/SKILL.md` | Canonical | Collects facts, request-right basis, amount, evidence, service and limitation data | Optional pre-dispute input |
| `skills/demand-received/SKILL.md` | Canonical | Triages received demands/notices and escalates to matter intake | Optional upstream input |
| `skills/deposition-prep/SKILL.md` | Compatibility | Maps legacy name to China hearing/witness preparation | Not a canonical C01 owner |
| `skills/evidence-preservation/SKILL.md` | Canonical | Evidence retention, electronic-data integrity and preservation route | Specialized Evidence action planning; consequential steps require review |
| `skills/legal-hold/SKILL.md` | Compatibility | Maps legacy name to evidence preservation | Not a canonical C01 owner |
| `skills/matter-briefing/SKILL.md` | Canonical | Summarizes posture, claims/defenses, evidence, risks and next decisions | Downstream presentation candidate |
| `skills/matter-close/SKILL.md` | Canonical | Closes matters and records results, costs and residual risks | Lifecycle endpoint; not core reasoning owner |
| `skills/matter-intake/SKILL.md` | Canonical | Reviews procedure, parties, claims, basis, evidence, preservation and enforceability | Primary intake and candidate-chain initializer |
| `skills/matter-update/SKILL.md` | Canonical | Appends procedural, evidence, risk and counsel changes to matter records | Adjacent incremental-update carrier |
| `skills/matter-workspace/SKILL.md` | Canonical | Creates and isolates matter context and directories | Matter identity/context carrier |
| `skills/oc-status/SKILL.md` | Canonical | Generates outside-counsel follow-up drafts | Optional review/provenance input; not methodology owner |
| `skills/portfolio-status/SKILL.md` | Canonical | Aggregates matter stages, amounts, deadlines, preservation and enforcement | Portfolio rollup; not matter-level reasoning owner |
| `skills/privilege-log-review/SKILL.md` | Compatibility | Maps legacy name to China evidence-confidentiality review | Not a canonical C01 owner |
| `skills/subpoena-triage/SKILL.md` | Compatibility | Maps legacy name to court/investigation-order triage | Not a canonical C01 owner |
| `skills/witness-trial-prep/SKILL.md` | Canonical | Links proof subjects, claims/defenses, evidence and hearing questions | Optional downstream Proof/Evidence consumer |

Classification totals:

- canonical Skills: 18;
- compatibility aliases: 4 (`deposition-prep`, `legal-hold`,
  `privilege-log-review`, `subpoena-triage`);
- deprecated Skills: 1 (`customize`).

Compatibility aliases must remain routing shims. C01 design must reference their
canonical replacements and must not give aliases independent methodology
ownership.

### 2.3 Agent Inventory

| Agent | Current tools and behavior | C01 classification |
|---|---|---|
| `agents/docket-watcher.md` | `Read`, `Write`; reads user-provided court/arbitration materials and ledger data, extracts procedural events and candidate deadlines, requires lawyer/administrator verification, does not submit to calendars | ADJACENT. It may supply procedural facts and candidate deadlines only. It must not infer Claim, Element, burden, outcome or strategy. Tool grants are not C01 authorization. |

There is no existing C01 reasoning Agent and no authorization to create one.
Whether any future Agent is needed is `REQUIRES DECISION`.

### 2.4 Existing Human-Review and Authority Controls

Current controls include:

- mandatory reviewer-note blocks containing source, read scope, unresolved
  items and human-confirmation gates;
- `matter-intake` candidate outcomes rather than an automatic filing decision;
- `brief-section-drafter` markers for unverified law, evidence and lawyer
  review;
- `docket-watcher` candidate deadlines requiring human verification;
- case-authority tiers, retrieval dates, similarity, distinctions and warnings;
- prohibition on treating China cases as common-law precedent;
- prohibition on US-style privilege/discovery assumptions.

These controls are real but distributed. A single formal C01 Human Review Gate
does not yet exist because D6 has not been created.

## 3. C01 Concept-to-Asset Mapping Matrix

Each methodology concept appears exactly once in this primary matrix.

| C01 concept | Existing asset | Current evidence | Coverage | Future change point | Future change type | Authorization required | Current action |
|---|---|---|---|---|---|---|---|
| Matter | `matter-workspace/SKILL.md`, `matter-intake/SKILL.md`, `matters/_log.yaml`, `matters/[slug]/matter.md` convention | Slug, parties, procedure, forum, stage, summary, claims/defenses, evidence and preservation fields exist; client position/objective and stable C01 links are not complete | PARTIAL | Existing matter context and intake assets | Workspace field and prompt/interface mapping | Approved D1, D2 and D6 plus separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Issue / Question | `matter-intake/SKILL.md`, `chronology/SKILL.md`, `matter-briefing/SKILL.md` | Procedure, jurisdiction, limitation, dispute focus and risks are discussed, but separately identified Question records and traceable IDs are absent | PARTIAL | `matter-intake` initialization and `claim-chart` analysis | Prompt and interaction mapping | Approved D1, D2 and D6 plus separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Claim | `matter-intake/SKILL.md`, `claim-chart/SKILL.md` | Claims/defenses, legal basis, amounts, key facts, evidence and gaps are tabulated; candidate status and full party/procedural linkage are incomplete | PARTIAL | `matter-intake` and `claim-chart` | Prompt, interaction and validation mapping | Approved D1, D2, D3 and D6 plus separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Request Right | `matter-intake/SKILL.md`, `claim-chart/SKILL.md`, `claim-chart/references/element-templates.md` | `请求权基础` is captured and templates group common requests, but Request Right is not a separate traceable object tied to alternatives and authority status | PARTIAL | Primarily `claim-chart`; ownership relative to `matter-intake` requires decision | Prompt/interface and documentation mapping | Approved D1-D3 and D6, ownership decision, and separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Element | `claim-chart/references/element-templates.md`, `claim-chart/SKILL.md` | Templates list claim/defense elements and evidence, but the current `claim-chart` output has no Element ID, authority, burden, proof rule or review status | PARTIAL | `claim-chart` and its reference layer | Prompt, reference-governance and validation mapping | Approved D1-D3, D5-D6 and separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Legal Fact | `chronology/SKILL.md`, `claim-chart/SKILL.md`, matter narrative/history conventions | Events are source-bound and linked to claims/defenses/proof purposes, but Case/Event/Element/Material Fact classifications and stable links are absent | PARTIAL | `chronology`, `claim-chart`, matter history conventions | Prompt, interaction and workspace-field mapping | Approved D1-D3 and D6 plus persistence decision and separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Proof | `claim-chart/SKILL.md`, `china-litigation-core-rules.md`, `witness-trial-prep/SKILL.md` | Facts, evidence, proof purpose, authenticity/legality/relevance and hearing proof subjects exist; burden allocation and proof-standard linkage are not systematic | PARTIAL | `claim-chart` with optional downstream `witness-trial-prep` | Prompt, authority, interaction and validation mapping | Approved D1, D3, D5-D6 plus separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Evidence | `claim-chart/SKILL.md`, `evidence-preservation/SKILL.md`, `confidential-evidence-review/SKILL.md`, chronology and matter evidence conventions | Evidence IDs, sources, proof purpose, authenticity/legality/relevance, gaps, preservation and confidentiality controls exist; end-to-end Element/burden linkage is incomplete | PARTIAL | `claim-chart` as index; specialized evidence Skills retain their current scope | Interaction and validation mapping | Approved D1, D3, D5-D6 plus separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Defense / Rebuttal | `claim-chart/SKILL.md`, `matter-briefing/SKILL.md`, `brief-section-drafter/SKILL.md`, element templates | Claims and defenses are co-listed, opponent evidence positions and common defenses exist; no separate Defense Element → Evidence → Rebuttal → Remaining Gap chain exists | PARTIAL | `claim-chart` as analysis candidate; briefing/drafting as consumers | Prompt, interaction and validation mapping | Approved D1, D4-D6 plus ownership decision and separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff | NO CHANGE — DESIGN ONLY |
| Human Review | `litigation-legal/CLAUDE.md`, reviewer-note patterns across core Skills, `docket-watcher.md` | Consequential actions, unverified law/evidence and candidate deadlines require human confirmation; review rules are distributed rather than a single D6 artifact | EXISTS | Existing distributed gates; any consolidation requires future D6 approval | Documentation, prompt and validation mapping | Approved D6 and separate `TASK_PHASE2_C01_IMPLEMENTATION` Handoff; Agent changes require separate approval | NO CHANGE — DESIGN ONLY |

Conclusion: no C01 concept is fully implemented as the complete v0.3 model.
Existing assets provide substantial partial coverage and a distributed Human
Review control, but they do not yet form a stable end-to-end C01 contract.

## 4. Existing Workflow Interaction Map

### 4.1 In-Domain Flow

```text
matter-workspace
  creates and isolates Matter context
        ↓
matter-intake
  captures posture, parties, candidate claims/bases, facts, evidence and gaps
        ↓
chronology
  organizes source-bound events and disputed facts
        ↘
         claim-chart
          maps claims/defenses, legal basis, facts, evidence and gaps
        ↓
matter-briefing / brief-section-drafter
  present or draft only from reviewed analysis
        ↓
qualified human review
  confirms law, evidence, claims, actions and external use
```

This is a future interaction hypothesis over existing assets, not a current
orchestrated workflow. No global orchestrator, new methodology layer or new
plugin is proposed.

### 4.2 Interaction Classification

| Asset | Classification | Permitted future relationship to C01 | Boundary |
|---|---|---|---|
| `matter-workspace` | CORE CONTEXT | Carry Matter identity and isolation | Must not perform legal analysis |
| `matter-intake` | CORE ENTRY | Initialize candidate Questions, Claims/Request Rights, facts and evidence | Must not select a final claim or filing path |
| `chronology` | CORE FACT SUPPORT | Supply source-bound events and future fact classifications | Must preserve sources, disputes and adverse facts |
| `claim-chart` | CORE ANALYSIS CANDIDATE | Potentially carry the central claim/element/proof/defense mapping | Ownership remains REQUIRES DECISION |
| `matter-briefing` | CORE PRESENTATION | Summarize reviewed mapping and unresolved risk | Must not convert candidates into conclusions |
| `brief-section-drafter` | ADJACENT DOWNSTREAM | Draft from human-approved claims/facts/evidence | Must not create or choose the underlying theory |
| `matter-update` | ADJACENT LIFECYCLE | Append new procedural/fact/evidence changes | Must not silently rewrite prior analysis/history |
| `evidence-preservation` | ADJACENT SPECIALIST | Consume reviewed evidence gaps and preservation needs | Consequential actions require separate human approval |
| `confidential-evidence-review` | ADJACENT SPECIALIST | Apply confidentiality and data-protection controls | No privilege or non-disclosure guarantee |
| `witness-trial-prep` | OPTIONAL DOWNSTREAM | Use reviewed proof subjects and evidence links | No witness coaching or unsupported fact creation |
| `docket-watcher` | ADJACENT AGENT | Supply procedural documents/events and candidate deadlines | No legal-methodology inference; no calendar submission |
| demand and inbound Skills | OPTIONAL UPSTREAM | Supply pre-dispute facts, requests, notices and evidence | Must enter C01 only through a separate reviewed matter context |
| portfolio and outside-counsel Skills | OPTIONAL REPORTING | Supply portfolio/counsel status and reviewed updates | Not owners of matter-level methodology |
| compatibility aliases | INCOMPATIBLE AS OWNERS | Route to canonical China-law Skills only | No independent C01 behavior |

## 5. Conceptual Input Interface

This section is a non-executable Markdown design. It is not YAML, JSON Schema,
MCP schema, workflow schema or runtime contract.

| Input group | Candidate fields / content | Provenance and validity requirements | Current asset anchor | C01 boundary |
|---|---|---|---|---|
| Matter context | Matter identifier, dispute type, parties, procedural posture, forum, client position, objective | Source matter file/ledger, inspection timestamp, conflict/isolation status | `matter-workspace`, `matter-intake`, `_log.yaml` | Missing client position/objective must remain explicit |
| Issue / Question candidates | Question identifier, text, category, related procedure/substance, status | Source facts or legal trigger; reviewer and unresolved status | `matter-intake`, `chronology` | No automatic issue finalization |
| Claim candidates | Claim identifier, requested relief, claimant/respondent, procedural vehicle, candidate status | User instruction, pleading/notice or lawyer-created candidate; source and reviewer | `matter-intake`, `claim-chart` | Alternative, cumulative and mutually exclusive candidates must remain visible |
| Request Right candidates | Basis identifier, authority candidate, relationship to Claim, alternatives | Current statute/interpretation source, effective date, retrieval date and verification status | `claim-chart`, element templates | Templates are illustrative and cannot become permanent doctrine |
| Element candidates | Element identifier, text, parent Request Right, authority, required facts | Current-authority citation and human verification | Element templates, `claim-chart` | No Element is satisfied merely because a template exists |
| Fact inputs | Fact identifier, Case/Event/Element/Material classification candidate, actor, date, assertion/source, adverse/disputed marker | Exact file/page/message/source, collection date, completeness and dispute status | `chronology`, matter history, `claim-chart` | Candidate Material Facts must not be presented as Judicial Facts |
| Proof inputs | Burden candidate, proof/evaluation rule candidate, authority/date, fact to prove | Current statute/judicial interpretation/evidence rule; pending markers where uncertain | `china-litigation-core-rules.md`, `claim-chart` | Burdens and standards cannot be inferred solely from examples |
| Evidence inputs | Evidence ID, name, source, original/derivative status, authenticity, legality, relevance, proof purpose, custody, confidentiality | Source and chain information, original carrier, collection method, review date | `claim-chart`, `chronology`, evidence Skills | Evidence strength and admissibility remain reviewable candidates |
| Defense / Rebuttal inputs | Defense ID, defense elements, required facts, burden candidate, evidence, rebuttal, remaining gap | Party position, source, adverse facts, authority/date and reviewer | `claim-chart`, briefing, element templates | Must preserve inconsistent evidence and further response paths |
| Authority inputs | Statute/interpretation/case reference, authority tier, issuer/court, date, source, retrieval date, freshness | Follow case-authority tier, similarity, distinction and usability rules | `legal-data` boundary and repository references | Cases calibrate reasoning and do not replace statutes/interpretations |
| Uncertainty and review | Missing fields, confidence basis, unresolved conflict, review status, reviewer, decision, timestamp | Every change must retain audit provenance | Distributed reviewer-note patterns | No consequential output before qualified human confirmation |

## 6. Conceptual Output Interface

All outputs below are candidate analytical structures. None is a legal opinion,
adjudication prediction, automatic claim selection or litigation strategy.

| Output | Required candidate content | Provenance / review controls | Possible existing consumer |
|---|---|---|---|
| Matter analysis index | Matter identity, posture, client position, objective, source range, unresolved context | Matter isolation and reviewer status | matter files, `matter-briefing` |
| Question register | Question IDs, text, related Claims/Defenses, facts, authority and open status | Source trigger and human validation | `matter-intake`, `claim-chart` |
| Claim / Request Right register | Candidate relief, basis, alternatives/cumulative/exclusive relations, parties and procedure | Authority/date, source and reviewer decision | `claim-chart`, `matter-briefing` |
| Element / Proof matrix | Element, required facts, burden candidate, proof rule, evidence, gap and human status | Current-authority verification and no automatic satisfaction | `claim-chart`, witness preparation |
| Legal Fact register | Fact classification candidate, event/source, relation to Element, disputed/adverse state | Exact provenance and distinction from judicial findings | `chronology`, matter history |
| Evidence matrix | Evidence ID, three-property review, proof purpose, opponent position, preservation/confidentiality risk and gap | Source, original-carrier and human verification | `claim-chart`, evidence Skills |
| Defense / Rebuttal map | Claim, Defense, Defense Element, facts/burden, evidence, Rebuttal, further response and remaining gap | Preserve all party perspectives and adverse facts | `claim-chart`, briefing, drafting |
| Authority check | Statutory basis, case tier, similarity, distinctions, freshness and usability | Retrieval date and warning against binding-precedent claims | legal research and reviewer notes |
| Gap / confidence report | Missing facts/evidence/authority, basis for any confidence statement, impact and proposed review question | No numeric confidence without disclosed basis | briefing and human review |
| Human review record | Candidate item, reviewer, decision, conditions, unresolved issues and timestamp | Qualified reviewer and consequential-action gate | all downstream consumers |

The output interface deliberately does not specify file serialization, runtime
objects, YAML, JSON, database tables or MCP payloads.

## 7. Skill and Agent Interaction Design

| Existing asset | Current responsibility | Potential future C01 responsibility | Interaction inputs / outputs | Overlap or conflict | Future authorization required | Current status |
|---|---|---|---|---|---|---|
| `matter-workspace` | Matter isolation and directory context | Carry stable Matter reference and links to reviewed analysis | Matter identity in; context reference out | Persistence contract differs from `matters/_README.md` | D1/D2/D6 approval, persistence decision and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `matter-intake` | Initial procedure/party/claim/evidence review | Initialize candidate Questions, Claims/Request Rights, facts and gaps | User/source materials in; candidate intake record out | May overlap with `claim-chart` as methodology owner | D1-D3/D6 approval, ownership decision and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `chronology` | Source-bound event timeline | Produce candidate Case/Event Fact links and adverse/disputed markers | Evidence/materials in; fact/event register out | Must not become the Claim/Element owner | D1-D3/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `claim-chart` | Claim/defense/fact/evidence/gap matrix | Candidate central owner for Request Right, Element, Proof and Defense/Rebuttal mapping | Reviewed intake/facts/evidence in; structured candidate mapping out | Strong overlap with intake and element templates; ownership unresolved | D1-D6 approval, explicit ownership decision and implementation Handoff | NO MODIFICATION AUTHORIZED |
| element templates reference | Illustrative claim/defense elements and evidence | Optional reviewed seed for Element candidates | Dispute type in; template candidates out | Risk of stale or hard-coded doctrine | D3/D5/D6 approval, authority-governance review and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `matter-briefing` | Management/lawyer matter summary | Present reviewed C01 analysis, gaps and adverse facts | Human-reviewed mapping in; summary out | Must not generate or silently finalize claims | D1/D4/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `brief-section-drafter` | Drafts sections from facts/evidence/authority | Consume only human-approved analysis references | Approved mapping in; reviewable draft out | High risk of turning candidates into advocacy assertions | D1/D3/D4/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `matter-update` | Append matter events and ledger effects | Record changes that invalidate or reopen candidate analysis | New event/evidence in; change notice out | Must preserve append-only history and avoid silent recomputation | D1/D2/D5/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| evidence Skills | Preservation and confidentiality safeguards | Consume reviewed evidence gaps and risk flags | Evidence IDs/gaps in; safeguard plan out | Consequential actions and data handling are specialized | D3/D5/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `witness-trial-prep` | Proof-subject and hearing-question preparation | Consume reviewed Element/Proof/Evidence links | Approved proof subjects in; reviewable question plan out | Must not invent facts or coach unsupported answers | D3/D5/D6 approval and implementation Handoff | NO MODIFICATION AUTHORIZED |
| `docket-watcher` Agent | Candidate procedural events/deadlines | Supply procedural facts only | Court/arbitration materials in; candidate events/deadlines out | `Write` tool overreach risk; no methodology inference | D1/D2/D5/D6 approval, separate Agent authorization and implementation Handoff | NO MODIFICATION AUTHORIZED |

No new Skill or Agent is assumed. If the existing assets cannot support the
approved ownership model, the outcome is `REQUIRES DECISION`, not permission to
create a component.

## 8. Future Change-Point Register

| Exact existing path | Candidate reason | Smallest conceivable future change | Dependencies and risks | D1-D6 prerequisite | Exact later authorization | C01-I action |
|---|---|---|---|---|---|---|
| `litigation-legal/skills/matter-intake/SKILL.md` | Natural entry for posture, parties, claims, facts and evidence | Add references to separately approved candidate Question/Claim identifiers and explicit handoff to mapping owner | Ownership duplication; premature claim selection | D1, D2, D3, D6 approved | `TASK_PHASE2_C01_IMPLEMENTATION` Handoff naming this path | NOT PERFORMED |
| `litigation-legal/skills/claim-chart/SKILL.md` | Closest current claim/fact/evidence matrix | Add separately approved fields/links for Request Right, Element, burden, proof rule, Defense/Rebuttal and gaps | Methodology drift; schema creep; overlap with intake | D1-D6 approved | `TASK_PHASE2_C01_IMPLEMENTATION` Handoff plus ownership decision | NOT PERFORMED |
| `litigation-legal/skills/claim-chart/references/element-templates.md` | Existing illustrative Element source | Add governance metadata or validation references only if separately approved | Stale doctrine and hard-coding | D3, D5, D6 approved | Specific reference-update authorization in implementation Handoff | NOT PERFORMED |
| `litigation-legal/skills/chronology/SKILL.md` | Existing source-bound event/fact extraction | Add approved fact-classification candidates and stable cross-references | Misclassification as judicial fact; duplication | D1-D3, D6 approved | `TASK_PHASE2_C01_IMPLEMENTATION` Handoff naming this path | NOT PERFORMED |
| `litigation-legal/skills/matter-workspace/SKILL.md` and matter conventions | Potential stable Matter context carrier | Add only approved analysis references, not an embedded runtime schema | Competing workspace layouts; cross-matter leakage | D1, D2, D6 approved | Persistence decision and implementation Handoff | NOT PERFORMED |
| `litigation-legal/skills/matter-briefing/SKILL.md` | Existing summary consumer | Require preservation of candidate status, adverse facts and unresolved gaps | Candidates may be flattened into conclusions | D1, D4, D6 approved | `TASK_PHASE2_C01_IMPLEMENTATION` Handoff naming this path | NOT PERFORMED |
| `litigation-legal/skills/brief-section-drafter/SKILL.md` | Existing drafting consumer | Require reviewed references before using C01 candidates | Advocacy output may overstate facts/law | D1, D3, D4, D6 approved | Specific downstream-consumer authorization | NOT PERFORMED |
| Evidence-related canonical Skills | Existing evidence safeguards | Accept reviewed Evidence IDs/gap references without changing specialized legal rules | Data/privacy risk; action authorization | D3, D5, D6 approved | Specific Skill-path authorization | NOT PERFORMED |
| `litigation-legal/agents/docket-watcher.md` | Existing procedural event source | If approved, expose only candidate event/deadline references to Matter context | Tool overreach; unverified source; scope expansion | D1, D2, D5, D6 approved | Separate Agent-change decision and implementation Handoff | NOT PERFORMED |
| `litigation-legal/CLAUDE.md` | Existing distributed professional gate | Align later with approved D6 without changing legal substance | Broad behavior impact across all Skills | D6 approved | Explicit system-alignment authorization | NOT PERFORMED |
| `litigation-legal/references/test-cases-cn.md` | Existing regression seed | Reference future C01 cases only under D5 governance | Conflation with future D5; test-scope drift | D5, D6 approved | Separate validation/reference authorization | NOT PERFORMED |

## 9. Implementation Boundary Report

### 9.1 MAY BE CONSIDERED IN A FUTURE HANDOFF

Only after D1-D6 approval and a path-specific Handoff:

- narrow changes to existing canonical Skills identified in Section 8;
- stable references between Matter, Question, Claim/Request Right, Element,
  Fact, Proof/Evidence and Defense/Rebuttal candidates;
- consumption of reviewed mappings by briefing/drafting Skills;
- validation against approved D5 cases;
- consolidation of qualified-human gates under approved D6;
- a separately approved, procedural-facts-only interaction with
  `docket-watcher`.

These are candidates, not approvals.

### 9.2 MUST REMAIN UNCHANGED

Under C01-I:

- all files under `litigation-legal/`;
- all 23 Skill definitions and the one Agent definition;
- `litigation-legal/CLAUDE.md`, plugin metadata and `.mcp.json`;
- matter ledger, workspace and history files;
- China-law references and element templates;
- the v0.2/v0.3 design artifacts and governance inputs;
- `PROJECT_SCOPE.md`, `PHASE_2_ROADMAP.md` and Architecture v0.5;
- all code, scripts, hooks, tests and connector assets.

### 9.3 REQUIRES ARCHITECTURE DECISION

- creating a new C01 Skill or Agent rather than extending an existing asset;
- choosing the canonical owner between `matter-intake` and `claim-chart`;
- introducing a shared runtime object, database, knowledge graph or schema;
- changing Matter persistence across `_log.yaml`, `matter.md` and `history.md`;
- creating a global orchestrator or cross-plugin methodology service;
- moving C01 ownership outside `litigation-legal`;
- granting an Agent authority to write C01 analysis or take consequential
  action.

### 9.4 OUT OF SCOPE

- automatic legal opinions, adjudication or outcome prediction;
- automatic claim selection or litigation strategy;
- suppression of adverse facts or inconsistent evidence;
- code, Skill, Agent, Plugin, MCP, workflow or runtime-schema changes;
- D1-D6 creation;
- filing, sending, calendar submission, preservation execution or other
  external/consequential action;
- database, case repository or knowledge-graph creation;
- implementation tests or release activity.

## 10. Risk Register

| Risk | Current evidence / trigger | Likelihood | Impact | Design control / future gate |
|---|---|---|---|---|
| Methodology drift | Multiple existing Skills already use overlapping claim/fact/evidence language | High | High | Treat v0.3 Sections 5-8 as immutable; D1-D4 approval before changes |
| Ownership duplication | `matter-intake`, `claim-chart` and `matter-briefing` overlap | High | High | Project Owner ownership decision before C01-II |
| Partial coverage overstated | Existing tables resemble C01 but omit stable IDs, burden/proof and rebuttal chain | High | High | Coverage labels and path evidence required; no “implemented” claim |
| Stale/hard-coded doctrine | Element templates contain dispute examples | Medium | High | Current-authority/date verification; templates remain candidates |
| Automated opinion/strategy behavior | Downstream briefing and drafting can sound conclusive | Medium | Critical | Candidate markers, adverse facts and D6 human gate |
| Adverse-fact suppression | Client-position analysis may favor one side | Medium | Critical | Mandatory adverse/disputed markers and Defense/Rebuttal path |
| Cross-matter leakage | Workspace Skill manages multiple matter directories | Low/Medium | Critical | Matter isolation, conflict checks and no cross-matter reads by default |
| Runtime schema creep | Desire for stable links may be translated into YAML/JSON/database design | High | High | This Spec remains Markdown; schema needs architecture decision and D2 approval |
| Compatibility-command confusion | Four legacy aliases coexist with canonical Skills | Medium | Medium | Canonical replacements only; aliases get no C01 ownership |
| Agent tool overreach | `docket-watcher` declares `Read` and `Write` | Medium | Critical | Procedural-facts-only boundary and separate Agent authorization |
| Workspace contract mismatch | `matter-workspace` and `matters/_README.md` document different layouts | Medium | Medium/High | Persistence decision before any field/link design |
| Case-authority misuse | Case examples may be treated as binding or current law | Medium | High | Authority tiers, freshness, similarity/distinction and statutory primacy |
| Validation conflation | Existing ten test cases are not D5 | Medium | Medium | Keep existing cases as seeds only; require approved D5 for C01 validation |
| Parallel methodology architecture | Gaps may encourage a new global layer | Low/Medium | Critical | Remain inside `litigation-legal`; architecture decision required for any deviation |

## 11. Non-Modification Plan

C01-I makes no implementation change. If later authorized, work should be
decomposed into separately reviewable changes while this Task makes none:

1. Approve D1-D6 as design artifacts; no runtime changes.
2. Decide canonical ownership for intake, central mapping, persistence and
   human review.
3. Approve a path-specific `TASK_PHASE2_C01_IMPLEMENTATION` Handoff naming the
   smallest existing Skill change set.
4. Review one Skill interaction boundary at a time; compatibility aliases stay
   routing-only.
5. Treat any Agent interaction as a separate decision with tool-scope review.
6. Execute C01-III validation only after separate authorization and approved D5.
7. Require qualified lawyer review before any consequential external use.

This plan contains no code, patches, prompt replacements or executable schemas.

## 12. Open Decisions and Next Authorization

| Decision needed | Question | Why unresolved | Required authority |
|---|---|---|---|
| C01 ownership | Does `claim-chart` own the central mapping, or does `matter-intake` own and delegate it? | Current responsibilities overlap | Project Owner / Architecture Decision |
| Persistence | Are C01 identifiers transient output references or stored in matter files? | Workspace layouts differ and no D2 exists | D2 approval plus Project Owner persistence decision |
| Request Right vs Claim | Are they separate records or related fields in the approved design artifact? | Current assets use `诉请` and `请求权基础` but no separate identity | D1/D2 approval and legal-methodology review |
| Element governance | How are templates versioned, refreshed and linked to current authority? | Existing templates are illustrative and undated | D3/D5 approval and authority-governance decision |
| Burden / proof rule source | Which current-law source and freshness mechanism supplies these fields? | Existing core rules do not provide a complete dynamic allocation model | D3 approval and Legal Data boundary review |
| Defense/Rebuttal ownership | Is the chain maintained in `claim-chart` or a separately approved existing consumer? | Current outputs co-list claims/defenses without a chain | D4 approval and ownership decision |
| Human gate | How is distributed review consolidated without broad unintended behavior change? | D6 is not generated | D6 approval and system-alignment review |
| Agent role | Does `docket-watcher` remain entirely adjacent or supply stable procedural-fact references? | Tool scope and source verification create risk | Separate Agent decision |
| Validation | How are existing test cases related to future D5 cases without conflation? | Existing tests predate C01 | D5 approval and C01-III authorization |
| Compatibility routes | Should documentation later point only to canonical commands? | Existing inbound docs still reference a compatibility alias | Separate documentation authorization; no C01-I change |

### Required Next Authorization

The next governance step is C01-I Design Review of this exact specification,
followed by explicit Project Owner approval or revision instructions.

Even after this specification is approved:

- D1-D6 remain ungenerated and unauthorized until separately approved;
- C01-II Skill/Agent enhancement remains unauthorized;
- C01-III validation remains unauthorized;
- implementation requires a separate
  `TASK_PHASE2_C01_IMPLEMENTATION` Handoff naming exact paths and acceptance
  criteria.

## 13. C01-I Acceptance Self-Check

| Criterion | Result | Evidence in this specification |
|---|---|---|
| AC-C01-I-001 — Fixed Input Identity | PASS | Section 1.2 records recomputed exact hashes and accepted architecture state |
| AC-C01-I-002 — Truthful Existing-Asset Inventory | PASS | Section 2 cites every asset path and distinguishes canonical, compatibility and deprecated assets |
| AC-C01-I-003 — Complete Methodology Mapping | PASS | Section 3 contains exactly one row for each of the ten required concepts, all with coverage, change point, authorization and NO CHANGE status |
| AC-C01-I-004 — Non-Executable Interface Design | PASS | Sections 5-6 are Markdown tables/prose and expressly exclude runtime serialization |
| AC-C01-I-005 — Implementation Boundary Completeness | PASS | Section 9 contains all four required boundary categories |
| AC-C01-I-006 — Professional and China-Law Boundary | PASS | Sections 5-6 and 10 require provenance, uncertainty, current authority, adverse facts and human review |
| AC-C01-I-007 — Single Authorized Output | PASS | This specification is the sole C01-I output; no Result, D1-D6 or implementation asset is created |
| AC-C01-I-008 — Review Readiness | PASS | Sections 1-12 provide inventory, mapping, interfaces, interactions, change register, boundary report, risks, non-modification plan and open decisions |

## 14. Current State and Next Step

```text
Phase 2 Track C

Architecture: ACCEPTED
C01 Design Baseline: APPROVED
C01-I Task: APPROVED
C01-I Implementation Design Specification: GENERATED — PENDING REVIEW
D1-D6: NOT GENERATED
C01-II Skill / Agent Enhancement: NOT AUTHORIZED
C01-III Validation: NOT AUTHORIZED
Implementation: NOT AUTHORIZED
```

Next step: submit this exact specification for C01-I Design Review and Project
Owner decision. Do not create D1-D6, an Implementation Handoff or any runtime
change as part of this C01-I execution.
