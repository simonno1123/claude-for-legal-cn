---
name: matter-workspace
description: >
  以监管专项、征求意见、整改项目、行政检查或处罚应对为单位建立工作台；支持 new/list/switch/close/none 的轻量事项隔离。
argument-hint: "<new | list | switch | close | none> [专项名称]"
---

# /matter-workspace

## 目标

为监管专项、整改项目、征求意见、行政检查或处罚应对建立独立工作台，避免不同专项的材料、Owner、期限和输出混淆。

默认目录：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/matters/<matter-slug>/`

## 子命令

- `new <slug>`：创建监管专项工作台。
- `list`：列出当前和归档专项。
- `switch <slug>`：切换当前专项。
- `close <slug>`：归档专项，不删除文件。
- `none`：回到 practice-level 上下文。

## Workflow

1. 读取监管画像中的 `## Matter workspaces` 或当前 active matter。
2. 如未启用 matter workspace，但用户只是做企业内部单一监管项目，可输出 practice-level 状态并说明不需要切换。
3. 创建时写入 `matter.md`、`history.md`、`notes.md`。
4. 不跨 matter 读取材料，除非配置明确允许且用户明确要求。

## matter.md 模板

```markdown
# 监管专项工作台

## 基本信息
- 专项：
- Slug：
- 来源：
- 监管机关：
- Owner：
- 状态：
- 开始日期：

## 材料
| 材料 | 来源 | 版本 | 状态 |
|---|---|---|---|

## 动作
| 动作 | Owner | 截止 | 状态 |
|---|---|---|---|

## 关联 tracker
- Gap IDs:
- Comment IDs:

## 保密和权限
```

## 输出

```markdown
# 监管专项工作台状态

> **复核提示**
> - **来源：** matter workspace
> - **读取范围：** [matter 文件]
> - **待判断事项：** [权限/跨事项读取/归档]
> - **行动前：** 不跨专项读取或输出未授权材料
```
