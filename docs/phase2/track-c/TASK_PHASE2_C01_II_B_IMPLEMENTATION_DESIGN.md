# TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C01 |
| Stage | C01-II-B-1 — Implementation Design |
| Document type | Documentation-only implementation design |
| Status | Completed design output; Architecture Review pending |
| Execution authority | Project Owner-approved `TASK_PHASE2_C01_II_B_IMPLEMENTATION_HANDOFF.md` |
| Handoff SHA-256 | `8989E7FCB9026B009F69BA2062C93FBD94337CEC7CB87FBF518E15671DADD623` |
| Design date | 2026-07-18 |

This document defines a reviewable, minimum-change implementation design for a possible later C01-II-B-2 stage. It does **not** authorize or perform Skill, Agent, code, Plugin, MCP, Workflow, runtime schema, or other runtime changes. Every proposed delta below is conceptual text-level design, not an applied patch.

## 1. Fixed Input Verification

### 1.1 Bound inputs

| Input | Repository path | SHA-256 | Verification |
|---|---|---|---|
| C01 v0.2 Reviewed Baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `67C74A63EE0BCCB4B20A9035467A16CF2B43EFD624E45C2B501A60A8590ED6E5` | PASS |
| C01-I Implementation Design Spec | `docs/phase2/track-c/TASK_PHASE2_C01_IMPLEMENTATION_DESIGN_SPEC.md` | `0274AB2C7542083BFBDFF98F00E7143F7D45927EEEED5675BF28BF6631A862C7` | PASS |
| C01-II-A Skill Design Mapping | `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md` | `ACBCCB077EB3EE7193C0AC031C23950FC9EF31FE43A44A3D5EB07ABC96474115` | PASS |
| C01-II-A Mapping Decision | `.codex-coordination/decisions/TASK_PHASE2_C01_II_A_MAPPING_DECISION.md` | `0D3A782C05C75DEA32E04346668CEBB60ACAF2C3B87DA0DB3CE61128BB477873` | PASS |
| C01-II-B Implementation Handoff | `.codex-coordination/inbox/TASK_PHASE2_C01_II_B_IMPLEMENTATION_HANDOFF.md` | `8989E7FCB9026B009F69BA2062C93FBD94337CEC7CB87FBF518E15671DADD623` | PASS |

The design is subordinate to those fixed inputs. In case of ambiguity, the narrower authorization boundary controls.

### 1.2 Methodology preserved

The approved legal-analysis sequence remains unchanged:

`Matter → Issue → Question → Claim → Request Right → Element → Legal Fact → Proof → Evidence → Defense / Rebuttal`

This design maps that sequence into existing assets. It does not create a global legal-reasoning core, a parallel methodology framework, an automatic legal-opinion system, a decision-prediction system, or a substitute for qualified lawyer judgment.

## 2. Authorization Boundary and Design Principles

### 2.1 Current authorization

The current stage permits only this Markdown design and its execution Result. C01-II-B-2 Skill/Agent modification and C01-II-B-3 validation execution remain **NOT AUTHORIZED**.

### 2.2 Controlling principles

1. **Reuse existing ownership.** Extend the current `litigation-legal` assets at their existing responsibilities; do not introduce a new methodology directory or orchestration layer.
2. **Candidate before approved.** Machine-assisted analysis remains explicitly provisional until qualified human review.
3. **Provenance before conclusion.** Facts, authorities, evidence, and legal propositions retain source, freshness, jurisdiction, adverse-material, and uncertainty signals.
4. **Conceptual contracts only.** Input/output fields in this document are documentation contracts, not runtime, MCP, Workflow, database, or serialization schemas.
5. **Minimum surface.** The first possible implementation package is limited to the four core analytical assets needed to carry the approved chain. Consumers and specialist safeguards follow only after core review.
6. **No silent automation.** No proposal permits automatic claim selection, element satisfaction, evidentiary admissibility findings, filing decisions, legal opinions, or judicial-outcome predictions.
7. **China-law fit.** Any later implementation must preserve current-law checking, authority hierarchy, territorial and temporal applicability, source traceability, and qualified-lawyer control appropriate to PRC legal work.

## 3. Exact Candidate Surface and Pre-change Identity

Only assets listed in C01-II-A Mapping Section 7.1 are eligible even for a future proposal. The current bytes remain unchanged.

| Package | Candidate path | Current SHA-256 | Bytes | Future role |
|---|---|---:|---:|---|
| P1 Core | `litigation-legal/skills/matter-intake/SKILL.md` | `F0FCBBBE233BDFA0D846A3DE78D17FE3C8DD03189B2745DAE3FE235EC70E0C00` | 2,960 | Initialize candidate Issue, Question, Claim, Request Right and gaps |
| P1 Core | `litigation-legal/skills/chronology/SKILL.md` | `927E7E08BBBE2B8ED97595CDBFEA4742E4C6B9D8DC9EFD41D9CE334D433702F2` | 1,489 | Normalize source-bound candidate Legal Facts |
| P1 Core | `litigation-legal/skills/claim-chart/SKILL.md` | `1B130FD98A1E46A3D928ADDC905A37B59B998F0B2EE9E86B81AE07193CFE4DCC` | 1,852 | Own the central candidate Claim/Right/Element/Proof/Evidence/Defense mapping |
| P1 Core | `litigation-legal/skills/claim-chart/references/element-templates.md` | `1EFD953B217290A4310084518CEE06E008631F303F65845677DD9A65EF56E6EA` | 2,918 | Add template governance and non-authoritative safeguards |
| P2 Lifecycle / Consumer | `litigation-legal/skills/matter-update/SKILL.md` | `04FB6C9D3A930C17ACD50957E9FD66A2821FAF5B4FE6FF03012E17EB1F94A2C0` | 1,121 | Record impact of new material on reviewed analysis |
| P2 Lifecycle / Consumer | `litigation-legal/skills/matter-briefing/SKILL.md` | `6064D4BFB3AE41F88EDF0D94628131AF6CB8C16EB8EEDD7BC0928EF8212C68B6` | 926 | Present approved/candidate state without collapsing distinctions |
| P2 Lifecycle / Consumer | `litigation-legal/skills/brief-section-drafter/SKILL.md` | `8FDC03E52A6BA4FF34DAE6890EDBA8A657EF2B455EDBC8C061FD4A0ACC664894` | 1,735 | Consume reviewed references for drafting, not choose litigation theory |
| P2 Lifecycle / Consumer | `litigation-legal/skills/witness-trial-prep/SKILL.md` | `14EAFE498D62CD3BF1796424D417B5C090022D0F60309994404BEDD3933A197A` | 771 | Consume reviewed Proof/Evidence references for preparation |
| P3 Evidence Specialist | `litigation-legal/skills/evidence-preservation/SKILL.md` | `A9E15EEC0FD36CBA03930FDB8FD1A903B60248319AD82F78B3ACF259E608F4EA` | 1,089 | Preserve evidence context without deciding probative or admissibility issues |
| P3 Evidence Specialist | `litigation-legal/skills/confidential-evidence-review/SKILL.md` | `96234688F60DB1AC44C1FBC3156F4D68C046D38B6EE6680FA29734938D36F209` | 1,212 | Preserve confidentiality controls while accepting reviewed references |
| P4 Deferred | `litigation-legal/skills/matter-workspace/SKILL.md` | `71BEA7881FD26E57B0C34AE42C71BE78977C11214170B7D826CF27D99B79782B` | 1,159 | Possible Matter container metadata only after persistence decision |
| P4 Deferred | `litigation-legal/agents/docket-watcher.md` | `70B1A279087AE86B31FC3FF94A4D9EC45C3C8C830D7B3964D793B721778307BD` | 1,923 | Possible procedural candidate signal only under separate Agent approval |
| P4 Deferred | `litigation-legal/CLAUDE.md` | `18094691C3BEF899063320B849D9D15B338970D4B20D05F91D2A5D01C6CA0236` | 5,208 | Possible system-level terminology alignment only after broad review |

Compatibility aliases, the deprecated Skill, manifests, plugin metadata, Workflow files, MCP configuration, runtime schemas, source code, and every asset outside this table are outside the proposed change surface.

## 4. Minimum-change Packaging and Authorization Sequence

### 4.1 Recommended sequence

| Sequence | Package | Proposed future authorization | Rationale |
|---:|---|---|---|
| 1 | P1 Core | First, separate C01-II-B-2 authorization | Smallest coherent chain that can initialize, normalize, and map candidate legal analysis |
| 2 | P2 Lifecycle / Consumer | Separate authorization after P1 review | Prevent consumers from depending on an unreviewed core contract |
| 3 | P3 Evidence Specialist | Separate authorization after P1 review | Preserve specialist safeguards and avoid expanding their legal-analysis role |
| 4 | P4 Deferred | No initial authorization recommended | Requires decisions with wider persistence, Agent, or system-instruction impact |

P1 is the recommended minimum viable modification surface. P2 and P3 are not prerequisites for reviewing P1. P4 should not be bundled with any initial implementation.

### 4.2 Dependency order within P1

1. Add governance metadata to the illustrative element templates.
2. Add candidate intake/handoff concepts to `matter-intake`.
3. Add source-bound Legal Fact concepts to `chronology`.
4. Add the central candidate analytical matrix and review controls to `claim-chart`.
5. Perform static and scenario review before considering any consumer changes.

No step creates a database, persistent graph, runtime state machine, new provider, new tool, or cross-matter data path.

## 5. Diff-level Text Design — P1 Core

The following blocks specify the intent and placement of possible future edits. They are not patches and must not be applied without separate C01-II-B-2 approval.

### 5.1 `litigation-legal/skills/matter-intake/SKILL.md`

**Placement:** extend the existing intake fields and output/review instructions; preserve the present human approval gate.

```diff
+ Add optional candidate analysis handoff fields: Issue Ref, Question Ref, Claim Ref, Request Right Ref.
+ For each field, require status `candidate`, source/provenance links, uncertainty, adverse facts, missing information, and assigned reviewer where known.
+ Distinguish client objective, requested remedy, asserted claim, and possible request-right basis; do not infer that any candidate basis is legally available.
+ Require current-law and authority verification before a candidate Request Right is used downstream.
+ Handoff only candidate references and open questions to chronology/claim-chart; do not select claims, make filing decisions, or issue legal opinions.
+ Preserve the existing requirement that qualified counsel approve consequential use.
```

**Concept ownership:** initializes Issue, Question, Claim and Request Right candidates; it does not own final element analysis.

### 5.2 `litigation-legal/skills/chronology/SKILL.md`

**Placement:** extend the current event/fact table and source rules.

```diff
+ Add a stable Legal Fact Ref for each candidate fact without changing the source record.
+ Record fact classification, asserted/disputed/unknown state, source and locator, date confidence, supporting and contradictory material, adverse significance, and linked Claim/Element refs when supplied.
+ Separate observed/source-reported fact from legal characterization and inference.
+ Mark conflicts and missing provenance; never resolve credibility, authenticity, admissibility, or legal effect automatically.
+ Return source-bound candidate Legal Fact refs to claim-chart while preserving chronology as the fact-normalization owner.
```

**Concept ownership:** owns candidate Legal Fact normalization; it does not own Claim or Proof conclusions.

### 5.3 `litigation-legal/skills/claim-chart/SKILL.md`

**Placement:** extend the existing claim/defense/request-right/fact/evidence matrix and review instructions.

```diff
+ Treat Claim Ref as the analysis unit and link a candidate Request Right Ref with jurisdiction, temporal applicability, authority source, verification date, uncertainty, and reviewer status.
+ For each candidate Element, record the proposition to be established, supporting and adverse Legal Fact refs, candidate burden/proof-rule source, supporting/contradictory Evidence refs, proof gap, and review status.
+ Preserve separate Defense and Rebuttal candidates, including their own elements, facts, evidence, adverse material, gaps, and reviewer decisions.
+ Use explicit lifecycle labels only as documentation metadata: candidate, reviewed-approved, reviewed-rejected, superseded, or unresolved.
+ Require qualified human review before any element is treated as satisfied, any evidence is treated as usable, or any theory is used in drafting, filing, negotiation, or advice.
+ Surface current-law, source, adverse-fact, proof, and authority gaps; never calculate an outcome score or issue a legal conclusion.
```

**Concept ownership:** central mapping owner for Claim, Request Right, Element, Proof, Evidence and Defense/Rebuttal relationships. Review labels are governance metadata, not a runtime state machine.

### 5.4 `litigation-legal/skills/claim-chart/references/element-templates.md`

**Placement:** add a governance preface and per-template source notes; retain templates as illustrative aids.

```diff
+ State that templates are non-authoritative issue-spotting aids, not complete statements of current law.
+ Require jurisdiction, authority level, effective date/currentness, source citation, version date, and human verifier before use.
+ Require the user to add adverse, exception, defense, burden, and remedy conditions applicable to the matter.
+ Prohibit automatic element satisfaction, automatic claim selection, and reliance on a template where controlling authority is missing or stale.
+ Preserve uncertainty and record deviations from the template.
```

**Concept ownership:** provides governed examples only; the Claim Chart and qualified reviewer remain controlling.

## 6. Diff-level Text Design — P2 Lifecycle and Consumers

P2 should be considered only after P1 has been reviewed and accepted.

### 6.1 `litigation-legal/skills/matter-update/SKILL.md`

```diff
+ When new material arrives, identify affected candidate/reviewed refs without silently overwriting prior analysis.
+ Record the change, source, affected Issue/Claim/Element/Fact/Proof/Evidence/Defense refs, impact hypothesis, reopened gaps, and required reviewer.
+ Require re-review before a previously approved analysis is reused when authority, facts, evidence, or adverse material materially changes.
```

### 6.2 `litigation-legal/skills/matter-briefing/SKILL.md`

```diff
+ Preserve candidate versus reviewed-approved/rejected/unresolved status in presentation outputs.
+ Present adverse facts, contrary authority, evidence and proof gaps, source freshness, and pending human decisions alongside favorable analysis.
+ Do not convert a briefing summary into a legal opinion or predicted outcome.
```

### 6.3 `litigation-legal/skills/brief-section-drafter/SKILL.md`

```diff
+ Accept only identified, reviewed references for propositions intended for external or consequential drafting.
+ Preserve citations, authority/currentness notes, adverse material, and unresolved qualifications supplied by the reviewed analysis.
+ Reject or flag missing approval; do not choose a claim, request right, element conclusion, or litigation theory.
+ Retain lawyer review before use in any filing, advice, negotiation, or client communication.
```

### 6.4 `litigation-legal/skills/witness-trial-prep/SKILL.md`

```diff
+ Link preparation topics to reviewed Proof and Evidence refs and the Legal Facts they may support or contradict.
+ Surface evidentiary, credibility, privilege, confidentiality, and adverse-material flags for lawyer handling.
+ Do not decide witness credibility, coach false testimony, determine admissibility, or replace trial counsel judgment.
```

## 7. Diff-level Text Design — P3 Evidence Specialists

P3 must preserve each specialist Skill's existing protective function.

### 7.1 `litigation-legal/skills/evidence-preservation/SKILL.md`

```diff
+ Accept reviewed/candidate Evidence and Legal Fact refs only as contextual identifiers for preservation scope.
+ Preserve source, custodian, collection, integrity, retention, privilege/confidentiality, and chain-of-custody context as applicable.
+ Do not decide probative value, authenticity, admissibility, element satisfaction, or legal sufficiency.
```

### 7.2 `litigation-legal/skills/confidential-evidence-review/SKILL.md`

```diff
+ Accept reviewed/candidate Evidence refs while preserving matter isolation, access controls, confidentiality and privilege handling.
+ Return only permitted metadata or redacted findings with source linkage and reviewer flags.
+ Do not weaken protective controls or infer that restricted evidence may be used in analysis, disclosure, filing, or advice.
```

## 8. Deferred Design Candidates — P4

No P4 change is recommended for the first C01-II-B-2 authorization.

### 8.1 `litigation-legal/skills/matter-workspace/SKILL.md`

**Reason deferred:** the current workspace structure and repository matter-layout guidance require a single persistence decision before adding C01 reference metadata. Premature edits could create competing storage conventions.

**Possible later, separately reviewed delta:** add only Matter-level identifiers, isolation rules and links to approved analysis artifacts after the canonical persistence location is decided. Do not embed legal-analysis logic in the workspace Skill.

### 8.2 `litigation-legal/agents/docket-watcher.md`

**Reason deferred:** Agent changes have a wider autonomous-observation and tool-use impact and require separate authorization.

**Possible later, separately reviewed delta:** emit source-bound procedural candidate facts/deadlines for human verification and optional intake; never update substantive analysis, calculate legal deadlines conclusively, or apply decisions automatically.

### 8.3 `litigation-legal/CLAUDE.md`

**Reason deferred:** this is a system-wide instruction surface. The existing distributed human-review, current-law, provenance and professional-boundary controls are already directionally compatible.

**Possible later, separately reviewed delta:** terminology alignment only after P1/P2/P3 behavior is validated. Human Review must remain a governance control pattern and must not become D6 or a runtime state machine.

## 9. Conceptual Input / Output Contract

These tables define information semantics for documentation and review. They do not prescribe JSON, YAML, database columns, runtime schemas, Workflow states, MCP payloads, or APIs.

### 9.1 Common conceptual input envelope

| Concept | Required semantics | Guardrail |
|---|---|---|
| Matter context | Matter identifier, objective, procedural posture, jurisdiction, applicable dates | Keep matters isolated; no cross-matter reuse without explicit approval |
| Source set | Source identifier, type, locator, date, provenance, access/confidentiality status | No unsupported fact or authority |
| Prior references | Candidate/reviewed analysis refs and version/status | No silent overwrite; preserve superseded/rejected history |
| Authority context | Jurisdiction, authority level, effective/currentness date, citation/source | Qualified reviewer verifies controlling/current law |
| Review context | Candidate status, reviewer role, decision, date, limitations | No self-approval by the generating system |

### 9.2 Core conceptual output records

| Record | Minimum semantics | Owner | Prohibited inference |
|---|---|---|---|
| Issue / Question candidate | Ref, statement, source/context, uncertainty, adverse/missing information, status | matter-intake | That the issue is dispositive or complete |
| Claim / Request Right candidate | Ref, requested relief, possible legal basis, authority/currentness data, adverse conditions, status | intake → claim-chart | That the claim is available, viable, or selected |
| Legal Fact candidate | Ref, neutral proposition, fact/inference distinction, source/locator, dispute/adverse state, linked refs | chronology | Credibility, authenticity, admissibility, or legal effect |
| Element / Proof candidate | Ref, proposition, authority/proof-rule candidate, supporting/adverse fact refs, evidence refs, gaps, status | claim-chart | Element satisfaction or burden discharge |
| Evidence candidate | Ref, description, source/custodian, integrity/access flags, supporting/contradictory links, gaps | claim-chart with specialists | Admissibility, weight, authenticity, or sufficiency |
| Defense / Rebuttal candidate | Ref, asserted theory, basis, elements, facts, evidence, gaps, adverse material, status | claim-chart | Ultimate merit or outcome prediction |
| Review decision | Target ref/version, qualified reviewer, approve/reject/request-revision decision, date, scope/limitations | qualified human | Runtime execution permission beyond the recorded scope |

### 9.3 Downstream consumption rule

A downstream consumer receives the reference, its review status, sources, limitations, adverse material and gaps. It must not strip those controls, silently upgrade a candidate, or reuse a decision outside its recorded matter/version/scope.

## 10. Agent and Human Review Integration Boundary

The controlling pattern is:

`Candidate Analysis → Qualified Human Review → Approval Decision → Optional Application`

This is a governance control pattern only.

- Skills may organize and surface candidates, sources, contradictions, adverse material, and gaps.
- A qualified human determines whether analysis is correct, complete, current, professionally usable, and within authority.
- Approval is scoped to a specific matter, artifact version and purpose.
- Application remains optional and may require an additional professional or procedural decision.
- No Agent or Skill may approve its own output, convert labels into autonomous Workflow transitions, or treat review metadata as permission to file, advise, disclose, send, or deploy.
- The current `docket-watcher` remains unchanged in this stage and is not a C01 analysis orchestrator.

## 11. Proposed C01-II-B-2 Authorization Units

Any future implementation authorization should name exact files, bind their pre-change hashes, and be independently reviewable.

### B-2.1 Core candidate mapping — recommended first

- Four P1 paths only.
- Documentation/instruction edits only.
- No alias, Agent, system, Workflow, schema, MCP, Plugin, manifest, or code change.
- Stop after static and scenario validation; obtain Architecture Review before P2/P3.

### B-2.2 Lifecycle consumers — conditional

- Four P2 paths only.
- Authorized only after B-2.1 output contract and status semantics are accepted.
- Must not add independent legal reasoning or bypass review.

### B-2.3 Evidence specialist integration — conditional

- Two P3 paths only.
- Authorized only after evidence-reference semantics and specialist protective controls are reviewed.
- Must not expand preservation/confidential-review Skills into admissibility or merits decision-makers.

### B-2.4 Deferred system surfaces — no current recommendation

- Each P4 path requires a separate decision.
- `matter-workspace` requires a persistence-location decision.
- `docket-watcher` requires Agent-specific safety review.
- `CLAUDE.md` requires system-wide regression review.

## 12. Risk Assessment

| ID | Risk | Trigger | Impact | Mitigation / gate |
|---|---|---|---|---|
| R01 | Parallel methodology | New core, directory, or second ownership chain | Conflicting legal analysis | Reuse owners in Section 3; reject any new methodology layer |
| R02 | Candidate treated as conclusion | Status/provenance omitted downstream | Unsupported advice or filing | Mandatory status, source, limitation and qualified-review fields |
| R03 | Stale or inapplicable PRC authority | Missing jurisdiction/effective date/freshness check | Incorrect legal basis | Require authority hierarchy, territorial/temporal fit, source and verification date |
| R04 | Favorable-only analysis | Adverse facts/authority/evidence omitted | Professional and litigation risk | Mandatory adverse/contradictory fields and reviewer checklist |
| R05 | Template overreach | Illustrative elements treated as current law | False completeness | Template governance, source/currentness verification and deviation record |
| R06 | Role collision | Intake/chronology/consumer performs Claim Chart conclusions | Inconsistent ownership | Enforce ownership table and reference-only handoffs |
| R07 | Runtime-schema drift | Conceptual contract copied into executable schema | Unreviewed compatibility change | Explicit non-schema language; path audit; separate schema prohibition |
| R08 | Human gate becomes automation | Status label drives Workflow or Agent action | Unauthorized autonomous use | Governance-only semantics; no runtime transition or self-approval |
| R09 | Specialist safeguard erosion | Evidence integration overrides privilege/confidentiality/preservation rules | Disclosure or integrity harm | Specialist controls prevail; pass refs only; separate P3 review |
| R10 | Matter isolation failure | References reused across matters | Confidentiality/provenance breach | Matter-bound refs and explicit cross-matter prohibition |
| R11 | Broad regression | System/Agent/Persistence surfaces bundled with core | Hard-to-review behavior changes | Defer P4; package exact paths with pre-change hashes |
| R12 | Compatibility regression | Alias or deprecated asset modified unnecessarily | Invocation breakage | Leave aliases/deprecated asset untouched; test existing routing later |

## 13. Rollback Plan for a Future Authorized Implementation

No rollback is required now because no runtime asset is modified. If a later C01-II-B-2 package is authorized:

1. Bind every target to the pre-change SHA-256 values in Section 3 and stop on mismatch.
2. Capture a reviewed, file-specific forward patch before applying it; do not overwrite unrelated user changes.
3. Apply one authorized package at a time, with P1 files in the dependency order in Section 4.2.
4. Run validation immediately after each file and package; do not continue on a boundary, content, or routing failure.
5. On failure, create and review an inverse patch limited to the authorized lines/files. Do not use `git reset --hard`, broad checkout, clean, or deletion operations.
6. Recompute hashes and confirm that rollback restores the intended pre-change bytes or an explicitly reviewed user-preserving equivalent.
7. Confirm no matter data migration, database transformation, external-provider change, or runtime-state conversion occurred; none is part of this design.
8. Record the rollback reason, affected package, before/after hashes, validation result and unresolved risk in the package Result.

Rollback triggers include: unauthorized path change, candidate status loss, provenance loss, Human Review bypass, stale-authority behavior, cross-matter leakage, alias regression, specialist-control weakening, or any implied automatic legal decision.

## 14. C01-II-B-3 Validation Plan (Design Only)

C01-II-B-3 execution is not authorized. The following plan is for later approval.

### 14.1 Static boundary checks

- Compare changed paths against the exact package allowlist and pre-change hashes.
- Confirm no code, Agent (unless separately authorized), alias, deprecated Skill, Plugin, manifest, MCP, Workflow, runtime schema, database, external provider, D1-D6, or new methodology asset changed.
- Confirm no executable schema or runtime transition was introduced.
- Run whitespace/conflict checks and verify staging remains empty unless a later authorization explicitly changes that rule.

### 14.2 Content and professional-boundary checks

- Verify every analytical output is marked candidate until qualified human review.
- Verify authority hierarchy, jurisdiction, effective/currentness date, source and verification uncertainty are present where law is relied upon.
- Verify source locators, adverse facts, contrary authority/evidence, gaps and rejected/superseded states remain visible.
- Verify no automatic legal opinion, claim selection, element satisfaction, admissibility finding, filing action or outcome prediction appears.
- Verify Human Review is governance, not a runtime state machine.

### 14.3 Scenario tests

| Scenario | Expected result |
|---|---|
| Incomplete intake with conflicting client account | Candidate Issues/Questions plus conflict and gap; no claim conclusion |
| Possible right basis with stale source | Mark unverified/stale and block consequential downstream use pending reviewer verification |
| Chronology contains favorable and adverse documents | Separate source-bound facts and contradictions; no credibility resolution |
| Element has strong evidence but missing controlling authority | Remain unresolved; no element-satisfied conclusion |
| Defense evidence is confidential | Preserve restricted handling and surface only permitted metadata |
| Consumer receives candidate rather than approved ref | Flag/reject consequential drafting; do not silently upgrade status |
| Updated law or new adverse fact | Reopen affected refs for review and preserve prior version history |
| Cross-matter reference supplied | Reject/flag unless explicit authorized transfer and provenance controls exist |
| Compatibility alias invokes canonical Skill | Existing routing remains unchanged |
| Docket event observed | Existing Agent behavior remains source-bound and human-verified; no substantive C01 update |

### 14.4 Validation evidence

A later validation Result should record exact inputs, path diff, before/after hashes, scenario evidence, failures and residual risk. Passing tests would support review only; it would not itself authorize deployment, filing, advice, or a new implementation phase.

## 15. Proposed Acceptance Criteria for a Future B-2 Package

| AC | Criterion |
|---|---|
| AC-B2-001 | Exact authorized input and target hashes match before editing |
| AC-B2-002 | Only explicitly authorized package paths change |
| AC-B2-003 | Proposed changes trace to C01-II-A Mapping Section 7.1 and this design |
| AC-B2-004 | Existing methodology ownership is preserved; no new reasoning core appears |
| AC-B2-005 | Candidate, provenance, adverse-material, uncertainty and gap semantics are explicit |
| AC-B2-006 | Human Review remains qualified, scoped, external to the generating Skill, and non-runtime |
| AC-B2-007 | China-law authority freshness, hierarchy and applicability checks are preserved |
| AC-B2-008 | No automatic opinion, prediction, filing, claim selection, element satisfaction or evidence decision is introduced |
| AC-B2-009 | Aliases, deprecated Skill, specialist safeguards and matter isolation remain intact |
| AC-B2-010 | Technical checks pass, staging remains empty, and the package Result binds all hashes |

## 16. Explicit Exclusions and Open Decisions

### 16.1 Excluded from this design execution

- Applying any text proposal in Sections 5–8.
- Modifying any file under `litigation-legal/`.
- Creating D1-D6 or an equivalent substitute.
- Adding code, database, knowledge graph, external provider, MCP, Workflow, runtime schema, Plugin, marketplace or deployment behavior.
- Creating a global legal-reasoning core or parallel framework.
- Staging, committing, tagging, pushing, releasing or publishing.

### 16.2 Decisions required before wider change

1. Whether Project Owner authorizes B-2.1 P1 only, with exact file/hashes.
2. Which qualified roles may approve which candidate records and purposes; this remains governance, not runtime schema.
3. Whether P1 review status terminology is acceptable for documentation-only use.
4. Whether and when P2/P3 consumers may rely on approved references.
5. Which canonical persistence location governs before any `matter-workspace` proposal.
6. Whether Agent or system-level changes are needed after P1–P3 validation; no need is presumed.

## 17. Completion State and Next Gate

This C01-II-B-1 design is complete for Architecture Review. It proposes no current implementation and makes no runtime change.

```text
C01-II-B-1 Implementation Design: COMPLETED / REVIEW PENDING
C01-II-B-2 Skill or Agent Modification: NOT AUTHORIZED
C01-II-B-3 Validation Execution: NOT AUTHORIZED
D1-D6: NOT AUTHORIZED
Code / Skill / Agent / Plugin / MCP / Workflow / Runtime Schema changes: NONE
Next gate: Architecture Coordinator Review → Project Owner Decision
```
