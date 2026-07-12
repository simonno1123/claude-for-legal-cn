# TASK_009_AI_GOVERNANCE_RECOVERY_EDIT — Codex Result

## Status

DONE

## Scope

Modified only `ai-governance-legal/` for repository content. Created this result
artifact under `.codex-coordination/outbox/` as required by the task.

## Modified Files

- `ai-governance-legal/CLAUDE.md`
- `ai-governance-legal/README.md`
- `ai-governance-legal/skills/cold-start-interview/SKILL.md`
- `ai-governance-legal/skills/ai-inventory/SKILL.md`
- `ai-governance-legal/skills/ai-inventory/references/ai-systems-schema.yaml`
- `ai-governance-legal/skills/use-case-triage/SKILL.md`
- `ai-governance-legal/skills/aia-generation/SKILL.md`
- `ai-governance-legal/skills/vendor-ai-review/SKILL.md`
- `ai-governance-legal/skills/policy-monitor/SKILL.md`
- `ai-governance-legal/skills/matter-workspace/SKILL.md`
- `ai-governance-legal/skills/customize/SKILL.md`

## Summary

Restored stateful AI governance workflow responsibilities while preserving China
Mainland legal substance and the existing `security-assessment` China compliance
content.

Restored lifecycle responsibilities:

1. `CLAUDE.md` operational guardrails: reviewer note, source provenance, no silent supplementation, consequential action gates, and state file map.
2. `cold-start-interview`: persistent profile path, `--redo`, `--check-integrations`, seed document learning, and state file initialization.
3. `ai-inventory`: persistent `ai-systems.yaml`, `list/add/edit/classify/show`, status, classification, and next review lifecycle.
4. `aia-generation`: stateful impact assessment workflow, seed/house-style handling, policy consistency diff, inventory update, and delegation to `security-assessment`.
5. `policy-monitor`: sweep/direct/acknowledge modes, outputs scan, registry/inventory/playbook comparison, `Last policy sweep`, and `gaps_found`.
6. `use-case-triage`: `use-case-registry.yaml`, approved/conditional/rejected/watch mapping, registry sync, and non-lawyer approval/rejection gate.
7. `vendor-ai-review`: playbook comparison, provisional mode, AI addendum gap, redline proposals, and policy consistency diff.
8. `matter-workspace`: `new/list/switch/close/none`, matter storage, active matter, and isolation rules.
9. `customize`: single-profile update path and re-review propagation to state files.

## 18-Point Checklist

1. Modify only allowed plugin content: PASS.
2. Preserve China AI law substance: PASS.
3. Do not modify other plugins in this task: PASS.
4. Do not add external API/MCP implementations: PASS.
5. Restore reviewer note guardrail: PASS.
6. Restore source provenance guardrail: PASS.
7. Restore no silent supplementation guardrail: PASS.
8. Restore consequential action gates: PASS.
9. Restore persistent profile path: PASS.
10. Restore `--redo`: PASS.
11. Restore `--check-integrations`: PASS.
12. Restore seed document learning: PASS.
13. Restore `ai-systems.yaml` lifecycle: PASS.
14. Restore impact assessment statefulness: PASS.
15. Restore policy monitor sweep and acknowledgment state: PASS.
16. Restore use-case registry sync and non-lawyer gates: PASS.
17. Restore vendor playbook/provisional/redline behavior: PASS.
18. Restore matter workspace lifecycle and customize alignment: PASS.

## Validation

Commands run:

```text
python3 -c "import json; json.load(open('ai-governance-legal/.claude-plugin/plugin.json')); json.load(open('ai-governance-legal/.mcp.json')); print('JSON_OK')"
find ai-governance-legal/skills -mindepth 2 -maxdepth 2 -name SKILL.md | sed 's#^ai-governance-legal/skills/##' | sort
rg -n "ai-systems\\.yaml|use-case-registry\\.yaml|vendor-ai-playbook\\.yaml|policy-sweep-log\\.yaml|--redo|--check-integrations|Last policy sweep|gaps_found|policy consistency|seed|house style|provisional|redline|new \\| list \\| switch \\| close \\| none|reviewer note|复核提示|No Silent|Source Provenance|待核验|non-lawyer|approval|rejection|acknowledge" ai-governance-legal/CLAUDE.md ai-governance-legal/README.md ai-governance-legal/skills
rg -n "EU AI Act|NIST|FTC|GDPR|FRIA|US state|Colorado|provider/deployer|high-risk AI|attorney work product|privilege|PRIVILEGED|Federal Register|CourtListener|Westlaw|state law|U\\.S\\.|US\\b|United States" ai-governance-legal
git diff --check -- ai-governance-legal
git diff --stat -- ai-governance-legal
```

Validation results:

- JSON validation: `JSON_OK`
- Command discoverability: all 11 root skills present.
- Foreign-law terms: only negative constraints or comparative exclusions found.
- `git diff --check -- ai-governance-legal`: no output.

## Diff Stat

```text
 ai-governance-legal/CLAUDE.md                      | 133 +++++++++++++---
 ai-governance-legal/README.md                      |  17 ++
 ai-governance-legal/skills/ai-inventory/SKILL.md   | 124 ++++++++++++---
 ai-governance-legal/skills/aia-generation/SKILL.md | 126 ++++++++++++++-
 .../skills/cold-start-interview/SKILL.md           | 146 +++++++++++------
 ai-governance-legal/skills/customize/SKILL.md      |  64 +++++---
 .../skills/matter-workspace/SKILL.md               |  67 ++++++--
 ai-governance-legal/skills/policy-monitor/SKILL.md |  91 +++++++++--
 .../skills/use-case-triage/SKILL.md                | 108 ++++++++-----
 .../skills/vendor-ai-review/SKILL.md               |  83 ++++++----
 10 files changed, 748 insertions(+), 211 deletions(-)
```

Note: the new untracked schema file is not included in `git diff --stat` until staged:

`ai-governance-legal/skills/ai-inventory/references/ai-systems-schema.yaml`

## Risks / Unresolved Issues

- `security-assessment/SKILL.md` was not modified because it was not in the allowed file list. `aia-generation` now delegates to it and adds the missing lifecycle behavior.
- `reg-gap-analysis` and `policy-starter` were not modified because they were not in the allowed file list.
- Existing unrelated corporate/regulatory changes remain in the worktree from prior tasks.

## Next Receiver

Gemini 3.5 Flash Review
