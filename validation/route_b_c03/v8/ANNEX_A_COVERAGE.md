# R3 附录 A 反例：V8-A 测试覆盖表

测试文件为 `test_gate_records.py`，全部使用虚构数据。"代码覆盖"表示有对应测试，并会得到预期的阻断理由码。"不由代码覆盖"表示该反例依赖人工判断或外侧事实，无法用记录表示（见设计 §六）。

| 反例 | 覆盖 | 测试或原因 |
| --- | --- | --- |
| A-01、A-02、A-29 | 代码 | `test_A01_A02_A29_prohibited_purpose` |
| A-03 | 代码 | `test_A03_tier_invalid` |
| A-04、A-05、A-33 | 代码 | `test_A04_A05_A33_stop_needs_typed_V` |
| A-06 | 代码 | `test_A06_checklist` |
| A-07 | 不由代码覆盖 | 组合识别风险只能由复核人判断 |
| A-08 | 代码 | `test_A08_conditions_not_accepted` |
| A-09 | 代码 | `test_A09_c11_original` |
| A-10 | 不由代码覆盖 | 倒填时间属于外侧事实（V8-B） |
| A-11、A-16 | 代码 | `test_A11_A16_binding` |
| A-12 | 代码 | `test_A12_cooling` |
| A-13 | 代码 | `test_A13_exclusive_cutoff` |
| A-14 | 部分 | 禁止目的走 `PURPOSE_PROHIBITED`；内容实质上是否属于策略，由复核人判断 |
| A-15、A-30、A-31 | 不适用 | 现行用途表不收集委托人凭证 |
| A-17 | 代码 | `test_A17_x_other_send` |
| A-18 | 部分 | 撤回状态以记录为准（`WITHDRAWN_OR_SUPERSEDED`）；遗漏的撤回属于外侧事实 |
| A-19、A-48 | 代码 | 正面结果仅为"可申请"；授权须绑定记录链（`test_A60_...`） |
| A-20 | 代码 | X 不在 R 之前即 `EVENT_ORDER_INVALID`（`_check_p`） |
| A-21 | 代码 | `test_A21_design_version` |
| A-22、A-23、A-39 | 代码 | `test_A22_A23_expired_at_check` |
| A-24、A-40 | 代码 | `test_A24_reconfirmation` |
| A-25 | 代码 | `test_A25_unknown_deadline_and_trial_shape` |
| A-26 | 代码 | `test_A26_bad_time` |
| A-27、A-28 | 代码 | `test_A27_A28_bytes_receiver` |
| A-32 | 部分 | 按申报值比较（`test_A32_same_family`）；可验证的来源属于 V8-B |
| A-34 | 不适用 | 数字签名属于 V8-B |
| A-35、A-46、A-63、A-77 | 部分 | 同一 M 只能有一份 X（`test_single_S_multiple_X`）；跨次重送属于 V8-B |
| A-36、A-53、A-57 | 代码 | `test_A57_other_candidates_correction_does_not_cover` |
| A-37、A-38 | 代码 | `test_A37_post_review_field_in_M` |
| A-41、A-42、A-43 | 部分 | 只检查 S 中的核对结果，当场是否真的核对由复核人负责 |
| A-44、A-45 | 代码 | `test_A44_A45_coverage` |
| A-47 | 代码 | 盲区须有 `ORIGINAL_VERIFICATION_OF_BLIND_SCOPE` 类型的 V |
| A-49、A-50 | 代码 | `test_A49_A50_declaration` |
| A-51、A-52 | 部分 | Q 对照表的各行须为"满足"；对照内容是否属实由复核人负责 |
| A-54 | 代码 | `test_A56_unanswered_relevance` |
| A-55 | 代码（正例） | `test_A55_same_round_refutation_clears` |
| A-56 | 代码 | `test_A56_unanswered_relevance` |
| A-58 | 不由代码覆盖 | H 只追加不覆写，由文件管理保证 |
| A-59、A-68、A-70、A-71 | 部分 | S 第 6 项核对须为"通过"；R 前再查一次由 `h_query` 承载 |
| A-60、A-61、A-62、A-69、A-75 | 代码 | `test_A60_A61_A62_A69_A75_use_stage` |
| A-64、A-65、A-66 | 部分 | 解除事件须早于 R；W 的内容由复核人负责 |
| A-67、A-72、A-73、A-74 | 代码 | `test_A72_A73_A74_post_r_rules`、`test_A67_increment_marked_unrelated` |
| A-76 | 不由代码覆盖 | 是否发送过属于外侧事实 |
