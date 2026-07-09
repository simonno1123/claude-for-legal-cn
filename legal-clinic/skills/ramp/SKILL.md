---
name: ramp
description: >
  为新加入中国法律诊所、法律援助或公服咨询项目的学生/志愿者生成入门培训、
  模拟练习、保密脱敏规则、期限意识和复核流程。
argument-hint: "[--card | --practice]"
---

# /legal-clinic:ramp

## Required Context

Read clinic profile, guides, review queue rules, deadline policy and handoffs:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
```

## Training Modules

1. Service scope and referral boundaries.
2. Confidentiality, desensitization and file access.
3. Unauthorized-practice prevention: students assist; supervisors approve.
4. Client intake practice.
5. Legal-aid criteria screen under China-law context.
6. Deadline ledger practice.
7. Review queue workflow.
8. Client communication tone.
9. Semester handoff expectations.

## Practice Mode

Use simulated facts only. After each exercise, ask the student to identify matter type, deadline clues, referral need, review trigger and materials needed.

## State Behavior

If a student is assigned active cases, surface their handoff memos and deadlines. Do not expose unrelated case materials.

## Output

For `--card`, produce a one-page student reference card with commands, review gates and escalation triggers.
