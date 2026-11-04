# DSP-004 外部审查委托书 REV1

**致审查者**：本委托书请一个不属于 Claude 模型家族的审查者阅读（例如其他公司的模型，或人工）。到目前为止，DSP-004 的所有审查都由 Claude 的全新子代理完成，属于同一模型家族。按路线图 REV1，关闭 DSP-004 之前至少需要一次外部审查（所有者决定 P8-EXTREVIEW）。

本次审查**只读**：请不要修改仓库，也不要运行任何会产生外部影响的程序。在本地重新计算散列、重新运行生成程序都可以。

仓库：`https://github.com/simonno1123/claude-for-legal-cn`（公开），基准提交见文末。

## 一、背景

DSP-004 是一项验证：在一台 Windows 电脑上，用固定的 CPython 3.12.10，以一个普通权限的专用账户 `dsp004val`，运行固定的 Harness REV4。Harness 依据已接受的输入 REV4，对 10 个固定的受测源码执行 28 个场景变体，并把结果与 15 个 Fixture 比对。

运行期间有三重保障：
- 监督程序先锁定 743 个文件，再核对散列与签名，并从进程外部检查子进程的身份和装载的本地模块。
- Windows 安全审计记录了进程的创建和退出。
- 收集程序按账户的整个历史导出审计事件，并检查记录编号是否连续。

运行依据的 Manifest REV1 列出了允许读取的全部 90 个文件，以及 96 个模块。

公开文件中，主机名、机器 SID 和所有者用户名已做脱敏替换：分别替换为 `REDACTED-HOST`、`S-1-5-21-REDACTED`、`REDACTED-OWNER`。脱敏前文件的 SHA 记在结果 JSON 里。

## 二、审查材料

| # | 文件 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- | --- |
| 1 | 路线图 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_COMPLETION_ROADMAP_REV1_CANDIDATE.md` | 5254 | `970472DC751CAB7844A23E6E06D8F142BFD7D9D0CD658C1E488EF8FC38622C82` |
| 2 | 类型合同 REV3（已接受） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md` | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` |
| 3 | 数组政策 REV3（已接受） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` |
| 4 | 输入 REV4（已接受） | `validation/route_b_c03/wp_008/DSP_004_INPUT_CANDIDATE_REV4.json` | 115428 | `685BBCBF13BF96746E6DE4201C1FCE72B667CD6A07D0CE0902D9EF9A6C4235C1` |
| 5 | Harness REV4（已接受） | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/harness_rev4.py` | 25803 | `0B2AC413272D048B75904689C3105B4758A31624356D69FD9CF4B81C622D2394` |
| 6 | 监督程序 | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/supervisor_formal_v2.ps1` | 26269 | `3463EC1E62193F84605ADD3FF8A8D695C6E92905F5BE1F68423765B5A023E1D3` |
| 7 | 收集程序 | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/collect_formal_v2.ps1` | 17175 | `8F130258F9D5BD9CC6C14FFE4F1BBE270632B66772145EE3B32296B7C1AF4840` |
| 8 | 约束清单 formal v2（已接受） | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2/bound_list_formal_v2.json` | 160152 | `19A1CE8D54AF938F86BF81DFA54AD2DC9719F12E498F0483AC8B0B08D486BF50` |
| 9 | Manifest REV1（已接受） | `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` | 451503 | `B73C19C7717AC8F889E122A2D9C375F28FB7B7ACAC2ABD55D5896BB8CC4870DD` |
| 10 | Manifest 配套政策 REV1（已接受） | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_MANIFEST_SUPPORT_POLICIES_REV1.md` | 11929 | `9F03F7199E5C50398F1E356F10A6FAD50A78A6AAA3710CF2107C4C5359ADB3BA` |
| 11 | Manifest 生成程序 | `validation/route_b_c03/wp_008/dsp004_phase6_manifest_v1/generate_manifest_rev1.py` | 28398 | `B0EB8D5F6131D9C5A1127676BEB44307AE2131C4B10A67ACD66660E82C804217` |
| 12 | 正式运行结果（已接受） | `validation/route_b_c03/wp_008/DSP_004_FORMAL_RUN_V2_RESULT.json` | 4307 | `86488C277577B259F6FE415FEF9525A43F32123808AFD127826ED01443226196` |
| 13 | 运行记录（已脱敏） | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2_run/formal_v2_run_record.RAW_REDACTED.json` | 392761 | `72F5F628F90E1CD0F8A2CD07BDE33A341E377E4C1E304FF677DCC49307AC330A` |
| 14 | 审计事件（已脱敏） | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2_run/formal_v2_events_history.RAW_REDACTED.xml` | 164804 | `A6F68DF4A0195538A7E7F6E33FE062D401B29CBC96F37D577E0DEB3E0987F60D` |
| 15 | 收集结果 | `validation/route_b_c03/wp_008/dsp004_phase7_formal_v2_run/formal_v2_post_collect_result.json` | 100070 | `4C640FB23B74DE1D22CB21A1EE9DE67E75795D0665BEE6C567AAF16FA362D518` |
| 16 | 所有者决定：阶段 1 | `validation/route_b_c03/wp_008/DSP_004_PHASE1_ADMISSION_DECISIONS_REV1.json` | 2712 | `0989FCEFD6A59FD6C2376BDE54882A142C111631C7A18086DEA311B81D154664` |
| 17 | 所有者决定：阶段 2–5 | `validation/route_b_c03/wp_008/DSP_004_PHASES_2_TO_5_OWNER_DECISIONS_REV1.json` | 3489 | `8FAB5BC81A4E5EEFE206C1E99D1C31D701F2892A788D5B56060B458745813FA9` |
| 18 | 所有者决定：阶段 6–7 | `validation/route_b_c03/wp_008/DSP_004_PHASE6_7_OWNER_DECISIONS_REV1.json` | 1277 | `D004C16A0644556449A3FBE662D62A896362D78933AD4444B0B80EE047FFA0B6` |
| 19 | 所有者决定：Manifest 接受 | `validation/route_b_c03/wp_008/DSP_004_PHASE6_ACCEPTANCE_REV1.json` | 2661 | `31F03A7EB585E97F8F19EF87808D8B5933E1401220D5509DB6ED6186849712E5` |
| 20 | 所有者决定：阶段 8 | `validation/route_b_c03/wp_008/DSP_004_PHASE8_DECISIONS_REV1.json` | 2434 | `A6B0FB548A2513F0B52C0789F1DF2225ECBC1881DC2BC23987282018BF3AE01F` |

## 三、请回答的问题

1. **身份**：表中每个文件的 SHA 是否与仓库一致？Manifest 中每个条目的 SHA 和字节数，是否与约束清单一致？
2. **Manifest**：
   - 是否符合类型合同 REV3 和数组政策 REV3？请特别检查 CANON-2 编码，以及条目聚合 SHA `6AE76B80…9713` 能否独立复算。
   - 配套政策 §D1 列出的 9 项偏离是否如实？还有没有未声明的偏离？
3. **运行结论**：
   - 运行记录、收集结果和审计事件三者之间是否一致？请核对进程号、时间、退出码、权限级别，以及记录编号的连续性。
   - 运行实际装载的模块和本地 DLL，是否都在 Manifest 内？
   - 28 个变体的结论是否与 Harness 和输入的规则相符？
4. **保障的强度**：
   - 监督程序和 Harness 声称的防护，是否真的成立？
   - 有没有被高估的地方？例如审计钩子并不是防篡改的沙箱。
   - 有没有一种在现有证据下无法发现的替换或绕过方式？
5. **治理**：
   - 每一步是否都有所有者的决定作为依据？
   - 记录人（Claude）有没有越权，比如自行接受、编造事实？
   - 已知局限是否都已如实声明？
6. **结论**：从技术上看，你是否认为证据足以支持关闭 DSP-004？如有保留，请写明条件。

## 四、回复格式

请按下面格式回复：
- 列出审查者的身份：模型或人员，以及版本。
- 每条发现按 **BLOCKING / NON-BLOCKING / NOTE** 分级，写明文件、位置和具体证据。
- 最后给出总结论，只能是以下三者之一：**支持关闭**、**有条件支持关闭**、**不支持关闭**。

所有者会把回复交回记录人。记录人逐条记录，并说明如何处置；是否关闭，由所有者最终决定。
