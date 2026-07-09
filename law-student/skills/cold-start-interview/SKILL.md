---
name: cold-start-interview
description: >
  建立或重建中国法学习画像：学生身份、学校/课程、法考目标、考试日期、
  薄弱科目、学习风格、材料目录、学术诚信边界和状态文件。支持 --redo 与
  --check-integrations。
argument-hint: "[--redo] [--check-integrations] [--full]"
---

# /law-student:cold-start-interview

This command is the only substantive law-student command that may run before setup. It writes:

```text
~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md
~/.claude/plugins/config/claude-for-legal/law-student/study-plan.yaml
~/.claude/plugins/config/claude-for-legal/law-student/session_history/
```

## Setup Gate

1. Check `~/.claude/plugins/config/claude-for-legal/law-student/CLAUDE.md`.
2. If populated and no `--redo`, ask before overwriting.
3. If partial setup contains `SETUP PAUSED AT`, offer to resume.
4. If missing, start the interview.
5. With `--check-integrations`, only verify MCP/storage availability and update the integration block. Do not rewrite the profile.

## Academic Integrity Preamble

Before asking profile questions, say:

> This is a study tool. I will help you build outlines, practice questions, case notes and writing feedback, but I will not write graded work, exam answers, journal notes or course submissions for you. Check your school rules, teacher instructions and exam discipline before using AI on graded tasks.

If the user mentions real parties, real filings, real claims, real deadlines or a real client matter, pause and redirect to `legal-clinic`, school clinic supervision, legal aid or a licensed lawyer.

## Interview Flow

Ask no more than 2-3 answerable prompts per turn. Wait for real answers before moving on.

### Part 1: Who And Goal

- Role: 法学院学生 / 法考考生 / 实习生 / 自学者.
- School/program and course year if applicable.
- Target: 课程考试 / 法考客观题 / 法考主观题 / 案例研习 / 写作训练 / 实务入门.
- Target exam or milestone date.

### Part 2: Learning Style

- `drill-me`: prefer Socratic pressure, one question at a time.
- `explain-to-me`: prefer brief explanation, then practice.
- `hybrid`: explanation first, then drill.
- What the student avoids studying.
- Strong and weak subjects.

### Part 3: China-Law Subjects

Capture current status and weak points for:

- 民法、刑法、行政法。
- 民诉、刑诉、行政诉讼。
- 商经、理论法、三国法、知产、劳动、数据合规。
- Optional school-specific subjects.

### Part 4: Materials Intake

Ask for paths, pasted text or "skip for now" for:

- 教材目录、课程 PPT、课堂笔记。
- 法条/司法解释清单。
- 指导性案例、典型案例、裁判文书。
- 历年课程试题、老师反馈。
- 法考真题、模拟题、错题本。
- 已写主观题答案、课程论文草稿、案例评析草稿.

If fewer than 10 useful materials are provided, write `LIMITED DATA: yes` and tell downstream skills to be more cautious.

### Part 5: Integration Check

Only mark an integration as connected if a tool call actually succeeds. Configuration alone is not enough.

Record:

```markdown
| Integration | Status | Fallback |
|---|---|---|
| legal-data | connected / configured-not-tested / unavailable | Ask user for statute/case text |
| WPS / cloud docs | connected / configured-not-tested / unavailable | Local File Mode |
```

## Write The Profile

Create parent directories as needed. The profile must include:

- Role and real-matter redirect.
- Academic integrity boundaries.
- Current courses and target exam date.
- Learning style.
- Strong/weak subjects.
- Materials table.
- Integration status.
- Output label rule.
- State file locations.

Before writing, summarize skipped items and ask whether to fill them now or leave placeholders.

## Initialize State

If no `study-plan.yaml` exists, create an initial scaffold:

```yaml
student:
  role:
  target:
  target_date:
  weekly_hours:
preferences:
  learning_style:
  output_mode: study scaffold
subjects:
  民法:
    weight: 1.0
    weak_points: []
session_history: []
integrity:
  no_ghostwriting: true
  real_matter_redirect: legal-clinic
```

If file writes are unavailable, output the YAML and tell the user where to save it. Do not silently claim persistence.

## Close

End with:

- What was saved.
- What is still placeholder.
- Suggested next command: `/law-student:study-plan --build` or `/law-student:socratic-drill [subject]`.
