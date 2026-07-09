---
name: research-start
description: >
  为中国法律诊所案件生成初步检索路径、法条清单、主管机关、案例线索和待核查问题。
  这是研究起点，不是最终法律意见。
argument-hint: "[案由或问题]"
---

# /legal-clinic:research-start

## Required Context

Read clinic profile, relevant guide, case intake, `deadlines-ledger.yaml` and review flags.

## Workflow

1. Confirm matter type and jurisdiction.
2. Identify legal relationship and procedural path.
3. List primary statutes, regulations, judicial interpretations and official guidance.
4. Identify official bodies: court, arbitration commission, legal aid center, regulator, mediation organization.
5. Generate search terms for legal-data, official websites and user-provided materials.
6. Mark every unverified source `[待核验]`.
7. If a possible deadline appears, hand off to `/legal-clinic:deadlines add`.
8. If research is for an external-facing memo/draft, submit output to review queue before final use.

## Output

```markdown
学生/志愿者法律服务工作底稿 / 需导师或执业律师复核

# Research Start

## Issue
## Possible Legal Basis
## Procedure / Forum
## Official Sources To Check
## Case / Typical Example Search
## Facts Needed
## Deadline / Limitation Watch
## Supervisor Questions
```

## Not Allowed

Do not invent statutes, cases, local forms or filing windows. If a legal basis cannot be verified, say what source must be checked.
