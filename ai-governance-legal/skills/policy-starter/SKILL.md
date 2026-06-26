---
name: policy-starter
description: >
  Draft a China enterprise AI-use policy covering prohibited use, approval workflow, data input, vendor review, real-name authentication, ICP/App filing, MLPS 2.0, content safety, human review, logs, incident response, and employee sign-off.
argument-hint: "[enterprise type / AI use scope / existing policy]"
---

# /policy-starter

## Mandatory Rules

- Draft under China Mainland AI, data, personal information, IP, cybersecurity, secrecy, telecom, app, and labor-management requirements.
- Do not adapt ABA, NIST, EU AI Act, or US corporate AI policy templates as the default structure.
- Include practical attachments: AI use approval form, employee sign-off page, external AI tool procurement checklist, content safety incident log.
- Do not promise that internal documents have common-law privilege or evidence-production immunity in China.

## Required Policy Controls

- Prohibit employees from entering state secrets, work secrets, unpublished listed-company information, customer confidential information, sensitive personal information, important data, source code, contract negotiation materials, case materials, or trade secrets into any unapproved external model.
- Require separate approval for public-facing AI services, generative AI, algorithm recommendation, deep synthesis, minors, medical, financial, legal, recruitment, credit, education, important data, data export, and paid commercial AI services.
- Require real-name authentication before public-facing generative AI or deep synthesis services launch.
- Require ICP filing/App filing and ICP License checks before public or paid launch.
- Require MLPS 2.0 assessment status before public high-risk AI launch or filing/security-assessment submission.
- Require visible marking and implicit watermark/metadata controls for deep synthesis outputs.
- Require content safety stop-filter: detect, intercept, dispose, preserve logs, and report to local CAC/public security within 24 hours where required.
- Require TC260-PG-20241A aligned safety testing for generative AI service safety review.
- Require vendor review for model API, SaaS AI tools, private deployment, open-source models, and cloud AI services.
- Require human review before outputs are used for medical, financial, legal, HR, customer compensation, regulatory, or public communications.

## Output Structure

```markdown
# Enterprise AI Use Policy (Draft)

## 1. Scope
## 2. Roles And Responsibilities
## 3. AI Tool Classification
## 4. Allowed, Restricted, And Prohibited Use
## 5. Data Input Rules
## 6. External AI Tool Procurement And Use
## 7. Public Services, Real-Name Authentication, ICP/App Filing, ICP License, Filing And Safety Assessment
## 8. MLPS 2.0 And Cybersecurity Controls
## 9. Deep Synthesis Visible Marking And Implicit Watermark
## 10. Content Safety Stop-Filter And 24-Hour Disposal/Reporting
## 11. Personal Information, Important Data, Trade Secrets, State Secrets, And IP Protection
## 12. Human Review Of AI Output
## 13. Log Retention, Complaint Handling, And Security Incident Response
## 14. Violations, Training, And Employee Sign-Off

## Attachment 1: AI Use Approval Form
| Item | Content |
|---|---|
| Use case | |
| AI tool/model/vendor | |
| Public-facing? | |
| Paid commercial service? | |
| ICP filing/App filing needed? | |
| ICP License needed? | |
| MLPS 2.0 level/report status | |
| Real-name authentication involved? | |
| Generative AI? | |
| Algorithm recommendation? | |
| Deep synthesis? | |
| Visible marking done? | |
| Implicit watermark/metadata done? | |
| Personal information/sensitive PI involved? | |
| Important data involved? | |
| Cross-border data flow involved? | |
| PIPIA/filing/security assessment needed? | |
| Human reviewer | |

## Attachment 2: External AI Tool Procurement Checklist
| Review item | Result | Evidence |
|---|---|---|
| Vendor has China filing/security assessment evidence `[to verify]` | | |
| Vendor is deployed in China or involves cross-border data flow | | |
| Vendor can provide MLPS Level 3/Level 2 evidence where needed | | |
| Vendor uses inputs/outputs for training | | |
| Vendor supports deletion, isolation, log export, and audit | | |
| Vendor supports real-name, content safety, visible marking, and implicit watermark where needed | | |
| Vendor provides data security and incident notification commitments | | |

## Attachment 3: Content Safety Incident Log
| Time | Incident | Interception/disposal | Log preserved | Report to local CAC? | Report to public security? | Owner |
|---|---|---|---|---|---|---|

## Attachment 4: Employee Sign-Off
[Employee confirms reading and compliance with this policy.]
```
