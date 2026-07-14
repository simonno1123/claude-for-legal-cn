# Matter Workspace Validation

## Scope

The Matter Workspace Validator checks the repository's accepted Schema,
templates, and synthetic `sample-matter` fixture. It runs locally and does not
contact a Schema registry, legal-data provider, MCP server, database, or online
API.

Package installation is environment provisioning, not Validator execution.
After the Python environment is prepared, all validation and integration tests
operate on repository files and temporary copies only.

## Requirements

Use Python 3.13 with the fixed validation environment:

```bash
python3 -m pip install --no-input \
  -r core/matter-workspace/validators/requirements.txt
```

The Validator never installs missing packages. A missing dependency produces a
machine-readable `FAIL` and exit code `2`.

## Entry Points

Run the complete persistent integration suite and Validator self-tests:

```bash
bash scripts/test-matter-workspace.sh
```

Run the Validator directly:

```bash
python3 core/matter-workspace/validators/validate.py --format text
python3 core/matter-workspace/validators/validate.py --format json
```

Both entry points derive the repository root from their own file locations.
They may be invoked from another current working directory:

```bash
cd /tmp
bash /absolute/path/to/claude-for-legal-cn/scripts/test-matter-workspace.sh
```

The project-wide regression also runs the Matter Workspace gate:

```bash
python3 scripts/localization-regression.py
```

## Output And Exit Codes

Text output starts with `PASS` or `FAIL`. JSON output contains deterministic
`status`, `checked`, `errors`, and `warnings` fields. It contains no timestamps
or absolute user paths.

| Exit code | Meaning |
|---|---|
| `0` | All selected checks passed. |
| `1` | Schema, YAML, template, fixture, reference, path, or self-test failure. |
| `2` | A required Python package is unavailable. |

## Integration Tests

The standard-library `unittest` suite lives under `tests/matter-workspace/`.
Negative tests copy accepted assets into a temporary directory before removing
fields, writing malformed YAML, changing Schema declarations or statuses, and
injecting unsafe paths. Accepted repository fixtures are never edited in place.

Run only the persistent tests with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover \
  -s tests/matter-workspace -p 'test_*.py' -v
```

## Failure Handling

### Missing Dependency

Use the fixed `requirements.txt` in a controlled environment. Do not add an
automatic installer to the Validator or suppress exit code `2`.

### YAML Parse Failure

Open the reported repository-relative file, fix syntax in an authorized task,
and rerun the complete test entry. Do not replace the file with Validator
output.

### Schema Or Template Failure

Review the reported instance path and the corresponding accepted Schema. Do
not loosen the Schema or rewrite a template automatically. Schema or template
changes require their own review because those assets are already accepted.

### Sample Reference Failure

Check entity IDs, `matter_slug`, `record_files`, typed references and target
paths. Do not create a missing legal fact or evidence record merely to satisfy
validation; correct only a confirmed fixture inconsistency.

### CI Failure

The existing GitHub Actions `validate` job prepares the pinned Python
environment and invokes `scripts/localization-regression.py`, which propagates
the Matter Workspace test exit code. Reproduce locally with the same
requirements and regression command before changing CI configuration.

## Safety Boundary

Validation proves structural consistency only. It does not verify legal truth,
evidentiary weight, admissibility, strategy quality, legal authority currency,
or professional approval. It never performs filing, sending, notification,
asset investigation, provider access, or autonomous legal action.
