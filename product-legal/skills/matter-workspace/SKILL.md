---
name: matter-workspace
description: >
  Phase 2 placeholder. Multi-client matter workspaces are disabled for Phase 1 China enterprise product legal workflows.
argument-hint: "<status | enable-guidance>"
---

# /matter-workspace

## Phase 1 状态

本命令在 `product-legal` 中国化 Phase 1 默认关闭。中国企业内部产品法务通常按产品、功能、营销活动或监管事项归档，不需要默认启用多客户工作区。

## Instructions

1. 直接说明当前为中国企业产品法务 practice-level 上下文，不创建事项目录。
2. 若用户明确说明其为外部律师并服务多个客户，仅输出启用建议和保密隔离注意事项。
3. 不得把该命令作为产品上线审查主入口。

## Output

```markdown
# 产品事项工作区状态

**当前状态：** Phase 1 默认关闭
**默认上下文：** 中国企业产品法务统一产品合规画像
**如需启用：** 仅限外部律师多客户场景，经人工确认后配置
```
