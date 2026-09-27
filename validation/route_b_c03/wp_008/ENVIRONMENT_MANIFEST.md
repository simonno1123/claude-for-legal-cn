# Route B C03 WP-008 Validation Environment Manifest

## 0. Manifest Control

| Field | Value |
| --- | --- |
| Purpose | VALIDATION PREPARATION IDENTITY BINDING ONLY |
| Bound Plan SHA-256 | `E9643D0993532A1E1603B66F95CD288F394BDDA621EFB6784B256CECFC915E6D` |
| Bound Plan Adoption Decision SHA-256 | `CDCFA2A057F477C86A5866D00A05FBE28062062A7AC771ED14BB1A7BD5D2E331` |
| Environment root | `.venv-validation` |
| Environment creation | PRE-EXISTING / NOT CREATED BY THIS PREPARATION |
| Package installation or update | NOT AUTHORIZED / NOT PERFORMED |
| Subject import or execution | NOT AUTHORIZED / NOT PERFORMED |
| Validation execution | NOT AUTHORIZED / NOT PERFORMED |

## 1. Host Identity

| Field | Recorded value |
| --- | --- |
| Operating system | `Microsoft Windows NT 10.0.26100.0` |
| Architecture | `X64` |
| PowerShell | `7.6.4` |
| Culture | `zh-CN` |
| Timezone | `China Standard Time` |

These values identify the preparation host only. They are not observed
validation results and do not establish environment acceptance for execution.

## 2. Environment File Identity

| Path | Bytes | SHA-256 | Permitted future role |
| --- | ---: | --- | --- |
| `.venv-validation/pyvenv.cfg` | 460 | `7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461` | Environment configuration identity |
| `.venv-validation/Scripts/python.exe` | 262144 | `560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E` | Future validation interpreter, only if separately authorized |
| `.venv-validation/Scripts/jq.exe` | 1026560 | `23CB60A1354EED6BCC8D9B9735E8C7B388CD1FDCB75726B93BC299EF22DD9334` | Future JSON inspection tool, only if separately authorized |
| `.venv-validation/Scripts/jsonschema.exe` | 108446 | `EE056533C215CD97187298826AD70B68DBC80C2E6881D0494F0494A12B3349A5` | Future schema validation tool, only if separately authorized |
| `.venv-validation/Scripts/pip.exe` | 108454 | `7DE9B91EA7C840110BE6ADEC48DEECD3ACC57D568C51252FC7CEA00710525F14` | INVENTORY ONLY — PACKAGE ACTION PROHIBITED |

The Python version recorded by `pyvenv.cfg` is `3.12.13` with
`include-system-site-packages = false`.

## 3. Existing Distribution Inventory

| Distribution | Recorded version | Planned status |
| --- | --- | --- |
| `attrs` | `26.1.0` | Present in validation environment; not a subject dependency |
| `jsonschema-specifications` | `2025.9.1` | Present in validation environment; not a subject dependency |
| `jsonschema` | `4.25.1` | Present in validation environment; use requires later exact authorization |
| `pip` | `25.0.1` | Present; package actions prohibited |
| `PyYAML` | `6.0.2` | Present; not selected by the adopted Plan |
| `referencing` | `0.37.0` | Present in validation environment; not a subject dependency |
| `rpds-py` | `2026.6.3` | Present in validation environment; not a subject dependency |
| `typing-extensions` | `4.16.0` | Present in validation environment; not a subject dependency |

Presence does not constitute permission to use a distribution. A later
execution authorization must enumerate the exact allowed tool set; every
unlisted tool remains prohibited.

## 4. Isolation Contract

| Boundary | Required state |
| --- | --- |
| Network | DISABLED / PROHIBITED |
| External provider or model | ABSENT / PROHIBITED |
| Route A or OCR | ABSENT / PROHIBITED |
| Case, matter, or evidence repository | ABSENT / PROHIBITED |
| Credential, secret, key, or token | ABSENT / PROHIBITED |
| Independent ACOS project | OUT OF SCOPE / PROHIBITED |
| Git remote or repository mutation | PROHIBITED |
| Upstream write set | EMPTY |
| Allowed future evidence destination | NOT YET BOUND |

## 5. Remaining Execution Blockers

```text
Validation Harness:
NOT CREATED / NOT AUTHORIZED

Allowed Command Set:
NOT BOUND

Evidence Destination:
NOT BOUND

Fixture Admission Decision:
NOT ESTABLISHED

Executor / Independent Reviewer Identity:
NOT BOUND

Validation Execution Authorization:
NOT ISSUED
```

Any file, distribution, host, configuration, or isolation-state change makes
this manifest stale and requires a new identity disposition before execution.
