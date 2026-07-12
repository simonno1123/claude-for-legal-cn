---
name: use-case-triage
description: >
  China AI use-case triage. Reads/writes use-case-registry.yaml, classifies launch gates, enforces non-lawyer approval/rejection gates, and routes to inventory, assessment, vendor review, privacy, IP, and product counsel.
argument-hint: "[AI use case / product requirement / vendor description]"
---

# /use-case-triage

## Mandatory Rules

- Apply `references/china-ai-governance-rules.md`.
- Default to China Mainland law and regulator practice.
- Do not classify by EU AI Act, NIST, FTC, GDPR DPIA, or US state-law categories unless the user explicitly asks for overseas comparison.
- Do not output final launch clearance.
- Read `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.
- Read/write `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/use-case-registry.yaml`.

## Registry Storage

Create if missing:

```yaml
use_cases: []
```

Each triage result should offer to add or update:

```yaml
use_cases:
  - id: uc-001
    name: "Customer support LLM"
    classification: "ASSESSMENT REQUIRED"
    status: conditional
    conditions:
      - "human review before customer commitment"
    red_lines: []
    related_systems: ["sys-001"]
    owner: "Product / Legal"
    decided_by: ""
    last_reviewed: "2026-07-09"
    next_review: "before public launch"
```

## Classification Labels

- `PROCEED`: May enter ordinary human compliance review.
- `ASSESSMENT REQUIRED`: Needs AI assessment, PIPIA, supplier review, IP/data review, MIIT/MLPS check, or policy approval before launch.
- `SPECIAL REVIEW`: Filing/security assessment, provincial CAC communication, high-risk sector, public opinion, deep synthesis, minors, important data, MLPS, telecom license, or cross-border issues are triggered.
- `STOP`: A P0 red line blocks launch.

Registry status mapping:

- `approved` only after legal/compliance approval is confirmed.
- `conditional` for `ASSESSMENT REQUIRED` or remediation conditions.
- `rejected` for `STOP` after legal/compliance confirmation.
- `watch` for insufficient facts or unverified rule status.

## P0 One-Vote-Veto Checks

Return `STOP` or `SPECIAL REVIEW` if any of the following is true:

- Public-facing generative AI or deep synthesis service has no real-name authentication plan.
- Public-facing Web/App/mini-program service lacks ICP filing or App filing evidence where required.
- Paid AI service, SaaS subscription, API billing, or membership fee lacks ICP License / value-added telecom license review.
- System has no MLPS 2.0 assessment plan where algorithm filing, generative AI security assessment, or public-facing high-risk AI service is triggered.
- Public-facing service uses an overseas or unfiled model API where China filing/security assessment is required.
- Training or fine-tuning uses sensitive personal information, children's personal information, medical data, biometric data, important data, or customer confidential data without lawful basis, separate consent, anonymization, PIPIA, classification/grading, and storage/export controls.
- The service can generate illegal or harmful content and lacks detect-intercept-dispose-log-report controls.
- The feature uses another person's face, voice, name, image, or identity characteristics without clear authorization.
- The service provides final medical diagnosis, prescription, financial decision, legal advice, credit decision, recruitment elimination, or similar high-impact decision without qualified human review.

## Triage Path

1. Search `use-case-registry.yaml` for an existing or similar entry.
2. Search `ai-systems.yaml` for related systems; if absent, suggest `/ai-governance-legal:ai-inventory add`.
3. Identify AI type, audience, data, launch channel, vendor/model source, and human review.
4. Split compliance tracks:
   - Algorithm recommendation filing.
   - Generative AI service filing/security assessment.
   - Deep synthesis marking and real-name authentication.
   - MIIT ICP filing/App filing and ICP License.
   - MLPS 2.0 and public security obligations.
   - PIPIA, important data, and cross-border data flow.
5. Check policy registry red lines and approved/conditional/never categories.
6. Produce classification and conditions.
7. Offer to write/update registry entry.

## Non-Lawyer Decision Gate

Before recording `approved` or `rejected`, read the profile user role. If the user
is not a lawyer/legal professional, require confirmation that legal/compliance has
reviewed. If not confirmed, output an attorney brief and record only `conditional`
or `watch`.

## Output Format

```markdown
# AI Use-Case Triage

> **复核提示**
> - **来源：** use-case-registry.yaml / ai-systems.yaml / 用户提供
> - **读取范围：** [registry/system records]
> - **待判断事项：** [approval/rejection gates and unresolved facts]
> - **时效性：** [filing/status items needing verification]
> - **行动前：** no launch, rejection, or approval without authorized review

**CLASSIFICATION:** [PROCEED / ASSESSMENT REQUIRED / SPECIAL REVIEW / STOP]
**Registry match:** [Direct / Near / New]

## Trigger Matrix
| Trigger | Hit? | Facts | China control point | Action |
|---|---:|---|---|---|

## Multi-Track Filing / Assessment / Launch Gates
| Track | Triggered? | Reason | Authority / entry | Missing materials |
|---|---:|---|---|---|

## Registry Update
| Field | Value |
|---|---|
| Proposed status | approved / conditional / rejected / watch |
| Conditions | |
| Next review | |

## Next Steps
1. `/ai-governance-legal:ai-inventory add|classify`
2. `/ai-governance-legal:aia-generation`
3. `/ai-governance-legal:vendor-ai-review`
```
