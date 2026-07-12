# Codex Task

## 1. Task ID

TASK_009_AI_GOVERNANCE_RECOVERY_EDIT

## 2. Status

READY

## 3. Background

The previous audit `TASK_008_AUDIT_AI_GOVERNANCE` concluded with a `REJECTED` state. While the Chinese regulatory references and `security-assessment` skill in the `ai-governance-legal` module are of high quality, multiple stateful workflows (triage, inventory lifecycle, sweeping, impact assessment) were lost, converting the module into static markdown templates.

This task is an EDIT task to restore the 8 missing responsibilities and align the module's CLAUDE.md with standard ACOS operational guardrails, while strictly preserving all existing China-law localization content.

## 4. Goal

Perform substantive restoration of all stateful AI governance workflows inside the existing root skill files under `ai-governance-legal/`.

## 5. Allowed Scope

Allowed to modify:
- `ai-governance-legal/CLAUDE.md`
- `ai-governance-legal/README.md`
- `ai-governance-legal/skills/cold-start-interview/SKILL.md`
- `ai-governance-legal/skills/ai-inventory/SKILL.md`
- `ai-governance-legal/skills/use-case-triage/SKILL.md`
- `ai-governance-legal/skills/aia-generation/SKILL.md`
- `ai-governance-legal/skills/vendor-ai-review/SKILL.md`
- `ai-governance-legal/skills/policy-monitor/SKILL.md`
- `ai-governance-legal/skills/matter-workspace/SKILL.md`
- `ai-governance-legal/skills/customize/SKILL.md`

Allowed to create supporting schema/examples under:
- `ai-governance-legal/skills/ai-inventory/references/` (e.g., example YAML)

## 6. Forbidden Actions

1. Do not modify files in other plugins (e.g., `employment-legal/`, `regulatory-legal/`).
2. Do not delete or degrade the existing China AI law substance (e.g., TC260-PG-20241A, Generative AI filings, Algorithm Recommendation filing details in `security-assessment/SKILL.md`).
3. Do not implement physical external database APIs. Keep local file-based trackers (`ai-systems.yaml`, `use-case-registry.yaml`, etc.) as state representations.
4. Do not perform `git commit` or `git add` unless explicitly authorized later.

## 7. Requirements

### 1. CLAUDE.md Guardrails Restoration (P0-附属)
- Restore core operational guardrails to `ai-governance-legal/CLAUDE.md`:
  - **Reviewer Note**: Require a reviewer note with `[待核验]` tags for unverified items.
  - **Source Provenance**: Explicit tracking of data sources.
  - **No Silent Supplementation**: Prohibit silent assumptions or overrides.
  - **Consequential Action Gates**: Require human validation before external submission or compliance filing.

### 2. Restore cold-start-interview (P0)
- Add persistent configuration write path to `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md` (or local instance path).
- Support `--redo` and `--check-integrations` parameters.
- Define policy library indexing and connector verification workflow (adapted to China MCP placeholders).

### 3. Restore ai-inventory (P0)
- Define persistent inventory storage in local file `ai-systems.yaml`.
- Support operations: `list | add | edit | classify | show`.
- Instruct on tracking system status, classification, and next review lifecycle.

### 4. Restore aia-generation / security-assessment (P0)
- Keep `aia-generation` as an alias to `security-assessment`, but ensure both represent a stateful assessment workflow.
- Restore impact assessment workflow: intake seed assessment, perform regulatory classification, do policy-consistency diff, and tag risk items.

### 5. Restore policy-monitor (P0)
- Restore swept output items scanning (simulate reading output directories).
- Compare swept items against enterprise policies and triage registry.
- Maintain `Last policy sweep` and count of `gaps_found`.

### 6. Restore use-case-triage (P1)
- Support reading and writing to local `use-case-registry.yaml`.
- Guide Codex on approved/conditional/rejected registry classification, and enforce a non-lawyer approval/rejection gate.

### 7. Restore vendor-ai-review (P1)
- Support comparative analysis of vendor terms against configured playbooks.
- Handle provisional approvals, AI addendum gaps, and propose redlines.

### 8. Restore matter-workspace (P1)
- Restore workspace lifecycle commands (`new | list | switch | close | none`) and matter isolation behavior.

### 9. Customize Skill Alignment (P1)
- Align `customize` with `cold-start-interview` update mechanisms.

## 8. Acceptance Criteria

1. All modified files are strictly within `ai-governance-legal/`.
2. Existing China AI law content and security assessment requirements are fully preserved.
3. Every skill file contains stateful behavioral instructions (yaml reading/writing, lifecycle status, or parameters) rather than just static text/table templates.
4. Validation command `python3 -c "import json; json.load(open('ai-governance-legal/.claude-plugin/plugin.json'))"` passes.

## 9. BLOCKED Rules

If any conflict occurs between ACOS guardrails and China AI regulatory defaults, or if any folder structure does not exist, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. Modified files and line changes
3. 18-point checklist verification status
4. Test or validation commands run
5. Risks or unresolved issues

## 11. Next Handoff Target

Gemini 3.5 Flash Review (replacing Claude)

## 12. Reason

To enable Gemini 3.5 Flash to review the recovery results and confirm valid status.
