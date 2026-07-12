---
name: cold-start-interview
description: >
  中国监管画像访谈。建立监管来源清单、制度库索引、重大性阈值、整改流程、Owner 和状态文件；支持 --redo 与 --check-integrations。
argument-hint: "[--redo | --check-integrations | --full]"
---

# /cold-start-interview

## 目标

建立可被 `reg-feed-watcher`、`policy-diff`、`gaps`、`comments` 和 `policy-redraft` 读取的中国监管实践画像。冷启动不是一次性问卷，而是状态化 workflow 的入口。

配置写入：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`

共享企业画像：

`~/.claude/plugins/config/claude-for-legal/company-profile.md`

状态文件：

- `gap-tracker.yaml`
- `comment-tracker.yaml`
- `verification-log.md`

## 模式

### `--check-integrations`

1. 检查 `.mcp.json` 中声明的 `legal-data` 与 `wps-cloud-docs` 是否存在。
2. 只有实际工具调用成功时才标为 `已连接`；无法测试时标为 `已配置未核验`。
3. 不得因 `.mcp.json` 存在就宣称数据源已生产级接入。
4. 更新配置中的 `## 可用集成` 表。

输出：

```markdown
# 集成检查
| 集成 | 状态 | 说明 | 不可用时回退 |
|---|---|---|---|
```

### `--redo`

重新访谈指定章节或全部章节。保留未变更的监管画像、制度库索引和 tracker 文件，不清空历史记录。

### 默认 / `--full`

运行完整访谈。若存在含 `<!-- SETUP PAUSED AT: -->` 的配置，询问用户是否继续；若存在已完成配置，询问是否更新，而不是覆盖。

## 访谈顺序

### 1. 企业与行业画像

- 企业主体、统一社会信用代码或内部简称。
- 注册地、主要经营地、业务覆盖省市。
- 行业和重点业务线。
- 是否涉及平台经济、数据/网信、金融、证券、医药、教育、进出口、产品质量、安全生产、广告、消费者权益、劳动用工等重点监管领域。

### 2. 监管来源清单

按中国来源建立 watchlist：

- 中央法律法规：国家法律法规数据库、中国人大网、国务院、中国政府网、司法部。
- 部门监管：网信办、市场监管总局、工信部、人社部、财政部、人民银行、金融监管总局、证监会、海关总署、国家知识产权局等。
- 司法与执法：最高人民法院、最高人民检察院、行政处罚公示、典型案例、监管问答。
- 地方来源：地方人大、地方政府、地方主管部门官网。
- 企业自有来源：内部合规台账、监管函、处罚决定、历史整改报告。

每个来源记录：来源名称、效力/内容类型、关注原因、检查频率、Owner、是否可自动检索。

### 3. 制度库索引

优先要求用户提供 WPS/金山文档、企业网盘、本地路径或粘贴目录。对每个制度记录：

- 制度名称。
- 文件位置或来源。
- 最近更新日期。
- Owner。
- 对应监管领域。
- 是否为正式现行版本。

不得在没有制度原文或索引时假设制度内容。若用户跳过，标记为 `[PENDING]`，并说明 `policy-diff` 会把相关要求默认列为“未匹配制度，需人工确认”。

### 4. 重大性阈值

建立三级阈值：

- `always_material`：立即处理，例如生效期限明确、处罚风险、监管函/检查、影响核心业务、需对外提交。
- `review_worthy`：需评估，例如征求意见稿、地方口径变化、同业处罚、监管问答。
- `fyi`：记录但暂不行动，例如一般新闻、会议讲话、非适用行业信息。

### 5. 整改与意见反馈流程

记录：

- 监管变化筛选人。
- 政策差距 Owner。
- 整改审批人。
- 征求意见稿是否反馈的决策人。
- 对外提交前的法务/合规负责人确认路径。
- 风险接受权限。

## 写入配置

创建父目录并写入：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`

模板：

```markdown
# Regulatory Legal Practice Profile

## 企业画像
...

## 监管来源清单
| 来源 | 类型 | 关注原因 | 频率 | Owner | 自动化状态 |
|---|---|---|---|---|---|

## 制度库索引
| 制度 | 文件/位置 | 最近更新 | Owner | 监管领域 | 状态 |
|---|---|---|---|---|---|

## 重大性阈值
### Always material
### Review-worthy
### FYI

## 整改流程
...

## 可用集成
| 集成 | 状态 | 回退 |
|---|---|---|
```

同时确保 tracker 文件存在；如不存在则创建空结构，不覆盖已有记录：

```yaml
gaps: []
```

```yaml
comments: []
```

## 完成输出

```markdown
# 中国监管画像已建立

> **复核提示**
> - **来源：** 用户提供 / 官方来源待核验
> - **读取范围：** [制度库索引状态]
> - **待判断事项：** [跳过或 PENDING 的项目]
> - **行动前：** 首次运行 `reg-feed-watcher` 前确认来源清单和重大性阈值

## 下一步
1. 运行 `/regulatory-legal:reg-feed-watcher` 检查监管动态。
2. 对重大事项运行 `/regulatory-legal:policy-diff`。
3. 用 `/regulatory-legal:gaps` 查看整改台账。
```
