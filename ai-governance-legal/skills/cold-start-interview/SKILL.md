---
name: cold-start-interview
description: >
  Single entry for China AI governance profile setup and customization. Writes the persistent profile, initializes inventory/registry/playbook state files, supports --redo and --check-integrations, and learns from seed documents.
argument-hint: "[--redo | --check-integrations | --full | enterprise / product / AI system description]"
---

# /cold-start-interview

## Mandatory Rules

- Default to China Mainland AI, data, personal information, telecom/app, cybersecurity, and content-safety rules.
- Do not ask EU AI Act, NIST, FTC, GDPR DPIA, or US state-law questions as default configuration fields.
- Write and update one profile only: `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`.
- Create parent directories as needed.
- `customize` updates this same profile; it must not create a second profile.
- Do not overwrite existing `ai-systems.yaml`, `use-case-registry.yaml`, `vendor-ai-playbook.yaml`, or `policy-sweep-log.yaml` unless the user explicitly confirms.

## Modes

### `--check-integrations`

1. Inspect declared integrations in `.mcp.json`: `legal-data` and `wps-cloud-docs`.
2. Mark an integration as `已连接` only if a real tool call succeeds in the current session.
3. If a connector is declared but untested, mark `已配置未核验`.
4. If unavailable, document fallback: user-provided files, local paths, and manual official-source verification.
5. Update `## 可用集成` in the persistent profile.

### `--redo`

Redo one section or the full profile. Preserve existing state files. If the user changes owners, thresholds, approved use categories, or vendor positions, flag affected inventory and registry records for re-review.

### Default / `--full`

Run the full setup. If an existing profile contains `[PLACEHOLDER]` or `[PENDING]`, offer resume. If populated, ask whether to update instead of replacing.

## Seed Documents To Learn From

Ask for paths, uploads, or pasted content for:

- AI use policy or acceptable-use policy.
- Existing AI system inventory or approved tool list.
- Prior China AI compliance assessment, safety assessment, PIPIA, or launch review.
- Vendor AI agreement, model API terms, DPA, security whitepaper, or procurement checklist.
- Content safety, MLPS, ICP/App filing, real-name authentication, complaint handling, and incident response materials.
- Public commitments, product notices, user agreements, privacy notices, and model/service descriptions.

For every seed document, record: location, date reviewed, owner, and what profile section it informed.

## Interview Dimensions

1. Enterprise profile: entity, industry, registered location, operating regions, public-facing products, paid services.
2. AI role: self-developed model, application service provider, third-party tool buyer, internal user, technical support provider.
3. AI type: generative AI, algorithm recommendation, deep synthesis, intelligent customer service, recruiting screening, risk scoring, code generation, office assistant.
4. Launch channel: internal tool, website, App, mini-program, SaaS/API, embedded product, offline deployment.
5. Infrastructure prerequisites: ICP filing, App filing, ICP License/value-added telecom license, MLPS 2.0 level/report status.
6. Data source: training data, fine-tuning data, user input, customer data, employee data, personal information, sensitive personal information, important data, trade secrets, copyrighted content.
7. Data export: overseas model API, overseas support, overseas storage, group HQ analytics, PI export count since Jan 1, sensitive PI count, important data status.
8. Regulatory triggers: public service, public opinion/social mobilization, minors, medical, financial, education, recruiting, legal, credit, consumer compensation.
9. Vendor: model API, cloud service, private deployment, open-source model, training/retention/export/deletion/audit clauses.
10. Controls: AI-use policy, prohibited uses, approval flow, human review, log retention, incident response, complaints, real-name authentication, visible marking, implicit watermark.

## Persistent Profile Structure

Write:

```markdown
# AI Governance Practice Profile - China Mainland

## Enterprise Profile
## AI Governance Team And Owners
## Available Integrations
## AI System Inventory Location
Inventory file: ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/ai-systems.yaml
## Use Case Registry
Registry file: ~/.claude/plugins/config/claude-for-legal/ai-governance-legal/use-case-registry.yaml
## China AI Launch Gates
## Impact Assessment House Style
## Vendor AI Governance Playbook
## AI Policy Commitments
## Outputs And Policy Sweep
Outputs folder:
Last policy sweep:
gaps_found:
## Seed Documents
## Matter Workspaces
```

Initialize missing state files:

```yaml
systems: []
```

```yaml
use_cases: []
```

```yaml
vendor_positions: []
```

```yaml
sweeps: []
```

## Output Format

```markdown
# China AI Governance Profile

> **复核提示**
> - **来源：** 用户提供 / 企业制度库 / 官方来源待核验
> - **读取范围：** [seed documents and config sections]
> - **待判断事项：** [PENDING items]
> - **时效性：** [rules or practices needing verification]
> - **行动前：** first live use should confirm inventory, registry, and launch gates

## Enterprise And Role
...

## State Files Initialized
| File | Status | Notes |
|---|---|---|

## Next Steps
1. `/ai-governance-legal:ai-inventory`
2. `/ai-governance-legal:use-case-triage`
3. `/ai-governance-legal:aia-generation`
4. `/ai-governance-legal:vendor-ai-review`
```
