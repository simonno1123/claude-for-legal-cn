# Route B C03 实现记录 V6（候选，V-015 分类边界）

本版依据所有者决定 AR-B-008-KEEP-OPEN（"保持开放，先补 V-015"，记录在 `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_CLOSURE_DECISION.json`）制作，目的是补上 RDM-DSP-012 指出的缺口：此前没有"针对法律或下游分类请求的有效拒绝入口"。

本版尚未审查，也未接受。AR-B-008 保持 `OPEN / BLOCKED`。

## 设计依据

本版不另起新的设计，而是直接落实已采纳的 WP-007 实现设计第 16 节：
- §16.1 规定了 5 个允许的候选类别；
- §16.2 规定了 10 个禁止的输出类别；
- §16.3 规定了 4 种合格人员处置，并明确人工批准不能激活能力，也不能取得下游权限；
- §14.1 规定，主张法律或下游权限时，结果为 `REJECTED — OUTPUT BOUNDARY FAILURE`。

## 需要所有者在验收时一并确认的取值

1. **判定结果包含两层状态。** 请求本身的状态，与候选的状态分开记录：
   - 不被允许的请求一律 `REJECTED`（依 §14.1）；
   - 但候选始终是 `HUMAN_REVIEW_PENDING`，下游始终阻断（依 Fixture V-015 和 §16）。
2. **允许的类别只认精确的 `CandidateClass` 成员。** 与成员值相同的原始字符串也按"不允许"处理。
3. **合格人员的处置只认 §16.3 列出的 4 种原文。** 即使是"批准"，下游也仍然阻断。

## 文件身份

| 文件 | V5（已验收） | V6 | 变化 |
| --- | --- | --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424…` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | 未变 |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5…` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | 未变 |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `D0D5DA397EF4DFA0…` | `82F6928E733DC643A6C7F7701E601BAC26A2AC710FC28DC45E14A2C422D84EC4` | 修改 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `F9CC7021C1A25866…` | `F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31` | 未变 |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E8…` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | 未变 |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D594518…` | `56409022573592EE982647C113B041EFBEC187E3B44A20A0F14B3A951A6E090B` | 修改 |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `C6E03A8AB0305B83…` | `C6E03A8AB0305B83F6042D8F8E379AE91047D41F4AB3467AC0A7281E7E4DA48E` | 未变 |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `96F874FD494AA672…` | `96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA` | 未变 |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD503…` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | 未变 |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `8D0B3CD664A89360…` | `8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686` | 未变 |

## 修改内容

- **`isolation.py`**：
  - 新增常量 `PROHIBITED_OUTPUT_CLASSES`（§16.2）和 `HUMAN_DISPOSITIONS`（§16.3）；
  - 新增记录类型 `ClassificationDetermination`；
  - 新增纯函数 `evaluate_classification_request`。
  - 导入 `.contracts`（同一包内的模块）和 `dataclasses`，两者都已在导入闭包中。
- **`contracts.py`**：`CandidateRecord` 在构造时校验 `candidate_class`，必须是 `CandidateClass` 成员。这样，禁止的类别无法成为候选。

## 本地验证（Linux，CPython 3.13；正式运行必须使用 3.12.10）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json` | 215603 | `C1A32F956E02DA1D2FF76B9FA8A773573B4705E6BBEFE7382213A17DCC0330FD` |
| `validation/route_b_c03/wp_008/c03_v6/harness_rev7.py` | 29193 | `EFE351B99A8882E43EFB21A83938FD5D691AE166929B923A9E856851FA7AAFB7` |
| `validation/route_b_c03/wp_008/c03_v6/build_input_rev7.py` | 9243 | `74C7183285C2EAB1BE42FFC2B607D5DF253F6B1FA62A3DFDDC71B6A70CC2CC42` |

- Harness REV7 运行退出码为 0；76 个变体全部通过：13 个完全符合，13 个部分符合，50 个不映射，运行时拦截 0 次。
- V-015 新增 6 个变体：
  - 1 个用 Fixture 原本的请求 `LEGAL_ADVICE_OR_DOWNSTREAM_AUTHORITY`，结果与 Fixture 预期一致；
  - 另外 5 个分别检验：禁止类别、原始字符串、允许类别、批准后仍阻断、候选构造时拒绝禁止类别。
- V-015 的覆盖等级由"仅观察"标为 `FULL`。

## 局限

- **只对调用方提供的类别标签作判定**，不判断内容是否构成法律意见。
- **尚未接入候选生成流程**：没有产生候选的代码路径，`CandidateRecord` 的构造校验是目前唯一的强制点。
