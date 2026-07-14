# TASK_021-01_CREATE_MATTER_WORKSPACE_CORE_STRUCTURE

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

Create the Matter Workspace Core directory structure that will host later
Schema, Template, Validator and Agent Integration work.

This task establishes the carrier structure only. It does not implement Matter
Schema or workflow behavior.

## Allowed Additions

```text
core/matter-workspace/
core/matter-workspace/schema/
core/matter-workspace/templates/
core/matter-workspace/examples/
core/matter-workspace/validators/
core/matter-workspace/docs/
```

Empty leaf directories may contain a minimal `.gitkeep` marker so the structure
can be preserved by Git.

## Excluded

- Modifying existing Agents.
- Modifying existing Skills.
- Modifying plugins.
- Modifying Phase 1.5 frozen documentation.
- Creating Schema definitions.
- Implementing MCP integrations.
- Implementing workflows.
- Deleting or moving existing files.

## Constraints

- Preserve the Phase 1.5 Baseline Freeze.
- Use additive evolution.
- Perform development outside `main`.
- Do not stage, commit or push.

## Validation

- The required directory tree exists.
- Existing China localization regression passes.
- Existing JSON/YAML validation passes where applicable.
- No existing Agent, Skill, plugin or frozen Phase 1.5 document is modified.

## Required Output

Create:

```text
.codex-coordination/outbox/TASK_021-01_CREATE_MATTER_WORKSPACE_CORE_STRUCTURE_RESULT.md
```

The RESULT must include:

1. Directory Change Report
2. Validation Result
3. Git Diff Summary
4. Boundary Confirmation

The RESULT is execution evidence only. Gemini is the next receiver for REVIEW
and DECISION.
