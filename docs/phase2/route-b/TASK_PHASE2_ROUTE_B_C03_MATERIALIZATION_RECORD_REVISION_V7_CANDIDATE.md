# Route B C03 实现记录 V7（候选：能力层测试缺口与控制接入）

本版依据所有者决定 AR-B-008-V7-FIRST（`.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_008_V7_FIRST_DECISION.json`）制作，目的是在决定 AR-B-008 之前，补上关闭证据包 REV1 第四节列出的能力层缺口，并把控制判定接入 `capability.py`。

本版已经过一次全新上下文子代理审查（同一模型家族，**不是外部审查**），结论为“通过，附说明”，无阻断项；处理情况见文末。本版尚未被接受。AR-B-008 保持 `OPEN / BLOCKED`。正式运行需要所有者另行授权。

**接入只完成了一部分。** 接入 `capability.py` 的只有转换前判定，即控制判定加身份关口；其余约 8 个判定函数仍是模块函数，见取值第 4 项。因此，关闭证据包第六节偏离第 3 项“只是缩小，没有消除”。

## 修改内容

**`failures.py`**
- 新增 `evaluate_integrity(subject_kind, *, expected_sha256, observed_sha256)`，对应 V-012 计划中的"输出散列、依赖身份"篡改。
  - 对象类别只认 4 种：`IDENTITY`、`OUTPUT`、`DEPENDENCY`、`AUDIT_REFERENCE`。
  - 散列不一致时为 `QUARANTINED — INTEGRITY FAILURE: <类别>`。
  - 期望值格式错误或类别未知时为 `PROTECTED_BLOCKED — INTEGRITY REFERENCE UNBOUND`（引用本身无效）；
  - 观察值缺失或格式错误时为 `QUARANTINED — INTEGRITY UNCERTAIN: <类别>`。这依据 WP-009 设计 §12：完整性不确定的对象应予隔离。
  - 一致时仍是 `PROTECTED_BLOCKED`，并注明"未授权执行"。
  - 这个函数只比较调用方提供的散列，本身不读取也不计算任何输出或依赖。

**`isolation.py`**：`assert_reference_only` 由只查顶层键名，扩展为：
- 每一层嵌套的字典键名都检查（沿用原来的禁止词表）；
- 字符串值中如果出现秘密标记，就隔离；
- 字节串一律拒绝；非字符串键名一律拒绝；
- 记录本身之下再嵌套超过 8 层容器时拒绝（循环引用也因此被拒绝）；
- 记录本身不是映射（字典）时拒绝。此前顶层若是字符串列表会被逐项接受，这是一项行为变化。

**`capability.py`**：新增 `C03Capability.evaluate_transition(...)` 和结果类型 `TransitionDetermination`。
- 这是 WP-009 设计要求的"每一次重要转换之前的判定"。
- 判定顺序：先做控制判定（紧急停止 → 撤销 → 控制状态未知）。只有在没有任何控制生效时，才进入身份关口。
- 进入身份关口时，`kill_active` 固定为 `False`，因为紧急停止已在前一步判定过。
- 结果类型自己保证以下约束：
  - 不会授权执行；
  - 被控制阻断时没有关口结果，状态为 `BLOCKED`，原因与控制判定相同；
  - 只有控制判定恰好是“无控制生效”（`PROTECTED_BLOCKED` 加对应原因）时，才有关口结果，并原样报告；
  - 关口结果的状态只能是 `BLOCKED`、`REJECTED` 或 `ELIGIBLE_FOR_MAPPING`；非 `ELIGIBLE_FOR_MAPPING` 时，允许写入的命名空间必须为空。

## 需要所有者在验收时一并确认的取值

1. **秘密标记表**（不区分大小写，按子串匹配字符串值）：`-----begin`、`bearer `、`authorization:`、`password=`、`password:`、`secret=`、`secret:`、`token=`、`token:`、`api_key=`、`api_key:`、`apikey=`、`private_key`；嵌套上限 8 层。
   - 这是一份固定的表，不是通用的秘密检测器。
   - 已有意去掉 `basic `，因为它容易误判普通文字。
2. **完整性比较**：
   - 对象类别只认上述 4 种；
   - 十六进制字母不区分大小写；
   - 观察值缺失时隔离（依 §12）；引用本身无效时阻断。
3. **转换前判定的顺序**：先控制，后关口。没有控制生效时才评估关口，并以 `kill_active=False` 调用。
4. **接入范围**：只把控制判定和身份关口接成转换前判定。以下各判定函数仍是模块函数，没有做成能力门面的方法：幂等、超时、回滚、取代、依赖、分类、完整性、审计链。原因是能力层本身没有这些转换；它们应当在各自的转换发生处调用，也就是以后的集成阶段。

## 文件身份

| 文件 | V6（已验收） | V7 |
| --- | --- | --- |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `C6E03A8AB0305B83F6042D8F8E379AE91047D41F4AB3467AC0A7281E7E4DA48E` | `A4A5861BD9042316C04C3247C9FA4839B9D097A5D14BEDD185A7BDBE1E24A5FE` |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `0A7E937AB514D865FB71306C368168F9D06B0BC091150FA22C7EA7F24A699FE6` | `FB5528D6FE5794BDDF55E99B6EBA26B8899BE377F997F2AFE198C3DCA02A5DE8` |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `8D0B3CD664A893609EDCEFABADCD48EAA77DEF6B519872DA27E9E15F68EA7686` | `E4EA6A90D6E8B18E7242F3C7D782F554AEF94B9C55AA731B83FEF0CB5E849DB6` |

其余 7 个源文件未变。

## 本地验证（Linux，CPython 3.13；正式运行必须使用 3.12.10）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/c03_v7/C03_V7_INPUT_CANDIDATE_REV8.json` | 247676 | `572D9C7DA572EE12FDAD7E0B70205744DFFE67AA90BDC6AA96F3786B92EB0BED` |
| `validation/route_b_c03/wp_008/c03_v7/harness_rev8.py` | 30299 | `C4086A40D985C3D4CDA2A155AF11646476871B9A3361C71C859C64ED489FF9DA` |
| `validation/route_b_c03/wp_008/c03_v7/build_input_rev8.py` | 13520 | `0B465904FA955459D3104E99800464C8E677122F282B9E07534F9357F939B4FA` |

- **Harness REV8 运行结果**：退出码 0；93 个变体全部通过：13 个完全符合，13 个部分符合，67 个不映射；运行时拦截 0 次，被测代码扫描 CLEAN。
- **新增 17 个原始检查变体**，都不映射 Fixture，所以覆盖等级没有变化：

| 场景 | 新增 | 检查内容 |
| --- | --- | --- |
| V-003 | 1 | 授权（激活决定）引用过时 |
| V-005 | 4 | 嵌套键名、值中的授权头、列表中的 PEM 标记，以及一个干净的嵌套对照 |
| V-012 | 7 | 审计链重复、分叉；输出散列篡改、依赖身份篡改；一致、未知类别、观察缺失 |
| V-009、V-010 | 3 | 转换前判定：撤销、紧急停止、控制状态未知 |
| V-001 | 1 | 转换前判定：没有控制时进入关口，未配置的能力被阻断 |
| V-015 | 1 | "已采纳事实"标签被拒绝 |

- **Harness REV8 相对 REV7 的代码变化**（已写入文件头说明）：
  - 输入与 3 个被测文件的散列；
  - 2 个适配器；
  - 返回类型 `TransitionDetermination`；
  - 类型为 `"None"` 的规则，只在调用无异常且返回 `None` 时通过；
  - 输出版本字符串。

## 局限

- **作用范围没有绑定。** `subject_scope` 由调用方提供，没有与配置或输入包绑定。调用方可以传入另一个范围，绕开只作用于某个范围的紧急停止，然后以 `kill_active=False` 进入关口。这并不比 V6 弱（V6 中 `kill_active` 本来就由调用方直接提供），但需要知道。
- **秘密标记是固定表，会有误判和漏判。**
  - 误判例：`idempotency token: X`、`secret: none`、`private_key_ref`。
  - 漏判例：`password = x`（等号两侧有空格）、`Bearer` 后跟制表符、`x-api-key:`、`api-key=`、`passwd=`、`Basic …`，以及 `ghp_`、`sk-`、`AKIA`、`eyJ` 之类的前缀。
- **嵌套键名检查沿用原有禁止词表**，所以合同中真实存在的字段 `history_preservation`（含 `history`）如果出现在嵌套层，也会被隔离。
- **以下情形不检查**：字节串的子类、重写了 `casefold` 的字符串子类、重写了 `lower` 的键名子类、字典视图、生成器、任意对象。如果映射的 `items()` 本身抛出异常，结果是该异常，而不是隔离。
- **V-001 的转换变体只比较状态和原因**，没有比较关口结果内部的字段。

- 转换前判定的变体使用默认的 `C03Capability()`（没有配置），所以"没有控制生效、关口放行"这一路径没有在门面上观察到；关口本身的放行路径已由原有的关口变体覆盖。
- 秘密标记只查字符串值，不检查自定义对象的内部；字节串无法在 JSON 输入中表达，所以"字节串拒绝"只有代码，没有运行变体。
- 8 个部分覆盖场景仍是部分覆盖，原因见关闭证据包第四节。

## 审查与处理

审查记录：`.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_V7_REVISION_REVIEW_REV1.md`。结论：通过，附说明；无阻断项。

| 意见 | 处理 |
| --- | --- |
| 1 文件身份表排版错误 | 已改正，三列齐全 |
| 2 `TransitionDetermination` 的约束弱于记录所述 | 已收紧：检查控制状态与原因的精确类型；“有关口结果”与“无控制生效”严格对应；限制关口状态；非放行状态下写入命名空间必须为空 |
| 3 作用范围没有绑定 | 写入局限 |
| 4 `assert_reference_only` 的行为变化与漏查 | 顶层非映射改为隔离；其余写入局限；层数说法已改正 |
| 5 观察值缺失时不隔离，偏离 §12 | 改为隔离（`INTEGRITY UNCERTAIN`），相应规则在构建脚本中同步修改 |
| 6 接入只完成一部分 | 已在文首写明 |
| 7 标记表误判和漏判 | 写入局限 |
| 8 V-001 变体没有比较关口内容 | 写入局限 |
| 9 工作区有未提交的正式运行脚本 | 随正式运行 v6 资产一并提交 |

修改后重新构建输入并运行：输入 REV8 的 SHA 变为上表所列值，93 个变体全部通过，分布不变。
