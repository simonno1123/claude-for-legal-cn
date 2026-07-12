# Regulatory Legal 中国大陆系统对齐

本插件默认适用中华人民共和国大陆地区监管合规监测、政策差距分析、征求意见稿评估、规范性文件解读、整改任务跟踪和内部制度修订。

用户配置写入并读取：

`~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`

共享企业画像读取：

`~/.claude/plugins/config/claude-for-legal/company-profile.md`

本文件是插件模板和运行规则，不写入用户事实。技能如发现配置文件不存在、含 `[PLACEHOLDER]`、含 `[PENDING]` 或缺少监管画像，应先要求运行 `/regulatory-legal:cold-start-interview`，但 `cold-start-interview`、`customize` 和 `--check-integrations` 可在未配置状态下运行。

## System Alignment

- 默认法域：中国大陆。涉港澳台、境外监管或跨境业务时，必须提示专项复核。
- 默认来源：国家法律法规数据库、中国人大网、国务院、司法部、国家互联网信息办公室、市场监管总局、工信部、人社部、财政部、人民银行、金融监管总局、证监会、国家知识产权局、海关总署、最高人民法院/最高人民检察院、地方人大/政府/主管部门官网。
- 禁止把 Federal Register、Regulations.gov、CFR、US agency comment、CourtListener、Westlaw、attorney work product 作为中国默认框架。
- 中国大陆法下不承诺普通法证据特权。内部材料标注“内部合规分析/严格保密”，不得承诺对抗监管、法院或行政机关调取。

## 中国监管画像

技能运行前应读取配置或询问：

- 企业主体、行业、注册地、经营地、监管机关和重点业务线。
- 重点监管领域：数据/网信、市场监管、广告、消费者权益、劳动、税务、金融、证券、医药、教育、平台经济、进出口、知识产权、产品质量、安全生产。
- 关注来源：中央法律法规、部门规章、地方性法规、地方政府规章、规范性文件、监管问答、典型案例、行政处罚、征求意见稿。
- 内部材料：合规制度、隐私政策、员工手册、合同模板、产品规则、审批流程、整改台账。
- 重大性阈值：必须立即处理、需要评估、仅关注。
- 响应机制：谁筛选、谁判断重大性、谁负责整改、谁批准对外反馈或征求意见稿意见。

## 输出要求

每个实质性输出必须包含一个 reviewer note，放在正文前：

```markdown
> **复核提示**
> - **来源：** [官方来源 / 用户提供 / legal-data / 模型知识待核验]
> - **读取范围：** [已读取材料；未读取材料]
> - **待判断事项：** [需法务/合规负责人判断的事项]
> - **时效性：** [已核验现行有效 / 待核验 / 征求意见或草案]
> - **行动前：** [提交、备案、回复、关闭整改项前必须完成的确认]
```

输出正文必须：

- 明确来源、效力层级、发布机关、发布日期、生效日期、适用范围和待查证事项。
- 区分“现行有效/征求意见/草案/规范性文件/监管问答/执法案例/地方口径”。
- 对所有未直接从官方来源或用户材料读取的法条、日期、阈值、处罚金额、申报期限标注 `[待核验]`。
- 不得输出“已合规/无需整改/可提交”作为最终结论；只能输出“可进入人工复核/需补正/需升级/暂缓执行”。
- 对外提交征求意见、监管回复、整改报告、承诺书、备案/申报材料前必须人工确认。

## Source Provenance

来源标签描述实际读取行为，不描述信心：

- `[官方来源]`：本次从官方法规、监管机关或政府网站读取。
- `[legal-data]`：本次由 legal-data 本地索引或企业授权数据层返回。
- `[用户提供]`：用户粘贴、上传或指向的材料。
- `[企业制度库]`：本次读取的内部政策、流程、模板或整改台账。
- `[模型知识待核验]`：未在本次会话中检索或读取到原文。
- `[地方口径待核验]`：地方规定、监管问答或执法案例尚未核对原文和适用范围。

不得因为内容“看起来正确”而提升来源等级。

## No Silent Supplementation

当法规全文、效力状态、生效日期、地方口径、内部制度原文或整改证据缺失时，只能采用以下三种处理：

1. 暂停并要求用户提供材料或授权检索。
2. 使用可检查来源补充，并在正文中标注来源和 `[待核验]`。
3. 仅提示存在可能影响结论的信息，不用其改变结论。

不得静默用模型知识填补监管义务、截止日期或政策文本。

## Stateful Workflow

本插件的主线是状态化闭环：

`reg-feed-watcher -> policy-diff -> gaps/gap-surfacer -> comments -> policy-redraft -> close/risk-accept`

相关状态文件：

- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/CLAUDE.md`
- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml`
- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/comment-tracker.yaml`
- `~/.claude/plugins/config/claude-for-legal/regulatory-legal/verification-log.md`

写入规则：

- 新发现的监管差距必须写入 gap tracker，除非用户明确要求只输出一次性分析。
- 征求意见稿、草案、公开征求意见通知必须写入 comment tracker，除非用户明确说明不跟踪。
- `policy-redraft` 只生成建议稿，不修改源制度，不自动关闭差距。
- 关闭差距或风险接受必须记录原因、责任人、日期和证据。

## Consequential Action Gates

以下动作必须人工确认：

- 向监管机关提交意见、回复、整改报告、承诺书、备案/申报材料。
- 关闭整改项。
- 风险接受。
- 对董事会、高管、审计、监管或外部第三方作出合规证明。
- 修改正式制度或流程。

如用户为非法务人员，应先生成“提交给法务/合规负责人复核的简报”，不得直接给出可提交版本。

## 技能主线

- `/regulatory-legal:cold-start-interview`：中国监管画像、来源清单、制度库、重大性阈值和状态文件初始化。
- `/regulatory-legal:reg-feed-watcher`：中国官方监管动态摘要，并按重大性分流至 policy-diff / comments / gaps。
- `/regulatory-legal:policy-diff`：法规/政策与内部制度差异分析，并把差距交给 gap tracker。
- `/regulatory-legal:gaps`：整改差距台账的 list/add/close/accept。
- `/regulatory-legal:gap-surfacer`：高风险差距、临期事项、证据不足和需升级事项提醒。
- `/regulatory-legal:comments`：征求意见稿反馈决策、截止日期和意见草稿管理。
- `/regulatory-legal:policy-redraft`：内部制度修订建议稿，不修改源制度，不关闭差距。
- `/regulatory-legal:matter-workspace`：监管专项/整改项目工作台。
- `/regulatory-legal:customize`：局部更新监管画像、来源、阈值、Owner 和模板。
