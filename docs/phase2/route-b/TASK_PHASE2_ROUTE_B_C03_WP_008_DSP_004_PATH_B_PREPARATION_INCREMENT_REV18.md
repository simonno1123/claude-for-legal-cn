# DSP-004 路径 B 筹备增量 REV18

本增量只记录路径 B 下的下一项筹备事实：OD-04 的仓库现有证据盘点已经写下。盘点只汇总 GitHub 仓库已经记下的记录，并逐项列出缺口。它不是新证据，不满足 OD-04，也不改 OD-04。OD-04 仍是 `DEFER_WITHOUT_EVIDENCE`，状态是 `OWNER_HELD_OPEN_NO_CLOSED_OPTIONS`。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本次授权是：2026-10-31，Project Owner 张纯熙选择"改变某项决定"中的 OD-04 补充证据。所有者无法提供 Windows 验证机，因此指示：只盘点 GitHub 仓库已有的 OD-04 相关记录，列出缺口，不准入，不改 OD-04，不关闭 DSP-004。

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV17.md` |
| 前一增量说明 | `CF474672F16301D1C246ACDA058D2689E536D10BC5954251E7498C0A616404E4`（8129 字节） |
| 前一增量 JSON | `EA33B5D5962EA929560C391D6AFCB3299FAD5A3E9C017D48E9E0C1882678E3E5`（11789 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV18.json` |
| 本增量 JSON SHA-256 | `54608E042A7AC33FD9E9A4C8D0F088673245270007ADB0403FBC451FD03FCDCE` |
| 本增量 JSON 字节 | 8529 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

前一增量 JSON 的重新散列与 REV17 说明里写下的 SHA 相同。相符不是接受。DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV17 已经记下的筹备事实保持原样。本增量不改它们。

## 1. 新增筹备事实

新增筹备事实的名称是 `OD04_REPOSITORY_EVIDENCE_INVENTORY_REV1_RECORDED_NOT_ADMITTED`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_OD04_EVIDENCE_INVENTORY_REV1_CANDIDATE.md` | 8273 | `C88AB81A9511836FA22B43BA8F536B652436F6B34366104F47248AA9916FCA1E` |
| `validation/route_b_c03/wp_008/DSP_004_OD04_EVIDENCE_INVENTORY_REV1_CANDIDATE.json` | 17820 | `81873771A15954217A8C89AE9B359FD4D0FDB2AA50D4D79EC825ADC1A2724761` |

盘点机器记录有 7 项字段核对，全部相符。相符只是字段一致，不是接受。

## 2. 盘点结果摘要

| 组成部分 | 仓库现状 |
| --- | --- |
| 导入闭包 | 部分，仅文本：受测文件与批次 Harness 的直接导入名；无标准库递归闭包 |
| 两侧调用身份 | 无 |
| 检查到使用的防替换 | 无；记录显示运行根文件的字节在观测之间变化过 |
| T0 | 无；只有定义，没有观察 |
| PE | 部分，仅身份：五个运行时文件的 SHA；无 PE 导入表，无 PYD |
| OS | 无 |

最需要所有者留意的两点：

1. `python.exe`、`python3.dll`、`python312.dll` 各有三个不同的已记录身份。运行根至少变化过两次。`pyvenv.cfg` 写的是 3.12.13，attempt_02 报告的是 3.12.14。
2. 运行根位于由工具管理的运行时缓存之下（重绑定候选第 3.1 节）。在这种布局下，仅凭仓库记录无法建立检查到使用的防替换。今后若要补 OD-04，需要先在验证机上取得一个不会被工具自动替换的、固定的运行根。这一点只是筹备观察，本增量不据此提供定位，OD-05 `REFUSE_LOCATOR` 不变。

## 3. 如实记载的形成情况

记录人在摸查阶段对 `ENVIRONMENT_MANIFEST.md` 做过一次文本检索。此前各增量都写明未读取该文件。本增量不使用、不引用、不绑定该文件内容，盘点里的环境身份全部取自准备计划、重绑定候选和 attempt_02 结果。机器记录里 `EnvironmentManifestRead` 因此写为 true，并附说明。

形成主机是云端 Linux 容器，不是验证机。未访问验证机，未读取工具缓存或历史 Windows 虚拟环境，未导入或执行任何仓库模块。

## 4. 本增量故意不做的事

- 不改 OD-04 或任何其他 OD 记录，不改 REV1 登记或 REV2 至 REV4 叠层。
- 不把盘点当作新证据，不把任何已记录 SHA 接受为运行根、来源或 Manifest 条目。
- 不提供运行根定位，不发明路径、启动序列或导入查询顺序。
- 不生成 Manifest，不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不改商业 P0。

## 5. 仍留着的状态

REV17 第 2 节与第 4 节列出的状态全部不变。唯一的补充是 OD-04 一行：它仍没有新证据，但现在仓库里已有一份盘点，写明哪些部分只能从验证机取得。

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。没有真实案件、个人信息、凭据或供应商调用。
