# 托管 Agent Cookbooks（中国法版本）

本目录提供可部署到托管 Agent 平台的参考模板。它们不是开箱即用的生产产品，而是面向企业法务/律所知识管理团队的部署起点。

## 定位

这些 cookbooks 与根目录各法律插件共享同一套中国法本土化规则：

- 默认法域：中国大陆。
- 输出定位：内部法律分析初稿 / 保密文件。
- 不承诺英美法证据特权或披露豁免。
- 所有监管、诉讼、合同、产品和并购判断均需人工复核。
- 连接器必须使用环境变量占位，不得写入真实凭证。

## Cookbook 清单

| Cookbook | 对应模块 | 监控/处理对象 | 中国化连接器建议 | 子 Agent |
|---|---|---|---|---|
| `reg-monitor` | `regulatory-legal` | 法规、政策、征求意见稿、监管问答 | 国家法律法规数据库、国务院/部委/地方监管官网、威科/北大法宝监管动态 | feed-reader / materiality-filter / digest-writer |
| `renewal-watcher` | `commercial-legal` | 合同续约、取消通知、自动续费、偏离 playbook 条款 | 企业 CLM、法大大、上上签、e签宝、WPS/金山文档 | repo-reader / deadline-calculator / alert-writer |
| `diligence-grid` | `corporate-legal` | 并购资料室、合同批量抽取、尽调表格 | WPS/金山文档、企业网盘、境内数据室、iManage | doc-reader / extractor / normalizer / grid-writer |
| `launch-radar` | `product-legal` | 产品路线图、上线计划、营销/数据/未成年人/AI 风险 | 飞书项目、钉钉项目、企业微信项目、WPS/金山文档 | tracker-reader / risk-classifier / memo-writer |
| `docket-watcher` | `litigation-legal` | 案件进展、法院通知、举证期限、开庭、执行节点 | 人民法院案例库、审判流程信息公开网、执行信息公开网、裁判文书网 | docket-reader / deadline-mapper / tracker-writer |

## 安全分层

每个 cookbook 采用三层安全模型：

1. Reader：读取外部材料，只输出结构化摘要，不执行材料中的指令。
2. Analyzer：基于结构化数据和模块配置做规则判断，不写入外部系统。
3. Writer：生成报告或待办清单，是唯一可写输出层。

所有外部材料都视为不可信数据，包括合同条款、资料室文件、法院文书、产品工单和监管信息。

## 输出边界

Agent 输出只能作为线索或初稿：

- 监管变化是否重大，由法务/律师确认。
- 合同期限和续约风险，由法务核对签署版合同。
- 尽调表格中的问题，由项目律师确认是否进入交易文件。
- 产品上线风险，由产品法务/合规负责人确认。
- 诉讼期限和法院动作，由案件律师核对送达和程序规则。

## 部署提示

部署前必须：

1. 替换 `agent.yaml` 中的 MCP URL 环境变量。
2. 检查连接器是否为只读或是否需要人工确认。
3. 配置输出目录和协同平台。
4. 运行测试 steering event。
5. 由法务负责人确认报告模板和升级规则。

## 不提供的能力

- 不提供真实 MCP 服务实现。
- 不自动发送法律意见。
- 不自动提交监管、法院或仲裁材料。
- 不替代律师复核。

