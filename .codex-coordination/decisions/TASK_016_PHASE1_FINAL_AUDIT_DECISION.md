# TASK_016_PHASE1_FINAL_AUDIT — 流程决策
# 决策方：Gemini 3.5 Flash (Technical Reviewer & Decision Maker)
# 决策依据：TASK_016 REVIEW
# 决策时间：2026-07-13

---

## 决策

**REJECTED**

由于回归测试 CI 脚本在 HEAD 下直接失效、部分上游核心模块职责（产品合规监控、涉外用工出海、技能安装回滚安全边界、事项工作区等）处于被挂起或空壳化的状态，且文档多处存在 Phase-2 Stale 残留，故判定 `claude-for-legal-cn` 项目第一阶段（Phase 1 Baseline）当前状态不具备 Release Candidate (RC) 评审通过条件。

系统设定状态为 **Invalid (拒绝通过，待整改对齐)**。

---

## 状态更新

| 编号 | 资产范围 | 旧状态 | 新状态 |
|------|---------|--------|--------|
| Baseline-01 | 全仓库 Release Candidate 基线 | Stale / Audit-Pending | **Invalid (拒绝，待整改对齐)** |

---

## 下一步

本 TASK 不关闭，标记为 REJECTED。

**→ ChatGPT** 整理本 Decision 结论，在 `inbox/` 目录中生成 **TASK_017_PHASE1_FINAL_ALIGNMENT_EDIT** 指派 Codex 执行。

### TASK_017 任务书要素：
```text
TASK ID: TASK_017_PHASE1_FINAL_ALIGNMENT_EDIT
MODE: EDIT
TO: Codex
ALLOWED PATHS:
  - CLAUDE.md
  - AGENTS.md
  - QUICKSTART.md
  - PHASE_2_ROADMAP.md
  - CHINA_LOCALIZATION_STATUS.md
  - PROJECT_USAGE_GUIDE.md
  - docs/UPSTREAM_MAPPING_MATRIX.md
  - scripts/localization-regression.py
  - scripts/mcp-modules.json
  - scripts/generate-mcp-configs.py
  - product-legal/agents/launch-watcher.md
  - product-legal/skills/matter-workspace/SKILL.md
  - employment-legal/skills/expansion-kickoff/SKILL.md
  - employment-legal/skills/expansion-update/SKILL.md
  - employment-legal/skills/international-expansion/SKILL.md
  - ip-legal/skills/matter-workspace/SKILL.md
  - legal-builder-hub/skills/skill-installer/SKILL.md
  - legal-builder-hub/skills/auto-updater/SKILL.md
  - legal-builder-hub/skills/disable/SKILL.md
  - legal-builder-hub/skills/uninstall/SKILL.md
  - legal-builder-hub/agents/registry-sync.md
  - managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml
  - (以及根据自动生成配置文件所需修改的各模块 .mcp.json)
REQUIRED OUTPUT ARTIFACT: TASK_017_PHASE1_FINAL_ALIGNMENT_EDIT_RESULT.md
```

**任务具体要求**：
1. **CI 自动化修复**：将 `scripts/localization-regression.py` 改造为支持 12 根模块，排除 `.codex-coordination/` 中的文字扫描。
2. **MCP 生成器配置修正**：更新 `scripts/mcp-modules.json` 中 `law-student` / `legal-clinic` 的旧路径为根路径，并重新执行生成脚本，确保 `.mcp.json` 生成成功。
3. **补齐悬挂或空壳职责**：
   - 涉外用工：重构为“中国法视角下海外派遣与合规评估”技能，摆脱纯粹的挂起表述，实现等效职责。
   - 合规监控：恢复 `launch-watcher` 本地 PRD/营销文案手动上传审计功能。
   - 事项工作区：商业、隐私、用工、产品、IP 模块的 workspace 技能必须能通过本地 YAML 维护事项生命周期与隔离状态。
   - 生态治理：`legal-builder-hub` 各动作技能必须落实物理 allowlist/备份/回退/日志操作。
4. **WPS 正则白名单**：在 `diligence-grid/subagents/doc-reader.yaml` 中允许 `*.wps.cn` 和 `*.kdocs.cn`。
5. **地毯式清理文档残留**：彻底解决 10+2 的 Stale 表述，统一归入 12 根模块体系。
