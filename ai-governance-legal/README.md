# AI Governance Legal (China Mainland)

This plugin supports China Mainland AI governance workflows for enterprise legal, compliance, security, data, and product teams. It covers generative AI services, algorithm recommendation, deep synthesis, vendor AI procurement, enterprise AI-use policy, personal information, important data, content safety, MIIT launch prerequisites, MLPS 2.0, and cross-border data routing.

> Professional note: outputs are internal compliance drafts. Filing, launch, vendor signing, regulator submission, data export, security assessment, and public commitments require review by legal, compliance, security owners, and China-qualified counsel where needed.

## Main Commands

| Command | Purpose |
|---|---|
| `/ai-governance-legal:cold-start-interview` | Single entry for China AI governance profile setup and customization |
| `/ai-governance-legal:ai-inventory` | Maintain AI system inventory |
| `/ai-governance-legal:use-case-triage` | Triage AI use cases and launch gates |
| `/ai-governance-legal:security-assessment` | Draft China AI safety and compliance assessment |
| `/ai-governance-legal:aia-generation` | Legacy alias for `security-assessment` |
| `/ai-governance-legal:vendor-ai-review` | Review third-party AI tools, model APIs, SaaS AI, cloud AI, and private deployments |
| `/ai-governance-legal:policy-starter` | Draft enterprise AI-use policy |
| `/ai-governance-legal:policy-monitor` | Monitor policy drift, vendor drift, and regulatory change impact |
| `/ai-governance-legal:reg-gap-analysis` | Convert China AI regulatory changes into remediation actions |
| `/ai-governance-legal:matter-workspace` | Organize an AI compliance project workspace |

`/ai-governance-legal:customize` is kept only as a compatibility placeholder. It redirects users to `/ai-governance-legal:cold-start-interview` and must not create a second configuration profile.

## Phase 1 Boundaries

The default framework is China Mainland law and regulator practice. EU AI Act, NIST AI RMF, FTC, GDPR DPIA, FRIA, US state AI laws, attorney work product, privilege circle, provider/deployer, and high-risk AI are not default frameworks. They may appear only as overseas or comparative-law references when the user asks for them.

## China Launch Gates

- Algorithm recommendation filing and generative AI service filing/security assessment are separate tracks.
- Deep synthesis requires real-name authentication, visible marking, and implicit watermark/metadata where required.
- Public-facing Web/App/mini-program services must check ICP filing and App filing.
- Paid SaaS/API/membership AI services must check value-added telecom license / ICP License triggers.
- Public-facing or high-risk AI systems must check MLPS 2.0 status; Level 3 is the default high-risk expectation unless local practice accepts Level 2 or transitional evidence.
- Content safety must include detect, intercept, dispose, preserve logs, and report to local CAC/public security where required.
- Important data cannot use the ordinary personal-information export exemption path.
- 2024 CAC cross-border data flow thresholds are treated as effective baseline rules.

## Quick Start

```bash
/ai-governance-legal:cold-start-interview
/ai-governance-legal:use-case-triage "Customer support plans to use an LLM to answer user complaints"
/ai-governance-legal:vendor-ai-review "Model API service terms"
/ai-governance-legal:security-assessment "Public-facing AI image generation service"
```

## References

- `references/china-ai-governance-rules.md`
- `references/currency-watch.md`
- `references/test-cases-cn.md`
