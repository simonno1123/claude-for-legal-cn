# TASK_010_CORPORATE_WRAPPER_REVIEW_RESULT

Artifact Type: RESULT
Producer: Codex
Task: TASK_010_CORPORATE_WRAPPER_REVIEW
Mode: READ ONLY, except for this permitted outbox RESULT artifact
Project: /Users/zhang/Documents/claude-for-legal-cn
Upstream: /Users/zhang/Documents/Playground/claude-for-legal-upstream/corporate-legal
Next Receiver: Gemini 3.5 Flash

This artifact reports facts only. It is not a REVIEW and not a DECISION.

## 1. Execution Status

Status: DONE

Workspace confirmed:

```text
/Users/zhang/Documents/claude-for-legal-cn
```

No plugin files were modified during TASK_010. The only file created by this task is this RESULT artifact under `.codex-coordination/outbox/`.

## 2. Active Corporate Root Skills

Command used:

```text
find corporate-legal/skills -maxdepth 2 -name SKILL.md | sort
wc -l corporate-legal/skills/*/SKILL.md
```

Active root skills found:

| Skill | Lines |
|---|---:|
| ai-tool-handoff | 24 |
| articles-of-association-audit | 142 |
| board-minutes | 149 |
| capital-contribution-audit | 205 |
| closing-checklist | 24 |
| cold-start-interview | 159 |
| customize | 55 |
| deal-team-summary | 24 |
| diligence-issue-extraction | 26 |
| entity-compliance | 183 |
| equity-transfer-pledge-review | 134 |
| governance-audit | 170 |
| integration-management | 25 |
| material-contract-schedule | 26 |
| matter-workspace | 195 |
| tabular-review | 24 |
| written-consent | 122 |

Total root skill lines: 1687

## 3. Phase-2 M&A Skills

Command used:

```text
find corporate-legal/phase-2/skills -maxdepth 2 -name SKILL.md | sort
wc -l corporate-legal/phase-2/skills/*/SKILL.md
```

Phase-2 M&A implementation skills found:

| Skill | Lines |
|---|---:|
| ai-tool-handoff | 104 |
| closing-checklist | 128 |
| deal-team-summary | 82 |
| diligence-issue-extraction | 125 |
| integration-management | 121 |
| material-contract-schedule | 86 |
| tabular-review | 87 |

Total phase-2 M&A implementation lines: 733

## 4. Upstream Root Skill Comparison

Upstream root skills:

```text
ai-tool-handoff
board-minutes
closing-checklist
cold-start-interview
customize
deal-team-summary
diligence-issue-extraction
entity-compliance
integration-management
material-contract-schedule
matter-workspace
tabular-review
written-consent
```

CN root `corporate-legal/skills/` contains all upstream root skills. No upstream root skill is missing after the wrapper fix.

CN root additionally contains China-law specific corporate skills:

```text
articles-of-association-audit
capital-contribution-audit
equity-transfer-pledge-review
governance-audit
```

## 5. Wrapper Review

The following M&A root wrapper skills exist:

```text
corporate-legal/skills/ai-tool-handoff/SKILL.md
corporate-legal/skills/closing-checklist/SKILL.md
corporate-legal/skills/deal-team-summary/SKILL.md
corporate-legal/skills/diligence-issue-extraction/SKILL.md
corporate-legal/skills/integration-management/SKILL.md
corporate-legal/skills/material-contract-schedule/SKILL.md
corporate-legal/skills/tabular-review/SKILL.md
```

Each wrapper:

- preserves the `/corporate-legal:<skill>` root command path;
- points to the corresponding China-law implementation under `corporate-legal/phase-2/skills/<skill>/SKILL.md`;
- states that `phase-2` is a historical storage location;
- states that the path does not mean lower priority or exclusion from v1 corporate-legal responsibilities.

Wrapper pattern is structurally consistent across the seven M&A skills.

## 6. Customize Skill Check

CN root customize exists:

```text
corporate-legal/skills/customize/SKILL.md
```

Observed mapping:

- Preserves `/corporate-legal:customize` command discoverability.
- Maps upstream profile customization to China-law corporate profile updates.
- Uses `~/.claude/plugins/config/claude-for-legal/corporate-legal/CLAUDE.md` as the single profile path.
- Directs missing or placeholder profile cases to `/corporate-legal:cold-start-interview`.
- Directs full profile refresh to `/corporate-legal:cold-start-interview --redo`.
- Prohibits Delaware, U.S. state-law, SEC, or common-law corporate defaults.

Potential consistency issue for reviewer:

```text
corporate-legal/skills/cold-start-interview/SKILL.md:159
- 不得另设 `customize` 配置入口；`company_profile` 必须由本技能统一生成和更新。
```

This line now conflicts in wording with the restored root `customize` compatibility entry. The likely intended rule is "do not create a second configuration source", but the current text can be read as prohibiting a `customize` entry altogether.

## 7. Dataroom Watcher Check

File checked:

```text
corporate-legal/agents/dataroom-watcher.md
```

Relevant finding:

```text
line 33: Run `/corporate-legal:closing-checklist` Mode 4 if it's briefing day.
```

The agent now references the root-discoverable `/corporate-legal:closing-checklist` command. No direct dependency on a hidden `phase-2` path was found.

## 8. CLAUDE.md Guardrails Check

File checked:

```text
corporate-legal/CLAUDE.md
```

Observed guardrails:

- China Mainland default legal scope is explicit.
- Foreign corporate-law defaults are prohibited unless user specifies another jurisdiction.
- 2024 China Company Law baseline is explicit.
- `[待查证]` and source verification requirements are present.
- Reviewer note block is present.
- Source provenance fields are present:
  - source;
  - reading scope;
  - jurisdiction;
  - items requiring verification;
  - consequential actions requiring human confirmation.
- U.S. attorney-work-product framing is prohibited.

Potential guardrail observation for reviewer:

- A standalone "no silent supplementation" rule was not found by exact wording.
- Similar control exists through source provenance, reading-scope, `[待查证]`, and human-confirmation requirements, but reviewer may decide whether explicit wording should be added later.

## 9. Documentation Wording Check

Files checked:

```text
corporate-legal/README.md
PROJECT_USAGE_GUIDE.md
```

Relevant facts:

- `corporate-legal/README.md` lists `/corporate-legal:customize` and all seven M&A wrapper commands in the root skill matrix.
- `corporate-legal/README.md` states that M&A / financing skills are Faithful Port v1 upstream responsibilities.
- `corporate-legal/README.md` states that `phase-2/skills/` is a historical implementation location, not devaluation.
- `PROJECT_USAGE_GUIDE.md` states the same for corporate M&A command exposure and `phase-2` non-devaluation.

No remaining corporate-specific "lower priority" or "downgrade" wording was found in the checked corporate wrapper context.

## 10. Localization Spot Check

Foreign-law references in the checked corporate files are generally negative constraints or comparative warnings, not default substantive law:

- `corporate-legal/README.md`: prohibits Delaware, Board Consent, Bylaws, Stockholder Consent, LLC defaults.
- `corporate-legal/CLAUDE.md`: prohibits Delaware, New York, LLC, bylaws, board consent, stockholder consent, SEC public company defaults.
- `corporate-legal/phase-2/skills/diligence-issue-extraction/SKILL.md`: prohibits Delaware, HSR, CFIUS, Section 280G, successor liability, attorney-client privilege, work product doctrine defaults.
- `corporate-legal/phase-2/skills/closing-checklist/SKILL.md`: prohibits HSR waiting period, CFIUS, Delaware good standing, privilege circle defaults.

Spot-checked phase-2 M&A implementations contain China Mainland transaction workflows, including corporate registration, equity and capital contribution, approvals, market-regulation changes, chops/certificates handover, personal information/data issues, and China-law closing gates.

## 11. JSON Validation

Command used:

```text
python3 -c 'import json, sys
for p in sys.argv[1:]:
    with open(p) as f: json.load(f)
    print(p + ": OK")' corporate-legal/.claude-plugin/plugin.json corporate-legal/.mcp.json corporate-legal/hooks/hooks.json
```

Output:

```text
corporate-legal/.claude-plugin/plugin.json: OK
corporate-legal/.mcp.json: OK
corporate-legal/hooks/hooks.json: OK
```

## 12. Marketplace Path Check

Command used:

```text
rg -n "corporate-legal" .claude-plugin/marketplace.json
```

Output:

```text
37:      "name": "corporate-legal",
39:      "source": "./corporate-legal",
```

Marketplace source path points to the corporate plugin directory.

## 13. Gaps and Observations for Reviewer

Confirmed facts:

1. The original root command discoverability issue for the seven M&A skills appears structurally restored through root wrapper skills.
2. The upstream `customize` root skill is now present in CN root skills.
3. `dataroom-watcher` now points to `/corporate-legal:closing-checklist`.
4. Corporate documentation no longer frames M&A / financing skills as lower-priority or outside v1 responsibilities.
5. JSON syntax validation passed for corporate plugin config files.

Remaining reviewer-facing issues:

1. `corporate-legal/skills/cold-start-interview/SKILL.md:159` still says not to create a `customize` configuration entry. This conflicts with the restored root `customize` command wording unless interpreted narrowly as "no second configuration source."
2. `corporate-legal/CLAUDE.md` has reviewer-note and source-provenance guardrails, but does not contain an exact standalone "no silent supplementation" instruction.
3. The wrapper approach restores discoverability without moving phase-2 implementation files. This is consistent with the approved fix approach, but final closure depends on reviewer acceptance of wrapper delegation rather than physical movement.

## 14. Current Git Status Snapshot

Command used:

```text
git status --short
```

Snapshot before writing this RESULT artifact showed existing uncommitted work from prior tasks:

```text
 M PROJECT_USAGE_GUIDE.md
 M ai-governance-legal/CLAUDE.md
 M ai-governance-legal/README.md
 M ai-governance-legal/skills/ai-inventory/SKILL.md
 M ai-governance-legal/skills/aia-generation/SKILL.md
 M ai-governance-legal/skills/cold-start-interview/SKILL.md
 M ai-governance-legal/skills/customize/SKILL.md
 M ai-governance-legal/skills/matter-workspace/SKILL.md
 M ai-governance-legal/skills/policy-monitor/SKILL.md
 M ai-governance-legal/skills/use-case-triage/SKILL.md
 M ai-governance-legal/skills/vendor-ai-review/SKILL.md
 M corporate-legal/README.md
 M corporate-legal/agents/dataroom-watcher.md
 M regulatory-legal/CLAUDE.md
 M regulatory-legal/README.md
 M regulatory-legal/agents/reg-change-monitor.md
 M regulatory-legal/skills/cold-start-interview/SKILL.md
 M regulatory-legal/skills/comments/SKILL.md
 M regulatory-legal/skills/customize/SKILL.md
 M regulatory-legal/skills/gap-surfacer/SKILL.md
 M regulatory-legal/skills/gap-surfacer/references/comment-tracker.yaml
 M regulatory-legal/skills/gap-surfacer/references/gap-tracker.yaml
 M regulatory-legal/skills/gaps/SKILL.md
 M regulatory-legal/skills/matter-workspace/SKILL.md
 M regulatory-legal/skills/policy-diff/SKILL.md
 M regulatory-legal/skills/policy-redraft/SKILL.md
 M regulatory-legal/skills/reg-feed-watcher/SKILL.md
?? .codex-coordination/
?? ai-governance-legal/skills/ai-inventory/references/
?? corporate-legal/skills/ai-tool-handoff/
?? corporate-legal/skills/closing-checklist/
?? corporate-legal/skills/customize/
?? corporate-legal/skills/deal-team-summary/
?? corporate-legal/skills/diligence-issue-extraction/
?? corporate-legal/skills/integration-management/
?? corporate-legal/skills/material-contract-schedule/
?? corporate-legal/skills/tabular-review/
```

The status includes work from earlier regulatory, ai-governance, corporate wrapper, and coordination tasks. TASK_010 did not stage or commit anything.

## 15. Result Summary

Corporate wrapper review facts are now available for Gemini 3.5 Flash.

Factual closure posture:

- Root corporate M&A command parity: restored by wrappers.
- `customize` root discoverability: restored.
- Dataroom watcher dependency: points to root command.
- Documentation devaluation wording: not found in checked corporate context.
- Remaining issues for reviewer: wording conflict in `cold-start-interview` around `customize`; possible explicit guardrail hardening for "no silent supplementation"; acceptance of wrapper delegation rather than file movement.
