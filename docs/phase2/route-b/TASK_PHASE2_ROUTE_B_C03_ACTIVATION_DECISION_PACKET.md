# C03 激活决定包（C03-CP-E-015，R3）

| 字段 | 值 |
| --- | --- |
| 证据编号 | `C03-CP-E-015` Activation Decision Packet |
| 依据 | 已接受的最终就绪复核 E-014（`docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_FINAL_READINESS_REVIEW.md`）；接受决定 `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_FINAL_READINESS_REVIEW_ACCEPTANCE_DECISION.md` |
| 所有者已作的选择（2026-11-13） | R-01：只申请能力激活；R-02：V8-A 纳入激活绑定；R-03：先选择"按 E-014 执行"（R2）；2026-11-13 所有者又选择"解除挂钩"，依据时效改为只约束案件级操作，见 `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AUTHORITY_FRESHNESS_SCOPE_AMENDMENT.md`（R3） |
| 起草 | Claude（记录人） |
| 状态 | **R3 已评审**。PR #119 经 Codex 评审后，所有者 2026-11-13 作出新激活决定 `C03-CP-D-015`，取代 `C03-CP-D-014`。本文件本身不激活 C03 |

## 一、拟激活的内容

| 项目 | 内容 |
| --- | --- |
| 激活语义 | **CAPABILITY_ONLY**（激活语义决定，2026-08-30） |
| 最大效果 | 启用下列确切版本的 C03 能力，调用关口保持关闭。所谓关闭，是指凡没有满足 Tier B 的确切案件授权包的调用，一律拒绝 |
| 明确不产生的效果 | 不接触任何案件材料；不生成任何候选；不作任何下游使用；不授权任何案件级执行（包括 CASE-D）；不构成长期权限；不改变 AR-B-010 逐项授权的要求 |
| 案件级使用的前提 | 每次都要另行提交 Tier B 的确切案件授权包，经新的独立决定链批准（计划 §3.1、§5；激活语义决定 §2）。在批准之前，E-014 第五节之二中标为 B 的各项必须已经处置，或由所有者明确接受 |

## 一之二、依据时效（R-03，按修订说明）

| 规则 | 内容 |
| --- | --- |
| 能力激活 | 能力激活不引用法律依据，不受依据时效约束，也不因依据过期而失效 |
| 案件级操作 | 包括 Tier B 授权包、候选复核、AR-B-010 逐项授权、案件级执行。每次开始时，都必须有在有效期内的依据时效包；已过期的，先重新核对依据。R2 复核清单 C4 和 R3 §9.2 的有效截止照常适用 |

## 二、绑定的确切版本

### 2.1 已验收实现（V7）

来源：`TASK_PHASE2_ROUTE_B_C03_TIER_A_CLOSURE_DECISION.json` 的 `AcceptedImplementation`，已在当前提交上逐一复算，全部一致。

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

### 2.2 V8-A（所有者选择纳入，R-02）

| 文件 | SHA-256 |
| --- | --- |
| `scripts/phase2_runtime/route_b_c03/gate_records.py` | `97B2BE912A35B84C41AE540D07F60AD998BE9B77F5D1E5AC25FA39E2B141E053` |
| `scripts/phase2_runtime/route_b_c03/gate_record_builder.py` | `1AF01E83A368EE3EC74D3C5067F973DE080E507252D18D3AC9D29B011DFAC27E` |
| `scripts/phase2_runtime/route_b_c03/gate_cli.py` | `09EA81FA8A6F78BBE7C4A0533177E3897589A8BC9EF7D5685C395944E53798E0` |

### 2.3 验证证据

Tier A 正式运行 v6：

| 文件 | SHA-256 |
| --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_AR_B_008_CLOSURE_EVIDENCE_PACKET_REV1.md` | `4F45F231C34C709FC0241BDC844FC0084D833239EF2A0E436C51BAD7AE8993FF` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_AR_B_008_CLOSURE_EVIDENCE_PACKET_REV2.md` | `BB46DD2FDAC93B67B2B206EB0500D16620CAD34651CA4898235EB6C009E49F00` |
| `validation/route_b_c03/wp_008/c03_v7/C03_V7_FORMAL_RUN_V6_RESULT.json` | `29EC91E712022E29897F0A0EFBCAAA7FEC78B76932DADCD06B154090C1A86AD2` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_MATERIALIZATION_RECORD_REVISION_V7_CANDIDATE.md` | `48DD57D9040425E5A19D9161599952EFF2BEAC07FE164EC7034A6028D6D8118F` |
| `validation/route_b_c03/wp_008/c03_v7/C03_V7_INPUT_CANDIDATE_REV8.json` | `572D9C7DA572EE12FDAD7E0B70205744DFFE67AA90BDC6AA96F3786B92EB0BED` |
| `validation/route_b_c03/wp_008/c03_v7/harness_rev8.py` | `C4086A40D985C3D4CDA2A155AF11646476871B9A3361C71C859C64ED489FF9DA` |
| `validation/route_b_c03/wp_008/c03_v7/formal_v6_run/install_formal_v6_result.json` | `389552F2785887853E4864C588BFD87094FCA5500AFDB90E78D842D31387A73A` |
| `validation/route_b_c03/wp_008/c03_v7/formal_v6_run/formal_v6_pre_collect_result.json` | `A215E59E53D7AFAF093B110D44BB7310090260396C3E44C15F1EAB06D40C4A2C` |
| `validation/route_b_c03/wp_008/c03_v7/formal_v6_run/formal_v6_post_collect_result.json` | `CCB0F77616F770300FD5F0D85530B155B3ACF7BFA2BF754005D0EA7EDAC7F1DD` |
| `validation/route_b_c03/wp_008/c03_v7/formal_v6_run/formal_v6_run_record.RAW_REDACTED.json` | `3BB10960E4C85B6017F1AB3E5B7674749C0F663E61FC5ED8D0B6E56C23A82888` |
| `validation/route_b_c03/wp_008/c03_v7/formal_v6_run/formal_v6_events_history.RAW_REDACTED.xml` | `D4CF10394B282345321AF98CCCDD6DCC2443FCFC3DB67ADF959AD92427083147` |

V8-A 测试与覆盖：

| 文件 | SHA-256 |
| --- | --- |
| `validation/route_b_c03/v8/test_gate_records.py` | `D339AB690E6CB0564513E6570971C55D9BB6C2BD2B5734B4FE91DF351109F24C` |
| `validation/route_b_c03/v8/ANNEX_A_COVERAGE.md` | `91EE60F926D8DE4436AAD4964E3C63E6EC8F8C29F0AFA08E3391C78CBA16FFA8` |
| `validation/route_b_c03/v8/RECORD_CONTRACTS.md` | `61E751ABD4B808404E83427E7413676718F9CA2CD5FA54C5FC7A90451C250948` |

### 2.4 绑定的治理文件

| 文件 | SHA-256 |
| --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_FINAL_READINESS_REVIEW.md` | `42C7604182762C912CD6C963599DD0DA160F84EF71C5C1599D9EAA392A0878BF` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AR_B_005_HUMAN_REVIEW_GATE_PACKET_R3.md` | `1029BD425BDBC10DD641FA4AC6A85A2845E75AD0C17B7FABA1342C3E49C0CFEB` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_V8_GATE_ENFORCEMENT_DESIGN.md` | `002F2173453062CABD99C53A660BAEBDE5A8005E8FAC4DB488B568BCAC34755F` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_PREREQUISITE_CLOSURE_PLAN.md` | `D27B8D6CFF4B4F39B6A34E34D61E691183B12FB03529F6AC665F20A54CA28329` |
| `.codex-coordination/decisions/TASK_PHASE2_ROUTE_B_C03_ACTIVATION_SEMANTICS_DECISION.md` | `ABD65E645CD8D7B91FCC7BFEEC472317CA56B0B3749CFDFFD8249E9DE007BDCF` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_AUTHORITY_FRESHNESS_SCOPE_AMENDMENT.md` | `72A3C88C8B2B150EE4E2AF7E5D680E1453C6660137FC3F4C703948E973A140AA` |

## 三、未结阻断项登记

| 阻断项 | 状态 |
| --- | --- |
| AR-B-001 | 即本次激活决定 |
| AR-B-002 至 AR-B-009 | 已关闭，多数带局限，见 E-014 第二节 |
| AR-B-010 | 逐项关口，不能整体关闭；每一次输出、每一个动作都要另行决定 |

截至本决定包，没有记录任何撤回、kill 或失效事件。

## 四、撤回与失效条件

出现下列任一情形，激活即失效，回到"未激活"：

1. 所有者撤回；
2. 第二节绑定的任何一个文件（V7 的 10 个实现文件、V8-A 的 3 个文件、验证证据和治理文件），其 SHA-256 发生改变；
3. kill 或撤回状态生效；
4. 计划 §7.7、§7.8、§7.9 所列的撤回条件出现，即依赖漏洞、设计漂移、配置或环境改变、证据失效、控制版本改变、审计完整性失败；
5. 发现身份不符。

失效之后，必须重新复核、重新作出激活决定，才能恢复。

## 五、继续适用的局限

E-014 第六节和第五节之二所列的局限全部继续适用。其中：

- 一人集中；
- V8-B 暂缓；
- 运行时机制和隔离层未验证；截断审计链是已知缺陷；
- 依据时效有 30 日上限，只约束案件级操作（第一节之二）。

## 六、需要所有者作出的决定

是否按本决定包激活 C03（CAPABILITY_ONLY）。
