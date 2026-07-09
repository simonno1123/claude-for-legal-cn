---
name: bar-prep-questions
description: >
  生成和讲解国家统一法律职业资格考试客观题/主观题练习，按薄弱科目、
  法考大纲、错题历史和现行中国法进行训练。
argument-hint: "[科目/章节] [--objective | --subjective | --session <n>]"
---

# /law-student:bar-prep-questions

## Required Context

Load:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
```

If the student profile does not identify the target exam, exam date or weak subjects, ask before generating questions.

## Source Discipline

- Use China National Unified Legal Professional Qualification Exam scope.
- Prefer current laws, judicial interpretations, official exam outline, user-provided prep materials and released questions.
- If relying on model knowledge, tag with `[待核验: model knowledge]`.
- Do not fabricate official真题, released answers, exam dates or pass standards.

## Modes

- `--objective`: single-choice, multiple-choice and indeterminate-choice questions.
- `--subjective`: small fact pattern, legal analysis, writing structure and scoring points.
- `--session <n>`: run N questions one at a time and write results to session history.

## Question Workflow

1. Confirm subject and type.
2. Weight subtopics by weak tags in `study-plan.yaml`.
3. Present one question at a time in session mode.
4. Wait for the student's answer.
5. Explain:
   - correct answer,
   - legal basis,
   - why each wrong option is wrong,
   - 易混点,
   - how to remember it.
6. Tag missed reasons:
   - 法条定位,
   - 概念混淆,
   - 构成要件遗漏,
   - 程序期限,
   - 事实代入,
   - 表达结构.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Flags:

# 法考练习

## Question
## Student Answer
## Correct Answer
## Legal Basis
## Wrong-Option Analysis
## 易混点
## Error Tags
```

## Persistence

For `--session <n>`, append results to `session_history` and update `study-plan.yaml`:

```yaml
session_history:
  - command: bar-prep-questions
    subject:
    mode:
    score:
    error_tags:
```

If persistence fails, output the record for manual saving.

## Academic Integrity

This skill may generate practice questions, but it must not answer active exams, contests or graded assignments. Convert such prompts into abstract practice problems.
