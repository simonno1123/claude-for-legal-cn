# Codex Task

## 1. Task ID

TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT

## 2. Status

READY

## 3. Background

Following the audit under `TASK_012`, the managed cookbooks and external plugins have been accepted with conditions. This task is an EDIT task to resolve the remaining foreign SaaS residue (`box` server in `doc-reader.yaml`), inject a local legal warning into `cocounsel-legal`'s research skill, and document the vendor plugin isolation policy.

## 4. Goal

Perform cleanup of the `box` residue, add the local warning to the deep-research skill, and create the `external_plugins/README.md` file.

## 5. Allowed Scope

Allowed to modify:
- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`
- `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md`

Allowed to create:
- `external_plugins/README.md`

## 6. Forbidden Actions

1. Do not modify files in other folders.
2. Do not run any Git commit or Git add commands.

## 7. Requirements

### 1. Naming Residue Cleanup in `doc-reader.yaml`
- Modify the file `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`.
- Remove the lines representing `box` mcp server:
  - Line 29: `- { type: mcp_toolset, mcp_server_name: box,     default_config: { enabled: true  } }`
  - Line 33: `- { type: url, name: box,     url: "${WPS_CLOUD_DOCS_MCP_URL}" }`
- Keep all other lines as is.

### 2. Warning Note in `cocounsel-legal/skills/deep-research/SKILL.md`
- Modify the file `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md`.
- Right after the YAML frontmatter (after line 8), insert:
  ```markdown
  > [!WARNING]
  > 本技能属于第三方的 Westlaw / 美国法外部插件。除非用户明确指定进行美国法或 Westlaw 检索，本技能默认不被加载，亦不得作为中华人民共和国大陆地区法律检索的默认手段。中国法域检索请导向 `regulatory-legal` 或根目录 `references/` 规范。
  ```

### 3. Create `external_plugins/README.md`
- Create a new markdown file at `external_plugins/README.md`.
- Provide the vendor plugin isolation policy:
  ```markdown
  # 外部第三方插件治理政策 (External Vendor Plugins Policy)

  为了保障 `claude-for-legal-cn` 默认中国法合规环境的纯净度，所有保留的第三方外部/Vendor插件（如 `cocounsel-legal`）必须遵守以下治理隔离政策：

  1. **默认非激活**：外部插件默认不载入核心市场（不登记在 `.claude-plugin/marketplace.json` 中）。
  2. **明确法域边界**：外部插件其自身的技能、代理配方和 README 中必须显式标注其法域约束（如：仅供美国法/Westlaw检索）。
  3. **禁止静默覆盖**：当用户请求中国 Mainland 法律事务时，系统禁止调用这些外部插件提供未经核验的境外法律结论。
  ```

## 8. Acceptance Criteria

1. Target files are modified/created exactly as instructed.
2. `doc-reader.yaml` no longer contains reference to `box` server.
3. `deep-research/SKILL.md` contains the warning box.
4. `external_plugins/README.md` is created with the required text.
5. All JSON/YAML files pass structural syntax tests.

## 9. BLOCKED Rules

If any conflict occurs, stop and report BLOCKED.

## 10. DONE Report Format

Codex should report:
1. Status (DONE)
2. Files modified/created
3. Summary of text changes
4. Validation results

## 11. Next Handoff Target

Gemini

## 12. Reason

To enable Gemini to review the alignment results and close the audit.
