---
name: cold-call-prep
description: >
  中国法课堂提问准备。针对案例、章节或法条主题，训练学生用自己的话回答
  老师追问，并记录薄弱点。
argument-hint: "[课程主题、案例或章节] [--drill-me | --outline-first]"
---

# /law-student:cold-call-prep

## Required Context

Read profile, current courses and materials:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
```

If the case or chapter text is not provided, ask the student to paste it, provide a path, or authorize use of model knowledge with `[待核验]` tags. Do not invent case facts.

## Workflow

1. Confirm course, teacher style if known, and whether this is class prep or graded assessment.
2. Build a prep map:
   - 30-second factual summary,
   - legal relationship,
   -争议焦点,
   - governing statutes/judicial interpretations,
   - request basis or elements,
   - likely defenses and proof issues,
   - policy or doctrinal tension.
3. Run Ask-Wait-Pushback:
   - Ask one likely teacher question.
   - Wait.
   - Give concise feedback.
   - Ask one follow-up.
4. Close with a short checklist for review before class.

## Output Scaffold

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Flags:

# Cold-Call Prep

## One-Minute Map
## Likely Questions
## Drill Log
## Need-To-Verify
## Before Class
```

## Anti-Ghostwriting Boundary

Do not script a memorized full answer for the student to recite. Give prompts, issue maps and feedback on the student's own answers.

## Tracking

Write a session note to:

```text
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
```

Use tags such as `案情概括`, `法条定位`, `争点提炼`, `追问抗压`, `证明责任`.
