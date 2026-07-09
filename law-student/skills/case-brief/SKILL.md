---
name: case-brief
description: >
  中国案例研习笔记。围绕案情、争点、法条、请求权基础/构成要件、证明责任、
  裁判要旨、类案价值和课堂讨论进行学习。
argument-hint: "[案例文本、案号或材料路径] [--drill]"
---

# /law-student:case-brief

## Required Context

Read the student profile and course context. If the case text is not provided, ask for:

- 裁判文书全文,
- 指导性案例/典型案例全文,
- 教材节选,
- 课堂材料,
- or permission to proceed with a limited `[待核验]` scaffold.

Do not invent facts, courts, holdings, docket numbers or裁判理由 from an案号 alone.

## China Case Study Mapping

Map upstream case-brief responsibility to 中国案例研习:

- 案情要点,
- 程序经过,
- 争议焦点,
- 适用法条/司法解释,
- 请求权基础 or 构成要件,
- 证明责任,
- 裁判要旨,
- 类案检索价值,
- 学习和考试价值.

## Modes

- Default: build a study scaffold from supplied case text.
- `--drill`: ask the student to fill each section first, then critique.

If learning style is `drill-me`, prefer `--drill` unless the user asks otherwise.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Read:
> - Flags:

# 案例研习

## 案例信息
## 核心事实
## 程序与裁判结果
## 争议焦点
## 法律依据
## 请求权基础 / 构成要件
## 事实对应关系
## 证明责任
## 裁判规则
## 类案检索要点
## 课堂/法考易错点
```

## Ask-Wait Option

When drilling:

1. Ask the student for the issue.
2. Wait.
3. Push back.
4. Ask for the legal basis.
5. Continue one section at a time.

## Tracking

Append summary tags to `session_history`:

```yaml
case_brief:
  subject:
  case_source:
  weak_tags:
    - 争议焦点
    - 法条定位
    - 裁判规则提炼
```

## Academic Integrity

Do not produce a ready-to-submit case note for a graded assignment. Provide scaffold and feedback unless the task is clearly ungraded study.
