# Route B C03 实现记录 V6（候选，V-015 分类边界）

本版依据所有者决定 AR-B-008-KEEP-OPEN（"保持开放，先补 V-015"，记录在 `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_009_CLOSURE_DECISION.json`）制作，目的是补上 RDM-DSP-012 指出的缺口：此前没有"针对法律或下游分类请求的有效拒绝入口"。

本版已经过一次全新上下文子代理审查（同一模型家族，不是外部审查），结论为“通过，附说明”，无阻断项；审查意见及处理见文末。本版尚未被接受。AR-B-008 保持 `OPEN / BLOCKED`。

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

对这三项的确认，同时也是对 V-015 分类边界设计的签署。RDM-DSP-012 曾提出“另签非法律推理的分类边界设计”；本版没有另起设计文件，而是以 §16 加上这三项取值作为该设计。

**关于 `FULL` 覆盖等级。** 这一等级依赖第 2 项：Fixture 的请求 `LEGAL_ADVICE_OR_DOWNSTREAM_AUTHORITY` 被拒绝，是因为它不是允许的成员（原因码 `CLASS NOT PERMITTED`），而不是因为评估器识别出它属于禁止类别。评估器是独立的纯函数，尚无生成候选的代码路径接入它。所有者如果接受“独立评估器加 `CandidateRecord` 构造校验”可以算作完全覆盖，V-015 记为 `FULL`；如果不接受，应改记为部分覆盖。这些限制已写入输入 REV7 的 `coverage_limitations_rev7`。

## 文件身份

| 文件 | V5（已验收） | V6 | 变化 |
| --- | --- | --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424…` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` | 未变 |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5…` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` | 未变 |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `D0D5DA397EF4DFA0…` | `144841285C8E7ED88BED930FD01FB314863DFE8B2F67BDF3C73D816BE5423A99` | 修改 |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `F9CC7021C1A25866…` | `F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31` | 未变 |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E8…` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` | 未变 |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `9BC554294D594518…` | `0A7E937AB514D865FB71306C368168F9D06B0BC091150FA22C7EA7F24A699FE6` | 修改 |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `C6E03A8AB0305B83…` | `C6E03A8AB0305B83F6042D8F8E379AE91047D41F4AB3467AC0A7281E7E4DA48E` | 未变 |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `96F874FD494AA672…` | `96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA` | 未变 |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD503…` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` | 未变 |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `8D0B3CD664A89360…` | `8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686` | 未变 |

## 修改内容

- **`isolation.py`**：
  - 新增常量 `PROHIBITED_OUTPUT_CLASSES`（§16.2）和 `HUMAN_DISPOSITIONS`（§16.3）；
  - 新增记录类型 `ClassificationDetermination`；
  - 新增纯函数 `evaluate_classification_request`。
  - `ClassificationDetermination` 在构造时自行校验：请求状态只能是 `REJECTED` 或 `HUMAN_REVIEW_PENDING`，候选状态必须是 `HUMAN_REVIEW_PENDING`，`downstream_blocked` 必须恰好是 `True`，原因码必须是非空字符串。因此即使绕过评估器直接构造，也无法得到“下游放行”的判定；
  - 导入 `.contracts`（同一包内的模块）和 `dataclasses`，两者都已在导入闭包中。
- **`contracts.py`**：
  - `CandidateRecord` 在构造时校验 `candidate_class`，必须是 `CandidateClass` 成员。这样，禁止的类别无法成为候选；
  - `CandidateRecord` 的 `downstream_blocked` 检查由真值判断改为必须恰好是 `True`（此前 `"no"` 之类的非空字符串可以通过）。

## 本地验证（Linux，CPython 3.13；正式运行必须使用 3.12.10）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/c03_v6/C03_V6_INPUT_CANDIDATE_REV7.json` | 216339 | `3E01C1961BC435608A7907A35C6E0C013E26312011A6D68983E44E24FEB76E2F` |
| `validation/route_b_c03/wp_008/c03_v6/harness_rev7.py` | 29193 | `8DA8A17274E61293433FAC61C912016F29CECA28B3DA782424701DC3E181A551` |
| `validation/route_b_c03/wp_008/c03_v6/build_input_rev7.py` | 10090 | `BA07B6D03E3AE59DE5DAD9BD2D32BF499A041458F01A312C1FB7637E17CD2CBA` |

- Harness REV7 运行退出码为 0；76 个变体全部通过：13 个完全符合，13 个部分符合，50 个不映射，运行时拦截 0 次。
- V-015 新增 6 个变体：
  - 1 个用 Fixture 原本的请求 `LEGAL_ADVICE_OR_DOWNSTREAM_AUTHORITY`，结果与 Fixture 预期一致；
  - 另外 5 个分别检验：禁止类别、原始字符串、允许类别、批准后仍阻断、候选构造时拒绝禁止类别。
- V-015 的覆盖等级由"仅观察"标为 `FULL`（条件见上文）。
- `c03_v6/` 目录新增 `.gitattributes`（`* -text`），与此前各版资产目录相同，防止换行符被改写。

**Harness REV7 相对 REV6 的代码变化**（均已写入其文件头说明）：
- 输入文件路径与 SHA、两个被测文件的 SHA 改为 V6 的值；
- 新增适配器 `ADP-EVALUATE-CLASSIFICATION`；
- 新增返回类型 `ClassificationDetermination`；
- 新增枚举字典比较分支（期望值为 `{"enum_class", "member"}` 时按枚举成员精确比较）。审查确认，REV6 的 55 条规则中没有一条会进入这个分支，所以它只影响 V6 新增的 6 条规则；
- 覆盖等级读取顺序改为 `coverage_class_rev7`，其次 `_rev6`，再次 `_rev3`；
- 输出中的版本字符串改为 REV7。

## 局限

- **只对调用方提供的类别标签作判定**，不判断内容是否构成法律意见。
- **尚未接入候选生成流程**：没有产生候选的代码路径，`CandidateRecord` 的构造校验是目前唯一的强制点。

## 审查与处理

审查记录：`.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_V6_REVISION_REVIEW_REV1.md`。结论：通过，附说明；无阻断项。

| 意见 | 处理 |
| --- | --- |
| N1：V-015 旧的局限说明与 `FULL` 并存，相互矛盾 | 已处理。输入 REV7 新增 `coverage_limitations_rev7`，写明它取代旧说明（旧文字按惯例原样保留）以及当前的各项限制 |
| N2：`FULL` 依赖的是“非成员一律拒绝”，较弱 | 已在上文写明，作为第 2 项取值的一部分由所有者确认；不接受则改记部分覆盖 |
| N3：`ClassificationDetermination` 不自行保证不变量 | 已修复，增加构造时校验 |
| 说明：没有另签分类边界设计 | 已写明：三项取值的确认即为该设计的签署 |
| 说明：`CandidateRecord` 的 `downstream_blocked` 只做真值判断 | 已修复，改为必须恰好是 `True` |
| 说明：拒绝、保持阻断、要求更正三种处置不影响结果 | 保留。结果都是继续阻断，符合 §16.3；处置的留痕属于审计记录，不在本评估器范围内 |
| 说明：`prepare_formal_v5.py` 未提交 | 它属于正式运行资产准备，随正式运行 v5 资产一并提交 |
| 说明：记录未列 Harness 代码变化和 `.gitattributes` | 已补 |

修改后在本地重新构建输入并运行：输入 REV7 的 SHA 变为上表所列值，76 个变体全部通过，结果分布不变。
