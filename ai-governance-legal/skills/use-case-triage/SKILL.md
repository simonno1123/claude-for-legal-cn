---
name: use-case-triage
description: >
  China AI use-case triage. Classifies AI features, vendors, models, algorithm recommendation, deep synthesis, and public launch prerequisites under China Mainland rules.
argument-hint: "[AI use case / product requirement / vendor description]"
---

# /use-case-triage

## Mandatory Rules

- Apply `references/china-ai-governance-rules.md`.
- Default to China Mainland law and regulator practice.
- Do not classify by EU AI Act, NIST, FTC, GDPR DPIA, or US state-law categories unless the user explicitly asks for overseas comparison.
- Do not output final launch clearance.

## Classification Labels

- `PROCEED`: May enter ordinary human compliance review.
- `ASSESSMENT REQUIRED`: Needs AI assessment, PIPIA, supplier review, IP/data review, MIIT/MLPS check, or policy approval before launch.
- `SPECIAL REVIEW`: Filing/security assessment, provincial CAC communication, high-risk sector, public opinion, deep synthesis, minors, important data, MLPS, telecom license, or cross-border issues are triggered.
- `STOP`: A P0 red line blocks launch.

## P0 One-Vote-Veto Checks

Return `STOP` if any of the following is true:

- Public-facing generative AI or deep synthesis service has no real-name authentication plan.
- Public-facing Web/App/mini-program service lacks ICP filing or App filing evidence where required.
- Paid AI service, SaaS subscription, API billing, or membership fee lacks ICP License / value-added telecom license where triggered.
- System has no MLPS 2.0 assessment plan where algorithm filing, generative AI security assessment, or public-facing high-risk AI service is triggered.
- Public-facing service uses an overseas or unfiled model API where China filing/security assessment is required.
- Training or fine-tuning uses sensitive personal information, children's personal information, medical data, biometric data, important data, or customer confidential data without lawful basis, separate consent, anonymization, PIPIA, classification/grading, and storage/export controls.
- The service can generate illegal or harmful content and lacks detect-intercept-dispose-log-report controls, including 24-hour reporting to local CAC and public security where required.
- The feature uses another person's face, voice, name, image, or identity characteristics without clear authorization.
- The service provides final medical diagnosis, prescription, financial decision, legal advice, credit decision, recruitment elimination, or similar high-impact decision without qualified human review.

## Triage Path

1. Identify AI type: generative AI, algorithm recommendation, deep synthesis, automated decision, internal assistant, vendor API, open-source model, or embedded product feature.
2. Identify audience: internal employees, enterprise customers, China public users, minors, regulated industry users, or overseas users.
3. Identify data: training data, fine-tuning data, prompts, outputs, logs, personal information, sensitive personal information, important data, commercial secrets, copyrighted content.
4. Identify launch channel: website, App, mini-program, SaaS/API, internal tool, embedded product, offline deployment.
5. Split the compliance tracks:
   - Algorithm recommendation filing.
   - Generative AI service filing/security assessment.
   - Deep synthesis marking and real-name authentication.
   - MIIT ICP filing/App filing and ICP License.
   - MLPS 2.0 and public security obligations.
   - PIPIA, important data, and cross-border data flow.
6. Check TC260-PG-20241A baseline: corpus security, model security, service security, quantitative testing, logs, emergency response.
7. Check adjacent modules: `privacy-legal`, `ip-legal`, `product-legal`, `commercial-legal`, `employment-legal` as needed.

## Output Format

```markdown
# AI Use-Case Triage

**CLASSIFICATION:** [PROCEED / ASSESSMENT REQUIRED / SPECIAL REVIEW / STOP]

## One-Line Conclusion
[State whether the item may enter human review, needs remediation, needs special review, or must stop.]

## Trigger Matrix
| Trigger | Hit? | Facts | China control point | Action |
|---|---:|---|---|---|

## Multi-Track Filing / Assessment / Launch Gates
| Track | Triggered? | Reason | Authority / entry | Missing materials |
|---|---:|---|---|---|
| Algorithm recommendation filing | | | Algorithm filing system / local CAC `[to verify]` | |
| Generative AI service filing / security assessment | | | Provincial CAC `[to verify]` | |
| Deep synthesis marking and real-name authentication | | | Deep synthesis rules / technical standards `[to verify]` | |
| ICP filing / App filing | | | MIIT / app filing channels `[to verify]` | |
| ICP License / value-added telecom license | | | MIIT `[to verify]` | |
| MLPS 2.0 assessment | | | Public security authority / testing institution `[to verify]` | |
| PIPIA / important data / data export | | | privacy-legal and data-security review | |

## P0 Gates
- [ ] Real-name authentication
- [ ] ICP filing / App filing
- [ ] ICP License for paid commercial service
- [ ] MLPS 2.0 assessment
- [ ] Content safety Stop-Filter and 24-hour disposal/report
- [ ] TC260-PG-20241A safety testing
- [ ] Visible marking and implicit watermark
- [ ] Training data source legality
- [ ] Important data classification and export control
- [ ] Vendor filing / no-training / deletion / audit
- [ ] Human review

## Next Steps
1. [Minimum remediation action]
2. [Questions requiring legal/compliance/security confirmation]
3. [Items requiring official-source verification]
```
