# Route B C03 WP-007/009 实现记录 V4（候选）

本记录说明 V4 有限修订改了什么，依据是 `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_V4_LIMITED_REVISION_AUTHORIZATION.md`。V4 尚未审查，也未被接受；AR-B-007 保持 `OPEN / BLOCKED`。

## 文件身份

V3 一栏取自已接受输入 REV4 的 `subject_identities`，与 DSP-004 正式运行 v2 所测的文件相同。

| 文件 | V3（已验证） | V4 | 变化 |
| --- | --- | --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | 未变 |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | 未变 |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4` | `10616DF4C6A9E1E792C6D50E8A47547C37CA790E3D82713AA56403A48EC69B51` | 修改 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445` | `F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31` | 修改 |
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
| `validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_INPUT_CANDIDATE_REV5.json` | 139703 | `8A422CEE97A9434201CFA4309A2359672DD3E9ADEBF9322CD1C2AFBD9A27800A` |
| `validation/route_b_c03/wp_008/ar_b_007_v4/harness_rev5.py` | 26685 | `7B0E16FF52725BD7B3DD85CD814D533B55C16B380C91035152E0AE647AF817C7` |
| `validation/route_b_c03/wp_008/ar_b_007_v4/build_input_rev5.py` | 14822 | `5D8C378DDF787A49EC19BB39E28EA4CAA6A97234D2F31D21734CAC1ED8AA3446` |

- Harness REV5 以 `-I -S -B` 运行，退出码 0。
- 42 个变体全部通过：12 个完全符合，5 个部分符合，25 个不映射；运行时拦截 0 次。
- 原有 28 个变体的结果不变。
- 新增 14 个变体覆盖 B1、B2、N1、N2，其中包括有效期下界的正向对照和"已就绪但未验证"的情形。

## 审查

- **结论**：全新子代理审查（同一模型家族，不是外部审查）为 PASS WITH NOTES，没有阻断项。
- **已按审查意见修改**：
  - 就绪检查改为严格比对：取值必须是精确的 `str` 类型，用 `str.__eq__` 比较；输入制品集合必须是元组，每一项必须是精确的 `ArtifactReference`。
  - 补充两个变体：有效期下界的正向对照；就绪但未验证。
  - 刷新了输入目录中过时的 `source_sha256` 元数据。
  - 改正授权记录中"所有字段必填"等措辞。

## 仍然保留的局限

- **映射相关（N3、N4）**：仍未处理，边界审查 REV1 中的全部注记也照旧保留。
- **由调用方提供的值**：就绪状态、有效期和 `evaluated_at` 都由调用方提供，网关只按其取值判断，不独立核实。
- **`redaction_state`**：仍由调用方自行声明，例如传入 `"NOT_REDACTED"` 也能通过。
- **脱敏仍是排除名单**，只能拦住已列出的写法：
  - 拦不住的：带空格或连字符的电话、身份证号和卡号，`+86` 前缀，紧贴字母的证件号，电子邮件，中文姓名，`sk_live_`、`ghp_`、`AKIA` 开头的密钥，JWT，`pwd=`，`api key`，`Authorization Basic`；
  - 误拦的：含 `TOKEN` 的普通标识，以及长度相当的数字串。误拦会导致隔离，方向是安全的。
- **时间格式只校验形状**：例如 `2026-13-45T99:99:99Z` 也能通过格式检查，但时间的先后比较仍然正确。
- **枚举类型检查只覆盖网关的输入记录**：其他记录（如 `RevocationOrKillReference`）中的枚举字段不检查类型；网关不使用这些记录。
- **既有的身份比对仍用 `!=`**：有意构造的 `str` 子类可以干扰比对。这部分不在本次修订范围内。
