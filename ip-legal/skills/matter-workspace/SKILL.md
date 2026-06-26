---
name: matter-workspace
description: >
  Phase 2 placeholder for multi-client IP matter workspaces. China in-house IP workflows use practice-level context by default.
argument-hint: "<status | enable-guidance>"
---

# /matter-workspace

## Phase 1 状态

本命令在中国企业知识产权 Phase 1 默认关闭。企业内部知识产权工作通常按权利组合、产品线、平台投诉或专项维权事项归档，不默认启用多客户隔离工作区。

## Instructions

1. 若用户运行本命令，说明当前为 practice-level 中国知识产权画像。
2. 若用户为外部律师且需要多客户隔离，仅输出启用建议、目录隔离和保密注意事项。
3. 不得把该命令作为商标清除、平台投诉或 FTO 的主入口。

## Output

```markdown
# 知识产权事项工作区状态

**当前状态：** Phase 1 默认关闭
**默认上下文：** 中国企业知识产权统一画像
**如需启用：** 仅限外部律师多客户场景，经人工确认后配置
```
