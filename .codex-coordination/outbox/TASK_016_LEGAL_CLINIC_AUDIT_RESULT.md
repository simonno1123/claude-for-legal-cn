# TASK_016_LEGAL_CLINIC_AUDIT_RESULT

ARTIFACT TYPE: RESULT  
PRODUCER: Codex  
NEXT RECEIVER: Gemini  
MODE: READ ONLY  
PROJECT: `/Users/zhang/Documents/claude-for-legal-cn`

## Structure

Upstream is root-level `legal-clinic/`; CN is still at [phase-2/legal-clinic](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic). CN has the same 16 skill names as upstream, plus `.mcp.json`, hooks, deadline/reference files.

Root parity is not preserved: [.claude-plugin/marketplace.json](/Users/zhang/Documents/claude-for-legal-cn/.claude-plugin/marketplace.json:8) lists root plugins through `law-student`, but no `legal-clinic` entry.

CN docs still mark it as phase-2: [PROJECT_USAGE_GUIDE.md](/Users/zhang/Documents/claude-for-legal-cn/PROJECT_USAGE_GUIDE.md:38), [UPSTREAM_MAPPING_MATRIX.md](/Users/zhang/Documents/claude-for-legal-cn/docs/UPSTREAM_MAPPING_MATRIX.md:27).

## Capability

Capability is directionally present: Chinese legal clinic / legal aid / public legal service workflows are stated in [README.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/README.md:3) and [CLAUDE.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/CLAUDE.md:5).

China mapping is appropriate: 中国高校法律诊所、法律援助、公服咨询、12348、司法局、法援中心、仲裁委、法院诉服等 are present.

## Responsibility

Preserved names, but several upstream responsibilities are materially under-implemented.

- `client-intake`: CN captures basic fields and output shell at [client-intake/SKILL.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/skills/client-intake/SKILL.md:11). Upstream includes practice-area routing, cross-area spotting, conflict checks, triage, supervision flags, and mandatory deadline handoff at upstream lines 46-130.
- `deadlines`: CN only says source/verification required and outputs a table at [deadlines/SKILL.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/skills/deadlines/SKILL.md:11). Upstream has add/report/update/complete/close modes, ledger writes, duplicate checks, warning rollups and integration at upstream lines 14-173.
- `supervisor-review-queue`: CN has priority ordering only at [supervisor-review-queue/SKILL.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/skills/supervisor-review-queue/SKILL.md:9). Upstream has activation by supervision model, queue schema, approve/edit/return and logging at upstream lines 14-108.
- `semester-handoff`: CN lists handoff fields at [semester-handoff/SKILL.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/skills/semester-handoff/SKILL.md:10). Upstream writes per-case memos, cohort summary, reads deadlines/comms, routes to review, and blocks invented handoffs at upstream lines 14-191.
- `cold-start-interview`: CN collects profile fields at [cold-start-interview/SKILL.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/skills/cold-start-interview/SKILL.md:10), but does not restore config persistence, supervisor-only setup gate, supervision model, seed docs, integration checks, or state paths that upstream requires.

## Operational Depth

This is not merely depth difference. Several operational workflows are reduced to static checklists, losing stateful behavior and routing.

CN total skill content is 306 lines; upstream is 2662 lines. The line count is not itself a defect, but it matches observed loss of modes, ledgers, queues, logs, handoffs, review actions, and persistence.

## Localization

Localization is strong directionally. CN default law is mainland China, with explicit exclusion of U.S. clinic/student-practice/privilege defaults at [CLAUDE.md](/Users/zhang/Documents/claude-for-legal-cn/phase-2/legal-clinic/CLAUDE.md:9). No active U.S./ABA/Westlaw/Clio residue was found in CN `phase-2/legal-clinic`.

## Runtime

JSON validation passed for:

- `phase-2/legal-clinic/.claude-plugin/plugin.json`
- `phase-2/legal-clinic/.mcp.json`
- `phase-2/legal-clinic/hooks/hooks.json`

Runtime risk remains: command names in CN README use `/legal-clinic:*`, but plugin is not root-level and not marketplace registered. This likely prevents normal discovery/install parity.

## Governance

There is clear Phase-2 governance drift. Current docs say phase-2 is not devaluation, but the module is still not root-exposed. After `law-student` promotion, README also has stale wording that `law-student` remains phase-2, though that is outside this audit’s scope.

## Risks

### Blocker

- Root marketplace discoverability missing for `legal-clinic`.
- Deadline ledger responsibility is not restored as an operational workflow.
- Supervisor review queue lacks approve/edit/return/log workflow and supervision-model activation.

### Gap

- Client intake lacks practice-area routing, cross-area spotting depth, mandatory deadline handoff, and verification/supervision output.
- Cold-start lacks persisted clinic profile, supervision model, seed docs, integration verification, and setup gate.
- Semester handoff lacks stateful per-case/cohort handoff generation and review routing.
- `status`, `memo`, `draft`, `research-start`, `client-comms-log`, and `ramp` are present but skeletal compared with upstream responsibilities.

### Observation

- China-law localization assets are directionally correct.
- `form-generation` and `plain-language-letters` are active in CN, while upstream treats them as deprecated redirects; not blocking, but should be reconciled during upgrade.

### Enhancement

- Future v2 could integrate real case-management, 12348/provider routing, OCR, and public-service platform connectors. Not required for v1.

## Lessons Learned

1. `legal-clinic` confirms that root parity and command discoverability are still mandatory for phase-2 modules when upstream treats them as root plugins.
2. For clinic/legal-aid modules, stateful operational safety is part of responsibility, not optional depth: deadlines, supervisor review, handoff and communication logs are core.

## Overall

ACTION REQUIRED

No files modified, staged, or committed.
