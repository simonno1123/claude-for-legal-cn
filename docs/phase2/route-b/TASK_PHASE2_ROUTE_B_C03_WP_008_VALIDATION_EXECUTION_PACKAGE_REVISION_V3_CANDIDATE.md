# Phase 2 Route B C03 WP-008 Validation Execution Package — Revision V3 Candidate

## 0. Revision Control

| Field | Value |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Package type | COMPLETE VALIDATION EXECUTION DESIGN PACKAGE V3 CANDIDATE |
| Source V2 Package SHA-256 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| Adopted limited-revision proposal SHA-256 | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` |
| Proposal adoption decision SHA-256 | `AAC1885173E2278ABCAFCA43C44777B9B2991DD3CCDB0C849E6D662344FD9D58` |
| Materialization authority | CONVERSATION-LEVEL PROJECT OWNER “授权”, following the proposal adoption and the offered preparation of limited design revision candidates |
| Authorized scope | TRUSTED IMPORT BOUNDARY AND CONCRETE INPUT BINDING ONLY, INCLUDING NECESSARY CROSS-REFERENCES |
| Activation semantics | `CAPABILITY_ONLY` |
| V3 candidate status | MATERIALIZED — FORMAL REVIEW / ADOPTION NOT AUTHORIZED OR ESTABLISHED |
| Existing harness materialization | PAUSED — PREVIOUS FIXED-SHA AUTHORIZATION NOT MIGRATED |
| Harness / concrete input binding / final Manifest / network attestation | NOT CREATED BY THIS REVISION |
| Python / subject / validation execution | NOT AUTHORIZED / NOT PERFORMED |
| Operational Tier A blockers closed | `0 / 3` — NO NEW CLOSURE |
| C03 readiness / automatic downstream transition | NOT READY / BLOCKED |

V2, its reviews and acceptance, the original Manifest Preparation Plan, and all
source/fixture bytes remain unchanged. This candidate does not supersede an
accepted baseline until a separate fixed-SHA decision says so. Previous Grade A
records do not establish this candidate's feasibility, correctness or runtime
readiness. No governance timestamp or third-party review is created here.

## 1. Limited Change Map

| Area | V3 design change | What remains unchanged |
| --- | --- | --- |
| Trusted import | Distinguish trusted bootstrap, static parsing, normal literal import, narrowly bound internal generation, and arbitrary dynamic execution | No general dynamic-code, network, process, package or path-discovery permission |
| Concrete input binding | Add a separately admitted fixed-path input binding, branch-reachability requirements, observation limits and prior comparison rules | Original fifteen fixtures, expected values, original coverage requirements and ten subject files |
| Dependency and identity references | Align this candidate with the companion Manifest Preparation Plan V2 Candidate; prevent circular hash references | No reuse of old source-materialization authority for changed design |
| Preflight and review criteria | Clarify subject-import boundary and extend existing checks to the two topics | Twelve preflight gates; original fifteen scenarios; no automatic PASS or closure |

The companion is
`docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN_REVISION_V2_CANDIDATE.md`.
It will bind this candidate's completed SHA. This file identifies the companion
by exact name, not a fabricated future hash; a later external acceptance record
must bind both completed file hashes. No file embeds its own hash or a future
receipt that would change those same bytes.

The V2 bytecode, exact-runtime-read and layered-network requirements are
retained, but their design existence is not an enforcement proof. Only necessary
reference, sequencing, review-question and state changes accompany the two
authorized topics. No subject repair or missing runtime mechanism is added.

## 2. Fixed Governing Lineage

| Baseline | SHA-256 | Required state |
| --- | --- | --- |
| Adopted Operational Validation Plan | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` | ADOPTED & SHA BOUND |
| Validation Preparation Packet | `13B73C5AABD062D322EA1E41C52B0F6A8E8D90E6E2BD8069738372384EA54A07` | ACCEPTED & SHA BOUND |
| Environment Identity Manifest | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` | ACCEPTED AS PREPARATION IDENTITY |
| Preparation Internal Review | `412FC5B32033495AFAC631581D19E6D20FC8200B04453961D875CD916083BD52` | PASS — GRADE A |
| Preparation Acceptance and Fixture Admission Decision | `0AA106618E545DF41B267EAD0CC4F28E7D15578728F123E4C5EBD7D81C967835` | 15 / 15 FIXTURES ADMITTED |

The baseline table is retained from V2. This turn verified file identities; it
does not independently re-perform earlier reviews or validate historical
authorization timing. The complete ten-subject and fifteen-fixture identity
lists remain in the fixed proposal and their original admission records.

Additional exact lineage:

| Record | SHA-256 | Qualification |
| --- | --- | --- |
| Original Manifest Preparation Plan | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` | PRESERVED SOURCE — NOT THIS COMPANION REVISION |
| Adopted revision proposal | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` | DESIGN DIRECTION, NOT EXECUTION AUTHORITY |
| Proposal adoption decision | `AAC1885173E2278ABCAFCA43C44777B9B2991DD3CCDB0C849E6D662344FD9D58` | CONVERSATION-LEVEL OWNER DIRECTION RECORDED |
| Existing future harness source authorization | `081624BE31AB69443DAF5C51FD169CEB8BC20577E22F107A48839FC06DC64B8B` | PRESERVED / NOT EXTENDED TO V3 |

Missing acceptance of the new design pair, concrete inputs or harness blocks
later execution. Existing source authority remains paused and must be separately
disposed of against the changed design; this document does not revoke, exhaust
or reissue it.

## 3. Future Harness Contract

| Field | Contract value |
| --- | --- |
| Future harness path | `validation/route_b_c03/wp_008/run_validation.py` |
| Language | Recorded Python 3.12.13, subject to fixed environment reconciliation |
| Dependencies | Exact accepted runtime Manifest; standard library and the ten subjects only |
| Harness / harness SHA | NOT CREATED / NOT ESTABLISHED |
| Bytecode | `-B` from interpreter startup; immediate verification and preservation of `sys.dont_write_bytecode = True` |
| Trusted code activity | Only the explicitly bound operations and phases in Section 6 |
| Arbitrary code / network / provider / model / API / MCP | PROHIBITED |
| Subprocess / package mutation / runtime discovery | PROHIBITED |
| Route A / OCR / case / legal / independent ACOS / Git | PROHIBITED |

The phase boundary is explicit: CPython must load a minimum trusted bootstrap
before in-process verification can run. That bootstrap is not subject code, and
its safety cannot be retrospectively established by a later audit hook.
Section 6 binds pre-process controls, bootstrap dependencies and subject import
separately; no subject may be preloaded to avoid monitoring.

Because the command retains isolated startup, project imports must not rely on
an implicitly searchable current directory. The accepted harness initialization
must bind its exact import roots and loader resolution to the accepted project
and runtime identities. Any search-path initialization is confined to that
reviewed block; no parent discovery, fallback root or later mutation is allowed.
A bound lookup root is not a directory-wide read grant: every module/file still
needs its exact Manifest identity and allowed operation.

Before subject import, the future harness must complete all twelve Section 9
gates, including fixed-SHA checks, accepted concrete-input identity, non-executing
parsing, input completeness/reachability analysis, environment restrictions and
in-process guards. Parsing a fixture for admission checks is not a scenario
call. The harness must not silently invent parameters, accept malformed bindings,
or start scenarios just because the original fixtures were admitted.

After an authorized controlled import, calls follow Section 10 in ascending
scenario order. The harness may not issue governance acceptance, blocker
closure, readiness, activation, legal correctness or downstream authority.

## 4. Python Runtime-Dependency Manifest Contract

### 4.1 Exact Future Asset

```text
validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json
```

Current state: NOT CREATED / NOT AUTHORIZED.

### 4.2 Mandatory Manifest Content

| Field | Requirement |
| --- | --- |
| Manifest ID/version | Exact immutable identity |
| Design binding | Accepted V3 Package and companion Plan file SHAs, both bound in a separate acceptance record |
| Python executable and configuration | Exact paths, bytes, SHA, version, roles and parsed `pyvenv.cfg` |
| Runtime/OS DLL set | Exact fixed loader closure, provenance and limitations |
| Standard-library set | Exact permitted sources, extensions and data; no blanket directory or bytecode/cache grant |
| Import set | Accepted harness and subject literal imports; recursive closure; separate built-in/frozen identities |
| Phase contract | T0 trust evidence references, T1 bootstrap, T2 parsing/guards, T3 imports and T4 call read sets |
| Trusted operation contract | Explicit allowed normal-load/AST/internal-generation operations and origin checks; unbound operations denied |
| Input binding | Exact fixed input-binding file SHA and its detached admission record; original fixture identities remain distinct |
| Excluded set | Denied capability modules and operations from Section 6 |
| Canonical ordering and aggregate | Companion Plan's exact entry format and SHA rules |
| Generation / review / adoption | Separate generation authority and independently recorded fixed-SHA disposition |

Every read needs both a manifested identity and a permitted purpose/phase.
Presence in the Manifest is not authority to execute arbitrary file contents,
instantiate a provider or mutate a package. Bootstrap verification must have a
trusted pre-process source; a self-hash check alone cannot establish that trust.

The future concrete-input binding is admitted before the harness is finalized.
The Manifest is generated after the accepted input and harness exist. Final run
authorization binds all completed hashes; no input or harness embeds a not-yet-
created Manifest hash as a self-dependent prerequisite.

## 5. Executable and Command Contract

### 5.1 Tool Allowlist

| Tool | SHA-256 | V3 candidate status |
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
- `<AUTHORIZED_RUN_ID>`, exact design-pair acceptance, harness SHA, input-binding
  SHA/admission, runtime-manifest SHA, network-attestation SHA, trusted-bootstrap
  evidence and exact command must be fixed by the later execution authorization;
- no additional argument, flag, environment variable, redirection, pipe,
  wildcard, shell operator, working directory, input, output, or tool is
  permitted;
- any drift blocks startup or subject import at the applicable phase, and always
  before scenario calls or evidence writes.

The exact input-binding location is a reviewed internal constant, not a new
CLI parameter:

`validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json`

No alternate path, fallback file, stdin data, environment-derived argument or
auto-discovery is permitted. This is a future candidate path, NOT CREATED and
NOT admitted by this document. The closed command above is unchanged from V2
and has not been executed.

## 6. Trusted Import and Three-Layer No-Network Contract

### 6.1 Layer 1 — Trusted Environment and Startup Boundary

Exact future network attestation:

`validation/route_b_c03/wp_008/NETWORK_ISOLATION_ATTESTATION.json`

NOT CREATED / NOT AUTHORIZED. It must retain V2's host/environment identity,
isolation-policy ID/version, enforcement source, inbound/outbound and loopback
state, DNS/proxy state, effective scope, run or validity binding, generator,
reviewer, limitations, SHA and Owner acceptance.

The environment must additionally supply independently reviewable startup
integrity/read-boundary evidence for the exact interpreter, bootstrap dependencies
and immutable accepted files. That evidence may be a separately bound part of an
accepted environment record; no new verifier, launcher, sandbox or environment
setting is implemented or authorized here. Hashing a pathname without preventing
replacement between check and use is insufficient. The later design must specify
the actual enforcement source and residual limits; unavailable assurance blocks
startup rather than being replaced with a model assertion.

A model statement, environment variable or active connection to an external
address cannot substitute for either required environment guarantee.

| Phase | Permitted scope | Required denial |
| --- | --- | --- |
| T0 — PREPROCESS_IDENTITY | Accepted environment/launcher verification before Python starts; no claim of in-process hook coverage yet | Unverified executable, root, bootstrap closure or replacement protection blocks startup |
| T1 — TRUSTED_BOOTSTRAP | Exact reviewed startup and guard dependencies only; command-level `-B` already applies | No subject preload, unlisted dependency, package mutation or network use |
| T2 — PREFLIGHT | Bound hash verification, restricted text/AST parsing, input binding checks and guard installation | No subject call/import or evidence-directory creation |
| T3 — SUBJECT_IMPORT | Ten fixed subjects and exact literal dependency closure; accepted operations in Section 6.3 only | Unbound source, loader, code generation, extra read or guard failure stops before scenarios |
| T4 — SCENARIO | Fixed accepted call bindings; already imported code; exact permitted data and evidence paths | No late imports, class/code generation, provider connection or scope widening |

### 6.2 Layer 2 — Restricted Static Parsing and Capability Scan

Before subject import, parse the accepted harness and ten subject sources only.
AST parsing produces syntax structures, not execution of the parsed program.
It must be attributable to the accepted parser and accepted bytes. The same
rule applies when a later authorized Manifest generator analyzes source without
importing it. This document does not run either parser.

Reject in harness/subject source:

- literal or dynamic imports of `ssl`, `http`, `urllib`, `ftplib`, `smtplib`,
  `imaplib`, `poplib`, `telnetlib`, `webbrowser`, `subprocess`,
  `multiprocessing`, `ctypes`, or any unmanifested module;
- subject socket imports/references; the harness's exact guard-initialization
  block is the only permitted socket import site and grants no socket use;
- arbitrary `eval`, `exec`, explicit dynamic `compile`/`__import__` calls,
  non-literal module selection, path loaders, plugins, shell/system calls,
  process creation and package discovery/mutation;
- changes to guards, audit controls, path/read/write sets or bytecode policy
  outside the exact reviewed initialization blocks.

This rule is about unauthorized operations, not a blanket prohibition of
interpreter-internal source compilation or normal module execution. No subject
source exception is added. Standard-library internal behavior is governed by
Section 6.3 and cannot be automatically whitelisted merely because it is in Lib.

### 6.3 Closed Trusted-Operation Contract

| Operation | Exact required origin and phase | Limits |
| --- | --- | --- |
| STATIC_AST_PARSE | Accepted parser, fixed input source bytes and AST-only mode during T2 | No execution of parsed input; fixture text is never code |
| NORMAL_LITERAL_IMPORT | Fixed module name, canonical path/SHA or built-in/frozen interpreter identity, loader, parent and allowed T1/T3 phase | No arbitrary dynamic name, path discovery, replacement loader or late T4 import |
| DATACLASS_INTERNAL_GENERATION | Fixed `dataclasses` source, internal call origin, accepted class/field definitions, generated content and namespace constraints during T1 or T3 only | T1 is limited to explicitly reviewed bootstrap/harness definitions; no subject preload; no field, annotation, factory, namespace or source from fixtures/CLI/environment |
| OTHER_CODE_OR_PACKAGE_ACTIVITY | No default exception | BLOCKED unless a later separately authorized design change binds it; this candidate grants none |

Local preparation observed `dataclasses._create_fn` executing generated methods
at line 473 of the standard-library file whose SHA is
`D242AEA5FCF6408B1C1F622442F88F68B9526CE1F8BD2890D74A144677C427D9`.
This is a source observation, not accepted import closure or execution evidence.
Future generation must reconcile the actual runtime SHA and exact dependency
path; a changed runtime invalidates the observation.

The accepted operation record must specify operation ID, module/source identity,
phase, accepted declaration sites, loader/caller provenance, generated-content
constraints, namespace/input constraints, enforcement method, and limitations.
For generated code without a file, do not invent a file hash. Use a reviewed
deterministic content/structure identity bound to the accepted declarations and
generator, independently reproducible under later authorization.

Module names, path prefixes, `co_filename`, `<string>`, stack text and event
names alone are insufficient proof. If the proposed mechanism cannot reliably
attribute and constrain an operation, keep the import blocked. No blanket
`exec`/`compile` exception, disabled hook interval or unguarded preload is allowed.

### 6.4 Layer 3 — In-Process Supplemental Denial

Before subject import, the exact accepted harness must:

1. install deterministic denial for `socket.socket`, `socket.create_connection`,
   `socket.socketpair` and the explicitly enumerated available construction
   helpers; helper inventory/identity must be accepted, not discovered and
   silently admitted at run time;
2. install an audit hook denying socket/process/ctypes/system operations,
   unauthorized code or package events, and non-allowlisted file access;
3. admit a compile/exec/import-related event only when it satisfies the exact
   Section 6.3 operation record; ambiguity is denial, not a permissive fallback;
4. verify the expected hook/guard and bytecode-policy state before subject import
   and at approved phase/call boundaries, fail closed on detected drift, and bind
   the independent environment protection needed for stronger integrity claims;
5. record initialization order and control state without opening a connection,
   and stop if any required control or proof is unavailable.

A Python hook or monkeypatch is not a tamper-proof security sandbox and cannot
by itself guarantee interception of every action or prevent every replacement.
Periodic identity checks do not prove no transient bypass. Environment-layer
isolation remains mandatory; claims of complete enforcement require its accepted
evidence. No execution is permitted when that evidence is unavailable.

All three layers remain necessary. A trusted code-origin exception never grants
network, filesystem, process, package or implementation authority.

## 7. Exact Read-Set Contract V3

Only the later accepted exact set may be read:

1. the Section 2 baseline records, this V3/companion design pair, their detached
   review/acceptance, proposal/adoption, input admission, harness acceptance,
   Manifest acceptance, network/startup-environment acceptance and exact run
   authorization, each enumerated by path and SHA;
2. the ten fixed subject files and fifteen originally admitted fixture files;
3. the one accepted `SCENARIO_INPUT_BINDING.json` at the Section 5 fixed path;
4. the accepted harness, exact environment configuration/executable and every
   permitted runtime Manifest entry, constrained by role and T1–T4 phase;
5. the exact accepted network attestation and startup-integrity evidence
   referenced by the run authorization.

Mandatory identity documents and bootstrap dependencies must have an externally
bound root of trust before they are used to validate later reads. The runtime
Manifest need not include a self-referential entry for its own file or future
receipts; their exact identities are bound by detached acceptance/run records.
No read permission is inferred from an unsigned document's contents.

No glob, repository enumeration, parent traversal, unresolved symlink, hidden
asset discovery, non-target read, Route A/OCR/case/evidence read, independent
ACOS read, Git metadata read or unmanifested runtime read is permitted.
Control-document paths are not scenario payloads; no actual case or external
locator is supplied to subject arguments.

## 8. Exact Write-Set Contract V3

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
all V3 preflight gates and controlled-import checks pass. It cannot overwrite or append to a prior run.

## 9. V3 Preflight Gates

All twelve gates must pass before subject import and any evidence directory is
created. T0 startup prerequisites occur before Python; T1 bootstrap is not
subject import. Reading bound text for preflight is not executing its scenario.

| ID | Required determination |
| --- | --- |
| `C03-WP008-V3-PF-001` | V3 and companion acceptance, original lineage, input admission, environment, harness, Manifest, network/startup evidence and exact authorization identities match |
| `C03-WP008-V3-PF-002` | Ten subject SHAs, fifteen original fixture SHAs and one concrete input-binding SHA match their distinct accepted records |
| `C03-WP008-V3-PF-003` | Interpreter/configuration/DLL/stdlib identities, T0 trust evidence and exact bootstrap/loader origin are bound; in-process self-check is not treated as the initial trust root |
| `C03-WP008-V3-PF-004` | Exact `-I -S -B` command, run ID, fixture/evidence roots and fixed internal input-binding location; no extra CLI, stdin, environment input or alternative path |
| `C03-WP008-V3-PF-005` | `-B` applied at startup; bytecode policy is verified at initialization and guarded boundaries; unverified immutability claims cannot substitute for environmental protection |
| `C03-WP008-V3-PF-006` | Restricted AST scan and trusted-operation records match; all fifteen bindings are complete, statically type/field consistent and traceable to reachable existing observation points |
| `C03-WP008-V3-PF-007` | Accepted environment-level network denial and startup/read-boundary evidence match the exact run with limitations resolved for required claims |
| `C03-WP008-V3-PF-008` | Socket denial and audit-hook policy are installed before subject import; trusted exceptions are narrow; no missing provenance, unguarded subject preload or hook-only sandbox claim |
| `C03-WP008-V3-PF-009` | Exact purpose/phase-limited read set and unchanged four-file write set; run directory absent |
| `C03-WP008-V3-PF-010` | Executor and independent reviewer roles are separately bound without real-person identity requirement |
| `C03-WP008-V3-PF-011` | No stale/withdrawn/revoked/superseded/kill state or unresolved critical issue; no missing observation mechanism or unreachable required comparison hidden as PASS |
| `C03-WP008-V3-PF-012` | Fixtures and concrete argument values contain no real matter, protected data, credentials, external locators, file payloads or executable input; only declared synthetic metadata |

Missing bindings or incomplete original scenario coverage block this full run.
A reduced subset is not automatically authorized. Preflight failure stops
without subject import or evidence writes; it cannot emit fabricated fifteen-row
execution results. After preflight, T3 import failure also stops before scenario
calls or evidence-directory creation.

## 10. Concrete Input Binding, Scenario and Raw Evidence Contract

### 10.1 Single Future Binding and Non-Circular Identity

Future asset: `validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json`.

This design does not create or admit that file or any concrete argument value.
Its later content must be independently reviewed and accepted before harness
finalization. It binds accepted design-pair SHAs, subject identities and original
fixture identities, but NOT the future harness, Manifest, own file SHA or own
future acceptance receipt. The harness then binds the accepted input SHA; the
Manifest binds accepted inputs/harness; a detached final run record binds all.

| Binding group | Mandatory design requirement |
| --- | --- |
| Identity | Binding ID/version, accepted design-pair identities, fifteen scenario IDs in original order, distinct original fixture path/SHA and subject path/SHA |
| Dispatch | Exact existing callable/constructor and fixed reviewed adapter mapping in harness; strings in JSON never drive arbitrary import, getattr, eval or code loading |
| Arguments | Every required argument with concrete type/value or explicit null; selected defaults explicit; typed construction order and enum mapping fixed |
| Baseline preconditions | Complete metadata needed to reach the intended branch, distinct from the one or more deliberate failure stimuli |
| Stimulus variants | Each independently required mismatch named and mapped; first early rejection cannot count as coverage of later unexercised checks |
| Policies/control inputs | Full policy identity, attempts/limits, validity/deadline/control flags and their synthetic provenance; no implied clock or real authority |
| Observation contract | Exact return/exception and measurement surface; construction, pure selection, environment enforcement and operational behavior separated |
| Oracle | Original fixture expected state/reason/write set retained; any comparison mapping fixed and accepted before results, never chosen post hoc |
| Limits and unresolved items | Explicit missing input, unreachable comparison or missing mechanism; no silent omission or automatic fallback to a weaker check |
| Isolation | Fresh per-scenario state; only the stated V-006 duplicate relation; no cleanup/rollback behavior that performs unauthorized I/O |

Exact local path/SHA references in control headers are necessary binding metadata,
not supplied case content or permission to open referenced assets. Scenario
arguments remain fictional metadata without paths, locators, protected data or
executable values. Synthetic IDs/SHAs/authority labels cannot claim genuine
asset integrity, Tier B authorization, activation or temporal lineage.

### 10.2 Original Fifteen Scenarios and Coverage Limits

The following mapping is carried verbatim from the adopted proposal's static
analysis. It specifies missing bindings and limits, NOT executed determinations.
No row is removed and no expected fixture field is rewritten.

| 原场景 | 现有候选入口/契约 | 仍需明确的具体输入 | 不能外推的结论 |
| --- | --- | --- | --- |
| C03-TA-V-001 | `evaluate_identity_gate` | configuration、envelope、expected 全字段；`packet=None`；validity、kill；确保到达 packet 检查前的前提逐项明确。 | 提前因 capability 未启用而拒绝，不能证明缺少案件绑定 authority 的分支被覆盖。 |
| C03-TA-V-002 | 身份引用构造器；`evaluate_identity_gate` | 明确哪项身份或授权字段 malformed/缺失，以及预期观察构造器拒绝还是 gate 拒绝；其余参数完整。 | 构造器失败不等于所有授权分支已验证；末尾授权引用比较的可达性限制见第 3.2 节，不能由输入绑定补救。 |
| C03-TA-V-003 | `evaluate_identity_gate` | 版本、implementation SHA、configuration SHA 的逐字段错配值；预期身份；各变体到达目标比较分支的完整前置参数。 | 单传 STALE 状态或比较一个字段不证明三个 exact-identity 比较均工作；不能把实际 BLOCKED 直接改写为 fixture 的 BLOCKED_STALE。 |
| C03-TA-V-004 | `evaluate_identity_gate` 的 matter/actor 等比较 | packet 与 envelope 的具体错配字段；原 fixture 的 matter/project/session/provider 四类边界分别绑定到真实参数与入口。 | 当前入口并未给出四类同名边界的完整参数面；未映射的 project/session/provider 要求为 NOT EVALUABLE，不能以 matter 拒绝覆盖。 |
| C03-TA-V-005 | `assert_reference_only` | 被检查的具体顶层键及无敏感值的占位方式；原 prohibited class 到该键检查的可追溯映射。 | 顶层键拒绝不证明任意值内容、嵌套对象或全部披露通道均受检测；不引入真实 credential/secret/token。 |
| C03-TA-V-006 | `IdempotencyKeyReference` 仅为引用契约 | 两次调用的完整身份和序列；需要明确现有哪个入口观察重复拒绝或副作用计数。 | 固定 subject 中未提供重复存储/判重入口；完整幂等要求当前为 NOT EVALUABLE。不得在 harness 中补建 replay cache 后替 subject 通过。 |
| C03-TA-V-007 | `evaluate_retry` | 完整 `RetryPolicyReference`、`FailureCode.TRANSIENT_FAILURE`、completed attempts、identical scope、deadline valid、kill/revoked/stale/quarantined。 | 只可观察重试资格；不执行重试、backoff、调度或以布尔输入证明实际 deadline 检测。 |
| C03-TA-V-008 | `TimeoutPolicyReference` 仅为引用契约 | 需固定 clock/起点/deadline/迟到处理的来源及实际入口；原 fixture 的 FUTURE_BINDING_REQUIRED 尚未消除。 | 当前未见计时与超时终止执行入口；完整要求为 NOT EVALUABLE，不能用预设 timeout 标记或异常构造替代。 |
| C03-TA-V-009 | `evaluate_identity_gate`；`protected_state` | 明确 configuration/packet 撤销变体、前置有效参数、模拟控制输入来源；另列边界接收前后的观察需求。 | 可观察给定撤销状态的拒绝/选择，不证明真实撤销接收时点或该时点后的实际无动作。 |
| C03-TA-V-010 | `evaluate_identity_gate`；`protected_state`；`evaluate_release` | kill 输入、release decision 明确空值及两个引用参数；隔离每个入口的前置条件。 | 给定 kill 后的结果或无 release 的拒绝，不等于完整外部 kill switch、不可自解除机制已经运行验证。 |
| C03-TA-V-011 | `RollbackReference` 仅为引用契约 | 明确当前/先前版本的合成引用、无 rollback authority，以及真正的资格判定观察入口。 | 固定 subject 未提供 rollback 资格/执行入口；不能把 `evaluate_release` 或数据构造充作回滚判定，完整要求为 NOT EVALUABLE。 |
| C03-TA-V-012 | `AuditIntegrityReference`；`build_audit_candidate` | 对照摘要、受影响引用、错配来源及检测入口必须明确。 | 记录一个 MISMATCH 或构造 audit candidate 不等于检测并隔离完整性失败；当前完整检测链为 NOT EVALUABLE。 |
| C03-TA-V-013 | `NullProviderPort.submit_reference` | 明确合成 request reference；分别定义 provider 未授权与 dependency 不可用的刺激和观察需求。 | 现有 NullProvider 的 NOT AUTHORIZED 拒绝不能证明不可用故障处理；不移除依赖、替换 Provider 或访问网络制造故障。 |
| C03-TA-V-014 | `assert_permitted_write_set` | 明确被禁止的 namespace 与非空合成引用序列；将不同禁止 namespace 分开绑定，不含实际外部路径。 | 只观察纯元数据拒绝，不实际执行 write/stage/commit/branch/push，也不宣称验证了远端 ACL。 |
| C03-TA-V-015 | `CandidateRecord` 的状态/notice/downstream 约束 | 完整合成候选元数据、具体 candidate class 与欲违反字段；分别绑定构造器检查与分类请求的观察入口。 | 状态/notice 检查不自动覆盖任意非法 class 或真实法律输出；无法映射的分类要求为 NOT EVALUABLE，不执行 legal reasoning。 |

The source observation behind the V-002 limitation remains:
`identity_gate.py` has its final authority-reference comparison after an
unconditional return. This candidate does not repair that code. An input cannot
make unreachable code reachable. Missing idempotency, timeout, rollback and
integrity observation mechanisms cannot be manufactured in the harness to pass
the corresponding subject requirement. These issues keep the full run blocked
until separately scoped, justified dispositions exist; this design grants none.

### 10.3 Expected, Observed and Comparison Separation

| Control | Mandatory future behavior |
| --- | --- |
| Scenario order | `C03-TA-V-001` through `C03-TA-V-015` ascending; no removed or silently skipped requirement |
| Isolation | Fresh state per scenario except explicit V-006 duplicate relation; no new replay/clock/rollback implementation |
| Stimulus | Loaded solely from accepted concrete bindings; not selected from expected result labels |
| Expected | Original admitted fixture and adopted Plan; amendments require their own authority |
| Observed | Unmodified raw subject return enum/reason or exception identity, with actual observation surface and provenance |
| Comparison | Separate accepted mapping and comparison outcome; no conversion of unavailable-provider behavior from an unauthorized-provider response without justified prior mapping |
| Writes | Subject attempted/effective writes and harness evidence writes distinguished; unknown is not recorded as an observed zero |
| Failure construction | `build_failure_record` and `protected_state` demonstrate only their construction/selection behavior, not independent detection of input flags |
| Audit identity | Unique immutable record ID and SHA per scenario; constructing an ID does not prove an operational audit chain |
| Stop | First critical mismatch stops later scenarios as NOT RUN; raw facts are not backfilled |
| Rerun | New run ID and separate authorization; no cleanup, repair or retry |
| Aggregate PASS | Harness calculation prohibited |

Without execution, status is NOT RUN. Missing required input is INPUT UNBOUND;
a required property with no admissible observation is NOT EVALUABLE. None means
PASS or closure. Constructor rejection cannot stand in for a gate branch;
metadata namespace denial cannot prove an OS write denial; a supplied deadline
flag cannot prove timeout detection; a supplied quarantine flag cannot prove
integrity failure. Do not issue actual prohibited operations to manufacture
those observations.

### 10.4 Unchanged Outputs and Added Provenance Fields

The four evidence files and V1 mandatory fields remain, together with these
retained V2 fields:

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

Add only provenance for the two revised topics, within those same four files:

| Raw field | Meaning |
| --- | --- |
| `trusted_operation_contract_reference` | Accepted Manifest operation-contract identity and exact applicability |
| `bootstrap_evidence_reference` | Detached trusted startup/environment evidence, not hook self-attestation |
| `trusted_phase_state` | Actual phase/guard state; T1/T2/T3/T4 distinct |
| `scenario_input_binding_sha256` | Accepted concrete binding bytes, separate from original fixture SHA |
| `stimulus_binding_id` | Exact scenario/variant/call selected before invocation |
| `comparison_rule_id` | Previously accepted expected-to-raw comparison mapping |
| `observation_surface` | Return, exception, pure metadata check or separately authorized measurement |
| `coverage_limitations` | Original requirements not demonstrated by the observation |
| `observed_provenance` | Actual source of returned values; no expectation-to-observation copying |

These are design field requirements, not materialized schemas or evidence.
Unavailable observations remain explicit and cannot be filled with expected
values, default zero counts or forged receipts.

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

Stop at the applicable startup/preflight/import/call boundary or before further write if any:

- identity, manifest, attestation, command, role, path, or authorization is
  absent, stale, mismatched, unaccepted, or ambiguous;
- unmanifested runtime read, bytecode/cache/temp write, network capability,
  socket/audit-guard failure, unauthorized dynamic code or package activity, process, provider, model,
  external service, repository, or asset appears;
- real matter, evidence, personal data, credential, secret, key, token, path,
  locator, or executable payload appears;
- expected/observed data is merged, copied, suppressed, overwritten, or
  inferred;
- duplicate effect, unauthorized retry, fallback, substitution, release,
  rollback, cleanup, rerun, or downstream transition occurs;
- audit continuity, determinism, run isolation, evidence completeness, or role
  independence cannot be established;
- input binding, callable reachability, original requirement coverage or trusted
  operation origin is unresolved, unreviewed or inconsistent;
- critical defect, kill, revocation, withdrawal, supersession, or integrity
  failure exists.

Stop authorizes no cleanup, retry, repair, rerun, rollback, acceptance, closure,
or activation.

## 13. V3 Review Questions

These are criteria only; no answers or review verdict are recorded.

| ID | Question |
| --- | --- |
| `C03-WP008-V3-RQ-001` | Are preserved baselines, adopted proposal, decision and the new candidate-pair identities exact without fabricated review or authorization hashes? |
| `C03-WP008-V3-RQ-002` | Are command-level -B, earliest possible bytecode verification and trust during bootstrap correctly separated? |
| `C03-WP008-V3-RQ-003` | Are bytecode/cache/temp writes and all writes outside the original four evidence files prohibited? |
| `C03-WP008-V3-RQ-004` | Is the exact accepted runtime-dependency Manifest still a necessary precondition? |
| `C03-WP008-V3-RQ-005` | Does the Manifest bind file/interpreter identity, loader, purpose, phase and trusted-operation origin? |
| `C03-WP008-V3-RQ-006` | Are unknown reads or imports denied at the applicable phase without pretending Python checked its own startup retrospectively? |
| `C03-WP008-V3-RQ-007` | Are the environment, static scan and in-process supplemental denial all retained? |
| `C03-WP008-V3-RQ-008` | Are environment/startup assurances independently bound rather than asserted by a model or hook? |
| `C03-WP008-V3-RQ-009` | Does AST analysis distinguish AST-only parsing and normal load from arbitrary dynamic execution? |
| `C03-WP008-V3-RQ-010` | Are guards installed before subject import, with anti-tamper limitations honestly bounded by external protection? |
| `C03-WP008-V3-RQ-011` | Is the closed -I -S -B command unchanged, with no new input-path CLI option? |
| `C03-WP008-V3-RQ-012` | Are exact read/write identities non-circular and operationally justified, including the one fixed input binding? |
| `C03-WP008-V3-RQ-013` | Do all twelve preflight gates precede subject import, scenario calls and evidence writes? |
| `C03-WP008-V3-RQ-014` | Are all fifteen original scenarios retained and independently bound to complete, reachable input variants? |
| `C03-WP008-V3-RQ-015` | Are expected, observed and comparison fields separate, without an aggregate PASS? |
| `C03-WP008-V3-RQ-016` | Are V2 raw fields preserved and new provenance fields confined to the same four files? |
| `C03-WP008-V3-RQ-017` | Are roles separated without requiring real-person information? |
| `C03-WP008-V3-RQ-018` | Do stop, no-cleanup, no-retry, stale-input and new-run-only rules remain fail closed? |
| `C03-WP008-V3-RQ-019` | Are raw evidence, adoption, blocker closure, readiness and activation separate? |
| `C03-WP008-V3-RQ-020` | Are Route A, OCR, legal/case processing, provider/network, independent ACOS and Git excluded? |
| `C03-WP008-V3-RQ-021` | Does this materialization create only design candidates, not a harness, input data, Manifest, attestation or execution evidence? |
| `C03-WP008-V3-RQ-022` | Are normal-import and dataclass-generation exceptions narrow in source, declaration, content, namespace and phase? |
| `C03-WP008-V3-RQ-023` | Are source names, stack labels and co_filename explicitly insufficient alone to prove trusted execution? |
| `C03-WP008-V3-RQ-024` | Are all concrete synthetic argument values separately admitted, without representing test labels as real authority or time? |
| `C03-WP008-V3-RQ-025` | Are incomplete mechanisms and the unreachable authority comparison preserved as open limits rather than bypassed? |
| `C03-WP008-V3-RQ-026` | Can early default rejection, failure-record construction or a supplied state flag not masquerade as full scenario coverage? |
| `C03-WP008-V3-RQ-027` | Are the unchanged fixture oracle and any justified comparison mapping fixed before execution? |
| `C03-WP008-V3-RQ-028` | Must the companion Plan and this Package be reviewed/accepted as exact completed bytes before any new operational authority? |

## 14. V3 Acceptance Gates

All twenty-four gates are pending formal review; none is a current PASS.

| ID | Gate |
| --- | --- |
| `C03-WP008-V3-G-001` | Exact source and decision lineage; old accepted bytes preserved |
| `C03-WP008-V3-G-002` | Dual bytecode protection with explicit startup trust boundary |
| `C03-WP008-V3-G-003` | Original four-file write set, no cache/temp or unauthorized side effects |
| `C03-WP008-V3-G-004` | Runtime Manifest remains separately generated, reviewed and accepted |
| `C03-WP008-V3-G-005` | Exact purpose/phase-limited read set, no hidden dependency or circular self-hash |
| `C03-WP008-V3-G-006` | All three no-network layers retained without hook-only sandbox claims |
| `C03-WP008-V3-G-007` | Guards and accepted operation policy precede subject import |
| `C03-WP008-V3-G-008` | Unchanged closed command and one internal constant input-binding path |
| `C03-WP008-V3-G-009` | Twelve preflight gates block incomplete binding or observation coverage before import |
| `C03-WP008-V3-G-010` | Fifteen scenarios retained in original order with exact reachable call bindings |
| `C03-WP008-V3-G-011` | Expected/raw observed/comparison remain separate |
| `C03-WP008-V3-G-012` | All V2 raw fields preserved; only scoped provenance fields added |
| `C03-WP008-V3-G-013` | Independent roles and Project Owner sole positive authority preserved |
| `C03-WP008-V3-G-014` | Stop, withdrawal, no-cleanup and new-run-only rules unchanged |
| `C03-WP008-V3-G-015` | Raw facts never substitute for governance or operational decisions |
| `C03-WP008-V3-G-016` | Route A/OCR/case/legal/provider/network/ACOS/Git exclusions retained |
| `C03-WP008-V3-G-017` | No execution artifact or concrete input materialized by this design revision |
| `C03-WP008-V3-G-018` | No readiness, blocker closure, activation or automatic transition |
| `C03-WP008-V3-G-019` | Normal import/AST/dataclass exceptions constrained beyond labels and filenames |
| `C03-WP008-V3-G-020` | Unbound recursive or late dynamic behavior fails closed |
| `C03-WP008-V3-G-021` | Synthetic input authority/time distinct from real facts |
| `C03-WP008-V3-G-022` | Missing mechanisms and unreachable comparisons not repaired or hidden |
| `C03-WP008-V3-G-023` | Original fixture identities/oracles and prior comparison rules preserved |
| `C03-WP008-V3-G-024` | Exact companion linkage and new-SHA review/acceptance required |

## 15. Remaining Preconditions and Limitations

| Item | Current state | Required future disposition |
| --- | --- | --- |
| V3 and companion Plan review/acceptance | NOT AUTHORIZED / NOT ESTABLISHED | Separate fixed-SHA review and Owner decision |
| Trusted operation enforcement / bootstrap integrity | NOT PROVEN / NOT IMPLEMENTED | Accepted exact mechanism and environment evidence; this design is not proof |
| Concrete scenario inputs | NOT CREATED / NOT ADMITTED | Separate exact artifact preparation, review and admission |
| Full original observation coverage | NOT ESTABLISHED | No unobservable requirement may be downgraded to PASS |
| Unreachable authority comparison | OPEN STATIC LIMITATION | Separate scope required for any code correction |
| Runtime Manifest / network attestation | NOT CREATED / NOT AUTHORIZED | Separate generation, review and acceptance |
| Harness | NOT CREATED / EXISTING MATERIALIZATION PAUSED | New exact-design disposition and source authority before materialization |
| Exact run and independent roles | NOT BOUND | Separate execution and review authority |
| Validation / operational blocker closure | NOT AUTHORIZED / NOT ESTABLISHED | Evidence-based later decisions, never inferred from design adoption |

## 16. Resulting Candidate State

```text
WP-008 Validation Execution Package V3:
DESIGN CANDIDATE MATERIALIZED — FORMAL REVIEW NOT AUTHORIZED

Source V2 / Prior Reviews and Decisions:
PRESERVED — NO RETROACTIVE ALTERATION OR AUTOMATIC EVIDENCE TRANSFER

Trusted Import / Concrete Input Binding:
DESIGN REQUIREMENTS RECORDED — NOT IMPLEMENTED OR ADMITTED

Unobservable Requirements / Unreachable Authority Comparison:
OPEN — NOT RESOLVED BY THIS REVISION

Harness / Scenario Input Binding / Runtime Manifest / Network Attestation:
NOT CREATED BY THIS REVISION

Validation Execution / Raw Evidence / E-011 / E-013:
NOT AUTHORIZED / NOT CREATED

Operational Tier A Blockers Closed:
0 / 3 — NO NEW CLOSURE

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next eligible step is a separately authorized read-only review of the exact
candidate pair. Source materialization, concrete input admission, environment
changes or operational validation do not follow automatically.
