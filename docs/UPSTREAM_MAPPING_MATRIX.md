# Upstream Mapping Matrix

Status: synchronized with the scope decision accepted on 2026-07-13.

This matrix tracks responsibility mapping between upstream `claude-for-legal`
and `claude-for-legal-cn`. A deferred responsibility remains traceable here but
does not block the Phase 1 baseline when its target phase and current boundary are explicit.

| Upstream module | Current CN location | Phase 1 baseline | Deferred responsibility |
|---|---|---|---|
| `commercial-legal` | `commercial-legal` | China contract review, playbooks, renewal templates, root skills and agents are present. Agent frontmatter is restored. | Stateful matter lifecycle and agent persistence are Phase 1.5. External notifications are Phase 2. |
| `privacy-legal` | `privacy-legal` | PIPL/DSL/CSL triage, PIPIA, processing-relationship review, rights requests and policy monitoring are present. | Persistent matter lifecycle is Phase 1.5. Real legal/privacy providers are Phase 2. |
| `product-legal` | `product-legal` | China consumer, advertising, platform, data, algorithm, quality and launch review is present. | Local launch tracker and matter lifecycle are Phase 1.5. External product-system monitoring is Phase 2. |
| `corporate-legal` | `corporate-legal` plus historical implementation storage at `corporate-legal/phase-2/skills` | China company law and M&A responsibilities are root-discoverable; seven M&A root wrappers delegate to the maintained implementations. | External VDR/enterprise integrations are Phase 2. Historical storage does not lower module status. |
| `employment-legal` | `employment-legal` | China hiring, wage/hour, leave, handbook, investigation, termination, compensation and social-insurance responsibilities are present. | Optional local matter lifecycle is Phase 1.5. Substantive international expansion/EOR capability is Phase 2; Phase 1 retains safe intake and professional handoff only. |
| `regulatory-legal` | `regulatory-legal` | China source provenance, feed/diff/tracker/comments/closure workflow and policy review are present. | Production regulator feeds and enterprise notifications are Phase 2. |
| `ai-governance-legal` | `ai-governance-legal` | China algorithm, generative AI, deep-synthesis, security-assessment, PIPL/DSL/CSL and registry workflows are present. | Production filing/provider integrations are Phase 2. |
| `litigation-legal` | `litigation-legal` | China litigation/arbitration, preservation, hearing, confidential-evidence and enforcement responsibilities are present; compatibility commands remain root-discoverable. | Court/arbitration system integrations are Phase 2. |
| `ip-legal` | `ip-legal` | China trademark, patent, copyright, platform takedown, trade secret, customs and OSS responsibilities are present. | Local matter lifecycle is Phase 1.5. Registry/provider automation is Phase 2. |
| `legal-builder-hub` | `legal-builder-hub` | China-law skill QA, static source review, planning templates and safety boundaries are present. | Physical install/update/rollback/disable/uninstall and remote registry synchronization are Phase 2. |
| `law-student` | `law-student` | Root marketplace exposure, China legal education, 法考, claim-basis analysis, case study, writing practice and learning guardrails are present. | Richer learning analytics are optional later depth, not a Phase 1 blocker. |
| `legal-clinic` | `legal-clinic` | Root marketplace exposure, China clinic/legal-aid intake, supervision, confidentiality, deadline tracking and handoff are present. | External clinic case-management integration is Phase 2. |
| `external_plugins/cocounsel-legal` | `external_plugins/cocounsel-legal` | Intentionally isolated vendor content; excluded from the default China marketplace and covered by `external_plugins/README.md`. | Vendor-controlled evolution remains outside the first-party Phase 1 baseline. |

## Root Assets

| Asset | Phase 1 baseline | Deferred responsibility |
|---|---|---|
| `managed-agent-cookbooks` | Five cookbooks remain available with China-law boundaries and schema validation. | Real enterprise providers and automated delivery are Phase 2. |
| MCP configuration | Twelve root `.mcp.json` files are generated from `scripts/mcp-template.json` and `scripts/mcp-modules.json`; `legal-data` is a local sample server. | Commercial databases, WPS and enterprise systems are production integrations for Phase 2. |

## Maintenance Rule

For every upstream update, record whether the responsibility is:

- included in the Phase 1 baseline;
- mapped to a China-law equivalent;
- assigned to Phase 1.5;
- assigned to Phase 2;
- intentionally isolated as external/vendor content.

Do not use directory names, historical `phase-2` storage, or practice-setting
preferences as a proxy for module value or acceptance priority.
