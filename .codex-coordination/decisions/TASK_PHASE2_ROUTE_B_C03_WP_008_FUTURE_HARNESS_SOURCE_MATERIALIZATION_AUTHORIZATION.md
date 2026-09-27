# Project Owner Route B C03 WP-008 Future Harness Source Materialization Authorization

## 0. Authorization Control

| Field | Value |
| --- | --- |
| Authorization type | ONE-TIME EXACT-ASSET STATIC SOURCE MATERIALIZATION |
| Sole authorized output | `validation/route_b_c03/wp_008/run_validation.py` |
| Governing V2 Package SHA-256 | `5265D6D422D8BC101107E81B71AFEB485DDDE300A959B3692DA944AE18829BE5` |
| V2 internal re-review SHA-256 | `A652ABCA2DCFAC9BBEB5074860D7F7457CE353BB95A858F4BEDF30FD5B52E299` |
| V2 adoption decision SHA-256 | `9CB805082CF7D635F21605A68622A7CB9F495599B1B95B18EDD09E464BAB6560` |
| Manifest Preparation Plan SHA-256 | `8C23436CD6CD7ADE9FFC30C44241D1D944A203AC00F0605B366B9F1658BBC239` |
| Manifest Preparation Plan review SHA-256 | `64AFB34D60B3C1C7FAD798AD2C226128C87D8C15BE33A4DA90E20F8149B85AEA` |
| Manifest Preparation Plan adoption SHA-256 | `20E513434365134800AE0A06C2F1DA09A861404ACE8412B62A064B3E6684BCEA` |
| Activation semantics | `CAPABILITY_ONLY` |
| Authorization source | CONVERSATION-LEVEL PROJECT OWNER AUTHORIZATION |
| Authorization status | **AUTHORIZED — EXACT-PATH AND EXACT-SCOPE BOUND** |

## 1. Authorized Purpose

This authorization permits materialization of one static Python source
candidate implementing the adopted WP-008 V2 harness contract. The source is
created solely so its exact SHA, AST, direct imports, capability surface, and
evidence-writing design can be independently reviewed and later used to derive
the final runtime-dependency Manifest.

Materialization creates no execution authority. Source existence, syntax,
apparent completeness, or later review cannot be represented as operational
conformance, successful validation, or evidence.

## 2. Mandatory Static Source Contract

The source candidate must encode, without executing:

1. the exact closed command interface for `--run-id`, `--fixture-root`, and
   `--evidence-root`, with no additional positional or optional inputs;
2. immediate `sys.dont_write_bytecode = True` establishment and verification;
3. fixed-SHA verification for governing records, the harness, ten subjects,
   fifteen fixtures, environment identity, future runtime Manifest, future
   network attestation, and exact execution authorization;
4. the 12 adopted V2 preflight gates before subject import or evidence-root
   creation;
5. static AST/import/capability scanning of its own accepted bytes and the ten
   fixed subject files;
6. deterministic socket-construction denial and a Python audit hook installed
   before subject import;
7. rejection of dynamic imports, dynamic code, process creation, package
   mutation, path discovery, non-manifest reads, and every unlisted write;
8. fixed ascending scenario order `C03-TA-V-001` through `C03-TA-V-015` with
   fresh isolated state and only the explicit V-006 duplicate relation;
9. independent expected and observed fields, with no harness aggregate PASS;
10. the exact four-file evidence write set and V2 raw control fields;
11. first-critical-failure stop, no cleanup, no retry, no overwrite, and
    new-authorization-only rerun semantics; and
12. explicit prohibition on governance acceptance, blocker closure, readiness,
    activation, legal conclusions, or downstream authority.

## 3. Source Construction Constraints

| Constraint | Required state |
| --- | --- |
| Language | Python source compatible with recorded Python `3.12.13` |
| Dependency class | Python standard library only, subject to later exact Manifest closure |
| Imports | Literal and statically enumerable only |
| Dynamic import/code | PROHIBITED |
| Network/provider/API/MCP | PROHIBITED |
| Subprocess/process creation | PROHIBITED |
| Package installation or mutation | PROHIBITED |
| Repository discovery, globbing, parent traversal, or Git reads | PROHIBITED |
| Paths | Exact authorized arguments and fixed internal constants only |
| Evidence writes | Defined in source but impossible until later execution authorization and all preflight gates pass |
| Source state after materialization | MATERIALIZED — INTERNAL REVIEW NOT AUTHORIZED |

The source may define data structures, deterministic helper functions, error
types, canonical serialization logic, static verification logic, and guarded
evidence-writing logic needed by the V2 contract. It may not embed real matter,
credentials, secrets, machine-specific tokens, network locators, or current
runtime results.

## 4. Manifest Dependency Qualification

The final runtime-dependency Manifest remains blocked until this source
candidate is independently reviewed and accepted by exact SHA. Materialization
of the harness provides only candidate AST and import data.

```text
Harness Source Materialization:
AUTHORIZED

Harness Internal Review / Acceptance:
NOT AUTHORIZED / NOT ESTABLISHED

Final PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json:
NOT AUTHORIZED / PRECONDITION BLOCKED
```

No current runtime-tree observation, inferred import, placeholder, wildcard,
or broad standard-library grant may substitute for the later accepted harness
import closure.

## 5. Explicitly Not Authorized

| Subject | State |
| --- | --- |
| Running or importing `run_validation.py` | NOT AUTHORIZED |
| Python syntax compilation, byte-compilation, test, smoke run, or formatter execution | NOT AUTHORIZED |
| Subject, fixture, DLL, module, or scenario execution/import | NOT AUTHORIZED |
| Harness internal review, revision, or acceptance | NOT AUTHORIZED |
| Final runtime-dependency Manifest creation | NOT AUTHORIZED |
| Network-isolation attestation creation | NOT AUTHORIZED |
| Evidence directory, `E-011`, or `E-013` creation | NOT AUTHORIZED |
| Validation execution or operational blocker closure | NOT AUTHORIZED |
| Environment or package mutation | NOT AUTHORIZED |
| Route A, OCR, case, legal, matter, or evidence activity | NOT AUTHORIZED |
| Provider, model, network, API, Connector, or MCP invocation | NOT AUTHORIZED |
| Independent ACOS project access or modification | NOT AUTHORIZED |
| Git commit, push, branch, merge, or remote action | NOT AUTHORIZED |

## 6. Authorization Effect

This authorization permits one new static source asset at the exact authorized
path. No other source, schema, fixture, evidence, manifest, attestation, test,
or runtime asset may be created or changed.

```text
Project Owner Authorization:
SIGNED & FILED

Automatic Downstream Transition:
BLOCKED
```
