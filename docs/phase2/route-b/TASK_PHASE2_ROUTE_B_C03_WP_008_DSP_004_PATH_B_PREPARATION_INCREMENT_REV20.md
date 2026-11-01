# DSP-004 路径 B 筹备增量 REV20

本增量记录两项筹备事实：

1. Project Owner 张纯熙改签了路径 B（签署记录 REV2），授权一次只读清单探测运行；
2. 这次探测已经运行，结果作为候选记下。

结果不改 OD-04。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。本增量不接受资产，不准入来源或运行根，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

现行范围原句：`改签路径 B：以本机 CPython 3.12.10 为验证机候选，授权一次只读清单探测运行（只读取解释器版本、内置与冻结模块、实际加载模块来源），不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

此前范围原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV19.md` |
| 前一增量说明 | `9ED3A2DC4492F1E5C6249A488AF5CE79DDE3EB51579EC12780B5B4505D159124`（4341 字节） |
| 前一增量 JSON | `89320D6FA5C82C4996A58DCF0BEED538A28D2D66D1EEA81E8411BB3393D743D5`（8001 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV20.json` |
| 本增量 JSON SHA-256 | `DCC28F38A9FF71DE7AA3D305ADF788C7558C43E61F266611B28B543DB2B22577` |
| 本增量 JSON 字节 | 6954 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

前一增量 JSON 的重新散列与 REV19 说明里写下的 SHA 相同。相符不是接受。

## 1. 新增筹备事实

| 事实 | 文件 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| `PATH_B_SCOPE_RESIGNED_REV2_INVENTORY_PROBE_ONLY` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV2.md` | 2127 | `2D3941021A15BB7116466531B7840171D420288332A29F773A61DE34F7BFD099` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV2.json` | 2034 | `58C9600334D18A39F771EFDBD43CC396B3DFCD77E7E3B6881D656E6672211992` |
| `OD04_INVENTORY_PROBE_REV1_OBSERVED_NOT_ADMITTED` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04_INVENTORY_PROBE_REV1_RESULT.md` | 4914 | `A2A1EEE1B9D4C2F7571D43E630C1E4E66F2675F0BDA64DC086F1830DA3DC7843` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_OD04_INVENTORY_PROBE_REV1_RESULT.json` | 18137 | `E33211D39A7A279DFEA4878A0E2A2792354C8F5287C5912E4A18174E3A2F6D9A` |

探测结果机器记录有 6 项字段核对，全部相符。

## 2. 探测补上了什么、还缺什么

补上的（仍是候选）：

- 解释器版本 3.12.10 已由运行确认；隔离参数全部生效。
- 已加载的 8 个运行时原生模块与 REV19 静态 SHA 全部一致。
- 本次加载的 22 个系统 DLL 已取得 SHA。
- 冻结模块清单已在本机核实：`os`、`stat`、`ntpath`、`codecs`、`io`、`abc` 等实际从 `python312.dll` 的冻结副本运行。
- 实际加载的 Lib 模块已观察；另有 2 个按名字加载的编码模块，已补上散列。

仍缺的：

- T0：Python 启动前、在解释器之外完成的核验。
- 两侧调用身份中调用方一侧。
- 检查到使用的防替换：Lib 目录可写，字节码缓存可能被读取。

## 3. 需要所有者留意

1. 签署记录 REV2 的原句由记录人起草、所有者选定，不是所有者逐字写出的。机器记录如实标注了这一点。
2. 探测还对已加载的原生模块做了只读散列，略超出原句列出的三项。记录人在运行前说明过，所有者随后运行了探测。
3. REV2 只授权一次探测，已经用掉了。之后任何运行都需要所有者重新授权。

## 4. 本增量故意不做的事

- 不改 OD-04 或其他 OD 记录，不改签署记录 REV1 的字节。
- 不准入本机或其运行时，不接受任何 SHA。
- 不生成 Manifest，不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不在仓库保存含本机路径的原始结果。不改商业 P0。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
