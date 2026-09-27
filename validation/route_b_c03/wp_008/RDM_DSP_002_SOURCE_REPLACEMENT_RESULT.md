# RDM-DSP-002 源码替换与回归结果

## 1. 本轮范围与实际完成项

授权来源：Project Owner 对“仅用已接受候选替换本项目的 identity_gate.py，保留旧版并重新测试；不启用真实业务、不修改 ACOS、不提交或推送 Git”的确认回复“授权”。本记录记载该授权下的执行事实，不另行推定签署时间、接受决定或下游权限。

本轮已完成：

- 先保留旧源码，替换前核对其 SHA 与原始源码完全相同。
- 将现有三项授权引用比较移动到 ELIGIBLE_FOR_MAPPING 返回之前；未修改其他源代码行。
- 核对当前 identity_gate.py 与已接受候选字节完全一致。
- 使用本地 Python 对替换后的实际源码重新执行合成数据诊断，同时对照保留的旧版。
- 保存逐项输出及本说明；未改写已有候选、接受决定、历史诊断脚本或历史结果。

## 2. 文件与固定身份

下表路径均相对于 claude-for-legal-cn 项目根目录。

| 角色 | 文件 | SHA-256 |
| --- | --- | --- |
| 替换后的当前源码 | scripts/phase2_runtime/route_b_c03/identity_gate.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| 未修改的已接受候选 | validation/route_b_c03/wp_008/IDENTITY_GATE_RDM_DSP_002_REVISION_CANDIDATE.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| 旧源码的逐字节保留副本 | validation/route_b_c03/wp_008/IDENTITY_GATE_RDM_DSP_002_PRE_REPLACEMENT.py | EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A |
| 未修改的数据契约 | scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| 复用的固定诊断用例脚本 | validation/route_b_c03/wp_008/test_identity_gate_rdm_dsp_002.py | 3ECC8614BAC8AC7960807571BA323CF24BA73D4916D83B4A59459EAED93F1833 |
| 本轮回归入口 | validation/route_b_c03/wp_008/test_identity_gate_rdm_dsp_002_installed.py | 9369DF33AE81337C59118B595FA0B07B15D742B5AEB7D5A5ECCCE365776EBBC6 |
| 本轮实际输出 | validation/route_b_c03/wp_008/RDM_DSP_002_INSTALLED_REGRESSION_OUTPUT.json | 9314604081A24F8FEECC119F99277D0B43E3A7072F043A6705D96B964A9E84DD |

旧版可用于恢复，但本轮未执行回滚。保留副本不替代已修复源码，不进入正常业务导入路径。

## 3. 回归方法

在项目根目录执行：

```powershell
& '.\.venv-validation\Scripts\python.exe' -I -S -B 'validation/route_b_c03/wp_008/test_identity_gate_rdm_dsp_002_installed.py'
```

实际解释器为 Python 3.12.14，退出码为 0。隔离模式启用、site 初始化禁用、字节码缓存写入禁用。

回归入口校验历史诊断脚本的固定 SHA 后加载它，仅在内存中把“原版”路径指向旧版保留副本，把“候选”路径指向替换后的实际 identity_gate.py。所有合成输入、预期状态、原因字符串及断言逻辑均复用，未修改其预期结果。输出字段明确重命名为 preserved_original 与 active_source，以区分旧版对照和当前源码。

测试前后均核对当前源码、保留旧版、已接受候选和数据契约的固定 SHA。当前源码与候选另做字节比较。真实事项、真实授权、真实有效期、业务调用和输入材料均未接入；所有测试值只表示合成元数据。

历史 test_identity_gate_rdm_dsp_002.py 原本把原始 SHA 绑定到当前源码路径，该脚本及旧结果保持不变。替换后不得直接将其旧调用方式作为现版本验证入口；新入口通过明确绑定保留副本完成可重复对照，不绕过 SHA 校验。

## 4. 实际结果

| 检查组 | 数量 | 替换后的实际源码 | 保留旧版对照 |
| --- | --- | --- | --- |
| 三项授权引用全部一致 | 1 | 1/1 符合预期 | 1/1 符合预期 |
| 三项授权引用至少一项不一致 | 7 | 7/7 正确 BLOCKED | 7/7 错误返回 ELIGIBLE_FOR_MAPPING |
| 原有前置保护条件及其优先级 | 30 | 30/30 符合预期 | 30/30 符合预期 |
| 门禁检查合计 | 38 | 38/38 通过 | 31/38 符合预期；7 项复现已知缺陷 |
| 共享契约空授权引用检查 | 3 | 3/3 正确抛出 ValueError | 共享契约检查 |

每项门禁检查同时核对状态、原因、审计关联标识和空写入命名空间。前置保护检查在最终授权引用不一致的条件下进行，确认拒绝优先级未变。诊断钩子拒绝事件为 0；此结果不是完整操作系统隔离或所有副作用均不存在的证明。

原版 7 项失败是一个检查不可达缺陷的不同输入组合复现，不是 7 个独立缺陷。退出码 0 表示“新源码通过且旧版缺陷按预期复现”，不表示旧版通过。

当前源码的本次有限修复已落地且通过上述局部回归。ELIGIBLE_FOR_MAPPING 仍不等于真实事项调用授权；本轮没有启用或运行映射业务。

## 5. 保留的限制与下一步

- 源码替换和局部合成回归已完成；这不是正式 WP-008 验证、C03 能力启用或 RDM-DSP-002 关闭决定。
- 原有 Scenario Input Binding 与 Comparison Contract 未修改或重新接纳；引用旧源码 SHA 的证据不能自动转用于新源码。
- 完整正式验证仍需处理输入与比较规则绑定、证据准入及运行依赖绑定。本次只为后续工作提供局部行为证据。
- 环境版本差异仍存在：pyvenv.cfg 记录 3.12.13，实际解释器报告 3.12.14。本轮未修改共享基础解释器、虚拟环境配置或历史环境清单。
- 未执行 Route A、OCR、真实案件处理、外部模型、网络服务、业务运行时或部署；未修改独立 ACOS 项目。
- 未进行 Git 暂存、提交、分支、合并或推送。已有接受/审查记录的形成时状态保持原文，不进行追溯改写。

本轮文件变更仅包括一个源码文件及四个本地支撑文件：旧版保留副本、回归入口、逐项输出 JSON 和本记录。
