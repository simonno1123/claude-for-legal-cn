# TASK_PHASE2_C02_I_REQUEST_RIGHT_VALIDATION_SPEC

## 0. Document Control

| Field | Value |
|---|---|
| Track | Phase 2 / Track C / TASK_PHASE2_C02 |
| Stage | C02-I Request Right Validation Execution |
| Execution date | 2026-07-20 |
| Mode | Read-only validation |
| Status | **BLOCKED — PARTIAL VALIDATION ONLY** |
| Final Execution Handoff SHA-256 | `F4E830148FFF96F105DE8030D5120CCD542CD55D637CFAE6AA772FAFB3E23564` |
| Project Owner Decision SHA-256 | `63BD152F430901927CD7F811EB7E157378723BED99AFB4B78EFD05063256C2A4` |
| Execution Notice SHA-256 | `FE652FF670504D7C0AD09F708D378A342FFD3BFC8D8268545C3BB8745440FFF9` |

This specification records a limited validation against materials that were actually accessible at execution time. It does not provide a legal opinion, select a final request right, determine evidentiary weight, predict adjudication, or estimate a win rate.

## 1. Validation Outcome

The structural model remains usable as a control framework, but the three-case validation cannot be completed because most source files recorded by the Case Material Import Manifest are no longer accessible at their bound paths.

```text
Governance inputs:         PASS
CASE-A structural test:    PARTIAL
CASE-B structural test:    BLOCKED
CASE-C structural test:    BLOCKED
Overall execution result:  BLOCKED — MATERIAL AVAILABILITY DRIFT
```

The limited execution validates one important boundary: a case name, inventory row, or missing file is not a fact and cannot independently support a request-right candidate. Missing inputs remain unresolved rather than being reconstructed from prior summaries.

## 2. Fixed Input Verification

| Input | Required and actual SHA-256 | Result |
|---|---|---|
| Final Execution Handoff | `F4E830148FFF96F105DE8030D5120CCD542CD55D637CFAE6AA772FAFB3E23564` | PASS |
| Project Owner Decision | `63BD152F430901927CD7F811EB7E157378723BED99AFB4B78EFD05063256C2A4` | PASS |
| Execution Notice | `FE652FF670504D7C0AD09F708D378A342FFD3BFC8D8268545C3BB8745440FFF9` | PASS |
| C01 Design Baseline v0.2 | `EAB7EE7C010D06E79D1391430226D883D6078135916BA90B3BC3FFE0907FD784` | PASS |
| Case Input Binding Manifest | `30D14805E7F9250C52E63B227BD02CA54F763B1E71C41141E3ACBB4E038BAE13` | PASS |
| Case Input Binding Result | `47AA406C95B27294328DB1686377AE971CAAEBBD1867B20FAF32AE69E64DE2DB` | PASS |
| Case Material Import Manifest | `2197BA0B96120A312F04B64F59F3E80FDCF80C585E90AC9240D1607BB695557C` | PASS |
| Case Material Import Result | `2269DE1DF06037851B10C5299F0DD0192C44AC7BE010702CD940253562DAEA05` | PASS |

The hashes above verify governance-document identity. They do not prove that every external case file remains present. Physical availability was therefore rechecked separately.

## 3. Execution-Time Material Availability

| Case | Manifest-recorded bound material | Accessible at execution | Result |
|---|---:|---:|---|
| CASE-A — 沐希鞋业买卖合同纠纷 | 2 files | 1 PDF | PARTIAL |
| CASE-B — 塑博坊人格否认责任 | 13 file nodes | 0 | BLOCKED |
| CASE-C — 张成棋执行衍生案件 | 1 workbook | 0 | BLOCKED |

### 3.1 Accessible Source

| Case | Source | SHA-256 | Verification |
|---|---|---|---|
| CASE-A | `C:\Users\Administrator\Documents\xwechat_files\simonno1123_a85c\msg\file\2026-06\温州沐希鞋业有限公司报告.pdf` | `8A654E4F136240496AE0EC3602CC1A7099CB546C3B6BD4AFFEDD0C90A5A2A898` | Hash matches manifest; 8 pages; pages 1–7 have a text layer; page 8 is blank |

The PDF was checked through both text extraction and rendered-page inspection. Its cover note states that the report is for reference and that the National Enterprise Credit Information Publicity System query page controls.

### 3.2 Unavailable Bound Sources

The following manifest paths were unavailable when execution began:

- CASE-A: `沐希10-12月账单.xls`;
- CASE-B: `浙江塑博坊判决书.pdf`;
- CASE-B: `资金流流水.xlsx`;
- CASE-B: the bound `工商调档资料` directory;
- CASE-C: `康尔达系列案件费用明细.xlsx`.

The WeChat records, payment vouchers, property registration, enforcement logs, and derivative-litigation documents were already marked missing by the manifest. No spreadsheet values, judgment content, corporate-record content, or enforcement facts were inferred from filenames or historic summaries.

## 4. Validation Method

```text
Evidence Source
    ↓
Source Statement / Recorded Data
    ↓
Event Fact Candidate
    ↓
Element Fact Candidate
    ↓
Material Fact Candidate
    ↓
Request Right Candidate
    ↓
Constituent Element
    ↓
Burden Candidate / Evidence Requirement / Gap
    ↓
Qualified Lawyer Review
```

Control rules:

1. A file is evidence, not a fact by itself.
2. A source statement is not automatically true, complete, or attributable to every relevant party.
3. A candidate legal fact is not a judicial fact.
4. A request right remains a candidate until its authority, elements, parties, facts, defenses, and evidence are reviewed.
5. Burden allocation is only a candidate requiring verification against current statutes, judicial interpretations, and evidence rules.
6. Missing or inaccessible material blocks the affected inference; it is never replaced by a case name or filename.

## 5. CASE-A — Request Right Structure Validation

### 5.1 Evidence Boundary

Only the company publicity report was accessible. It can support a limited enterprise-identity and registered-role timeline. It cannot establish a transaction, contract, delivery, acceptance, debt amount, due date, non-payment, authority for a particular communication, or defense.

### 5.2 Source Statements and Candidate Facts

| ID | Source statement or recorded data | Permitted candidate fact | Boundary |
|---|---|---|---|
| A-S01 | The report identifies 温州沐希鞋业有限公司 and unified social credit code `91330324MACGRX8D8R` | A registered company with that identifier is reported as the possible transaction entity | Identity only; transaction-party status unresolved |
| A-S02 | Page 2 reports a natural-person wholly owned limited company, legal representative 温德义, registered capital RMB 200,000, and status `存续` | Current registered form and roles as shown in the report | Must be rechecked against the live publicity system |
| A-S03 | Page 3 records changes on 2024-06-05, including legal representative from 崔龙 to 温德义 and shareholder/type changes | Registered-role attribution may depend on the transaction date | Does not prove authority or ratification in a specific transaction |
| A-S04 | The 2023 annual-report section records then-shareholders 崔龙 and 周宁, subscribed amounts of RMB 150,000 and RMB 50,000, and paid-in amount 0 at that reporting point | Historic registered contribution information may be time-sensitive context | Not a finding of capital defect, abuse, or liability |
| A-S05 | The report records inclusion in the abnormal-operation list on 2025-07-01 for failure to timely publish the 2024 annual report | A public-registration compliance event is reported | Does not prove inability to perform, insolvency, or transaction breach |
| A-S06 | The report displays no branch, judicial-assistance, movable-mortgage, or equity-pledge information | The report returned no such entries at generation time | Absence in this report is not proof that no relevant asset, obligation, or proceeding exists |

No Case Fact concerning the alleged sale, orders, delivery, payment, or communications was available.

### 5.3 Request Right Candidate Map

#### RR-A1 — Sale-price payment claim against the company

Status: **Candidate template only / not factually activated**.

| Constituent element candidate | Required case fact | Current evidence | Gap / blocking condition |
|---|---|---|---|
| Agreement and attribution to the respondent | Offer/acceptance, order placement, contracting identity, seal/account/contact attribution | Company identity report only | Contract, orders, WeChat, account and representative-authority material missing |
| Seller performance or delivery | Goods, quantity, time, delivery recipient, acceptance or absence of timely objection | None | Delivery notes, logistics, receipt, inspection and return records missing |
| Payment condition and maturity | Agreed price, reconciliation, invoice terms, due date | None | Bill workbook unavailable; contract and reconciliation missing |
| Non-payment and outstanding amount | Complete payment history, credits, returns, set-off and balance | None | Payment vouchers and bank records missing |
| Proper claimant and respondent | Seller identity and transaction counterparty | Respondent registration identity only | Claimant records and transaction attribution missing |

Candidate burden note: claimant-side facts supporting contract formation, performance, maturity and amount would require source-backed proof; payment, set-off, quality objections and other defenses require separate allocation review. No final burden allocation is made because current normative authority and the missing case record were not available within this execution.

#### RR-A2 — Alternative restitutionary or other non-contract route

Status: **Not generated**.

No evidence establishes invalidity, failure of a contract basis, receipt of a specific benefit, or another factual predicate. The framework therefore does not activate an alternative request right from the dispute label alone.

### 5.4 Defense and Rebuttal Readiness

Potential defense categories can be reserved as placeholders only:

- denial of contracting identity or representative authority;
- denial or qualification of delivery/acceptance;
- quality, quantity, return, discount, set-off, or payment issues;
- maturity, limitation-period, or procedural objections.

None is recorded as an actual defense. Correspondence, transaction documents and the represented party's instructions are required before adversarial mapping.

### 5.5 CASE-A Result

```text
Fact / legal-fact separation:       PASS
Enterprise identity extraction:    PASS (limited and time-sensitive)
Request-right activation:          BLOCKED
Element decomposition:             PARTIAL — template only
Evidence requirement mapping:      PASS
Case-specific burden mapping:      BLOCKED
Human review boundary:             PASS
```

## 6. CASE-B — Evidence-to-Element Mapping Validation

No CASE-B bound file was accessible. The judgment, bank-flow workbook, and corporate-record directory could not be opened or independently hashed.

```text
Evidence items read:               0
Case Facts extracted:              0
Legal Fact candidates generated:   0
Request Right candidates:          0
```

The manifest label `塑博坊人格否认责任` is a test theme, not evidence and not a final request-right selection.

| Validation question | Required evidence category | Current status |
|---|---|---|
| What underlying creditor right and enforceable obligation exist? | Judgment, contract, settlement, payment and enforcement records | INACCESSIBLE |
| Which company and which person/entity are proposed respondents? | Corporate registration, shareholder and control records | INACCESSIBLE |
| What specific conduct is alleged to justify a responsibility path? | Bank flows, related-party transactions, accounting and asset records | INACCESSIBLE |
| What loss or non-realization is alleged, and how is it linked to the conduct? | Enforcement results, asset records and transaction timeline | INACCESSIBLE |
| What competing explanation or rebuttal exists? | Separate books/accounts, ordinary-course transactions, contribution and governance records | INACCESSIBLE |

Any shareholder-liability, controlling-person, contribution, commingling, abuse, or other responsibility route remains **NOT GENERATED** pending current-law authority review and evidence access.

```text
Element-evidence mapping:           BLOCKED
Missing-fact detection:             PASS
No evidence-to-conclusion shortcut: PASS
Human review boundary:              PASS
```

## 7. CASE-C — Competing Request Right Analysis Validation

The only file recorded as bound for CASE-C, `康尔达系列案件费用明细.xlsx`, was unavailable. Property registration, enforcement logs and derivative-litigation materials were already marked missing.

```text
Evidence items read:               0
Case Facts extracted:              0
Legal Fact candidates generated:   0
Competing request rights:           0
```

| Required input | Purpose | Current status |
|---|---|---|
| Enforceable instrument and enforcement case records | Identify parties, obligation, scope and procedural posture | MISSING |
| Enforcement rulings and execution log | Separate completed measures, available remedies and unresolved issues | MISSING |
| Specific asset clue and ownership record | Identify asset, title, timing and relevant actor | MISSING |
| Transfer/payment/consideration evidence | Test whether any separate substantive theory is factually supportable | MISSING |
| Proposed derivative-litigation record | Identify requested legal consequence and procedural vehicle | MISSING |

The model therefore does not choose between continued enforcement, a procedural challenge, or a separate substantive request-right path.

```text
Alternative request rights:         NOT GENERATED
Priority analysis:                  BLOCKED
Missing-fact detection:             PASS
Enforcement/substantive separation: PASS (as a control rule)
Human review boundary:              PASS
```

## 8. Cross-Case Validation

| Control | Result | Observation |
|---|---|---|
| Evidence is not treated as fact automatically | PASS | The company report is recorded as a source with limited propositions and caveats |
| Case label is not treated as a request right | PASS | CASE-B/C labels did not activate claims |
| Missing source does not become an inferred fact | PASS | Inaccessible spreadsheets, judgment and records remain unresolved |
| Alternative candidates remain possible | PASS | No final selection was made |
| Burden mapping remains authority-dependent | PASS | No definitive allocation was hard-coded |
| Qualified lawyer retains control | PASS | Every legal-fact and request-right output remains a candidate |
| Three real cases fully exercise the model | FAIL | Only one enterprise publicity report was accessible |

## 9. Case Authority Check

Statutory basis:

- Not retrieved in this execution. No article-level substantive conclusion is made.

Guiding cases / reference cases:

- `[case-missing]` No live case-authority source was used within the authorized material scope.

Similarity and distinctions:

- Not assessed because no comparable case text was retrieved and CASE-B/C source records were inaccessible.

Usability:

- `not comparable`.

Warning:

China Mainland cases are references for reasoning and similar-case review. They are not common-law precedent and do not replace statutes or judicial interpretations. No live case-authority source is connected for this validation result; any later substantive request-right or burden conclusion must be checked against current statutes, judicial interpretations, evidence rules, the People's Court Case Library or another authoritative database, and the complete case file.

## 10. Acceptance Criteria Assessment

| AC | Status | Basis |
|---|---|---|
| AC-C02-I-VAL-001 — Inputs match binding manifests exactly | **FAIL / BLOCKED** | Governance document hashes match, but only 1 manifest-recorded physical file remained accessible |
| AC-C02-I-VAL-002 — Trace the 3-Layer Request-Right Foundation analysis | **PARTIAL** | CASE-A was traced only through enterprise identity; CASE-B/C could not be activated |
| AC-C02-I-VAL-003 — Differentiate evidence and facts strictly | **PASS** | Source, source statement, candidate fact and gap remained separate |
| AC-C02-I-VAL-004 — Prohibit win predictions or automated adjudication | **PASS** | No merits result, automatic conclusion or probability was generated |
| AC-C02-I-VAL-005 — Zero prompt changes or code regressions | **PASS** | No file under `litigation-legal/` was modified by this execution |
| AC-C02-I-VAL-006 — Git validation | **See Result** | Final `git diff --check` and staging status are recorded in the execution Result |

## 11. Final Validation Determination

```text
Status:
BLOCKED — PARTIAL VALIDATION ONLY

Reason:
Material availability drift prevents case-level completion.

Validated:
- governance identity;
- source/fact/legal-fact separation;
- no-shortcut behavior;
- CASE-A enterprise-identity extraction;
- gap preservation;
- qualified-human-review boundary.

Not validated:
- CASE-A transaction facts and request-right activation;
- CASE-B element/evidence mapping;
- CASE-C competing request-right analysis;
- case-specific final burden allocation;
- substantive legal conclusions.
```

The next lawful step is not C02-II. The missing or inaccessible materials must first be restored to the exact approved paths or rebound through a new manifest with byte hashes, followed by a separately authorized validation rerun.
