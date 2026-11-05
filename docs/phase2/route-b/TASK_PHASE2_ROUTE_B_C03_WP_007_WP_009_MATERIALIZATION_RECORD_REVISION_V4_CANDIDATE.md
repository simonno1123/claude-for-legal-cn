# Route B C03 WP-007/009 实现记录 V4（候选）

本记录说明 V4 有限修订改了什么，依据是 `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_V4_LIMITED_REVISION_AUTHORIZATION.md`。V4 尚未审查，也未被接受；AR-B-007 保持 `OPEN / BLOCKED`。

## 文件身份

V3 一栏取自已接受输入 REV4 的 `subject_identities`，与 DSP-004 正式运行 v2 所测的文件相同。

| 文件 | V3（已验证） | V4 | 变化 |
| --- | --- | --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | 未变 |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | 未变 |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4` | `A7D30CF9F0694C46C904DB8EFBCCAA5ED205CF73E3E7AA1DBD5A6A45187CB05A` | 修改 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | `3B652CF9D5B07147A15C909FC7ADE56680C0D15ABF7907864E9970ACB1AD5F4B` | 修改 |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | 未变 |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` | 未变 |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734` | `6F30D996119F61A19B20208FC44C8AF1FB96ADFE09ADE3538675B9D3F2933734` | 未变 |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `A704BDB22C55C92D0909FA0D6A668D8C149724B2A7627938C301758F1D09F561` | `96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA` | 修改 |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | 未变 |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `028EE9DDD7A2C06840A6F344A4C4CC716EFF95073BE39CA6E57FB7FDBBFA6DD5` | `8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686` | 修改 |

## 修改内容

**`contracts.py`**
- 新增三个校验函数：`require_enum`、`require_utc_timestamp`、`is_utc_timestamp`。
- 新增两个就绪取值常量：`ARTIFACT_READY = "READY"`、`ARTIFACT_VALIDATED = "VALIDATED"`。
- `CapabilityConfigurationReference`：构造时校验 `state` 必须是 `CapabilityState` 的成员（B1）。
- `TierBAuthorityPacketReference`：
  - 校验 `output_class`、`revocation_state`、`state` 三个枚举字段的类型；
  - `valid_from`、`valid_until` 必须是 UTC 时间格式，且前者早于后者（N2）。
- `GovernedInputEnvelopeReference`：
  - `requested_output_scope` 必须是元组，且每项都是 `CandidateClass` 成员；
  - `input_artifact_references` 必须是元组，且每项都是 `ArtifactReference`。
- `AuditRecordCandidate` 新增 `__post_init__`（N1）：
  - 全部字段必填，散列字段校验格式；
  - 脱敏筛查改为扩充后的敏感词表，加上身份证号、手机号、银行卡号、`sk-` 密钥前缀四个模式；
  - 直接构造这个记录也绕不过这些检查。

**`audit.py`**：`build_audit_candidate` 只负责构造记录，校验全部由 `__post_init__` 执行。

**`identity_gate.py`**
- 新增必填关键字参数 `evaluated_at`。
- 终止标志必须严格等于 `False` 才算未终止（B2）。
- 能力状态只有 `ENABLED_CAPABILITY_ONLY` 能继续往下；其他类型或取值一律阻断（B1）。
- 新增有效期窗口检查，不满足时返回 `BLOCKED — AUTHORITY FAILURE`（N2）。
- 在返回 ELIGIBLE 之前，新增输入制品检查：制品集合为空，或任一制品未就绪、未验证，返回 `BLOCKED — READINESS/PROVENANCE FAILURE`（N2）。

**`capability.py`**
- `evaluate_gate` 的 `validity_confirmed`、`kill_active`、`evaluated_at` 三个参数都不再有默认值（B2）。
- `is_active` 改为按枚举成员身份判断。

**未修改的文件**：`mapping.py`、`isolation.py`、`failures.py`、`provider_port.py`，以及两个包的 `__init__.py`。

**导入**：没有新增任何导入。只多用了已有的 `re` 模块，因此依赖闭包预计不变；正式运行会核对这一点。

## 本地验证（Linux，CPython 3.13，不是正式环境）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_INPUT_CANDIDATE_REV5.json` | 136693 | `84F719D8EDE0735B6B01AE1D66DC97527AE85534D53E5D7E59E9A3CE3F4A43C9` |
| `validation/route_b_c03/wp_008/ar_b_007_v4/harness_rev5.py` | 26685 | `18564502FDDFF90F302CF71829D6882CCB0DE823F2748A0C33E3D51338ECED8B` |
| `validation/route_b_c03/wp_008/ar_b_007_v4/build_input_rev5.py` | 13534 | `DA7B5A16ADAA8616190EFB4A38575B65CBE3E6A44D6D9DDD9B7DD3E02F578426` |

- Harness REV5 在本地以 `-I -S -B` 运行，退出码 0。
- 40 个变体全部通过：完全符合 12 个，部分符合 5 个，不映射 23 个；拦截 0 次。
- 原有 28 个变体的结果没有变化。新增的 12 个变体覆盖 B1、B2、N1、N2，全部通过。

## 仍然保留的局限

- N3、N4 两项（映射相关），以及边界审查 REV1 中的全部注记。
- 就绪状态、有效期和 `evaluated_at` 都由调用方提供；网关只按其取值判断，不独立核实。
