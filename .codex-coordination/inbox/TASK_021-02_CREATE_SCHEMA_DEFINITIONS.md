# TASK_021-02_CREATE_SCHEMA_DEFINITIONS

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

Create the core Matter Workspace data-model Schema definitions under
`core/matter-workspace/schema/`.

## Allowed Additions

- `core/matter-workspace/schema/matter.yaml`
- `core/matter-workspace/schema/party.yaml`
- `core/matter-workspace/schema/fact.yaml`
- `core/matter-workspace/schema/evidence.yaml`
- `core/matter-workspace/schema/issue.yaml`
- `core/matter-workspace/schema/claim.yaml`
- `core/matter-workspace/schema/strategy.yaml`
- `core/matter-workspace/schema/decision.yaml`

## Constraints

- Maintain compatibility with the Phase 1.5 Local Workflow Contract.
- Use Schema definitions only; do not implement runtime behavior.
- Do not modify an existing module, Agent, Skill, plugin, workflow, MCP
  configuration, or frozen Phase 1.5 document.
- Do not add a database, external integration, or UI.
- Do not stage, commit, or push.

## Validation

- Parse all eight files as YAML.
- Validate each document as JSON Schema Draft 2020-12.
- Resolve all local cross-Schema references without network access.
- Confirm a Phase 1.5-compatible `matter.yaml` fixture validates.
- Run the existing China localization regression.
- Confirm no unrelated working-tree changes were introduced.

## Required Output

Create:

```text
.codex-coordination/outbox/TASK_021-02_CREATE_SCHEMA_DEFINITIONS_RESULT.md
```

The RESULT must include Schema files, validation results, diff/status summary,
execution status and unresolved issues. It is execution evidence only; Gemini
is the next receiver for REVIEW and DECISION.
