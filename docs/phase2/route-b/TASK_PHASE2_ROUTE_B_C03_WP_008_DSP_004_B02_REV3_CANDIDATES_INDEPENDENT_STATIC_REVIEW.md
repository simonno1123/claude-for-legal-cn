# DSP-004 B-02 REV3 两份文档候选 — 独立静态复核

本记录是 FA-04 已经点名、路径 B 筹备增量 REV1 尚未做的在库只读复核。对象只有两份物理文档候选。复核确认它们的字节和文内结构。它不把任一 SHA 接受为正式合同，不完成 `DSP004-FA-04`，也不关闭 B-02 或 DSP-004。

依据仍是已经记入的路径 B 原句：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

## 1. 复核基准

| 项目 | 本记录的事实 |
| --- | --- |
| 复核时 `HEAD` | `24c702bbde24c0ea392c064de9fac46e601bdfb6` |
| 两份候选的物化提交 | `60491b56d88583c676a1c2ce856953e96865be7e` |
| 前一筹备增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV1.md` |
| 机器可读结果 | `validation/route_b_c03/wp_008/DSP_004_B02_REV3_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` |
| 该结果 SHA-256 | `21D053CAD383598857F1DDCE170AB28759A035B85C7A3D967C5C20B9AC5AEEB0` |
| 该结果字节 | 11088 |
| 受测模块导入或执行 | 未进行 |
| 商业 P0 | 未执行，未修改 |
| 已固定候选 | 未修改 |

机器结果不嵌入本说明的 SHA。本说明只在外部绑定已经写完的机器结果。

本次使用本机 Python 只做字节散列和候选正文的结构清点。未导入 `identity_gate`、合同模块、捕获候选或场景运行器，未编译 C#，未重放业务场景，未生成 Manifest。

这是同仓库内的后续静态复核，不是跨供应商外审，也不是 Project Owner 对这两个 SHA 的接受。

## 2. 两个物理候选

复核前的预期身份与当前 `main` 上的字节一致。物化提交之后这两份文件没有再改。

| 候选 | 路径 | 字节 | SHA-256 |
| --- | --- | --- | --- |
| 类型合同 REV3 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_TYPED_CONTRACT_REV3_CANDIDATE.md` | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` |
| 数组政策 REV3 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_ARRAY_POLICY_REGISTRY_REV3_CANDIDATE.md` | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` |

两份文件均为 UTF-8、无 BOM、无 CR、无行尾空白。任一文件都不包含对方的 SHA-256。文内互指的路径只是配套定位。

候选正文自己写明：物化不等于固定 SHA 接受，后续复核结论不在形成记录里预填 PASS。本复核记录该句，并维持同一边界。

## 3. 结构

类型合同展开为第 0 至第 6 节。第 2 节的顶层恰好 11 组：`manifest_identity`、`root_bindings`、`runtime_identity`、`import_contract`、`trusted_operation_contract`、`input_contract`、`entries`、`excluded_sets`、`closure_evidence`、`aggregate_identity`、`governance`。第 3.7 节的 Entry 是严格十五字段。`read_phase` 保持逗号连接字符串，第 5.3 节写明它不变成数组。

数组政策第 2 节是连续的 `AP-001` 至 `AP-032`，各一次。其中 `SET_SORTED` 27 条，`ORDERED` 5 条。第 5 节自报的组内计数与路径前缀一致：

| 顶层组 | 政策数 |
| --- | --- |
| `manifest_identity` | 0 |
| `root_bindings` | 4 |
| `runtime_identity` | 4 |
| `import_contract` | 5 |
| `trusted_operation_contract` | 5 |
| `input_contract` | 6 |
| `entries` | 1 |
| `excluded_sets` | 3 |
| `closure_evidence` | 3 |
| `aggregate_identity` | 1 |
| `governance` | 0 |
| 合计 | 32 |

类型合同里写成“数组”的成员是 29 个，都能对上登记路径。其余 3 条登记路径是三组闭集：`import_contract.denied_modules`、`excluded_sets.denied_modules`、`excluded_sets.denied_capabilities`。类型合同把它们写成集合，成员名单只出现在类型合同里：拒绝模块 12 个，拒绝能力 10 个，排除类别 10 个。登记要求固定集合各出现一次，没有把这些名字再列一遍。Entry 类别与用途对应表是 12 行。没有发现第 33 条数组路径。

两份候选第 0 节引用的 Plan V2.2 仍是 54703 字节，`6AD0CFD1FBEB09A5100B577DC1FD2E66054E3155AB299D697CEAD81425DF00BA`。Execution Package V3.2 仍是 54109 字节，`87EE2451298189FDDED9F49AC8106B902290A2AA38CD58158B5972F0BE4463BD`。这是引用散列的再核对，不是对这两份设计文件的接受。

14 项机器核对全部通过。通过表示身份和结构核对成立，并且 ORDERED 缺口仍写在候选里。通过不表示 B-02 关闭。

## 4. 五条 ORDERED 缺口

这五条有选择器和重复拒绝规则，没有填入实际来源。

| Policy ID | 路径 | 选择器 | 本次所见 |
| --- | --- | --- | --- |
| `AP-006` | `runtime_identity.declared_startup_sequence` | `runtime_identity.startup_contract` | 无实际启动序列文件、SHA 或唯一定位 |
| `AP-009` | `import_contract.lookup_order` | `import_contract.origin_policy` | 无实际搜索序列来源 |
| `AP-020` | `input_contract.fixtures` | `manifest_identity.fixture_catalog` | 无原 15 项 fixture 序列的来源文件 |
| `AP-021` | `input_contract.scenarios` | `input_contract.binding` | 无场景序列的已绑定文件身份 |
| `AP-022` | `input_contract.scenarios[].variants` | `input_contract.binding` | 无逐场景登记行 |

数组政策第 3.1 节和第 5 节写明这些真实来源值没有填入。第 4.3 节写明 `AP-006`、`AP-009`、`AP-020`、`AP-021`、`AP-022` 缺一项就不能因表格存在而通过。本复核看到表格在，实际序列来源不在。按候选自己的规则，这五条仍是缺口。

## 5. 六项修订保真尚未在库内建立

类型合同把设计来源写成“A—F 六项定点修订”，并指向会话定位 writing 87426 与 writing 90376。这两个定位不是文件 SHA。仓库里没有单独的 REV2 合同或 REV3 附录文件。

数组政策第 4 节标题写“六项 REV3 修订”，正文编号只有 `4.1` 至 `4.5`。第 4.3 节同时写了 ORDERED 完整性规则和 `NOT_APPLICABLE` 规则。A 至 F 没有标在这些规则上。

因此，类型合同第 6 节所称的六项修订保真，不能用仓库字节对会话原文核对。本复核不补写会话文本。

## 6. B-02 仍然缺少的事项

候选自己的未绑定清单，加上本复核不能代替的接受，仍然包括：

- 这两个物理候选的固定 SHA 接受
- 每条 ORDERED 路径的实际来源文件、唯一序列定位和逐场景登记行
- 四根、大小写、重解析和别名事实
- 具体输入、变体、观察与可达性的准入
- 排除类别的成员关系和装载分支分类依据
- 编码器、生成器和对政策的运行验证
- D-007、可信装载、输出隔离、计时和外侧停止
- 对会话 writing 87426 与 writing 90376 的六项修订保真

`DSP004-FA-04` 因此仍是“设计文本已经在库复核，接受仍开放”。B-02 保持 `OPEN`。

## 7. 本记录的效力

```text
INDEPENDENT STATIC REVIEW RECORDED — REV3 DOCUMENT TEXT ONLY

两个 SHA 的正式合同接受：未建立
B-02：OPEN
DSP004-FA-04：未完成
DSP004-FA-08：未完成
DSP-004：OPEN / HOLD
```

DSP-004 保持 `OPEN / HOLD`。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

本记录不接受 `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F`，也不接受 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123`。两者都不是正式 B-02 合同。

本记录不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`，不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，也不关闭 DSP-004。不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。商业 P0 保持原样。没有真实案件、个人信息、凭据或供应商调用。
