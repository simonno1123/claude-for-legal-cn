# RDM-DSP-002 Python 合成数据功能诊断

## 范围与结论

依据 Project Owner 本轮“运行python。”指令，实际运行本地 Python，对当前身份门禁源码和已接受候选进行并排功能诊断。本记录不是正式 WP-008 验证报告、RDM 关闭决定、候选源码替换决定或能力启用决定。

诊断脚本退出码为 0。候选通过 38/38 项门禁检查；共享数据契约通过 3/3 项空值拒绝检查。原始源码在 7 种授权引用不一致组合下均错误返回 ELIGIBLE_FOR_MAPPING，成功复现本次修订针对的缺陷。候选在相同组合下均返回 BLOCKED。

ELIGIBLE_FOR_MAPPING 仅为函数返回状态，不代表本轮建立了真实案件调用授权或执行了映射业务。

## 实际运行方式

在项目根目录中执行：

```powershell
& '.\.venv-validation\Scripts\python.exe' -I -S -B 'validation/route_b_c03/wp_008/test_identity_gate_rdm_dsp_002.py'
```

- 实际解释器输出版本：Python 3.12.14，64 位 AMD64。
- 启用隔离模式、禁用 site 初始化、不写入字节码缓存。
- 先计算并匹配三份源文件 SHA，再编译并加载其实际字节；未执行项目包初始化文件。
- 原版和候选在独立模块名下加载；二者共享同一份已绑定的数据契约。
- 使用内存中的合成元数据；授权标签、有效期标签和输入 SHA 字段均为测试值，不代表实际授权、时间验证或真实材料。
- Python 进程仅向标准输出打印 JSON。审计钩子对网络、子进程与文件写入等指定事件进行防护，本次拒绝事件计数为 0；此钩子不构成完整操作系统隔离证明。
- 输出 JSON 由协调员保存；仅规范化换行为 LF 并保留末尾换行，未改变任何 JSON 字段值。
- 未替换原始源码，未修改候选或 contracts.py；执行结束后重新核对三份源文件，SHA 均不变。
- 未执行 Git 提交或推送，未访问或修改独立 ACOS 项目。

## 测试覆盖与结果

| 检查组 | 场景数 | 原始源码 | 候选 |
| --- | --- | --- | --- |
| 三项授权引用全部一致 | 1 | 1/1 符合预期 | 1/1 符合预期 |
| 三项授权引用至少一项不一致 | 7 | 0/7 符合预期；均错误放行 | 7/7 正确阻断 |
| 前置保护条件及其优先级 | 30 | 30/30 符合预期 | 30/30 符合预期 |
| 门禁检查合计 | 38 | 31/38 符合预期 | 38/38 符合预期 |
| 共享数据契约空引用构造检查 | 3 | 共享契约检查 | 3/3 正确抛出 ValueError |

每项门禁检查同时比较返回状态、原因、审计关联标识与空写入命名空间。前置保护检查在最终授权引用不一致的条件下运行，以验证已有拒绝路径仍具有原来的优先级。

30 项前置条件覆盖：kill、缺失配置、3 种非活动配置状态、5 项能力身份字段、5 项域身份字段、缺失授权包、4 种非接受包状态、2 种非 CLEAR 撤销状态、有效性未确认、3 项事项/主体隔离字段、2 项目的/操作字段、输入集合 SHA 与输出边界。

三位编码顺序：事项授权引用、执行授权引用、授权包决策引用。0 表示匹配，1 表示不匹配。

| 场景 | 预期 | 原始源码实际返回 | 候选实际返回 |
| --- | --- | --- | --- |
| authority-000 | ELIGIBLE_FOR_MAPPING | ELIGIBLE_FOR_MAPPING | ELIGIBLE_FOR_MAPPING |
| authority-001 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-010 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-011 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-100 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-101 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-110 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |
| authority-111 | BLOCKED | ELIGIBLE_FOR_MAPPING | BLOCKED |

7 项原版失败是同一个检查不可达缺陷的不同组合复现，不代表 7 个独立缺陷。脚本以“原版缺陷如预期复现，且候选全部符合预期”为成功条件；退出码 0 不代表原始源码通过验证。

## 固定输入与诊断脚本

| 文件（项目内相对路径） | SHA-256 |
| --- | --- |
| scripts/phase2_runtime/route_b_c03/contracts.py | 7EA17AC467011A198DCEF268ED792CA0D448D2DD3C0E510E516AEF98FCF04DE4 |
| scripts/phase2_runtime/route_b_c03/identity_gate.py | EA762C13F1DED4ABEAE27D16DD1087901D73E0B6B0A680791E3082AEFFB4D90A |
| validation/route_b_c03/wp_008/IDENTITY_GATE_RDM_DSP_002_REVISION_CANDIDATE.py | 9E57E16C2AA1B7235EB5DE8C89A8F05319B7876AE1CF7715FBE6BE624647F445 |
| validation/route_b_c03/wp_008/test_identity_gate_rdm_dsp_002.py | 3ECC8614BAC8AC7960807571BA323CF24BA73D4916D83B4A59459EAED93F1833 |
| .venv-validation/Scripts/python.exe | 560B9EF7D856608AB8DA02DED2DC8A1951AD1F424C382C0EC6A698874165A18E |
| .venv-validation/pyvenv.cfg | 7AFB3C331994D8D1CB462B711254E30BAE372DC8A28F2C485AFA79B030775461 |

## 环境记录差异与限制

pyvenv.cfg 中记载 version = 3.12.13，而本次实际执行的 sys.version 为 3.12.14。上述 Python 启动器和配置文件 SHA 均已记录，但不能据此宣称完整基础解释器、标准库及依赖都已固定或正式验收。未修改环境配置或历史环境清单。

本诊断未验证真实授权来源、可信导入边界的全链路安全、真实时间有效性、完整输入接纳、业务映射、其他 RDM 项或完整 C03 一致性计划。未使用真实案件材料，未开展 OCR、外部模型调用或运行时部署。

本次仅增加诊断脚本、观察输出 JSON 和此诊断说明。候选未提升为当前实现；RDM-DSP-002 未由本报告自动关闭。正式验证所需的环境绑定和证据准入仍须单独完成。

逐项实际输出见同目录 RDM_DSP_002_PYTHON_SMOKE_TEST_OUTPUT.json。
