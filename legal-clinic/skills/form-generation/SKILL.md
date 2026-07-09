---
name: form-generation
description: >
  生成中国法律诊所内部表单，如接待表、材料清单、授权确认、送达地址确认、
  复核表和期限登记表。不得替代官方最新格式。
argument-hint: "[表单类型]"
---

# /legal-clinic:form-generation

## Required Context

Read clinic guides, official/local template notes, review queue and deadline ledger.

## Forms

- intake form,
- material checklist,
- legal-aid application checklist,
- authorization confirmation,
- service address confirmation,
- evidence list,
- deadline registration form,
- supervisor review form.

## Rules

- If an official court/arbitration/agency form exists, tell the user to verify and use the official form.
- Any external submission form enters `review-queue.yaml` as `pending_review`.
- Any date or filing window in a form must be logged or checked in `deadlines-ledger.yaml`.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

# Form Draft

## Purpose
## Fields
## Instructions
## Required Attachments
## Deadline / Review Triggers
```
