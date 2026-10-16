# Route B C03 / WP-008 — 双层一致性候选预声明错误注入计划 REV1

## 1. 范围与目的

承接本项目已授权的批量本地合成工作。本轮只检查上一轮双层 detached 一致性候选的测试敏感性：原版应完成既定测试；八个分别派生的单点内存错误版本应在预先指定的断言位置被发现。不得修改任何已有候选、验证器或已接受文件，不作来源准入、真实捕获、集成、部署或接受决定。

起始 main 提交：`f149e30eedb4cdbcc26ba068eaf2ead54ba8deb0`。DSP-004 保持 OPEN / HOLD；B-01、B-02 保持 OPEN；所有 LIMITED、历史失败及原记录继续保留。独立 ACOS 和其他项目不在范围内。

本轮定点重新核验九个既有文件：四个运行输入、上一轮另外四个文件，以及复用结构的旧错误注入控制端。此九项清单与上一轮七十项保护检查不等同；不得声称本轮又完整复核七十项。Git 范围检查用于确保本轮仅新增限定文件。

## 2. 固定运行输入

| 角色 | 相对项目路径 | SHA-256 | 字节 |
| --- | --- | --- | --- |
| scalar | `validation/route_b_c03/wp_008/RDM_CANON2_SCALAR_ENTRY_ENCODING_CANDIDATE_REV1.py` | `532A77331FCF746759323D2E96EDF36C706A49ABC71875E984E1405FEF1708D4` | 8234 |
| tree | `validation/route_b_c03/wp_008/RDM_CANON2_STRUCTURAL_LAYOUT_CANDIDATE_REV1.py` | `F7DD5F91B7E8AD3B75281042207969FD3919FE46D90F4FC80C4E16A349403A87` | 9953 |
| binding | `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_CANDIDATE_REV1.py` | `32535D3E4800E39E8AAF510166AD2AF04E0436D39E7C0BAD528B329D24E66821` | 5799 |
| validation | `validation/route_b_c03/wp_008/RDM_CANON2_DETACHED_PROJECTION_BINDING_VALIDATION_REV1.py` | `944A36B0B608B40EACE207CFC0BC4F54EC0CC4C37D81B55CE076EFE97A49D476` | 13142 |

九个保护项完整路径、字节及 SHA 由结果归档记录。固定 Python 为 `C:/Users/Administrator/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe`，SHA-256 为 `B847BB9F4E48C19F585C8BF7D8B355F3F8C6D2125717ECE9C9D7E16FB9F09DE8`。控制端从旧脚本结构派生新文件，不改写旧脚本，也不通过旧脚本自动发现或执行其他项目文件。

## 3. 预声明的九个进程与八个错误

BASE-BINDING 使用四个原始固定快照，预计 106 个检查与 3 个字节向量全部完成。其完整 ValidatorResult 必须与上一轮归档解压后的 Result 严格一致；比较只针对结果数据，不要求耗时或 wrapper 元数据相同。

每个 MU-B 版本只从同一原始 binding 快照替换一次指定片段；互不串联，两个依赖与验证器均不变。替换片段的 Before / After 原文、唯一匹配数和预声明身份同时固定在控制端内，不将变异源码写成物理候选。

| ID | 唯一变化主题 | 预期 AssertionError ID | 内存源码 SHA-256 | 字节 |
| --- | --- | --- | --- | --- |
| MU-B01 | 全文散列保护移除 | `L-LABEL-STALE-FULL-SHA` | `11EBD7A12AF07BEAA4EDD8245EE13100629BEACA8302B41E06C67B7CB8EFB973` | 5764 |
| MU-B02 | 正文聚合散列保护移除 | `B-AGGREGATE-MISMATCH` | `03CD28E0F619ED747DEFBCCF2264461B1D668E10E5D2AEA38809CFD0E115358B` | 5770 |
| MU-B03 | 正文条目数保护移除 | `B-COUNT-MISMATCH` | `EC5113EE8477E692805F5BCB0E59750D322A4FD7D4719655E4165B72FEE86886` | 5770 |
| MU-B04 | 正文总字节数保护移除 | `B-TOTAL-MISMATCH` | `73D3A0FAD551855816817F11A42D5B0014172CB19E645F9AE2D473A58438CD59` | 5771 |
| MU-B05 | detached 聚合散列保护移除 | `D-MISMATCH-AGGREGATE_SHA256` | `9F1E2087EA471904969BF58ADF34C4F129ACC038D5D8F971F3326C9F2A941183` | 5765 |
| MU-B06 | detached 条目数保护移除 | `D-MISMATCH-ENTRY_COUNT` | `E38808C8846B503EC9E7EA2D9C806DDF6DB7DEEEAF8765AF4612A141C4874D0A` | 5775 |
| MU-B07 | detached 总字节数保护移除 | `D-MISMATCH-BYTE_TOTAL` | `D2547E6CBA6574643CAB94FFE8662AF45AF975A297D9D94173617BD1B00E589D` | 5776 |
| MU-B08 | 非权威限定语不完整 | `P-ONE.QUALIFIER` | `5B3351956372A90A10A86A4EEC8D47C37595DE8289C6105CAF954F45B9C6BA88` | 5776 |

## 4. 判定标准

错误版本必须先通过快照散列/长度核对、严格 UTF-8、AST 解析及编译，并完成固定模块装载；仅当异常为 RUN_CLOSED_VALIDATOR 阶段的原生 AssertionError，且唯一字符串参数与本表指定 ID 完全相同时，才计入“该预设错误被发现”。语法失败、装载失败、散列不符、超时、任意其他异常或不同断言都不能冒充发现。

每个进程使用全新 -I -S -B Python，stdin 只接收封闭 CaseId 与对应四个快照。两个固定模块槽位由当前进程创建并在退出前核对所有权、移除；不得加载项目普通模块路径。

wrapper 对预期 AssertionError 可退出 0；这仅表示“预期错误已观察”，**不是变异候选通过**。错误版本的 SubjectValidationPassed 必须为 false、ValidatorResult 必须为 null；不得声称八次负例完成全部 106 个检查。若任一预期不满足，批次停止并保留真实结果，不自动重试或改写为成功。

本轮不计算一般 mutation score，不将 8 / 8 解释为任意错误覆盖率，也不将上一轮检查数与本轮负例数相加作为业务进度。

## 5. 过程与证据保留

父进程在内存派生八份字节，保存每份完整 gzip / SHA / 长度、Before / After 和原始候选 SHA；每个新 Python 子进程保存原始 stdout 与 stderr 的 gzip / SHA / 长度、退出码、耗时、实际 FailurePhase / FailureType / FailureAssertion 及固定输入身份。

局部输入/运行/流等待为 5000 / 30000 / 5000 ms，停止等待 5000 ms，批次逻辑上限 60000 ms。输出上限在收集后检查；这些不是在线内存限额、OS 沙箱、所有子孙进程清理或物理硬停止保证。

归档复核需重建八份内存变异字节并与原始快照比对，核对九份原始进程记录与归档 parsed Record 一致、固定 Case 顺序及源身份一致、九次两个模块槽位均移除。原版的 106 项结果需逐项唯一；八个负例只核实指定异常，不虚构未执行检查。

## 6. 交付与后续边界

仅新增：本计划、新私有错误注入控制端、观察 JSON、结果报告四个文件。先固定计划与控制端身份，再执行本地合成批次，后用 apply_patch 归档实际返回内容。

候选接受未授权；完整 Manifest / 正式 typed contract / 政策注册表不物化；不准入任何来源，不执行实际业务捕获，不调用 Gemini 或其他外部审查模型，不生成正式隐私/安全/法律总体结论。阶段普通提交/推送只作本项目备份，不构成接受或状态升级。
