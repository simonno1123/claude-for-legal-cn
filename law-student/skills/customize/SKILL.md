---
name: customize
description: >
  局部更新中国法学习画像、学习偏好、法考日期、弱项权重、输出风格、
  材料路径和状态文件。完整重建仍由 cold-start-interview 负责。
argument-hint: "[field=value] [--redo-section <section>] [--check-integrations]"
---

# /law-student:customize

## Purpose

This is the Faithful Port compatibility entry for customization. It maps the upstream profile-update responsibility to China-law student profile updates.

Use it for local changes. Use `/law-student:cold-start-interview --redo` for a full profile rebuild.

## Allowed Updates

- Role or target: 法学院学生 / 法考考生 / 实习生 / 自学者.
- Target exam date or weekly hours.
- Learning style: drill-me / explain-to-me / hybrid.
- Weak subject weights.
- Materials directory.
- Preferred output format.
- Academic integrity notes.
- Integration status via `--check-integrations`.

## Not Allowed

- Converting the plugin into legal advice for real matters.
- Removing the anti-ghostwriting rules.
- Disabling real-matter redirect.
- Treating generated text as graded work.

## Workflow

1. Load `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md`.
2. If missing, route to cold-start.
3. Show the current relevant field.
4. Ask for confirmation before changing it.
5. Write the updated profile.
6. If the change affects schedule or weak subjects, update `study-plan.yaml` or ask the user to run `/law-student:study-plan --update`.

## State Update Format

When updating `study-plan.yaml`, record:

```yaml
customization_log:
  - date:
    field:
    old:
    new:
    reason:
```

## Output

```markdown
学习笔记 / 非法律意见

Updated:
Not changed:
Next suggested command:
```

## Persistence Failure

If profile or plan writes fail, output a patch-style summary for manual saving and explicitly say the persistent config was not updated.
