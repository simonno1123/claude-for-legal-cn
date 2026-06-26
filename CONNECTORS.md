# 添加连接器

## China Case Authority Update Connectors

The repository now reserves an update interface for guiding cases, reference cases, typical cases, and ordinary judgments:

- Rule file: `references/china-case-authority.md`
- Source/update contract: `references/case-authority-sources.json`

Recommended MCP connector placeholders:

| Connector | Source | Purpose |
|---|---|---|
| `people-court-case-library` | ??????? | guiding cases and reference cases |
| `supreme-peoples-court` | ???????? | guiding cases, typical cases, judicial policy releases |
| `china-judgments-online` | ??????? | ordinary judgments for trend/sample research |
| `commercial-legal-database` | ???? / ???? / ?? / Alpha | bring-your-own-key legal research integration |

These connectors must return metadata including case type, case number, issuing court/body, retrieval date, source URL, and freshness tag. They must not store real credentials in repository files; use environment variables only.


> 中国版默认连接器建议见 [`references/china-connectors.md`](references/china-connectors.md)。本文件继续作为连接器提交和评估说明。

插件在连接到权威数据源时效果最佳。如果你构建或运营法律数据源、法律研究工具、合同管理系统（CLM）、文档管理系统（DMS）、电子取证平台或法律实务管理系统，我们欢迎你的 MCP 连接器加入本套件。

## 优秀的法律 MCP 连接器标准

- **通过 HTTPS 的远程 MCP 服务器**，支持 OAuth 或 API Key 认证（streamable HTTP 或 SSE 传输）
- **以读取为主的工具** — 搜索、获取、列表。写入工具（创建、发送、归档）需要在客户端侧设置明确的确认提示；请在工具描述中说明。
- **结果包含出处信息** — 返回来源、检索日期和可用于引用的标识符。插件按来源标注每条引用；你的连接器应当使之成为可能。
- **结果中不含指令性内容** — 插件将检索内容视为数据而非指令。如果你的工具结果包含元数据或系统备注，请清晰标记以免看起来像嵌入的指令。
- **速率限制和错误应优雅降级** — 插件有连接器无响应时的降级方案；干净的错误信息优于超时。

## 如何提交

1. 发布你的 MCP 服务器并记录其工具、认证流程和数据覆盖范围。
2. 提交 PR，将你的服务器添加到相关插件的 `.mcp.json` 中，包含 URL、认证方式和一句话描述。
3. 说明最适用于哪些法律实务领域/插件。
4. 我们会针对插件工作流进行测试后合并。通过检索质量和注入防护检查的连接器会进入默认 `.mcp.json`；其他连接器将在插件 README 中记录，供用户自行添加。

## 当前连接器

各插件默认 `.mcp.json` 中配置的连接器：

| 连接器 | 适用插件 | 说明 |
|---|---|---|
| **企业微信 / 钉钉 / 飞书** | 全部 12 个 | 企业通讯平台 |
| **WPS / 金山文档** | 全部 12 个 | 文档协作平台 |
| **北大法宝** | legal-clinic, ip-legal, litigation-legal, law-student | 法律法规/案例检索 |
| **威科先行** | 全部法律实务插件 | 综合法律信息平台 |
| **Alpha 法律智能操作系统** | litigation-legal, commercial-legal | 案例检索/合同审查 |
| **法信** | litigation-legal, legal-clinic | 裁判规则/法律观点 |
| **中国裁判文书网** | litigation-legal, legal-clinic, law-student | 裁判文书公开检索 |
| **法大大** | commercial-legal | 电子签名/合同管理 |
| **上上签 / e签宝** | commercial-legal | 电子签名 |
| **iManage** | commercial-legal, corporate-legal | 文档管理系统 |
| **Jira / 飞书项目** | product-legal | 项目追踪 |

详见各插件目录中的 `.mcp.json` 获取权威列表。

## 期望添加的连接器

以下连接器将显著增强特定插件的功能。如果你构建或运营其中之一，请参见上方"如何提交"。

- **中国知识产权管理系统**（国知局专利检索/商标检索、合享智慧 Incopat、智慧芽 PatSnap）— `ip-legal` 专利/商标组合管理的完整对接
- **国家知识产权局商标检索** — 商标状态和期限追踪，用于 `ip-legal` 品牌管理
- **中国法院公开网 / 审判流程信息公开网** — 案件进度追踪，用于 `litigation-legal`
- **企查查 / 天眼查 / 启信宝** — 企业信息查询，用于 `corporate-legal` 尽职调查
- **国家企业信用信息公示系统** — 工商信息/行政处罚/经营异常查询
- **信用中国** — 信用信息/行政处罚/黑名单查询
- **中国政府网 / 国务院公报** — 法规政策动态，用于 `regulatory-legal`
- **各部委官方网站 RSS** — 市场监管总局/网信办/工信部/银保监/证监会等监管动态
- **中国人大网** — 立法动态/征求意见稿追踪
- **全球 AI 监管追踪器** — 多法域 AI 法规追踪，用于 `ai-governance-legal` 和 `regulatory-legal`

## 问题反馈

在本仓库提交 issue。合作或集成相关问题，请参见各插件 README 中的联系方式。
