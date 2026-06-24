---
name: customize
description: >
  Deprecated compatibility command. Product-legal China localization uses cold-start-interview as the only Phase 1 initialization entry.
argument-hint: "[地区/行业/产品类型/监管主题]"
---

# /customize

## Phase 1 状态

本命令已并入 `/product-legal:cold-start-interview`，不再作为独立初始化入口。这样可以避免产品画像、监管口径和风险阈值在多个配置入口之间相互覆盖。

## Instructions

1. 如果用户试图运行本命令，先说明当前中国版已采用单入口初始化。
2. 引导用户运行 `/product-legal:cold-start-interview --redo` 更新产品画像。
3. 如用户只是补充某个地方监管口径或行业口径，可输出一段可复制到产品画像中的补充配置，但不得另建独立配置源。

## Output

```markdown
# 配置入口提示

`/product-legal:customize` 已并入 `/product-legal:cold-start-interview`。

建议动作：
- 更新整体产品画像：运行 `/product-legal:cold-start-interview --redo`
- 只补充地方/行业口径：将以下补充项写入现有产品画像
```
