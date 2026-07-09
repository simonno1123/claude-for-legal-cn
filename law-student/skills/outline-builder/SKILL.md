---
name: outline-builder
description: >
  按中国成文法体系、司法解释、课程材料和法考大纲搭建复习大纲。支持从
  学生材料提取结构、标记缺口和生成复习任务。
argument-hint: "[科目或专题] [--from-materials] [--update]"
---

# /law-student:outline-builder

## Required Context

Load:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
```

Ask for course notes, textbook table of contents, statute list, PPT or法考大纲. If unavailable, produce a scaffold with `[待填: 用户材料]` rather than a falsely complete outline.

## China-Law Structure

Use Chinese statutory hierarchy:

1. 法律关系 and basic concepts.
2. Current statutes and judicial interpretations.
3. Elements or request bases.
4. Defenses, exceptions and limitation periods.
5. Proof burden and procedure.
6. Guiding/typical cases or classroom examples.
7. Exam or practice prompts.

For民法, prioritize 请求权基础 and抗辩. For刑法, prioritize构成要件/违法性/责任. For procedure, prioritize jurisdiction, deadlines, evidence and remedies.

## Workflow

1. Confirm subject, exam goal and available materials.
2. Read materials if provided.
3. Build a skeleton first.
4. Mark all unsupported sections:
   - `[待填: 教材]`,
   - `[待核验: 法条]`,
   - `[需要案例]`,
   - `[老师重点未知]`.
5. Ask the student to fill one section or upload materials.
6. Update weak tags in the plan if recurring gaps appear.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources:
> - Flags:

# [Subject] Outline

## 1. 体系定位
## 2. 法条框架
## 3. 构成要件 / 请求权基础
## 4. 抗辩、例外和期限
## 5. 证明责任 / 程序节点
## 6. 案例和裁判规则
## 7. 易错点
## 8. 下一步填充任务
```

## Anti-Ghostwriting Boundary

Do not turn a professor's assignment into a complete answer. The outline is a study structure. If the user needs graded work help, provide feedback prompts and require their own draft.

## Persistence

When a course or subject outline is updated, record the update in `session_history` and, if useful, add next tasks to `study-plan.yaml`.
