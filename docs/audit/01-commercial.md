# Audit 01

Plugin: `commercial-legal`
Standard: `FAITHFUL_PORT_STANDARD` v1
Mode: REVIEW ONLY

## Revision History

| Date | Event | Overall | Reason |
|---|---|---|---|
| 2026-07-04 | Initial Review | ACTION REQUIRED | The initial review treated the missing standalone upstream `customize` skill as a direct parity defect. |
| 2026-07-04 | Reclassified under `FAITHFUL_PORT_STANDARD` v1 | Conditional PASS | Responsibility Mapping was accepted as the governing test. The preference-management responsibility appears mapped into the China-law cold-start / update workflow, but command-level verification remains an Observation or limited Gap rather than a proven Blocker. |

## Structure

The `commercial-legal` directory is preserved at the root level. Core plugin
assets are present:

- `.claude-plugin/plugin.json`
- `README.md`
- `CLAUDE.md`
- `skills/`
- `agents/`
- `references/`
- `hooks/hooks.json`
- `.mcp.json`
- `logs/.gitkeep`

The upstream agent set is preserved:

- `deal-debrief.md`
- `playbook-monitor.md`
- `renewal-watcher.md`

The upstream skill set is mostly preserved. The China-law port has 11 skills
while upstream has 12. The standalone upstream `skills/customize/SKILL.md` is
not present as a separate file.

The China-law port adds China-specific references, including contract playbooks,
approval and seal policy, NDA rules, SaaS data review, renewal deadline rules,
and test cases. These additions are not parity defects.

## Capability

The upstream capability is commercial contract and deal workflow support.

The China-law plugin preserves this capability through China Mainland contract
review, NDA review, SaaS/MSA review, vendor agreement review, renewal tracking,
escalation, stakeholder reporting, amendment history, matter workspace, and
supporting agents.

Capability status: Preserved.

## Responsibility

Preserved or mapped responsibilities include:

- collect commercial review preferences and operating context;
- route commercial review requests;
- review vendor agreements;
- review NDAs;
- review SaaS / MSA terms;
- flag escalations;
- track renewals;
- summarize for stakeholders;
- maintain amendment history;
- organize matter workspace outputs;
- monitor playbooks;
- debrief deals;
- watch renewals.

The main mapping issue is upstream `customize`.

Under literal file comparison, `customize` is missing. Under Responsibility
Mapping, the relevant responsibility is preference management and profile update.
The China-law implementation appears to consolidate that responsibility into the
cold-start interview / update workflow instead of maintaining a separate skill.

Assessment: Mapped, pending command-level verification.

## Operational Depth

Operational depth differs from upstream in the following ways:

- preference updates appear consolidated into a China-law onboarding/update path;
- China-specific playbooks are richer than upstream in some substantive areas;
- provider and connector behavior differs from upstream;
- the references layer is expanded for China-law contract operations.

These are Observations unless later runtime testing proves that the preference
management responsibility cannot be completed.

## Localization

China-law localization is strong. The plugin replaces upstream commercial legal
substance with China Mainland contract concepts, including:

- contract formation and performance risk;
- approval authority and company seal control;
- NDA and confidentiality obligations;
- SaaS and data processing concerns;
- dispute resolution and jurisdiction;
- renewal and deadline handling;
- escalation gates for local legal review.

Foreign-law terminology appears to be compatibility wording or negative
constraint context rather than controlling legal substance.

Localization status: Sufficient for Conditional PASS.

## Runtime

No command-path fix was performed in this audit.

Observed runtime posture:

- plugin manifest exists;
- `.mcp.json` exists;
- hooks file exists;
- agent files exist;
- no obvious root-level directory break was identified.

Remaining runtime question:

- confirm whether any README or command example invokes `customize` as a
  standalone commercial command that no longer exists.

## Governance

The plugin does not appear to violate `PROJECT_SCOPE.md`.

The added China-specific references and playbooks are acceptable v1 localization
assets. They do not constitute v2 provider integration or a specialized practice
pack by themselves.

## Risks

### Blocker

None proven under `FAITHFUL_PORT_STANDARD` v1.

### Gap

- Possible command-level gap if `customize` is referenced as a standalone command
  but no equivalent invocation is available.

### Observation

- `customize` is consolidated rather than preserved as a standalone skill.
- China-law playbooks expand some areas beyond upstream operational depth.
- Connector/provider behavior differs and should remain a v2+ concern unless
  runtime breaks.

### Enhancement

- Add explicit documentation showing how preference updates are performed in the
  China-law commercial workflow.
- Add a command-level smoke test for preference update / cold-start update flows.

## Lessons Learned

1. This plugin validated that Responsibility Equivalence is more accurate than
   literal skill parity. A missing file is not automatically a missing
   responsibility.
2. Later plugin audits should identify Capability, Responsibility, and
   Operational Depth separately before assigning severity.

## Overall

Conditional PASS
