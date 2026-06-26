# Claude for Legal (中国法企业法务定制版)
> ?????????[PROJECT_USAGE_GUIDE.md](PROJECT_USAGE_GUIDE.md)


本项目是基于 Anthropic `claude-for-legal` 原型进行深度本地化改造的开源项目。针对中国大陆法系（成文法）特点及国内企业合规、法务核心工作流进行了底层架构与 Prompt 的全量重雕，旨在打造开箱即用的“AI 法律协同副驾驶（Copilot）”。

> ⚠️ **专业免责声明**
> 本项目定位为法律协同工具。大模型生成的所有分析意见、合同审查结论、法律文书初稿，**必须经由具备中华人民共和国执业资格的律师或企业内部专业法务进行复核**，系统输出不得直接作为企业最终决策或法庭辩论依据。

---

## 📌 项目定位与主场景优先级

本项目核心服务于以下场景，研发与 Prompt 调优资源按此优先级倾斜：

1. **企业内控法务（In-house Legal）** —— 高频、流程化、强合规控制（默认主场景）
2. **律所执业律师（Law Firm）** —— 个性化对抗、检索增强与文书辅助
3. **法律教育与援助（Phase 2）** —— 学术与公益性长尾场景（已移入 `phase-2/` 目录挂载）

---

## 📦 核心插件矩阵 (第一阶段正式模块)

默认 Marketplace 仅加载以下 9 个完全适配中国大陆法律环境的商业法律插件：

- `commercial-legal`: 境内商业合同审查与法律风险识别
- `privacy-legal`: 个人信息保护法（PIPL）合规与数据安全审查
- `corporate-legal`: 公司治理、股权质押、股东出资加速到期等合规审查
- `employment-legal`: 劳动合同法法定解除、N/N+1/2N 补偿计算及员工手册审计（当前重点深改）
- `product-legal`: 境内产品上市合规、消费者权益保护审查
- `regulatory-legal`: 行政监管应对、行业准入与合规检查
- `ai-governance-legal`: 国内生成式人工智能服务管理暂行办法及合规备案协同
- `ip-legal`: 著作权、商标局/专利局流转程序与平台维权投诉（通知-删除）
- `litigation-legal`: 境内民商事诉讼/仲裁管辖、举证期限及财产保全协同

---

## 🚀 快速开始 (Quickstart)

### 1. 配置环境与 Marketplace

在你的 MCP 客户端（如 Claude Desktop、Cursor 等）中配置项目路径，并激活默认的插件 Marketplace 配置文件。

### 2. 注入中国默认连接器 (MCP)

项目在 `.mcp.json` 中预留了国内标准法律科技与办公生态的占位接口。请在本地环境中配置相应的环境变量或标准 API 桥接器：

- `npc-law-database`: 国家法律法规数据库 / 中国人大网流式检索
- `gov-regulatory-sites`: 国务院及各部委、地方监管官网动态合规检查
- `wps-cloud-docs`: 金山文档 / WPS WebOffice 云端文件同步

注：若未配置云端 MCP 连接器，系统默认激活 **Local File Mode**，你可直接向 Claude 拖入本地 `.docx`、`.xlsx`、`.pdf` 用工材料，Claude 将利用 Context Window 进行结构化解析。

### 3. 一键初始化首测

在客户端中直接输入以下命令，触发劳动用工模块的冷启动访谈，验证底座是否正常：

```bash
/employment-legal:cold-start-interview
```

---

## 🗺️ 路线图 (Roadmap)

以下模块由于两域差异或生态进阶定位，已移入 `phase-2/` 目录，将在第二阶段进行中国化适配：

- `law-student` / `legal-clinic` (法律诊所与法学生学术协同)
- `legal-builder-hub` (法律 MCP 工具链构建中心)

