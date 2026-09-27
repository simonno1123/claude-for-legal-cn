# Phase 2 Route B C03 WP-008 Python Runtime Dependency Manifest Preparation Plan — Revision V2 Candidate

## 0. Plan Revision Control

| Field | Value |
| --- | --- |
| Project | `claude-for-legal-cn` |
| Plan type | DOCUMENT-ONLY MANIFEST PREPARATION DESIGN — REVISION V2 CANDIDATE |
| Original Preparation Plan SHA-256 | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` |
| Preserved source Execution Package V2 SHA-256 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| Paired Execution Package V3 Candidate | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V3_CANDIDATE.md` |
| Paired V3 Candidate SHA-256 | `499D4A8391C67896229524F67CBD736C8701AF04BA7698726AF6E12746803E7E` |
| Adopted limited-revision proposal SHA-256 | `AC90F5DA143256FBC4F9409F0130FCB11D187E97DA550C72931B9209C3E71516` |
| Proposal adoption decision SHA-256 | `AAC1885173E2278ABCAFCA43C44777B9B2991DD3CCDB0C849E6D662344FD9D58` |
| Current materialization authority | CONVERSATION-LEVEL PROJECT OWNER “授权” FOR LIMITED DESIGN REVISION CANDIDATES |
| Scope | TRUSTED IMPORT BOUNDARY / CONCRETE INPUT BINDING / NECESSARY CROSS-REFERENCES ONLY |
| Activation semantics | `CAPABILITY_ONLY` |
| Plan V2 candidate status | MATERIALIZED — FORMAL REVIEW / ADOPTION NOT AUTHORIZED OR ESTABLISHED |
| Final Manifest / concrete binding / harness | NOT CREATED BY THIS REVISION |
| Python / import / validation execution | NOT AUTHORIZED / NOT PERFORMED |
| Automatic downstream transition | BLOCKED |

The original Plan and accepted records remain unchanged. Old review results do
not transfer to this candidate. Its exact companion hash is recorded above;
a later detached acceptance record must bind both completed candidate hashes.
Neither document contains its own hash or a future receipt that changes the
bytes being accepted. The proposal adoption accepted direction only; the current
user message authorizes these design candidates, not technical review or use.

## 1. Purpose and Limited Boundary

This candidate defines the design for later generation of:

`validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`

The Manifest remains a fixed-file, purpose- and phase-limited read contract for
one accepted WP-008 harness, ten subjects and admitted metadata inputs. It is
not a package lockfile, installation instruction, general executable allowlist,
network-isolation proof, validation result or runtime approval.

| Limited revision | Contract effect |
| --- | --- |
| Trusted import origin/phase | Separate bootstrap, parser, normal import and narrowly accepted internal code generation; no arbitrary dynamic execution |
| Concrete input binding | Require one separately admitted `SCENARIO_INPUT_BINDING.json`, distinct from the original fifteen fixtures |
| Necessary references/sequencing | Bind the V3/Plan V2 pair, accepted input, then harness and Manifest without circular future hashes |
| Necessary provenance fields | Extend import/phase/read identity and detached receipt semantics; no new runtime output or tool |

Existing root integrity, file hashes, static generation, deny lists, independent
review, exact-write and no-execution boundaries are retained. Field adjustments
below express only the two adopted topics. No subject, fixture, environment,
source authorization, runtime schema file or separate ACOS project is changed.

## 2. Sequencing and Non-Circular Identity

| Stage | Required separately governed action | Current candidate state |
| --- | --- | --- |
| RDM-V2-01 | Materialize V3 Package and this Plan V2 candidate | DESIGN CANDIDATES ONLY |
| RDM-V2-02 | Independently review both completed fixed SHAs and obtain Owner adoption | NOT AUTHORIZED / NOT ESTABLISHED |
| RDM-V2-03 | Prepare, review and admit the fixed concrete input binding against original fixture and subject identities | NOT AUTHORIZED / NOT CREATED |
| RDM-V2-04 | Resolve required observation/reachability limitations without hidden scope reduction; separately authorize any out-of-scope code change | OPEN / NO REPAIR AUTHORITY |
| RDM-V2-05 | Obtain exact-design harness source authority, then materialize/review/accept source without execution | EXISTING SOURCE AUTHORITY PAUSED / NOT MIGRATED |
| RDM-V2-06 | Authorize static Manifest generation with accepted input, harness, runtime roots and origin-policy evidence | NOT AUTHORIZED |
| RDM-V2-07 | Generate one new Manifest candidate and compute its file SHA | NOT AUTHORIZED / BLOCKED |
| RDM-V2-08 | Review exact file/operation/input closure and obtain detached fixed-SHA acceptance | NOT AUTHORIZED / NOT ESTABLISHED |
| RDM-V2-09 | Establish separately accepted environment/startup/network assurances and exact run authority | BLOCKED |

Source-only design work is not an actual import. The input binding contains no
future harness, Manifest, own file or own receipt hash. An accepted harness may
bind the earlier accepted input. The Manifest may then bind both. Independent
review/acceptance records and final run authorization bind the completed files
externally, never by mutating an already-hashed candidate.

The Manifest's own file, its future review/acceptance records and exact future
run authority are not self-referential entries in its hash stream; they are
independently fixed by later detached records and pre-process verification.

No wildcard, runtime-tree dump, invented future import, inferred parameter,
reduced scenario subset or prototype validation run can replace this sequence.

## 3. Preserved Source-Plan Preparation Observations

The following tables are historical observations copied from the source Plan,
NOT a new environment inventory or current accepted runtime closure. Their
counts and “observed” wording describe that earlier preparation. This revision
does not execute Python or repeat runtime-tree enumeration. Runtime volatility
remains a limitation; the later authorized generator must recalculate identities.

### 3.1 Environment Identity

The following observations were obtained without launching Python, importing a
module, executing a subject, or mutating the environment:

| Observation | Recorded value | Qualification |
| --- | --- | --- |
| Validation Python | `.venv-validation/Scripts/python.exe` | Existing candidate executable only |
| Validation Python SHA-256 | `560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E` | MATCHED TO ACCEPTED ENVIRONMENT RECORD |
| `pyvenv.cfg` SHA-256 | `7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461` | READ-ONLY RECONCILIATION |
| Recorded Python version | `3.12.13` | FROM `pyvenv.cfg` / NOT EXECUTED |
| Base runtime root | Bound by `pyvenv.cfg` | LOCAL ROOT IDENTITY / CANONICAL ENTRIES MUST USE ROOT TOKENS |
| Base non-`site-packages` standard-library candidate files | `975` files / `19,882,606` bytes | PREPARATION OBSERVATION / NOT FINAL CLOSURE |
| Base non-`site-packages` DLL or PYD candidates | `44` files / `25,543,424` bytes | PREPARATION OBSERVATION / NOT FINAL LOADED SET |
| Base `site-packages` DLL or PYD candidates | `88` files | EXCLUDED BY `-S`; NO READ AUTHORITY GRANTED |
| Validation-environment PYD candidates | `2` files under `site-packages` | EXCLUDED BY `-S`; NO READ AUTHORITY GRANTED |

Counts describe the observed trees and do not authorize all observed files.
The final Manifest must contain only the resolved fixed closure required by the
accepted harness, subjects, CPython bootstrap, extension modules, and OS loader.

### 3.2 Core Runtime Candidate Identities

| Logical identity | Bytes | SHA-256 | Current qualification |
| --- | ---: | --- | --- |
| `VENV_ROOT/Scripts/python.exe` | `262144` | `560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E` | ACCEPTED ENVIRONMENT CANDIDATE |
| `VENV_ROOT/pyvenv.cfg` | `460` | `7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461` | PREPARATION IDENTITY |
| `RUNTIME_ROOT/python.exe` | `91648` | `D8E3F0ADF246DB00358C0C4ED349CF714898178F9558FB0E944F79F5C07F8EAA` | PREPARATION OBSERVATION |
| `RUNTIME_ROOT/python3.dll` | `56320` | `2D2330CE33D1443C67B1804BBF1A561653499DD4DCF8918048747CC17D1A63C4` | PREPARATION OBSERVATION |
| `RUNTIME_ROOT/python312.dll` | `6969856` | `64A1DAD031E97F13B1A0BAC26C689D8E14A18D7DD1EAB06E17F70E22373F4EEC` | PREPARATION OBSERVATION |
| `RUNTIME_ROOT/vcruntime140.dll` | `124544` | `D5E4D9A3E835FA679450145D6A7D94E36573A509317111904D9B3712C30D9066` | PREPARATION OBSERVATION |
| `RUNTIME_ROOT/vcruntime140_1.dll` | `49792` | `1F2D41C4AA5DB0BC33EBF7B66D72943A817D7CE6CBE880502A9403823633093F` | PREPARATION OBSERVATION |

The final generator must recalculate every identity. These observations cannot
be copied into the final Manifest without exact fixed-run reconciliation.

## 4. Subject Static-Import Preparation Inventory

The source Plan recorded the following textual imports for the ten fixed
subject files, whose identities remain preserved:

| Category | Unique recorded targets | Preparation disposition |
| --- | --- | --- |
| Future directive | `__future__` | Resolve exact source file if read at runtime; otherwise record as compiler directive with no file-read grant |
| Standard library | `collections.abc`, `dataclasses`, `enum`, `hashlib`, `json`, `re`, `typing` | Resolve recursive file and extension closure after harness acceptance |
| Internal relative modules | `.capability`, `.contracts`, `.identity_gate`, `.provider_port` | Map only to the ten fixed subject files |

The static scan observed no subject import statement for `socket`, `ssl`,
`http`, `urllib`, `subprocess`, `multiprocessing`, or `ctypes`. This is a
preparation observation, not an executed capability result or final security
determination. The later accepted harness and final generator must repeat the
scan against exact SHA-bound bytes.


The proposal additionally records the local `dataclasses._create_fn` internal
generation site, with source SHA
`D242AEA5FCF6408B1C1F622442F88F68B9526CE1F8BD2890D74A144677C427D9`.
That observation motivates exact operation-origin binding; it is not runtime
execution evidence or permission to trust the whole standard library.

## 5. Root and Path Identity Model

The future Manifest must avoid ambiguous, user-dependent, or freely resolved
paths. Every entry uses one accepted root token and a normalized relative path:

| Root token | Bound source | Permitted content |
| --- | --- | --- |
| `PROJECT_ROOT` | Exact execution authorization | Accepted V3/Plan V2 identities, enumerated governance records, harness, ten subjects, fifteen fixtures and the one admitted concrete input binding only |
| `VENV_ROOT` | Accepted environment identity | Validation executable and `pyvenv.cfg` only unless separately enumerated |
| `RUNTIME_ROOT` | Accepted `pyvenv.cfg` plus environment review | CPython runtime, standard library, DLLs, PYDs, and required data files only |
| `SYSTEM_ROOT` | Separately accepted host/runtime identity | Exact OS-supplied DLL closure only |

Canonical entry paths use `ROOT_TOKEN/relative/path`, forward slashes, preserved
case, no drive letters, no `..`, no empty segments, no alternate data streams,
and no unresolved environment variables. Root-token resolution is local and
must be separately verified before subject import. Startup dependencies require
accepted T0 verification before the interpreter uses them, not retrospective
self-verification by Python.

Symlinks, junctions, mount points, and other reparse points are prohibited
unless the final Manifest records both link identity and resolved target as
separate fixed entries and an independent review accepts the mapping.


An exact normalized path and hash are insufficient if the file can be replaced
between verification and loading. The startup/environment evidence must bind
the relevant integrity enforcement and residual limits. No permission to create
a new verifier or reconfigure the environment is granted by this Plan.

## 6. Future Manifest Object Contract

The future JSON contains one canonical top-level object. This section is a
design contract only; no JSON or schema is created in this revision.

| Group | Mandatory content |
| --- | --- |
| `manifest_identity` | Manifest ID/version; accepted V3 and Plan V2 SHAs; input-binding SHA; harness/environment/subject/fixture identities; generation authorization SHA |
| `root_bindings` | Accepted root sources, exact resolver/case/reparse rules and startup-integrity provenance |
| `runtime_identity` | Interpreter implementation/version/architecture, executable/configuration/core DLL identities |
| `import_contract` | Harness/subject/recursive literal imports; exact loader/caller identities; built-in/frozen modules; explicit allowed phases and denied modules |
| `trusted_operation_contract` | Exact operation IDs, type, source or interpreter identity, declaration sites, origin/content/namespace constraints, phases, enforcement basis and limitations |
| `input_contract` | Exact one concrete-binding file, original fifteen fixture identities, subject/callable bindings, prior admission source and observation-completeness disposition |
| `entries` | Canonically ordered explicit file entries; no glob or directory grant |
| `excluded_sets` | Denied capabilities, site-packages, tools, cache/bytecode, tests and unused artifacts |
| `closure_evidence` | Static source/PE/OS resolver identities, origin-policy evidence, unresolved/duplicate counts, limitations and provenance |
| `aggregate_identity` | Entry count, byte total, category counts and file-entry aggregate SHA |
| `governance` | Generation authority/role and required independent disposition procedure; no embedded future self-dependent review, acceptance or own file SHA |

The candidate Manifest cannot truthfully embed its own later review/acceptance
SHA without a cycle or post-review mutation. Those completed dispositions are
detached records that bind the immutable Manifest file SHA, required alongside
it by the run authorization. This clarifies the original governance group and
does not waive review or acceptance.

No timestamp is used as an identity substitute; no live credential, token,
external locator, installation instruction, runtime result or aggregate
validation verdict belongs in the Manifest. Generated-code identities are
non-file operation records, not fictitious `entries`.

The trusted-operation contract is part of the full Manifest file hash. The
entry aggregate alone does not protect or certify operation/input policy; later
checks must bind the complete accepted Manifest and its detached disposition.

## 7. Explicit Entry Contract

Every file entry must contain:

| Field | Requirement |
| --- | --- |
| `ordinal` | One-based integer matching canonical order |
| `entry_id` | Stable category-prefixed identifier |
| `category` | Closed enumeration from Section 8 |
| `root_id` | One accepted root token |
| `relative_path` | Normalized, case-preserved, forward-slash path |
| `byte_length` | Exact non-negative integer |
| `sha256` | Full uppercase 64-hex SHA-256 |
| `role` | Closed file-read purpose |
| `required_by` | Exact bootstrap, harness, subject, extension, PE, or governance reference |
| `import_name` | Exact module name or `NOT_APPLICABLE` |
| `loader_kind` | `SOURCE`, `EXTENSION`, `DLL`, `DATA`, `CONFIG`, `EXECUTABLE`, or `GOVERNANCE` |
| `read_phase` | Nonempty ordered phase string using `T1`, `T2`, `T3`, `T4`; multiple phases comma-separated without spaces/duplicates in ascending order |
| `executable` | Boolean process-entrypoint flag; `true` only for the accepted validation Python; `false` is not a blanket denial/permission of module-internal execution |
| `network_capable` | Boolean classification with basis; capability does not grant use |
| `reparse_state` | `DIRECT` or accepted exact link mapping |

No field may contain `UNKNOWN`, wildcard syntax, an unresolved path, an omitted
hash, an inferred file, or a directory-only grant in an accepted Manifest.


Phase meanings are fixed by Package V3 Section 6: T1 trusted bootstrap, T2
preflight/guard setup, T3 controlled subject import, T4 scenario calls. One source
may need T2 text parsing and T3 loading; that combination must be explicit.
T0 verification is a pre-process prerequisite, not a Python read-phase grant.

File identity/read phases alone do not grant import or internal generation.
Every permitted code operation additionally needs its Section 11 origin contract.

## 8. Closed Entry Categories

| Category | Scope |
| --- | --- |
| `PYTHON_EXECUTABLE` | Exact validation executable only |
| `PYTHON_CONFIG` | Exact `pyvenv.cfg` only |
| `CPYTHON_CORE_DLL` | Exact CPython and VC runtime libraries |
| `STDLIB_SOURCE` | Resolved standard-library source file |
| `STDLIB_EXTENSION` | Resolved PYD and its owned DLL dependencies |
| `STDLIB_DATA` | Exact data file required by an accepted import |
| `OS_RUNTIME_DLL` | Exact OS-supplied PE dependency |
| `HARNESS_SOURCE` | Exact accepted harness source only |
| `SUBJECT_SOURCE` | One of ten fixed subject files |
| `GOVERNANCE_INPUT` | Exact accepted governance record needed by preflight |
| `FIXTURE_INPUT` | One of fifteen admitted fixture files |
| `SCENARIO_INPUT_BINDING` | The one separately admitted fixed-path concrete binding, no alternate file |

`site-packages`, installer artifacts, development headers, test modules,
Tk/Tcl assets, package metadata, documentation, bytecode, and caches remain
excluded under this candidate. An import dependency or a reviewer statement
cannot waive that exclusion. Any future relaxation requires a separately
authorized design change, not admission through this Manifest. `-S` remains
mandatory and cannot be waived. This prevents the source Plan's general
exception wording from overriding Package V3's closed import boundary.


The fixed binding path is
`PROJECT_ROOT/validation/route_b_c03/wp_008/SCENARIO_INPUT_BINDING.json`.
Its presence in this category is not admission or permission to create it.
It is data only and cannot supply source code, module names for runtime dispatch
or actual authority to subject code.

## 9. Deterministic Static Generation Algorithm

Only after separate authorization, a generator may:

1. verify the accepted design pair, input admission, original fifteen fixtures,
   ten subject identities, harness, environment and generation authority;
2. bind exact roots, startup/loader provenance and permitted reparse mappings;
3. parse fixed harness/subject source as AST-only text, without importing or
   executing them; parsing-related interpreter activity must itself have a
   separately reviewed trusted origin and tool boundary;
4. reject arbitrary dynamic code/imports, non-literal names, free path loaders,
   package discovery, guard mutation or any unresolvable operation;
5. resolve literal imports and recursive exact standard-library source/extension
   closure statically; distinguish ordinary source execution needed by a normal
   import from arbitrary data-driven execution;
6. enumerate exact built-in/frozen interpreter identities separately from files;
7. resolve CPython/extension PE and OS dependencies with accepted static resolvers
   and exact search order; record limitations rather than probing by execution;
8. derive required literal data reads and explicit T1–T4 entry phases;
9. map every permitted parse/import/internal-generation operation to the accepted
   Section 11 origin contract; generated artifacts are constrained by accepted
   declarations, not generated by importing subjects during this step;
10. reconcile input-binding field completeness, reachable callable mapping and
    unresolved original observation requirements against admitted evidence;
    do not execute constructors or cases to fill the gaps;
11. exclude denied modules, site-packages, unused code, tests, bytecode/cache,
    installers and package metadata; reject any unproven transitive path;
12. hash exact files, encode categories/phases canonically, compute file-entry
    totals and aggregate without hashing the Manifest into itself;
13. emit one new candidate only under exact-path creation authority, without
    overwriting a prior file; compute the complete file SHA externally; and
14. stop without an accepted/completeness/readiness claim on any unresolved
    dependency, code origin, input identity, required observation or hash.

This Plan does not execute a generator, parser or runtime probe. A generator
does not issue its own independent review, admission, acceptance or validation
outcome. Its fixed source/tool access must be separately authorized; no new
utility or agent is materialized by this candidate.

## 10. CPython Bootstrap, PE, and OS Dependency Rules

Static Python import closure alone is insufficient. The final Manifest must
also bind:

- the validation launcher and base CPython executable relationship;
- `python3.dll`, `python312.dll`, and required VC runtime files;
- every selected PYD and its runtime-owned DLL dependencies;
- every exact OS-supplied DLL resolved under the accepted host identity;
- the resolver search order and duplicate-name disposition; and
- the distinction between files present in the runtime tree and files
  actually granted to the accepted closure.

System DLL names without exact accepted root, bytes, and SHA are insufficient.
An executed process-module observation may be used only if separately
authorized as an inventory-only probe; this Plan does not authorize such a
probe. Otherwise the generator must use a separately reviewed static PE
dependency resolver and record its limitations.


The V3 T0 trust boundary applies before these components load. Required
bootstrap/verification dependencies and the integrity mechanism preventing
check-to-use replacement must have independent accepted evidence. The
in-process harness cannot retroactively protect bootstrap activity. No
runtime probe is authorized here to discover or demonstrate that protection.

Trust requirements are unmet unless a later reviewed mechanism and exact
environment evidence exist. A statement that the audit hook is installed is
not an OS/loader isolation or anti-tamper proof.

## 11. Closed Trusted Import and Capability Rules

The full contract must enumerate harness/subject/recursive imports, built-in
and frozen identities, file-backed sources, extension/PE dependencies, literal
data reads, code-generation origins and denied operations separately.

Isolated startup cannot assume the project current directory is importable.
Record the exact accepted import roots and loader resolution used by the
reviewed initialization block. A lookup root grants no directory-wide access;
every module/file and operation still requires an explicit identity. Parent
discovery, additional roots, fallback resolution and later search-path mutation
remain prohibited.

The denied set remains `ssl`, `http`, `urllib`, `ftplib`, `smtplib`,
`imaplib`, `poplib`, `telnetlib`, `webbrowser`, `subprocess`,
`multiprocessing` and `ctypes`, plus every unmanifested capability.
`socket` is permitted only for the exact independently reviewed harness guard
initialization; no subject socket access or network operation is granted.

| Operation class | Required origin and phase | Prohibited inference |
| --- | --- | --- |
| STATIC_AST_PARSE | Accepted parser identity, accepted exact source bytes, AST-only mode, T2 | Parsing is not permission to execute arbitrary code or input |
| NORMAL_LITERAL_IMPORT | Exact module identity, path/SHA or bound interpreter identity, accepted loader/parent and T1/T3 phase | Name matching or being in Lib is not sufficient trust |
| DATACLASS_INTERNAL_GENERATION | Accepted fixed generator source, internal origin, class/field declaration sites, content/namespace constraints and T1/T3 phase | No declarations, factories, annotations or executable values from fixture/CLI/environment; T1 cannot preload subjects |
| Other code/package activity | Denied by default | No general compile/exec/import exception, hidden hook suspension or T4 late loading |

An operation record must contain an operation ID, class, accepted source/module
or interpreter identity, allowed phases, declaration-site identities, origin
evidence, deterministic generated-content/structure constraints where needed,
namespace/input restrictions, enforcement method and explicit limitations.
A generated operation is not assigned a fictional filesystem SHA.

Runtime module names, `co_filename`, path prefixes, stack text and `<string>`
cannot alone establish trust. The required mechanism must prevent untrusted
data and unbound sources from acquiring an allowed operation's identity.
If the event data and external controls cannot establish those constraints,
generation/review must record an unresolved blocker, not an optimistic exception.

The audit hook/socket wrapper are supplemental in-process controls, not a
tamper-proof sandbox. Required protection against modifications, transient
bypasses or actions outside hook coverage needs independent environment evidence.
No accepted import record permits additional network, process, file write or
package activity.

An allowed dependency reaching a denied module or an unbound generation path
cannot be silently included. It stays blocked until an exact, non-capability
path is demonstrated by authorized static evidence and independently accepted.
Any change requiring source, environment or forbidden capability modification
is outside this limited revision.

Input bindings do not enlarge imports. Dispatch is a fixed reviewed mapping in
the accepted harness; data cannot name a new module or choose an arbitrary
callable. Missing callable/reachability/observation requirements keep the full
fifteen-scenario validation blocked, even if file hashes match.

## 12. Canonicalization and Aggregate SHA

Canonical entries are sorted by this tuple:

```text
(category, root_id, relative_path, entry_id)
```

Each aggregate-stream record is UTF-8 without BOM and consists of the following
fields separated by one ASCII unit separator (`0x1F`) and terminated by one LF:

```text
ordinal, entry_id, category, root_id, relative_path, byte_length, sha256,
role, required_by, import_name, loader_kind, read_phase, executable,
network_capable, reparse_state
```

The aggregate SHA-256 is calculated over the concatenated record bytes. The
Manifest file SHA-256 is separately calculated over the final canonical JSON
bytes and must not be embedded self-referentially.

Canonical JSON requirements are UTF-8 without BOM, LF line endings, two-space
indentation, lexicographically ordered object keys, array order as defined by
this Plan, no insignificant trailing whitespace, and one final LF.


The original aggregate field sequence is preserved. For `read_phase`, canonical
serialization is the nonempty ascending comma-joined subset of T1,T2,T3,T4,
without spaces or duplicates. A single phase is serialized as its token.
All other existing fields retain their declared representations.

The aggregate covers file entries only. `trusted_operation_contract`,
`input_contract` and other top-level groups are protected by the full canonical
Manifest file SHA, which must be checked as well; a matching entry aggregate
alone is not an accepted policy match. Operation records are ordered by exact
operation ID and input scenario records by original scenario ID/accepted variant
order. Duplicate IDs or ambiguity are blockers.

The concrete binding and harness do not contain the future Manifest's SHA.
The Manifest does not include its own file SHA or future review/acceptance
receipt hashes. Detached disposition/run records bind those completed identities,
preserving exact bytes without a self-referential hash cycle.

## 13. Review, Acceptance and Staleness Rules

Independent review must verify:

- completed V3/Plan V2 candidate identities and their exact paired acceptance;
- original fixture/subject identities, concrete-input identity/admission,
  accepted harness, environment, root/file and aggregate identities;
- exact import/bootstrap/PE/OS/data closure, loader/caller origin, phase and
  trusted-operation constraints, with no hook-only trust claim;
- no wildcard, directory grant, site-package, arbitrary dynamic import,
  unbound generated code, missing file hash or unknown dependency;
- consistency of original requirements, admitted argument variants, reachable
  call mapping and stated observation limits, without executing subjects as a
  shortcut to supply missing binding data;
- canonical ordering, phase encoding, entry aggregate and full file SHA;
- generator/reviewer role separation and Owner sole positive authority;
- absence of execution, network/package activity, actual input materialization
  by the design revision, evidence creation or readiness overstatement; and
- detached review/acceptance binding without self-hash or post-review mutation.

Changes to the design pair, concrete-input bytes or admission, harness, subject,
environment, interpreter, roots, resolver, loader, code-origin contract, phase
policy, denied set, entries or acceptance lineage make the dependent Manifest
stale. It cannot be silently patched or reused under another SHA.

The source Plan's acceptance and the proposal direction adoption are preserved,
not promoted into acceptance of this Plan V2 candidate. No source permission or
operational outcome automatically transfers. The unresolved authority-comparison
reachability and missing observation mechanisms remain open and out of repair
scope; adoption of a design document does not cure them.

Stable role identities are sufficient. No real-person identity information is
required to preserve separation between materializer, executor, independent
reviewer and Project Owner.

## 14. Plan V2 Review Questions

Twenty-five criteria for a later authorized review; no determinations are issued.

| ID | Question |
| --- | --- |
| `C03-WP008-RDM-V2-RQ-001` | Are original Plan, preserved V2 Package, proposal/adoption and paired V3 identities exact without claiming new reviews? |
| `C03-WP008-RDM-V2-RQ-002` | Is the order design pair, accepted concrete input, accepted harness, then Manifest non-circular? |
| `C03-WP008-RDM-V2-RQ-003` | Are preserved preparation observations clearly historical and not a current runtime inventory? |
| `C03-WP008-RDM-V2-RQ-004` | Does the exact root/reparse model prevent ambiguous path resolution and require check-to-use integrity? |
| `C03-WP008-RDM-V2-RQ-005` | Do top-level groups include exact phase/operation and input-binding identities while keeping future receipts detached? |
| `C03-WP008-RDM-V2-RQ-006` | Does each entry preserve path, bytes, SHA, role, loader and explicitly canonical read phases? |
| `C03-WP008-RDM-V2-RQ-007` | Are unknowns, placeholders, globs, directory grants and unbound paths barred from an accepted Manifest? |
| `C03-WP008-RDM-V2-RQ-008` | Are site-packages, installers, tests, bytecode/cache and unused artifacts excluded by default? |
| `C03-WP008-RDM-V2-RQ-009` | Does static generation parse accepted sources without importing/executing them or constructing test cases? |
| `C03-WP008-RDM-V2-RQ-010` | Are non-file built-in/frozen/generated identities distinct from actual file entries? |
| `C03-WP008-RDM-V2-RQ-011` | Does startup require accepted bootstrap/PE/OS evidence before Python rather than retrospective self-certification? |
| `C03-WP008-RDM-V2-RQ-012` | Do transitive denied imports or unbound internal generation fail closed? |
| `C03-WP008-RDM-V2-RQ-013` | Are canonical entries, phase encoding, policy/file identity and aggregate/file SHA boundaries reproducible? |
| `C03-WP008-RDM-V2-RQ-014` | Can the Manifest not authorize execution, mutation, network or operational PASS? |
| `C03-WP008-RDM-V2-RQ-015` | Are independent review, Owner acceptance and all new input/operation staleness dependencies mandatory? |
| `C03-WP008-RDM-V2-RQ-016` | Are stable role identities adequate without collecting real-person data? |
| `C03-WP008-RDM-V2-RQ-017` | Are unresolved sources, call reachability and observation requirements recorded as blockers rather than inferred? |
| `C03-WP008-RDM-V2-RQ-018` | Has materialization remained document-only, without a Manifest, harness, input binding or evidence? |
| `C03-WP008-RDM-V2-RQ-019` | Are Route A/OCR/case/legal/provider/network/independent ACOS/Git excluded? |
| `C03-WP008-RDM-V2-RQ-020` | Does C03 remain not ready, without new closure or automatic downstream transition? |
| `C03-WP008-RDM-V2-RQ-021` | Are AST parsing, literal loading and dataclass generation constrained by exact origin/phase and not by spoofable names alone? |
| `C03-WP008-RDM-V2-RQ-022` | Does the plan avoid presenting Python hooks as a complete sandbox or granting blanket dynamic execution? |
| `C03-WP008-RDM-V2-RQ-023` | Is the concrete binding a distinct admitted input whose metadata cannot choose arbitrary imports/callables? |
| `C03-WP008-RDM-V2-RQ-024` | Do input fields/expected values never substitute for observed behavior or missing subject mechanisms? |
| `C03-WP008-RDM-V2-RQ-025` | Are existing accepted bytes preserved and the new candidate-pair references free of self-dependent future hashes? |

## 15. Plan V2 Acceptance Gates

Twenty gates remain pending formal review; no PASS is asserted.

| ID | Gate |
| --- | --- |
| `C03-WP008-RDM-V2-G-001` | Exact original and paired candidate lineage, no historical review transfer |
| `C03-WP008-RDM-V2-G-002` | Non-circular accepted-input and accepted-harness sequencing |
| `C03-WP008-RDM-V2-G-003` | Historical observations qualified, no current closure or inventory claim |
| `C03-WP008-RDM-V2-G-004` | Exact roots/reparse/integrity constraints and trusted startup evidence |
| `C03-WP008-RDM-V2-G-005` | Complete scoped file/operation/input object groups |
| `C03-WP008-RDM-V2-G-006` | Explicit canonical read phases and closed entry categories |
| `C03-WP008-RDM-V2-G-007` | Static generation without subject import or execution |
| `C03-WP008-RDM-V2-G-008` | Exact harness/subject/recursive import and code-origin closure |
| `C03-WP008-RDM-V2-G-009` | Independent bootstrap/PE/OS evidence, not hook-only self-trust |
| `C03-WP008-RDM-V2-G-010` | Denied capabilities and unbound transitive operations cannot be admitted silently |
| `C03-WP008-RDM-V2-G-011` | Canonical entry aggregate, policy/full-file hash and detached receipts remain distinct |
| `C03-WP008-RDM-V2-G-012` | New input, phase and origin drift invalidates dependent records |
| `C03-WP008-RDM-V2-G-013` | Independent stable roles without real-person information |
| `C03-WP008-RDM-V2-G-014` | No Manifest, concrete input, harness, execution or evidence materialized |
| `C03-WP008-RDM-V2-G-015` | Route A/OCR/case/legal/provider/network/ACOS/Git boundaries retained |
| `C03-WP008-RDM-V2-G-016` | No readiness, blocker closure or automatic downstream transition |
| `C03-WP008-RDM-V2-G-017` | Narrow parse/import/dataclass exceptions; no blanket dynamic execution |
| `C03-WP008-RDM-V2-G-018` | Concrete input identity cannot supply code or arbitrary dispatch |
| `C03-WP008-RDM-V2-G-019` | Unobservable requirements and unreachable comparison remain unresolved |
| `C03-WP008-RDM-V2-G-020` | V3 and Plan V2 require separate fixed-SHA review/adoption before use |

## 16. Resulting Candidate State

```text
Runtime Dependency Manifest Preparation Plan V2:
DESIGN CANDIDATE MATERIALIZED — FORMAL REVIEW NOT AUTHORIZED

Paired V3 Package:
EXACT CANDIDATE SHA RECORDED — NOT ACCEPTED BY THIS DOCUMENT

Original Plan / Accepted Records / Subjects / Fixtures:
PRESERVED — NO HISTORICAL STATUS REWRITE

Concrete Input / Harness / Manifest:
NOT CREATED BY THIS REVISION

Trusted Import Enforcement / Complete Input Coverage:
NOT ESTABLISHED — DESIGN REQUIREMENTS ONLY

Unreachable Comparison / Missing Observation Mechanisms:
OPEN — NO SOURCE REPAIR AUTHORIZED

Python / Subject / Validation Execution:
NOT AUTHORIZED / NOT PERFORMED

Raw Evidence / E-011 / E-013:
NOT CREATED / NOT AUTHORIZED

Operational Tier A Blockers Closed:
0 / 3 — NO NEW CLOSURE

C03 Readiness / Automatic Downstream Transition:
NOT READY / BLOCKED
```

The next eligible step is a separately authorized read-only review of this
fixed-SHA Plan V2 together with the exact V3 Package. No source materialization,
input admission, runtime generation, network attestation, probe or validation
follows automatically.
