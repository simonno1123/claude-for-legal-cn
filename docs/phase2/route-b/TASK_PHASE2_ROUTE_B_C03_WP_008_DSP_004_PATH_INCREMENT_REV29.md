# DSP-004 路径增量 REV29

本增量记录一项事实：所有者把阶段 1 的审查者从 Codex 改为记录人自审。到目前为止什么都没有执行。`Signed` 与 `Accepted` 都是 false。准入是 `NOT_ADMITTED`。DSP-004 保持 `OPEN / HOLD`。

所有者原话：`你先自审，后续有必要再说。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_INCREMENT_REV28.md` |
| 前一增量说明 | `46FD084444FA4486C604FEA19F394D189D26BF57E66AAF574FFB4C15A39A59FB`（1864 字节） |
| 前一增量 JSON | `585E181C48228754D3E45165D3AB94E8B5F1F638D7C55D777B6D8254B68274F3`（3072 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_INCREMENT_REV29.json` |
| 本增量 JSON SHA-256 | `77788E4808AAB6135C99BB12DFFF705561A582CEBE899408F561FD8E3FE9D4D6` |
| 本增量 JSON 字节 | 2429 |
| 记录人 | Claude（`RECORDER_ONLY`，不是所有者） |

## 1. 新增事实

| 事实 | 文件 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| `PHASE1_REVIEWER_CHANGED_TO_RECORDER_SELF_REVIEW` | `validation/route_b_c03/wp_008/DSP_004_PHASE1_OWNER_DECISIONS_REV2.json` | 1854 | `5CBC930D81245A499A97C5B959034E247C53F467105D29992B51AD62B906C5F9` |

决定 REV2 只修改 P1-REVIEWER。P1-HOST（本机加独立普通账户）和 P1-AUDIT（允许进程创建审计）保持 REV1 不变。

## 2. 自审的条件与局限

- 每次审查都由一个全新的子代理做。它没有看过编写过程，只拿到最终材料和固定的核对清单，并被要求专门找问题。
- 能用机器核对的项目（散列、字节数、签名、审计事件是否齐全）一律由脚本核对。
- Windows 安全日志的 4688/4689 事件作为系统写下的旁证。
- 每份审查记录都写明：审查者与记录人属于同一模型家族，没有外部审查。

局限：同一模型家族的审查者可能和编写者有同样的盲点。脚本核对和系统审计日志能减轻这个问题，但不能消除。所有者认为有必要时，可以随时补一次外部审查。

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
