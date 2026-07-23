# TASK_PHASE2_C02_III_REQUEST_RIGHT_VALIDATION_ENHANCEMENT_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-III Request Right Validation Enhancement |
| Execution date | 2026-07-20 |
| Mode | Read-only validation enhancement |
| Status | **DONE — COMPLETED WITH MATERIAL GAPS** |
| Approved Handoff SHA-256 | `3682724AF43E93AE1E9D674E30C7AF1FE6DDF544E83E968AFC023547F9328A35` |
| Handoff Review SHA-256 | `2B779EBB72B160F50DD8B38180ED33D4F7EF38723FA5149201292BAE1D0F344B` |
| Project Owner Decision SHA-256 | `1EAA030E3DA83560E8146701FE0F7EE29CEFD42796876AEA107369D5928F94BE` |
| C02-II Design Spec SHA-256 | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` |
| C02-II Design Result SHA-256 | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` |

This artifact applies the C02-II request-right model to the currently accessible validation inputs. It is not a legal opinion, merits determination, litigation strategy, runtime schema, Skill prompt, Agent definition, or implementation artifact.

## 1. Validation Objective and Boundary

C02-III tests whether the C02-II model can preserve a traceable path from material registration to lawyer-reviewable request-right candidates:

```text
Case Material Registry
        ↓
Source Statement / Raw Fact
        ↓
Legal Fact Candidate
        ↓
Element Fact Candidate
        ↓
Request Right Candidate
        ↓
Constituent Element
        ↓
Evidence Requirement / Gap
        ↓
Qualified Human Review
```

The validation may identify candidate structures and blocking conditions. It may not:

- infer facts from a case name, filename, prior summary, missing document, or document count;
- treat a source statement as established truth;
- select a final request right or litigation route;
- decide authenticity, admissibility, credibility, probative weight, or proof sufficiency;
- output a win/lose state, probability, merits score, or automated legal conclusion;
- modify any file under `litigation-legal/` or create a runtime implementation.

## 2. Fixed Input Verification

### 2.1 Required C02-II Inputs

| Input | Required SHA-256 | Actual SHA-256 | Result |
|---|---|---|---|
| C02-II Design Spec | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` | `BB4C2A1B8977A99EB46E4854BDDCF7F4B6759523F6E926654BED365F71C55FE1` | PASS |
| C02-II Design Result | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` | `3BCE75F664CECB079AACBBAB622F71915DEAF15DC81B335CB8E1BBE51FC2B047` | PASS |

### 2.2 Supporting Governance Inputs

| Supporting input | SHA-256 | Result |
|---|---|---|
| C02-I Case Input Binding Manifest | `30D14805E7F9250C52E63B227BD02CA54F763B1E71C41141E3ACBB4E038BAE13` | VERIFIED |
| C02-I Case Input Binding Result | `47AA406C95B27294328DB1686377AE971CAAEBBD1867B20FAF32AE69E64DE2DB` | VERIFIED |
| C02-I Case Material Import Manifest | `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C` | VERIFIED |
| C02-I Case Material Import Result | `2269DE1DF06037851B10C5299F0DD0192C44AC7BE010702CD940253562DAEA05` | VERIFIED |
| C02-I Request Right Validation Spec | `FD51E092DC8C4DA3A06BC9FB711D80CEA958E3DE6B6288EE1DB4490A4C6CD94C` | VERIFIED |
| C02-I Request Right Validation Result | `F0003635F051D9CA89956EBC624F7EE8B285D7A5D8202D85B88C4EBF1664A7B7` | VERIFIED |

These supporting inputs document prior discovery and availability states. They do not prove that an external material remains accessible at C02-III execution time; every physical path is rechecked below.

## 3. Validation Status Model

The C02-II controlled values remain authoritative:

| Status | Meaning in this validation |
|---|---|
| `UNKNOWN` | A candidate cannot yet be evaluated or has not completed qualified review |
| `SUPPORTED` | A verified source currently supports the mapped candidate proposition, subject to all stated limits and human review |
| `BLOCKED` | A required source, authority, fact, access condition, OCR/text layer, or human decision is missing |

Registry controls use additional access descriptors that do not replace those legal-validation values:

| Registry descriptor | Meaning |
|---|---|
| `ACCESSIBLE_VERIFIED` | File exists at the bound path and its byte hash was recomputed successfully |
| `MISSING_AT_BOUND_PATH` | File or directory does not exist at the path recorded in the approved import manifest |
| `TEXT_LAYER_VERIFIED` | Machine-readable text was extracted from all substantive pages |
| `OCR_BLOCKED` | Image content requires OCR or human transcription that was not available in the authorized execution |
| `NOT_APPLICABLE_UNAVAILABLE` | OCR cannot be evaluated because the physical file is unavailable |

No registry descriptor is a merits assessment.

## 4. Case Material Registry

### 4.1 CASE-A — C02-CASE-A-001 / 沐希鞋业买卖合同纠纷

| Document ID | Material | Bound path | Expected hash | Actual hash | Access | Text/OCR status | Human review | Validation state |
|---|---|---|---|---|---|---|---|---|
| A-D01 | Muxi Bill (10–12) | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\沐希鞋业合同案\沐希10-12月账单.xls` | `6B1E5ED87165576847EEBC67B50E048FBC7F8C2FD708172C492BEFBD5F526082` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| A-D02 | Muxi Company Report | `C:\Users\Administrator\Documents\xwechat_files\simonno1123_a85c\msg\file\2026-06\温州沐希鞋业有限公司报告.pdf` | `8A654E4F136240496AE0EC3602CC1A7099CB546C3B6BD4AFFEDD0C90A5A2A898` | `8A654E4F136240496AE0EC3602CC1A7099CB546C3B6BD4AFFEDD0C90A5A2A898` | `ACCESSIBLE_VERIFIED` | `TEXT_LAYER_VERIFIED` — 2,996 extracted characters across pages 1–7; page 8 visually verified as blank | REQUIRED / PENDING | `SUPPORTED` for source identity only |
| A-D03 | WeChat chat logs | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| A-D04 | Payment vouchers | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |

CASE-A registry result: **1 of 4 material categories accessible; 3 blocked**.

### 4.2 CASE-B — C02-CASE-B-001 / 塑博坊人格否认责任

| Document ID | Material | Bound path | Expected hash | Actual hash | Access | Text/OCR status | Human review | Validation state |
|---|---|---|---|---|---|---|---|---|
| B-D01 | Court Judgment | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\浙江塑博坊判决书.pdf` | `FE0636347235BF3EBC800032BB075B2CC62F486279796FA6AB66A6EE5B412EA2` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| B-D02 | Bank Flow Records | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\资金流流水.xlsx` | `85ACDB7FEC78A4FCB195844F229C470A8927B4B52698278B7CE501B7D52A8833` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| B-D03 | Corporate Registration Records | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\塑博坊案\工商调档资料\` | Prior manifest: `Bound Multiple` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| B-D04 | Shareholder Lists | Expected within corporate-record set; no independently bound file | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| B-D05 | Enforcement Documents | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |

CASE-B registry result: **0 of 5 material categories accessible; all blocked**. The prior directory-level entry did not bind each child file by path and hash, and the directory is now unavailable, so C02-III cannot validate the earlier node count or OCR-gap count.

### 4.3 CASE-C — C02-CASE-C-001 / 张成棋执行衍生案件

| Document ID | Material | Bound path | Expected hash | Actual hash | Access | Text/OCR status | Human review | Validation state |
|---|---|---|---|---|---|---|---|---|
| C-D01 | Kangerda Fee Details | `C:\Users\Administrator\WPSDrive\729282343\WPS云文档\wps个人云文档\私有\法律案件\康尔达系列案\康尔达系列案件费用明细.xlsx` | `0A984697AA7B1EAA4157F8C8CF84B0E114AA7097118E0054023337BC2163764B` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| C-D02 | Property Registration | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| C-D03 | Enforcement Logs | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |
| C-D04 | Derivative-Litigation Materials | `NOT_FOUND` | `NOT_AVAILABLE` | `NOT_AVAILABLE` | `MISSING_AT_BOUND_PATH` | `NOT_APPLICABLE_UNAVAILABLE` | PENDING | `BLOCKED` |

CASE-C registry result: **0 of 4 material categories accessible; all blocked**.

### 4.4 Registry Summary

```text
Required material categories:      13
Accessible and hash-verified:       1
Missing at bound path / not found: 12
PDFs with substantive text verified: 1
Workbooks available for reading:    0
Cases with complete material set:   0
```

## 5. Enhanced Validation Procedure

For each accessible document, validation must follow all steps below:

1. **Bind material**: record case ID, document ID, path or approved object reference, byte hash, type, access scope, text/OCR status, and review status.
2. **Locate source**: record page, sheet/cell, message/time range, or another auditable locator.
3. **Extract source statement**: preserve attribution and extraction method; do not rewrite it as an objective fact.
4. **Create Raw Fact candidate**: describe only what the located source records.
5. **Create Legal Fact candidate**: state the proposed legal relevance and the transformation rationale.
6. **Map Element Fact**: link the candidate to a specific request-right element and preserve supporting, adverse, and conflicting sources.
7. **Map Evidence Requirement**: identify what evidence category is required and what authenticity, admissibility, completeness, or authority review remains.
8. **Assign controlled state**: use only `UNKNOWN`, `SUPPORTED`, or `BLOCKED` under the C02-II definitions.
9. **Apply Human Review Gate**: a qualified lawyer verifies parties, requested legal effect, current law, source meaning, defenses, gaps, and any intended use.

If a required document is inaccessible, processing stops at the registry or evidence-requirement layer. The model must not synthesize the missing raw fact.

## 6. CASE-A Mapping Validation

### 6.1 Permitted Source Use

The company report may support only time-sensitive enterprise identity and registered-role candidates. It does not establish:

- a sales contract or other transaction;
- the claimant or respondent's actual transaction attribution;
- authority of a representative for a specific act;
- delivery, receipt, inspection, objection, return, or quality facts;
- price, reconciliation, invoice, maturity, payment, or outstanding balance;
- authenticity, admissibility, credibility, or proof sufficiency.

### 6.2 Request-Right Candidate and Element–Evidence Trace

`RR-A1 — Sale-price payment claim against the company` is retained solely as a validation placeholder and is **not factually activated**.

| Element candidate | Required fact / Element Fact candidate | Current mapped evidence | Evidence requirement / gap | Status |
|---|---|---|---|---|
| Proper parties and attribution | The claimant and respondent were parties to the alleged transaction, including any representative authority | A-D02 supports only registered-company identity and historical registered roles | Contract, orders, account/contact attribution, seal or authorization records | `BLOCKED` |
| Agreement / legal basis candidate | Offer, acceptance, subject, quantity, price and other formation facts; current legal basis | None | Contract, orders, communications and current-law verification | `BLOCKED` |
| Seller performance | Goods, quantity, delivery time, recipient, acceptance or objection | None | Delivery notes, logistics, receipt, inspection, return and objection records | `BLOCKED` |
| Payment condition and maturity | Agreed price, reconciliation, invoicing terms and due date | None | Missing bill workbook, contract, reconciliation and invoice records | `BLOCKED` |
| Non-payment and amount | Complete payment, credit, return, discount, set-off and balance history | None | Payment vouchers, bank records and complete account ledger | `BLOCKED` |
| Defense and rebuttal visibility | Actual quality, quantity, payment, set-off, authority, limitation or procedural positions | None | Party instructions and adverse-source materials | `BLOCKED` |

Validation result:

```text
Material registry:                 PASS — LIMITED
Raw Fact → Legal Fact controls:    PASS — IDENTITY USE ONLY
Request-right activation:         BLOCKED
Element–evidence trace:            PARTIAL — GAPS STRUCTURED
Human Review Gate:                 PASS
```

No alternative restitutionary or other request right is generated because its factual predicates and current legal basis are not established by the accessible source.

## 7. CASE-B Mapping Validation

No CASE-B file is accessible at the approved paths. The case label is not evidence and does not activate a company-personality-denial, shareholder-responsibility, controlling-person, contribution, commingling, abuse, or other route.

The model can preserve the following prerequisites as unfilled validation interfaces only:

| Interface prerequisite | Required material category | Current status |
|---|---|---|
| Underlying creditor right and enforceable obligation | Judgment, contract, settlement, payment and enforcement records | `BLOCKED` |
| Identity and role of proposed respondents | Current corporate registration, shareholder and control records | `BLOCKED` |
| Specific conduct proposed as legally relevant | Complete bank flows, accounting, related-party transactions, asset records and source attribution | `BLOCKED` |
| Connection between conduct and non-realization of the claimed right | Enforcement results, asset changes and chronological source records | `BLOCKED` |
| Competing explanation, defense and rebuttal | Separate books/accounts, ordinary-course transactions, contribution and governance records | `BLOCKED` |
| Current legal basis and burden candidate | Current statutes, judicial interpretations and evidence rules | `BLOCKED` |

Validation result:

```text
Material registry:                 PASS — ALL GAPS EXPLICIT
Raw Fact → Legal Fact controls:    NOT EXERCISED
Request-right activation:         NOT GENERATED
Element–evidence trace:            BLOCKED
Gap preservation:                 PASS
Human Review Gate:                 PASS
```

## 8. CASE-C Mapping Validation

No CASE-C file is accessible at the approved paths. The matter name and prior fee-workbook label do not establish an enforceable instrument, an enforcement measure, an asset clue, ownership, a transfer, consideration, harm, or a separate substantive cause of action.

| Interface prerequisite | Required material category | Current status |
|---|---|---|
| Enforceable obligation and procedural posture | Enforceable instrument and enforcement case records | `BLOCKED` |
| Measures already taken and unresolved enforcement issue | Enforcement rulings and complete execution log | `BLOCKED` |
| Specific asset clue, ownership and timing | Property registration and reliable title/source records | `BLOCKED` |
| Transfer, payment, consideration and relevant actors | Transaction, payment and communication evidence | `BLOCKED` |
| Proposed derivative route and requested legal effect | Pleadings, procedural records and current legal authority | `BLOCKED` |

Validation result:

```text
Material registry:                 PASS — ALL GAPS EXPLICIT
Raw Fact → Legal Fact controls:    NOT EXERCISED
Alternative request rights:        NOT GENERATED
Element–evidence trace:            BLOCKED
Enforcement/substantive separation: PASS — CONTROL RULE ONLY
Human Review Gate:                 PASS
```

The framework does not choose between continued enforcement, a procedural remedy, or a separate substantive request-right path.

## 9. Cross-Case Model-Fit Assessment

| Validation control | Result | Observation |
|---|---|---|
| Registry accepts path, byte hash, access and text/OCR states | PASS | One file is positively verified; all unavailable categories remain explicit |
| Raw Fact remains distinct from Legal Fact and Element Fact | PASS — LIMITED | Reconfirmed on CASE-A enterprise-identity source; CASE-B/C not exercised |
| Element maps to a stated evidence requirement | PARTIAL | CASE-A gaps are traced; CASE-B/C remain interface-level only |
| Missing prerequisites produce `BLOCKED` without invented facts | PASS | Twelve categories remain unavailable and no replacement facts were generated |
| Request-right candidates remain candidate-only | PASS | No candidate was finally selected or ranked |
| Adverse facts, defense and rebuttal remain visible requirements | PASS | They are required fields and remain gaps where sources are absent |
| Qualified lawyer retains final authority | PASS | All legal relevance, authority, burden, and application decisions require human review |
| Three cases fully validate real-case operability | FAIL / BLOCKED | No case has a complete material set; CASE-B/C have no accessible file |

## 10. Human Review Gate

Before any candidate may be applied, a qualified lawyer must confirm at minimum:

- client position, parties, requested legal effect, and procedural posture;
- source path/object identity, byte hash, access scope, and source locator;
- extraction accuracy, attribution, chronology, ambiguity, and conflicting sources;
- current statutes, judicial interpretations, evidence rules, and authority effective dates;
- each constituent element, required fact, burden candidate, evidence requirement, defense, and rebuttal;
- authenticity, admissibility, completeness, credibility, and proof sufficiency as distinct questions;
- that no outcome prediction, probability, automatic strategy selection, or final legal opinion is presented as a machine decision.

This is a governance control pattern, not a runtime state machine.

## 11. China-Law Authority Boundary

No live statute, judicial interpretation, guiding case, People's Court Case Library entry, or other case-authority source was retrieved in this execution. Accordingly:

- no article-level legal basis is treated as verified;
- no definitive burden allocation is made;
- no case is used as common-law precedent;
- every later substantive request-right analysis must verify current China Mainland law and any comparable authoritative cases against the complete record.

## 12. Acceptance Criteria Assessment

| AC | Status | Basis |
|---|---|---|
| AC-C02-III-001 — Registry verifies document hashes and OCR statuses | **PASS WITH MATERIAL GAPS** | All 13 categories have explicit current access and text/OCR states; the sole accessible PDF matches its approved hash and substantive text layer was verified |
| AC-C02-III-002 — Trace the elements–evidence mapping | **PARTIAL** | CASE-A has a limited element–evidence gap trace; CASE-B/C remain blocked before source extraction |
| AC-C02-III-003 — Structure gaps based on element prerequisites | **PASS** | Each case preserves missing element facts and required evidence without synthesized facts |
| AC-C02-III-004 — Prohibit win predictions or automated merits evaluation | **PASS** | No outcome, probability, merits score, or automated legal conclusion was produced |
| AC-C02-III-005 — Zero prompt changes or code regressions under `litigation-legal/` | **PASS** | This execution creates documentation outputs only; final repository verification is recorded in the Result |
| AC-C02-III-006 — Git validation | **See Result** | Final `git diff --check`, staging, and target-module status verification are recorded after both outputs are materialized |

## 13. Final Determination

```text
C02-III Execution:
DONE — VALIDATION ENHANCEMENT COMPLETED WITH MATERIAL GAPS

Model-fit conclusion:
PARTIAL / NOT READY FOR IMPLEMENTATION

Validated:
- deterministic material registry controls;
- explicit text/OCR and access-state recording;
- source/fact/legal-fact/element separation;
- element-prerequisite gap mapping;
- candidate-only semantics;
- Human Review Gate.

Not validated:
- a complete transaction request-right trace for CASE-A;
- a source-backed responsibility trace for CASE-B;
- a source-backed enforcement-to-derivative-right trace for CASE-C;
- case-specific final legal basis or burden allocation;
- production or runtime implementation.
```

C02-II Implementation and C03 remain **NOT AUTHORIZED**. The next governance step is Architecture Coordinator review of this Spec and the corresponding Result. A future substantive rerun requires restoration or approved rebinding of the missing case materials, with per-file paths and byte hashes and verified text/OCR coverage.
