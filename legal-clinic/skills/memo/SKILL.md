---
name: memo
description: >
  生成中国法律诊所案件备忘录学习稿。保留学生分析区、事实核验项、期限风险、
  法援/分流判断和导师复核问题。
argument-hint: "[案情或接待记录] [--internal | --supervisor]"
---

# /legal-clinic:memo

## Required Context

Read case intake, research notes, `deadlines-ledger.yaml`, `client-comms`, relevant guide and `review-queue.yaml`.

## Memo Principle

This is a scaffold for student analysis. Do not finalize legal advice. Use:

- `[待核验]` for unverified law/facts,
- `[学生分析]` where the student must reason,
- `[导师复核]` for judgment calls.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

# 案件备忘录

## 基本信息
## 事实时间线
## 当事人诉求
## 核心法律问题
## 可能法律依据
## 证据情况
## 程序路径
## 期限台账
## 法律援助 / 分流判断
## 学生分析区
## 风险和待核验事项
## 导师/律师复核问题
```

## State Behavior

- Any new deadline becomes a `/legal-clinic:deadlines add` candidate.
- Any memo used for client-facing advice or filing support must enter `review-queue.yaml` as `pending_review`.
- Store under `cases/[case_id]/memo-[date].md` when possible.
