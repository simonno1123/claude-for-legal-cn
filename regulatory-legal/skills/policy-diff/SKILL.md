---
name: policy-diff
description: >
  中国法规/政策与内部制度差异分析。提取新规要求，核验效力状态，匹配制度库，形成差距项并交给 gap tracker。
argument-hint: "[法规/政策文本 + 内部制度/流程/模板 | GAP/事项 ID]"
---

# /policy-diff

## 目标

将监管变化转换为可整改、可跟踪的制度差距。该技能必须连接 `reg-feed-watcher` 与 `gaps`，而不是只输出一次性表格。

## Workflow

### Step 1: 读取配置和输入

读取：

- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`
- 制度库索引。
- 用户提供、官方来源或 `reg-feed-watcher` 传入的监管文本。

若缺少监管原文或制度原文，不得推测。要求用户粘贴、上传、指定文件，或同意使用待核验来源。

### Step 2: 效力和时效核验

标注：

- 发布机关。
- 效力层级。
- 发布日期。
- 生效日期。
- 是否为征求意见稿、草案、规范性文件、监管问答或执法案例。
- 是否已核验官方原文。

无法核验时，所有日期和义务标注 `[待核验]`，并不得作为“已逾期”整改项。

### Step 3: 提取要求

把监管文本拆为离散要求：

| # | 要求 | 适用对象 | 生效/截止 | 来源 |
|---|---|---|---|---|

要求必须具体到动作、对象、期限或材料；不得写成“加强管理”这类泛化描述。

### Step 4: 匹配制度库

对每项要求匹配：

- 直接命中：制度明确覆盖。
- 部分命中：制度涉及主题但缺少新要求。
- 未命中：没有对应制度或流程。
- 不适用：企业业务/地域/主体不适用，但需说明依据。
- 观察项：征求意见稿、草案、监管趋势，暂不构成整改义务。

### Step 5: 生成差距并写入 tracker

对 `partial`、`full`、`new-policy` 生成 gap 项：

```yaml
- id: GAP-[next]
  requirement: "[具体要求]"
  regulation: "[文件名称 + 条款/来源]"
  source_level: "[法律/行政法规/部门规章/地方规定/规范性文件/监管问答/执法案例]"
  source_tag: "[官方来源/legal-data/用户提供/待核验]"
  policy_affected: "[制度名称或 new policy needed]"
  gap_type: "partial|full|new-policy|watch"
  owner: "[Owner 或 unassigned]"
  opened: "[YYYY-MM-DD]"
  due: "[YYYY-MM-DD 或 null]"
  status_verified: true|false
  status: "open"
  evidence: ""
  resolution: ""
```

重复项按“同一要求 + 同一制度”去重。不得因规则未核验而标为 overdue。

### Step 6: 输出

```markdown
# 监管政策差异分析

> **复核提示**
> - **来源：** [来源标签]
> - **读取范围：** [监管文本和制度文本]
> - **待判断事项：** [需人工判断]
> - **时效性：** [已核验 / 待核验]
> - **行动前：** 确认规则现行有效和制度版本

## 规则状态
| 项目 | 内容 |
|---|---|
| 发布机关 | |
| 效力层级 | |
| 状态 | |
| 生效/截止 | |

## 要求提取
| # | 要求 | 适用对象 | 来源 | 核验 |
|---|---|---|---|---|

## 差异清单
| 要求 | 现有制度 | 差距类型 | 整改动作 | Owner | Gap ID |
|---|---|---|---|---|---|

## 不构成整改义务 / 观察项

## 下一步
- [ ] 对 `partial/full/new-policy` 运行 `/regulatory-legal:gaps`
- [ ] 对需修订制度运行 `/regulatory-legal:policy-redraft`
- [ ] 对征求意见事项运行 `/regulatory-legal:comments`
```
