# DSP-004 路径增量 REV30

本增量记录一项事实：所有者本人运行了阶段 1 的环境准备脚本。新建了普通账户 `dsp004val`，开启了进程创建和进程结束审计，审计事件包含命令行。这是环境准备，不是运行证据。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_INCREMENT_REV29.md` |
| 前一增量说明 | `5A11945ED8505640962B4F0EC10E99ACB19A88CDDFFB0CFDEC25EF5A7C509CBB`（2151 字节） |
| 前一增量 JSON | `77788E4808AAB6135C99BB12DFFF705561A582CEBE899408F561FD8E3FE9D4D6`（2429 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_INCREMENT_REV30.json` |
| 本增量 JSON SHA-256 | `D4A4EDB15627CC73082D2FC6FFD1077CDE64FFEC632CD5882DC9F78420A0B3C1` |
| 本增量 JSON 字节 | 2413 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增事实

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `validation/route_b_c03/wp_008/DSP_004_PHASE1_SETUP_REV1_RESULT.json` | 2944 | `718D7F4F2BB2477AE64F6776B8C0081FCEB355041AD9AEEB5F7D93A2D970540E` |
| `validation/route_b_c03/wp_008/dsp004_phase1_setup_rev1/phase1_setup.cmd` | 1345 | `F965D70FE7147CFEFA7C045441DEE7B5433C409CBE7AD6446A6438F1FDA882D6` |
| `validation/route_b_c03/wp_008/dsp004_phase1_setup_rev1/phase1_setup_check.RAW_REDACTED.txt` | 1325 | `47AA70D25BABFBFEBF076398E9C9C205EEAF4C9FCEC803C82E2B674DCB6CE427` |

核对输出按原样字节提交，编码为 GBK。其中只把管理员组成员列表里所有者的账户名替换成了 `<OWNER_ACCOUNT>`。替换前的散列记在结果 JSON 里。

## 2. 观察结果

| 编号 | 项目 | 观察 |
| --- | --- | --- |
| P1S-01 | 脚本以管理员身份运行 | 高强制级别 `S-1-16-12288` |
| P1S-02 | 进程创建审计 | 成功事件已开启 |
| P1S-03 | 进程终止审计 | 成功事件已开启 |
| P1S-04 | 审计事件记录命令行 | `0x1` |
| P1S-05 | `dsp004val` 账户 | 已启用，需要密码 |
| P1S-06 | `dsp004val` 所属组 | 只有 `Users` |
| P1S-07 | 管理员组成员 | 不含 `dsp004val` |

## 3. 备注

- 以上观察来自所有者运行的脚本的自报，不是运行证据。
- 按本机策略，`dsp004val` 的密码约在 2026-12-13 到期。在那之后运行，需要先改密码。
- 安全日志的保留容量没有改动，正式运行前再核对。
- 审查者与记录人属于同一模型家族，没有外部审查。

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
