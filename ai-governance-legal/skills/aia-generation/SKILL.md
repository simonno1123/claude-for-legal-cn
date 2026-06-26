---
name: aia-generation
description: >
  兼容旧命令的中国 AI 合规安全评估报告入口。建议新项目优先使用 /security-assessment。
argument-hint: "[AI 系统或使用场景说明]"
---

# /aia-generation

This is a compatibility alias for `/ai-governance-legal:security-assessment`.

When invoked, produce the same China Mainland AI safety and compliance assessment output as `skills/security-assessment/SKILL.md`. Do not use EU AI Act FRIA, GDPR DPIA, NIST AI RMF, or US impact-assessment templates as the default framework.

Mandatory additions:

- Distinguish algorithm recommendation filing from generative AI service filing/security assessment.
- Use TC260-PG-20241A as the operational safety review baseline where generative AI service safety assessment is triggered.
- Treat real-name authentication, content safety stop-filter, 24-hour report/disposal mechanism, visible/implicit marking, and vendor filing status as hard launch gates.
