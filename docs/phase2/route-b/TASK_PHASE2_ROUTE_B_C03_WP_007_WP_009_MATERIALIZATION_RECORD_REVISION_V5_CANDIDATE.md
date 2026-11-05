# Route B C03 WP-007/009 实现记录 V5（候选，AR-B-009）

依据：`.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_WORK_AUTHORIZATION.md`。本版尚未审查、尚未接受；AR-B-009 保持 `OPEN / BLOCKED`。

## 文件身份

| 文件 | V4（已验收） | V5 | 变化 |
| --- | --- | --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424…` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | 未变 |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5…` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | 未变 |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `10616DF4C6A9E1E7…` | `D0D5DA397EF4DFA0DB47D924A90CB9EBD9017F737FCB7B915AE9633D7C6F310A` | 修改 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `F9CC7021C1A25866…` | `F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31` | 未变 |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E8…` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | 未变 |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D594518…` | `9BC554294D5945188A153F0A5CBEDFAB4E483C95B133683B7517ECC334D4205B` | 未变 |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `6F30D996119F61A1…` | `19E7EB6EFBA6AB8F13F7FB0268EF8F047F776F387B6C2C8CDB2D01DC514F3A3E` | 修改 |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `96F874FD494AA672…` | `96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA` | 未变 |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD503…` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | 未变 |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `8D0B3CD664A89360…` | `8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686` | 未变 |

## 修改内容

- **`contracts.py`**：新增记录类型 `IdempotencyRecord`，字段为键散列、范围散列、记录时间和效果引用；构造时逐项校验。
- **`failures.py`**：
  - 新增返回类型 `ControlDetermination`（受保护状态加原因码）。
  - 新增 7 个纯函数，各自对应设计的一节：

| 函数 | 对应设计 | 可能的结果 |
| --- | --- | --- |
| `evaluate_control_precedence` | §13、§8 | 已终止 / 已撤销 / 阻断（控制状态未知、状态合同错误、没有生效的控制） |
| `evaluate_idempotency` | §10 | 阻断（首次使用、重复使用、未绑定、重放、版本或授权失效）/ 隔离（键冲突、先前记录不一致） |
| `evaluate_timeout` | §11 | 隔离（超时未完成、迟到结果）/ 阻断（期限未到、期限内结果不得使用、超时政策未绑定） |
| `evaluate_rollback` | §14 | 已终止 / 已撤销 / 待回滚（只有资格，或已有决定但不执行）/ 阻断 |
| `evaluate_supersession` | §14 | 已过时（被取代的版本）/ 阻断 |
| `verify_audit_chain` | §15 | 隔离（完整性失败）/ 阻断（链不可用；或校验一致，但只是候选、不持久化） |
| `evaluate_dependency` | §17、V-013 | 阻断（未授权、不可用、可用但未授权执行） |

**没有任何函数会返回"执行"或"已激活"的状态。** 新增导入只有 `hashlib`、`json`、`dataclasses.fields`。这些模块已在 Harness 的导入闭包中，因此闭包预计不变，由正式运行核对。

## 验证资产（本地：Linux，CPython 3.13）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/ar_b_009_v5/C03_V5_INPUT_CANDIDATE_REV6.json` | 198716 | `0BF2068E300C7ED9050644C6F252D3615CBCA70AA4CE8488AEC123DA74C22C62` |
| `validation/route_b_c03/wp_008/ar_b_009_v5/harness_rev6.py` | 28099 | `537736595EC29249A679EFED639FD35CFD8EE11BB46470DD9EDF222364F9F619` |
| `validation/route_b_c03/wp_008/ar_b_009_v5/build_input_rev6.py` | 24537 | `45816D298CD11CA7649CBE2006193B4A13706A9ECB2DCF092EB8662E303BE757` |

- **运行结果**：Harness REV6 以 `-I -S -B` 运行，退出码为 0；67 个变体全部通过，运行时拦截 0 次。
  - 完全符合 Fixture：12 个；
  - 部分符合：13 个，其中 8 个是这次新增并映射到 Fixture 的变体；
  - 按设计不映射：42 个。
- **新增变体**：25 个，覆盖 V-006、V-008、V-009、V-010、V-011、V-012、V-013 七个场景。这七个场景的覆盖等级从"仅观察"或"部分"标为 `PARTIAL_LIMITED`。
- **审计链的预期头部**：由生成脚本按同一规则独立重写的实现算出，没有调用受测代码。

## 仍然保留的局限

- **只验证判定逻辑。** 计时器、信号传播与接收回执、持久化的幂等记录、真实依赖和网络都没有被观察；设计也规定不实现这些。
- **判定依据都由调用方提供**：时间、作用范围、已接受版本清单、决定是否有效。
- **审计链只校验调用方提供的候选记录**：不签名，也不防止调用方同时改动记录和预期头部。
- **V-015（分类边界）不在本版范围内。**
