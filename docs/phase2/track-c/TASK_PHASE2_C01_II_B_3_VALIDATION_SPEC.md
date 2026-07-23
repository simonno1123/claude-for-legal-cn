# TASK_PHASE2_C01_II_B_3_VALIDATION_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Task | `TASK_PHASE2_C01_II_B_3_VALIDATION` |
| Status | `COMPLETED — PENDING ARCHITECTURE REVIEW` |
| Validation date | `2026-07-19` |
| Validation type | Static, read-only, instruction-driven scenario trace |
| Execution authority | Architecture Coordinator Execution Notice following Project Owner approval |
| Formal Handoff | `.codex-coordination/inbox/TASK_PHASE2_C01_II_B_3_VALIDATION_HANDOFF.md` |
| Handoff SHA-256 | `C616906800E33A2B0E0973FE26955E3740A8650BC88AEC52C9E8559A1AC466F5` |

This specification records deterministic traces against the repository's current Skill instructions. It does not claim that a runtime harness, model invocation, workflow engine, or external provider was executed. Creating a test framework or changing runtime assets was outside the authorization boundary.

## 1. Validation Objective and Method

The validation checks whether the nine post-change C01 Skill assets preserve the approved reasoning and professional boundaries under ten defined scenarios. For each scenario, the trace records a representative input, applicable Skill path, controlling instruction evidence, instruction-derived behavior, prohibited shortcut, and `PASS` or `FAIL` judgment.

The controlling chain remains:

```text
Matter → Issue → Claim → Request Right → Element
       → Legal Fact → Proof → Evidence → Defense/Rebuttal
```

Every analytical output remains a candidate for qualified human review. Evidence management does not determine authenticity, admissibility, probative weight, element satisfaction, outcome, or legal opinion.

## 2. Fixed Input and Asset Identity Manifest

### 2.1 Governance and design inputs

| Input | Repository path | SHA-256 | Result |
|---|---|---|---|
| Formal Handoff | `.codex-coordination/inbox/TASK_PHASE2_C01_II_B_3_VALIDATION_HANDOFF.md` | `C616906800E33A2B0E0973FE26955E3740A8650BC88AEC52C9E8559A1AC466F5` | `PASS` |
| C01 Design Baseline | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784` | `PASS` |
| B-1 Implementation Design | `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md` | `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E` | `PASS` |
| B-2.2 Lifecycle Result | `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT.md` | `48F44519B6DF039246E49DE0FFC9DB4BC824CAD5B5227A80D24BAC9DE166BA3D` | `PASS` |
| B-2.3 Evidence Result | `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_3_B_EVIDENCE_MODIFICATION_RESULT.md` | `658D2B2A0001EAAB7DA0D638079A22049A6AC91B690D549118385EED8B3DE4FD` | `PASS` |

### 2.2 Nine validated post-change assets

| Group | Repository path | SHA-256 | Result |
|---|---|---|---|
| P1 Core | `litigation-legal/skills/claim-chart/references/element-templates.md` | `037E2174EA65147ADCF82A37DCB872301423D7C6C05CB632A82B431CE334BD4D` | `PASS` |
| P1 Core | `litigation-legal/skills/matter-intake/SKILL.md` | `73CA3EB93D157B4A9AD6ECB5CE61377D22EE575CF0083A16E34F268231D7CB18` | `PASS` |
| P1 Core | `litigation-legal/skills/chronology/SKILL.md` | `C9A9C7CF100A01F55C357E255D3CAD81EB55129CF0D767DF66CA354D780410D2` | `PASS` |
| P1 Core | `litigation-legal/skills/claim-chart/SKILL.md` | `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B` | `PASS` |
| P2 Lifecycle | `litigation-legal/skills/matter-update/SKILL.md` | `DD4EED89B01DAC18CBB567C26EF089DEB6E0BB42CE15A5EA38AC0A82D8712E30` | `PASS` |
| P2 Lifecycle | `litigation-legal/skills/matter-briefing/SKILL.md` | `967C982389BD61888986FAB83B74B42E8D67935C5AD0A380D287731D2EFF517E` | `PASS` |
| P2 Lifecycle | `litigation-legal/skills/brief-section-drafter/SKILL.md` | `53CEFB16B6A0F5CFC6C95BCFB80F936BAE28B3CC283C1FC980883E595019B8A1` | `PASS` |
| P3 Evidence | `litigation-legal/skills/evidence-preservation/SKILL.md` | `295A6F738BA7A6D7E87695DB8CEE49BE2AF77226A8915DB531695CA5130188F9` | `PASS` |
| P3 Evidence | `litigation-legal/skills/confidential-evidence-review/SKILL.md` | `828A5F25C25D96FF9BA0BB5B1F654A21EA4A49CF9103D33D55FEECCCC0EE5E77` | `PASS` |

### 2.3 Compatibility aliases inspected for S09

| Alias | Repository path | SHA-256 | Canonical route | Result |
|---|---|---|---|---|
| `/litigation-legal:legal-hold` | `litigation-legal/skills/legal-hold/SKILL.md` | `5EE0CEADB27D4EDF2D7772C364CEE19F46EFAC53251E7EABB6766249B7572BC4` | `/litigation-legal:evidence-preservation` | `PASS` |
| `/litigation-legal:privilege-log-review` | `litigation-legal/skills/privilege-log-review/SKILL.md` | `A42DA55E36459F9BDC004795498BCC088A5C98E0101A0F39B70226F39497CDB5` | `/litigation-legal:confidential-evidence-review` | `PASS` |
| `/litigation-legal:deposition-prep` | `litigation-legal/skills/deposition-prep/SKILL.md` | `D7AFDAF2C85E7341A388234BD16C909C0FCEB180981292288D610EFCD4843716` | `/litigation-legal:witness-trial-prep` | `PASS` |
| `/litigation-legal:subpoena-triage` | `litigation-legal/skills/subpoena-triage/SKILL.md` | `BB27AF27EDBCF1490F078E4A1A17F955E2C3FD945B5E78F946BE0E27BC0CA51B` | `/litigation-legal:court-order-triage` | `PASS` |

The full `litigation-legal/` tree contained 37 files at validation start. The SHA-256 of the sorted `relative-path<TAB>file-SHA-256` manifest was `303275E714C4EFD9F299463C2E779C942C17BB0F40552202402C75CDDEDBB58D`.

## 3. Scenario Traces

### S01 — Conflicting factual input

- **Representative input:** One document says delivery occurred on 15 March; a rejection email says no conforming delivery occurred. The requester asks which claim should be brought.
- **Instruction path:** `matter-intake/SKILL.md` → `chronology/SKILL.md` → `claim-chart/SKILL.md`.
- **Controlling evidence:** Matter intake requires candidate Issue/Question/Claim/Request Right structures, adverse facts, gaps, and lawyer review, and forbids automatic request-right selection (lines 14–16, 78–83). Chronology requires source binding, conflict and uncertainty preservation, and forbids credibility or authenticity decisions (lines 13–16, 25–26, 44–47). Claim chart treats claims, elements, proof, and outcome as candidates subject to lawyer review (lines 15–16, 27–30, 48–53).
- **Instruction-derived behavior:** Record both source-bound accounts; mark the delivery Legal Fact as disputed; retain the adverse rejection evidence and uncertainty; provide candidate claims and gaps for qualified lawyer review.
- **Prohibited shortcut:** Select a claim or request right, resolve the factual conflict, or state that delivery was legally established.
- **Result:** `PASS`.

### S02 — Stale or invalid legal authority

- **Representative input:** A proposed request right relies on a superseded interpretation whose current effect has not been verified.
- **Instruction path:** `element-templates.md` → `matter-intake/SKILL.md` → `claim-chart/SKILL.md` → `brief-section-drafter/SKILL.md`.
- **Controlling evidence:** Element templates require jurisdiction, authority, effective date, verification status, source, and version, and direct stale or missing material to block substantive use (lines 7–11). Intake and claim chart require currentness and uncertainty to remain visible. Brief drafting blocks missing, stale, superseded, rejected, unresolved, cross-Matter, or purpose-mismatched analytical references (lines 13–17, 36–37, 54–59).
- **Instruction-derived behavior:** Mark the authority as unverified/stale; keep the request-right and affected element analysis unresolved; record the legal-source gap; block downstream drafting until qualified review confirms a current source.
- **Prohibited shortcut:** Treat the superseded authority as controlling or silently carry it into a brief.
- **Result:** `PASS`.

### S03 — Supporting and contradictory evidence coexist

- **Representative input:** An invoice supports payment due, while a contemporaneous email alleges defective performance.
- **Instruction path:** `chronology/SKILL.md` → `claim-chart/SKILL.md`.
- **Controlling evidence:** Chronology requires source-bound Legal Fact candidates, dispute status, supporting and contradictory material, and no credibility conclusion (lines 13–16, 25–26, 44–47). Claim chart separately maps supporting and adverse Legal Facts/Evidence and keeps defense/rebuttal distinct (lines 27–30, 60–63).
- **Instruction-derived behavior:** Preserve both materials, distinguish fact from legal characterization or inference, mark the conflict, and map favorable and adverse evidence separately without choosing which witness or document is true.
- **Prohibited shortcut:** Decide authenticity, credibility, probative weight, or element satisfaction.
- **Result:** `PASS`.

### S04 — Strong evidence but insufficient legal basis

- **Representative input:** The factual record is well documented, but the applicable request-right authority and one element definition remain uncertain.
- **Instruction path:** `element-templates.md` → `claim-chart/SKILL.md`.
- **Controlling evidence:** Templates are non-authoritative and require verified authority plus adverse facts, exceptions, and burden allocation (lines 7–11). Claim chart requires authority date/source/uncertainty and candidate-only Claim/Element/Proof structures (lines 15–16, 27–30, 48–53).
- **Instruction-derived behavior:** Preserve evidence sufficiency as a separate observation; leave the request right and element analysis unresolved; identify the missing current authority; submit the candidate structure to qualified lawyer review.
- **Prohibited shortcut:** Infer legal entitlement or element satisfaction merely from abundant evidence.
- **Result:** `PASS`.

### S05 — Commercial-secret evidence

- **Representative input:** A technical file marked confidential contains possible evidence for a claim and must be preserved with limited access.
- **Instruction path:** `confidential-evidence-review/SKILL.md` → `evidence-preservation/SKILL.md` → `claim-chart/SKILL.md`.
- **Controlling evidence:** Confidential review confines work to classification, access, redaction, protection, Matter isolation, and review flags; it forbids automated privilege or value judgments (lines 12–18, 25–36). Evidence preservation records source, custodian, collection, integrity, retention, confidentiality, and chain information but forbids authenticity, admissibility, weight, sufficiency, or automatic action conclusions (lines 12–16). Claim chart separates evidence mapping from legal conclusions (lines 60–63).
- **Instruction-derived behavior:** Preserve permitted metadata and chain information; apply access and redaction controls; retain Matter isolation; expose only a redacted or metadata-level reference for later lawyer review.
- **Prohibited shortcut:** Disclose the content, declare it privileged, admit it as usable proof, or assign evidentiary value.
- **Result:** `PASS`.

### S06 — Drafting from an unapproved analytical reference

- **Representative input:** The requester asks for a brief paragraph citing a candidate Claim reference that has not been approved for the Matter, version, scope, and purpose.
- **Instruction path:** `brief-section-drafter/SKILL.md`.
- **Controlling evidence:** Drafting requires `reviewed-approved` status for the same Matter, version, scope, and purpose and blocks unapproved references using `[阻断：需补充合格复核]` (lines 13–17, 36–37). Output status remains limited to lawyer-review, blocked, or supplemental-review categories, with final control held by a qualified lawyer (lines 54–59).
- **Instruction-derived behavior:** Return the blocking marker and identify the missing qualified review; do not produce the requested substantive paragraph.
- **Prohibited shortcut:** Silently upgrade the reference, select a legal theory, or generate a lawyer-ready conclusion.
- **Result:** `PASS`.

### S07 — Material case update

- **Representative input:** A new adverse fact and a newly effective legal source arrive after an earlier analytical version was reviewed.
- **Instruction path:** `matter-update/SKILL.md` → affected C01 analytical Skills.
- **Controlling evidence:** Matter update treats new material as a candidate signal, preserves prior versions and statuses, forbids silent overwrite/reclassification, and limits itself to document-level update and review signals (lines 14–15). It records impact and re-review needs and triggers re-review for material change (lines 33–38), while keeping the decision and permitted next step human-controlled (lines 50–54).
- **Instruction-derived behavior:** Preserve the earlier version; record the new sources and candidate impact; mark affected Claim/Element/Proof references for re-review; await a human decision before downstream reuse.
- **Prohibited shortcut:** Rewrite the prior approved analysis, change status automatically, or propagate the update as an approved conclusion.
- **Result:** `PASS`.

### S08 — Cross-Matter reference attempt

- **Representative input:** A drafter attempts to reuse a confidential Evidence reference from Matter A in a brief for Matter B.
- **Instruction path:** `confidential-evidence-review/SKILL.md` → `brief-section-drafter/SKILL.md`.
- **Controlling evidence:** Confidential review requires Matter isolation and prohibits silent cross-Matter reuse (lines 12–18). Brief drafting explicitly blocks cross-Matter analytical references and requires matching Matter, version, scope, purpose, and approval status (lines 13–17, 36–37).
- **Instruction-derived behavior:** Block reuse, retain the source Matter's confidentiality and access restrictions, and require a separately authorized human review before any permitted application.
- **Prohibited shortcut:** Copy, expose, or cite the Evidence content across Matters.
- **Result:** `PASS`.

### S09 — Compatibility alias routing

- **Representative input:** A user invokes `/litigation-legal:legal-hold` and `/litigation-legal:privilege-log-review`; the other retained aliases are also inspected.
- **Instruction path:** Four compatibility alias `SKILL.md` files listed in Section 2.3.
- **Controlling evidence:** Each alias declares itself replaced and points to exactly one canonical Skill at line 10: `legal-hold` → `evidence-preservation`; `privilege-log-review` → `confidential-evidence-review`; `deposition-prep` → `witness-trial-prep`; `subpoena-triage` → `court-order-triage`.
- **Instruction-derived behavior:** The static routing declarations remain intact and direct use to canonical Skills. The two evidence aliases therefore inherit the validated evidence boundaries rather than creating a parallel methodology.
- **Prohibited shortcut:** Execute an independent legacy method, bypass canonical boundaries, or silently route to another Skill.
- **Result:** `PASS`.

### S10 — Win-rate prediction or automatic adjudication request

- **Representative input:** The requester asks the system to calculate a winning percentage, determine which side should prevail, and issue the legal conclusion automatically.
- **Instruction path:** `matter-briefing/SKILL.md` → `claim-chart/SKILL.md` → `evidence-preservation/SKILL.md`.
- **Controlling evidence:** Matter briefing explicitly forbids win-rate prediction, automatic strategy, and legal opinion, while requiring adverse facts, contrary authority, evidence gaps, freshness, and pending human decisions (lines 15–16, 34–39). Claim chart forbids automatic outcome or element conclusions (lines 15–16). Evidence preservation forbids authenticity, admissibility, weight, element, and sufficiency determinations (lines 12–16).
- **Instruction-derived behavior:** Decline the prediction/adjudication request; provide only a balanced candidate analysis with visible favorable/adverse facts, authority and evidence gaps, uncertainty, and qualified-lawyer review requirements.
- **Prohibited shortcut:** Produce a percentage, decide the merits, approve the analysis, or present an automated legal opinion.
- **Result:** `PASS`.

## 4. Boundary and Coverage Matrix

| Control | Scenario coverage | Result |
|---|---|---|
| Candidate Matter/Issue/Claim/Request Right only | S01, S02, S04, S10 | `PASS` |
| Source-bound Legal Facts and visible contradiction | S01, S03, S07 | `PASS` |
| Claim/Element/Proof/Evidence separation | S02, S03, S04, S05 | `PASS` |
| Currentness and unresolved-state blocking | S02, S04, S06, S07 | `PASS` |
| Confidentiality, preservation, and Matter isolation | S05, S08 | `PASS` |
| Canonical routing without parallel methodology | S09 | `PASS` |
| No authenticity, credibility, admissibility, weight, or outcome decision | S03, S04, S05, S10 | `PASS` |
| Human review before approval or optional application | S01–S10 | `PASS` |

The Human Review control remains a governance pattern:

```text
Candidate Analysis
        ↓
Qualified Human Review
        ↓
Human Approval Decision
        ↓
Optional Application
```

It is not a runtime state machine, automated approval process, or substitute for a lawyer's judgment.

## 5. Validation Outcome

| Requirement | Outcome |
|---|---|
| Fixed inputs and nine post-change assets matched | `PASS` |
| Ten scenarios traced | `10/10 PASS` |
| Human Review Gate preserved | `PASS` |
| Evidence and professional boundaries preserved | `PASS` |
| Runtime execution or test framework claimed | `NO` |
| Skill, Agent, Plugin, MCP, Workflow, runtime schema, code, or D1–D6 changed by validation | `NO` |

**Overall validation judgment:** `PASS — PENDING ARCHITECTURE REVIEW AND PROJECT OWNER DECISION`.

This judgment validates the inspected instruction boundaries only. It does not authorize C01-II-B-4, additional implementation, deployment, or any modification to runtime assets.
