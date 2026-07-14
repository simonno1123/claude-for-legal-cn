# TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING - RESULT

## Identity

```text
TASK ID: TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING
ARTIFACT TYPE: RESULT
PRODUCER: Codex
NEXT RECEIVER: Gemini
MODE: EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
PHASE: Phase 1.5 Post-Freeze Development / Integration Verification
BRANCH: feature/matter-workspace
```

## Status

`DONE`

The offline Matter Workspace chain is covered by persistent integration tests
and routed through the repository's existing localization regression and CI
job. No file was staged, committed, pushed or merged. This RESULT records
execution evidence only and does not issue an ACCEPT/REJECT decision.

## 1. Modified Files

| File | Change |
|---|---|
| `tests/matter-workspace/test_validator.py` | Added 13 persistent `unittest` integration tests for the accepted Schema, templates, sample records, Validator CLI and failure propagation. |
| `scripts/test-matter-workspace.sh` | Runs the persistent suite, verifies deterministic machine-readable negative behavior, and then runs the accepted Validator self-tests. |
| `scripts/localization-regression.py` | Routes the Matter Workspace test entry into the existing regression command and propagates its exit status and bounded diagnostics. |
| `.github/workflows/ci.yml` | Provisions Python 3.13, installs the scoped pinned dependency declaration, and runs the existing localization regression route. |
| `core/matter-workspace/validators/requirements.txt` | Declares exact versions for the Validator's direct and required transitive Python packages. |
| `core/matter-workspace/docs/VALIDATION.md` | Documents local/CI entry points, dependencies, offline boundary, output/exit contracts and safe failure recovery. |
| `.codex-coordination/outbox/TASK_021-05_INTEGRATION_TESTS_AND_CI_ROUTING_RESULT.md` | This required RESULT artifact. |

The accepted `validate.py` implementation required no testability repair and
was not modified. The accepted Schema, templates and examples remained read
only.

## 2. Test Architecture

### Persistent suite

`tests/matter-workspace/test_validator.py` uses Python standard-library
`unittest`. Destructive scenarios copy all accepted assets into isolated
`TemporaryDirectory` trees before mutation; no accepted fixture is edited in
place.

The 13 tests cover:

1. all eight Schema files, YAML parsing and 127 local `$ref` resolutions;
2. all eight accepted templates;
3. the full nine-record Sample Matter and typed-reference graph;
4. deterministic JSON `PASS` output and exit code `0` from an external cwd;
5. deterministic JSON `FAIL` output and exit code `1` for a negative mutation;
6. a missing required field;
7. malformed YAML;
8. template/Schema mismatch;
9. illegal entity status;
10. record-path traversal;
11. a missing record target;
12. strict separation of `date` and timezone-bearing `date-time`;
13. dependency pinning, existing-CI routing and regression failure
    propagation.

### Repository entry

`scripts/test-matter-workspace.sh` resolves the repository root from its own
path, so it does not depend on the caller's cwd. It runs:

```text
unittest integration suite
        -> explicit machine-readable negative contract
        -> Validator positive self-test suite
```

`PYTHONDONTWRITEBYTECODE=1` prevents test execution from adding bytecode
artifacts to the repository.

### Failure behavior

The integration suite directly exercises:

- missing required data;
- malformed YAML;
- Schema/type mismatch;
- illegal lifecycle/entity status;
- unsafe or missing local record paths;
- invalid date/date-time formats;
- Matter test-entry failure propagation through the localization regression.

## 3. CI Integration

The existing `.github/workflows/ci.yml` remains the only CI workflow route.
No parallel CI framework was created.

The existing `validate` job now:

1. uses `actions/setup-python@v5` with Python `3.13`;
2. caches pip data using
   `core/matter-workspace/validators/requirements.txt` as the dependency key;
3. installs exact versions from the scoped requirements file;
4. runs `python3 scripts/localization-regression.py`, which invokes
   `scripts/test-matter-workspace.sh`.

The exact dependency set is:

```text
attrs==26.1.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
PyYAML==6.0.3
referencing==0.37.0
rpds-py==2026.5.1
```

Package provisioning is CI setup only. The Validator and integration tests
contain no network, API, provider or external-service operation.

The regression runner:

- resolves paths from the script location;
- runs the Matter gate with the repository root as cwd;
- captures and bounds failure diagnostics;
- returns non-zero when the Matter gate fails;
- does not recurse into itself.

## 4. Validation Results

### Matter Workspace gate from an external cwd

```text
cd /private/tmp
bash /Users/zhang/Documents/claude-for-legal-cn/scripts/test-matter-workspace.sh

Ran 13 tests in 1.784s
OK
PASS
checked sample_entities=8 sample_record_paths=8 sample_records=9
sample_references=31 schema_refs=127 schemas=8 self_tests=3 templates=8
```

### Existing project regression

```text
python3 scripts/localization-regression.py
China localization regression OK

python3 scripts/generate-mcp-configs.py --check
Validated 12 .mcp.json files.

bash scripts/test-legal-data.sh
legal-data local MCP smoke test: PASS

bash scripts/test-cookbooks.sh
managed-agent cookbooks: PASS (5/5)
```

The persistent suite includes a controlled fake test-entry failure and confirms
that `localization-regression.py` reports the Matter gate and exits non-zero.

### Structured files and CI syntax

```text
Structured parse: PASS (49 JSON, 63 YAML)
CI workflow parse: PASS (1 existing job)
git diff --check: PASS
Python test syntax/execution: PASS
Matter implementation offline scan: PASS
Generated __pycache__ directories: none
```

### Dependency reproducibility check

```text
python3 -m pip install --dry-run --no-index \
  -r core/matter-workspace/validators/requirements.txt
```

All six exact versions were satisfied locally. `--dry-run --no-index` ensured
that this validation neither installed packages nor contacted a package index.

### Accepted-asset immutability

The 25 accepted YAML files under `schema/`, `templates/` and `examples/` were
rehash-checked twice after implementation:

```text
aggregate SHA-256:
5f1601e569d606848e444f8e2a0cde9312656f2cad39c66c06f5790e49202125
```

Both rounds matched. Including the three accepted `.gitkeep` placeholders,
the 28-file tree aggregate also matched in two rounds. No accepted asset has a
modification time later than the accepted TASK_021-04 decision artifact.

## 5. Remaining Risks

- The GitHub-hosted CI job has not run remotely because this TASK forbids
  commit and push. Its YAML, route, dependency declaration and local behavior
  were validated without network access.
- Exact version pins provide deterministic resolution at the package-version
  level but do not include package hashes. Hash-locked installation may be
  considered in a separately authorized supply-chain hardening task.
- The integration gate validates technical structure and local references; it
  does not decide legal truth, admissibility, strategy or legal outcome.
- Agent, Skill, workflow, MCP and business-module integration remain outside
  this TASK.

## 6. Git Status / Diff Summary

```text
Current branch: feature/matter-workspace
Staged files: 0
Tracked modifications introduced by TASK_021-05:
  .github/workflows/ci.yml
  scripts/localization-regression.py

Tracked diff stat:
  2 files changed, 49 insertions(+), 1 deletion(-)

TASK_021-05 additions/authorized untracked paths:
  tests/matter-workspace/test_validator.py
  core/matter-workspace/docs/VALIDATION.md
  core/matter-workspace/validators/requirements.txt

TASK_021-04 file updated within authorized scope:
  scripts/test-matter-workspace.sh
```

The remaining untracked `core/` and `.codex-coordination/` artifacts belong to
TASK_021-01 through TASK_021-04 and their accepted ACOS history. No unrelated
tracked path was modified by TASK_021-05. Nothing is staged.

## 7. Handoff

```text
NEXT RECEIVER: Gemini
ROLE: Review / Decision Layer
```

Gemini should review the persistent negative coverage, failure propagation,
clean-runner dependency setup, offline boundary and accepted-asset evidence
before issuing REVIEW/DECISION.
