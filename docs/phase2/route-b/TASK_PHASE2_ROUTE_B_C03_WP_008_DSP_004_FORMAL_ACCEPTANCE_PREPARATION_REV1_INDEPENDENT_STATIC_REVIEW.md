# DSP-004 正式验收筹备包 REV1 — 独立静态复核

本记录只覆盖正式验收筹备包的固定字节、来源身份和关卡原文。它是筹备包第 8 节所缺的在库只读复核。关卡完成、来源准入、根批准、Manifest、正式运行和 DSP-004 关闭仍待 Project Owner 的单独决定。

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `f5b66ab4c2fb03e919c9a1c1d3b88d338026d513` |
| 筹备包物化提交 | `4005b37a98cb0783dcba46bd684f65103f48074b` |
| 剩余工作交接提交 | `6f0b4a72a8caf70561dac74373120f58616f1f3e` |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_PREPARATION_REV1_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `459BAB3E2D5C06395E7AF2E5AF89BB556311C2B16846053964AF5A1AE47902D5` |
| 该结果字节 | 11573 |
| 受测模块导入或执行 | 未进行 |
| 第 4 节两个环境文件 | 未读取 |
| 已固定文件 | 未修改 |
| 路径 A / 路径 B | 未选择 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。作者静态核对 `DSP_004_FORMAL_ACCEPTANCE_PREPARATION_REV1_STATIC_CHECK.json` 仍写明 `IndependentReviewPerformed: false`；该历史结论保持原字节，本记录不回写它。

本次使用本机 Python 只做字节散列和 JSON 解析。未导入 `identity_gate`、合同模块、捕获候选或场景运行器，未编译 C#，未重放业务场景。

复核会话与筹备包物化提交分离，并保持只读。这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 的阳性决定。

## 2. 固定复核对象

| 路径 | 字节 | SHA-256 | 结果 |
| --- | --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_PREPARATION_PACKAGE_REV1.md` | 11121 | `FD27724FF5DB9C7F2DCC5175FD6B4E588F1961D73ADC2807E9EF2DE8004D4055` | 与作者静态核对一致 |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_PREPARATION_CANDIDATE_REV1.json` | 15464 | `127521BAF310DDF57C33336B8A17B29D40002E4419A5E5CCB0ED029562DB24E2` | 与筹备包正文及作者静态核对一致 |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_PREPARATION_REV1_STATIC_CHECK.json` | 10828 | `B121068AEF2EC1F3BB4B62435FECD4FDE2687179F85A0E6411E18BC28F327912` | 作者核对原样保留 |

三份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。筹备 JSON 无重复键。

作者静态核对中的 35 个受保护路径与当前字节一致，其中包含交接文件第 7 节的固定身份清单。交接文件自身仍为 14774 字节，SHA-256 `538283D7E48520B56B90ACA42A705A43AFEA468AF6DE8B7A46AE34636A3805AA`。

## 3. 筹备包正文结论

```text
STATIC PASS / LIMITED — PREPARATION PACKAGE TEXT AND FIXED-IDENTITY REVIEW ONLY

范围内文本或身份阻断项：0
关卡完成数：0
已建立的根绑定：0
已建立的实际侧来源：0
接受 / 来源准入 / 运行资格：NOT ESTABLISHED
```

| 核对项 | 静态评定 | 定位 |
| --- | --- | --- |
| 六侧角色 | PASS | `SRC004-E/A` 的 Project、Session、Provider 各一，无重复 |
| 三项预期保真 | PASS | 载体 SHA `BE8C55796587BBA65E22B048291E1688A8B076D02DA2A48DE412919BEB10F368`；定位、身份、版本和 `SYNTHETIC-*-001` 与基线第 3.1–3.3 节唯一行一致 |
| 三项实际侧 | PASS / GAP | 身份、载体、捕获观察保持 null；`admission_effect` 均为 `NONE_GRANTED_BY_THIS_PACKAGE` |
| 四类准备根 | PASS / GAP | 四项 `binding_state` 均为 `NOT_ESTABLISHED_BY_THIS_PACKAGE`，`read_authority_granted` 为 false |
| 八个关卡 | PASS / GAP | `DSP004-FA-01` 至 `FA-08` 的 `completed` 仍为 false |
| 复核状态字段 | PASS | 筹备 JSON 的 `review_status` 仍为 `NOT_INDEPENDENTLY_REVIEWED` |
| 原 Fixture 与现门禁 | PASS / GAP | `C03-TA-V-004.json` 仍要求 `BLOCKED_ISOLATED` / `BOUNDARY_MISMATCH`；`identity_gate.py` 仍只比较事项 ID、版本和 actor，返回 `REJECTED — ISOLATION FAILURE`，参数中没有 Project、Session、Provider |
| 运行依赖 Manifest | PASS / GAP | `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在，本复核未创建 |
| 环境清点 | 未执行 | `.venv-validation/pyvenv.cfg` 与 `.venv-validation/Scripts/python.exe` 的许可状态仍是 `PROPOSED_ONLY_NOT_GRANTED_BY_THIS_PACKAGE` |

`PROJECT_ROOT` 记录的 `C:/Users/Administrator/Documents/claude-for-legal-cn-phase2.5` 仍只是历史工作区定位。本复核环境不把它当作可信根或读取授权。

19 项机器核对全部通过。通过表示筹备包如实保留缺口，不表示缺口已经关闭。

## 4. 筹备包之后的身份，以及它们没有关闭的事项

下列文件在 `4005b37` 之后进入仓库。本复核重算了引用散列，确认与各文件现在的字节一致。这不是对这些设计正文的接受，也不是对来源与根候选全文的独立设计复核。

| 提交 | 路径 | 字节 | SHA-256 | 仍保留的状态 |
| --- | --- | --- | --- | --- |
| `60491b56d88583c676a1c2ce856953e96865be7e` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md` | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` | B-02 OPEN；固定 SHA 接受未建立 |
| `60491b56d88583c676a1c2ce856953e96865be7e` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` | 32 条路径政策仍是文档对应；实际序列来源未填 |
| `f20fc2c7294cc6d95b49edf4e974c37ff08463d8` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_ENVIRONMENT_IDENTITY_REBINDING_REV1_CANDIDATE.md` | 15112 | `DC6DAA71B5ADB99E1E2FF61FD535B51C661C7671E3E08F651046740300B329EA` | 七个历史环境观察未在本复核重读 |
| `f3a41bca5d6857f2bb22a6a51c10895ea84ef076` | `docs/phase2/route-b/DSP_004_SOURCE_USE_AND_INPUT_EXTENSION_REV1_CANDIDATE.md` | 24541 | `F4B995D8F2DA424E68D94EA7E31FB6387F628C7681BEF5CC05807A29D6684A2F` | 形成时状态仍为独立静态复核待完成 / 未接受；17 个 REF 散列匹配 |
| `25a65aae4212823c09e0b6acb0287cb933148468` | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_SOURCE_ROOT_ADMISSION_PREPARATION_REV1_CANDIDATE.md` | 21257 | `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` | 形成时状态仍为固定 SHA 独立静态复核待完成 / 未接受；B 节 7 个散列匹配 |

`DSP004-FA-04` 因此仍是“设计文本已经存在，接受仍开放”。REV3 候选没有把该关卡改为完成。

来源使用候选的提交说明写的是 `back up accepted DSP-004 source-use design REV1`。文件字节写的是 `MATERIALIZED — INDEPENDENT STATIC REVIEW PENDING / NOT ACCEPTED`。提交说明不是接受记录。本复核不改写该提交。

来源与根候选要求本批次复核通过会话交付，并且不另增第二份复核文件。仓库里没有与 writing block 31684 对应的独立底稿，所以本复核只确认七个参考文件的字节，不把嵌入正文宣告为已与会话原文逐字核对。该候选自己的设计正文复核仍未作为在库记录存在。

Plan V2.2 仍为 54703 字节，`6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA`。Execution Package V3.2 仍为 54109 字节，`87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD`。

## 5. 仍须 Project Owner 决定的事项

交接文件第 6 节的路径 A 与路径 B 都还没有被选择。本复核不代替该选择。

| ID | 当前事实 | 仍要 Owner 决定的对象 | 决定前不能做的事 |
| --- | --- | --- | --- |
| `DSP004-FA-01` | 在库只读复核已写入本记录 | 是否把该复核计入关卡完成 | 不把筹备 JSON 的 `completed` 改为 true |
| `DSP004-FA-02` / `DSP004-R-02` | 四根未绑定；两个环境文件未读 | 是否授权精确只读清点，以及准备根的来源、解析和读取范围 | 不探测 `.venv-validation`，不用历史 Windows 路径补可信根 |
| `DSP004-FA-03` / `DSP004-R-01` | 三个实际侧来源为 null | 六侧来源的实际捕获入口、职责和调用归属 | 不从预期、关联字符串或 null 回填实际侧 |
| `DSP004-FA-04` / `DSP004-R-03` | REV3 类型合同与数组政策候选已固定字节，B-02 仍 OPEN | 是否对上述两个 SHA 作有限设计接受 | 不把玩具投影或未接受候选当成正式合同 |
| `DSP004-R-04` | 来源使用候选的提交说明与文件状态不一致 | 以哪一份固定字节作为有限设计决定的对象 | 不把提交标题当作签署 |
| `DSP004-FA-05` / `DSP004-R-05` | 完整输入、比较映射和 Harness 未作固定 SHA 处置 | 当前适用的输入候选、映射和 Harness | 不把 189 项合成检查拼成输入准入 |
| `DSP004-FA-06` / `DSP004-R-06` | 依赖、启动和隔离前提未建立 | 允许保留的 LIMITED 范围 | 不把私有子进程或散列相同写成生产装载 |
| `DSP004-R-07` | 停止与清理限制仍在 | 可以保留的 LIMITED 是否明确可接受 | 不宣告零 I/O、零残留或物理硬停止 |
| `DSP004-FA-07` / `DSP004-FA-08` / `DSP004-R-08` | Manifest 与正式运行未授权 | 关卡顺序满足之后的 Manifest、运行范围和关闭决定 | 不生成 Manifest，不把 DSP-004 标为 CLOSED |
| 来源与根候选复核 | 参考散列已核对；设计正文的在库复核未建立 | 是否授权单独的在库设计复核；该候选原批次禁止另增复核文件 | 不在未授权时补写第二份复核来冒充原批次会话结论 |

## 6. 本记录的效力

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。全部既有 LIMITED、历史失败和后续验证记录保留。

本记录不接受任何候选，不准入来源，不建立准备根，不生成 Manifest，不授权正式运行，也不把 Phase 2 Provider 或运行时描述为已经可用。没有真实案件、个人信息、凭据或供应商调用。独立 ACOS 与其他项目未访问。

阶段备份只保存本复核记录。备份与关卡接受是两件不同的事。
