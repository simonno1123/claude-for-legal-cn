# DSP-004 路径 B 筹备增量 REV6

本增量只记录路径 B 下的下一项筹备事实：一份 FA-06 剩余 LIMITED 登记候选。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

本步授权原句是：`写下一项筹备文档，不准入、不接受资产、不关 DSP-004.`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV5.md` |
| 前一增量 JSON | `32527B68DAA54A5763473AF4488DA19653778B5A85BE41CF585FE7C4BFC902ED`（4678 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV6.json` |
| 本增量 JSON SHA-256 | `48AB526A92412AFCD3CDB982E7A68FB936D5D6325C26C7506C83428A16799FDA` |
| 本增量 JSON 字节 | 2845 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 至 REV5 已经记下的筹备事实保持原样。本增量不改它们。

## 1. 新增筹备事实：FA-06 剩余 LIMITED 登记候选

这是只列出的登记候选，不是处置，不是来源准入，也不是 Manifest。`Signed` 与 `Accepted` 均为 false。准入状态是 `NOT_ADMITTED`。`DSP004-FA-06` 仍是 `未建立充分前提`。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.md` | 22701 | `AAF90D311F2C85C48EF652E903D4B430D1F339F1FA465527DE679087F30B2305` |
| `validation/route_b_c03/wp_008/DSP_004_FA06_LIMITED_REGISTER_REV1_CANDIDATE.json` | 38377 | `500015848949A8B789E0E44F2BB21AE0676D50B9440EA89124BB30CDC8B06254` |

登记 61 行，顺序是点名来源的原文顺序，随后才是另外已经分条的记录。没有重排，没有新编号，没有处置。`EVIDENCE_PRESENT_UNACCEPTED` 35 行，`EVIDENCE_ABSENT` 16 行，`REQUIRES_RUNTIME_ROOT` 10 行。

两份虚拟环境缺失记录已散列，里面没有 LIMITED 条目，所以没有入行。`PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json` 仍不存在，本增量没有创建它。

四项已经点名的 LIMITED 审查项仍在：`C03-WP008-V3-RQ-021`、`C03-WP008-V3-G-017`、`C03-WP008-RDM-V2-RQ-018`、`C03-WP008-RDM-V2-G-014`。本增量不把它们标成消除。

三个实际侧仍为 null / `UNBOUND`：`SRC004-A-PROJECT`、`SRC004-A-SESSION`、`SRC004-A-PROVIDER`。REV1 点名的七个既有捕获候选仍是 `NOT_SELECTED` / `NOT_ADMITTED`。

`DSP004-FA-03` 仍是 `MISSING_BINDING_AND_ACTUAL_ENTRY`。`DSP004-FA-04` 仍未完成。B-01 保持 `OPEN`。B-02 保持 `OPEN`。

## 2. 本增量故意不做的事

- 不准入任何来源，不把任何固定 SHA 接受为正式合同、Manifest 或来源准入。
- 不把两个 REV3 SHA `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` 与 `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-03`，也不完成 `DSP004-FA-04`。B-01 与 B-02 保持 `OPEN`。
- 不完成 `DSP004-FA-06`。它仍是 `未建立充分前提`。
- 不执行捕获代码、`identity_gate`、Fixture、场景运行器或受测模块。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不改商业 P0。

## 3. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 三个实际侧的来源身份、版本、载体、定位、产生者职责、授权和已经绑定的捕获入口
- 另一次获准调用；只有那次调用发生时才允许读取实际引用
- 哪些依赖、启动、隔离、停止与清理 LIMITED 可以保留
- 导入闭包、两侧调用身份、检查到使用的防替换，以及 T0 / PE / OS 证据
- 是否对两个 REV3 SHA 作固定 SHA 接受
- 是否对 FA-03、ORDERED 清点或本登记的固定 SHA 作接受或准入
- `AP-006` 与 `AP-009` 在运行根确立之后的实际定位
- Manifest、正式运行和 DSP-004 关闭
