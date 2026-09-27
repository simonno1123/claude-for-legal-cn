# Project Owner Route B C03 WP-008 Python Runtime Dependency Manifest Preparation Authorization

## 0. Authorization Control

| Field | Value |
| --- | --- |
| Authorization type | ONE-TIME DOCUMENT-ONLY MANIFEST PREPARATION AUTHORIZATION |
| Authorized output | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_PYTHON_RUNTIME_DEPENDENCY_MANIFEST_PREPARATION_PLAN.md` |
| Governing V2 Package | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_VALIDATION_EXECUTION_PACKAGE_REVISION_V2.md` |
| Governing V2 Package SHA-256 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| V2 internal re-review SHA-256 | `A652ABCA2DCFAC9BBEB5074860D7F7457CE353BB95A858F4BEDF30FD5B52E299` |
| V2 adoption decision SHA-256 | `9CB805082CF7D635F21605A68622A7CB9F495599B1B95B18EDD09E464BAB6560` |
| Environment identity manifest SHA-256 | `EFCF1A783199F58387BDBB0704563ED943A5E6A3E319A04CE6D58E57FC5CA531` |
| Activation semantics | `CAPABILITY_ONLY` |
| Authorization source | CONVERSATION-LEVEL PROJECT OWNER AUTHORIZATION |
| Authorization status | **AUTHORIZED — FIXED-BASELINE AND EXACT-SCOPE BOUND** |

## 1. Authorized Purpose

This authorization permits preparation of one document-only design plan for
the future exact asset:

```text
validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json
```

The preparation plan may define:

1. the closed manifest schema and canonical serialization rules;
2. the exact identity categories required by V2, including Python executable,
   `pyvenv.cfg`, runtime DLLs, standard-library files, extension modules, data
   files, harness imports, subject imports, and denied modules;
3. a deterministic inventory and SHA-256 calculation method;
4. the difference between currently observable environment identity and
   future harness-dependent identity;
5. review, acceptance, staleness, mismatch, and fail-closed rules;
6. exact preparation review questions and acceptance gates; and
7. the lawful sequencing required before final Manifest materialization.

## 2. Permitted Read-Only Inspection

| Read scope | Permitted use |
| --- | --- |
| Adopted V2 Package, review, adoption, Plan, preparation, and environment records | Fixed governance and environment identity only |
| Ten fixed Route B C03 subject files | Text/AST import and capability inventory only |
| Existing `.venv-validation` Python executable and `pyvenv.cfg` | Identity, version-record, path, byte-size, and SHA reconciliation only |
| Existing `.venv-validation` runtime DLL and standard-library trees | Non-mutating path, byte-size, and SHA inventory design only |

Inspection must remain inside the current `claude-for-legal-cn` project and
the already identified local validation environment. It does not authorize
repository-wide discovery, independent ACOS access, external provider access,
or execution of the inspected files.

## 3. Mandatory Dependency Qualification

The final Manifest requires a closed harness import set derived from an exact,
separately reviewed and accepted harness AST. No harness currently exists.
Therefore:

```text
Final PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json Materialization:
BLOCKED — ACCEPTED HARNESS SHA AND IMPORT SET NOT ESTABLISHED
```

The authorized preparation plan must preserve this dependency explicitly. It
must not use a placeholder, inferred list, model-generated list, wildcard, or
current environment enumeration as a substitute for the future accepted
harness import set.

## 4. Explicitly Not Authorized

| Subject | State |
| --- | --- |
| Final `PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` creation | NOT AUTHORIZED / PRECONDITION BLOCKED |
| Harness, schema implementation, script, or test-code creation | NOT AUTHORIZED |
| Python, module, DLL, fixture, subject, or harness execution/import | NOT AUTHORIZED |
| Package installation, update, repair, deletion, or environment mutation | NOT AUTHORIZED |
| Network probe, provider, model, API, Connector, or MCP invocation | NOT AUTHORIZED |
| Evidence directory, `E-011`, or `E-013` creation | NOT AUTHORIZED |
| Validation execution or operational blocker closure | NOT AUTHORIZED |
| Route A, OCR, case, legal, matter, or evidence activity | NOT AUTHORIZED |
| Independent ACOS project access or modification | NOT AUTHORIZED |
| Git commit, push, branch, merge, or remote action | NOT AUTHORIZED |

## 5. Authorization Effect

This authorization allows materialization of the single preparation-plan
document and the minimum read-only inspection needed to ground it. It does not
authorize final Manifest generation, acceptance, harness work, execution, or
any downstream transition.

```text
Project Owner Authorization:
SIGNED & FILED

Automatic Downstream Transition:
BLOCKED
```
