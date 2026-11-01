# DSP-004 路径 B 筹备增量 REV22

本增量记录一项筹备事实：Project Owner 张纯熙为 OD-04 选择了 `OD04-A`。选择已记下，尚未打开任何后续交付物。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

现行范围原句：`改签路径 B：以本机 CPython 3.12.10 为验证机候选，授权一次只读清单探测运行（只读取解释器版本、内置与冻结模块、实际加载模块来源），不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV21.md` |
| 前一增量说明 | `AB3495AA66A3EFCE27ED261AC01C9013188D5CA57080AE7082760CECE668F4CE`（3545 字节） |
| 前一增量 JSON | `34D613D88566BA2417CF5F73D1E9B4D83D3DEFE3E338617A91631A17148665C6`（5836 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV22.json` |
| 本增量 JSON SHA-256 | `A3B5721CA683D8F333AB84A47DC7553AAF652A59ED1550F47E17A912C181AC39` |
| 本增量 JSON 字节 | 5763 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04_OPTION_A_SELECTED_RECORDED_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04_OPTION_DECISION_REV1.md` | 2268 | `83B1B10DA26885A93909A335E8EE7F7B20D9CF69FCC010FB9CD4D79FBBDC0018` |
| `validation/route_b_c03/wp_008/DSP_004_OD04_OPTION_DECISION_REV1.json` | 2788 | `AB89F775ED43E80B00B1F68DFAA6D25C6EADD6505EB5606E4A09236B6E20C826` |

## 2. OD-04 现状

OD-04 由 `DEFER_WITHOUT_EVIDENCE` 变为 `OD04-A` 已选、尚未打开。证据仍未补足。

下一步需要所有者分别授权：

1. 以管理员身份建立专用运行时目录并设置访问控制（会改动本机）；
2. 编写并审查外层监督进程，绑定编译产物的 SHA；
3. 用监督进程做一次只跑清单探测的 T0 演练。

## 3. 本增量故意不做的事

- 不打开上述任何一项，不改动环境，不写代码，不运行程序。
- 不改其他 OD 决定。
- 不准入运行根，不接受任何 SHA，不生成 Manifest，不授权正式运行，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
