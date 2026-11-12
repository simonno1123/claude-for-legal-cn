# V8-A 记录字段合同（实现细则）

本文件是设计 `C03-GATE-ENFORCEMENT-V8` R2 §四 的实现细则，以 `scripts/phase2_runtime/route_b_c03/gate_records.py` 中的 `SPECS`、`H_SPECS`、`G_SPECS` 为准。

## 通用规则

- 任何记录或事件的形成时间（`formed_at`、`at`、`received_at`、`sent_at`）都不得晚于本次校验时传入的当前时间。
- X 中每一个可见部分不是"通过"的项，都必须在 H 中登记为模型停点，即发现事件的 `X` 指向本轮 X，并有对应的解除事件。
- 时间顺序必须满足 Q2 < AUTH < Q3。

- 每份记录都有共同字段 `record`、`schema`（固定为 `C03-V8-R1`）、`formed_at`、`method`、`refs`。
- `formed_at` 必须是带时区偏移的时间。
- `method` 只能取 `file_a`、`file_b`、`chat_c` 之一。
- `refs` 的每个值都必须是 SHA-256（64 位大写十六进制）。
- 共同字段之外只能有该类记录规定的字段，不能多也不能少。每个字段都按类型和内容逐一检查：非空文本、SHA-256、带时区偏移的时间、合法日期。

## 各类记录

| 记录 | 字段要点 |
| --- | --- |
| M | `candidate`：九个子字段，含 `capability`、`operation`、`generator_model_family`，`output_sha256` 为 SHA；`case`：`code` 和 `version`；`trace_refs`：代号 → `{path, sha256}`，至少一条；三类引用列表，每项为 SHA；`authority`：`pack_sha256`、`check_date`（YYYY-MM-DD）、`entries`；`known_limitations`、`prohibited_uses`、`planned_scope` 均为非空文本；`design_version`；`reviewer`：`code` 和 `qualification_ref` |
| I | `reviewer_name`；`items`：第 1、2、3、5、6 项为"确认"，第 4 项取"提供并确认""仅确认""未参与"三者之一；`refs`：`{M}` |
| T | `use_code`、`output_class`、`audience`、`next_step`、`l1_positive_confirmation`；`h_query`：L2 必填，L1 为 null；`corrections`：`[{discovery, description, diff_ref}]`；`refs`：`{M, I}` |
| 停点查询答复（`h_query`、`h_check`、`h_increment`） | `{answers, last_event}`。`answers` 以发现事件的 SHA 为键，值为 `{relevant, reason, covered, clearance}`。取值约束：`relevant` 为"不相关"时，`covered` 为"不适用"，`clearance` 为 null；`relevant` 为"相关"时，或者 `covered` 为"已覆盖"且 `clearance` 为一条解除事件的 SHA，或者 `covered` 为"未覆盖"且 `clearance` 为 null。所有答复均由复核人作出 |
| E | `d_sha256`、`task_sha256`、`scope`、`allowed_fields`（非空）、`receiver`；`conditions`：四项处理条件均为"接受"；`config_sha256`、`window{start,end}`、`withdrawn`；`refs`：`{M, T}` |
| S | `sent_sha256`、`scope`、`receiver`、`config_sha256`；`checks`：第 1 至 6 项均为"通过"；`h_check`：T 之后、发送之前出现的每个发现事件都要有答复；`request_id`、`sent_at`；`refs`：`{E}` |
| X | `opinions`：C1 至 C11 每项为 `{visible, blind}`。`visible` 取"通过""不通过""无法判断-可见范围内"之一；`blind` 为 null，或为 `{sub, value: "无法判断-脱敏盲区"}`，其中 `sub` 只能是 R3 §6.2 为该项列出的子判断；C6、C7、C8 不得有 `blind`。另有 `provider`、`model`、`model_family`、`received_at`、`request_id`；`refs`：`{S}` |
| V | `item`、`issue`；`clearance_type` 为两种解除类型之一；`evidence`：`[{code, sha256, locator}]`，非空，每个 SHA 必须出现在 M 的 `trace_refs` 中；`refs`：`{M, T, X}` |
| W | `result` 为"通过"或"不通过"；`location`：原件定位列表；`refs`：`{M, T, discovery}` |
| R | `h_query`、`actual_scope`、`checklist`、`c11_original_verified`；`deadlines`：`[{item, status, expiry}]`；`no_deadline_declaration`、`validity_cutoff`；`material_conflict` 为"有"或"无"；`withdrawn`；`disposition` 为 4 种原文之一；`reason`。`refs` 必须完整列出 R 所依据的全部前件：`{M, I, T}`；L2 另加 `X`；全部 V 按 SHA 排序后依次记为 `V1…Vn`，全部 W 依次记为 `W1…Wn`；`h_query` 中引用的解除事件依次记为 `CL1…CLn` |
| CORR | `items`：C 项 → "通过"或"不通过"；`statement`；`refs`：`{R}` |
| P | `reconfirm`：第 1 至 4 项均为"已重查"（第 5 项 H 增量核对由 `h_increment` 承载）；`authority_recheck_at`；`h_increment`；`refs`：`{R}` |
| Q（Q1、Q2、Q3） | `stage`；`rows`：七个固定键 `deadlines`（与 R 完全相同）、`new_deadlines`、`expired_deadlines`、`cutoff`、`authority`、`qualification`、`withdrawal`；`h_increment`；`auth_checks`：只有 Q3 使用，五个固定键。各份的 `refs`：Q1 为 `{R, [P], application_body}`，Q2 为 `{Q1, application_body}`，Q3 为 `{AUTH, Q2}` |
| AUTH | `action` 必须等于 T 的 `next_step`；`scope` 为 `{candidate, version, M}`；`own_deadline`；`max_uses`；`refs`：`{Q2, application_body}` |
| G 事件 | 初始事件：`{kind: "initial", auth, max_uses, used: 0, at}`；使用事件：`{kind: "use", auth, q3, at}` |
| H 事件 | 发现事件：`{event, type, case, item, issue, candidate, M, X（SHA 或"不适用"）, stage, at}`；解除事件：`{event, type, refs_discovery, scope_candidate, evidence, at}`。`evidence` 为原件定位 `{code, sha256, locator}`，或记录引用 `{record: "W"/"X", sha256}` |
