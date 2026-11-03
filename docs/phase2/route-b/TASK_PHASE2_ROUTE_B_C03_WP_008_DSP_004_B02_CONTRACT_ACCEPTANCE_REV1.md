# DSP-004 B-02 类型合同与数组政策：审查与接受

按所有者决定 P3-CONTRACT，记录人对类型合同 REV3 和数组政策 REV3 做了在库审查。审查者是一个没看过编写过程的全新子代理，与记录人属于同一模型家族，不是外部审查。审查**没有发现阻断项**，所以 P3-CONTRACT 的条件已经满足：这两份文件按下列确切 SHA 记为**所有者已接受**。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_B02_CONTRACT_ACCEPTANCE_REV1.json` | 5225 | `54CF25C86DBB6B1DC296BCCA9E8813F5B20EF835B1203905EF52FFE5E9B0CA04` |

| 已接受的文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md` | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` |

## 1. 审查结果

审查结论：没有阻断项。审查清点的数量：41 个命名类型；Entry 有 15 个字段；合同中有 32 条数组路径，与登记中的 32 条政策一一对应，没有遗漏、多余或重复；其中 ORDERED 5 条，SET_SORTED 27 条。

| 编号 | 级别 | 所见 | 状态 |
| --- | --- | --- | --- |
| 1 | MAJOR | entry_id 'category prefix' never defined (contract:334, inherited from Plan V2.2:286) | open; must be fixed by the bound identifier source or read as set membership before Manifest generation |
| 2 | MAJOR | InputContract.binding fixes the path SCENARIO_INPUT_BINDING.json (contract:311-313, 461), while P4-DRAFT keeps the new input in a separate file | open; needs an owner decision before Manifest generation |
| 3 | MINOR | startup step ordinal not explicitly tied to array position | open |
| 4 | MINOR | three fixed sets called sets; shape fixed only by registry | open |
| 5 | MINOR | some array sizes stated only in the registry | open |
| 6 | MINOR | cross-reference contract:518 should point to section 5.1 | open |
| 7 | NOTE | layout line shortened but unambiguous | none |
| 8 | NOTE | no hard-coded 3.12.13; environment_acceptance should point to phase-1 admission | none |
| 9 | NOTE | no real provider required | none |
| 10 | NOTE | no LIMITED must be eliminated | none |
| 11 | NOTE | files grant no admission, run or Manifest | none |
| 12 | NOTE | five ORDERED source values still empty; blocks Manifest generation, not acceptance | open for Manifest |
| 13 | NOTE | sampled claims match Plan V2.2 and Package V3.2 | none |

## 2. 接受的范围

接受的是这两份文件在上述确切字节下的设计文本，作为 B-02 的类型合同和数组政策，供以后的 Manifest 工作使用。

在生成 Manifest 之前，还要先解决三件事：
- 第 1 项：`entry_id` 的"类别前缀"要有确定的定义；
- 第 2 项：合同写死的输入路径（`SCENARIO_INPUT_BINDING.json`）与新的输入候选文件不一致，需要所有者决定；
- 5 条 ORDERED 路径的实际序列来源还是空的。

这次接受不准入来源，不生成 Manifest，也不授权运行。

## 3. 阶段 4 的开发性试运行（不是证据）

REV39 绑定规则之后，记录人在自己的 Linux 容器里（Python 3.13）把 Harness REV1 跑了一次，只为检查 Harness 本身。结果：28 个变体全部符合预先声明的规则；20 个变体与 Fixture 预期一致，其余 8 个按设计不做映射。这次运行用的不是已准入的 CPython 3.12.10 环境，所以不是证据。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/dsp004_phase4_harness_rev1/devrun1_container_py313.json` | 19750 | `469F62C02F6B3690B641768DA9EF6C319D50C27826FA319D9FAC846AA73D1FAA` |

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 的类型合同和数组政策已按确切 SHA 接受；ORDERED 来源和上面第 1、2 项仍待解决。
