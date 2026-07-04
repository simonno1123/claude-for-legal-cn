# Claude for Legal CN
> 详细使用说明请参阅：[PROJECT_USAGE_GUIDE.md](PROJECT_USAGE_GUIDE.md)


本项目是 Anthropic `claude-for-legal` 的中国法完整移植版本，v1 目标是 **Complete Chinese Port / Faithful Port**：尽量保持上游目录、插件、技能、代理、工作流和文档概念的可比结构，并将其中的法律内容、资料源、引用规则和人工复核门替换为中华人民共和国大陆地区法律体系下的对应实现。

v1 的目标不是重新排序业务优先级，也不是新增专业化产品层。项目治理边界见 [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md)，上游映射基线见 [docs/UPSTREAM_MAPPING_MATRIX.md](docs/UPSTREAM_MAPPING_MATRIX.md)。

> ⚠️ **专业免责声明**
> 本项目定位为法律协同工具。大模型生成的所有分析意见、合同审查结论、法律文书初稿，**必须经由具备中华人民共和国执业资格的律师或企业内部专业法务进行复核**，系统输出不得直接作为企业最终决策或法庭辩论依据。

---

## 📌 项目定位

本项目服务于上游 `claude-for-legal` 覆盖的法律工作场景，并以中国法语境实现对应职责。不同模块不因企业、律所、教育、公益或治理场景而在 v1 中被视为价值更低；当前目录状态只反映移植过程中的工程状态，不构成长期产品分级。

- 企业法务、律所律师、监管合规、诉讼仲裁、知识产权、产品、隐私与 AI 治理等场景应按上游职责逐项完成中国法映射。
- 法学生、法律诊所、法律援助和技能生态治理模块也应按 Faithful Port 标准验收。
- 后续商业数据库、OCR、工商/执行信息、专业 Practice Pack 和工作流自动化属于 v2+ 扩展，不属于 v1 完整移植完成条件。

---

## 📦 当前插件矩阵

当前默认 Marketplace 加载以下中国法模块。该清单是当前工程状态，不替代上游完整映射验收：

- `commercial-legal`: 境内商业合同审查与法律风险识别
- `privacy-legal`: 个人信息保护法（PIPL）合规与数据安全审查
- `corporate-legal`: 公司治理、股权质押、股东出资加速到期等合规审查
- `employment-legal`: 劳动合同法法定解除、N/N+1/2N 补偿计算及员工手册审计（当前重点深改）
- `product-legal`: 境内产品上市合规、消费者权益保护审查
- `regulatory-legal`: 行政监管应对、行业准入与合规检查
- `ai-governance-legal`: 国内生成式人工智能服务管理暂行办法及合规备案协同
- `ip-legal`: 著作权、商标局/专利局流转程序与平台维权投诉（通知-删除）
- `litigation-legal`: 境内民商事诉讼/仲裁管辖、举证期限及财产保全协同
- `legal-builder-hub`: 中国法律技能生态治理、社区技能 QA、安装审查、禁用/卸载、更新差异审查与 MCP 安全边界

---

## 🚀 快速开始 (Quickstart)

### 1. 配置环境与 Marketplace

在你的 MCP 客户端（如 Claude Desktop、Cursor 等）中配置项目路径，并激活默认的插件 Marketplace 配置文件。

### 2. 注入中国默认连接器 (MCP)

项目在 `.mcp.json` 中接入统一中国法律数据层，并预留国内办公与企业法务系统接口。请在本地环境中配置相应的环境变量或标准 API 桥接器：

- `legal-data`: 已提供 `connectors/legal-data/server.js` 最小本地 MCP server，默认读取 `LOCAL_LEGAL_INDEX` 本地 JSON 索引；未配置时仅使用样例索引做离线冒烟测试。
- `npc-law-database`: 国家法律法规数据库 / 中国人大网流式检索入口，现已收敛到 `legal-data` 统一层。
- `gov-regulatory-sites`: 国务院及各部委、地方监管官网动态合规检查
- `wps-cloud-docs`: 金山文档 / WPS WebOffice 云端文件同步

其他企业系统连接器仍为占位，包括 CLM、电子签章、法院/仲裁案件进度、项目管理和协同系统。它们用于部署方按自身授权环境桥接，不表示仓库已经内置商业 API 或真实凭证。

注：若未配置云端 MCP 连接器，系统默认激活 **Local File Mode**，你可直接向 Claude 拖入本地 `.docx`、`.xlsx`、`.pdf` 用工材料，Claude 将利用 Context Window 进行结构化解析。

### 3. 一键初始化首测

在客户端中直接输入以下命令，触发劳动用工模块的冷启动访谈，验证底座是否正常：

```bash
/employment-legal:cold-start-interview
```

---

## 🗺️ 路线图 (Roadmap)

v1：Complete Chinese Port / Faithful Port。目标是完成上游 `claude-for-legal` 能力在中国法体系下的一一对应实现，并保持后续上游 diff 可审查。

v2+：在 v1 基线稳定后，再接入 MCP Provider、商业法律数据库、OCR、工商/执行信息、专业 Practice Pack、工作流自动化和公共能力层。

当前 `law-student` / `legal-clinic` 仍位于 `phase-2/` 目录，这只是当前目录状态，不代表模块价值低于其他上游模块；是否恢复根目录 parity 需在 Faithful Port 映射审核中决定。
