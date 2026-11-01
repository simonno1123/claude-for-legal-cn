# DSP-004 路径 B 筹备增量 REV25

本增量记录两项筹备事实：

1. Project Owner 张纯熙授权第二版 T0 演练（签署记录 REV4）。
2. 第二版的全部程序在运行之前已经审查，确切字节已经绑定。

任何第二版程序都还没有运行。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

现行范围句子：`授权第二版 T0 演练：按独立审查列出的条件修订监督程序，运行前先审查并把确切字节提交绑定，再由所有者以管理员身份运行一次安装器、运行一次监督下的清单探测。不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004；不改动系统审计策略。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV24.md` |
| 前一增量说明 | `226A21365D1D4DDDF073AC00F4FBE56D12F4C0B442443104B6C19D52C7E61479`（4239 字节） |
| 前一增量 JSON | `A6CD76B4491D764242D583F1F8EDA0CE2A94E7F8057669D293552163CB05ED87`（6927 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV25.json` |
| 本增量 JSON SHA-256 | `58DA5D11A44FC773CDBF94F4CBB0AA3EBB79B7372EF1BB0E90508585295FE9B2` |
| 本增量 JSON 字节 | 6744 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

| 事实 | 文件 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| `PATH_B_SCOPE_RESIGNED_REV4_V2_DRY_RUN` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV4.md` | 1632 | `BC6847FFC87D6927E5EEA4AF33CE2AFC5C010AB337714BC0A23E5D39E96E00FB` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV4.json` | 2535 | `3A8381FE940FA3107AA01C35C850D5BA471D5A919F7FDE6D9FF5A29CB124F86A` |
| `OD04A_V2_BOUND_BEFORE_RUN_NOT_ADMITTED` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04A_T0_DRY_RUN_V2_PRE_RUN_BINDING.md` | 4488 | `0B5651A2FA586ACB0BF7D31A36376CE39664A149AE13F803EBEE34D3AF9879ED` |
| 同上 | `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_V2_PRE_RUN_BINDING.json` | 28299 | `C19A15FF8EB51314F7C5CA9197CB8CEEFF923FFF0B38E0F857F9580BF8A5723E` |

## 2. 与第一版相比

- 这次的顺序是先审查、再提交绑定、最后运行，纠正了 REV24 指出的 IR-10。
- 运行时标准库已与 CPython 官方 v3.12.10 源码逐一核对，全部一致。
- 运行前审查认为代码层面可以运行，但结果上限仍是非证据性的工程观察。

## 3. 本增量故意不做的事

- 不运行任何程序，不改动环境，不改动系统审计策略。
- 不准入任何证据，不生成 Manifest，不正式运行，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
