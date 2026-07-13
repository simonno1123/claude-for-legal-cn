# TASK_017_PHASE1_SCOPE_RECLASSIFICATION — 审查报告
# 审查方：Gemini 3.5 Flash (Technical Reviewer)
# 审查依据：Codex RESULT（TASK_017_PHASE1_SCOPE_RECLASSIFICATION_RESULT.md）
# 审查时间：2026-07-13
# 审查模式：READ ONLY (基于工作区现状与移植标准对齐审查)

---

## 一、 审查结论与判定

基于对 Codex 在 `TASK_017` 中所提交之范围重分类事实结果（RESULT）的深度核对，结合 `FAITHFUL_PORT_STANDARD.md` 与当前 Release Candidate (RC) 准备阶段的实际要求，评估意见如下：

**判定结果：ACCEPTED_WITH_RECLASSIFICATION (接受重分类判定)**

### 核心裁定理由：
1. **定位调整的合规性**：
   `TASK_016` 暴露出的“职责悬挂”多为工作流系统或外部集成功能（如 Builder Hub 的物理安装回滚、Launch-Watcher 的外部办公系统自动读取、多客户端 Workspace 数据库隔离）。在 Phase 1 (Faithful Port v1 基线) 中，核心目标是**中国法实体法逻辑映射的对齐与防污染安全**，而非构建一整套复杂的 AI 协作平台操作系统（ACOS-Platform）。因此，将开发深度分为：
   - **Phase 1 (当前基础层)**：确保实体法内容 100% 对齐中国法、12 根模块Parity发现性、必需的 CI 自动化与 MCP 路径正确、所有声明与实际代码一致不产生欺骗性。
   - **Phase 1.5 (本地工作流层)**：实现本地 YAML 驱动的 matters 隔离生命周期和人工作业 trackers。
   - **Phase 2 (外部系统与生态集成层)**：引入物理 allowlist 下载安装、外部系统监控触发及真实 Provider。
   该分层不仅合理，而且是防止项目无限膨胀、确保 Phase 1 顺利冻结（Freeze）的唯一可行路径。
2. **声明真实性原则 (Declaration Honesty)**：
   Codex 指出，一旦部分上游职责后移至 Phase 1.5 或 Phase 2，则现有的 `README.md`、`PROJECT_SCOPE.md` 和各模块技能说明中“声称已完全实现”或“Phase 2 暂缓”的矛盾提法必须在 Phase 1 结项前完成修正。**不能在代码中仅是空壳占位，而在文档中宣称 100% 移植完毕。** 这一事实诊断极其精准，Gemini 完全予以采纳。

---

## 二、 重分类细目判定表 (Review Verdicts)

### 1. 必须在 Phase 1 修复的基线问题 (Phase 1 Mandatory)
这些问题直接阻塞 CI 合规通过或构成断链，必须由 ChatGPT 在 `TASK_018` 中下发修复：
*   **B-1a / B-1b / B-1c (CI 与 MCP 路径修复)**：
    - `scripts/localization-regression.py` 必须改造为支持 12 根模块，且**必须将 `.codex-coordination/` 目录排除在外国法文字扫描之外**（当前 CI 失败正是因为扫描了协调历史记录）。
    - `scripts/mcp-modules.json` 中的 `phase-2/` 路径必须修正为顶级路径，确保 MCP 配置文件生成器能顺利运行。
*   **G-3 (产品合规跨命令断链)**：
    - 修复 `seven-category-framework.md` 引用不存在命令 `/privacy-legal:pia-audit` 与 `/ai-governance-legal:cac-filing` 的问题，改用现有的 `pia-generation` 或 `use-case-triage` 命令。
*   **G-4a (WPS schema 内部自洽)**：
    - 在 `doc-reader.yaml` 中允许 `docs.wps.cn` 和 `kdocs.cn` 域名通过正则校验，使其与 wps-cloud-docs 声明保持自洽。
*   **G-5a / G-5b / G-5c / G-5d (文档与元数据状态同步)**：
    - 清理 `AGENTS.md`、`QUICKSTART.md`、`PHASE_2_ROADMAP.md`、`CHINA_LOCALIZATION_STATUS.md`、`PROJECT_USAGE_GUIDE.md` 中的所有 "10+2" 陈旧表述，统一描述为 12 根模块。
    - 将 `legal-builder-hub` 技能（如 installer）描述中的执行性动词收窄，明确第一阶段仅为“安全性静态 QA 与记录生成”，不执行物理安装，以保障声明真实性。
*   **G-1a / G-2a (Workspace 契约与 Agent Frontmatter)**：
    - 收窄 commercial 等模块 workspace 的命令行参数声明（argument hint），补齐 `commercial-legal` 等 4 个代理的合法 frontmatter 元数据，消除 validator 警告。

### 2. 延后至 Phase 1.5 开发的本地工作流 (Phase 1.5 Backlog)
这些能力对当前单会话合规审查非必需，但在本地团队协作中必要，列入 Phase 1.5 待办：
*   **本地 Matters 隔离生命周期**：在商业、隐私、用工、产品、IP 等模块中建立通用的、基于本地 YAML 的 `new/list/switch/close/none` 隔离契约，支持 private-practice 模式。
*   **产品上线本地 Tracker & 监测记录**：支持以本地 YAML 形式手工维护 product launch tracker。

### 3. 延后至 Phase 2 开发的生态与连接器 (Phase 2 Backlog)
这些能力需要外部 API 鉴权、物理安全边界设计或跨境专业数据库，列入 Phase 2 待办：
*   **`employment-legal` 跨境用工实质能力**：涉外 EOR 选型、目标法域当地用工及税务法规库。
*   **`legal-builder-hub` 物理文件操作**：物理拉取 allowlist、自动执行文件下载/覆盖、disable/uninstall 目录操作、自动应用更新并创建备份回滚点。
*   **产品合规自动监控**：对接飞书/钉钉/Jira 等外部系统的监控 agent。
*   **真实云端连接器集成**：真实的威科先行、北大法宝、WPS 开放平台 API 对接与端到端鉴权。

---

## 三、 对 ChatGPT 的下一步任务生成指导

ChatGPT 应据此 Review 结论，在 `inbox/` 目录中下发：
**`TASK_018_PHASE1_ALIGNMENT_EDIT`**

**任务书约束**：
- **允许修改**：仅允许修改上述 **Phase 1 Mandatory** 列表中的脚本、生成器 json、broken command references、WPS 正则允许域名、agent frontmatter、文档路径以及 marketplace.json / plugin.json 描述。
- **禁止修改**：禁止为 workspace 开发持久化逻辑，禁止为 Builder Hub 开发物理文件写操作，禁止引入任何实质性跨境劳动法律库。
