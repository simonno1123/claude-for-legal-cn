---
name: plain-language-letters
description: >
  将法律诊所内部说明、材料清单或进展告知改写为当事人可理解的白话中文版本。
  仍需导师/律师复核后才能发送。
argument-hint: "[原文或目标受众]"
---

# /legal-clinic:plain-language-letters

## Required Context

Read case status, client communication preferences, deadlines ledger and review queue.

## Rewrite Rules

- Short sentences.
- Avoid legal jargon or explain it.
- Put action items first.
- Include what to bring, where to go, and by when.
- Do not promise outcomes.
- Do not include internal risk analysis or strategy.
- Keep `[待核验]` items visible to supervisor; remove from client version only after approval.

## Review Gate

All plain-language client-facing text must enter `review-queue.yaml` as `pending_review` and cannot be sent until `approved`.

## Deadline Behavior

If the plain-language letter mentions a deadline, confirm it appears in `deadlines-ledger.yaml` or create a `VERIFY` handoff.
