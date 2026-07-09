---
name: study-plan
description: >
  生成、更新、查看或冲刺调整中国法课程/法考学习计划。读写 study-plan.yaml，
  根据 session_history、错题、弱项和目标日期动态调整。
argument-hint: "[--build | --update | --status | --cram]"
---

# /law-student:study-plan

## Required Context

Load before doing substantive work:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
```

If the profile is missing or still contains placeholders, stop and route to `/law-student:cold-start-interview`.

## Modes

- `--build`: create a new plan. Use when no plan exists or the user asks to start over.
- `--update`: update weights and next tasks from session history.
- `--status`: show today, this week, slipping subjects, and next review dates.
- `--cram`: build a high-yield final-stage plan, emphasizing current law, core elements, error patterns and rest.

## Plan Logic

1. Calculate available days and weekly hours.
2. Weight subjects by:
   - target exam or course date,
   - weak subjects in profile,
   - recent session scores,
   - repeated error tags,
   - legal update/currency needs.
3. Split each subject into:
   - law-text reading,
   - element/request-basis map,
   - case or example,
   - objective questions,
   - subjective writing,
   - review and recall.
4. Keep plans realistic. If hours are impossible, say so and propose a smaller plan.

## YAML Shape

Write or update:

```yaml
student:
  target:
  target_date:
  weekly_hours:
plan:
  current_phase: foundation | consolidation | mock | cram
  generated_at:
  next_review_at:
subjects:
  民法:
    weight: 1.4
    weak_points:
      - 请求权基础识别
    next_tasks:
      - read: 民法典合同编
      - drill: 买卖合同风险负担
    last_score:
session_history:
  - date:
    command:
    subject:
    score:
    error_tags: []
```

If writes fail, present the updated YAML for manual saving and flag that persistence did not occur.

## Output Format

```markdown
学习笔记 / 非法律意见

> **Reviewer note**
> - Sources: 学习画像 + study-plan.yaml + session_history
> - Flags: [missing data / none]
> - Before relying: 核对考试日期、学校规则和法考大纲版本

# 学习计划

## 当前阶段
## 本周重点
## 今日任务
## 弱项权重调整
## 复盘安排
## 需要补充的材料
```

## Anti-Ghostwriting Boundary

Do not write assignment answers or course submissions as part of the plan. Schedule practice tasks and feedback loops instead.

## Integration

- `/law-student:session` appends performance data that this command reads.
- `/law-student:bar-prep-questions --session <n>` and `/law-student:irac-practice` should write score/error tags back into the plan.
- `/law-student:customize` may adjust weights and schedule constraints.
