# TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT_RESULT

Artifact Type: RESULT
Producer: Codex
Task: TASK_013_COOKBOOKS_AND_EXTERNAL_PLUGINS_ALIGNMENT_EDIT
Mode: EDIT
Project: /Users/zhang/Documents/claude-for-legal-cn
Next Receiver: Gemini

This artifact reports execution facts only. It is not a REVIEW and not a DECISION.

## 1. Status

DONE

## 2. Files Modified / Created

Modified:

- `managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml`
- `external_plugins/cocounsel-legal/skills/deep-research/SKILL.md`

Created:

- `external_plugins/README.md`

No files were staged or committed.

## 3. Summary of Changes

### managed-agent-cookbooks/diligence-grid/subagents/doc-reader.yaml

Removed the `box` MCP tool/server entries exactly as requested:

```yaml
- { type: mcp_toolset, mcp_server_name: box,     default_config: { enabled: true  } }
- { type: url, name: box,     url: "${WPS_CLOUD_DOCS_MCP_URL}" }
```

The active MCP tool/server entries now use:

```yaml
- { type: mcp_toolset, mcp_server_name: wps-cloud-docs,  default_config: { enabled: true  } }
- { type: mcp_toolset, mcp_server_name: imanage, default_config: { enabled: false } }

- { type: url, name: wps-cloud-docs,  url: "${WPS_CLOUD_DOCS_MCP_URL}" }
- { type: url, name: imanage, url: "${IMANAGE_MCP_URL}" }
```

### external_plugins/cocounsel-legal/skills/deep-research/SKILL.md

Inserted the required warning box immediately after YAML frontmatter:

```markdown
> [!WARNING]
> 本技能属于第三方的 Westlaw / 美国法外部插件。除非用户明确指定进行美国法或 Westlaw 检索，本技能默认不被加载，亦不得作为中华人民共和国大陆地区法律检索的默认手段。中国法域检索请导向 `regulatory-legal` 或根目录 `references/` 规范。
```

### external_plugins/README.md

Created the vendor plugin isolation policy with these rules:

- default inactive / not in core marketplace;
- explicit jurisdiction boundary;
- no silent override for China Mainland legal matters.

## 4. Validation Results

### Target Checks

`doc-reader.yaml` no longer contains either of these server/tool entries:

```text
mcp_server_name: box
name: box
```

The warning box exists in:

```text
external_plugins/cocounsel-legal/skills/deep-research/SKILL.md
```

The vendor policy file exists:

```text
external_plugins/README.md
```

### YAML Validation

Command:

```text
ruby -e 'require "yaml"; ARGV.each { |f| YAML.load_file(f); puts "#{f}: OK" }' managed-agent-cookbooks/*/agent.yaml managed-agent-cookbooks/*/subagents/*.yaml
```

Result: all managed-agent cookbook YAML files parsed successfully.

### JSON Validation

Command:

```text
for f in managed-agent-cookbooks/*/steering-examples.json external_plugins/cocounsel-legal/.claude-plugin/plugin.json external_plugins/cocounsel-legal/.mcp.json; do python3 -m json.tool "$f" >/dev/null && echo "$f: OK"; done
```

Result: all checked cookbook and CoCounsel JSON files parsed successfully.

## 5. Notes

The task explicitly required removing the `box` MCP server/tool entries and keeping all other lines as-is. Therefore no other URL host allowlist or schema patterns were changed.

## 6. Handoff

NEXT RECEIVER: Gemini

Gemini should review this RESULT and issue REVIEW / DECISION for TASK_013.
