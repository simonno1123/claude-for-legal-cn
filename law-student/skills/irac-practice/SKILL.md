---
name: irac-practice
description: >
  中国法主观题与课程论证训练。可使用 IRAC 作为表达容器，但实体分析必须
  回到法条、构成要件、请求权基础、证明责任和裁判规则。
argument-hint: "[题目、事实或学生答案] [--grade | --drill]"
---

# /law-student:irac-practice

## Method

IRAC is only a writing container:

- Issue = 争点识别。
- Rule = 法条、司法解释、构成要件、请求权基础、程序规则。
- Application = 事实与要件逐项对应，含抗辩和证明责任。
- Conclusion = 可争议结论和得分风险。

Do not import common-law defaults as substantive law. Default to PRC mainland law and the student's course or法考 scope.

## Required Context

Read:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/
```

If the user wants grading, require their own answer first. Do not provide a model answer first.

## Modes

- `--drill`: ask one issue or element question at a time and wait.
- `--grade`: grade the student's answer against a rubric.
- default: if no student answer is provided, run `--drill`.

## Rubric

```markdown
## Scoring
- Issue spotting:
- Rule/source accuracy:
- Element/request-basis structure:
- Fact application:
- Defense/exception:
- Proof/procedure:
- Conclusion:
- Expression:
```

Use qualitative levels if no numeric rubric is provided: strong / adequate / weak / missing.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Flags:

# IRAC / 主观题 Feedback

## What You Did Well
## Missing Issues
## Rule / Source Checks
## Element Mapping
## Fact Application
## Score Risk
## Next Drill
```

## Anti-Ghostwriting Boundary

Do not write the student's final answer. You may give a short generic example of a reasoning move, but not a paragraph that answers the actual graded question for submission.

## Tracking

Append session notes to:

```text
~/.claude/plugins/config/claude-for-legal/law-student/irac-sessions/[student]/
```

Update weak tags in `study-plan.yaml`, especially `争点遗漏`, `规则错误`, `事实代入薄弱`, `抗辩遗漏`, `证明责任错误`.
