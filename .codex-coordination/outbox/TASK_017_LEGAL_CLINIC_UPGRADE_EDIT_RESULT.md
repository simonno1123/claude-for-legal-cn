# TASK_017_LEGAL_CLINIC_UPGRADE_EDIT_RESULT

ARTIFACT TYPE: RESULT
PRODUCER: Codex
NEXT RECEIVER: Gemini
MODE: EDIT
PROJECT: /Users/zhang/Documents/claude-for-legal-cn

## Status

DONE

## Files Moved

- Moved `phase-2/legal-clinic/` to root `legal-clinic/`.
- Renamed `legal-clinic/deadlines.yaml` to `legal-clinic/deadlines-ledger.yaml`.
- Source path `phase-2/legal-clinic/` no longer exists on disk.

## Files Modified / Created In Scope

- `.claude-plugin/marketplace.json`
- `PROJECT_USAGE_GUIDE.md`
- `docs/UPSTREAM_MAPPING_MATRIX.md`
- `legal-clinic/.claude-plugin/plugin.json`
- `legal-clinic/README.md`
- `legal-clinic/CLAUDE.md`
- `legal-clinic/deadlines-ledger.yaml`
- `legal-clinic/review-queue.yaml`
- `legal-clinic/client-comms/_README.md`
- `legal-clinic/handoffs/_README.md`
- `legal-clinic/skills/build-guide/SKILL.md`
- `legal-clinic/skills/client-comms-log/SKILL.md`
- `legal-clinic/skills/client-intake/SKILL.md`
- `legal-clinic/skills/client-letter/SKILL.md`
- `legal-clinic/skills/cold-start-interview/SKILL.md`
- `legal-clinic/skills/customize/SKILL.md`
- `legal-clinic/skills/deadlines/SKILL.md`
- `legal-clinic/skills/draft/SKILL.md`
- `legal-clinic/skills/form-generation/SKILL.md`
- `legal-clinic/skills/memo/SKILL.md`
- `legal-clinic/skills/plain-language-letters/SKILL.md`
- `legal-clinic/skills/ramp/SKILL.md`
- `legal-clinic/skills/research-start/SKILL.md`
- `legal-clinic/skills/semester-handoff/SKILL.md`
- `legal-clinic/skills/status/SKILL.md`
- `legal-clinic/skills/supervisor-review-queue/SKILL.md`
- `legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml`

## Marketplace Registration

Added root-level plugin entry:

```json
{
  "name": "legal-clinic",
  "displayName": "法律诊所与援助 (Legal Clinic & Aid)",
  "source": "./legal-clinic",
  "description": "提供中国高校法律诊所、基层法律援助中心、12348公共法律服务时效台账与导师审查流。"
}
```

Confirmed marketplace lines:

```text
100:      "name": "law-student",
102:      "source": "./law-student",
109:      "name": "legal-clinic",
111:      "source": "./legal-clinic",
```

## Documentation Alignment

Updated:

- `PROJECT_USAGE_GUIDE.md`
- `docs/UPSTREAM_MAPPING_MATRIX.md`

Validation:

```text
rg -n 'phase-2/(law-student|legal-clinic)' PROJECT_USAGE_GUIDE.md docs/UPSTREAM_MAPPING_MATRIX.md
```

Result: no matches.

Also checked README + both governance docs together:

```text
rg -n 'phase-2/(law-student|legal-clinic)' README.md PROJECT_USAGE_GUIDE.md docs/UPSTREAM_MAPPING_MATRIX.md
```

Result: no matches.

## Restored Capabilities

### Structure

- `legal-clinic/` now exists at root.
- `phase-2/legal-clinic/` has been removed/migrated.
- Root `legal-clinic/skills/` contains all 16 skill folders.

### Stateful Timeline Tracking

Restored `deadlines-ledger.yaml` and rewrote `/legal-clinic:deadlines` to support:

- `add`
- `report`
- `update`
- `complete`
- `close`
- duplicate checks
- warning cadence `[30, 14, 7, 3, 1]`
- no AI final deadline calculation
- supervisor review escalation for close deadlines

### Supervisor Review Queue

Created root `legal-clinic/review-queue.yaml` and upgraded `/legal-clinic:supervisor-review-queue` with strict states:

- `pending_review`
- `approved`
- `returned_with_comments`

External-facing, rights-dispositive, deadline-sensitive and case-closure outputs are blocked until approved.

### Client Intake

Upgraded `/legal-clinic:client-intake` to include:

- issue routing,
- conflict checks,
- legal-aid criteria screen under PRC Legal Aid Law context,
- triage classification,
- mandatory deadline handoff,
- supervisor review queue handoff.

### Handoff

Upgraded `/legal-clinic:semester-handoff` to:

- read active cases, deadlines, communications and review queue;
- generate per-case handoff memos;
- generate cohort summaries;
- queue handoffs for supervisor review.

### Other Skill Depth

All remaining skills now include China-law clinic context, stateful file behavior, review gate behavior, deadline handoff, or supervisor approval loops:

- `build-guide`
- `client-comms-log`
- `client-letter`
- `customize`
- `draft`
- `form-generation`
- `memo`
- `plain-language-letters`
- `ramp`
- `research-start`
- `status`

## Validation Results

### JSON Validation

All commands exited 0:

```text
python3 -m json.tool .claude-plugin/marketplace.json >/dev/null
python3 -m json.tool legal-clinic/.claude-plugin/plugin.json >/dev/null
python3 -m json.tool legal-clinic/.mcp.json >/dev/null
python3 -m json.tool legal-clinic/hooks/hooks.json >/dev/null
```

### YAML Validation

All commands exited 0:

```text
ruby -e 'require "yaml"; ARGV.each { |f| YAML.load_file(f); puts "YAML OK #{f}" }' \
  legal-clinic/deadlines-ledger.yaml \
  legal-clinic/review-queue.yaml \
  legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml
```

Output:

```text
YAML OK legal-clinic/deadlines-ledger.yaml
YAML OK legal-clinic/review-queue.yaml
YAML OK legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml
```

### Directory Checks

```text
legal-clinic-root:exists
phase-2-legal-clinic:removed
```

### Skill Inventory

Root skill files:

```text
legal-clinic/skills/build-guide/SKILL.md
legal-clinic/skills/client-comms-log/SKILL.md
legal-clinic/skills/client-intake/SKILL.md
legal-clinic/skills/client-letter/SKILL.md
legal-clinic/skills/cold-start-interview/SKILL.md
legal-clinic/skills/customize/SKILL.md
legal-clinic/skills/deadlines/SKILL.md
legal-clinic/skills/draft/SKILL.md
legal-clinic/skills/form-generation/SKILL.md
legal-clinic/skills/memo/SKILL.md
legal-clinic/skills/plain-language-letters/SKILL.md
legal-clinic/skills/ramp/SKILL.md
legal-clinic/skills/research-start/SKILL.md
legal-clinic/skills/semester-handoff/SKILL.md
legal-clinic/skills/status/SKILL.md
legal-clinic/skills/supervisor-review-queue/SKILL.md
```

### Stateful Keyword Check

Confirmed in `legal-clinic/`:

- `deadlines-ledger.yaml`
- `review-queue.yaml`
- `pending_review`
- `approved`
- `returned_with_comments`
- `导师`
- `执业律师`
- `法律援助`
- `12348`
- `法援`

### Foreign-Law Residue Check

Search terms checked:

```text
CourtListener|Descrybe|Westlaw|Clio|Slack|Google Drive|ABA|Model Rules|FRCP|state bar|U.S.|US|United States|attorney-client|work product|privilege|California|Illinois|CA|IL|immigration|asylum|ICE|eviction|housing|family law
```

Remaining hit:

- `legal-clinic/skills/build-guide/SKILL.md`: negative instruction, "Do not import U.S. clinic practice rules."

No foreign-law default framework was found in the upgraded module.

## Git Status Notes

Task-scoped status:

```text
 M .claude-plugin/marketplace.json
 M PROJECT_USAGE_GUIDE.md
 M docs/UPSTREAM_MAPPING_MATRIX.md
 D phase-2/legal-clinic/.claude-plugin/plugin.json
 D phase-2/legal-clinic/.gitignore
 D phase-2/legal-clinic/.mcp.json
 D phase-2/legal-clinic/CLAUDE.md
 D phase-2/legal-clinic/README.md
 D phase-2/legal-clinic/client-comms/_README.md
 D phase-2/legal-clinic/deadlines.yaml
 D phase-2/legal-clinic/handoffs/_README.md
 D phase-2/legal-clinic/hooks/hooks.json
 D phase-2/legal-clinic/references/plausibility-bands/CN.md
 D phase-2/legal-clinic/references/test-cases-cn.md
 D phase-2/legal-clinic/skills/build-guide/SKILL.md
 D phase-2/legal-clinic/skills/client-comms-log/SKILL.md
 D phase-2/legal-clinic/skills/client-intake/SKILL.md
 D phase-2/legal-clinic/skills/client-intake/references/intake-templates/README.md
 D phase-2/legal-clinic/skills/client-letter/SKILL.md
 D phase-2/legal-clinic/skills/cold-start-interview/SKILL.md
 D phase-2/legal-clinic/skills/customize/SKILL.md
 D phase-2/legal-clinic/skills/deadlines/SKILL.md
 D phase-2/legal-clinic/skills/draft/SKILL.md
 D phase-2/legal-clinic/skills/form-generation/SKILL.md
 D phase-2/legal-clinic/skills/memo/SKILL.md
 D phase-2/legal-clinic/skills/plain-language-letters/SKILL.md
 D phase-2/legal-clinic/skills/ramp/SKILL.md
 D phase-2/legal-clinic/skills/research-start/SKILL.md
 D phase-2/legal-clinic/skills/semester-handoff/SKILL.md
 D phase-2/legal-clinic/skills/status/SKILL.md
 D phase-2/legal-clinic/skills/supervisor-review-queue/SKILL.md
 D phase-2/legal-clinic/skills/supervisor-review-queue/references/review-queue.yaml
?? legal-clinic/
```

Repository also contains pre-existing unrelated modifications from earlier tasks; they were not staged or committed.

## Unresolved Risks / Follow-Up

- This task did not implement real external providers or case-management integrations, per scope.
- `review-queue.yaml` and `deadlines-ledger.yaml` are local file workflows, not automated notification systems.
- Final acceptance should verify whether Gemini wants `deadlines.yaml` compatibility alias retained. TASK_017 explicitly required `deadlines-ledger.yaml`, so the migrated module uses that name.

## Forbidden Actions Compliance

- No `git add`.
- No commit.
- No changes to unrelated plugins.
- No real MCP provider implementation.
- No REVIEW or DECISION produced.
