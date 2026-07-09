---
name: client-comms-log
description: >
  追加式记录中国法律诊所与当事人的沟通纪要、材料补充、承诺事项、期限线索
  和下一步。沟通记录不替代法律分析。
argument-hint: "[case_id] [沟通内容]"
---

# /legal-clinic:client-comms-log

## Required Context

Append to:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/[case_id]/log.md
```

Read `deadlines-ledger.yaml` and `review-queue.yaml` for deadline and review implications.

## Log Entry

```markdown
## [YYYY-MM-DD HH:MM] - [phone/wechat/sms/email/in-person]

Participants:
Client statement:
Materials provided:
Clinic response:
Promises made:
Deadline clues:
Next action:
Review needed:
```

## Rules

- Record facts, not unreviewed strategy.
- Do not promise results.
- Do not create client-facing advice without review.
- If a deadline clue appears, hand off to `/legal-clinic:deadlines add`.
- If the clinic promised a response, create a review queue item or next-action note.

## Persistence Failure

If the log cannot be written, output the Markdown entry and state that it must be manually saved.
