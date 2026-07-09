---
name: flashcards
description: >
  生成、更新和复习中国法条、概念、构成要件、期限、易混点和错题卡片。
  使用 Leitner-style buckets 并写入学习状态。
argument-hint: "[科目或专题] [--generate | --drill | --session <n>]"
---

# /law-student:flashcards

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/flashcards/
```

If no profile exists, route to cold-start.

## Card Types

- 法条定位卡: question asks where the rule comes from.
- 构成要件卡: front asks for elements; back gives element map and易错点.
- 请求权基础卡: front gives fact pattern; back asks claim basis and defenses.
- 程序期限卡: front asks deadline, trigger and consequence.
- 易混点卡: compare two similar concepts.
- 错题卡: derived from session_history error tags.

## Modes

- `--generate`: generate cards from supplied material or weak tags.
- `--drill`: ask cards one at a time, wait for answer, then reveal.
- `--session <n>`: run N cards and update buckets.

## Card Format

```markdown
---
subject:
topic:
source:
bucket: 1
last_seen:
next_review:
error_tags: []
---

Q:
A:
Why it matters:
Verify:
```

Use `[待核验]` on any statute, article number or case rule that is not confirmed from user materials or legal-data.

## Drill Flow

1. Show front only.
2. Wait for the student's answer.
3. Reveal back and critique.
4. Move bucket:
   - correct and confident: +1,
   - partially correct: stay,
   - wrong: bucket 1.
5. Write updated card metadata where possible.

## Persistence

Store per subject:

```text
~/.claude/plugins/config/claude-for-legal/law-student/flashcards/[subject]/cards.md
```

Append session score to `session_history` and update weak tags in `study-plan.yaml`.

## Academic Integrity

Cards are memory aids. Do not convert them into complete answer scripts for graded tasks.
