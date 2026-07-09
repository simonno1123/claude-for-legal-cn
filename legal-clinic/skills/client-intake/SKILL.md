---
name: client-intake
description: >
  中国法律诊所当事人接待与初筛。执行案由路由、冲突检查、法援资格初核、
  风险分流、期限识别和导师/律师复核交接。
argument-hint: "[案情摘要] [--new | --update]"
---

# /legal-clinic:client-intake

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/
```

If setup is missing, stop and route to `/legal-clinic:cold-start-interview`.

## Intake Workflow

1. Explain that intake gathers facts and does not provide final legal advice.
2. Confirm consent, confidentiality, contact method and whether emergency help is needed.
3. Route by issue:
   - 劳动争议,
   - 消费者权益,
   - 婚姻家庭/人身安全,
   - 房屋租赁/物业,
   - 小额债务,
   - 校园权益,
   - 行政投诉/复议/诉讼,
   - legal-aid application or referral.
4. Collect:
   - parties and related parties,
   - opposing party,
   - timeline,
   - claims/requests,
   - documents/evidence,
   - existing complaints/arbitration/lawsuits,
   - deadlines in documents,
   - urgent risks.
5. Conflict check:
   - same/opposing party,
   - related party,
   - positional conflict,
   - student/family conflict.
   Do not resolve conflicts. Flag for supervisor.
6. Legal-aid criteria screen:
   - economic difficulty indication,
   - matter type under PRC Legal Aid Law or local aid rules,
   - applicant identity/materials,
   - urgent rights protection need.
7. Triage:
   - urgent,
   - time_sensitive,
   - standard,
   - out_of_scope_referral.
8. Mandatory deadline handoff: every surfaced date becomes a proposed `/legal-clinic:deadlines add` entry.
9. Queue any high-risk or external-facing next step to supervisor review.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

> **Reviewer note**
> - Sources:
> - Flags:
> - Before relying: confirm facts, conflict check and deadline calculation

# 接待初筛

## 当事人陈述
## 案由与受理/分流方向
## 关键事实时间线
## 证据和材料缺口
## 法律援助资格初核
## 冲突检查
## 风险分级
## 期限交接
## 需复核事项
## 下一步
```

## Deadline Handoff

For each deadline:

```text
/legal-clinic:deadlines add
  case_id=
  matter_type=
  deadline_type=
  description=
  due_date=VERIFY
  source=
  owner_student=
  supervisor=
```

Never compute a final due date without source verification and supervisor confirmation.

## State Writes

- Save intake summary under `cases/[case_id]/intake.md` where available.
- Append communication fact to `client-comms/[case_id]/log.md` when intake includes a contact record.
- Add urgent or external-facing outputs to `review-queue.yaml` with `pending_review`.
