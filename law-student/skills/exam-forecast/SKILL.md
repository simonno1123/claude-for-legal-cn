---
name: exam-forecast
description: >
  根据法考大纲、课程范围、老师材料、过往试题、错题历史和新法新规生成
  复习权重和风险提示。不是押题，不承诺命中。
argument-hint: "[科目/课程] [--course | --fakao]"
---

# /law-student:exam-forecast

## Boundary

This skill produces study prioritization, not predictions of real exam questions. It must say when materials are insufficient and must not claim access to unreleased exam content.

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
```

Ask for:

- course syllabus,
- teacher slides,
- past exams,
- official法考大纲,
- released questions,
- recent law updates.

If unavailable, mark the forecast `LIMITED DATA`.

## Analysis Factors

- Exam scope and date.
- User weak subjects.
- Session error patterns.
- Teacher/course emphasis if materials exist.
- Current statutes and judicial interpretations.
- New or revised laws likely to affect study priority.
- High-frequency法考 topics.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Flags:
> - Before relying: verify syllabus / 法考大纲 version

# 复习重点 Forecast

## Confidence
## High Priority
## Medium Priority
## Low Priority
## New Law / Current-Law Watch
## Why These Weights
## What Not To Overstudy
## Next Study-Plan Update
```

## Persistence

Write forecast summary to:

```text
~/.claude/plugins/config/claude-for-legal/law-student/exam-forecasts/[subject]/forecast-[YYYY-MM-DD].md
```

Update `study-plan.yaml` priorities if the user confirms. Do not silently override the plan.

## Anti-Ghostwriting Boundary

Do not produce a memorized answer bank. Convert the forecast into study tasks, drills and source checks.
