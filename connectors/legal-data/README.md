# Legal Data Connector

`legal-data` 是本项目的统一中国法律数据 MCP 入口。它不是单一供应商连接器，而是一个 provider router，用来把业务插件的法律数据请求路由到官方本地索引、商业 API/MCP 或人工上传材料。

## 统一能力

| Tool | 说明 |
|---|---|
| `law_search` | 检索法律法规、规章、地方性法规、监管规则 |
| `article_lookup` | 按法规名称和条号定位法条 |
| `regulation_detail` | 获取法规全文、效力级别、发布机关、施行日期和时效状态 |
| `case_search` | 检索指导性案例、参考案例、公报案例、典型案例、最高人民法院法答网精选系列和普通裁判文书 |
| `case_detail` | 获取案号、法院、裁判日期、争议焦点、裁判要旨、法答网问答元数据和来源链接 |
| `case_authority_rank` | 按中国法权威层级排序案例和司法问答参考 |
| `judicial_answer_search` | 检索最高人民法院法答网精选系列问答 |
| `judicial_answer_detail` | 获取法答网精选问答标题、发布日期、来源链接和问答内容摘要 |
| `citation_check` | 校验法条、法规、案号、引用文本和时效状态 |

## Provider 优先级

默认路由建议：

1. 企业已授权商业 API/MCP：元典、北大法宝、法律之星、威科先行、法信；
2. 本地官方索引：国家法律法规数据库、最高法、最高人民法院法答网精选系列、人民法院案例库、裁判文书网；
3. 人工上传材料：法规 PDF、案例、律师检索报告、商业数据库导出；
4. 无可用来源时，返回“需要人工检索/上传”的明确提示。

当前仓库提供一个**最小可运行本地 MCP server**：`server.js`。它不联网、不保存 API Key、不调用商业数据库，只读取 `LOCAL_LEGAL_INDEX` 指向的本地 JSON 索引；未配置时加载 `local-index.sample.json` 作为 smoke test 和离线演示数据。

## 重要边界

- 不保存真实 API Key。
- 不把商业源结果伪装成官方源。
- 不把内置样例索引当作真实法律数据库；样例条文均为摘要，依赖前必须替换为官方或企业授权索引。
- 不把普通裁判文书表述为中国法上的判例约束。
- 法答网精选系列属于最高法司法问答和裁判口径参考，不得替代法律、司法解释、指导性案例或正式裁判文书。
- 输出必须包含来源、检索日期、时效状态和复核提示。
- 政府网站默认不高频实时抓取，优先走采集入库或人工上传。

## 本地索引格式

`LOCAL_LEGAL_INDEX` 可以指向一个 JSON 文件，也可以指向包含 `index.json` 或 `local-index.json` 的目录。索引顶层结构：

```json
{
  "version": "0.1.0",
  "generated_at": "2026-06-30",
  "regulations": [],
  "cases": [],
  "judicial_answers": []
}
```

每条法规至少应包含：

- `id`
- `title`
- `aliases`
- `authority_level`
- `issuing_authority`
- `effective_date`
- `status`
- `source_type`
- `source_name`
- `source_url`
- `retrieved_at`
- `articles[]`，其中每条含 `article_no`、`heading`、`text`

案例和法答网问答需包含 `authority_rank`，取值建议：

| Rank | 含义 |
|---|---|
| `guiding_case` | 指导性案例 |
| `reference_case` | 人民法院案例库参考案例 |
| `gazette_case` | 最高人民法院公报案例 |
| `typical_case` | 典型案例/监管案例 |
| `judicial_answer` | 最高人民法院法答网精选问答 |
| `ordinary_judgment` | 普通裁判文书 |

## 运行与测试

```bash
node connectors/legal-data/server.js --self-test
bash scripts/test-legal-data.sh
```

MCP 客户端通过各模块 `.mcp.json` 中的 stdio 配置启动：

```json
{
  "type": "stdio",
  "command": "node",
  "args": ["connectors/legal-data/server.js"]
}
```

可选环境变量：

| 环境变量 | 用途 |
|---|---|
| `LOCAL_LEGAL_INDEX` | 本地法规/案例/法答网索引 JSON 文件或目录 |
| `LEGAL_DATA_PROVIDER` | 预留 provider router 策略；当前最小 server 仅执行本地索引 |
| `YUANDIAN_API_KEY` / `PKULAW_API_KEY` / `LAW_STAR_API_KEY` | 预留商业 provider 凭证；当前最小 server 不读取、不外发 |

## 状态

当前目录已提供最小可运行本地 MCP server、样例索引和 smoke test。商业 provider router、官网采集、本地索引构建器和企业授权数据库适配器仍由部署方按授权环境扩展。
