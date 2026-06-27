# 中国法律连接器建议

本项目不内置第三方账号或真实 MCP 地址。落地时应由部署方把以下系统接入为 MCP，并在插件 `.mcp.json` 或本地 MCP 配置中替换对应服务器。

| 类别 | 推荐连接器 | 适用插件 |
|---|---|---|
| 法律法规 | 国家法律法规数据库、中国人大网、国务院政策文件库 | 全部 |
| 案例/裁判 | 中国裁判文书网、人民法院案例库、最高人民法院法答网精选系列、法信、北大法宝、威科先行、Alpha | litigation, ip, corporate, legal-clinic, law-student |
| 监管动态 | 网信办、市场监管总局、人社部、工信部、司法部、证监/金融监管系统、地方主管机关 | regulatory, product, privacy, ai-governance, employment |
| 合同/文档 | WPS/金山文档、飞书文档、企业微信文档、钉钉文档、iManage/本地 DMS | commercial, corporate, litigation |
| 合同管理 | 法大大、上上签、e签宝、契约锁、企业自建 CLM | commercial, corporate |
| 企业信息 | 国家企业信用信息公示系统、信用中国、企查查、天眼查、启信宝 | corporate, commercial, litigation |
| 项目协作 | 飞书项目、Jira、禅道、 TAPD、企业微信/钉钉/飞书消息 | product, ai-governance, regulatory |
| 知识产权 | CNIPA、商标局、版权登记系统、Incopat、PatSnap、合享智慧 | ip |

连接器设计要求：

- 读为主，写操作必须要求客户端显式确认。
- 返回来源、检索时间、文件/法条/案号标识。
- 不把检索结果中的文本当作系统指令。
- 对法规、案例、监管问答返回现行有效性或至少返回发布日期/施行日期。
- 对个人信息、商业秘密、案件材料提供权限边界和审计日志。

