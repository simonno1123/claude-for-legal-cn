---
name: reg-feed-watcher
description: >
  中国官方监管动态摘要。读取监管画像和来源目录，按重大性阈值筛选法律法规、部门规章、规范性文件、监管问答、执法案例和征求意见稿，并分流到 policy-diff / comments / gaps。
argument-hint: "[--since YYYY-MM-DD | 来源/日期范围/监管领域]"
---

# /reg-feed-watcher

## 目标

拉取或整理中国监管动态，按企业重大性阈值筛选，输出摘要，并把可跟踪事项分流：

- 现行有效或即将生效的监管义务 -> `/regulatory-legal:policy-diff`
- 征求意见稿、草案、公开征求意见通知 -> `comment-tracker.yaml`
- 明确整改事项 -> `gap-tracker.yaml`

## 强制规则

- 读取 `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`。
- 调用本技能目录下 `references/source-catalog.md` 作为中国来源目录。
- 不使用 Federal Register、Regulations.gov 或美国 agency feed 作为默认来源。
- 未核验官方原文时标注 `[官方来源待查证]`。
- 不得把征求意见稿、草案、监管问答或执法案例当作现行有效规则。
- 不得静默补充监管动态；若来源不足，应说明覆盖缺口。

## Workflow

### Step 0: 覆盖检查

对比配置中的监管来源清单和 `references/source-catalog.md`：

- 是否缺少企业重点领域的中央主管部门。
- 是否缺少经营地地方来源。
- 是否缺少征求意见、处罚公示、监管问答来源。

如存在明显缺口，在摘要开头提示一次，并建议用 `/regulatory-legal:customize` 或 `/regulatory-legal:cold-start-interview --redo` 更新。

### Step 1: 获取事项

按可用来源顺序处理：

1. 用户粘贴或上传的监管动态。
2. `legal-data` 或企业本地索引返回的法律法规、规章、规范性文件、案例或问答。
3. 官方网站、政府网站、监管机关页面或企业自建采集结果。
4. 未能检索时，仅输出覆盖缺口，不用模型知识补齐。

每条事项至少记录：

- 来源名称。
- 发布机关。
- 文件/事项标题。
- 类型：法律、行政法规、部门规章、地方规定、规范性文件、监管问答、执法案例、征求意见稿、草案、处罚/监管动态。
- 发布日期、生效日期或征求意见截止日期。
- 官方链接或用户材料来源。
- 来源标签。

### Step 2: 去重与效力识别

同一事项在多个来源出现时保留官方来源作为主记录。对状态进行标注：

- `现行有效`
- `尚未生效`
- `征求意见`
- `草案`
- `规范性文件`
- `监管问答/指导口径`
- `执法案例/行政处罚`
- `待核验`

### Step 3: 重大性分类

按配置中的 `always_material`、`review_worthy`、`fyi` 分类。

默认规则：

- 已生效或有明确生效日期且影响企业重点业务：高优先级。
- 征求意见稿有截止日期：需评估，并写入 comment tracker。
- 同业处罚、监管问答、地方口径：需评估或 FYI，视行业匹配度而定。
- 新闻、会议讲话、非适用行业信息：FYI。

### Step 4: 写入跟踪

征求意见稿/草案/公开征求意见：

- 写入 `comment-tracker.yaml`，状态为 `undecided`。
- 记录 comment deadline、Owner、官方链接、是否已提醒。

明确需要制度差异分析的事项：

- 在摘要中标注“建议运行 `/regulatory-legal:policy-diff`”。
- 如用户要求自动建立预备项，可在 gap tracker 中写入 `gap_type: watch`，不得当作已确认差距。

### Step 5: 输出

```markdown
# 中国监管动态摘要

> **复核提示**
> - **来源：** [官方来源 / legal-data / 用户提供 / 待核验]
> - **读取范围：** [检查的来源和期间]
> - **待判断事项：** [N 项需法务/合规判断]
> - **时效性：** [已核验 / 待核验]
> - **行动前：** 对重大事项运行 policy-diff；对外动作需人工确认

## 高优先级
| 来源 | 文件/事项 | 状态 | 影响 | 动作 |
|---|---|---|---|---|

## 需评估
| 来源 | 文件/事项 | 截止/生效 | 建议动作 |
|---|---|---|---|

## 征求意见稿/草案
| 文件 | 发布机关 | 截止 | Comment ID | Owner |
|---|---|---|---|---|

## FYI

## 覆盖缺口

## 建议动作
- [ ] 运行 `/regulatory-legal:policy-diff`
- [ ] 查看 `/regulatory-legal:gaps`
- [ ] 查看 `/regulatory-legal:comments`
```
