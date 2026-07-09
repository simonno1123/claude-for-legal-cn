---
name: session
description: >
  管理一次中国法学习会话，按科目、题型和目标记录练习结果、错因标签、
  待复习点和下一步任务，并写入 session_history。
argument-hint: "[科目] [题量或时长] [--objective | --subjective | --case | --statute]"
---

# /law-student:session

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
```

Append to:

```text
~/.claude/plugins/config/claude-for-legal/law-student/session_history/YYYY-MM-DD-[subject].md
```

Also update `study-plan.yaml.session_history` when file writes are available.

## Session Types

- `--objective`: 法考客观题、单选、多选、不定项。
- `--subjective`: 法考主观题、课程案例分析、论证结构。
- `--case`: 案例研习、争点与裁判规则。
- `--statute`: 法条定位、构成要件、期限、例外。

If no type is given, ask the student to pick one. Do not silently choose.

## Flow

1. Confirm subject, session type, target count/time and learning mode.
2. Check academic integrity. If this is graded work, only run a feedback/scaffold session.
3. Ask one task or question at a time.
4. Wait for the student's answer.
5. Give feedback:
   - correct points,
   - missing elements,
   - wrong legal basis,
   - fact-to-element gaps,
   - citation/source items to verify.
6. Assign error tags:
   - 法条定位,
   - 请求权基础,
   - 构成要件,
   - 事实代入,
   - 抗辩,
   - 证明责任,
   - 程序期限,
   - 表达结构.
7. At the end, write the session summary.

## Session Record

```markdown
# Session History

Date:
Subject:
Type:
Source materials:
Score:

## Questions / Tasks
1. Prompt:
   Student answer:
   Feedback:
   Error tags:

## Pattern Summary
- Strong:
- Weak:
- Repeat errors:

## Next Tasks
- Review:
- Drill:
- Writing:
```

## Learning Mode Boundary

Do not dump a full answer set at the beginning. If the student requests all answers first, refuse and offer to run the session one item at a time.

## Persistence Failure

If `session_history` or `study-plan.yaml` cannot be written, output the Markdown record and updated YAML fragment. Tell the user persistence failed instead of claiming the plan was updated.
