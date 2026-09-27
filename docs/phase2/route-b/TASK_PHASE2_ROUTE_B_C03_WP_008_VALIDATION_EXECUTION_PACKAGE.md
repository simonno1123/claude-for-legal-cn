# Phase 2 Route B C03 WP-008 Validation Execution Package

## 0. Package Control

| Field | Value |
| --- | --- |
| Package type | VALIDATION EXECUTION DESIGN PACKAGE |
| Activation semantics | `CAPABILITY_ONLY` |
| Materialization authorization SHA-256 | `F87C1D014C2AAF63908F5182404BFFA5A229568D0DFE5A924037D0328B21390E` |
| Package status | **MATERIALIZED — PACKAGE REVIEW NOT AUTHORIZED** |
| Harness or test code | NOT CREATED / NOT AUTHORIZED |
| Command execution | NOT AUTHORIZED / NOT PERFORMED |
| Raw validation evidence | NOT CREATED |
| `C03-CP-E-011` / `C03-CP-E-013` | NOT CREATED / NOT AUTHORIZED |
| Tier A blockers closed | `0 / 3` |
| C03 activation readiness | NOT READY |
| Automatic downstream transition | BLOCKED |

This Package defines an exact future execution contract. It is not a harness,
command, test, execution authorization, runtime observation, validation result,
or blocker-closure decision.

## 1. Fixed Governing Lineage

| Baseline | SHA-256 | Required state |
| --- | --- | --- |
| Adopted Operational Validation Plan | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` | ADOPTED & SHA BOUND |
| Validation Preparation Packet | `13B73C5AABD062D322EA1E41C52B0F6A8E8D90E6E2BD8069738372384EA54A07` | ACCEPTED & SHA BOUND |
| Environment Identity Manifest | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` | ACCEPTED AS PREPARATION IDENTITY |
| Preparation Internal Review | `412FC5B32033495AFAC631581D19E6D20FC8200B04453961D875CD916083BD52` | PASS — GRADE A |
| Preparation Acceptance and Fixture Admission Decision | `0AA106618E545DF41B267EAD0CC4F28E7D15578728F123E4C5EBD7D81C967835` | 15 / 15 FIXTURES ADMITTED |

Any mismatch, modification, withdrawal, supersession, revocation, or kill state
blocks harness materialization and execution.

## 2. Future Harness Contract

### 2.1 Exact Future Asset

| Field | Contract value |
| --- | --- |
| Future harness path | `validation/route_b_c03/wp_008/run_validation.py` |
| Language | Python 3.12.13 |
| Dependencies | Python standard library only |
| Harness state | NOT CREATED / NOT AUTHORIZED |
| Harness SHA | NOT AVAILABLE — MUST BE FIXED BEFORE EXECUTION |
| Network capability | PROHIBITED |
| Provider/model capability | PROHIBITED |
| Filesystem discovery | PROHIBITED OUTSIDE EXACT READ/WRITE SETS |
| Subprocess or dynamic execution | PROHIBITED |
| Package installation | PROHIBITED |
| Real matter / OCR / legal access | PROHIBITED |

### 2.2 Mandatory Harness Responsibilities

Before importing any validation subject, a later harness must:

1. verify its own SHA against the execution authorization;
2. verify every governing baseline, subject, environment, and fixture SHA;
3. verify the exact run ID, evidence destination, command identity, and
   authorization reference;
4. verify that the allowed read and write sets are exact and closed;
5. establish no-network, no-provider, no-subprocess, no-dynamic-execution, and
   no-package-mutation guards;
6. reject all unlisted arguments, files, environment variables, fixtures,
   scenario IDs, output paths, and tools;
7. execute scenarios in fixed order `C03-TA-V-001` through
   `C03-TA-V-015` with isolated state per scenario;
8. record expected and observed values in separate fields;
9. stop immediately on a critical mismatch or boundary violation;
10. write only the exact authorized raw-evidence files.

The harness must not determine Plan adoption, fixture admission, evidence
acceptance, blocker closure, readiness, activation, or legal correctness.

## 3. Executable and Tool Allowlist

| Tool | Bound identity | Future permission |
| --- | --- | --- |
| `.venv-validation/Scripts/python.exe` | `560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E` | Sole candidate execution tool; still NOT AUTHORIZED |
| `.venv-validation/Scripts/jq.exe` | `23CB60A1354EED6BCC8D9B9735E8C7B388CD1FDCB75726B93BC299EF22DD9334` | EXCLUDED FROM EXECUTION ALLOWLIST |
| `.venv-validation/Scripts/jsonschema.exe` | `EE056533C215CD97187298826AD70B68DBC80C2E6881D0494F0494A12B3349A5` | EXCLUDED FROM EXECUTION ALLOWLIST |
| `.venv-validation/Scripts/pip.exe` | `7DE9B91EA7C840110BE6ADEC48DEECD3ACC57D568C51252FC7CEA00710525F14` | PROHIBITED |

Only the exact Python executable may be proposed by a later execution
authorization. No shell utility, package manager, network client, provider,
model, connector, MCP, API, or external process is admitted.

## 4. Closed Future Command Template

The only permissible command form for a later authorization is:

```text
.venv-validation/Scripts/python.exe -I -S validation/route_b_c03/wp_008/run_validation.py --run-id <AUTHORIZED_RUN_ID> --fixture-root validation/route_b_c03/wp_008/fixtures --evidence-root validation/route_b_c03/wp_008/evidence/<AUTHORIZED_RUN_ID>
```

Hard constraints:

- `<AUTHORIZED_RUN_ID>` must be replaced by one exact immutable identifier in
  the later execution authorization;
- the future harness SHA and exact full command must be bound before use;
- no other flag, environment variable, redirection, pipe, wildcard, shell
  operator, working directory, input path, output path, or tool is permitted;
- `-I -S` is mandatory; site packages are unavailable to the harness;
- any command drift or unknown argument blocks execution.

This Package records the template only. It does not execute it.

## 5. Exact Read-Set Contract

### 5.1 Governing and Subject Read Set

| Class | Exact content |
| --- | --- |
| Governing documents | Five fixed-SHA assets in Section 1 plus this Package, its later review/adoption, and later exact execution authorization |
| Subject files | Ten implementation paths and SHAs bound in the adopted Plan |
| Environment files | Exact `pyvenv.cfg` and Python executable identities bound by the environment manifest |
| Fixtures | Fifteen exact admitted JSON files bound by the admission decision |
| Future harness | Exact path and future fixed SHA from Section 2 |

No repository-wide enumeration, implicit glob, parent-directory traversal,
symlink traversal, hidden asset discovery, non-target file read, Route A/OCR
asset read, case/evidence read, independent ACOS read, or Git metadata read is
permitted during future execution.

## 6. Exact Future Write-Set Contract

For one later-authorized `<AUTHORIZED_RUN_ID>`, the only permitted write root
is:

```text
validation/route_b_c03/wp_008/evidence/<AUTHORIZED_RUN_ID>/
```

The only permitted future files are:

| File | Purpose |
| --- | --- |
| `run_manifest.json` | Exact baseline, subject, environment, fixture, harness, command, role, and authorization identities |
| `scenario_results.jsonl` | One immutable expected/observed record per scenario |
| `audit_revocation_results.jsonl` | Audit continuity, revocation, kill, rollback, integrity, and write-set observations |
| `defect_register.json` | Closed defect records or explicit empty register |

Every other write is prohibited. The future harness must create the run
directory only after all preflight checks pass and must fail if the directory
already exists or contains any entry. No overwrite, append to a prior run,
rename across run roots, cleanup outside the run root, Git write, upstream
write, ACOS write, temporary-file spill, bytecode, cache, log, or telemetry
write is permitted.

The evidence root and files do not exist under this Package authorization.

## 7. Preflight Gate

All rows must pass before any subject import or evidence-directory creation.

| Preflight ID | Required determination |
| --- | --- |
| `C03-WP008-PF-001` | Package, Plan, preparation, environment, review, admission, harness, and execution-authorization SHAs match |
| `C03-WP008-PF-002` | Ten subject file SHAs match the adopted Plan |
| `C03-WP008-PF-003` | Fifteen fixture file SHAs match the admission decision |
| `C03-WP008-PF-004` | Python executable and `pyvenv.cfg` SHAs match |
| `C03-WP008-PF-005` | Full command, run ID, working directory, read set, and write set match |
| `C03-WP008-PF-006` | Network, provider, subprocess, dynamic execution, package mutation, and external access guards are active |
| `C03-WP008-PF-007` | Evidence run directory is absent and parent destination is exact |
| `C03-WP008-PF-008` | Executor and independent reviewer identities are separately bound with no conflict |
| `C03-WP008-PF-009` | No stale, withdrawn, revoked, superseded, or kill state applies |
| `C03-WP008-PF-010` | No real matter, evidence, personal data, credential, secret, key, token, path, locator, or executable payload exists in fixtures |

Any preflight failure stops without subject import, fixture use, or evidence
directory creation.

## 8. Scenario Execution Contract

| Field | Mandatory future behavior |
| --- | --- |
| Scenario order | Ascending `C03-TA-V-001` through `C03-TA-V-015` |
| State isolation | Fresh scenario state; no state inheritance except explicit duplicate relation in V-006 |
| Expected values | Loaded from exact admitted fixture and Plan contract |
| Observed values | Captured separately; never copied from expected fields |
| Write set | Captured and compared against exact permitted/prohibited sets |
| Audit identity | Unique immutable record ID and SHA per scenario |
| Stop behavior | Immediate stop on critical mismatch; later scenarios marked NOT RUN |
| Rerun | Prohibited under same run ID; requires new exact authorization and run ID |

No aggregate PASS may be computed by the harness. The harness may record only
per-check matches, mismatches, blocked conditions, and raw observations. A
separate reviewer determines validation outcomes.

## 9. Raw Evidence Schemas

### 9.1 Scenario Result Record

Each future `scenario_results.jsonl` row must contain:

```text
run_id
record_id
scenario_id
fixture_id
fixture_sha256
subject_manifest_sha256
environment_manifest_sha256
harness_sha256
execution_authorization_sha256
expected_state
expected_reason_class
expected_permitted_write_set
expected_prohibited_effect
observed_state
observed_reason_class
observed_write_set
observed_effect_class
audit_record_id
audit_record_sha256
preflight_state
stop_state
raw_match_state
limitation
```

### 9.2 Audit/Revocation Result Record

Each future `audit_revocation_results.jsonl` row must contain:

```text
run_id
record_id
control_class
source_scenario_id
expected_control_state
observed_control_state
write_set
continuity_predecessor_sha256
record_sha256
revocation_or_kill_reference
rollback_or_supersession_reference
integrity_state
release_authority_present
raw_match_state
limitation
```

### 9.3 Defect Register

Each future defect must contain a unique ID, severity, class, affected subject,
scenario and record IDs, expected/observed difference, boundary effect, stop
state, permitted disposition, supersession reference, and reviewer state.

## 10. Roles and Independence Contract

| Stable role ID | Responsibility | Current binding |
| --- | --- | --- |
| `C03-WP008-EXECUTOR` | Perform one exact authorized run and attest raw evidence completeness | NOT BOUND |
| `C03-WP008-IMPLEMENTATION-AUTHOR` | Explain subject design; may not execute or review own corrections | ROLE DEFINED / PERSON NOT REQUIRED |
| `C03-WP008-INTERNAL-REVIEWER` | Independently review raw evidence against adopted Plan | NOT BOUND |
| `C03-WP008-PROJECT-OWNER` | Sole positive authority for execution, evidence acceptance, blocker closure, readiness, and activation | CONVERSATION-LEVEL AUTHORITY ROLE |

Stable role identities are sufficient; no real-person name is required. The
executor and reviewer must be different task/session roles. The reviewer must
not author or modify the future harness, execute the run, or repair evidence.

## 11. Immediate Stop and Withdrawal Controls

Future preparation or execution must stop if:

1. any fixed identity, SHA, role, command, path, or authorization is absent,
   stale, mismatched, or ambiguous;
2. any unlisted read, write, argument, tool, environment variable, dependency,
   process, network, provider, model, external service, repository, or asset is
   requested or observed;
3. any real matter, evidence, personal data, credential, secret, key, token,
   file locator, or executable payload appears;
4. any expected/observed field is merged, prefilled, suppressed, overwritten,
   inferred, or silently normalized;
5. any unauthorized write, duplicate effect, retry execution, fallback,
   substitution, release, rollback, or downstream transition occurs;
6. audit continuity, raw evidence completeness, run isolation, determinism, or
   reviewer independence cannot be established;
7. a critical defect, kill state, revocation, withdrawal, supersession, or
   evidence-integrity failure exists.

Stop does not authorize cleanup, retry, repair, rerun, rollback, evidence
acceptance, or blocker closure.

## 12. Governance Materialization Boundary

Raw future files are not themselves accepted governance evidence. After a
separately authorized run:

1. raw files must be fixed by SHA without modification;
2. `C03-CP-E-011` and `C03-CP-E-013` may be materialized only under a separate
   exact-asset authorization;
3. expected and observed data must remain visibly separate;
4. reviewer determinations must be added only in a separate review artifact;
5. Project Owner acceptance and each `AR-B-007`, `AR-B-008`, and `AR-B-009`
   closure decision remain separate;
6. no result can activate C03 automatically.

## 13. Execution-Package Review Questions

| ID | Question |
| --- | --- |
| `C03-WP008-EPQ-001` | Does the Package bind all adopted Plan, preparation, environment, review, and admission baselines by exact SHA? |
| `C03-WP008-EPQ-002` | Is the future harness path, language, dependency boundary, and prohibited capability set exact? |
| `C03-WP008-EPQ-003` | Must the harness verify every identity before subject import or evidence-directory creation? |
| `C03-WP008-EPQ-004` | Is the Python executable the sole candidate execution tool with all others excluded? |
| `C03-WP008-EPQ-005` | Is the command template closed and incapable of accepting unbound flags or paths? |
| `C03-WP008-EPQ-006` | Are the read set and prohibited discovery/traversal paths exact? |
| `C03-WP008-EPQ-007` | Is the future write root unique per run with exactly four permitted files? |
| `C03-WP008-EPQ-008` | Does preflight block before import or write on every identity, isolation, role, or content failure? |
| `C03-WP008-EPQ-009` | Are all 15 scenarios ordered, isolated, and bound to admitted fixtures? |
| `C03-WP008-EPQ-010` | Are expected and observed fields physically and semantically separated? |
| `C03-WP008-EPQ-011` | Is aggregate PASS computation prohibited in the harness? |
| `C03-WP008-EPQ-012` | Do raw evidence schemas cover identity, state, reason, write set, audit, stop, and limitation fields? |
| `C03-WP008-EPQ-013` | Are executor, author, reviewer, and Project Owner roles separated without requiring real-person identity? |
| `C03-WP008-EPQ-014` | Are all critical stop and withdrawal conditions explicit and fail closed? |
| `C03-WP008-EPQ-015` | Are raw evidence, governance materialization, review, acceptance, closure, and activation separate? |
| `C03-WP008-EPQ-016` | Does the Package prohibit Route A, OCR, case, legal, provider, network, ACOS, and Git activity? |
| `C03-WP008-EPQ-017` | Does Package materialization avoid harness, command, result, evidence-directory, or runtime creation? |
| `C03-WP008-EPQ-018` | Are every unresolved execution identity and later decision explicitly blocking? |

## 14. Execution-Package Acceptance Gates

| ID | Gate |
| --- | --- |
| `C03-WP008-EPG-001` | Fixed governing lineage is complete and exact |
| `C03-WP008-EPG-002` | Future harness contract is closed and standard-library-only |
| `C03-WP008-EPG-003` | Tool allowlist contains only exact Python and excludes package/external tools |
| `C03-WP008-EPG-004` | Command template and all placeholders require later exact binding |
| `C03-WP008-EPG-005` | Read set and write set are exact and closed |
| `C03-WP008-EPG-006` | Ten preflight gates stop before import or write |
| `C03-WP008-EPG-007` | Fifteen admitted scenarios are ordered and isolated |
| `C03-WP008-EPG-008` | Expected and observed evidence cannot be merged or prefilled |
| `C03-WP008-EPG-009` | Raw scenario, audit/revocation, and defect schemas are complete |
| `C03-WP008-EPG-010` | Role independence and sole-positive-authority boundaries are preserved |
| `C03-WP008-EPG-011` | Stop, withdrawal, rerun, and no-cleanup boundaries fail closed |
| `C03-WP008-EPG-012` | Governance materialization and raw execution evidence remain separate |
| `C03-WP008-EPG-013` | No Route A, OCR, case, legal, provider, network, ACOS, or Git path is authorized |
| `C03-WP008-EPG-014` | No harness, evidence directory, result, command, or runtime action is created |
| `C03-WP008-EPG-015` | C03 readiness, blocker closure, activation, and downstream transition remain blocked |

## 15. Remaining Execution Blockers

| Blocker | Current state | Required future action |
| --- | --- | --- |
| Execution Package internal review | NOT AUTHORIZED | Fixed-SHA read-only review |
| Execution Package adoption | NOT ESTABLISHED | Project Owner decision after review |
| Harness design/materialization | NOT AUTHORIZED / NOT CREATED | Separate exact-file authorization, review, and acceptance |
| Harness SHA | NOT AVAILABLE | Fixed after accepted materialization |
| Exact run ID | NOT BOUND | Execution authorization |
| Exact full command | NOT BOUND | Execution authorization |
| Evidence run root | NOT CREATED | Execution authorization after preflight |
| Executor role instance | NOT BOUND | Execution authorization |
| Independent reviewer role instance | NOT BOUND | Result review authorization |
| Validation execution | NOT AUTHORIZED | Separate exact-scope Project Owner decision |

## 16. Resulting State

```text
WP-008 Validation Execution Package:
MATERIALIZED — PACKAGE REVIEW NOT AUTHORIZED

Validation Harness / Harness SHA:
NOT CREATED / NOT AVAILABLE

Command / Evidence Root / Executor:
NOT BOUND / NOT CREATED / NOT BOUND

Validation Execution / Runtime Observation:
NOT AUTHORIZED / NOT PERFORMED

C03-CP-E-011 / C03-CP-E-013:
NOT CREATED / NOT AUTHORIZED

Tier A Blockers Closed:
0 / 3

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next permissible action is a separate fixed-SHA internal review of this
Package. No harness materialization or validation execution follows
automatically.
