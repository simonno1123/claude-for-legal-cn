---
name: customize
description: >
  Update the single China AI governance profile created by cold-start-interview. Does not create a second profile; syncs changes to inventory, registry, playbook, sweep, and matter state when needed.
argument-hint: "[configuration update request]"
---

# /customize

## Compatibility Notice

This command is not a standalone second profile. It updates the same persistent
profile and state files used by `/ai-governance-legal:cold-start-interview`.

Profile path:

`~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`

## Updateable Areas

- AI system inventory defaults.
- Launch gates and China AI red lines.
- Use-case registry categories: approved, conditional, rejected/watch.
- Algorithm recommendation filing status.
- Generative AI service filing/security assessment status.
- ICP filing, App filing, ICP License, MLPS status.
- Important data or data export settings.
- Vendor API, training, retention, deletion, audit, liability, and redline positions.
- Content safety and deep synthesis marking controls.
- Owners, approval paths, and non-lawyer gates.
- Outputs folder and policy sweep settings.
- Matter workspace settings.

## Workflow

1. Read current profile and relevant state files.
2. Identify requested changes and affected records.
3. Preview a change table.
4. Ask for confirmation before writing.
5. Write profile updates.
6. If the update affects existing systems/use cases/vendors/matters, mark them for re-review rather than silently changing their final status.

Affected state examples:

- New launch gate -> update `use-case-registry.yaml` entries to `review_needed`.
- Vendor redline change -> flag vendor review outputs for re-check.
- MLPS/ICP status update -> update linked systems in `ai-systems.yaml`.
- Policy sweep config change -> do not rewrite `Last policy sweep`; run `policy-monitor sweep`.

## Output Format

```markdown
# AI Governance Profile Update

> **复核提示**
> - **来源：** current profile / user instruction / state files
> - **读取范围：** [profile and affected state files]
> - **待判断事项：** [records requiring re-review]
> - **时效性：** [filing/status changes needing verification]
> - **行动前：** confirm before writing profile or state changes

| Field | Old value | New value | Affected files | Follow-up |
|---|---|---|---|---|
```
