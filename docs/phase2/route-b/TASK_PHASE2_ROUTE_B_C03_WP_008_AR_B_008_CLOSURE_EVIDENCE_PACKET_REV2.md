# AR-B-008 关闭证据包 REV2（带局限，V7 之后）

本文件是关闭证据包 REV1（`docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_AR_B_008_CLOSURE_EVIDENCE_PACKET_REV1.md`）的更新版。REV1 之后，所有者决定先做 V7（AR-B-008-V7-FIRST）。V7 已完成实现、审查和正式运行 v6，结果通过。本文件只写与 REV1 不同的部分，其余内容沿用 REV1：
- §7.8 的要求（REV1 第一节）；
- 场景类别与标签的说明；
- 部分覆盖的两种原因；
- 移交、撤回条件与关闭后果的框架。

本文件由记录人 Claude 起草（`RECORDER_ONLY`），本身不关闭任何事项。AR-B-008 保持 `OPEN / BLOCKED`，直到所有者另行作出决定。

## 一、证据更新

| 证据 | 文件 | 状态 |
| --- | --- | --- |
| V7 实现记录 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_MATERIALIZATION_RECORD_REVISION_V7_CANDIDATE.md` | **待验收** |
| V7 修订审查 | `.codex-coordination/reviews/TASK_PHASE2_ROUTE_B_C03_V7_REVISION_REVIEW_REV1.md` | PASS WITH NOTES，意见已处理 |
| 输入 REV8、Harness REV8、Manifest REV5、政策 REV5 | `validation/route_b_c03/wp_008/c03_v7/`；`docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_C03_V7_MANIFEST_SUPPORT_POLICIES_REV5.md` | Manifest、政策与四项取值已接受（V7-ACCEPT-MANIFEST） |
| 验证执行授权 | `validation/route_b_c03/wp_008/c03_v7/C03_V7_OWNER_DECISIONS_REV1.json`（V7-RUN-FORMAL-V6） | 已签发 |
| 观察到的验证结果（E-011，同时作为 V7 散列下的 E-013） | `validation/route_b_c03/wp_008/c03_v7/C03_V7_FORMAL_RUN_V6_RESULT.json` | PASS，**待验收** |

**正式运行 v6 的结果**
- 输入与覆盖：CPython 3.12.10；输入 REV8 的散列与绑定一致；93 个变体全部通过，覆盖全部 15 个场景，其中 V7 新增的 17 个全部通过。
- 锁定与检查：锁定 863 个文件，散列和签名都没有问题；监督程序 29 项检查全部通过。
- 导入与运行时：实际导入的 96 个模块与 Manifest REV5 一致；与 v5 相比，只有 `__main__` 和项目路径不同；运行时拦截 0 次，被测代码扫描 CLEAN。
- 系统审计：审计记录编号 65637 到 79061 连续，共 13425 条；自 v5 以来没有失败登录。全部进程以普通权限运行，退出码都是 0。启动脚本只调用了一次。

可重现性的边界与 REV1 相同：每个版本只运行过一次，没有同一版本的重复运行。

## 二、REV1 第四节"能力层内仍可补充的验证"的处理

| 项目 | V7 的处理 | 正式运行 v6 |
| --- | --- | --- |
| 审计链的重复记录与分叉 | 新增 2 个变体（代码原已拒绝） | 通过 |
| 输出散列、依赖身份篡改 | 新增 `evaluate_integrity`：不一致时隔离，观察值缺失时也隔离（依 WP-009 §12）；另有 5 个变体 | 通过 |
| 值本身与嵌套结构中的秘密 | `assert_reference_only` 现在检查各层键名和字符串值，标记表固定为 13 个；另有 4 个变体 | 通过 |
| 身份引用（授权引用）过期 | 新增 1 个变体：激活决定引用过时，关口拒绝 | 通过 |
| "已采纳事实"标签 | 新增 1 个变体：被拒绝，原因是"不是允许的成员" | 通过 |
| 接入 `capability.py` | 新增 `evaluate_transition`：先判控制，后过关口；新增 3 个变体，与 V-001 的 1 个对照 | 通过 |

**仍然存在的局限**（详见 V7 实现记录"局限"一节）：
- `subject_scope` 没有绑定；
- 秘密标记表会有误判和漏判；
- 嵌套键名检查会误伤 `history_preservation`；
- 转换前判定只在未配置的能力上观察过；
- 其余约 8 个判定函数没有接入 `capability.py`，留到集成阶段；
- 截断的审计链如果附带它自己的链头，仍会通过。

## 三、覆盖情况

覆盖等级没有变化：7 个场景完全覆盖，8 个部分覆盖。V7 新增的变体都是不映射 Fixture 的原始检查，所以不改变场景的覆盖等级。它们缩小的是每个场景"未验证的内容"，具体如下（其余场景与 REV1 第四节相同）：

| 场景 | REV1 的未验证项 | 现在 |
| --- | --- | --- |
| V-003 | 授权引用过期没有单独的变体 | 已有变体 |
| V-005 | 嵌套结构和值本身中的秘密 | 已检查，限于固定标记表 |
| V-012 | 重复、分叉、输出散列、依赖身份 | 已有变体；截断链、持久化、运行中的检测与隔离仍未验证 |
| V-009、V-010 | 只有独立的判定函数 | 已通过能力门面上的转换前判定验证；传播时间与信号机制仍未验证 |
| V-015 | "已采纳事实"标签没有测试 | 已有变体 |

## 四、AR-B-007、AR-B-009 在 V7 散列下的效力

自两项关闭以来，被测源码的变化如下：

| 文件 | 自 AR-B-007 关闭（V4）以来 | 自 AR-B-009 关闭（V5）以来 |
| --- | --- | --- |
| `contracts.py` | V5、V6 修改 | V6 修改 |
| `failures.py` | V5、V7 修改 | V7 修改（只新增 `evaluate_integrity`，原有函数未改） |
| `isolation.py` | V6、V7 修改 | V6、V7 修改 |
| `capability.py` | V7 修改 | V7 修改 |
| 其余 6 个文件 | 未变 | 未变 |

- **AR-B-007**：撤回条件包括"散列变化"，所以照字面已回到开放状态（REV1 第三节已说明）。
- **AR-B-009**：撤回条件包括"控制版本变化"，而控制判定所在的 `failures.py` 已被 V7 修改。照字面，这一项现在也应视为回到开放状态。

**依据。** 正式运行 v6 在当前散列下重新运行了两项涉及的全部变体，全部通过。关口、映射、隔离、候选和审计变体属于 AR-B-007；撤销、紧急停止、幂等、超时、回滚、取代、审计链和依赖变体属于 AR-B-009。

**提议。** 在当前散列下重新关闭 AR-B-007 和 AR-B-009，范围和局限与原关闭决定相同，并加上 V7 实现记录中的局限。当前散列如下：

| 文件 | SHA-256 |
| --- | --- |
| `scripts/phase2_runtime/__init__.py` | `49B8B1BD319B6424323AD0EDC04B3969D71196CD8D69E12C16D5442B17340844` |
| `scripts/phase2_runtime/route_b_c03/__init__.py` | `F669613D65267EC5D4D42CB79008EB510307A99B20E40EE13E9E1E0E404A504D` |
| `scripts/phase2_runtime/route_b_c03/contracts.py` | `144841285C8E7ED88BED930FD01FB314863DFE8B2F67BDF3C73D816BE5423A99` |
| `scripts/phase2_runtime/route_b_c03/identity_gate.py` | `F9CC7021C1A2586611FBCA7333F8ADC8BDE3A6436663680EEA100CA26EDC9C31` |
| `scripts/phase2_runtime/route_b_c03/mapping.py` | `320F7E8576C1C4E81B4E78E6058000E4D720173948BE736AD846B8CAD664EC66` |
| `scripts/phase2_runtime/route_b_c03/isolation.py` | `FB5528D6FE5794BDDF55E99B6EBA26B8899BE377F997F2AFE198C3DCA02A5DE8` |
| `scripts/phase2_runtime/route_b_c03/failures.py` | `A4A5861BD9042316C04C3247C9FA4839B9D097A5D14BEDD185A7BDBE1E24A5FE` |
| `scripts/phase2_runtime/route_b_c03/audit.py` | `96F874FD494AA67276604A8AD49813F68B7BF4F2C28E63FC9D6C6ECE127C44DA` |
| `scripts/phase2_runtime/route_b_c03/provider_port.py` | `66E4DA862BBBD50380B17686DB6BC2AB6D5D3B861AB53FCDDE1B608F86DEA381` |
| `scripts/phase2_runtime/route_b_c03/capability.py` | `E4EA6A90D6E8B18E7242F3C7D782F554AEF94B9C55AA731B83FEF0CB5E849DB6` |

## 五、带局限关闭需要所有者承担的偏离（更新 REV1 第六节）

1. **退出门禁**：8 个场景只部分覆盖，完全覆盖的 7 个场景也各有局限；审查不是外部审查。与 REV1 相同。
2. **证据**：以正式运行 v6 同时作为 E-011 和当前散列下的 E-013。
3. **目标**：已缩小，但没有消除。现在接入能力门面的只有转换前判定，其余判定函数仍是独立调用的模块函数。

**移交项。** 以下各项作为待办项和剩余风险，列入最终就绪审查（`C03-CP-E-014`）：
- REV1 第四节"未验证的内容"一列中，本文件第三节没有消除的部分；
- 本文件第二节列出的局限。

**撤回条件、关闭后果**：与 REV1 第六节相同。关闭后，Tier A 的 3 个阻断项全部关闭，全部 10 个阻断项中关闭 3 个。C03 只是可以申请最终就绪审查授权（C03-TA-D-017），不会因此激活，下游的自动转换继续阻断。

## 六、需要所有者一并决定的事项

1. 验收正式运行 v6 的结果和 V7 实现。
2. 在当前散列下重新关闭 AR-B-007 和 AR-B-009（第四节）。
3. 带局限关闭 AR-B-008（第五节），或者继续保持开放。

**记录人的建议：三项都同意。** 能力层范围内可以补的验证已经补完。剩下的局限要等能力层以外的机制出现，继续开放也推进不了。
