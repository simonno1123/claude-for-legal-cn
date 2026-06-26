---
name: cold-start-interview
description: >
  Single entry for China AI governance profile setup and customization. Captures AI systems, data, public launch channels, filings, MLPS, telecom/app prerequisites, vendors, controls, and approval owners.
argument-hint: "[enterprise / product / AI system description; optional policies, vendor terms, inventory]"
---

# /cold-start-interview

## Mandatory Rules

- Default to China Mainland AI, data, personal information, telecom/app, cybersecurity, and content-safety rules.
- Do not ask EU AI Act, NIST, FTC, GDPR DPIA, or US state-law questions as default configuration fields.
- Output `ai_governance_profile` as the only initialization and customization base for this plugin.
- `customize` is not an independent entry; it redirects here.

## Interview Dimensions

1. Enterprise profile: entity, industry, registered location, public-facing products, paid services.
2. AI role: self-developed model, application service provider, third-party tool buyer, internal user, technical support provider.
3. AI type: generative AI, algorithm recommendation, deep synthesis, intelligent customer service, recruiting screening, risk scoring, code generation, office assistant.
4. Launch channel: internal tool, website, App, mini-program, SaaS/API, embedded product, offline deployment.
5. Infrastructure prerequisites: ICP filing, App filing, ICP License/value-added telecom license, MLPS 2.0 level/report status.
6. Data source: training data, fine-tuning data, user input, customer data, employee data, personal information, sensitive personal information, important data, trade secrets, copyrighted content.
7. Data export: overseas model API, overseas support, overseas storage, group HQ analytics, export population count since Jan 1, sensitive PI count, important data status.
8. Regulatory triggers: public service, public opinion/social mobilization, minors, medical, financial, education, recruiting, legal, credit, consumer compensation.
9. Vendor: model API, cloud service, private deployment, open-source model, training/retention/export/deletion/audit clauses.
10. Controls: AI-use policy, prohibited uses, approval flow, human review, log retention, incident response, complaints, real-name authentication, visible marking, implicit watermark.

## Output Format

```markdown
# China AI Governance Profile

## Enterprise And Role
- Entity:
- Industry:
- Registered location:
- AI role:
- Service audience:
- Paid commercial service:

## AI System Inventory Draft
| System | Type | Internal/Public | Launch channel | Data | Vendor | Regulatory tags |
|---|---|---|---|---|---|---|

## Filing / Infrastructure Status
| Item | Status | Evidence | Gap |
|---|---|---|---|
| Algorithm recommendation filing | | | |
| Generative AI service filing/security assessment | | | |
| Deep synthesis marking | | | |
| Real-name authentication | | | |
| ICP filing | | | |
| App filing | | | |
| ICP License / value-added telecom license | | | |
| MLPS 2.0 level/report | | | |

## Data And Cross-Border Profile
| Item | Status | Notes |
|---|---|---|
| Personal information | | |
| Sensitive personal information | | |
| Important data | | |
| Overseas model/API/storage/support | | |
| PI exported since Jan 1 | | |
| Sensitive PI exported since Jan 1 | | |
| PIPIA status | | |

## High-Risk Triggers
- [ ] Public generative AI
- [ ] Algorithm recommendation / public opinion attribute
- [ ] Deep synthesis
- [ ] Personal information / sensitive personal information
- [ ] Important data
- [ ] Cross-border data flow
- [ ] Minors
- [ ] Medical / financial / education / recruiting / legal / credit
- [ ] Vendor training or cross-border processing
- [ ] Paid public service requiring telecom license review

## Next Steps
1. `/ai-governance-legal:ai-inventory`
2. `/ai-governance-legal:use-case-triage`
3. `/ai-governance-legal:security-assessment`
4. `/ai-governance-legal:vendor-ai-review`
```
