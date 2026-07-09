---
name: semester-handoff
description: >
  生成中国法律诊所学期/人员交接备忘录。读取活动案件、期限台账、沟通记录和
  复核队列，输出每案交接和班级总览，并进入导师/律师复核。
argument-hint: "[semester] [--case <case_id> | --cohort]"
---

# /legal-clinic:semester-handoff

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/
~/.claude/plugins/config/claude-for-legal/legal-clinic/cases/
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
```

Write:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/[semester]/[case_id].md
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/[semester]/_summary.md
```

## Workflow

1. Require an active-case list. If none exists, ask; do not invent cases.
2. Map outgoing student to incoming student. If unknown, mark `TBD - supervisor to assign`.
3. For each active case, gather:
   - posture,
   - open deadlines,
   - completed work,
   - open evidence/materials,
   - recent communications,
   - review queue status,
   - client relationship notes,
   - first-week priorities.
4. Generate per-case handoff memo.
5. Generate cohort summary.
6. Submit handoff package to `review-queue.yaml` as `pending_review`.

## Per-Case Memo

```markdown
# Case Handoff

Case ID:
Matter type:
Outgoing student:
Incoming student:
Supervisor:

## Current Posture
## Pending Deadlines
## Work Completed
## Open Issues
## Documents / Evidence Location
## Client Communications Summary
## Review Queue Items
## Supervisor Flags
## First-Week Priorities
```

## Cohort Summary

```markdown
# Cohort Handoff Summary

Active cases:
Cases with deadlines in 30 days:
Unassigned incoming owners:
Cases requiring supervisor decision:
Training topics for next cohort:
```

## Blocking Rule

Handoff memos may not be released as final to incoming students until reviewed. Case closure must always be separately approved.
