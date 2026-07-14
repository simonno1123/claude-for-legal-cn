# TASK_021-03_CREATE_TEMPLATE_FIXTURES

## Identity

```text
STATUS: READY
ARTIFACT TYPE: TASK
PRODUCER: ChatGPT
TO: Codex
NEXT RECEIVER: Gemini
MODE: EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
PHASE: Phase 1.5 Post-Freeze Development
PARENT: TASK_021_MATTER_WORKSPACE_ENHANCEMENT
```

## Objective

Create Matter Workspace initialization templates and sanitized example fixture
data using the accepted TASK_021-02 Schema definitions.

## Allowed Additions

### Templates

- `core/matter-workspace/templates/civil-litigation/`
- `core/matter-workspace/templates/enforcement/`
- `core/matter-workspace/templates/corporate/`

Required responsibilities:

- Civil litigation: Matter, Party, Evidence and timeline/Fact templates.
- Enforcement: debtor/Party and asset-relation/Fact templates.
- Corporate: company-relation/Fact and shareholder-analysis/Issue templates.

### Sanitized fixture

- `core/matter-workspace/examples/sample-matter/`

The fixture may contain only fictional, generic parties and facts. It must not
include a real client, person, company, case number or confidential source.

## Constraints

- Use the accepted Core Schema files without modifying them.
- Keep Phase 1.5 Matter fields and local-path conventions compatible.
- Do not modify anything outside `core/matter-workspace/`, except the required
  ACOS TASK and RESULT artifacts.
- Do not integrate Agents, workflows, MCP, databases, UI or external services.
- Do not stage, commit or push.

## Validation

- Parse every new file as YAML.
- Validate each template and sample entity against its declared Core Schema.
- Verify all sample entity references and `record_files` paths are internally
  consistent.
- Run the existing China localization regression.
- Confirm no unrelated working-tree changes were introduced.

## Required Output

Create:

```text
.codex-coordination/outbox/TASK_021-03_CREATE_TEMPLATE_FIXTURES_RESULT.md
```

The RESULT must include created templates, fixture inventory, validation
results, diff/status summary and execution status. It is execution evidence
only; Gemini is the next receiver for REVIEW and DECISION.
