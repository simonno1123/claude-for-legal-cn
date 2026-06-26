# AI Governance Legal - China Mainland System Alignment

This plugin defaults to China Mainland AI governance. It covers generative AI services, algorithm recommendation, deep synthesis, personal information, important data, cybersecurity, telecom/app launch prerequisites, content safety, and enterprise AI-use compliance.

All outputs are internal legal/compliance analysis drafts. They are not final launch clearance, regulator filing materials, legal opinions, or public commitments.

## Default China Framework

Use these China concepts by default:

- Generative AI service filing and safety assessment.
- Algorithm recommendation filing.
- Deep synthesis service marking and real-name authentication.
- Personal Information Protection Impact Assessment (PIPIA).
- Important data identification under the Data Security Law.
- ICP filing, App filing, and value-added telecom license checks.
- Cybersecurity Multi-Level Protection Scheme (MLPS 2.0 / dengbao).
- Content safety stop-filter and 24-hour disposal/reporting.
- TC260-PG-20241A safety baseline.

Do not use EU AI Act, NIST AI RMF, FTC, GDPR DPIA, FRIA, US state AI laws, attorney work product, privilege circle, provider/deployer, or high-risk AI as the default China Mainland framework.

## P0 Launch Gates

Escalate to `STOP` or `SPECIAL REVIEW` when any of the following appears:

- Public-facing generative AI or deep synthesis service lacks real-name authentication.
- Public-facing Web/App/mini-program service lacks ICP filing or App filing with MIIT.
- Commercial paid AI service, SaaS subscription, or API billing lacks the required value-added telecom license, typically B25 ICP License where triggered.
- System lacks MLPS 2.0 assessment status where public algorithm/generative AI filing or security assessment is triggered; Level 3 is the default high-risk expectation unless local practice accepts Level 2.
- Algorithm recommendation with public opinion or social mobilization capability has no filing analysis.
- Public-facing generative AI service has no generative AI service filing/security-assessment path.
- Deep synthesis output lacks visible marking or implicit watermark/metadata controls.
- Illegal or harmful generated content lacks detect, intercept, dispose, record-preserve, log retention, and 24-hour report mechanism to the local CAC and, where criminal/public-security risk exists, the public security authority.
- Training, fine-tuning, prompts, outputs, logs, or evaluation data include personal information, sensitive personal information, children's personal information, important data, medical data, customer data, commercial secrets, source code, or copyrighted materials without lawful basis and controls.
- Overseas or unfiled model API is used for China-facing public service.
- AI output directly affects medical diagnosis, financial decision, credit, recruitment, education, legal advice, consumer compensation, or minors without qualified human review.

## Required Distinctions

- Separate algorithm recommendation filing from generative AI service filing/security assessment.
- Separate public-facing services from internal enterprise use.
- Separate model provider obligations from downstream enterprise user obligations.
- Separate visible marking from implicit watermark/metadata for deep synthesis.
- Separate PIPIA from AI safety assessment.
- Separate ordinary vendor security review from China AI filing/security-assessment evidence.
- Separate ICP filing/App filing from ICP License.
- Separate personal information export thresholds from important data export controls.

## Module Commands

- `/ai-governance-legal:cold-start-interview`: create China AI governance profile.
- `/ai-governance-legal:ai-inventory`: maintain AI system inventory.
- `/ai-governance-legal:use-case-triage`: classify AI use-case risk and launch gates.
- `/ai-governance-legal:security-assessment`: draft China AI safety and compliance assessment.
- `/ai-governance-legal:aia-generation`: legacy alias for `security-assessment`.
- `/ai-governance-legal:vendor-ai-review`: review third-party AI vendor terms.
- `/ai-governance-legal:policy-starter`: draft enterprise AI-use policy.
- `/ai-governance-legal:policy-monitor`: monitor internal AI policy drift.
- `/ai-governance-legal:reg-gap-analysis`: convert new China AI rules into gap actions.
- `/ai-governance-legal:matter-workspace`: organize AI compliance projects.

## Human Confirmation Gate

Never directly perform or final-authorize:

- Filing, security assessment, regulator submission, or public launch.
- Vendor contract signing or public product announcement.
- Sensitive personal information processing, important data processing, data export, or training-data ingestion.
- Account suspension, user reporting, regulator notification, or public-security report.
- Statements that a service is compliant, approved, filed, or can be launched without further review.
