# Route B C03 V6 修订审查 REV1（V-015 分类边界）

| 字段 | 值 |
| --- | --- |
| 审查对象 | 分支 `feat/c03-v015-v6`，提交 `e08ed7e` |
| 审查者 | 全新上下文子代理（Claude，与记录人同一模型家族，**不是外部审查**），只读 |
| 结论 | **PASS WITH NOTES**：无阻断项，3 个非阻断项，若干注记 |

## 已核实

- **失败即关闭**：14 种类别请求 × 15 种处置，共 210 种组合，全部得到"候选 `HUMAN_REVIEW_PENDING`、`downstream_blocked is True`"。
  - 类别请求包括：`str` 子类、同值的仿冒枚举成员、成员值原始字符串、禁止类别的大小写与空格变体、`None`、整数、字节串、枚举类本身、其他枚举的成员、空字符串；
  - 处置包括：大小写与空格变体、`str` 子类、`"REQUEST_CORRECTION"`、`"APPROVE"`、带句号的批准原文、元组、字节串、整数、枚举成员；
  - 原因：`type(...) is` 判断先于任何 `in` 或 `==`；禁止类别即使配上"批准"也仍被拒绝。
- **`CandidateRecord`**：拒绝原始字符串、`str` 子类、仿冒枚举、`"FINAL_LEGAL_OPINION"` 和 `None`。
- **其他**：导入和调用期间不打开文件；没有新增模块；在全新解释器中先导入 `isolation` 也正常。
- **三项取值**：与 §14.1、§16.1–16.3 一致。Fixture 的 `HUMAN_REVIEW_PENDING_DOWNSTREAM_BLOCKED` 与 §14.1 的 `REJECTED` 之间的张力，以"请求拒绝、候选待审"两层状态公开处理，记录和规则的 `mapping_basis` 都写明了。
- **`FULL` 覆盖等级**：有先例可援（V-005、V-014 也以纯函数观察加声明局限记为 `FULL`；V-003 也把 Fixture 抽象映射到原生状态），但见 N1、N2。
- **Harness REV7 相对 REV6**：代码变化全部在文件头声明（输入与被测文件散列、新适配器、新返回类型、枚举字典比较分支、覆盖等级读取顺序、输出版本字符串）。新的枚举字典分支不会把原有失败变成通过：REV6 的 55 条规则中没有一条在 `state`/`type` 以外使用字典期望值，所以只影响 V6 的 6 条新规则。
- **可重现**：构建脚本生成的输入为 215,603 字节、SHA `C1A32F95…30FD`、76 个变体，与提交一致。REV6 → REV7 只有：重算散列（24 个对象的 `source_sha256` 和各适配器的被测文件散列）、新适配器、6 条规则和 6 个变体、V-015 的覆盖等级与理由。原有 55 条规则和其他场景逐字节不变。
- **运行**：退出码 0，76/76 通过；13 完全符合，13 部分符合，50 不映射；0 失败，0 拦截，被测代码扫描 CLEAN（CPython 3.13.18，非正式运行要求的 3.12.10）。
- **记录**：10 个源文件散列和 3 个验证资产的散列、大小都正确；总数和 6 个变体的描述准确。

## 非阻断项

- **N1 V-015 旧局限文字未更新。** 输入 REV7 中 V-015 的旧局限说明（"CandidateRecord 没有法律分类评估器""Fixture 的禁止分类请求仍不可评估"）和 `binding_state: PARTIAL_OBSERVABLE` 仍在，与 `coverage_class_rev7: FULL` 并存，理由没有调和这一矛盾。建议新增 `coverage_limitations_rev7` 或明确豁免。
- **N2 `FULL` 依赖的测试较弱。** Fixture 映射变体通过，只是因为评估器拒绝一切非白名单值；`LEGAL_ADVICE_OR_DOWNSTREAM_AUTHORITY` 得到的是通用原因 `CLASS NOT PERMITTED`，而不是 `PROHIBITED CLASS`。也没有真实生成候选的路径。只有所有者接受"独立纯函数加构造校验"即为完全覆盖，`FULL` 才成立，应作为第 1 或第 2 项取值的一部分写明。
- **N3 `ClassificationDetermination` 不自行保证不变量。** 冻结数据类没有 `__post_init__`，直接构造 `downstream_blocked=False` 可以成功（已实测）。评估器本身不会这样做，但"下游永远阻断"只对评估器的输出成立，对类型本身不成立。

## 注记

- **未另签设计。** RDM-DSP-012 提出"另签非法律推理的分类边界设计"；V6 依据现有 §16，并把语义（两层状态、原因码）写进代码。所有者对三项取值的确认实质上就是该设计的签署，记录应写明。
- **既有弱点（非 V6 引入）**：`CandidateRecord` 只对 `downstream_blocked` 做真值判断，`"no"` 可以通过；建议改为 `is not True`。
- **非批准处置不影响结果。** 对允许的类别，`REJECT`、`KEEP BLOCKED`、`REQUEST CORRECTION` 都返回"CANDIDATE CLASS PERMITTED — HUMAN REVIEW PENDING"。这是安全的，但人工"拒绝"在结果中不留痕迹。
- **工作区有未跟踪文件** `c03_v6/prepare_formal_v5.py`，不在 `e08ed7e` 中，超出本次审查范围，提交前应处理。
- **记录小缺口**：没有列出 Harness 的代码变化（只给了散列），也没有提到新增的 `.gitattributes`。

## 处理

见实现记录 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_MATERIALIZATION_RECORD_REVISION_V6_CANDIDATE.md` 的"审查与处理"一节。
