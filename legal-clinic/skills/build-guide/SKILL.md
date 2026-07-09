---
name: build-guide
description: >
  为中国法律诊所某一案由建立办案指南，沉淀接待问题、材料清单、法律依据、
  期限风险、分流路径、教学姿态和复核门控。
argument-hint: "[案由]"
---

# /legal-clinic:build-guide

## Required Context

Read `CLAUDE.md`, existing guides, `deadlines-ledger.yaml` patterns and `review-queue.yaml` return reasons. Write:

```text
~/.claude/plugins/config/claude-for-legal/legal-clinic/guides/[案由].md
```

## Guide Sections

```markdown
# [案由] 办案指南

## 适用范围
## 不接收 / 必须分流
## 接待问题
## 材料清单
## 法律依据和待核验来源
## 常见程序路径
## 期限风险和 deadlines-ledger.yaml 字段
## 法援资格初核
## 教学姿态
## 必须进入 review-queue.yaml 的事项
## 学生练习任务
```

## Review Gate

New or revised guides must be submitted to `review-queue.yaml` as `pending_review`. A guide is not operational until approved.

## China-Law Mapping

Use 中国法律援助、公服咨询、仲裁、诉讼、行政投诉、调解 and local official forms. Do not import U.S. clinic practice rules.
