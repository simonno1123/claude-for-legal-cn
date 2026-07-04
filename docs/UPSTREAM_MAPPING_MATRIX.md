# Upstream Mapping Matrix

This matrix tracks the current relationship between upstream `claude-for-legal`
and `claude-for-legal-cn`. It is a governance document for the v1 Faithful Port
baseline, not a claim that every row is already complete.

Status legend:

- **保留**: the upstream concept/path is preserved or intentionally mirrored.
- **已中国化**: the capability has China-law substance.
- **待核对**: parity must still be checked against the latest upstream version.
- **偏移风险**: current CN structure or positioning diverges from Faithful Port.

| Upstream module | Current CN location | Current status | Notes / recommendation |
|---|---|---|---|
| `commercial-legal` | `commercial-legal` | 保留 / 已中国化 / 待核对 | Directory is preserved and China contract substance is present. Verify every upstream skill, agent, workflow, and doc has a one-to-one responsibility mapping. |
| `privacy-legal` | `privacy-legal` | 保留 / 已中国化 / 待核对 | China PIPL/DSL/CSL framing is present. Check whether retained compatibility names such as `dsar-response` remain acceptable under Faithful Port. |
| `product-legal` | `product-legal` | 保留 / 已中国化 / 待核对 | China product, consumer, advertising, platform, data, and algorithm logic is present. Broken cross-module references should be handled in a later structure/runtime pass. |
| `corporate-legal` | `corporate-legal` plus `corporate-legal/phase-2` | 已中国化 / 偏移风险 / 待核对 | Core China company-law work exists, but some M&A/diligence upstream responsibilities are moved under `phase-2`. Decide whether v1 should restore root-level command parity. |
| `employment-legal` | `employment-legal` | 保留 / 已中国化 / 待核对 | China labor-law substance is present. Confirm expansion and matter-workspace responsibilities against upstream instead of ranking by local business priority. |
| `regulatory-legal` | `regulatory-legal` | 保留 / 已中国化 / 待核对 | China regulator-source logic is present. Verify upstream source-monitoring and policy-diff responsibilities remain equivalent. |
| `ai-governance-legal` | `ai-governance-legal` | 保留 / 已中国化 / 待核对 | China AI governance content is present. Confirm upstream skill count, agent expectations, and command examples. |
| `litigation-legal` | `litigation-legal` | 保留 / 已中国化 / 待核对 | China litigation/arbitration substance is present. Compatibility names such as `subpoena-triage`, `deposition-prep`, and `privilege-log-review` should be reviewed as v1 parity decisions, not product enhancements. |
| `ip-legal` | `ip-legal` | 保留 / 已中国化 / 待核对 | China trademark, patent, copyright, platform takedown, trade secret, and OSS logic is present. Verify upstream workflow parity. |
| `legal-builder-hub` | `legal-builder-hub` | 保留 / 已中国化 / 偏移风险 | Directory is present, but docs currently frame it as a promoted first-sequence governance module. For v1, treat it as an upstream module with China-governance substance, not as a higher-priority product layer. |
| `law-student` | `phase-2/law-student` | 已中国化 / 偏移风险 / 待核对 | Current CN content exists under `phase-2`. Faithful Port requires a decision on whether to restore root-level source parity or explicitly document a temporary directory exception. Do not treat the module as lower value. |
| `legal-clinic` | `phase-2/legal-clinic` | 已中国化 / 偏移风险 / 待核对 | Current CN content exists under `phase-2`. Faithful Port requires a decision on directory parity and marketplace inclusion. Do not treat clinic/legal aid workflows as lower value. |
| `external_plugins/cocounsel-legal` | `external_plugins/cocounsel-legal` | 保留 / 待核对 / 偏移风险 | Vendor U.S.-law content remains isolated and is not in the CN default marketplace. Decide whether v1 preserves it as an external vendor plugin, adds a China-law equivalent, or documents it as out of China-port scope. |

## Current Governance Findings

- CN has meaningful China-law substance, but current documentation still reflects a product-priority split rather than a pure Faithful Port baseline.
- `law-student` and `legal-clinic` are the clearest directory parity risks because upstream uses root-level modules while CN currently stores them under `phase-2/`.
- `corporate-legal/phase-2` is a second parity risk because some upstream corporate/M&A responsibilities are not exposed at the root skill path.
- MCP provider routing and legal database integrations should remain v2+ expansion items unless the upstream capability itself requires the placeholder interface.

## Next Review Step

Build a row-level inventory for every upstream:

- plugin manifest;
- README / CLAUDE.md;
- each skill;
- each agent;
- hooks and workflows;
- MCP config;
- managed-agent cookbook.

Each item should be marked `ported`, `mapped with China-law equivalent`,
`temporarily deferred`, or `requires decision`.

