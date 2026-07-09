---
name: deadlines
description: >
  读写中国法律诊所期限台账 deadlines-ledger.yaml，支持 add/report/update/complete/close，
  跟踪劳动仲裁时效、诉讼时效、举证期限、复议/起诉/上诉/补正/投诉期限等。
argument-hint: "add | report | update | complete | close"
---

# /legal-clinic:deadlines

## Required Context

Read and write:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
```

If missing, initialize from `legal-clinic/deadlines-ledger.yaml` template or ask to run cold-start.

## Non-Negotiable Rule

The skill tracks and sanity-checks deadlines. It does not finally calculate legal time limits. The student computes from source documents and governing rules; the supervisor confirms.

## Actions

### `add`

Required fields:

- `case_id`
- `case_name`
- `matter_type`
- `deadline_type`
- `description`
- `due_date` or `VERIFY`
- `source`
- `owner_student`
- `supervisor`

Before writing:

1. Check for duplicate `case_id + deadline_type + due_date`.
2. If `due_date` is concrete, compare against `references/plausibility-bands/CN.md` as a rough sanity check.
3. If outside typical range, stop and require recalculation or supervisor confirmation.
4. Set `review_required: true`.
5. If due within warning cadence, add a warning entry and queue supervisor review.

### `report`

Produce:

- overdue,
- due today/3 days,
- due 7 days,
- due 14/30 days,
- by student,
- by matter type,
- unverified `VERIFY` deadlines,
- unassigned items.

### `update`

Modify fields and append a dated note. Do not overwrite source history silently.

### `complete`

Confirm the actual filing/submission/action happened. Set `status: completed` and `completed_date`.

### `close`

Allowed only when no longer applicable. Require reason and supervisor approval if it affects rights.

## Ledger Entry

```yaml
- id:
  case_id:
  case_name:
  matter_type:
  deadline_type:
  description:
  due_date:
  source:
  source_verified: false
  owner_student:
  supervisor:
  status: upcoming
  warnings: []
  review_required: true
  notes:
```

## Integration

- `client-intake`, `draft`, `memo` and `status` must hand off surfaced deadlines here.
- `semester-handoff` reads this ledger.
- `supervisor-review-queue` prioritizes close deadlines.
