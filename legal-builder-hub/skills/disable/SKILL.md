---
name: disable
description: >
  禁用不合规、过期、含凭证风险或尚未中国化的技能，并记录原因和恢复条件。
argument-hint: "[技能名称]"
---

# /legal-builder-hub:disable

## 禁用触发

- 出现 P0 阻断。
- 含真实凭证或敏感配置。
- 默认输出美国法/普通法框架。
- 乱码、JSON 错误或 frontmatter 缺失。
- 复核失败。

## 输出

```markdown
技能：[名称]
禁用原因：[原因]
影响范围：[命令/模块]
恢复条件：[修复项]
```

