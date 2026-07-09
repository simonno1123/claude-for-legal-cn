---
name: status
description: >
  生成法律诊所案件状态摘要，面向内部团队、导师/律师或当事人。读取期限台账、
  沟通记录和复核队列，区分 internal / supervisor / client 三种受众。
argument-hint: "[case_id] [internal | supervisor | client]"
---

# /legal-clinic:status

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/cases/[case_id]/
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/[case_id]/log.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
```

## Audience Modes

- `internal`: full facts, work done, open issues, deadlines, evidence gaps, owner.
- `supervisor`: decisions needed, risk flags, review queue items, deadline concerns.
- `client`: plain-language progress only; no strategy, no unapproved advice, no internal risk analysis.

Client-facing status cannot be final without `review-queue.yaml` status `approved`.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

# Case Status

## Current Posture
## Completed Work
## Pending Deadlines
## Communications Since Last Update
## Evidence / Materials Needed
## Review Queue Items
## Referral / Escalation Need
## Next Actions
```

## State Writes

If the status surfaces a new deadline, hand it off to `/legal-clinic:deadlines add`.

If the status is client-facing, submit it to `/legal-clinic:supervisor-review-queue submit` before final use.
