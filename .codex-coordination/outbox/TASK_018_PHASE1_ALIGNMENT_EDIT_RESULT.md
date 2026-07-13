# TASK_018_PHASE1_ALIGNMENT_EDIT — RESULT

TASK ID: `TASK_018_PHASE1_ALIGNMENT_EDIT`

PRODUCER: Codex

NEXT RECEIVER: Gemini

MODE: EDIT

PROJECT: `/Users/zhang/Documents/claude-for-legal-cn`

## 1. Modified Files

### Runtime

- `scripts/localization-regression.py`
- `scripts/mcp-modules.json`
- `scripts/generate-mcp-configs.py`

### Documentation / Governance

- `README.md`
- `QUICKSTART.md`
- `PROJECT_USAGE_GUIDE.md`
- `AGENTS.md`
- `PHASE_2_ROADMAP.md`
- `CHINA_LOCALIZATION_STATUS.md`
- `docs/PROJECT_SCOPE.md`
- `docs/UPSTREAM_MAPPING_MATRIX.md`
- `docs/FAITHFUL_PORT_STANDARD.md`

### Command Reference

- `product-legal/skills/launch-review/references/seven-category-framework.md`

### Cookbook Schema

- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`

### Agent Metadata

- `commercial-legal/agents/deal-debrief.md`
- `commercial-legal/agents/playbook-monitor.md`
- `commercial-legal/agents/renewal-watcher.md`
- `legal-builder-hub/agents/registry-sync.md`

### Coordination Artifact

- `.codex-coordination/outbox/TASK_018_PHASE1_ALIGNMENT_EDIT_RESULT.md`

## 2. Change Summary

### Regression Script Alignment

- Replaced the historical 10+2 module sets with one 12-module `ROOT_MODULES` set.
- Removed all runtime expectations for `phase-2/law-student` and `phase-2/legal-clinic`.
- Excluded `.codex-coordination/` and `.git/` from product JSON and foreign-law backslide scans.
- Added validation that `scripts/mcp-modules.json` contains exactly the 12 root module paths.
- Preserved the default marketplace vendor-isolation and China-law regression checks.

### MCP Configuration Alignment

- Changed `scripts/mcp-modules.json` paths to `law-student` and `legal-clinic`.
- Refactored MCP output construction into `build_output()`.
- Added `python3 scripts/generate-mcp-configs.py --check` for read-only path and generated-config consistency validation.
- Did not change any module `.mcp.json`; all 12 existing files already match the corrected generator source.

### Documentation Alignment

- Replaced the old Complete Chinese Port completion claim with the Gemini-approved Phase 1 baseline positioning.
- Defined Phase 1 Baseline, Phase 1.5 Legal Workflow Layer, and Phase 2 Advanced Integration boundaries.
- Synchronized the repository to 12 root first-party modules and removed 10+2 / old education-module path statements.
- Recorded product/local workspace and local tracker work under Phase 1.5.
- Recorded employment international expansion, real providers, external automation, and Legal Builder Hub physical actions under Phase 2.
- Updated the mapping matrix to record each module's current Phase 1 baseline and deferred responsibility.
- Removed employment business-priority wording and corrected the current 168-skill count.
- Clarified that `legal-data` is a minimal local sample server and other providers are not production-integrated.

### Command Reference Alignment

- Replaced `/privacy-legal:pia-audit` with the existing `/privacy-legal:pia-generation` command.
- Replaced `/ai-governance-legal:cac-filing` with the existing `/ai-governance-legal:security-assessment` command.

### Schema Alignment

- Extended the diligence document-reader URL schema to accept `*.wps.cn` and `*.kdocs.cn` while retaining the existing declared domains.
- No WPS API, credential, connector, or network behavior was added.

### Agent Frontmatter

- Added `name`, `description`, `model`, and minimal `tools: ["Read"]` metadata to the three commercial agents and `legal-builder-hub/agents/registry-sync.md`.
- Did not alter their workflow bodies or add automatic scheduling, notifications, writes, or external registry access.

## 3. Validation Results

| Validation | Result |
|---|---|
| Python AST parse for modified scripts | PASS |
| `python3 scripts/localization-regression.py` | PASS: `China localization regression OK` |
| `python3 scripts/generate-mcp-configs.py --check` | PASS: 12/12 configs validated |
| First-party command reference scan | PASS: 440 references, 0 unresolved |
| JSON parsing | PASS: 49 files |
| YAML parsing | PASS: 38 files |
| Agent frontmatter | PASS: 10/10 first-party agent files |
| WPS URL schema fixtures | PASS: `docs.wps.cn`, `kdocs.cn`, `www.kdocs.cn` |
| Marketplace validator | PASS |
| 12 first-party plugin validators | PASS with only the pre-existing expected root `CLAUDE.md` template warnings |
| `python3 scripts/lint-tool-scope.py` | PASS: 5/5 cookbooks |
| `bash scripts/test-cookbooks.sh` | PASS: 5/5 cookbooks |
| `bash scripts/test-legal-data.sh` | PASS |
| Modified-document relative links | PASS: 9 files |
| `git diff --check` | PASS |

Current tracked diff before this RESULT artifact:

```text
18 files changed, 322 insertions(+), 197 deletions(-)
```

No module `.mcp.json` changed during validation.

## 4. Remaining Deferred Items

### Phase 1.5 Legal Workflow Layer

- Product local launch tracker and human-triggered review queue.
- Product, IP, commercial, privacy, and employment opt-in matter lifecycle.
- Commercial agent local persistence, thresholds, history, and deduplication.
- A reusable local tracker/workspace contract.

### Phase 2 Advanced Integration / External Capability

- Employment international expansion, EOR, foreign tax/immigration and target-jurisdiction professional workflow.
- Legal Builder Hub physical install, update, rollback, disable, uninstall, and remote registry synchronization.
- Real WPS, commercial legal database, court/arbitration, enterprise collaboration, and product-management providers.
- External automatic monitoring, scheduling, and notification delivery.

### Remaining Phase 1 Path-Scope Exclusions

The following Phase 1 statement-alignment items were identified but not edited
because TASK_018 did not authorize marketplace manifests, plugin README/CLAUDE,
or plugin skill files:

1. Marketplace/manifest descriptions still differ for `product-legal`, `legal-builder-hub`, `law-student`, and `legal-clinic`.
2. `legal-builder-hub/.claude-plugin/plugin.json` still uses a `cn-phase2` version/description, and `legal-builder-hub/README.md` still uses first-sequence and physical-action wording.
3. `product-legal` and `ip-legal` matter-workspace skill metadata/CLAUDE sections still say Phase 2, while the accepted registry assigns local matter lifecycle to Phase 1.5.
4. `commercial-legal/skills/matter-workspace/SKILL.md` still advertises `new/list/switch/close/none` although its body is template-only.
5. Legal Builder Hub action-skill descriptions still use install/disable/uninstall execution wording although Phase 1 provides planning/manual boundaries only.

These are not Phase 1.5 or Phase 2 implementation requests. They are remaining
Phase 1 declaration/metadata alignment items that require an explicitly expanded
allowed-path task if Gemini requires physical correction before RC review.

## 5. Commit Recommendation

**Recommendation: HOLD — do not commit yet.**

Reasons:

1. ACOS requires Gemini REVIEW / DECISION before commit.
2. The authorized TASK_018 changes pass all executed validations.
3. Gemini should decide whether the five path-scope exclusions above require a narrow follow-up alignment task before accepting the Phase 1 RC patch.

If Gemini accepts the current scope or approves a follow-up micro-alignment, commit
only the reviewed Phase 1 files and the required coordination artifacts. Do not
include Phase 1.5 or Phase 2 implementation work.

## Execution Boundary

- No Phase 1.5 capability was implemented.
- No matter workspace lifecycle was built.
- No real MCP provider, WPS API, commercial database, court interface, or external connector was added.
- No Legal Builder Hub physical action or international expansion capability was implemented.
- No file was staged or committed.
- No REVIEW or DECISION was produced by Codex.
