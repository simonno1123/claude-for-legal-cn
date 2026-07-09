---
name: supervisor-review-queue
description: >
  管理中国法律诊所导师/律师复核队列。读写 review-queue.yaml，支持查看、
  approve、return，严格使用 pending_review / approved / returned_with_comments 状态。
argument-hint: "[list | submit | approve <id> | return <id>]"
---

# /legal-clinic:supervisor-review-queue

## Required Context

Read and write:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
```

If no formal review queue is configured, still enforce that external-facing and rights-dispositive outputs require a recorded supervisor decision.

## States

- `pending_review`
- `approved`
- `returned_with_comments`

No other final states are permitted for v1.

## Must Queue

- client letters,
- filings, complaints, arbitration applications, legal-aid applications,
- settlement, withdrawal, admission, waiver, payment commitment,
- deadline-expiring actions,
- vulnerable-party matters,
- case closure,
- semester handoff release.

## Actions

### `list`

Show queue by urgency:

- due within 3 days,
- due within 7 days,
- external submission,
- vulnerable party,
- normal.

### `submit`

Create a `pending_review` item with:

```yaml
- id:
  case_id:
  item_type:
  student:
  supervisor:
  submitted_at:
  status: pending_review
  urgency:
  flags: []
  content_path:
  deadline_id:
  decision_log: []
```

### `approve`

Only the supervisor or authorized reviewer may approve. Append decision log and set `status: approved`.

### `return`

Set `status: returned_with_comments`; require comments and next revision owner.

## Blocking Rule

If an output is client-facing, court/agency-facing, or rights-dispositive and no `approved` record exists, say:

> This cannot be finalized or sent yet. It is pending supervisor/lawyer review in `review-queue.yaml`.

## Teaching Signal

When returning items, capture the teaching reason: missing facts, unsupported legal basis, deadline uncertainty, tone, evidence gap, procedural issue or unauthorized-practice risk.
