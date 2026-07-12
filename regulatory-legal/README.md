# Regulatory Legal（中国监管合规定制版）

本插件面向中国企业法务、合规、内控和监管事务团队，用于跟踪中国人大、国务院、部委、地方政府、监管机关发布的法律法规、部门规章、规范性文件、监管问答、征求意见稿和执法动态，并转化为内部制度修订、整改任务、征求意见反馈决策和可关闭的整改台账。

## 核心命令

| 命令 | 用途 |
|---|---|
| `/regulatory-legal:cold-start-interview` | 建立中国监管画像、行业标签、来源清单和重大性阈值 |
| `/regulatory-legal:reg-feed-watcher` | 生成中国监管动态摘要 |
| `/regulatory-legal:policy-diff` | 将新规与内部制度/流程/模板做差异分析 |
| `/regulatory-legal:gaps` | 维护监管差距和整改任务台账 |
| `/regulatory-legal:gap-surfacer` | 提醒高风险差距、期限和需升级事项 |
| `/regulatory-legal:comments` | 评估征求意见稿是否反馈，并起草内部意见 |
| `/regulatory-legal:policy-redraft` | 生成制度修订建议稿 |
| `/regulatory-legal:matter-workspace` | 按监管专项或整改项目建立工作台 |
| `/regulatory-legal:customize` | 局部更新监管来源、阈值、Owner 和模板 |

## 状态化工作流

本插件的 v1 Faithful Port 工作流不是一次性摘要，而是闭环：

```text
reg-feed-watcher -> policy-diff -> gaps/gap-surfacer -> comments -> policy-redraft -> close/risk-accept
```

- `cold-start-interview` 建立监管画像、制度库索引、重大性阈值和 Owner。
- `reg-feed-watcher` 发现监管动态并按重大性分流。
- `policy-diff` 将监管要求映射到内部制度并生成 gap。
- `gaps` 和 `gap-surfacer` 维护整改生命周期，直到关闭或风险接受。
- `comments` 跟踪征求意见稿是否反馈、截止日期和提交状态。
- `policy-redraft` 只生成制度修订建议稿，不修改源制度，不自动关闭 gap。

## 默认资料源

- 国家法律法规数据库、中国人大网、国务院、司法部。
- 国家网信办、市场监管总局、工信部、人社部、财政部、人民银行、金融监管总局、证监会、海关总署、国家知识产权局。
- 最高人民法院、最高人民检察院。
- 地方人大、地方政府、地方主管部门官网。
- 用户提供的内部制度、合规台账、监管函、处罚决定、问答或征求意见稿。

## 输出边界

所有输出均为内部监管合规分析初稿。对外提交征求意见、监管回复、整改报告、承诺书、备案/申报材料，或关闭整改项、作出风险接受前，必须经企业法务、合规负责人或中国执业律师复核。
