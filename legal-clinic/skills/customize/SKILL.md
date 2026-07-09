---
name: customize
description: >
  局部更新中国法律诊所项目画像、案由范围、复核人、期限提醒、学生名单、
  分流资源和模板偏好。完整重建仍由 cold-start-interview 负责。
argument-hint: "[field=value] [--redo-section <section>]"
---

# /legal-clinic:customize

## Required Context

Read and write:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
```

## Allowed Updates

- Service areas and matter types.
- Supervisors/reviewers.
- Student roster and case owners.
- Review triggers.
- Deadline warning days.
- Referral resources.
- Template and guide paths.
- MCP/integration status.

## Not Allowed

- Removing supervisor approval for external-facing or rights-dispositive actions.
- Disabling deadline verification.
- Treating AI output as final legal advice.
- Removing real-party confidentiality rules.

## Workflow

1. Show current value.
2. Ask for confirmation.
3. Write updated profile.
4. If deadline warnings change, update `deadlines-ledger.yaml`.
5. If review triggers change, update `review-queue.yaml`.
6. Record a customization log entry.

If writes fail, output a manual patch and state persistence failed.
