# TASK_PHASE2_C01_II_B_2_3_A_EVIDENCE_TARGET_INVENTORY

## Status

`DONE — Read-only Inventory; Pending Architecture Coordinator Review`

- Inventory date: `2026-07-19`
- Executor: `Codex`
- Authorized stage: `C01-II-B-2.3-A Evidence Target Inventory and Scope Binding`
- Implementation status: `NOT AUTHORIZED`

## 1. Purpose and Boundary

This document maps the C01 Evidence layer onto four existing `litigation-legal` Skill candidates. It records current identities, responsibilities, gaps, overlap risks and a minimal future whitelist proposal.

This is documentation-only engineering analysis. It does not modify any Skill, define a runtime schema, create an evidence repository, determine evidence usability, or authorize B-2.3-B.

## 2. Authorization and Input Identity

### 2.1 Governance identity

| Record | Repository path | SHA-256 | Status |
|---|---|---|---|
| Approved Handoff | `.codex-coordination/inbox/TASK_PHASE2_C01_II_B_2_3_EVIDENCE_HANDOFF.md` | `D3A2ACFC1D90F6C38CBD2BD13A86FE5784F6683DDB3B52FE706E12C87920DBD7` | Exact match |
| Architecture Review | `.codex-coordination/reviews/TASK_PHASE2_C01_II_B_2_3_EVIDENCE_HANDOFF_REVIEW.md` | `D843B22EED34CF42AC9597BCF11DA950DF0D6EA7420980B55E006B1E9C5CD70D` | `PASS`, Grade `A` |
| Project Owner Decision | `.codex-coordination/decisions/TASK_PHASE2_C01_II_B_2_3_EVIDENCE_HANDOFF_DECISION.md` | `00B7D7AFD62F8519B713996AFB3DD95A860D570CCF8FDCFE115C95FBB4D2B24F` | `ACCEPTED`, B-2.3-A only |

### 2.2 Fixed input verification

| Input | Repository path | Required and actual SHA-256 | Result |
|---|---|---|---|
| C01 Design Baseline v0.2 | `docs/phase2/track-c/TASK_PHASE2_C01_LITIGATION_REASONING_FRAMEWORK_DESIGN_v0.2.md` | `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784` | PASS |
| C01-II-A Skill Design Mapping | `docs/phase2/track-c/TASK_PHASE2_C01_II_A_SKILL_DESIGN_MAPPING.md` | `8E52FB0F5DC13DD82B610E351653F11DA16178D6073621C0D773136DA9695870` | PASS |
| C01-II-B-1 Design | `docs/phase2/track-c/TASK_PHASE2_C01_II_B_IMPLEMENTATION_DESIGN.md` | `E02165FD2872ECE840652EA6F2E8AE3EE4ADBD7A6D12A273F8C765F06F427A7E` | PASS |
| B-2.2-B Lifecycle Modification Result | `docs/phase2/track-c/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT.md` | `48F44519B6DF039246E49DE0FFC9DB4BC824CAD5B5227A80D24BAC9DE166BA3D` | PASS |
| B-2.2-B Lifecycle Result Record | `.codex-coordination/outbox/TASK_PHASE2_C01_II_B_2_2_B_LIFECYCLE_MODIFICATION_RESULT_RECORD.md` | `E45C1EF28CFB2A9A80D2925618587122D2B917C92FC68E14E5110B3AFD78EFAB` | PASS |

The four P1 Core and three P2 Lifecycle files also matched every post-change hash fixed by Handoff §4. No baseline drift was found.

## 3. Candidate Inventory

| Candidate and exact path | Current SHA-256 | Current role | Identified gap | Proposed instruction treatment | Isolation / overlap risk | Recommendation |
|---|---|---|---|---|---|---|
| `litigation-legal/skills/confidential-evidence-review/SKILL.md` | `96234688F60DB1AC44C1FBC3156F4D68C046D38B6EE6680FA29734938D36F209` | Specialist review of commercial secrets, personal information, state secrets, minors' information, cross-border data, redaction and protected submission | Does not explicitly bind outputs to Matter-scoped Evidence refs, access controls, source linkage, permitted-metadata limits or reviewer flags; approved/reviewed status could otherwise be misread as permission to disclose or use | Add only the B-1 §7.2 protection-preserving block in §5.2 | High sensitivity: integration must not weaken confidentiality, imply privilege, or decide disclosure/filing/use | **MODIFY** |
| `litigation-legal/skills/evidence-preservation/SKILL.md` | `A9E15EEC0FD36CBA03930FDB8FD1A903B60248319AD82F78B3ACF259E608F4EA` | Specialist design for retention scope, electronic-data integrity reinforcement, PRC litigation evidence preservation and arbitration-to-court preservation routing | Does not explicitly treat Evidence/Legal Fact refs as contextual identifiers only; source, custodian, collection, integrity, retention and chain-of-custody context are not bound together; no express prohibition on authenticity, admissibility, weight or sufficiency decisions | Add only the B-1 §7.1 preservation-context block in §5.1 | Medium/high: must not become a runtime legal hold, evidence repository, admissibility engine or merits owner | **MODIFY** |
| `litigation-legal/skills/witness-trial-prep/SKILL.md` | `14EAFE498D62CD3BF1796424D417B5C090022D0F60309994404BEDD3933A197A` | Downstream preparation of proof subjects, claim/defense links, evidence links, questions and high-risk hearing issues | It does not yet require reviewed Proof/Evidence refs, supporting/contradictory Legal Facts, adverse/confidentiality flags, or explicit no-credibility/no-coaching/no-admissibility boundaries | No B-2.3-B block. Preserve the B-1 §6.4 proposal for a separately scoped downstream/lifecycle task, shown in §5.3 | High role collision: it is a hearing-preparation consumer, not one of the two P3 evidence specialists; including it would expand B-2.3 beyond B-1 §13.4 | **DEFER** |
| `litigation-legal/skills/claim-chart/SKILL.md` | `172C0D28AE870972BC737A5ED0636F8322E75F6BB9FA153B5CCF2287BD5AFD6B` | Adopted P1 central owner for Claim, Request Right, Element, Proof, Evidence and Defense/Rebuttal mapping, including evidence three-property review, gaps and human-review status | Specialist metadata such as custody, integrity and access restrictions is intentionally supplied by evidence specialists; duplicating it here would blur ownership | No instruction block proposed. Consume specialist context through references after separate approval and validation | High duplication and baseline-drift risk because this file already carries an adopted P1 post-change identity | **NO CHANGE** |

## 4. Minimal Future B-2.3-B Whitelist Proposal

If and only if the Project Owner separately approves B-2.3-B, the smallest isolated change set is:

| Seq | Proposed target | Bound pre-change SHA-256 | Future action |
|---|---|---|---|
| 1 | `litigation-legal/skills/evidence-preservation/SKILL.md` | `A9E15EEC0FD36CBA03930FDB8FD1A903B60248319AD82F78B3ACF259E608F4EA` | Additive instruction-only modification traced to B-1 §7.1 |
| 2 | `litigation-legal/skills/confidential-evidence-review/SKILL.md` | `96234688F60DB1AC44C1FBC3156F4D68C046D38B6EE6680FA29734938D36F209` | Additive instruction-only modification traced to B-1 §7.2 |

No other target is recommended for B-2.3-B. In particular:

- `claim-chart/SKILL.md` remains the approved central analytical mapper and should not be reopened.
- `witness-trial-prep/SKILL.md` remains deferred to a separately reviewed downstream/lifecycle package.
- Agents, `CLAUDE.md`, persistence layout, databases, schemas, MCP, Workflow, Plugin and D1-D6 remain excluded.

## 5. Proposed Prompt Blocks

These blocks are design text only. They must not be applied without a new Project Owner decision binding the exact target paths and pre-change hashes.

### 5.1 `evidence-preservation` — trace to B-1 §7.1

```diff
+ Accept reviewed/candidate Evidence and Legal Fact refs only as contextual identifiers for preservation scope.
+ Preserve source, custodian, collection, integrity, retention, privilege/confidentiality, and chain-of-custody context as applicable.
+ Do not decide probative value, authenticity, admissibility, element satisfaction, or legal sufficiency.
```

Placement should be limited to the existing instruction layer. Existing PRC litigation/arbitration preservation routes, original-carrier safeguards and the prohibition on importing US legal-hold effects must remain authoritative.

### 5.2 `confidential-evidence-review` — trace to B-1 §7.2

```diff
+ Accept reviewed/candidate Evidence refs while preserving matter isolation, access controls, confidentiality and privilege handling.
+ Return only permitted metadata or redacted findings with source linkage and reviewer flags.
+ Do not weaken protective controls or infer that restricted evidence may be used in analysis, disclosure, filing, or advice.
```

Here, “privilege handling” must remain subordinate to the Skill's existing PRC rule that no common-law evidentiary privilege may be claimed against lawful court, tribunal or authority requirements. It does not create a privilege log or withholding right.

### 5.3 `witness-trial-prep` — deferred B-1 §6.4 text, not a B-2.3-B proposal

```diff
+ Link preparation topics to reviewed Proof and Evidence refs and the Legal Facts they may support or contradict.
+ Surface evidentiary, credibility, privilege, confidentiality, and adverse-material flags for lawyer handling.
+ Do not decide witness credibility, coach false testimony, determine admissibility, or replace trial counsel judgment.
```

This block is recorded solely to explain the observed gap and phase separation. It is not in the proposed B-2.3-B whitelist.

### 5.4 `claim-chart` — no prompt block

No change is proposed. The adopted P1 content already:

- maps supporting and contradictory Evidence refs to candidate Elements, Legal Facts, Defenses and Rebuttals;
- records three-property review, proof purpose, gaps and status;
- prohibits automated evidence-usability, element-satisfaction and outcome decisions; and
- requires qualified human review.

Adding P3 custody, preservation or confidentiality ownership here would duplicate specialist responsibilities and weaken isolation.

## 6. Conceptual Input / Output Boundary

This table describes reviewable documentation semantics only. It is not JSON, YAML, database, Workflow, MCP or runtime-schema design.

| Specialist | Contextual input only | Reviewable output | Must never infer or trigger |
|---|---|---|---|
| Evidence preservation | Matter-bound Evidence/Legal Fact ref, version/status, source, custodian, location/carrier, collection context, retention need, integrity and confidentiality flags | Preservation-scope notes, authentic-carrier/integrity safeguards, chain-of-custody gaps, PRC court/arbitration route notes and reviewer flags | Authenticity finding, admissibility, probative weight, legal sufficiency, element satisfaction, repository write or automated preservation action |
| Confidential evidence review | Matter-bound Evidence ref, version/status, source link, access classification, commercial-secret/personal-information/state-secret/minor/cross-border flags and stated review purpose | Permitted metadata, redacted finding, access/protective-measure recommendation, source linkage, limitations and reviewer flags | Permission to disclose, file, advise or reuse; common-law privilege; merits/admissibility decision; cross-Matter transfer |

The specialists do not own the Claim/Element/Evidence merits graph. `claim-chart` remains the candidate mapping owner; the specialists provide constrained preservation or protection context only.

## 7. PRC Evidence and Professional Boundaries

- Statutes, judicial interpretations and applicable PRC evidence rules remain primary. Case materials may calibrate reasoning but are not common-law precedent and do not replace mandatory rules.
- Original carriers, source/custodian information, formation and collection context, hashes/timestamps where available, and integrity gaps should be preserved as review facts—not converted into authenticity conclusions.
- Personal information, commercial secrets, state secrets, minors' information and cross-border data require purpose limitation, least-necessary disclosure, redaction/protected-submission analysis and qualified review.
- Evidence “真实性、合法性、关联性”, admissibility, weight, burden discharge and legal sufficiency remain candidate legal assessments for qualified lawyers or the competent adjudicative body.
- No credibility score, admissibility score, outcome score, automatic legal opinion or evidence-use decision is permitted.

## 8. Human Review Control

The future design must preserve:

`Candidate Evidence Context → Qualified Human Review → Scoped Decision → Optional Application`

- Candidate/reviewed labels are documentation governance metadata, not runtime states.
- Review approval must identify the Matter, ref/version, reviewer, purpose, scope, limitations and date.
- A preservation or confidentiality recommendation does not approve evidence use.
- Restricted, stale, cross-Matter, incomplete-chain or purpose-mismatched material must remain flagged or blocked for consequential use.

## 9. Proposed B-2.3-B Acceptance Criteria

| ID | Proposed criterion |
|---|---|
| AC-B23B-001 | Recompute all B-2.3-A fixed inputs and bind this Inventory, its Result and the separately approved B-2.3-B Handoff exactly. |
| AC-B23B-002 | Immediately before editing, both targets match the pre-change hashes in §4; any drift blocks execution. |
| AC-B23B-003 | Modify only the two whitelisted Skill files; changes are additions-only and frontmatter remains byte-for-byte unchanged. |
| AC-B23B-004 | Every added instruction traces to B-1 §§7.1–7.2 and the blocks in §5; specialist protective functions remain intact. |
| AC-B23B-005 | Preservation refs remain contextual only; no authenticity, admissibility, weight, sufficiency or element decision is introduced. |
| AC-B23B-006 | Confidential-review integration preserves Matter isolation, access limits, source linkage, permitted-metadata/redaction boundaries and qualified reviewer flags. |
| AC-B23B-007 | No common-law privilege effect, automated action, database, repository, schema, Agent, MCP, Workflow, Plugin, `CLAUDE.md`, P4 or D1-D6 change is introduced. |
| AC-B23B-008 | Human Review remains qualified, scoped, external to the generating Skill and non-runtime. |
| AC-B23B-009 | `git diff --check` passes, staging remains empty and the Result records exact before/after hashes and the complete path set. |

## 10. Proposed Read-only Validation Scenarios

| Scenario | Required future behavior |
|---|---|
| Candidate evidence has no complete source/custodian/collection chain | Preserve and flag the gap; do not declare it authentic or inadmissible. |
| Restricted defense evidence is passed to analysis | Return only permitted metadata or redacted findings; do not imply permission to disclose or use. |
| Evidence ref belongs to another Matter or a mismatched purpose | Reject or flag the context; do not silently transfer or reuse it. |
| Electronic data has a copied file but no original carrier/integrity context | Recommend preservation/integrity follow-up; do not score credibility or authenticity. |
| Personal information exceeds the stated review purpose | Apply least-necessary/redaction and human-review controls; do not broaden access. |
| A reviewed ref is supplied to a specialist | Treat the review status as scoped metadata only; do not infer admissibility, sufficiency or filing authorization. |

## 11. Read-only Integrity Record

Before creating this document:

- `litigation-legal/` contained `37` files.
- The SHA-256 of the sorted `path<TAB>file-SHA-256` manifest was `F559E4481C1DAC3FBE264F2735F368F30F88E1FD94FCF555A9562A12044E36D8`.
- The only implementation paths shown by Git were the seven previously adopted P1/P2 modifications.
- The three previously untouched candidates were clean; `claim-chart/SKILL.md` matched its adopted P1 hash.
- The staging area was empty and `git diff --check` passed.

The same manifest identity and implementation path set must remain unchanged at closeout.

## 12. Decision and Next Gate

Inventory recommendation:

- **MODIFY in a future separately approved B-2.3-B:** `evidence-preservation/SKILL.md`, `confidential-evidence-review/SKILL.md`.
- **NO CHANGE:** `claim-chart/SKILL.md`.
- **DEFER:** `witness-trial-prep/SKILL.md`.

Next recipient: **Architecture Coordinator (ChatGPT)** for AC-B23A review. The Architecture Coordinator may then submit a recommendation to the **Project Owner**. Only a new Project Owner decision may authorize B-2.3-B.
