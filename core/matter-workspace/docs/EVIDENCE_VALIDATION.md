# Evidence Validation Framework

## Purpose

The Evidence Validation Framework determines whether an Evidence record is
structurally suitable for a Matter Workspace process. It does not determine
authenticity, admissibility, evidentiary weight, liability, strategy, or case
outcome. It never repairs, supplements, or rewrites an Evidence record.

The implementation is fully offline:

```text
core/matter-workspace/validators/evidence_validation.py
```

## Result Contract

Every validation returns the same machine-readable fields:

```yaml
status: PASS | FAIL
errors: []
warnings: []
reviewer_required: true
```

`FAIL` means at least one structural or state-consistency error exists.
Warnings preserve non-blocking work for a later workflow stage.
`reviewer_required` is true unless the record contains a structurally
consistent approved Human Review Gate. A `PASS` result is not a legal approval.

## Validation Profiles

### Record

The `record` profile applies the accepted `evidence.yaml` Schema and checks:

- required fields and field formats;
- Evidence lifecycle and Human Review consistency;
- typed Fact and Issue relationship targets against `fact_refs` and
  `issue_refs`.

For example, `verified` Evidence must have an approved Human Review Gate, and
an approved or rejected gate must identify its reviewer and review time.

### Template

The `template` profile adds reusable template controls:

- `module_fields.template` must be true;
- domain templates must contain a supported `classification`;
- domain templates must contain Fact and Issue references with typed mappings;
- domain templates must contain a pending Human Review Gate.

The original generic Evidence seed template remains backward compatible.
Missing domain mappings on that generic seed are warnings. Templates carrying
`module_fields.domain` are checked strictly and fail when a required mapping or
gate is missing.

### Workflow Entry

The `workflow-entry` profile defines the minimum boundary before an accepted
Evidence Intake Record proceeds to Normalization:

- the record must pass the Evidence Schema;
- Evidence `status` must be `received`;
- a pending Human Review Gate must be present;
- acquisition may remain `to_assess` but cannot be marked `unlawful`;
- typed relationship targets, when present, must resolve to the corresponding
  reference list.

Classification is not required at this boundary because Classification is a
later workflow stage. A missing classification produces a warning that must be
resolved there. Fact and Issue links may likewise be completed later; the
framework checks their consistency without inventing targets.

## Template Validation

Validate every Evidence template in the repository:

```bash
python3 core/matter-workspace/validators/evidence_validation.py \
  --templates --format text
```

Use JSON for automation:

```bash
python3 core/matter-workspace/validators/evidence_validation.py \
  --templates --format json
```

Validate a single Evidence record before workflow entry:

```bash
python3 core/matter-workspace/validators/evidence_validation.py \
  --profile workflow-entry path/to/evidence.yaml
```

The command returns exit code `0` for `PASS`, `1` for `FAIL`, and `2` when the
offline framework cannot initialize. It does not install dependencies or
contact any service.

## Failure Handling

Validation errors must be returned to a human-controlled correction process.
The framework must not:

- infer missing evidence or relationships;
- alter lifecycle or review state;
- approve its own output;
- parse documents, images, bank records, or chat histories;
- retrieve external data;
- generate a legal opinion or litigation filing.

Corrections remain separate, attributable actions. After correction, the
record must be validated again before advancing.
