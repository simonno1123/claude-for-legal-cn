# DSP-004 路径 B 筹备增量 REV21

本增量记录一项筹备事实：OD-04 剩余三项（T0、两侧调用身份、检查到使用的防替换）的设计候选已经写下，并为 OD-04 起草了一张可以勾选的选项表。它只是设计文档，不选择选项，不实现代码，不改动环境，不运行程序。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。

现行范围原句：`改签路径 B：以本机 CPython 3.12.10 为验证机候选，授权一次只读清单探测运行（只读取解释器版本、内置与冻结模块、实际加载模块来源），不接受资产、不生成 Manifest、不正式运行、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV20.md` |
| 前一增量说明 | `2C541D8982905393BEC867CCE4C1ED8378F86282A8258BCBD75EC18C779757F4`（4332 字节） |
| 前一增量 JSON | `DCC28F38A9FF71DE7AA3D305ADF788C7558C43E61F266611B28B543DB2B22577`（6954 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV21.json` |
| 本增量 JSON SHA-256 | `34D613D88566BA2417CF5F73D1E9B4D83D3DEFE3E338617A91631A17148665C6` |
| 本增量 JSON 字节 | 5836 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04_T0_AND_CHECK_TO_USE_DESIGN_CANDIDATE_REV1_RECORDED_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04_T0_AND_CHECK_TO_USE_DESIGN_CANDIDATE_REV1.md` | 7483 | `55834EE899B61FE4300BBD890205BF9696F312411826E8759E39E79D4A6D5C5F` |
| `validation/route_b_c03/wp_008/DSP_004_OD04_T0_AND_CHECK_TO_USE_DESIGN_CANDIDATE_REV1.json` | 5110 | `F3B40E76C245A91F09EA2D88C985CE828A06FAA49AB15A0012B9528CFF097B9E` |

## 2. 设计要点

- **防替换**：两层强制来源。第一层是管理员专用目录加访问控制，普通进程写不进去；第二层是运行期间由外层监督进程以禁止写入和删除的方式持有全部绑定文件。另外用空的字节码前缀目录，让解释器不读取 Lib 里的缓存。
- **T0**：由外层监督进程在 Python 启动之前完成：散列核对、访问控制快照、锁文件、记录时间点，然后用固定参数启动 Python。任何一项不符都阻止启动。
- **两侧调用身份**：监督进程记录自身身份；对子进程，核对系统查询到的主映像路径、父进程号，以及子进程原样回传的一次性随机数。

## 3. 待所有者勾选

| 选项 | 内容 |
| --- | --- |
| `OD04-A`（记录人推荐） | 管理员专用目录的运行时副本 + 持有文件句柄 + 空字节码前缀目录 + 外层监督进程 |
| `OD04-B` | 同 A，运行时改用官方可嵌入版 |
| `OD04-C` | 维持现状 |

选 A 或 B 之后，还需要所有者分别授权：建立专用目录并设置访问控制（需要管理员身份，会改动本机）；编写并审查监督进程；做一次只运行清单探测的 T0 演练。

## 4. 本增量故意不做的事

- 不选择 OD-04 选项，不改 OD-04 记录。
- 不实现代码，不改动环境，不运行程序。
- 不准入运行根，不接受任何 SHA，不生成 Manifest，不授权正式运行，不关闭 DSP-004。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
