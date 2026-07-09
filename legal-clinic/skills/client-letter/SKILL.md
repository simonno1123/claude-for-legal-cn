---
name: client-letter
description: >
  起草面向当事人的中文说明信、材料清单、进展告知和风险提示。必须白话、
  不承诺结果，发送前必须进入 supervisor-review-queue。
argument-hint: "[信件目的]"
---

# /legal-clinic:client-letter

## Required Context

Read case status, client-comms log, deadline ledger, review queue and clinic profile.

## Allowed Letter Types

- 预约/接待确认.
- 材料补充清单.
- 进展告知.
- 分流建议.
- 风险提醒.
- 复核后可发送的下一步说明.

## Drafting Rules

- Use plain Chinese.
- No promise of outcome.
- No unapproved legal advice.
- State what the client should do, by when, and what to bring.
- Mark unverified facts or deadlines.
- Do not include internal strategy or review comments.

## Review Gate

Every client-facing letter is submitted to `review-queue.yaml` as `pending_review`. It may not be sent until `approved`.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

# Client Letter Draft

## Purpose
## Draft Text
## Materials Requested
## Deadlines Mentioned
## Review Queue Entry
```

If a deadline is mentioned, confirm it exists in `deadlines-ledger.yaml` or add a `VERIFY` handoff.
