# Claude for Legal CN 项目使用指南

本指南面向企业法务、律师、合规团队、法律科技团队、法律诊所和法律学习者，说明如何使用 `claude-for-legal-cn` 的中国法本土化插件体系。

> 重要提示：本项目是法律协同工具，不是执业律师替代品。所有输出均为法律分析初稿、审查辅助、文书草稿或学习材料。涉及签署、盖章、提交、起诉、仲裁、备案、解雇、付款、和解、撤诉、权利处分等后果性动作前，必须由执业律师或企业专业法务复核。

## 1. 项目定位

`claude-for-legal-cn` 是面向中国大陆法律体系的 AI 法律协同插件集合。v1 治理目标是 Complete Chinese Port / Faithful Port，即对上游 `claude-for-legal` 的目录、插件、技能、代理、工作流和文档概念建立一一对应的中国法实现。

当前仓库已经包含多个中国法模块、案例规则层、MCP 占位配置和本地最小 legal-data server。它们应按 Faithful Port 标准逐项验收，而不是按企业法务、律所、教育、公益或治理场景做价值排序。

项目范围以 [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md) 为准；上游映射以 [docs/UPSTREAM_MAPPING_MATRIX.md](docs/UPSTREAM_MAPPING_MATRIX.md) 为基线。

默认法域是中华人民共和国大陆地区。涉港澳台、境外法、跨境数据、外商投资负面清单、涉外管辖等问题，应切换为提示模式，并结合对应法域律师意见。

## 2. 模块总览

### 当前默认 Marketplace 模块

| 模块 | 适用场景 | 常用入口 |
|---|---|---|
| `employment-legal` | 劳动用工、解除、补偿、员工手册、工时休假、社保公积金 | `/employment-legal:cold-start-interview` |
| `corporate-legal` | 公司治理、新公司法、出资、股权转让、章程审查、实体合规 | `/corporate-legal:cold-start-interview` |
| `commercial-legal` | 商事合同、采购销售、SaaS、NDA、续约、授权用印 | `/commercial-legal:review` |
| `litigation-legal` | 民商事诉讼/仲裁、保全、举证期限、庭审质证、执行 | `/litigation-legal:matter-intake` |
| `product-legal` | 产品上线、广告营销、消费者权益、电商平台、质量召回 | `/product-legal:launch-review` |
| `privacy-legal` | 个人信息保护、PIPIA、数据出境、委托处理、个人权利请求 | `/privacy-legal:use-case-triage` |
| `ip-legal` | 商标、专利、著作权、平台维权、开源合规、商业秘密 | `/ip-legal:clearance` |
| `ai-governance-legal` | 生成式 AI、算法推荐、深度合成、AI 备案、安全评估 | `/ai-governance-legal:use-case-triage` |
| `regulatory-legal` | 监管动态、政策差异、征求意见稿、整改台账、制度修订 | `/regulatory-legal:reg-feed-watcher` |
| `legal-builder-hub` | 法律技能生态治理、社区技能审查、安装/禁用/卸载、更新差异审查、MCP 安全边界 | `/legal-builder-hub:skills-qa` |

### 教学与公益服务模块

| 模块 | 适用场景 | 常用入口 |
|---|---|---|
| `legal-clinic` | 法律诊所、法律援助、12348、公服咨询、导师复核 | `/legal-clinic:client-intake` |
| `law-student` | 中国法学习、法考、请求权基础、案例研读、主观题训练 | `/law-student:study-plan` |

`corporate-legal` 的并购尽调、交割清单、重大合同附表和投后整合属于 corporate Faithful Port v1 职责，命令通过根级 `/corporate-legal:*` 暴露。部分实质实现因历史原因仍存放在 `corporate-legal/phase-2/skills/`，但该路径不代表能力降权，也不代表 v1 可以跳过这些职责。

`legal-clinic` 和 `law-student` 已按 Faithful Port v1 恢复根目录 parity，并通过根级 `/legal-clinic:*`、`/law-student:*` 命令暴露。历史 `phase-2` 路径不代表能力降权，也不再作为这两个模块的默认入口。

## 3. 推荐安装方式

### 3.1 添加插件市场

在 Claude Code 或支持插件市场的 MCP 客户端中添加本仓库路径：

```text
/plugin marketplace add <你的本地仓库路径>/claude-for-legal-cn
```

如果使用其他路径，请替换为你的本地仓库路径。

### 3.2 安装具体模块

示例：

```text
/plugin install employment-legal@claude-for-legal-cn
/plugin install corporate-legal@claude-for-legal-cn
/plugin install commercial-legal@claude-for-legal-cn
```

安装后重启客户端，再运行对应模块的 `cold-start-interview`。

## 4. 第一次使用流程

建议按下面顺序：

1. 选择模块。
2. 运行该模块的冷启动访谈。
3. 配置或确认连接器。
4. 上传或指定本地文件。
5. 运行具体技能。
6. 人工复核输出。
7. 将后续动作放入审批、交割、整改或复核队列。

示例：

```text
/employment-legal:cold-start-interview
/employment-legal:termination-review
```

```text
/corporate-legal:cold-start-interview
/corporate-legal:articles-of-association-audit
```

```text
/commercial-legal:review
```

## 5. 文件输入方式

项目支持两种工作方式：

### Local File Mode

未配置云端连接器时，直接向模型提供本地文件，例如：

- `.docx`
- `.xlsx`
- `.pdf`
- 合同扫描件 OCR 文本
- 制度、章程、员工手册
- 裁判文书、监管函、审批记录

适合本地审查、小团队和内网环境。

### MCP Connector Mode

配置 MCP 后，可对接：

- 国家法律法规数据库 / 中国人大网
- 人民法院案例库
- 最高人民法院官网
- 中国裁判文书网
- 北大法宝 / 威科先行 / 法信 / Alpha
- WPS / 金山文档
- 企业微信 / 钉钉 / 飞书
- 企查查 / 天眼查 / 国家企业信用信息公示系统

真实 API Key 不应写入仓库，应使用环境变量。

## 6. 中国案例规则层

项目已加入可更新的案例规则层：

- `references/china-case-authority.md`
- `references/case-authority-sources.json`
- `references/case-authority-mcp.example.json`

### 使用原则

中国法不是普通法判例法体系。案例可以帮助判断，但不能替代法律、行政法规、司法解释和强制性规则。

案例分层：

| 层级 | 来源 | 用途 |
|---|---|---|
| A | 法律、行政法规、司法解释 | 直接规范依据 |
| B | 最高人民法院指导性案例 | 强参考层 |
| C | 人民法院案例库参考案例 | 类案参考层 |
| D | 公报案例、典型案例、监管案例 | 补充参考层 |
| E | 普通裁判文书 | 趋势和样本 |

### 何时必须做类案检查

以下场景建议触发案例检索：

- 诉讼、仲裁、执行、保全、举证责任、损害赔偿。
- 劳动解除、员工手册效力、社保公积金、竞业限制。
- 公司出资、股东责任、股权转让、并购争议。
- 违约金调整、格式条款、印章和法定代表人越权。
- 知识产权侵权、平台投诉、不正当竞争、商业秘密。
- 广告、产品、消费者权益、平台治理。
- 数据、AI、算法等新型合规问题。

输出应包含：

- 适用法条。
- 指导性案例/参考案例。
- 类案相似点。
- 类案差异点。
- 可引用程度。
- 更新状态。

## 7. 模块使用示例

### 7.1 劳动解除审查

```text
/employment-legal:termination-review
```

适合审查：

- 第39条严重违纪解除。
- 第40条不胜任或医疗期满解除。
- 第41条经济性裁员。
- 三期女职工、医疗期、工伤停工留薪期保护。
- 工会通知程序。
- 2N 违法解除风险。

### 7.2 新公司法章程审计

```text
/corporate-legal:articles-of-association-audit
```

适合审查：

- 股权转让旧法条款残留。
- 五年出资期限。
- 审计委员会/监事会路径。
- 职工董事。
- 法定代表人权限。
- 董监高忠实勤勉义务和影子董事责任。

### 7.3 合同审查

```text
/commercial-legal:review
```

适合审查：

- 合同效力。
- 违约责任。
- 格式条款。
- 盖章和授权。
- 发票税务。
- 电子签名。
- 争议解决。

### 7.4 产品上线审查

```text
/product-legal:launch-review
```

适合审查：

- 消费者权益。
- 广告宣传。
- 自动续费。
- 七日无理由退货。
- 电商平台规则。
- 质量安全和召回。
- 未成年人保护。
- 个人信息和算法触点。

### 7.5 并购尽调

```text
/corporate-legal:diligence-issue-extraction
```

适合审查：

- 股权权属和出资。
- 国资、外资、经营者集中。
- 重大合同控制权变更。
- 许可证不可转让。
- 劳动社保。
- 税务和行政处罚。
- 数据和系统交割。

## 8. 输出如何复核

每份输出建议按以下清单复核：

| 项目 | 检查问题 |
|---|---|
| 法域 | 是否默认中国大陆？是否涉及港澳台或境外法？ |
| 法条 | 是否给出具体法律名称和条文？ |
| 案例 | 是否区分指导性案例、参考案例和普通裁判文书？ |
| 事实 | 是否基于用户提供材料？是否有推测？ |
| 地方差异 | 是否需要地方规定或地方裁审口径？ |
| 后果动作 | 是否需要人工确认门？ |
| 证据 | 是否列出证据缺口和证明责任？ |
| 更新性 | 法规、案例和监管口径是否需要最新核验？ |

## 9. 安全和合规边界

不得做：

- 承诺案件结果。
- 承诺证据特权或英美法披露豁免。
- 伪造法条、案例、案号、监管文件。
- 自动发送律师函、投诉、起诉状、仲裁申请。
- 自动签署、盖章、备案、付款、和解或撤诉。
- 把真实 API Key、Token、密码写入仓库。

必须做：

- 标注来源和待核查项。
- 对重大法律后果设置人工确认门。
- 对个人信息、商业秘密和未公开交易信息做最小化处理。
- 对案例和监管动态保留更新接口。

## 10. 更新和维护

### 推荐更新周期

| 内容 | 周期 |
|---|---|
| 法律法规和司法解释 | 每月或重大修法时 |
| 人民法院案例库参考案例 | 活跃模块每周，非活跃模块每月 |
| 指导性案例 | 每月 |
| 监管问答和执法案例 | 每月 |
| 地方劳动、社保、公积金、假期口径 | 每季度或政策调整时 |
| AI、数据出境、平台治理规则 | 每月 |

### 更新步骤

1. 更新资料源或 MCP 连接器。
2. 运行相关模块回归测试。
3. 检查 JSON、frontmatter 和乱码。
4. 生成 AI/人工复核包。
5. 修正 Prompt。
6. 提交 Git 并推送。

## 11. 常见问题

### 未配置连接器能不能用？

可以。系统会进入 Local File Mode，但引用和案例检索能力会弱一些。高风险结论必须人工核验。

### 为什么不能直接输出最终法律意见？

因为模型无法承担执业责任，也不能保证资料完整、法规现行有效或案例最新。它适合做初稿、结构化审查和风险提示。

### 指导性案例是不是判例法？

不是。指导性案例和参考案例可用于类案参考和裁判规则校准，但不能替代成文法和司法解释，也不能作为普通法意义上的 binding precedent。

### `phase-2` 模块是否代表低优先级？

不是。`phase-2` 目前只是当前仓库的目录状态，不应理解为模块价值、验收标准或上游职责优先级较低。按照 v1 Faithful Port 原则，法律诊所、法学生、并购尽调和其他上游能力都应建立中国法对应实现；是否调整目录和 marketplace 暴露方式，应在后续结构映射阶段统一决定。

## 12. 推荐入口

企业法务初次使用：

```text
/employment-legal:cold-start-interview
/commercial-legal:review
/corporate-legal:cold-start-interview
```

诉讼律师初次使用：

```text
/litigation-legal:matter-intake
```

数据和 AI 合规初次使用：

```text
/privacy-legal:use-case-triage
/ai-governance-legal:use-case-triage
```

法律学习和诊所：

```text
/law-student:cold-start-interview
/legal-clinic:cold-start-interview
```
