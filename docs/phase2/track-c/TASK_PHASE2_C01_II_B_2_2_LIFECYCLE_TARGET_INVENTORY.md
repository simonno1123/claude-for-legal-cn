# TASK_PHASE2_C01_II_B_2_2_LIFECYCLE_TARGET_INVENTORY

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C01 |
| Stage | C01-II-B-2.2-A — Lifecycle Target Inventory and Scope Binding |
| Document type | Read-only target inventory and future whitelist proposal |
| Status | COMPLETED — Architecture Review pending |
| Approved revised Handoff SHA-256 | `3C77E57951B5016766D363B8E588464B453F62805A8E4397B1D508ED36A3F85C` |
| Inventory date | 2026-07-18 |

This document records a read-only inventory. It does not authorize or apply any change under `litigation-legal/`. Every proposed instruction block is text for a possible later B-2.2-B authorization, not an executable patch, runtime schema, Workflow, or state machine.

## 1. Fixed Input and P1 Baseline Verification

### 1.1 Governance and design inputs

| Input | Required and actual SHA-256 | Result |
|---|---|---|
| C01 Design Baseline v0.2 | `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784` | PASS |
| C01-I Implementation Design Spec | `9C123A93D2C348C53A48A7F8526A1913443EFA785FE1691174696102714E3553` | PASS |
| C01-II-A Skill Design Mapping | `8E52FB0F5DC13DD82B610E351653F11DA16178D6073621C0D773136DA9695870` | PASS |
| C01-II-B-1 Implementation Design | `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E` | PASS |
| C01-II-B-2.1 Implementation Result | `B41815E98949EDFEB16C43818DF67D8885AC12770DBC841BE0310EE920EFA7A0` | PASS |
| C01-II-B-2.1 Result Record | `54A8925B9F0057758CF5028D7D273AEFF57EB8CAD9557ADED981C2DD89AE0E36` | PASS |

### 1.2 P1 post-change identities

| P1 asset | Post-change SHA-256 | Result |
|---|---|---|
| `litigation-legal/skills/claim-chart/references/element-templates.md` | `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D` | PASS |
| `litigation-legal/skills/matter-intake/SKILL.md` | `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18` | PASS |
| `litigation-legal/skills/chronology/SKILL.md` | `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2` | PASS |
| `litigation-legal/skills/claim-chart/SKILL.md` | `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B` | PASS |

The four P1 files are fixed inputs to this inventory. They are not candidates for B-2.2-B modification.

## 2. Audit Method and Architecture Facts

The inventory used four read-only evidence layers:

1. the 24-asset C01-II-A inventory and ownership matrix;
2. B-1 Design §§6, 9, 10 and 11;
3. current bytes and SHA-256 identities of all 23 Skill definitions and the one Agent;
4. direct content inspection of P1, the four P2 candidates, adjacent lifecycle Skills, both P3 specialists, P4 surfaces, the Agent and `litigation-legal/CLAUDE.md`.

Current architecture count:

| Class | Count | Lifecycle treatment |
|---|---:|---|
| Canonical Skills | 18 | Three proposed MODIFY, fourteen NO CHANGE, one DEFER |
| Compatibility aliases | 4 | NO CHANGE; routing only |
| Deprecated Skill | 1 | NO CHANGE; redirect only |
| Agent | 1 | DEFER; separate Agent/tool-scope authority required |
| System instruction (`CLAUDE.md`, outside 24-asset count) | 1 | DEFER; broad system review required |

No new Skill, lifecycle controller, orchestration layer, database, knowledge graph, schema, or persistence convention is needed for the proposed minimum package.

## 3. Lifecycle Control Model

### 3.1 Governance-only flow

The existing P1 owners remain controlling:

`matter-intake / chronology / claim-chart → qualified review → matter-update → qualified re-review → matter-briefing / brief-section-drafter → optional application`

The arrows describe document handoffs and manual review dependencies only. They do not create autonomous transitions.

### 3.2 Responsibility boundaries

| Stage | Existing owner | Lifecycle responsibility | Must not do |
|---|---|---|---|
| Candidate initialization | `matter-intake` | Supply candidate Issue/Question/Claim/Request Right refs | Select the legal basis or authorize filing |
| Fact normalization | `chronology` | Supply source-bound candidate Legal Fact refs | Resolve credibility, admissibility or legal effect |
| Analytical mapping | `claim-chart` | Own candidate Claim/Right/Element/Proof/Evidence/Defense relationships | Self-approve or predict outcome |
| Change detection | `matter-update` | Identify affected refs and request re-review | Rewrite P1 analysis or silently replace history |
| Presentation | `matter-briefing` | Present status, adverse material, freshness, gaps and pending decisions | Upgrade a candidate or issue a legal opinion |
| Consequential drafting | `brief-section-drafter` | Consume reviewed refs while retaining limitations | Choose theory or treat unreviewed propositions as approved |
| Hearing/witness preparation | `witness-trial-prep` | Current role remains unchanged | Enter P3 evidence/confidentiality/admissibility scope in this package |

## 4. Candidate Target Matrix

Each current hash was recomputed from the canonical workspace. `MODIFY` means “recommended for a separately approved B-2.2-B”; it does not authorize a present edit.

| Exact path | Current SHA-256 | Current role | Gap | Proposed instruction edit | Overlap/isolation risk | Recommendation |
|---|---|---|---|---|---|---|
| `litigation-legal/skills/matter-update/SKILL.md` | `04FB6C9D3A930C17ACD50957E9FD66A2821FAF5B4FE6FF03012E17EB1F94A2C0` | Appends procedural, evidence, deadline, preservation, settlement, enforcement and counsel updates | Does not identify affected C01 refs, preserve prior analytical status, record an impact hypothesis, reopen gaps or assign re-review | Add source-bound affected-ref, impact, reopened-gap and required-reviewer fields; prohibit silent overwrite; require re-review after material change | Medium: must remain an impact signal, not a second chronology/claim-chart owner or persistence engine | **MODIFY** |
| `litigation-legal/skills/matter-briefing/SKILL.md` | `6064D4BFB3AE41F88EDF0D94628131AF6CB8C16EB8EEDD7BC0928EF8212C68B6` | Presents procedure, claims/defenses, evidence, preservation, settlement, enforcement and next decisions | Summary can flatten candidate/reviewed/rejected/unresolved states and omit adverse material, authority freshness and pending review | Preserve status and version; present adverse facts/authority, proof/evidence gaps, freshness and pending human decisions; prohibit opinion/prediction | Low: presentation only; must not become an analytical owner | **MODIFY** |
| `litigation-legal/skills/brief-section-drafter/SKILL.md` | `8FDC03E52A6BA4FF34DAE6890EDBA8A657EF2B455EDBC8C061FD4A0ACC664894` | Drafts reviewable local sections for pleadings, arbitration, preservation, investigation and enforcement documents | Requires lawyer review but does not require reviewed analytical refs or preserve source/currentness/adverse qualifications | Gate consequential propositions on identified reviewed refs; preserve citations, currentness, adverse material and limitations; flag missing approval; prohibit theory selection | High: external advocacy risk; guardrail additions only, no substantive reasoning | **MODIFY** |
| `litigation-legal/skills/witness-trial-prep/SKILL.md` | `14EAFE498D62CD3BF1796424D417B5C090022D0F60309994404BEDD3933A197A` | Organizes proof subjects, claim/defense links, evidence links, questions and risks | Does not consume reviewed Proof/Evidence refs or explicitly preserve adverse/credibility boundaries | No B-2.2-B prompt block recommended now; B-1 §6.4 intent requires a later decision on reviewed Evidence refs and evidence/confidentiality/admissibility boundaries | High: proposed behavior touches P3 specialist and professional-evidence controls | **DEFER** |

## 5. Proposed Prompt Blocks for Future B-2.2-B

These blocks are design text only. They must not be applied without a new Project Owner decision binding exact files and pre-change hashes.

### 5.1 `matter-update` — trace to B-1 §6.1

```diff
+ Identify each affected Issue/Question/Claim/Request Right/Element/Legal Fact/Proof/Evidence/Defense/Rebuttal ref and its current version/status.
+ Record the new material's source and date, the candidate impact hypothesis, contradictory or adverse material, reopened gaps, and required qualified reviewer.
+ Preserve the prior record; do not silently overwrite, approve, reject, or reclassify existing analysis.
+ Require re-review before reusing an approval when authority, facts, evidence, adverse material, or purpose materially changes.
+ Return documentation-only update and re-review signals; do not update a runtime state, ledger, calendar, filing, or external system automatically.
```

### 5.2 `matter-briefing` — trace to B-1 §6.2

```diff
+ Preserve each referenced artifact's version and candidate/reviewed-approved/reviewed-rejected/superseded/unresolved status.
+ Present favorable and adverse facts, contrary authority, proof/evidence gaps, authority/source freshness, limitations, and pending human decisions together.
+ Mark any stale, reopened, missing, or purpose-limited approval and prevent it from appearing as an unqualified conclusion.
+ Do not convert a status summary into a legal opinion, claim selection, element conclusion, strategy decision, or predicted outcome.
```

### 5.3 `brief-section-drafter` — trace to B-1 §6.3

```diff
+ For any proposition intended for filing, advice, negotiation, client communication, or other consequential use, require an identified reviewed-approved ref for the same matter, version, scope, and purpose.
+ Preserve citations, authority/currentness notes, adverse material, unresolved qualifications, source links, and reviewer limitations from the approved analysis.
+ Flag or reject missing, stale, superseded, rejected, unresolved, cross-matter, or purpose-mismatched approval; do not silently upgrade it.
+ Do not choose a Claim, Request Right, Element conclusion, litigation theory, filing action, or legal strategy.
+ Keep every draft subject to qualified-lawyer review before external or consequential use.
```

No instruction block is proposed for `witness-trial-prep` under B-2.2-B.

## 6. Complete 24-Asset Disposition

| Asset | Class | Disposition | Reason |
|---|---|---|---|
| `brief-section-drafter` | Canonical | MODIFY | Downstream consequential-use gate in B-1 §6.3 |
| `chronology` | Canonical | NO CHANGE | P1 fixed owner; B-2.1 post-change baseline |
| `claim-chart` | Canonical | NO CHANGE | P1 fixed central owner; B-2.1 post-change baseline |
| `cold-start-interview` | Canonical | NO CHANGE | Environment/profile configuration, not matter lifecycle |
| `confidential-evidence-review` | Canonical | NO CHANGE | P3 specialist; explicitly excluded |
| `court-order-triage` | Canonical | NO CHANGE | Upstream procedural candidate supplier; no P2 ownership |
| `demand-draft` | Canonical | NO CHANGE | Separate pre-dispute communication flow; no B-1 P2 change point |
| `demand-intake` | Canonical | NO CHANGE | Separate upstream demand intake; no lifecycle ownership |
| `demand-received` | Canonical | NO CHANGE | Opponent-demand intake/routing; no lifecycle ownership |
| `evidence-preservation` | Canonical | NO CHANGE | P3 specialist; explicitly excluded |
| `matter-briefing` | Canonical | MODIFY | Lifecycle presentation gate in B-1 §6.2 |
| `matter-close` | Canonical | NO CHANGE | Outcome closure already has a manual gate; not dynamic C01 re-review |
| `matter-intake` | Canonical | NO CHANGE | P1 fixed initializer; B-2.1 post-change baseline |
| `matter-update` | Canonical | MODIFY | Lifecycle invalidation/re-review signal in B-1 §6.1 |
| `matter-workspace` | Canonical | DEFER | P4 persistence convention decision required |
| `oc-status` | Canonical | NO CHANGE | Adjacent counsel reporting; not a C01 lifecycle owner |
| `portfolio-status` | Canonical | NO CHANGE | Aggregate view; changing it before matter-level validation risks status flattening |
| `witness-trial-prep` | Canonical | DEFER | B-1 §6.4 overlaps P3 evidence/professional controls |
| `deposition-prep` | Compatibility alias | NO CHANGE | Routing only; no independent C01 fields |
| `legal-hold` | Compatibility alias | NO CHANGE | Routing only; no independent C01 fields |
| `privilege-log-review` | Compatibility alias | NO CHANGE | Routing only; no independent C01 fields |
| `subpoena-triage` | Compatibility alias | NO CHANGE | Routing only; no independent C01 fields |
| `customize` | Deprecated | NO CHANGE | Redirect only; separate deprecation governance |
| `docket-watcher` | Agent | DEFER | Agent/tool-scope change expressly excluded |

Additional system surface:

- `litigation-legal/CLAUDE.md`: **DEFER**. Existing distributed Human Review and China-law alignment remain controlling; any edit requires broad system-behavior review.

## 7. Conceptual Lifecycle Contract

This contract defines documentation semantics only. It is not JSON, YAML, a runtime schema, a database model, a Workflow, an MCP payload, or an API.

### 7.1 Common lifecycle input

| Field concept | Required meaning | Guardrail |
|---|---|---|
| Matter identity | Matter ref and isolation context | Reject/flag cross-matter use without explicit authorized transfer |
| Target ref | Exact C01 ref, artifact version and current status | Never resolve a ref by guess or silently substitute a newer version |
| Change source | Source identity, locator, date and provenance | Unsupported change cannot invalidate or approve analysis |
| Change type | Fact, authority, evidence, adverse material, purpose, procedural posture or reviewer decision | Classification remains candidate until reviewed |
| Impact hypothesis | Possible affected refs and reason | `matter-update` signals impact; P1 owners perform analysis |
| Review requirement | Required qualified role, scope, purpose and pending decision | No generating Skill may self-approve |

### 7.2 Conceptual outputs

| Output | Producer | Required semantics | Prohibited effect |
|---|---|---|---|
| Update/reopen signal | `matter-update` | Source, affected refs, candidate impact, reopened gaps, reviewer required | No overwrite, runtime transition or automatic downstream action |
| Lifecycle briefing | `matter-briefing` | Version/status, favorable/adverse material, freshness, gaps, pending decision, limitations | No opinion, prediction or silent status upgrade |
| Drafting gate result | `brief-section-drafter` | Approved-ref match or explicit block/flag with reason | No theory selection or use of unreviewed proposition as approved |
| Human decision | Qualified reviewer | Target/version, decision, date, scope, purpose and limitations | No permission outside recorded scope or automatic application |

### 7.3 Status handling

The existing P1 documentation labels remain unchanged:

`candidate`, `reviewed-approved`, `reviewed-rejected`, `superseded`, `unresolved`.

Lifecycle consumers may preserve and display these labels. They must not create a runtime state machine, add new automatic transitions, or treat a label as authority to file, advise, send, disclose, negotiate, or deploy.

## 8. Human Review Integration

The controlling pattern remains:

`Candidate Analysis → Qualified Human Review → Approval Decision → Optional Application`

| Gate | Trigger | Required manual decision | Failure behavior |
|---|---|---|---|
| G1 — Material-change review | New fact, authority, evidence, adverse material, purpose or posture may affect a ref | Decide affected scope and whether P1 analysis must reopen | Keep prior record; mark candidate impact and pending review |
| G2 — Briefing review | Summary will be relied on for management, client or case decision | Confirm status, sources, freshness, adverse material and limitations | Display unresolved/stale state; do not flatten to conclusion |
| G3 — Drafting input review | Proposition will enter consequential drafting | Confirm same matter/version/scope/purpose approval | Block or flag the proposition; do not invent approval |
| G4 — Application review | Filing, advice, negotiation, communication or other use is proposed | Qualified lawyer decides whether and how to apply | No automatic action; application remains optional |

## 9. Overlap and Isolation Analysis

| Boundary | Overlap risk | Required isolation |
|---|---|---|
| `matter-update` vs `chronology` | Duplicate fact creation | Update references sources and affected Legal Fact refs; chronology remains fact-normalization owner |
| `matter-update` vs `claim-chart` | Second analytical owner | Update emits impact/reopen signals; claim-chart remains Claim/Element/Proof/Defense owner |
| `matter-briefing` vs P1 | Status flattened into conclusion | Briefing consumes refs and preserves all states/limitations; it does not reclassify |
| `brief-section-drafter` vs P1 | Drafting chooses theory | Drafter gates on reviewed refs; it does not select or approve Claim/Right/Element |
| `witness-trial-prep` vs P3 | Evidence, credibility, confidentiality or admissibility logic duplicated | Defer; no B-2.2-B change proposed |
| Lifecycle vs Agent | Autonomous deadlines/actions | `docket-watcher` remains unchanged and outside the lifecycle package |
| Lifecycle vs persistence/runtime | Prompt labels become stored state or transitions | No schema, Workflow, ledger write, database or automatic transition |

The lifecycle scope is isolatable without any P3, P4, Agent, Workflow, MCP, code, schema or system-instruction change.

## 10. Minimal Future B-2.2-B Whitelist

If Project Owner later authorizes implementation, the recommended exact whitelist is:

1. `litigation-legal/skills/matter-update/SKILL.md` — pre-change SHA-256 `04FB6C9D3A930C17ACD50957E9FD66A2821FAF5B4FE6FF03012E17EB1F94A2C0`
2. `litigation-legal/skills/matter-briefing/SKILL.md` — pre-change SHA-256 `6064D4BFB3AE41F88EDF0D94628131AF6CB8C16EB8EEDD7BC0928EF8212C68B6`
3. `litigation-legal/skills/brief-section-drafter/SKILL.md` — pre-change SHA-256 `8FDC03E52A6BA4FF34DAE6890EDBA8A657EF2B455EDBC8C061FD4A0ACC664894`

Recommended implementation order: `matter-update → matter-briefing → brief-section-drafter`.

No other path is proposed for B-2.2-B. Approval of this inventory would not itself authorize those edits.

## 11. Proposed Acceptance Criteria for B-2.2-B

| AC | Future criterion |
|---|---|
| AC-B22B-001 | Revised Handoff and all fixed input hashes match before editing |
| AC-B22B-002 | All three whitelist files match the pre-change hashes in §10 |
| AC-B22B-003 | Only those three files change; `witness-trial-prep` and every other asset remain unchanged |
| AC-B22B-004 | Changes are additive instruction text traceable to B-1 §§6.1–6.3 and this inventory §5 |
| AC-B22B-005 | `matter-update` signals impact/re-review but does not overwrite P1 analysis or persist runtime state |
| AC-B22B-006 | `matter-briefing` preserves version/status, adverse material, freshness, gaps and limitations |
| AC-B22B-007 | `brief-section-drafter` requires scope-matched reviewed refs for consequential propositions and retains lawyer review |
| AC-B22B-008 | No automatic opinion, claim/theory selection, element conclusion, prediction, filing, sending or application appears |
| AC-B22B-009 | P1, P3, P4, Agent, CLAUDE, aliases, Plugin, MCP, Workflow, schema, code and D1-D6 remain unchanged |
| AC-B22B-010 | `git diff --check` passes, staging remains empty, before/after hashes and rollback evidence are recorded |

## 12. Future Validation Scenarios (Not Executed)

| Scenario | Expected behavior |
|---|---|
| New adverse document affects an approved Element | Update emits candidate impact and re-review request; prior approval is preserved, not reused silently |
| Controlling authority may be stale | Briefing shows freshness issue and pending review; drafter blocks/flags consequential reliance |
| A reviewed-rejected theory remains in history | Briefing preserves rejected status; drafter does not present it as approved |
| Approval belongs to another matter or purpose | Drafter flags scope mismatch and does not use it as authority |
| Summary contains favorable and adverse material | Both appear with sources, gaps and limitations; no predicted outcome |
| Candidate status supplied for external pleading text | Consequential proposition is blocked/flagged pending qualified-lawyer approval |
| Witness preparation requests evidence/confidentiality conclusions | Remains outside B-2.2-B; route to separately governed review rather than expanding the Skill |

## 13. Risk Register

| ID | Risk | Mitigation/gate |
|---|---|---|
| L01 | Update silently overwrites approved/rejected history | Add append-only language; emit signal only; preserve prior version/status |
| L02 | Lifecycle labels become runtime transitions | State explicitly that labels are documentation metadata; prohibit Workflow/schema/action changes |
| L03 | Briefing flattens uncertainty or adverse material | Require status, freshness, adverse material, gaps and limitations together |
| L04 | Drafter treats reviewed content as universally approved | Match matter, version, scope and purpose; qualified lawyer reviews the final draft |
| L05 | P2 duplicates P1 analysis | Keep update/presentation/drafting roles consumer-only; P1 owners remain controlling |
| L06 | Witness preparation crosses into P3 | Defer the file; exclude it from the minimal whitelist |
| L07 | Alias or aggregate reporting behavior regresses | Leave aliases, `portfolio-status`, `oc-status` and downstream adjacent Skills unchanged |
| L08 | China-law freshness/provenance is lost | Preserve authority hierarchy, jurisdiction, temporal applicability, source and verification limitations |

## 14. Current State and Next Gate

```text
C01-II-B-2.2-A Lifecycle Target Inventory: COMPLETED / REVIEW PENDING
C01-II-B-2.2-B Lifecycle Skill Modification: NOT AUTHORIZED
C01-II-B-2.3 Evidence Specialist: NOT AUTHORIZED
C01-II-B-2.4 Deferred surfaces: NOT AUTHORIZED
C01-II-B-3 Validation execution: NOT AUTHORIZED
Files under litigation-legal changed by B-2.2-A: NONE
Next: Architecture Coordinator Review → Project Owner Decision
```
