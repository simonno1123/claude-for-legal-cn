# TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING

## Identity

```text
STATUS: READY
ARTIFACT TYPE: TASK
PRODUCER: ChatGPT
TO: Codex
NEXT RECEIVER: Gemini
MODE: EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
PHASE: Phase 1.5 Post-Freeze Development / Integration Verification
PARENT: TASK_021_MATTER_WORKSPACE_ENHANCEMENT
BRANCH: feature/matter-workspace
```

## Objective

Complete the offline Matter Workspace validation chain:

```text
Schema -> Templates -> Sample Matter -> Offline Validator -> Regression / CI
```

Add persistent integration tests for positive and failure scenarios, route the
accepted Validator into the repository's existing regression/CI path, and
document local use and failure recovery.

## Existing Route

The repository already contains:

- `.github/workflows/ci.yml`;
- `scripts/localization-regression.py`;
- `scripts/test-matter-workspace.sh`.

Prefer the existing route. Do not create a parallel CI framework or duplicate
workflow unless the current route cannot satisfy this TASK.

## Allowed Paths

### Read-only accepted assets

- `core/matter-workspace/schema/**`
- `core/matter-workspace/templates/**`
- `core/matter-workspace/examples/**`

### Authorized additions/edits

- `tests/matter-workspace/**`
- `core/matter-workspace/docs/**`
- `core/matter-workspace/validators/**` only for a testability defect proven by
  the new integration tests; preserve the accepted CLI and exit contract.
- `scripts/test-matter-workspace.sh`
- `scripts/localization-regression.py`
- `.github/workflows/ci.yml` only for the minimum existing-job routing or
  dependency setup required by this TASK.
- A narrowly scoped Matter Validator dependency declaration under
  `core/matter-workspace/validators/` if CI reproducibility requires it.
- `.codex-coordination/outbox/TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING_RESULT.md`

Do not modify `.github/workflows/cla.yaml` or unrelated scripts/workflows.

## Required Implementation

### 1. Persistent integration tests

Use a repository-native, non-network test mechanism. Prefer Python standard
library `unittest` unless an existing project test runner is already declared.

Tests must cover:

- loading all eight Schema files;
- YAML parsing and local `$ref` resolution;
- all accepted template instances;
- the complete Sample Matter and typed references;
- deterministic JSON `PASS` output and exit code `0`;
- invocation from outside the repository working directory;
- missing required field;
- malformed YAML;
- Schema/type mismatch;
- illegal lifecycle/entity status;
- record path traversal or missing target;
- deterministic JSON `FAIL` output and non-zero exit behavior;
- strict separation of `date` and timezone-bearing `date-time`.

Negative cases must use temporary directories, in-memory mutation or copied
fixtures. Never alter an accepted fixture in place.

### 2. Regression routing

Integrate the Matter Workspace test entry into
`scripts/localization-regression.py` or its direct existing CI route.

Requirements:

- failure must propagate and make the regression command non-zero;
- diagnostics must identify the Matter Workspace test entry;
- no recursion between `localization-regression.py` and
  `test-matter-workspace.sh`;
- invocation must work from any current working directory;
- existing regression behavior must remain intact.

### 3. CI routing

Update the existing `.github/workflows/ci.yml` only as needed so a clean Ubuntu
runner executes the Matter Workspace integration gate.

Dependency rule:

- do not assume GitHub-hosted runners preinstall `PyYAML`, `jsonschema` or
  `referencing`;
- do not add an unpinned `pip install` command;
- use an existing repository dependency mechanism if one exists;
- otherwise add an explicit, narrowly scoped and version-pinned dependency
  declaration and document that package provisioning is CI setup, while the
  Validator itself performs no network access;
- if reproducible dependency provisioning cannot be established within scope,
  stop and report `BLOCKED` rather than creating a CI route known to fail.

No network, API, provider or external service may be contacted by the Validator
or tests after dependency provisioning.

### 4. Documentation

Add a concise guide under `core/matter-workspace/docs/` covering:

- Validator and integration-test entry points;
- required Python dependencies and offline boundary;
- text and JSON output contracts;
- exit codes `0`, `1`, and `2`;
- local invocation from repository root and another cwd;
- interpretation of Schema, YAML, reference and dependency failures;
- safe recovery steps that do not edit accepted fixtures automatically.

## Validation Required

- Run the new persistent integration tests.
- Run `bash scripts/test-matter-workspace.sh`.
- Run `python3 scripts/localization-regression.py` and prove it invokes the
  Matter Workspace gate.
- Exercise all four required error categories: missing field, malformed YAML,
  Schema mismatch and illegal status.
- Validate deterministic JSON output and exit codes.
- Validate `.github/workflows/ci.yml` syntax/structure without pushing.
- Run existing JSON/YAML, legal-data and cookbook checks.
- Confirm accepted Schema/template/example assets remain byte-for-byte
  unchanged.
- Confirm no unrelated tracked or untracked change was introduced.

## Forbidden

- Modifying business/legal plugins, Agents, Skills or legal workflows.
- Adding a legal Skill or substantive legal opinion behavior.
- MCP, PKULaw, judgment-database, court-system, WPS or enterprise integration.
- External databases or online legal APIs.
- Automatic legal judgment or autonomous legal action.
- Execution-derived litigation, evidence collection or asset investigation
  functionality.
- Modifying accepted Schema, templates or examples.
- Creating a new CI platform when the existing workflow is sufficient.
- Dependency installation in the local execution environment.
- `git add`, commit, push or merge.

## Required Output

Create:

```text
.codex-coordination/outbox/TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING_RESULT.md
```

The RESULT must include:

1. Modified Files
2. Test Architecture
3. CI Integration
4. Validation Results
5. Remaining Risks
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
