# TASK_018_PHASE1_ALIGNMENT_EDIT

STATUS: READY

TO: Codex

FROM: ChatGPT

MODE: EDIT

PROJECT:
/Users/zhang/Documents/claude-for-legal-cn


## OBJECTIVE

根据：

TASK_017_PHASE1_SCOPE_RECLASSIFICATION_DECISION

执行 Phase 1 Release Candidate 必要对齐修复。

目标：

使项目达到 Phase 1 Freeze 前工程一致状态。

本任务不扩展业务能力。


---

## ALLOWED PATHS

### Runtime

scripts/**


### Documentation

README.md
QUICKSTART.md
PROJECT_USAGE_GUIDE.md
AGENTS.md
PHASE_2_ROADMAP.md
CHINA_LOCALIZATION_STATUS.md
docs/**


### Configuration

managed-agent-cookbooks/**


### Agent Metadata

相关 agent markdown 文件。


---

## REQUIRED ACTIONS


### 1. Regression Script Alignment

修复：

scripts/localization-regression.py


要求：

- 支持当前 root modules；
- 不再引用已迁移 phase-2/law-student；
- 不再引用已迁移 phase-2/legal-clinic；
- 正确处理 .codex-coordination；
- regression 可执行。


---

### 2. MCP Configuration Alignment

检查并修复：

scripts/mcp-modules.json

scripts/generate-mcp-configs.py


要求：

- 删除失效路径；
- 指向当前模块位置；
- generator 可运行。


---

### 3. Documentation Alignment

同步：

README.md

QUICKSTART.md

PROJECT_USAGE_GUIDE.md

AGENTS.md

PHASE_2_ROADMAP.md

CHINA_LOCALIZATION_STATUS.md

docs/**


修正：

- 模块数量；
- 路径；
- 阶段状态。


---

### 4. Command Reference Verification

检查：

product-legal

ai-governance-legal

相关 command。


要求：

引用必须：

- 存在；
- 可解析；
- 名称一致。


---

### 5. Schema Validation

检查：

managed-agent-cookbooks/**


仅修复：

- YAML schema；
- URL pattern；
- 配置一致性。


禁止实现真实外部连接。


---

### 6. Agent Frontmatter

补充缺失 metadata。

禁止修改 agent 行为逻辑。


---

## FORBIDDEN

禁止：

- 新增 Phase 1.5 功能；
- Matter Workspace建设；
- 执行衍生诉讼系统建设；
- MCP真实接入；
- 北大法宝接口；
- 裁判文书接口；
- WPS API；
- Legal Builder Hub执行能力；
- 跨境业务能力扩展；
- git add；
- git commit。


---

## OUTPUT

生成：

.codex-coordination/outbox/

TASK_018_PHASE1_ALIGNMENT_EDIT_RESULT.md


RESULT必须包含：

1. Modified Files
2. Change Summary
3. Validation Results
4. Remaining Deferred Items
5. Commit Recommendation
