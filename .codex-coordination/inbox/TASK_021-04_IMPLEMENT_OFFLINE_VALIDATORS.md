# TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS

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
BRANCH: feature/matter-workspace
```

## Objective

Implement a deterministic, local-only Matter Workspace validator based on:

- accepted TASK_021-02 Schema Definitions;
- accepted TASK_021-03 Templates and Sample Matter fixtures.

The validator must validate the Core Schema documents, every template and the
complete `examples/sample-matter/` fixture without network access.

## Allowed Paths

### Read-only inputs

- `core/matter-workspace/schema/**`
- `core/matter-workspace/templates/**`
- `core/matter-workspace/examples/**`

### Authorized additions/edits

- `core/matter-workspace/validators/**`
- `scripts/test-matter-workspace.sh`
- `.codex-coordination/outbox/TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS_RESULT.md`

The accepted Schema, templates and example fixtures must not be modified under
this TASK.

## Required Implementation

### 1. Offline Schema validation

- Parse all eight YAML Schema files.
- Validate each as JSON Schema Draft 2020-12.
- Resolve cross-Schema `$ref` values from a local registry only.
- Never retrieve a Schema or reference over the network.

### 2. Template validation

- Discover all YAML files under `core/matter-workspace/templates/`.
- Map every template to its declared Core Schema.
- Fail on an unknown, missing or ambiguous Schema declaration.
- Validate every template instance.

### 3. Sample Matter validation

- Validate all YAML records under `examples/sample-matter/` against the
  appropriate Core Schema.
- Verify `matter_slug` consistency.
- Verify that every `record_files` path exists and stays inside the fixture.
- Verify typed entity references, participants, key Facts, Claim legal-basis
  references and Decision input references.
- Reject duplicate entity IDs and path traversal.

### 4. Strict format handling

- Validate `date` as `YYYY-MM-DD` only.
- Validate `date-time` as RFC 3339 with a time component and timezone.
- Preserve a regression case for the TASK_021-03 observation where the default
  Python format checker may treat a date-only value as both formats.

### 5. Machine-readable result

Provide a CLI with deterministic exit behavior:

```text
PASS -> exit code 0
FAIL -> non-zero exit code
```

Support JSON output containing at least:

```json
{
  "status": "PASS",
  "checked": {},
  "errors": []
}
```

Do not include timestamps, absolute user paths or nondeterministic ordering in
the machine-readable result.

### 6. Basic test entry

Create `scripts/test-matter-workspace.sh` as the repository test entry. It must:

- invoke the offline validator from any current working directory;
- propagate the validator exit code;
- perform no installation and no network access.

If required Python libraries are unavailable, fail clearly with a concise
dependency message. Do not install dependencies in this TASK.

## Validation Required

- Run the validator against all accepted Schema, templates and sample files.
- Run `scripts/test-matter-workspace.sh`.
- Exercise one isolated negative fixture or in-memory mutation and confirm a
  non-zero/FAIL result without modifying accepted fixture files.
- Run `python3 scripts/localization-regression.py`.
- Run existing structured JSON/YAML checks.
- Confirm no unrelated tracked or untracked changes were introduced.

## Forbidden

- MCP integration or provider work.
- External databases, online APIs or network Schema retrieval.
- PKULaw, judgment-database or court-system integrations.
- Modifying business/legal plugins, Agents, Skills or workflows.
- Modifying accepted Schema, templates or example fixtures.
- Automatic legal judgment or autonomous legal action.
- UI implementation.
- Dependency installation.
- `git add`, commit, push or merge.

## Required Output

Create:

```text
.codex-coordination/outbox/TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS_RESULT.md
```

The RESULT must include:

1. Modified Files
2. Validator Design
3. Validation Examples
4. Test Results
5. Remaining Work
6. Git Status / Diff Summary

The RESULT is execution evidence only and must not issue an ACCEPT/REJECT
decision.

## Handoff

```text
NEXT RECEIVER: Codex
ROLE: Execution Layer

After Codex RESULT:
NEXT RECEIVER: Gemini
ROLE: Review / Decision Layer
```
