---
name: skill-installer
description: >
  安装或接入已通过中国法审查的技能，生成安装记录、版本信息和回滚点。
argument-hint: "[技能名称或路径]"
---

# /legal-builder-hub:skill-installer

## 安装前门槛

- `skills-qa` 结论为 PASS 或 PASS WITH CONDITIONS 且条件已处理。
- 无真实凭证。
- 有测试用例或明确的人工复核说明。
- 安装来源可信并记录版本。

## 输出

```markdown
## 安装记录

技能：[名称]
来源：[路径/仓库/供应商]
版本：[版本]
审查结论：[结论]
安装范围：[默认启用/实验启用/仅手动调用]
回滚方式：[说明]
```

