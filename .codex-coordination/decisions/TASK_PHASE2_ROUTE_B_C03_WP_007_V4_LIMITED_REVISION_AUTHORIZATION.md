# Route B C03 WP-007 V4 有限修订授权

| 字段 | 值 |
| --- | --- |
| 决定 | 授权一次有限实现修订（V4），只修正安全/隐私边界审查 REV1 中的 B1、B2、N1、N2 |
| 决定人 | Project Owner（张纯熙），2026-11-04，在记录人的问题中选择"修 B1、B2 和 N1–N2（推荐）"；选项由记录人 Claude 起草 |
| 依据 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_SECURITY_PRIVACY_BOUNDARY_REVIEW_REV1.md`（结论 FAIL） |
| 记录人 | Claude，`RECORDER_ONLY` |
| 效力 | 只授权修订与随后的审查和验证准备；不接受 V4，不关闭 AR-B-007，不激活 C03 |

## 修订范围

| 编号 | 问题 | 修订 |
| --- | --- | --- |
| B1 | 能力状态的检查是排除名单，未知状态可以通过网关 | 构造时校验网关输入记录（能力配置、授权包、输入信封）中枚举字段的类型；网关改为只放行 `ENABLED_CAPABILITY_ONLY` |
| B2 | 外层封装把终止状态默认为"未终止" | 去掉默认值；网关只把严格等于 `False` 的终止标志视为未终止 |
| N1 | 审计脱敏是弱排除名单，必填字段不校验，可以绕过构造函数 | 校验移入 `AuditRecordCandidate.__post_init__`；除 `input_artifact_references`（默认空元组）与 `supersedes`（默认 `NONE`）外各字段必填；扩充敏感词，增加身份证号、手机号、银行卡号、密钥前缀的识别 |
| N2 | 网关不检查制品就绪状态与有效期窗口 | 网关检查授权包有效期窗口，并要求每个输入制品已就绪、已验证 |

不在范围内：N3、N4（映射相关）和全部注记，保持为已知局限，留待以后处理。

## 需要所有者在验收 V4 时一并确认的设计澄清

原设计没有规定以下取值。V4 采用关闭失败的取法，这些取法需要在验收时一并确认：

1. 制品就绪的取值：`readiness_state` 必须等于 `READY`，`validation_state` 必须等于 `VALIDATED`，其他取值一律阻断。
2. **输入制品集合为空时阻断**，阻断原因为 `BLOCKED — READINESS/PROVENANCE FAILURE`。
3. 授权包的 `valid_from` 和 `valid_until` 必须是 `YYYY-MM-DDTHH:MM:SSZ` 格式的 UTC 时间，且前者早于后者。
4. 网关新增必填参数 `evaluated_at`（同样格式），由调用方提供；需满足 `valid_from ≤ evaluated_at < valid_until`，否则阻断，原因为 `BLOCKED — AUTHORITY FAILURE`。网关自身不读时钟，保持纯函数。
5. `C03Capability.evaluate_gate` 的 `validity_confirmed`、`kill_active`、`evaluated_at` 三个参数都没有默认值。

## 后续步骤（各自另需决定）

1. V4 实现记录与全新子代理审查，包括重做安全/隐私边界检查。
2. 输入 REV5：更新散列，补充覆盖 B1、B2、N1、N2 的变体。Harness REV5：更新固定散列、新增适配器。
3. 约束清单 v3、Manifest REV2、安装器与监督程序，然后由所有者授权正式运行 v3。
4. 正式运行结果的验收，以及 AR-B-007 的关闭决定。

AR-B-007 保持 `OPEN / BLOCKED`；C03 保持 `NOT READY`。
