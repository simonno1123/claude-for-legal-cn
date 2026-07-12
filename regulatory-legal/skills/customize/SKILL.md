---
name: customize
description: >
  局部更新中国监管画像、来源清单、重大性阈值、Owner、整改流程、制度库索引和输出模板，并提示对 tracker 的影响。
argument-hint: "[要更新的配置项]"
---

# /customize

## 目标

在不重跑完整 cold-start 的情况下，更新监管实践画像。该技能必须写入配置文件，并提示哪些状态文件或开放事项可能受影响。

配置路径：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`

## 可更新字段

- 监管来源清单。
- 重点监管领域。
- 制度库索引。
- 重大性阈值。
- Gap Owner / Comment Owner。
- 整改审批链。
- 风险接受权限。
- 输出模板或内部复核口径。

## Workflow

1. 读取当前配置。
2. 对比用户提出的新配置。
3. 输出字段变更表。
4. 标记影响范围：
   - 是否影响 `reg-feed-watcher` 覆盖。
   - 是否影响 `policy-diff` 匹配制度。
   - 是否影响 gap/comment Owner。
   - 是否需要重分配开放 tracker 项。
5. 经用户确认后写入配置。
6. 如 Owner 或阈值变更，提示是否需要重新运行 `/regulatory-legal:gaps` 或 `/regulatory-legal:comments`。

## 输出格式

```markdown
# 监管画像更新记录

> **复核提示**
> - **来源：** 用户确认
> - **读取范围：** 当前监管画像
> - **待判断事项：** [是否需要重分配开放事项]
> - **行动前：** 写入配置前确认

| 字段 | 原值 | 新值 | 影响范围 |
|---|---|---|---|

## 需要同步更新
- [ ] 来源清单
- [ ] 重大性阈值
- [ ] 整改台账
- [ ] 征求意见 tracker
- [ ] 制度库
- [ ] Owner/审批链
```
