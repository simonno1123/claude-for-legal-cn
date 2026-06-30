# 连接器与 MCP 接入策略

本项目不要求每个业务插件各自直连具体供应商。所有中国法插件应优先通过统一的 **Legal Data MCP Layer** 获取法律法规、法条、案例和引用核验能力。

## 一、统一 Legal Data MCP Layer

业务插件只调用统一能力，不绑定具体数据源：

| 能力 | 用途 |
|---|---|
| `law_search` | 检索法律、行政法规、部门规章、地方性法规、监管规则 |
| `article_lookup` | 按法规名称、条号、发布日期或时效状态定位法条 |
| `regulation_detail` | 获取法规全文、效力级别、发布机关、施行日期、时效状态 |
| `case_search` | 检索指导性案例、参考案例、公报案例、典型案例、普通裁判文书 |
| `case_detail` | 获取案号、法院、裁判日期、裁判要旨、争议焦点、来源链接 |
| `case_authority_rank` | 按中国法权威层级标注案例参考强度 |
| `citation_check` | 校验法条、法规、案号和引用文本是否存在、是否过期、是否误引 |

底层数据源由 provider router 决定，可以是官方本地索引、商业 API/MCP、企业授权数据库或人工上传材料。

## 二、数据源分层

### 1. 官方免费源

| 数据源 | 适用范围 | 推荐接入方式 |
|---|---|---|
| 国家法律法规数据库 / 中国人大网 | 法律、行政法规、地方性法规、司法解释入口 | 定期采集、本地索引、人工下载上传 |
| 国务院、部委、地方监管官网 | 监管政策、部门规章、地方口径 | 定期采集、本地索引、低频浏览器辅助 |
| 人民法院案例库 | 指导性案例、参考案例 | 本地索引、人工上传、可用 API 时接入 |
| 最高人民法院 | 指导性案例、公报案例、典型案例、司法政策 | 定期采集、本地索引 |
| 中国裁判文书网 | 普通裁判文书、趋势样本 | 本地索引、人工上传、低频检索 |

官方源免费且权威，但通常没有稳定 API，不适合高频实时调用。默认策略是“采集/下载/上传 → 清洗去重 → local-index → MCP 查询”。

### 2. 商业付费源

| 数据源 | 适用范围 | 接入定位 |
|---|---|---|
| 元典开放平台 | 法规、案例、企业风险、引用核验、幻觉检测 | 推荐 MCP/API provider |
| 北大法宝 OpenAPI/MCP | 法规、法条、案例、引用法规、专业检索 | 推荐商业法律数据库 provider |
| 法律之星接口 | 法规检索、时效状态、发布机关、逻辑关键词组合 | 推荐法规 API 候选源 |
| 威科先行 | 综合法律数据库、实务文章、案例法规 | 企业授权后接入 |
| 法信 | 裁判规则、法律观点、案例 | 企业授权后接入 |
| Alpha、企查查、天眼查、启信宝 | 企业画像、诉讼执行、行政处罚、股权工商 | 放入 enterprise-data 层，不进入 legal-data 默认层 |

商业源限制较少、检索效率高，但受授权范围和费用影响。任何商业源都不得成为唯一强依赖。

### 3. 本地与人工源

| 来源 | 用途 |
|---|---|
| `local-legal-index` | 官方网站、企业授权数据库导出、历史检索结果的本地索引 |
| `manual-upload` | 用户上传法规 PDF、案例、检索报告、裁判文书、法律意见摘录 |
| `review-packet` | 供模型交叉审查和人工专家复核的模块审查包 |

## 三、推荐 MCP 配置形态

项目已收敛为一个全局法律数据入口。仓库内置 `connectors/legal-data/server.js` 作为最小本地 MCP server；生产环境可在同一接口后接企业授权商业库、官方本地索引或人工上传材料：

```json
{
  "mcpServers": {
    "legal-data": {
      "command": "node",
      "args": ["connectors/legal-data/server.js"],
      "env": {
        "LEGAL_DATA_PROVIDER": "${LEGAL_DATA_PROVIDER:auto}",
        "YUANDIAN_API_KEY": "${YUANDIAN_API_KEY}",
        "PKULAW_API_KEY": "${PKULAW_API_KEY}",
        "LAW_STAR_API_KEY": "${LAW_STAR_API_KEY}",
        "LOCAL_LEGAL_INDEX": "${LOCAL_LEGAL_INDEX:./data/legal-index}"
      },
      "title": "统一中国法律数据层",
      "description": "统一提供法律法规、法条、案例、引用核验和案例权威排序能力。"
    }
  }
}
```

各业务插件不得再分别硬编码 `npc-law-database`、`court-case-local-index`、`pkulaw-openapi`、`yuandian-legal-data` 等供应商名称；这些应作为 `legal-data` 内部 provider。当前最小 server 只执行本地 JSON 索引查询，不联网调用商业源。

## 四、案例权威层连接器

案例体系保留为全局基础设施，不作为独立业务插件。

| Connector | Source | Purpose |
|---|---|---|
| `people-court-case-library` | 人民法院案例库 | 指导性案例、参考案例 |
| `supreme-peoples-court` | 最高人民法院 | 指导性案例、公报案例、典型案例、司法政策 |
| `china-judgments-online` | 中国裁判文书网 | 普通裁判文书、趋势样本、类案研究 |
| `commercial-legal-database` | 北大法宝 / 威科先行 / 法信 / 元典 | 企业自有授权的法规案例检索 |
| `manual-case-upload` | 用户上传材料 | 律师检索报告、PDF 案例、内部案例库 |

返回结果必须包含：案例类型、案号、法院或发布机关、发布日期或裁判日期、检索日期、来源 URL、权威等级、时效/更新标签。

## 五、输出要求

任何插件引用外部法律数据时，必须标注：

- 来源类型：官方、商业、本地索引、人工上传；
- 检索日期；
- 法规时效性；
- 案例权威等级；
- 是否需要人工复核；
- 如为商业源，标注“基于企业授权范围返回”。

## 六、后续扩展

`enterprise-data` 与 `workflow-docs` 可在后续阶段独立成层：

- `enterprise-data`：企业工商、股权、年报、行政处罚、执行/失信、知识产权；
- `workflow-docs`：WPS/金山文档、CLM、电子签约、飞书、钉钉、企业微信。

当前优先级只聚焦 `legal-data`：法律法规与案例。
