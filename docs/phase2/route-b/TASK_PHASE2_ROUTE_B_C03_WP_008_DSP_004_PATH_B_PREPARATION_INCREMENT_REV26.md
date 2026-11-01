# DSP-004 路径 B 筹备增量 REV26

本增量记录一项筹备事实：第二版 T0 演练已运行，结果为 `PASS_T0_DRY_RUN_V2`。运行后独立审查把它定性为**非证据性的工程观察**。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。OD-04 状态保持 `OD04_A_DRY_RUN_OBSERVATION_NOT_EVIDENCE`。DSP-004 保持 `OPEN / HOLD`。

现行范围句子：`授权第二版 T0 演练：按独立审查列出的条件修订监督程序，运行前先审查并把确切字节提交绑定，再由所有者以管理员身份运行一次安装器、运行一次监督下的清单探测。不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004；不改动系统审计策略。` 另有所有者以 `重试` 一词授权的重试，记在结果记录第 1 节。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV25.md` |
| 前一增量说明 | `68C15AC811B7FCBD2E1715C6E01E313AC1BB689FC12A0239FCFBF49541C801E2`（2922 字节） |
| 前一增量 JSON | `58DA5D11A44FC773CDBF94F4CBB0AA3EBB79B7372EF1BB0E90508585295FE9B2`（6744 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV26.json` |
| 本增量 JSON SHA-256 | `250021F33339614AC6EB2E4C9518FAB8571857581292445C1B4916802B4684C9` |
| 本增量 JSON 字节 | 6262 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04A_V2_DRY_RUN_PASSED_NON_EVIDENTIARY_OBSERVATION`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04A_T0_DRY_RUN_V2_RESULT.md` | 5370 | `99F0BB962950DAD0A40B324D5E750AAECDC96179CA55D7AE877CEBFFF86DD19E` |
| `validation/route_b_c03/wp_008/DSP_004_OD04A_T0_DRY_RUN_V2_RESULT.json` | 20187 | `E0A9B86D49DBFC2333733E0A02C2AF76F9B7D267BDDCE4AC06AE4B036000AD3B` |

三份原始记录按原样字节提交在 `validation/route_b_c03/wp_008/dsp004_od04a_t0_dry_run_v2/`。

## 2. 结论摘要

- 23 项核对全部成立；运行前后两次外部取回核对，已安装文件都与预先绑定的版本一致。
- 与第一版相比，以下问题已有记录支撑地关闭或基本关闭：提权状态（IR-04）、探测脚本位置（IR-12）、先绑定后运行（IR-10）、从外部核对模块（IR-02）、环境与参数（IR-05）、目录树与访问控制（IR-06）、签名（IR-08）。
- 仍然存在的问题：监督程序为自己作证（IR-01 的核心）、同一账户篡改（IR-03）、KnownDLLs（IR-07）、普通用户组授权（IR-14）、没有系统写下的旁证、只在所有者电脑上运行了一次。

要成为证据还缺的六项，写在结果记录第 6 节。

## 3. 本增量故意不做的事

- 不准入任何证据，不改 OD-04 状态，不改动系统审计策略，不再运行任何程序。
- 不生成 Manifest，不正式运行，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
