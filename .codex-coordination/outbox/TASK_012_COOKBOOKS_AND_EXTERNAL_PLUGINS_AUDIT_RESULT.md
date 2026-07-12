# TASK_012_COOKBOOKS_AND_EXTERNAL_PLUGINS_AUDIT_RESULT

Artifact Type: RESULT
Producer: Codex
Task: TASK_012_COOKBOOKS_AND_EXTERNAL_PLUGINS_AUDIT
Mode: READ ONLY audit; no target files modified
Project: /Users/zhang/Documents/claude-for-legal-cn
Standard: docs/FAITHFUL_PORT_STANDARD.md
Next Receiver: Gemini

This artifact reports execution facts and a factual recommendation only. It is not a REVIEW and not a DECISION.

## Structure

### managed-agent-cookbooks

Audited directories:

- `managed-agent-cookbooks/diligence-grid/`
- `managed-agent-cookbooks/docket-watcher/`
- `managed-agent-cookbooks/launch-radar/`
- `managed-agent-cookbooks/reg-monitor/`
- `managed-agent-cookbooks/renewal-watcher/`

Each cookbook has:

- `README.md`
- `agent.yaml`
- `steering-examples.json`
- `subagents/` with expected subagent YAML manifests

Top-level cookbook README states China-law positioning, China Mainland default jurisdiction, non-reliance on common-law privilege, human review gates, env-var connector placeholders, and no production MCP implementation claims. See `managed-agent-cookbooks/README.md:7-13`, `managed-agent-cookbooks/README.md:25-33`, `managed-agent-cookbooks/README.md:35-60`.

### external_plugins/cocounsel-legal

Audited files:

- `external_plugins/cocounsel-legal/.claude-plugin/plugin.json`
- `external_plugins/cocounsel-legal/.mcp.json`
- `external_plugins/cocounsel-legal/README.md`
- `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md`

The external plugin is structurally complete for a vendor plugin. It is not listed in `.claude-plugin/marketplace.json`; the default marketplace lists core CN plugins only. `docs/UPSTREAM_MAPPING_MATRIX.md:28` already marks this path as `保留 / 待核对 / 偏移风险`.

## Capability

### managed-agent-cookbooks

Capability mapping is present and China-law oriented:

- `reg-monitor`: China regulatory monitoring and digest generation.
- `renewal-watcher`: China contract renewal / termination reminders.
- `diligence-grid`: China M&A diligence grid and VDR/table extraction.
- `launch-radar`: China product launch legal-risk radar.
- `docket-watcher`: China litigation/arbitration docket and deadline monitoring.

The cookbook index maps each cookbook to the corresponding root module and China connector suggestions at `managed-agent-cookbooks/README.md:17-23`.

### external_plugins/cocounsel-legal

Capability is vendor-specific Westlaw / U.S. legal research, not China-law legal research. `external_plugins/cocounsel-legal/README.md:5` explicitly says it is for Westlaw / U.S. law research and not part of the default CN install list. It also directs China legal research to CN sources.

## Responsibility

### Preserved / localized responsibilities

managed-agent-cookbooks preserve operational responsibilities as deployable managed-agent templates:

- Reader / analyzer / writer separation is explicit in the top-level README at `managed-agent-cookbooks/README.md:25-33`.
- Human review and non-final-output boundaries are explicit at `managed-agent-cookbooks/README.md:35-43`.
- Deployment as templates, not production services, is explicit at `managed-agent-cookbooks/README.md:55-60`.
- `diligence-grid` preserves VDR watch and table extraction responsibilities while pointing to CN corporate/M&A context and the corporate tabular-review implementation. See `managed-agent-cookbooks/diligence-grid/agent.yaml:13-42` and `managed-agent-cookbooks/diligence-grid/agent.yaml:77-100`.
- `launch-radar` preserves product launch triage responsibilities with China regulatory trigger examples and human review gates. See `managed-agent-cookbooks/launch-radar/README.md:9-12`, `managed-agent-cookbooks/launch-radar/README.md:41-54`.

### Missing responsibilities

No missing cookbook-level responsibility was identified from the audited files.

For `external_plugins/cocounsel-legal`, China-law research responsibility is intentionally not implemented in this vendor plugin. The README positions it outside the default CN research flow. This should be treated as an external/vendor boundary decision rather than a missing CN research capability if Gemini accepts the current governance framing.

### Foreign-law assumptions

- Cookbooks: no U.S. legal default framework was found driving the cookbook workflows. Foreign-law / common-law references in cookbooks are mainly negative constraints, for example `managed-agent-cookbooks/launch-radar/README.md:53`.
- CoCounsel: U.S. law is the actual default substance of the external plugin. See `external_plugins/cocounsel-legal/README.md:8-19` and `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md:4-17`.

## Localization

### managed-agent-cookbooks

Localization status: substantially localized.

Evidence:

- Top-level default jurisdiction is China Mainland: `managed-agent-cookbooks/README.md:7-13`.
- Connectors are CN-oriented: `managed-agent-cookbooks/README.md:17-23`.
- Diligence grid uses China Mainland and claude-for-legal-cn rules: `managed-agent-cookbooks/diligence-grid/agent.yaml:77`.
- Launch radar uses CN trigger examples including minors, personal information, algorithm recommendation, auto-renewal, live-commerce, advertising, product recall, CCC, medical / financial / education categories: `managed-agent-cookbooks/launch-radar/README.md:9-12`, `managed-agent-cookbooks/launch-radar/README.md:47`.
- Docket watcher, reg monitor, and renewal watcher use China Mainland connectors and review gates.

Classified occurrences:

- `managed-agent-cookbooks/launch-radar/README.md:19`: foreign project-management tools are allowed only as optional extensions for foreign-invested or outbound teams, not default CN configuration. Classification: compatibility note.
- `managed-agent-cookbooks/launch-radar/README.md:53`: common-law privilege / work-product disclaimer. Classification: negative constraint.
- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml` contains `mcp_server_name: box` and an MCP server named `box` while pointing to `${WPS_CLOUD_DOCS_MCP_URL}`. Classification: residue requiring remediation or at least reviewer confirmation, because `CHINA_LOCALIZATION_STATUS.md:108-112` claims old international SaaS naming was cleared.
- Several cookbooks retain `imanage` as an optional connector. Classification: compatibility / optional DMS connector, not default legal framework.

### external_plugins/cocounsel-legal

Localization status: intentionally isolated, not localized in substance.

Evidence:

- README CN boundary notice: `external_plugins/cocounsel-legal/README.md:3-5`.
- U.S. federal/state law and Westlaw substance: `external_plugins/cocounsel-legal/README.md:8-19`.
- Skill description says use for U.S. law: `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md:4-5`.
- Skill routes foreign/non-U.S. law away from Deep Research: `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md:48-49`.

Classification: isolated external/vendor content, subject to governance confirmation. If v1 requires every retained external plugin to be China-law localized internally, this would be a Gap. If v1 accepts intentional external/vendor preservation, it is an Observation.

## Runtime

Validation performed:

- JSON validation passed for:
  - `external_plugins/cocounsel-legal/.claude-plugin/plugin.json`
  - `external_plugins/cocounsel-legal/.mcp.json`
  - all five cookbook `steering-examples.json`
- YAML validation via Ruby Psych passed for all cookbook `agent.yaml` and subagent YAML files.
- Referenced deployment script exists: `scripts/deploy-managed-agent.sh`.
- Referenced module/skill/agent paths checked and found present, including:
  - `corporate-legal/phase-2/skills/tabular-review/references/ma-diligence-columns.md`
  - `commercial-legal/agents/renewal-watcher.md`
  - `commercial-legal/skills/renewal-tracker`
  - `commercial-legal/skills/escalation-flagger`
  - `commercial-legal/skills/stakeholder-summary`
  - `product-legal/agents/launch-watcher.md`
  - `product-legal/skills/is-this-a-problem`
  - `regulatory-legal/agents/reg-change-monitor.md`
  - `regulatory-legal/skills/gap-surfacer`
  - `regulatory-legal/skills/policy-diff`
  - `litigation-legal/agents/docket-watcher.md`
  - `litigation-legal/skills/portfolio-status`
  - `litigation-legal/skills/matter-update`

Runtime concerns:

- `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md:6-8` allows `Bash` and requires polling/sleep behavior. As an external vendor plugin this may be acceptable, but it should remain outside default CN marketplace exposure.
- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml` uses `box` naming while configured to WPS URL. This is not a broken path, but it is a connector-label mismatch and foreign SaaS naming residue.

## Governance

### managed-agent-cookbooks

Governance mostly aligns with `PROJECT_SCOPE` and `FAITHFUL_PORT_STANDARD`:

- Cookbooks are documented as templates, not production products.
- MCP/provider integrations are placeholders via environment variables.
- Human review gates are preserved.
- Responsibilities are not framed as v2-only.

Potential governance issue:

- `CHINA_LOCALIZATION_STATUS.md:111-112` claims old international SaaS naming was cleared, but `box` remains in `diligence-grid/subagents/doc-reader.yaml`. This weakens that claim.

### external_plugins/cocounsel-legal

Governance is mostly contained:

- README says this is a third-party Westlaw / U.S.-law plugin and not default CN install: `external_plugins/cocounsel-legal/README.md:5`.
- Default marketplace does not include `cocounsel-legal`.
- `docs/UPSTREAM_MAPPING_MATRIX.md:28` correctly flags this path as pending review / deviation risk.

Governance decision needed:

- Gemini should decide whether v1 accepts `external_plugins/cocounsel-legal` as intentionally preserved external/vendor content, or requires a stronger explicit out-of-scope marker inside the skill itself.

## Risks

### Blocker

None identified.

### Gap

1. `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml` retains `box` as MCP tool/server naming while pointing to `${WPS_CLOUD_DOCS_MCP_URL}`. This is a foreign SaaS naming residue and connector-label mismatch. It does not remove a responsibility, but it contradicts the repository's stated cleanup claim.

### Observation

1. `external_plugins/cocounsel-legal` remains U.S.-law / Westlaw content by design. It is isolated from the default marketplace and README warns CN users not to use it for China law.
2. `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md` itself does not contain the README's Chinese boundary notice. If the plugin is installed directly, the skill-level instructions remain purely Westlaw/U.S.-law oriented.
3. Cookbooks use deployment placeholders and environment-variable MCP URLs, consistent with v1 non-goals for real provider integration.
4. Optional `imanage` connector references remain in diligence/renewal contexts. These appear to be optional DMS compatibility references, not default China-law assumptions.

### Enhancement

1. Add a short skill-level boundary note to `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md` mirroring README: not default CN legal research; use only when user explicitly requests CoCounsel / Westlaw / U.S. law.
2. Add a small `external_plugins/README.md` explaining vendor-plugin isolation policy.
3. Consider a lightweight managed-agent cookbook smoke test that checks YAML parse, path existence, default marketplace exclusion of vendor plugins, and forbidden SaaS label residue.

## Lessons Learned

1. External vendor plugins should be audited under a separate classification: `intentionally preserved external/vendor content`, not ordinary China-law plugin localization.
2. README-level isolation is useful but not always enough; skill-level boundary language may be needed when a plugin can be installed directly.
3. Connector names matter. Even when URLs are placeholders, foreign SaaS labels can undermine localization claims and should be treated as governance evidence, not just cosmetic text.
4. Managed-agent cookbooks should be checked both for legal localization and for operational path validity because they bridge multiple root modules.

## Overall

Factual recommendation: Conditional PASS

Rationale:

- No Blocker found.
- Managed-agent cookbooks are structurally complete, China-law oriented, and runtime references validated.
- CoCounsel is not localized in substance, but it is isolated as a non-default external vendor plugin and already flagged in governance docs.
- Conditional status is due to one connector-label residue (`box`) and the need for Gemini to confirm that CoCounsel should remain preserved as external/vendor content rather than be treated as an unlocalized v1 module.

NEXT RECEIVER: Gemini
