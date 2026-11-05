# Route B C03 实现记录 V7（候选：能力层测试缺口与控制接入）

本版依据所有者决定 AR-B-008-V7-FIRST（`.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_AR_B_008_V7_FIRST_DECISION.json`）制作，目的是在决定 AR-B-008 之前，补上关闭证据包 REV1 第四节列出的能力层缺口，并把控制判定接入 `capability.py`。

本版尚未审查，也未接受。AR-B-008 保持 `OPEN / BLOCKED`。正式运行需要所有者另行授权。

## 修改内容

**`failures.py`**
- 新增 `evaluate_integrity(subject_kind, *, expected_sha256, observed_sha256)`，对应 V-012 计划中的"输出散列、依赖身份"篡改。
  - 对象类别只认 4 种：`IDENTITY`、`OUTPUT`、`DEPENDENCY`、`AUDIT_REFERENCE`。
  - 散列不一致时为 `QUARANTINED — INTEGRITY FAILURE: <类别>`。
  - 观察值缺失或格式错误时为 `PROTECTED_BLOCKED`，不隔离。
  - 一致时仍是 `PROTECTED_BLOCKED`，并注明"未授权执行"。
  - 这个函数只比较调用方提供的散列，本身不读取也不计算任何输出或依赖。

**`isolation.py`**：`assert_reference_only` 由只查顶层键名，扩展为：
- 每一层嵌套的字典键名都检查（沿用原来的禁止词表）；
- 字符串值中如果出现秘密标记，就隔离；
- 字节串一律拒绝；非字符串键名一律拒绝；
- 嵌套超过 8 层也拒绝。

**`capability.py`**：新增 `C03Capability.evaluate_transition(...)` 和结果类型 `TransitionDetermination`。
- 这是 WP-009 设计要求的"每一次重要转换之前的判定"。
- 判定顺序：先做控制判定（紧急停止 → 撤销 → 控制状态未知）。只有在没有任何控制生效时，才进入身份关口。
- 进入身份关口时，`kill_active` 固定为 `False`，因为紧急停止已在前一步判定过。
- 结果类型自己保证以下约束：
  - 不会授权执行；
  - 被控制阻断时没有关口结果；
  - 只有在没有控制生效时，才原样报告关口结果。

## 需要所有者在验收时一并确认的取值

1. **秘密标记表**（不区分大小写，按子串匹配字符串值）：`-----begin`、`bearer `、`authorization:`、`password=`、`password:`、`secret=`、`secret:`、`token=`、`token:`、`api_key=`、`api_key:`、`apikey=`、`private_key`；嵌套上限 8 层。
   - 这是一份固定的表，不是通用的秘密检测器。
   - 已有意去掉 `basic `，因为它容易误判普通文字。
2. **完整性比较**：
   - 对象类别只认上述 4 种；
   - 十六进制字母不区分大小写；
   - 观察值缺失时阻断而不隔离。
3. **转换前判定的顺序**：先控制，后关口。没有控制生效时才评估关口，并以 `kill_active=False` 调用。
4. **接入范围**：只把控制判定和身份关口接成转换前判定。以下各判定函数仍是模块函数，没有做成能力门面的方法：幂等、超时、回滚、取代、依赖、分类、完整性、审计链。原因是能力层本身没有这些转换；它们应当在各自的转换发生处调用，也就是以后的集成阶段。

## 文件身份

| 文件 | V6（已验收） | V7 |
| --- | --- | --- |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `4083702B31623A38B4D2CB36F3038B85F66A3725E404205AED8AA2E226F921A7` |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `3B5769A25500D3C21535F542C387E6CE362B4C40FB6AF4D06872BD730F939E2B` |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `CA93D99B407BEC4F4F0796EB70C2B2A61E878FE545EB1120F9C06BF3E02AD81F` |

其余 7 个源文件未变。

## 本地验证（Linux，CPython 3.13；正式运行必须使用 3.12.10）

| 资产 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/c03_v7/C03_V7_INPUT_CANDIDATE_REV8.json` | 247690 | `33A84CDBCBBBC51A5A83745997F80FCBE89FBB51F54D14BCFE322A6E042DC4A4` |
| `validation/route_b_c03/wp_008/c03_v7/harness_rev8.py` | 30299 | `557B1CDFB28D419FF172590C723273FF2DB0FFCE175BB903CA06C3842C14B8D1` |
| `validation/route_b_c03/wp_008/c03_v7/build_input_rev8.py` | 13534 | `118B3ACBA1C284D3012D2F9170F6D987CDFF928C86916D1C34EE00DE79261C68` |

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

- 转换前判定的变体使用默认的 `C03Capability()`（没有配置），所以"没有控制生效、关口放行"这一路径没有在门面上观察到；关口本身的放行路径已由原有的关口变体覆盖。
- 秘密标记只查字符串值，不检查自定义对象的内部；字节串无法在 JSON 输入中表达，所以"字节串拒绝"只有代码，没有运行变体。
- 8 个部分覆盖场景仍是部分覆盖，原因见关闭证据包第四节。
