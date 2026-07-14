# TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS - RESULT

## Identity

```text
TASK ID: TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS
ARTIFACT TYPE: RESULT
PRODUCER: Codex
NEXT RECEIVER: Gemini
MODE: EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn
PHASE: Phase 1.5 Post-Freeze Development
BRANCH: feature/matter-workspace
```

## Status

`DONE`

The authorized offline Validator and repository test entry were implemented
and validated. No files were staged, committed, pushed, or merged. This RESULT
provides execution evidence only and does not issue an ACCEPT/REJECT decision.

## 1. Modified Files

| File | Purpose |
|---|---|
| `core/matter-workspace/validators/validate.py` | Executable offline CLI for Schema, template, sample, reference and self-test validation. |
| `scripts/test-matter-workspace.sh` | Executable repository test entry that verifies negative FAIL behavior, then runs the positive self-test suite. |
| `.codex-coordination/outbox/TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS_RESULT.md` | Required RESULT artifact. |

The accepted TASK_021-02 Schema files and TASK_021-03 templates/examples were
read only. Their 25 SHA-256 values were captured before implementation and
matched in two consecutive final verification rounds.

## 2. Validator Design

### Offline Schema registry

The CLI:

- requires exactly the eight accepted Draft 2020-12 Schema names;
- parses each Schema as YAML and runs `Draft202012Validator.check_schema`;
- permits only the accepted `.invalid` Schema identifier namespace;
- statically resolves every `$ref` and JSON Pointer against the local Schema
  set;
- builds a `referencing.Registry` containing only local resources;
- contains no HTTP client, URL opener, socket or provider integration.

The accepted Schema set contains 127 locally resolved `$ref` values.

### Strict formats

The CLI installs isolated format checks:

- `date`: valid `YYYY-MM-DD` calendar date only;
- `date-time`: RFC 3339 time component plus explicit `Z` or numeric timezone.

This prevents a date-only value from also satisfying `date-time`, covering the
portability observation recorded in TASK_021-03.

### Template validation

- Discovers every YAML file under `templates/`.
- Requires exactly one `# Template schema:` declaration.
- Maps the declaration to a known local Schema name without opening the
  declared path or any external resource.
- Rejects missing, ambiguous, unknown or unsafe declarations.
- Validates each template against its declared Schema.

The accepted declarations are treated as logical `schema/<name>.yaml`
locators. They are not dereferenced as filesystem imports.

### Sample validation

The CLI validates all nine sample YAML records and checks:

- one root Matter and eight unique entity IDs;
- common `matter_slug` values;
- safe, existing, non-symlink `record_files` paths inside the fixture;
- exact coverage of all entity files by `record_files`;
- record section/type consistency;
- Party, Fact, Evidence, Issue, Claim, Strategy and Decision references;
- participants, key Facts, Claim legal-basis links and Decision inputs;
- nested Claim element/defense links, Issue position links and Evidence holder
  references;
- duplicate IDs, duplicate paths and path traversal.

### Deterministic CLI contract

```text
PASS -> exit code 0
FAIL -> exit code 1
missing dependency -> exit code 2
```

Supported modes:

```text
validate.py --format text
validate.py --format json
validate.py --self-test --format text
validate.py --negative-test --format json
```

JSON keys and error lists are sorted. Output contains no timestamp, absolute
user path or nondeterministic traversal order.

## 3. Validation Examples

### Positive text result

```text
PASS
checked sample_entities=8 sample_record_paths=8 sample_records=9
sample_references=31 schema_refs=127 schemas=8 self_tests=0 templates=8
```

Exit code: `0`.

### Positive machine-readable result

```json
{"checked":{"sample_entities":8,"sample_record_paths":8,"sample_records":9,"sample_references":31,"schema_refs":127,"schemas":8,"self_tests":0,"templates":8},"errors":[],"status":"PASS","warnings":[]}
```

Two independent invocations produced byte-identical JSON. The output was also
checked for `/Users/` and the local username; neither appeared.

### Negative mutation result

An in-memory Fact status mutation produces:

```json
{"checked":{"sample_entities":8,"sample_record_paths":8,"sample_records":9,"sample_references":31,"schema_refs":127,"schemas":8,"self_tests":1,"templates":8},"errors":["negative-test: intentional invalid Fact mutation rejected"],"status":"FAIL","warnings":[]}
```

Exit code: `1`. No accepted fixture file is modified.

### Missing dependency result

Running with Python site packages disabled produces:

```json
{"checked":{},"errors":["missing Python dependency: yaml"],"status":"FAIL","warnings":[]}
```

Exit code: `2`. The Validator does not install or download anything.

## 4. Test Results

### Repository test entry

```text
bash scripts/test-matter-workspace.sh
PASS
checked sample_entities=8 sample_record_paths=8 sample_records=9
sample_references=31 schema_refs=127 schemas=8 self_tests=3 templates=8
```

The same absolute test entry passed when invoked from `/private/tmp`, confirming
that it is independent of the caller's current working directory.

The three isolated self-tests cover:

1. strict date/date-time separation and timezone enforcement;
2. rejection of an invalid in-memory Fact status;
3. rejection of an in-memory `../outside.yaml` record path.

### Existing project validation

```text
python3 scripts/localization-regression.py
China localization regression OK

python3 scripts/generate-mcp-configs.py --check
Validated 12 .mcp.json files.

Structured validation OK: 49 JSON, 63 YAML
legal-data local MCP smoke test: PASS
managed-agent cookbooks: PASS (5/5)
bash -n scripts/test-matter-workspace.sh: PASS
Python syntax validation: PASS
Whitespace validation: PASS
Offline implementation scan: PASS
```

### Accepted-asset immutability

```text
Accepted asset hash validation round 1 OK: 25 files
Accepted asset hash validation round 2 OK: 25 files
```

During validation, one manually transcribed baseline digest was initially two
characters short and produced a false drift alert. Direct inspection showed
the file unchanged; the corrected 64-character digest then passed both full
verification rounds. No repository file was reverted or altered in response.

## 5. Remaining Work

- TASK_021-05 may add persistent integration-test fixtures and CI routing for
  the Validator; TASK_021-04 intentionally adds only the basic test entry.
- Runtime environments need `PyYAML`, `jsonschema` and `referencing`. This TASK
  does not install or fetch them; missing dependencies fail explicitly.
- The accepted template declaration comments are logical Schema locators, not
  valid relative filesystem imports. The Validator safely maps only the known
  Schema basename. Any decision to normalize those comments requires a
  separately authorized template-alignment task.
- No Agent, workflow, MCP or business-module integration has begun.

## 6. Git Status / Diff Summary

```text
Current branch: feature/matter-workspace
Validator lines: 802
Test-entry lines: 29
Tracked file changes: 0
Staged files: 0
```

`git diff --stat` remains empty because all TASK_021 additions are untracked.
TASK_021-04 adds only:

```text
?? core/matter-workspace/validators/validate.py
?? scripts/test-matter-workspace.sh
?? .codex-coordination/outbox/TASK_021-04_IMPLEMENT_OFFLINE_VALIDATORS_RESULT.md
```

The pre-existing `.gitkeep` and TASK_021-01 through TASK_021-03 artifacts remain
present and untracked. A final boundary check found no tracked modification and
no unrelated untracked path.

## 7. Handoff

`NEXT RECEIVER: Gemini`

Gemini should review the offline guarantees, strict format behavior, reference
coverage, deterministic output, negative exit contract and accepted-asset hash
evidence before issuing REVIEW/DECISION. TASK_021-05 must not begin before that
decision.
