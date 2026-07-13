# TASK_016_PHASE1_FINAL_AUDIT — 审查报告
# 审查方：Gemini 3.5 Flash (Technical Reviewer)
# 审查依据：Codex RESULT（TASK_016_PHASE1_FINAL_AUDIT_RESULT.md）
# 审查时间：2026-07-13
# 审查模式：READ ONLY (基于文件系统与运行期交叉核验)

---

## 一、 审查结论与判定

基于对 Codex 审计报告事实部分的深度核对及在本地工作目录下的交叉验证，得出以下评审结论：

**判定结果：REJECTED (ACTION REQUIRED)**

### 核心拒绝原因：
1. **自动化 CI 回归测试失效与生成器阻断 (P0 - Blocker)**：
   - 物理提升 `law-student` 和 `legal-clinic` 后，现有的回归检查脚本 `scripts/localization-regression.py` 仍持有旧有的 `phase-2/` 路径期望，且未将 `.codex-coordination/` 下的历史负向约束提及过滤，导致 CI 脚本在 HEAD 状态下运行直接退出 `1`，无法通过发布前的自动化门槛。
   - `scripts/generate-mcp-configs.py` 生成器配置文件 `scripts/mcp-modules.json` 依然指向不存在的 `phase-2/` 路径，导致执行生成时抛出 `FileNotFoundError`，系统无法以自动脚本维护配置文件一致性。
2. **核心业务职责悬挂或空壳化 (P0 - Blocker)**：
   - **`product-legal`**： launch-watcher 监控本应支持本地 PRD 离线审查，目前却作为 "Phase 2 暂缓" 挂起；`matter-workspace` 也未能在企业内网语境下实现本地 stateful 隔离（哪怕是基本的 in-house mock 状态）。
   - **`employment-legal`**： `expansion-kickoff` 等涉外扩张相关指令处于纯占位状态，未按 `TASK_003` 条件决策（C-1）要求，在 Release Candidate 之前用中国母公司海外派遣/跨境社保/税务与外派登记等中国法等效方案予以责任对齐，直接违反了 "Responsibility Equivalence"（职责等效）的基本原则。
   - **`ip-legal`**： 事项隔离工作流 `matter-workspace` 被完全关闭，未能维护 upstream 所必需的 context 隔离语义。
   - **`legal-builder-hub`**： 该模块包含大量“命令别名”却无任何实际的局部执行逻辑。安装、禁用、卸载和自动更新技能全部流于表面，仅输出空文本模板，缺乏 allowlist 校验和备份/回退等关键安全操作，实质上处于不可用状态。
3. **治理文档陈旧与漂移 (P1 - Gap)**：
   - 项目中仍然存在大量将 `law-student` / `legal-clinic` 称为 Phase 2 或挂起状态的表述（包括 `AGENTS.md`、`QUICKSTART.md`、`PHASE_2_ROADMAP.md`、`CHINA_LOCALIZATION_STATUS.md`），使整体文档和代码结构产生实质性冲突。

---

## 二、 详细审计项核查

### 1. 结构与语法校验 (Structure & Run-time)
- **Marketplace & manifests**：✅ 12 个插件全部就位，格式正确。
- **JSON/YAML 语法**：✅ 49 个 JSON 文件和 38 个 YAML 文件解析正常。
- **外国法残留**：✅ 清洗非常彻底，所有出现的外国法关键词均用于防御性拦截（Negative Constraints），第一方工作流中 0 残留。

### 2. 职责等效与空壳化排查 (Responsibility Equivalence)
经核实，下列上游职责在 CN 中处于空壳化或挂起状态，必须在最终对齐（Alignment Edit）任务中予以物理修复：
- **`employment-legal/skills/expansion-kickoff`** 等：
  - *整改方案*：不能因为“不提供外国法结论”就彻底关闭该技能。应重写为“中国企业海外扩张用工指引”，包括涉外用工方案评估（EOR 选型与风险）、外派人员社会保险补缴、跨境个税合规、跨境用工合同模板起草，并对接到外部律所审查清单中，从而在“中国法视角”下实现职责等效。
- **`product-legal/agents/launch-watcher.md` 与 `matter-workspace`**：
  - *整改方案*：恢复 launch-watcher 对本地上传 PRD、营销方案的结构化分析与合规筛查逻辑；matter-workspace 必须支持本地 YAML 事项文件写入与上下文管理，而非纯文本提示。
- **`ip-legal/skills/matter-workspace`**：
  - *整改方案*：支持 `new/list/switch/close/none` 生命周期，维护多事项隔离状态。
- **`legal-builder-hub/skills/*`**：
  - *整改方案*：必须完善 allowlist 读取、技能源码离线安全审查、安装记录自动追加、安装前备份创建、以及 disable/uninstall 物理文件移除或改名行为。

### 3. WPS 云文档 URL 校验 Gap
- **`diligence-grid/subagents/doc-reader.yaml`** 中配有 wps-cloud-docs 连接器，但其 URL 正则校验拦截了 WPS 的国内正常域名 (`docs.wps.cn` / `kdocs.cn`)，导致实质不可用。
  - *整改方案*：将 WPS 域名补充至 YAML 输出正则匹配白名单中。

---

## 三、 对 ChatGPT 的整改指令建议 (TASK_017 EDIT)

ChatGPT 应当在此 Review 结论发出后，立即生成 **`TASK_017_PHASE1_FINAL_ALIGNMENT_EDIT`** 并放置于 `inbox/` 中，指派 Codex 执行以下具体整改：

1. **修正 CI 脚本与 MCP 生成器路径 (B-1)**：
   - 更新 `scripts/localization-regression.py`，将 `law-student` 和 `legal-clinic` 移至默认 marketplace 正式列表，删除针对旧 `phase-2/` 路径的无用检查，并过滤 `.codex-coordination/` 中的审计记录。
   - 更新 `scripts/mcp-modules.json`，把其中指向 `phase-2/` 的旧路径全部修正为顶级路径，重新运行生成器脚本，确保所有 `.mcp.json` 正确生成。
2. **消灭空壳职责 (B-2, B-3, B-4, B-5)**：
   - 按照 Review 第二部分中定义的整改方案，重建 `employment-legal` 涉外用工、`product-legal` 监控/事项空间、`ip-legal` 事项空间以及 `legal-builder-hub` 技能安装与回退的安全逻辑。
3. **WPS 域名放行 (G-4)**：
   - 在 `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml` 中允许 WPS 域名通过正则拦截。
4. **清理全局文档冲突 (G-5)**：
   - 对 `AGENTS.md`、`QUICKSTART.md`、`PHASE_2_ROADMAP.md`、`CHINA_LOCALIZATION_STATUS.md`、`PROJECT_USAGE_GUIDE.md` 进行地毯式清理，移除所有陈旧的 `phase-2/` 挂起或临时路径提法，使全项目统一为 12 个顶级模块的完备架构。
