---
name: security-assessment
description: >
  China AI safety assessment and compliance impact assessment. Covers generative AI filing/security assessment, algorithm filing, deep synthesis marking, TC260-PG-20241A, real-name authentication, ICP/App filing, MLPS 2.0, important data, and vendor risk.
argument-hint: "[AI system or use-case description]"
---

# /security-assessment

## Mandatory Rules

- Apply `references/china-ai-governance-rules.md`.
- Use "China AI Safety And Compliance Assessment" as the default output title.
- Do not write EU AI Act FRIA, GDPR DPIA, NIST AI RMF, FTC, or US state-law analysis unless expressly requested as overseas comparison.
- Do not output "compliant", "approved", "can launch", or "no filing needed" as a final conclusion.
- Mark unverified filing thresholds, official lists, provincial CAC windows, MIIT status, MLPS level, telecom license status, and standard versions as `[to verify]`.
- Treat the 2024 CAC cross-border data flow thresholds as effective baseline rules; do not mark the 100,000 / 1,000,000 / 10,000 thresholds themselves as unverified.

## Required Assessment Blocks

### 1. Organization Security

- Responsible department and accountable person.
- Compliance, legal, security, product, data, and algorithm owners.
- Real-name authentication owner and evidence.
- Labeling personnel management, training, sampling audit, and correction mechanism.
- Incident response owner and 24-hour disposal/report path.

### 2. Corpus And Data Security

- Training, fine-tuning, prompt, output, and log data sources.
- Personal information, sensitive personal information, children's personal information, important data, commercial secrets, and copyrighted content.
- Data classification and grading.
- Important data identification, localized storage, and export restriction.
- Lawful basis, authorization, separate consent, anonymization/de-identification, deletion, and retention.
- Filtering of illegal and harmful information in corpus.
- IP clearance and source traceability.

### 3. Model Security

- Model source: self-developed, open-source, domestic vendor, overseas vendor, private deployment.
- Refusal mechanism, harmful output tests, hallucination controls, bias tests, adversarial prompt testing.
- TC260-PG-20241A quantitative items:
  - Overall safety test set size.
  - Refusal test set size, with 500 as a key check item where applicable.
  - Safety assessment test set, with 2,000 as a key check item where applicable.
  - Labeler consistency ratio.
  - Sampling inspection ratio.
  - Red-team/adversarial prompt test records.
- Human review for medical, legal, financial, recruitment, credit, minors, or other high-impact outputs.

### 4. Service Security

- Real-name authentication for public-facing generative AI or deep synthesis services.
- Content safety stop-filter: detect, intercept, dispose, preserve logs, report to local CAC within 24 hours where required, and report to public security where criminal/public-security risk exists.
- Complaint and reporting channels.
- Minor protection.
- User agreement, service rules, prohibited-use rules, and account sanctions.
- Network log retention; no less than six months where network-log retention is required.

### 5. Filing, Assessment, Marking, And Infrastructure

- Algorithm recommendation filing.
- Generative AI service filing/security assessment.
- Deep synthesis visible marking and implicit watermark/metadata.
- ICP filing and App filing.
- ICP License / value-added telecom license where paid commercial operation is triggered.
- MLPS 2.0 assessment level, report number, testing institution, date, scope, and整改 status.
- PIPIA, important data, and 2024 cross-border data flow assessment.
- Vendor filing status and China compliance evidence.
- For financial-data, credit-card, risk-scoring, algorithmic pricing, or consumer profiling scenarios, treat credit card repayment as consumer spending behavior. Do not exclude it from spending/caliber calculations unless a China-qualified legal/compliance reviewer gives a documented contrary basis.

## Output Format

```markdown
# China AI Safety And Compliance Assessment (Draft)

> Jurisdiction: China Mainland
> Nature: internal compliance draft, not a filing submission, launch clearance, or regulator response
> To verify: [official filing status / local CAC window / MIIT filing / MLPS level / telecom license / standard version / vendor evidence]

## One-Line Conclusion
[May enter human review / needs remediation / needs special review / suspend launch]

## System Profile
| Item | Content |
|---|---|
| AI type | |
| Audience | |
| Public-facing? | |
| Generative AI? | |
| Algorithm recommendation? | |
| Deep synthesis? | |
| Website/App/mini-program/SaaS/API? | |
| Paid commercial service? | |
| Model/vendor | |
| Data source | |
| Responsible department | |

## Assessment Blocks
| Block | Risk level | Key facts | China control point | Remediation |
|---|---|---|---|---|
| Organization security | | | | |
| Corpus and data security | | | | |
| Model security | | | | |
| Service security | | | | |
| Filing/assessment/marking/infrastructure | | | | |

## Multi-Track Obligations
| Obligation | Triggered? | Reason | Authority/path | Evidence gap |
|---|---:|---|---|---|
| Algorithm recommendation filing | | | | |
| Generative AI service filing/security assessment | | | | |
| Deep synthesis visible marking | | | | |
| Deep synthesis implicit watermark/metadata | | | | |
| Real-name authentication | | | | |
| ICP filing / App filing | | | | |
| ICP License / value-added telecom license | | | | |
| MLPS 2.0 assessment | | | | |
| PIPIA / important data / data export | | | | |

## 2024 Cross-Border Data Flow Routing
| Scenario | Route |
|---|---|
| Non-CIIO exports fewer than 100,000 individuals' non-sensitive PI since Jan 1 | Exempt from CAC security assessment, standard contract filing, and certification; PIPIA and basic safeguards still apply |
| Non-CIIO exports 100,000 to fewer than 1,000,000 individuals' PI since Jan 1 | Standard contract or personal information protection certification path |
| Non-CIIO exports fewer than 10,000 individuals' sensitive PI since Jan 1 | Standard contract or personal information protection certification path |
| Non-CIIO exports 1,000,000 or more individuals' PI, or 10,000 or more individuals' sensitive PI since Jan 1 | CAC data export security assessment path |
| Important data / CIIO / sector-specific catalogue hit | Important data or CIIO route overrides PI exemption |

## Quantitative Safety Items
| Item | Required/target | Current | Gap |
|---|---|---|---|
| Overall safety test set | 2,000 items where applicable `[to verify]` | | |
| Refusal test set | 500 items where applicable `[to verify]` | | |
| Labeler consistency | threshold `[to verify]` | | |
| Sampling inspection ratio | threshold `[to verify]` | | |
| Log retention | no less than 6 months where required | | |
| MLPS report number | required where triggered | | |

## P0 Gates
- [ ] Real-name authentication
- [ ] ICP filing / App filing
- [ ] ICP License for paid commercial service
- [ ] MLPS 2.0 assessment report
- [ ] Content safety Stop-Filter and 24-hour report path
- [ ] TC260-PG-20241A test materials
- [ ] Training data lawful source and sensitive information filtering
- [ ] Important data classification and export controls
- [ ] Visible marking and implicit watermark
- [ ] Vendor filing/security evidence/no-training clause
- [ ] Human review and complaint handling

## Remediation List
| Priority | Item | Owner | Deadline | Evidence |
|---|---|---|---|---|
```
