# DSP-004 路径 B 筹备增量 REV19

本增量只记录路径 B 下的下一项筹备事实：OD-04 的本机固定运行时候选观察已经写下。观察对象是所有者本机上一个按用户安装的 CPython 3.12.10。它是候选，不是证据准入，不改 OD-04。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。它不接受资产，不准入来源或运行根，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本次授权是：2026-10-31，Project Owner 张纯熙说明本机装有 Python，指示继续 OD-04。所有者通过访问提示，批准了对本机按用户安装的 CPython 文件夹和系统 DLL 文件夹的只读访问。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV18.md` |
| 前一增量说明 | `A3699A567AEEB36187FDB7877BFC50862E77A98F4C75D165E80B5619F9E59E05`（5092 字节） |
| 前一增量 JSON | `54608E042A7AC33FD9E9A4C8D0F088673245270007ADB0403FBC451FD03FCDCE`（8529 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV19.json` |
| 本增量 JSON SHA-256 | `89320D6FA5C82C4996A58DCF0BEED538A28D2D66D1EEA81E8411BB3393D743D5` |
| 本增量 JSON 字节 | 8001 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

前一增量 JSON 的重新散列与 REV18 说明里写下的 SHA 相同。相符不是接受。REV1 至 REV18 已经记下的筹备事实保持原样。

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04_LOCAL_FIXED_RUNTIME_CANDIDATE_OBSERVATION_REV1_RECORDED_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04_LOCAL_FIXED_RUNTIME_CANDIDATE_OBSERVATION_REV1.md` | 6197 | `75845A476D1B88B4C136886A7030982B0F173BD71215CC35C56FECA84EB540D3` |
| `validation/route_b_c03/wp_008/DSP_004_OD04_LOCAL_FIXED_RUNTIME_CANDIDATE_OBSERVATION_REV1.json` | 54439 | `6F99BAE833A112D982667C30EE9D9FCC53037EF41CA13362EC0AE6FA5E602C34` |

观察机器记录有 6 项字段核对，全部相符。相符只是字段一致，不是接受。

## 2. OD-04 六个组成部分，REV18 与 REV19 对照

| 组成部分 | REV18（仓库记录） | REV19（本机候选） |
| --- | --- | --- |
| 导入闭包 | 部分，仅直接导入文本 | 导入时闭包闭合：68 个 Lib 文件已散列；全边上界未闭合 |
| 两侧调用身份 | 无 | 无 |
| 检查到使用的防替换 | 无 | 无；Lib 可写，有字节码缓存，部分模块从冻结副本加载 |
| T0 | 无 | 无 |
| PE | 部分，仅 5 个文件的身份 | 44 个 PE 文件的身份和导入表；两个读取器一致 |
| OS | 无 | 只有 23 个系统 DLL 和 14 个 API-set 的名称；字节因硬链接未取得 |

## 3. 需要所有者留意

1. 本机不是记录中的验证机。如果今后想用本机做验证机，需要由所有者另行决定，并重新建立项目工作副本和验证环境。本增量不作这个决定。
2. 候选运行时是固定安装的，不会像原来的工具缓存那样被自动替换，满足 REV18 指出的前提条件。但 Lib 目录对当前用户可写，而且有字节码缓存，所以要建立检查到使用的防替换，还需要另外的冻结或权限措施。
3. 两侧调用身份和 T0 必须在受控条件下运行解释器才能取得。路径 B 没有授权运行，本增量也不运行。

## 4. 本增量故意不做的事

- 不改 OD-04 或任何其他 OD 记录，不改 OD-05 `REFUSE_LOCATOR`。
- 不把本机或其运行时准入为验证环境，不接受任何 SHA。
- 不写本机绝对路径，只用根令牌加相对路径。
- 不生成 Manifest，不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不运行解释器，不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不改商业 P0。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
