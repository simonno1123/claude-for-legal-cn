# Claude for Legal CN
> 详细使用说明请参阅：[PROJECT_USAGE_GUIDE.md](PROJECT_USAGE_GUIDE.md)


本项目以 Anthropic `claude-for-legal` 为上游参考，建设面向中国执业律师、企业法务、法律诊所和法律学习者的 AI 辅助工具基础层。Phase 1 目标是完成中国法实体内容、12 个根模块、基线可运行性和文档真实性对齐；上游职责继续保持可追踪映射。

Phase 1 不重新排序业务价值，也不把状态化工作流或真实外部集成伪装成已完成能力。项目治理边界见 [docs/PROJECT_SCOPE.md](docs/PROJECT_SCOPE.md)，上游映射与阶段归属见 [docs/UPSTREAM_MAPPING_MATRIX.md](docs/UPSTREAM_MAPPING_MATRIX.md)。

> ⚠️ **专业免责声明**
> 本项目定位为法律协同工具。大模型生成的所有分析意见、合同审查结论、法律文书初稿，**必须经由具备中华人民共和国执业资格的律师或企业内部专业法务进行复核**，系统输出不得直接作为企业最终决策或法庭辩论依据。

---

## 📌 项目定位

本项目服务于上游 `claude-for-legal` 覆盖的法律工作场景，并以中国法语境映射对应职责。不同模块不因企业、律所、教育、公益或治理场景而被视为价值更低；Phase 1/1.5/2 仅表示工程交付边界，不构成模块价值排序。

- Phase 1：核心中国法能力、Local File Mode、根命令、CI、配置和文档基线。
- Phase 1.5：本地事项空间、tracker、history 和人工触发的工作流生命周期。
- Phase 2：真实 MCP Provider、外部系统自动监控、跨境专业包及技能安装/更新/回滚等高权限生态操作。

---

## 📦 当前插件矩阵

当前默认 Marketplace 加载以下中国法模块。该清单是当前工程状态，不替代上游完整映射验收：

- `commercial-legal`: 境内商业合同审查与法律风险识别
- `privacy-legal`: 个人信息保护法（PIPL）合规与数据安全审查
- `corporate-legal`: 公司治理、股权质押、股东出资加速到期等合规审查
- `employment-legal`: 劳动合同法法定解除、N/N+1/2N 补偿计算及员工手册审计
- `product-legal`: 境内产品上市合规、消费者权益保护审查
- `regulatory-legal`: 行政监管应对、行业准入与合规检查
- `ai-governance-legal`: 国内生成式人工智能服务管理暂行办法及合规备案协同
- `ip-legal`: 著作权、商标局/专利局流转程序与平台维权投诉（通知-删除）
- `litigation-legal`: 境内民商事诉讼/仲裁管辖、举证期限及财产保全协同
- `legal-builder-hub`: 中国法律技能 QA、静态来源审查、变更计划与 MCP 安全边界；物理安装、更新、回滚、禁用和卸载属于 Phase 2
- `law-student`: 提供中国法考备考、请求权基础训练、民商事案例研习与苏格拉底提问式辅导
- `legal-clinic`: 提供中国高校法律诊所、基层法律援助中心、12348公共法律服务时效台账与导师审查流

---

## 🚀 快速开始 (Quickstart)

### 1. 配置环境与 Marketplace

在你的 MCP 客户端（如 Claude Desktop、Cursor 等）中配置项目路径，并激活默认的插件 Marketplace 配置文件。

### 2. 配置中国连接器占位 (MCP)

项目在 `.mcp.json` 中配置统一中国法律数据层，并预留国内办公与企业法务系统接口。除本地样例 `legal-data` server 外，其他接口均需要部署方自行实现和授权：

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

Phase 1：冻结中国法实体内容、12 个根模块、基线运行时和治理文档。

Phase 1.5：建设本地、人工触发的事项空间、tracker 和生命周期。

Phase 2：接入真实 MCP Provider、商业法律数据库、OCR、工商/执行信息、跨境专业包、外部自动监控和技能生态执行能力。

当前 `law-student` 与 `legal-clinic` 已完成第一阶段改造并移动至根目录，完全实现了顶级模块的 Parity 发现性与有状态职责恢复。
