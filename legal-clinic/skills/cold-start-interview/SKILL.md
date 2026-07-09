---
name: cold-start-interview
description: >
  由指导教师、执业律师、法援律师或授权负责人初始化中国法律诊所/法律援助
  项目画像，建立服务范围、学生名单、复核规则、期限台账、沟通记录和交接路径。
argument-hint: "[--redo] [--check-integrations]"
---

# /legal-clinic:cold-start-interview

## Authority Gate

This setup must be run by a supervising teacher/lawyer or authorized clinic coordinator. If a student runs it, route them to `/legal-clinic:ramp` unless the supervising reviewer has delegated setup authority.

## State Paths

Create or update:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/legal-clinic/deadlines-ledger.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/review-queue.yaml
~/.claude/plugins/config/claude-for-legal/legal-clinic/client-comms/
~/.claude/plugins/config/claude-for-legal/legal-clinic/handoffs/
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/
~/.claude/plugins/config/claude-for-legal/legal-clinic/cases/
```

If writes fail, output the files as YAML/Markdown and explicitly say setup was not persisted.

## Interview

Ask in small batches and wait for answers:

1. Institution type: 高校法律诊所 / 法律援助中心 / 公益组织 / 公共法律服务咨询点.
2. Supervisors: names, roles, license/authorization basis, review availability.
3. Students/volunteers: roster, semester dates, responsible matters.
4. Service region and accepted matter types.
5. Whether real-party materials may be processed, and required consent/confidentiality rules.
6. Legal-aid screening rules: economic difficulty, case scope, local legal aid center requirements.
7. Review model:
   - all outputs require review,
   - external-facing outputs require review,
   - configurable high-risk flags.
8. Deadline warning cadence: default `[30, 14, 7, 3, 1]`.
9. Referral resources: 12348, local legal aid center, labor arbitration, court service center, regulator/agency, mediation organizations.
10. Seed documents: clinic handbook, intake forms, local forms, court/arbitration templates, prior anonymized examples.

## Initialize `deadlines-ledger.yaml`

```yaml
default_deadline_policy:
  jurisdiction: China Mainland
  warning_days: [30, 14, 7, 3, 1]
  manual_review_required: true
  no_ai_final_calculation: true
deadlines: []
```

## Initialize `review-queue.yaml`

```yaml
review_queue:
  states:
    - pending_review
    - approved
    - returned_with_comments
  required_review:
    - client_letter
    - filing
    - arbitration_application
    - legal_aid_application
    - settlement
    - withdrawal
    - deadline_expiring
    - case_closure
  queue: []
  log: []
```

## Close

Confirm:

- where the profile and ledgers were saved,
- which placeholders remain,
- who can approve outputs,
- suggested next command: `/legal-clinic:ramp` for students or `/legal-clinic:build-guide [案由]` for supervisors.
