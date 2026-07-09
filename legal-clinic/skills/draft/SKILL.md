---
name: draft
description: >
  生成中国法律诊所常用文书学习稿，如投诉材料、仲裁申请书、起诉状提纲、
  证据目录、调解方案、法律援助申请材料清单等。所有对外文本必须复核。
argument-hint: "[文书类型和事实]"
---

# /legal-clinic:draft

## Required Context

Read case file, intake, memo, guide, `deadlines-ledger.yaml`, official/local templates and `review-queue.yaml`.

## Draftable China-Law Artifacts

- 劳动仲裁申请书学习稿.
- 民事起诉状提纲.
- 消费者投诉材料.
- 行政复议/行政投诉材料清单.
- 证据目录.
- 调解方案.
- 法律援助申请材料清单.
- 送达地址确认、授权确认、事实说明.

## Gates Before Drafting

Ask:

1. Will this be sent to a client, court, arbitration commission, legal aid center or regulator?
2. Has the supervising reviewer approved the direction?
3. Are names and identifying facts safe to process?
4. Are deadlines in `deadlines-ledger.yaml` current?
5. Is there an official local form that must be used?

## Output Label

Every draft starts:

```text
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核
```

## Review Queue

All drafts intended for external use must be submitted to `/legal-clinic:supervisor-review-queue submit` with `pending_review`. They cannot be final until `approved`.

## Deadline Behavior

If a draft references a filing, appeal, hearing, evidence or correction deadline, hand it off to `/legal-clinic:deadlines add` or update the ledger.
