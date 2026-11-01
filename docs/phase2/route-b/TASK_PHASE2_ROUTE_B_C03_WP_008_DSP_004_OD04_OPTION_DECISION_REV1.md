# DSP-004 OD-04 选项决定记录 REV1

本记录写下 Project Owner 张纯熙对 OD-04 的选择：`OD04-A`。选择本身不准入任何东西，也不打开后续交付物。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

现行范围原句：`改签路径 B：以本机 CPython 3.12.10 为验证机候选，授权一次只读清单探测运行（只读取解释器版本、内置与冻结模块、实际加载模块来源），不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 所有者原话 | `a` |
| 原话语境 | 回复记录人列出 A（推荐）、B、C 三个选项的提问，2026-10-31 18:48（美国太平洋时间）。同一条回复没有回答是否合并 PR #26 |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_OD04_OPTION_DECISION_REV1.json` |
| 机器记录 SHA-256 | `AB89F775ED43E80B00B1F68DFAA6D25C6EADD6505EB5606E4A09236B6E20C826` |
| 机器记录字节 | 2788 |
| 选项来源 | `validation/route_b_c03/wp_008/DSP_004_OD04_T0_AND_CHECK_TO_USE_DESIGN_CANDIDATE_REV1.json` |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 选择

| 选项 | 内容 | 选中 |
| --- | --- | --- |
| `OD04-A` | 管理员专用目录的运行时副本 + 运行期持有文件句柄 + 空字节码前缀目录 + 外层监督进程完成 T0 和两侧身份 | 是 |
| `OD04-B` | 同 A，运行时改用官方可嵌入版 | 否 |
| `OD04-C` | 维持 `DEFER_WITHOUT_EVIDENCE` | 否 |

OD-04 由此前的 `DEFER_WITHOUT_EVIDENCE` 变为 `OD04-A` 已选、尚未打开。`Decided` 是 true，`Opened` 是 false。证据仍未补足。

## 2. 选择没有授权的事

- 建立专用运行时目录，或改动任何访问控制；
- 编写或编译外层监督进程；
- 运行任何程序，包括 T0 演练；
- Manifest、正式运行、FA-08、关闭 DSP-004。

## 3. 下一步需要所有者分别授权

1. 以管理员身份建立专用运行时目录并设置访问控制（会改动本机）；
2. 编写并审查外层监督进程，绑定编译产物的 SHA；
3. 用监督进程做一次只跑清单探测的 T0 演练。

其他 OD 决定不变。DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
