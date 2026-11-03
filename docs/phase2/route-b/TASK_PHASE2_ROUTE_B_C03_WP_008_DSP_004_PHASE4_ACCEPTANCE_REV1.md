# DSP-004 阶段 4 接受与两项合同决定

第二版（输入候选 REV4、Harness REV2）的审查**没有发现阻断项**。审查者是全新子代理，与记录人属于同一模型家族。所有者随后作出三项决定：接受阶段 4，并就类型合同的两项重要问题作了决定。

| 机器记录 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_PHASE4_ACCEPTANCE_REV1.json` | 5428 | `983BBB1813E92A7BE831944ACBB00F42404F5CA3397516EBCFD7AF366A696F64` |

## 1. 已接受

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json` | 115428 | `685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1` |
| `validation/route_b_c03/wp_008/dsp004_phase4_harness_rev2/harness_rev2.py` | 22043 | `4A4B859405D31AD5716615E7FE5FF0330143BB48F2AAB83BC487CC9CE786D7B7` |

接受的范围：这两个文件作为阶段 4 的输入和 Harness，供以后在已准入的阶段 1 环境中做受监督的正式运行。这次接受不生成 Manifest，也不授权运行。正式运行使用的 Harness 修订版，要保持这里的输入和比较逻辑不变，并补上下表中的问题。

## 2. 审查确认的内容

第一版的两个阻断项都已真正修好。审查者故意放进了下列错误，新版都能正确判为失败或不予执行：
- 错误的枚举类；
- `str` 的子类；
- 仿冒的类；
- 用列表冒充元组；
- 用 `True` 冒充 `1`；
- `ValueError` 的子类；
- 残留的 `.pyc` 字节码。

另外，在 Python 3.12 和 3.13 上，输出除版本号外完全一致。审查者人工抽查了 13 个变体，全部吻合。

## 3. 留待正式运行前修好的问题

| 编号 | 问题 |
| --- | --- |
| MINOR-1 | guard misses os.open with write flags, os.startfile, truncate, link/symlink, utime, sqlite3, tempfile |
| MINOR-2 | docstring/binding over-claim: exec/compile not blocked; hook can be disarmed from inside; scan bypassable via module attributes |
| MINOR-3 | a guard denial does not force FAIL or change the exit code |
| MINOR-4 | pass-with-mapping-mismatch not counted; mapped OBSERVE_ONLY would go to partial bucket |
| MINOR-5 | lenient compare for rule shapes absent from REV4 (null expected, empty requirement, True==1 in construct, CR-014 prefix) |
| NOTE-1 | observation shows class names only |
| NOTE-2 | six-side Consistent compares harness constants |
| NOTE-3 | some stops exit 3 not 2; BaseException escapes |
| NOTE-4 | applies_to not checked against variant id |

## 4. 两项合同决定

| 编号 | 所有者的选择 |
| --- | --- |
| P6-INPUT-PATH | 生成 Manifest 时，输入绑定指向 `validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json`。这项决定取代已接受类型合同 REV3 中写死的 `SCENARIO_INPUT_BINDING.json`（合同第 311–313、461 行；登记第 115–116 行）。合同文件本身不改。 |
| P6-ENTRY-ID | `entry_id` 的"类别前缀"不另定格式规则。只要 `entry_id` 属于绑定的标识来源集合（合同第 58 行），就算格式合规。这解决了合同审查的第 1 项。 |

生成 Manifest 之前，仍需补齐 5 条 ORDERED 路径的实际序列来源（AP-006、AP-009、AP-020、AP-021、AP-022）。

DSP-004 保持 `OPEN / HOLD`。
