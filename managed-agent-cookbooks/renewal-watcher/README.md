# Renewal Watcher - 中国合同续约/终止提醒托管代理模板

## 定位

本模板用于扫描合同管理系统、电子签约平台、WPS/金山文档或企业网盘中的合同元数据，识别自动续约、提前通知、到期终止、价格调整、保证金返还和履约节点，并生成提醒报告。

它是 cookbook，不是成品合同管理系统。部署方需要接入自己的 CLM、电子签约或文档系统，并配置业务线提醒规则。

## 推荐连接器

```bash
export CN_CLM_MCP_URL=...
export CN_ESIGN_MCP_URL=...
export WPS_CLOUD_DOCS_MCP_URL=...
../../scripts/deploy-managed-agent.sh renewal-watcher
```

可接入系统包括法大大、上上签、e签宝、企业 CLM、WPS/金山文档、企业网盘或内部合同台账。

## 安全分层

| 层级 | 是否读取合同元数据/条款 | 权限 | 说明 |
|---|---|---|---|
| `repo-reader` | 是 | 只读 | 读取合同元数据和关键条款 |
| `deadline-calculator` | 否 | 本地计算 | 计算提醒窗口和风险级别 |
| `alert-writer` | 否 | 写入 | 输出提醒报告 |

合同元数据和条款都按不可信输入处理。代理不得直接修改合同、不得发送通知、不得替代法务判断。

## 输出

- `./out/renewal-alerts-<YYYY-MM-DD>.md`
- 可选 `handoff_request`：由外部编排层转发到飞书、钉钉、企业微信、邮件或 CLM 任务中心

## 中国法注意事项

- 自动续约、提前通知和解除权应结合《民法典》合同编、具体合同约定和行业监管要求审查。
- 供应商、经销、平台、电商和消费者合同可能叠加格式条款、显著提示和公平交易要求。
- 涉及个人信息、数据处理、电子签章或跨境履约时，应联动 privacy-legal、ai-governance-legal 或 commercial-legal 模块复核。
