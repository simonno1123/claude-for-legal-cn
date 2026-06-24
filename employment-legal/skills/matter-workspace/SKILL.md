---
name: matter-workspace
description: >
  Phase 1 默认关闭的劳动事项工作区管理。中国企业法务主场景默认使用统一 practice-level 上下文；仅外部律师多客户服务时才建议启用事项隔离。
argument-hint: "<status | enable-guidance>"
---

# /matter-workspace

## Phase 1 状态

本命令在 `employment-legal` 中国化第一阶段默认关闭。企业内控法务场景通常以同一用人单位为主，不应引入美式多客户/多 matter 模板，以免污染劳动用工分析。

## Instructions

1. 读取 `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`。
2. 若 `## Matter workspaces` 中 `Enabled` 为 `✗`、`Disabled`、`X` 或空值，直接告知：
   > 当前为中国企业法务默认模式，劳动事项工作区已关闭。请直接使用 practice-level 上下文处理解除、社保、工时、假期、手册和调查事项。外部律师如需多客户隔离，应先完成独立配置并经人工确认。
3. 不得自动创建、切换或读取多事项目录。
4. 如用户明确说明是外部律师且需要隔离多个客户，可输出配置建议，但仍要求人工确认后再启用。

## 输出口径

```markdown
# 劳动事项工作区状态

**当前状态：** Phase 1 默认关闭
**默认上下文：** 中国企业法务 practice-level
**原因：** 避免多客户/跨事项模板污染企业内部劳动法工作流
**如需启用：** 请由外部律师或管理员重新配置，并确认客户隔离、资料权限和保密规则
```
