# AR-B-007 关闭证据包 REV1（候选）

AR-B-007 是 C03 平台层（Tier A）的阻断项"适配器与 C03 实现"，对应工作包 C03-CP-WP-007。本文件把关闭所需的证据，逐项对照计划 §7.7 的退出门禁，供所有者决定是否关闭。本文件由记录人 Claude 起草（`RECORDER_ONLY`），本身不关闭任何事项。

## 一、证据清单

| 证据 | 文件 | SHA-256（前 16 位） | 状态 |
| --- | --- | --- | --- |
| 实现设计（C03-CP-E-008） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN.md` | `BD4BCC607CBFE99A…` | 已采纳 |
| 实现设计审查 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN_REVIEW.md` | `5A7E290A6DE71B2A…` | 通过 |
| 实现设计采纳决定 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_IMPLEMENTATION_DESIGN_ADOPTION_DECISION.md` | `71911C4B56C4C1D1…` | 所有者决定 |
| 实现记录 V3（C03-CP-E-009） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_007_WP_009_MATERIALIZATION_RECORD_REVISION_V3.md` | `4B67889AF50273EF…` | 已接受 |
| 实现记录 V3 审查 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_WP_009_MATERIALIZATION_REVIEW_REVISION_V3.md` | `62A5BF7855C27EEE…` | 通过 |
| 安全/隐私边界审查 REV1 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_SECURITY_PRIVACY_BOUNDARY_REVIEW_REV1.md` | `E05C2C4CBEE4FBC0…` | FAIL（2 个阻断项） |
| V4 有限修订授权 | `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_WP_007_V4_LIMITED_REVISION_AUTHORIZATION.md` | `4D062B831D17A182…` | 所有者决定 |
| 实现记录 V4（候选） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_007_WP_009_MATERIALIZATION_RECORD_REVISION_V4_CANDIDATE.md` | `89492F303321A994…` | **待验收** |
| V4 修订审查（含安全边界复查） | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_WP_007_V4_REVISION_REVIEW_REV1.md` | `7E1B8321915F5330…` | PASS WITH NOTES，意见已处理 |
| 依赖清单 Manifest REV2 | `validation/route_b_c03/wp_008/ar_b_007_v4/PYTHON_RUNTIME_DEPENDENCY_MANIFEST_REV2.json` | `55308C77DBF8AB04…` | 已接受 |
| V4 所有者决定 | `validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_OWNER_DECISIONS_REV1.json` | `D387C931C2CA978F…` | Manifest 接受，正式运行授权 |
| 正式运行 v3 结果 | `validation/route_b_c03/wp_008/ar_b_007_v4/C03_V4_FORMAL_RUN_V3_RESULT.json` | `1832BF88C660569A…` | PASS，**待验收** |

## 二、退出门禁对照（计划 §7.7）

| 门禁 | 证据 | 是否满足 |
| --- | --- | --- |
| 独立的设计审查 | 实现设计审查与采纳决定 | 满足 |
| 实现审查 | V3 审查与接受；V4 修订审查 | 满足；V4 待所有者验收 |
| 安全/隐私边界审查 | REV1 发现 2 个阻断项，V4 已修正；V4 修订审查逐条复核了 6 项关闭失败条件，全部成立 | 满足（复核由修订审查完成，没有另出单独一份边界审查报告） |
| 确切的文件与依赖散列 | Manifest REV2；正式运行 v3 实际导入的模块与 Manifest 完全一致 | 满足 |
| 所有者实现验收 | — | **待所有者决定** |

## 三、关闭失败条件（计划 §7.7）

| 条件 | 当前状态 |
| --- | --- |
| 行为或数据结构超出合同 | 没有发现 |
| 上游写入集合非空 | 为空：代码没有任何输入输出，正式运行中拦截 0 次 |
| 隐藏的推断或默认值 | REV1 发现的两项（B1、B2）已修正，正式运行的变体已覆盖 |
| 凭据泄露 | 没有发现；审计脱敏有已知局限（排除名单式），见 V4 实现记录 |
| 未绑定的依赖 | 没有；正式运行的导入闭包等于 Manifest |
| 自我授权的路径 | 没有发现 |

撤回条件（依赖漏洞、设计漂移、散列变化、授权撤销、验证失败）：目前都没有触发。

## 四、需要所有者知道的几点

- **全部审查都来自与记录人同一模型家族的全新子代理，没有外部审查。** 计划 §7.7 没有明确要求外部审查；DSP-004 关闭时做过一次外部审查，但那次审查针对的是 V3 代码。
- **已知局限照旧保留**：映射相关的 N3、N4；脱敏只能拦住已列出的写法；就绪状态、有效期和评估时间由调用方提供，网关不独立核实。
- **关闭 AR-B-007 只关闭平台层 3 个阻断项中的 1 个。** AR-B-008（运行验证）、AR-B-009（恢复与审计控制）和 Tier B 的 7 项仍未关闭，C03 仍为 `NOT READY`，不会自动推进到下游。
