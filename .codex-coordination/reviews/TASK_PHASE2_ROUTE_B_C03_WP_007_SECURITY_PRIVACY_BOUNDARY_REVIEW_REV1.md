# Route B C03 WP-007 安全/隐私边界审查 REV1（AR-B-007 关闭门禁）

| 字段 | 值 |
| --- | --- |
| 依据 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN.md` §7.7 退出门禁"security/privacy boundary review" |
| 审查对象 | `scripts/phase2_runtime/__init__.py`、`scripts/phase2_runtime/route_b_c03/*.py`，共 10 个文件，main `29a9ebb`；与已接受 Manifest REV1 的 SUBJECT_SOURCE 散列全部一致 |
| 审查者 | 全新上下文子代理（Claude，与记录人同一模型家族，**不是外部审查**），只读 |
| 记录人复核 | 记录人已在源码中核实 B1、B2（`identity_gate.py:35-44`；`capability.py:41`；`contracts.py:113-130`） |
| 结论 | **FAIL**：2 个阻断项，4 个非阻断项，4 个注记 |
| 效力 | 只是审查记录。AR-B-007 保持 `OPEN / BLOCKED`；不授权任何修改 |

## 逐项失败条件

1. **超出合同**：没有超出合同的行为。有几处做得比合同要求少，见 N1–N4。映射执行状态恒为 BLOCKED，提供方为空且不可注入。
2. **上游写入**：为空。代码没有文件、网络、环境、进程或全局状态写入；网关决定允许写入的命名空间恒为空。
3. **隐藏默认或推断**：**违反**，见 B1、B2。
4. **凭据与泄露**：不处理凭据，异常信息不回显输入值。脱敏只靠一个较弱的排除名单，见 N1。
5. **依赖**：只用标准库，并且全部在 Manifest 内；没有 eval、exec、importlib、subprocess、ctypes 或网络调用。
6. **自我授权**：代码不会自行设置启用状态或批准状态；候选记录只能处于"待人工复核"；释放只能进入禁用态；终止和撤销需要释放权限。

## 阻断项

**B1：能力状态的检查是排除名单，未知状态会通过网关**
- 位置：`identity_gate.py:35-44`。代码只排除 DISABLED、REVOKED、STALE 三种状态。
- 原因：`CapabilityConfigurationReference` 不检查 `state` 的类型（`contracts.py:113,117-130`）。
- 后果：
  - 传入字符串 `"DISABLED"`（例如来自 JSON）或 `"BOGUS"`，结果都是 `ELIGIBLE_FOR_MAPPING`。
  - 由于状态不等于枚举值 ENABLED，构造时也不会要求提供启用决定的引用。
- 违反：不变式 II-001、II-004（未知输入应当关闭失败）。
- 修正：只放行 `state is CapabilityState.ENABLED_CAPABILITY_ONLY`，并在 `__post_init__` 中校验所有枚举字段的类型。

**B2：终止状态默认是"未终止"**
- 位置：`capability.py:41`，`kill_active: bool = False`。
- 后果：调用方不传这个参数时，网关返回 `ELIGIBLE_FOR_MAPPING`。底层函数 `evaluate_identity_gate` 把它列为必填，只有外层封装加了默认值。
- 违反：设计 §13，终止状态应当由独立来源提供。
- 修正：去掉这个默认值。

**目前的实际影响有限**：ELIGIBLE 不会触发任何动作，C03 也没有激活。但这两项都符合计划中"关闭失败"条件的字面要求。

## 非阻断项

**N1 审计脱敏**
- 脱敏只靠子串排除名单，漏掉了 `api_key`、`credential` 和中文个人信息。
- `redaction_state` 由调用方自行声明。
- 必填字段没有校验非空。
- `AuditRecordCandidate` 可以绕过构造函数直接创建。

**N2 网关检查不全**：网关不检查输入制品的就绪状态与来源（设计 §14.1），有效期也只依赖调用方传入的布尔值。

**N3 映射与网关没有绑定**：
- `apply_mapping_rule` 可以直接调用；
- 授权检查只要求一个非空字符串；
- 隔离辅助函数从未被调用，内容型字符串可能经 `DIRECT_COPY` 原样传出。

**N4 映射合同的缺口**：
- 没有要求 `enumeration_version`；
- 重复键会静默覆盖；
- `True == 1` 可能导致类型串用；
- `null_policy`、`conflict_policy`、`human_review_required` 没有执行；
- 两个布尔字段有默认值（方向是安全的）。

## 注记

- 映射追踪对值做不加盐的 SHA-256，取值较少时可被字典还原。
- `FailureRecord` 和 `GateDecision` 直接构造时，可以放进不安全的值；目前没有代码路径这样构造。
- 隔离检查的异常信息中会出现键名（不含值）。
- 重试只依赖调用方传入的布尔值，并且从不实际执行重试。

## 隐私

代码不读取、不保存案件内容。但内容可能经由字符串字段流转（N1、N3），审计层不能可靠地拦住。

## 与 DSP-004 的关系

DSP-004 正式运行的 28 个变体没有覆盖 B1、B2 这两种输入（原始字符串或未知状态、未传终止状态）。正式运行通过不代表这两项没有问题；这是那次验证的覆盖缺口。

## 修正的影响

任何修正都会改变受测源码的散列，因而需要依次重做：
1. 有限修订授权；
2. 新的实现记录与审查；
3. 新的 Manifest；
4. 重新运行验证；
5. 重新审查。
