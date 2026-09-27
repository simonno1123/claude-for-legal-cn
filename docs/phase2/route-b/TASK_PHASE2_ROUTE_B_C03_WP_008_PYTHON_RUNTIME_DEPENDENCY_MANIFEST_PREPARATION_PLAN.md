# Phase 2 Route B C03 WP-008 Python Runtime Dependency Manifest Preparation Plan

## 0. Plan Control

| Field | Value |
| --- | --- |
| Plan type | DOCUMENT-ONLY RUNTIME DEPENDENCY MANIFEST PREPARATION PLAN |
| Governing V2 Package SHA-256 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| V2 internal re-review SHA-256 | `A652ABCA2DCFAC9BBEB5074860D7F7457CE353BB95A858F4BEDF30FD5B52E299` |
| V2 adoption decision SHA-256 | `9CB805082CF7D635F21605A68622A7CB9F495599B1B95B18EDD09E464BAB6560` |
| Preparation authorization SHA-256 | `C892115AA83A10F0081B2F2CF9276F9C706B29E711C69F99272573F8B979F034` |
| Environment identity manifest SHA-256 | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` |
| Activation semantics | `CAPABILITY_ONLY` |
| Plan status | **MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED** |
| Final Manifest | NOT CREATED / PRECONDITION BLOCKED |
| Harness | NOT CREATED / NOT AUTHORIZED |
| Python or validation execution | NOT AUTHORIZED / NOT PERFORMED |
| Automatic downstream transition | BLOCKED |

## 1. Purpose and Boundary

This Plan defines how a later separately authorized process may generate the
exact future asset:

```text
validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json
```

The future Manifest is a fixed-file read-authority contract for one accepted
WP-008 harness and the ten fixed Route B C03 subject files. It is not a package
lockfile, software bill of materials, installation instruction, executable
allowlist, network-isolation proof, validation result, or runtime approval.

This Plan records preparation observations and design requirements only. It
does not represent the current runtime tree, import closure, DLL closure, or OS
loader closure as complete or accepted.

## 2. Mandatory Sequencing and Circular-Dependency Resolution

The V2 Package requires the Manifest to include a closed harness import set
derived from an accepted harness AST. No harness exists. Therefore the lawful
sequence is:

| Stage | Required action | Current state |
| --- | --- | --- |
| `RDM-01` | Materialize and review this preparation Plan | PLAN MATERIALIZED / REVIEW NOT AUTHORIZED |
| `RDM-02` | Project Owner adopts the fixed-SHA Plan | NOT ESTABLISHED |
| `RDM-03` | Separately authorize, materialize, review, and accept the exact harness source without executing it | NOT AUTHORIZED |
| `RDM-04` | Separately authorize deterministic Manifest generation against the accepted harness, subjects, and environment | NOT AUTHORIZED |
| `RDM-05` | Materialize the exact Manifest JSON and calculate its file SHA | NOT AUTHORIZED / BLOCKED |
| `RDM-06` | Independently review the Manifest, entry closure, aggregate SHA, and exclusions | NOT AUTHORIZED |
| `RDM-07` | Project Owner accepts or rejects the exact Manifest SHA | NOT AUTHORIZED |
| `RDM-08` | Continue to the separately governed network-attestation and harness-execution prerequisites | BLOCKED |

No placeholder harness import set, wildcard, inferred future import, broad
standard-library directory grant, or current environment dump may substitute
for `RDM-03`.

## 3. Read-Only Preparation Observations

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

The ten fixed subject files currently expose the following unique textual
import targets:

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

## 5. Root and Path Identity Model

The future Manifest must avoid ambiguous, user-dependent, or freely resolved
paths. Every entry uses one accepted root token and a normalized relative path:

| Root token | Bound source | Permitted content |
| --- | --- | --- |
| `PROJECT_ROOT` | Exact execution authorization | V2, accepted governance records, harness, ten subjects, and fifteen fixtures only |
| `VENV_ROOT` | Accepted environment identity | Validation executable and `pyvenv.cfg` only unless separately enumerated |
| `RUNTIME_ROOT` | Accepted `pyvenv.cfg` plus environment review | CPython runtime, standard library, DLLs, PYDs, and required data files only |
| `SYSTEM_ROOT` | Separately accepted host/runtime identity | Exact OS-supplied DLL closure only |

Canonical entry paths use `ROOT_TOKEN/relative/path`, forward slashes, preserved
case, no drive letters, no `..`, no empty segments, no alternate data streams,
and no unresolved environment variables. Root-token resolution is local and
must be separately verified before any subject import.

Symlinks, junctions, mount points, and other reparse points are prohibited
unless the final Manifest records both link identity and resolved target as
separate fixed entries and an independent review accepts the mapping.

## 6. Future Manifest Object Contract

The final JSON must contain one top-level object with these mandatory groups:

| Group | Mandatory content |
| --- | --- |
| `manifest_identity` | Manifest ID, format version, V2 SHA, harness SHA, environment SHA, subject-manifest SHA, fixture-admission SHA, and generation authorization SHA |
| `root_bindings` | Root token, accepted source SHA, resolver rule, case rule, and reparse-point rule |
| `runtime_identity` | Python version, implementation, architecture, executable entry, `pyvenv.cfg` entry, and CPython DLL entries |
| `import_contract` | Harness direct imports, subject direct imports, recursive resolved imports, built-ins, frozen modules, and denied modules |
| `entries` | Canonically ordered explicit file entries with no glob or directory grant |
| `excluded_sets` | `site-packages`, denied capability modules, tools, caches, bytecode, tests, and unused extensions |
| `closure_evidence` | Static resolver version, PE resolver version, OS dependency source, unresolved count, duplicate count, and limitation record |
| `aggregate_identity` | Entry count, byte total, category counts, and aggregate SHA-256 |
| `governance` | Generator role, reviewer role, review SHA, acceptance decision SHA, state, and staleness rule |

The final JSON must not contain comments, timestamps used as identity, live
credentials, tokens, network locators, package installation instructions,
runtime results, or an aggregate validation verdict.

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
| `read_phase` | `STARTUP`, `PREFLIGHT`, `GUARD_INIT`, `SUBJECT_IMPORT`, or `SCENARIO` |
| `executable` | Boolean; `true` only for the accepted validation Python |
| `network_capable` | Boolean classification with basis; capability does not grant use |
| `reparse_state` | `DIRECT` or accepted exact link mapping |

No field may contain `UNKNOWN`, wildcard syntax, an unresolved path, an omitted
hash, an inferred file, or a directory-only grant in an accepted Manifest.

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

`site-packages`, installer artifacts, development headers, test modules,
Tk/Tcl assets, package metadata, documentation, bytecode, and caches are denied
unless an exact accepted harness import proves necessity and a separate review
approves the minimum entry. `-S` remains mandatory and cannot be waived.

## 9. Deterministic Generation Algorithm

A future separately authorized generator must perform these steps without
importing or executing the harness or subjects:

1. verify all governing SHAs, the accepted harness SHA, ten subject SHAs,
   environment SHA, and generation authorization;
2. establish the four root mappings and reject any unaccepted reparse point;
3. parse the accepted harness and ten subjects as text/AST;
4. reject dynamic imports, dynamic code, non-literal module names, path-based
   loaders, package discovery, or unresolvable import semantics;
5. derive direct import sets and resolve the recursive standard-library file
   closure from exact accepted runtime roots without importing modules;
6. distinguish built-in and frozen modules from file-backed modules and record
   non-file identities without granting fictitious file reads;
7. resolve extension-module and CPython PE imports against exact runtime and
   accepted system roots;
8. resolve required standard-library data files from literal accepted code
   references only;
9. exclude `site-packages`, denied modules, unused extensions, tests, cache,
   bytecode, installers, and package metadata;
10. hash every explicit file and calculate byte and category totals;
11. sort entries canonically and calculate the aggregate entry-stream SHA;
12. write one new Manifest candidate without overwriting any prior candidate;
13. calculate the Manifest file SHA externally; and
14. stop with no acceptance claim if any identity, import, dependency, path,
   category, or closure element is unresolved.

Generation cannot determine that the Manifest is complete, accepted, safe, or
execution-ready. Those determinations belong to later independent review and
Project Owner decision.

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

## 11. Import and Capability Closure Rules

The future import contract must separately record:

1. harness direct imports;
2. subject direct imports;
3. recursive standard-library imports;
4. built-in modules;
5. frozen modules;
6. file-backed source modules;
7. extension modules and PE dependencies;
8. literal data-file reads; and
9. denied capability modules.

The denied set must include at least `ssl`, `http`, `urllib`, `ftplib`,
`smtplib`, `imaplib`, `poplib`, `telnetlib`, `webbrowser`, `subprocess`,
`multiprocessing`, and `ctypes`. `socket` may appear only in the exact accepted
harness guard-initialization block and must remain denied to subjects.

If a recursive allowed standard-library module imports a denied capability,
the generator must not silently include it. The Manifest candidate is blocked
until the harness design is narrowed or an exact non-capability path is proven
and independently accepted.

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

## 13. Review, Acceptance, and Staleness Rules

The final Manifest cannot become governing unless an independent review verifies:

- every governing, harness, subject, environment, root, entry, and aggregate
  identity;
- exact import, bootstrap, extension, PE, OS, data, and exclusion closure;
- no wildcard, directory grant, site-package, dynamic import, denied module,
  unbound file, missing hash, or unresolved dependency;
- canonical ordering, aggregate-stream reproduction, and Manifest file SHA;
- reviewer independence and Project Owner sole-positive-authority boundaries;
  and
- absence of execution, network access, package mutation, evidence creation,
  or readiness overstatement.

Any change to the harness, subject, environment, Python version, root mapping,
entry bytes, dependency resolver, denied set, V2 Package, or acceptance lineage
makes the Manifest stale and blocks execution. Stale manifests are preserved as
historical records and cannot be patched or reused under a new SHA.

## 14. Preparation Review Questions

| ID | Question |
| --- | --- |
| `C03-WP008-RDM-RQ-001` | Does the Plan bind V2, its review, adoption, authorization, and environment identity by full SHA? |
| `C03-WP008-RDM-RQ-002` | Does it correctly block final Manifest creation until an exact harness is accepted? |
| `C03-WP008-RDM-RQ-003` | Are preparation observations separated from final accepted identities? |
| `C03-WP008-RDM-RQ-004` | Does the root-token model preserve exact resolution without ambiguous or freely resolved paths? |
| `C03-WP008-RDM-RQ-005` | Does the top-level Manifest contract contain every V2-required identity group? |
| `C03-WP008-RDM-RQ-006` | Does every future entry require exact path, bytes, SHA, role, phase, loader, and provenance fields? |
| `C03-WP008-RDM-RQ-007` | Are directory grants, globs, placeholders, unknown fields, and unresolved paths prohibited? |
| `C03-WP008-RDM-RQ-008` | Are `site-packages`, installers, tests, bytecode, cache, and unused extensions denied by default? |
| `C03-WP008-RDM-RQ-009` | Does generation parse accepted harness and subject AST without importing or executing them? |
| `C03-WP008-RDM-RQ-010` | Are built-in, frozen, source, extension, data, DLL, and governance identities separated? |
| `C03-WP008-RDM-RQ-011` | Does the Plan require CPython bootstrap, PE extension, and exact OS dependency closure? |
| `C03-WP008-RDM-RQ-012` | Does the denied-module rule fail closed when an allowed module reaches a denied capability? |
| `C03-WP008-RDM-RQ-013` | Are canonical ordering, aggregate-stream bytes, aggregate SHA, and file SHA reproducible? |
| `C03-WP008-RDM-RQ-014` | Is the Manifest prevented from granting execution, mutation, network, or validation authority? |
| `C03-WP008-RDM-RQ-015` | Are independent review, Project Owner acceptance, and staleness controls mandatory? |
| `C03-WP008-RDM-RQ-016` | Does the Plan avoid requiring real-person identity while preserving stable role separation? |
| `C03-WP008-RDM-RQ-017` | Are all unresolved dependencies blockers rather than inferred or automatically admitted entries? |
| `C03-WP008-RDM-RQ-018` | Does the Plan avoid creating a final Manifest, harness, evidence, or runtime result? |
| `C03-WP008-RDM-RQ-019` | Are Route A, OCR, case, legal, provider, network, independent ACOS, and Git activity excluded? |
| `C03-WP008-RDM-RQ-020` | Does the resulting state remain fail closed with C03 activation not ready? |

## 15. Preparation Acceptance Gates

| ID | Gate |
| --- | --- |
| `C03-WP008-RDM-G-001` | Fixed governing lineage and authorization are complete |
| `C03-WP008-RDM-G-002` | Circular dependency is resolved through accepted-harness-first sequencing |
| `C03-WP008-RDM-G-003` | Preparation observations are qualified and non-governing |
| `C03-WP008-RDM-G-004` | Root-token and reparse-point controls are exact and fail closed |
| `C03-WP008-RDM-G-005` | Manifest object and entry field contracts are complete |
| `C03-WP008-RDM-G-006` | Entry categories and default exclusions are closed |
| `C03-WP008-RDM-G-007` | Generator algorithm is deterministic and non-executing |
| `C03-WP008-RDM-G-008` | Harness and subject import closure is exact and separately recorded |
| `C03-WP008-RDM-G-009` | CPython bootstrap, PE, and OS dependency closure is mandatory |
| `C03-WP008-RDM-G-010` | Denied capability modules cannot be admitted transitively |
| `C03-WP008-RDM-G-011` | Canonical entry stream and both aggregate and file SHA rules are reproducible |
| `C03-WP008-RDM-G-012` | Review, acceptance, mismatch, withdrawal, and staleness rules fail closed |
| `C03-WP008-RDM-G-013` | Stable role separation is preserved without real-person binding |
| `C03-WP008-RDM-G-014` | Final Manifest, harness, evidence, and execution remain uncreated |
| `C03-WP008-RDM-G-015` | Route A, OCR, case, legal, provider, network, independent ACOS, and Git boundaries are preserved |
| `C03-WP008-RDM-G-016` | Readiness, blocker closure, activation, and downstream transitions remain blocked |

## 16. Resulting State

```text
Python Runtime Dependency Manifest Preparation Plan:
MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED

Final PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json:
NOT CREATED / PRECONDITION BLOCKED

Accepted Harness SHA / Harness Import Set:
NOT ESTABLISHED

Runtime Manifest Review / Acceptance:
NOT AUTHORIZED / NOT ESTABLISHED

Python / Subject / Fixture / Validation Execution:
NOT AUTHORIZED / NOT PERFORMED

Evidence / E-011 / E-013:
NOT CREATED / NOT AUTHORIZED

Operational Tier A Blockers Closed:
0 / 3

C03 Activation Readiness:
NOT READY

Automatic Downstream Transition:
BLOCKED
```

The next permissible action is a separate fixed-SHA internal read-only review
of this Plan. No harness, final Manifest, network attestation, execution, or
evidence action follows automatically.
