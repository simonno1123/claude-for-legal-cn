# Phase 2 Route B C03 WP-008 Validation Execution Package — Revision V2

## 0. Revision Control

| Field | Value |
| --- | --- |
| Package type | COMPLETE VALIDATION EXECUTION DESIGN PACKAGE V2 |
| Source Package SHA-256 | `CE08ABFBA7742CC6A5CCAFD34B2D9A5FF236296F2BE6120AD04CF25ABAC9EC9F` |
| Source internal review SHA-256 | `88C1F6B55D22DB5B054C5284E7DAB26BCADEE745BF92A2A0C7341F409780FD68` |
| Limited-revision authorization SHA-256 | `A4E964CB3E5BA08E40A322C2AF8881004F3282618C03256C0E535E46035FD641` |
| Authorized defects | `C03-WP008-EP-B-001`, `C03-WP008-EP-B-002`, `C03-WP008-EP-B-003` |
| Activation semantics | `CAPABILITY_ONLY` |
| V2 status | **MATERIALIZED — INTERNAL RE-REVIEW NOT AUTHORIZED** |
| Harness/runtime manifest/network attestation | NOT CREATED / NOT AUTHORIZED |
| Command or validation execution | NOT AUTHORIZED / NOT PERFORMED |
| Raw evidence / `E-011` / `E-013` | NOT CREATED / NOT AUTHORIZED |
| Tier A blockers closed | `0 / 3` |
| C03 activation readiness | NOT READY |
| Automatic downstream transition | BLOCKED |

V1 remains historical and non-adopted. V2 is a complete superseding candidate
for review only and cannot close its own defects or authorize execution.

## 1. Authorized Defect Corrections

| Defect ID | V2 correction | Resulting control |
| --- | --- | --- |
| `C03-WP008-EP-B-001` | Command adds `-B`; harness must set `sys.dont_write_bytecode = True` before any import | Bytecode/cache writes are prohibited by command and runtime invariant |
| `C03-WP008-EP-B-002` | Exact future Python runtime-dependency manifest is mandatory, separately materialized, reviewed, accepted, and SHA-bound | Standard-library and runtime DLL read set must be complete before execution |
| `C03-WP008-EP-B-003` | Exact subject capability scan, harness socket denial, Python audit hook, and environment network-denial attestation are mandatory | Network denial becomes layered, enforceable, and reviewable |

No other scope, scenario, output, role, or downstream boundary is expanded.

## 2. Fixed Governing Lineage

| Baseline | SHA-256 | Required state |
| --- | --- | --- |
| Adopted Operational Validation Plan | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` | ADOPTED & SHA BOUND |
| Validation Preparation Packet | `13B73C5AABD062D322EA1E41C52B0F6A8E8D90E6E2BD8069738372384EA54A07` | ACCEPTED & SHA BOUND |
| Environment Identity Manifest | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` | ACCEPTED AS PREPARATION IDENTITY |
| Preparation Internal Review | `412FC5B32033495AFAC631581D19E6D20FC8200B04453961D875CD916083BD52` | PASS — GRADE A |
| Preparation Acceptance and Fixture Admission Decision | `0AA106618E545DF41B267EAD0CC4F28E7D15578728F123E4C5EBD7D81C967835` | 15 / 15 FIXTURES ADMITTED |

Any mismatch, withdrawal, supersession, revocation, kill state, or unbound V2
dependency blocks harness materialization and execution.

## 3. Future Harness Contract

| Field | Contract value |
| --- | --- |
| Future harness path | `validation/route_b_c03/wp_008/run_validation.py` |
| Language | Python 3.12.13 |
| Dependencies | Accepted Python runtime manifest plus standard library only |
| Harness state | NOT CREATED / NOT AUTHORIZED |
| Harness SHA | NOT AVAILABLE — MUST BE FIXED, REVIEWED, AND ACCEPTED |
| Bytecode | PROHIBITED BY `-B` AND `sys.dont_write_bytecode = True` |
| Network | PROHIBITED BY THREE-LAYER CONTROL IN SECTION 6 |
| Provider/model/API/MCP | PROHIBITED |
| Subprocess/dynamic execution/package mutation | PROHIBITED |
| Repository discovery or traversal | PROHIBITED |
| Route A/OCR/case/legal/ACOS/Git access | PROHIBITED |

Before importing any subject module, the future harness must:

1. set `sys.dont_write_bytecode = True` and verify it remains true;
2. verify its own exact accepted SHA;
3. verify every baseline, subject, environment, fixture, runtime-dependency
   manifest, and network-attestation SHA;
4. perform the exact pre-import AST/import-capability scan in Section 6;
5. install socket denial and Python audit-hook controls in Section 6;
6. verify the full command, run ID, role bindings, read set, write set, and
   execution authorization;
7. reject every unlisted argument, input, path, environment variable, module,
   tool, fixture, scenario, and output;
8. execute scenarios in fixed ascending order with isolated state;
9. keep expected and observed fields separate;
10. stop on the first critical mismatch without cleanup, retry, or rerun.

The harness cannot determine governance acceptance, blocker closure, readiness,
activation, legal correctness, or downstream authority.

## 4. Python Runtime-Dependency Manifest Contract

### 4.1 Exact Future Asset

```text
validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json
```

Current state: **NOT CREATED / NOT AUTHORIZED**.

### 4.2 Mandatory Manifest Content

| Field | Requirement |
| --- | --- |
| Manifest ID/version | Exact immutable identity |
| Python executable | Exact path, bytes, SHA-256, version, and role |
| `pyvenv.cfg` | Exact path, bytes, SHA-256, and parsed configuration |
| Runtime DLL set | Every Python/runtime DLL expected to load, with path, bytes, SHA-256, and role |
| Standard-library set | Every standard-library source, bytecode, extension, and data file expected to be read, with path, bytes, SHA-256, and role |
| Harness import set | Closed allowed module list derived from accepted harness AST |
| Subject import set | Closed allowed module list derived from ten fixed subject files |
| Excluded module set | Exact denied capability modules from Section 6 |
| Canonical ordering | UTF-8, normalized forward-slash paths, case-preserved, lexicographically sorted |
| Aggregate SHA | SHA-256 of the canonical ordered entry stream |
| Generation authority | Exact separate authorization and generator identity |
| Review/adoption | Exact review SHA and Project Owner acceptance decision |

Every runtime or standard-library read must be present in the accepted
manifest. Unknown, additional, missing, changed, or dynamically resolved reads
block before subject import. Presence in the manifest grants read authority only
for the exact run and does not authorize package mutation or arbitrary imports.

## 5. Executable and Command Contract

### 5.1 Tool Allowlist

| Tool | SHA-256 | V2 status |
| --- | --- | --- |
| `.venv-validation/Scripts/python.exe` | `560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E` | Sole future candidate tool; NOT YET AUTHORIZED |
| `.venv-validation/Scripts/jq.exe` | `23CB60A1354EED6BCC8D9B9735E8C7B388CD1FDCB75726B93BC299EF22DD9334` | EXCLUDED |
| `.venv-validation/Scripts/jsonschema.exe` | `EE056533C215CD97187298826AD70B68DBC80C2E6881D0494F0494A12B3349A5` | EXCLUDED |
| `.venv-validation/Scripts/pip.exe` | `7DE9B91EA7C840110BE6ADEC48DEECD3ACC57D568C51252FC7CEA00710525F14` | PROHIBITED |

### 5.2 Corrected Closed Command Template

```text
.venv-validation/Scripts/python.exe -I -S -B validation/route_b_c03/wp_008/run_validation.py --run-id <AUTHORIZED_RUN_ID> --fixture-root validation/route_b_c03/wp_008/fixtures --evidence-root validation/route_b_c03/wp_008/evidence/<AUTHORIZED_RUN_ID>
```

Mandatory rules:

- `-I`, `-S`, and `-B` are indivisible and mandatory;
- `<AUTHORIZED_RUN_ID>`, the harness SHA, runtime-manifest SHA,
  network-attestation SHA, and exact full command must be fixed by the later
  execution authorization;
- no additional argument, flag, environment variable, redirection, pipe,
  wildcard, shell operator, working directory, input, output, or tool is
  permitted;
- any drift blocks execution before import or write.

This template is recorded only and has not been executed.

## 6. Three-Layer No-Network Contract

### 6.1 Layer 1 — Execution-Environment Attestation

Exact future asset:

```text
validation/route_b_c03/wp_008/NETWORK_ISOLATION_ATTESTATION.json
```

Current state: **NOT CREATED / NOT AUTHORIZED**.

It must bind the host/environment identity, isolation-policy ID/version,
enforcement source, outbound and inbound network state, loopback treatment,
DNS/proxy state, effective scope, start/expiry or run binding, generator,
reviewer, limitations, SHA-256, and Project Owner acceptance decision.

A model statement, environment variable, unsupported assertion, or active call
to an external address cannot substitute for the attestation.

### 6.2 Layer 2 — Pre-Import AST and Capability Scan

Before subject import, the future harness must parse its own accepted source
and all ten subject files as text/AST and reject:

- imports or dynamic loads of `ssl`, `http`, `urllib`, `ftplib`, `smtplib`,
  `imaplib`, `poplib`, `telnetlib`, `webbrowser`, `subprocess`,
  `multiprocessing`, `ctypes`, or any non-manifest module;
- subject imports of `socket` or calls/references capable of creating or using
  a socket;
- `eval`, `exec`, `compile`, `__import__`, dynamic module loading, shell/system
  calls, process creation, package loading, or path-based code discovery;
- code that changes `sys.dont_write_bytecode`, network guards, audit hooks,
  allowed paths, or the exact write set.

The harness may import `socket` only in its fixed, independently reviewed guard
initialization block. No other harness or subject use is permitted.

### 6.3 Layer 3 — In-Process Runtime Denial

Before subject import, the future harness must:

1. replace `socket.socket`, `socket.create_connection`, `socket.socketpair`,
   and every available socket-construction helper with deterministic denial
   functions;
2. register a Python audit hook that raises a terminal validation exception on
   `socket.*`, `subprocess.*`, `ctypes.*`, `os.system`, dynamic-code, package,
   or non-allowlisted file-access events;
3. prevent later replacement/removal of the denial functions and audit hook;
4. record guard identity, initialization order, and success in preflight raw
   state without opening a network connection;
5. stop before subject import if any guard or audit hook cannot be established.

The environment attestation, static scan, and runtime denial must all pass.
None can waive or replace another.

## 7. Exact Read-Set Contract V2

The future read set consists only of:

1. fixed governing documents in Section 2 plus V2, its re-review, adoption,
   runtime-manifest acceptance, network-attestation acceptance, harness
   acceptance, and exact execution authorization;
2. ten subject files bound in the adopted Plan;
3. fifteen admitted fixtures;
4. exact environment configuration and executable files;
5. exact accepted harness;
6. every and only entry in the accepted Python runtime-dependency manifest;
7. exact accepted network-isolation attestation.

No glob, repository-wide enumeration, parent/symlink traversal, hidden asset
discovery, non-target read, Route A/OCR/case/evidence read, independent ACOS
read, Git metadata read, or unmanifested runtime read is permitted.

## 8. Exact Write-Set Contract V2

For one later-authorized run, the only permitted write root is:

```text
validation/route_b_c03/wp_008/evidence/<AUTHORIZED_RUN_ID>/
```

The only permitted files are:

| File | Purpose |
| --- | --- |
| `run_manifest.json` | Exact run and control identities |
| `scenario_results.jsonl` | Expected/observed scenario records |
| `audit_revocation_results.jsonl` | Audit, revocation, kill, rollback, integrity, and write-set observations |
| `defect_register.json` | Closed defect register or explicit empty register |

The command-level `-B` flag and pre-import
`sys.dont_write_bytecode = True` must both remain active. `.pyc`,
`__pycache__`, temporary, cache, log, telemetry, crash, coverage, trace,
package, Git, upstream, ACOS, or any other write is prohibited.

The future run directory must be absent before preflight and created only after
all V2 preflight gates pass. It cannot overwrite or append to a prior run.

## 9. V2 Preflight Gates

All rows must pass before subject import or evidence-directory creation.

| ID | Required determination |
| --- | --- |
| `C03-WP008-V2-PF-001` | V2, Plan, preparation, environment, review, admission, runtime manifest, network attestation, harness, and execution authorization SHAs match |
| `C03-WP008-V2-PF-002` | Ten subject SHAs and fifteen fixture SHAs match |
| `C03-WP008-V2-PF-003` | Python executable, `pyvenv.cfg`, runtime DLL, and standard-library manifest entries match |
| `C03-WP008-V2-PF-004` | Full command contains exact `-I -S -B`, run ID, fixture root, evidence root, and no additional input |
| `C03-WP008-V2-PF-005` | `sys.dont_write_bytecode` is true before every import and cannot be changed |
| `C03-WP008-V2-PF-006` | Exact subject and harness AST/capability scan passes |
| `C03-WP008-V2-PF-007` | Accepted environment network-denial attestation matches the exact run |
| `C03-WP008-V2-PF-008` | Socket denial functions and Python audit hook are installed before subject import |
| `C03-WP008-V2-PF-009` | Exact read/write sets match; evidence run directory is absent |
| `C03-WP008-V2-PF-010` | Executor and independent reviewer roles are separately bound with no conflict |
| `C03-WP008-V2-PF-011` | No stale, withdrawn, revoked, superseded, kill, or unresolved critical-defect state applies |
| `C03-WP008-V2-PF-012` | Fixtures contain no real matter, protected data, credentials, paths, locators, or executable payloads |

Any failure stops before import, fixture use, or write.

## 10. Scenario and Raw Evidence Contract

| Control | Mandatory future behavior |
| --- | --- |
| Scenario order | `C03-TA-V-001` through `C03-TA-V-015` ascending |
| Isolation | Fresh state per scenario except explicit V-006 duplicate relation |
| Expected values | Loaded from accepted fixture and adopted Plan |
| Observed values | Captured independently; never copied or inferred from expected values |
| Write set | Captured and compared to exact permitted/prohibited sets |
| Audit identity | Unique immutable record ID and SHA per scenario |
| Stop | First critical mismatch stops later rows as NOT RUN |
| Rerun | New run ID and separate authorization required |
| Aggregate PASS | Harness calculation prohibited |

Future raw schemas remain the four files and mandatory fields defined by V1,
with the following V2 additions to `run_manifest.json` and every dependent raw
record:

```text
runtime_dependency_manifest_sha256
runtime_dependency_aggregate_sha256
network_isolation_attestation_sha256
network_isolation_policy_id
ast_capability_scan_state
socket_denial_guard_state
python_audit_hook_state
dont_write_bytecode_state
command_flags
unmanifested_read_count
prohibited_write_count
```

## 11. Role and Governance Separation

| Role ID | Responsibility | Binding state |
| --- | --- | --- |
| `C03-WP008-EXECUTOR` | One exact run and raw-evidence attestation | NOT BOUND |
| `C03-WP008-IMPLEMENTATION-AUTHOR` | Explain design; cannot execute or review own correction | ROLE DEFINED |
| `C03-WP008-INTERNAL-REVIEWER` | Independently review raw evidence | NOT BOUND |
| `C03-WP008-PROJECT-OWNER` | Sole positive authority | CONVERSATION-LEVEL ROLE |

Stable role identities are sufficient; real-person names are not required.
Executor and reviewer must be different task/session roles. Raw evidence,
governance materialization, review, acceptance, three blocker-closure decisions,
readiness, and activation remain separate.

## 12. Stop, Withdrawal, and Staleness Controls

Stop before import or further write if any:

- identity, manifest, attestation, command, role, path, or authorization is
  absent, stale, mismatched, unaccepted, or ambiguous;
- unmanifested runtime read, bytecode/cache/temp write, network capability,
  socket/audit-guard failure, dynamic code, process, package, provider, model,
  external service, repository, or asset appears;
- real matter, evidence, personal data, credential, secret, key, token, path,
  locator, or executable payload appears;
- expected/observed data is merged, copied, suppressed, overwritten, or
  inferred;
- duplicate effect, unauthorized retry, fallback, substitution, release,
  rollback, cleanup, rerun, or downstream transition occurs;
- audit continuity, determinism, run isolation, evidence completeness, or role
  independence cannot be established;
- critical defect, kill, revocation, withdrawal, supersession, or integrity
  failure exists.

Stop authorizes no cleanup, retry, repair, rerun, rollback, acceptance, closure,
or activation.

## 13. V2 Review Questions

| ID | Question |
| --- | --- |
| `C03-WP008-V2-RQ-001` | Does V2 bind source, review, authorization, and five governing baselines by exact SHA? |
| `C03-WP008-V2-RQ-002` | Is `C03-WP008-EP-B-001` corrected by both `-B` and `sys.dont_write_bytecode`? |
| `C03-WP008-V2-RQ-003` | Is every bytecode, cache, temporary, and non-evidence write prohibited? |
| `C03-WP008-V2-RQ-004` | Is `C03-WP008-EP-B-002` corrected by an exact accepted runtime-dependency manifest gate? |
| `C03-WP008-V2-RQ-005` | Does the runtime manifest cover executable, configuration, DLL, standard-library, and import identities? |
| `C03-WP008-V2-RQ-006` | Are unknown or unmanifested reads blocked before subject import? |
| `C03-WP008-V2-RQ-007` | Is `C03-WP008-EP-B-003` corrected through three independent no-network layers? |
| `C03-WP008-V2-RQ-008` | Is the environment attestation exact, reviewable, run-bound, and non-model-generated? |
| `C03-WP008-V2-RQ-009` | Does the AST scan deny network, process, ctypes, dynamic-code, and non-manifest capabilities? |
| `C03-WP008-V2-RQ-010` | Are socket denial and the audit hook installed before subject import and protected from replacement? |
| `C03-WP008-V2-RQ-011` | Does the corrected command remain closed and contain `-I -S -B` exactly? |
| `C03-WP008-V2-RQ-012` | Are the read and write sets internally realizable after the three corrections? |
| `C03-WP008-V2-RQ-013` | Do all twelve preflight gates run before import or write? |
| `C03-WP008-V2-RQ-014` | Are all fifteen admitted scenarios ordered and isolated? |
| `C03-WP008-V2-RQ-015` | Are expected and observed evidence fields kept separate and aggregate PASS prohibited? |
| `C03-WP008-V2-RQ-016` | Do raw records include all V2 runtime and network control identities? |
| `C03-WP008-V2-RQ-017` | Are executor, reviewer, author, and Project Owner roles separated without real-person requirement? |
| `C03-WP008-V2-RQ-018` | Are stop, withdrawal, no-cleanup, and new-run-only rerun rules fail closed? |
| `C03-WP008-V2-RQ-019` | Are raw evidence, governance materialization, review, acceptance, closure, readiness, and activation separate? |
| `C03-WP008-V2-RQ-020` | Does V2 prohibit Route A, OCR, case, legal, provider, network, ACOS, and Git activity? |
| `C03-WP008-V2-RQ-021` | Did V2 materialization create no harness, runtime manifest, attestation, command execution, evidence, `E-011`, or `E-013`? |

## 14. V2 Acceptance Gates

| ID | Gate |
| --- | --- |
| `C03-WP008-V2-G-001` | Fixed source/review/authorization and governing lineage is complete |
| `C03-WP008-V2-G-002` | Bytecode control is dual and command-enforced |
| `C03-WP008-V2-G-003` | Exact write set excludes cache, temp, logs, telemetry, and side effects |
| `C03-WP008-V2-G-004` | Runtime-dependency manifest contract is complete and separately gated |
| `C03-WP008-V2-G-005` | Exact read set includes only accepted manifest entries |
| `C03-WP008-V2-G-006` | Network isolation uses accepted environment, static scan, and runtime denial layers |
| `C03-WP008-V2-G-007` | Socket guards and Python audit hook precede subject import |
| `C03-WP008-V2-G-008` | Closed command contains exact `-I -S -B` and later-bound identities |
| `C03-WP008-V2-G-009` | Twelve preflight gates stop before import or write |
| `C03-WP008-V2-G-010` | Fifteen admitted scenarios remain ordered and isolated |
| `C03-WP008-V2-G-011` | Expected and observed evidence remain separate |
| `C03-WP008-V2-G-012` | V2 raw control fields are complete |
| `C03-WP008-V2-G-013` | Role independence and sole-positive-authority boundaries are preserved |
| `C03-WP008-V2-G-014` | Stop, withdrawal, no-cleanup, and rerun rules fail closed |
| `C03-WP008-V2-G-015` | Raw evidence and governance decisions remain separate |
| `C03-WP008-V2-G-016` | Route A, OCR, case, legal, provider, network, ACOS, and Git paths remain prohibited |
| `C03-WP008-V2-G-017` | No harness, manifest, attestation, command, evidence, or runtime action was created |
| `C03-WP008-V2-G-018` | C03 readiness, blocker closure, activation, and downstream transition remain blocked |

## 15. Remaining Execution Blockers

| Blocker | Current state | Required future action |
| --- | --- | --- |
| V2 internal re-review | NOT AUTHORIZED | Exact-SHA read-only review |
| V2 adoption | NOT ESTABLISHED | Project Owner decision after re-review |
| Python runtime-dependency manifest | NOT CREATED / NOT AUTHORIZED | Separate materialization, review, and acceptance |
| Network-isolation attestation | NOT CREATED / NOT AUTHORIZED | Separate materialization, review, and acceptance |
| Harness | NOT CREATED / NOT AUTHORIZED | Separate materialization, review, and acceptance |
| Exact run ID/full command/evidence root | NOT BOUND | Execution authorization |
| Executor and independent reviewer instances | NOT BOUND | Execution/review authorizations |
| Validation execution | NOT AUTHORIZED | Separate exact-scope Project Owner decision |

## 16. Resulting State

```text
WP-008 Validation Execution Package V1:
HISTORICAL / NON-ADOPTED / SUPERSEDED CANDIDATE

WP-008 Validation Execution Package V2:
MATERIALIZED — INTERNAL RE-REVIEW NOT AUTHORIZED

Original Blocking Defects Addressed by Design:
3 / 3 — CLOSURE REQUIRES RE-REVIEW

Runtime Manifest / Network Attestation / Harness:
NOT CREATED / NOT AUTHORIZED

Validation Execution / Raw Evidence / E-011 / E-013:
NOT AUTHORIZED / NOT CREATED

Tier A Blockers Closed:
0 / 3

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next permissible action is a separate fixed-SHA internal re-review of V2.
No later asset or action follows automatically.
