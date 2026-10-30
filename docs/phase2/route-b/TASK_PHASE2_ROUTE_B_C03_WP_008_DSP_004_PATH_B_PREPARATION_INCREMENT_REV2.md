# DSP-004 路径 B 筹备增量 REV2

本增量只记录路径 B 下的下一项筹备事实：两份 REV3 文档候选的在库独立静态复核。它不接受资产，不准入来源，不生成 Manifest，不授权正式运行，也不关闭 DSP-004。

依据仍是路径 B 签署记录。原句是：`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 前一增量 | `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_PATH_B_PREPARATION_INCREMENT_REV1.md` |
| 前一增量 JSON | `045D2DC6C9ED53CB8F795E670A35653576095AE4D2224139F426CFF01C39CA4B`（5737 字节） |
| 本增量 JSON | `validation/route_b_c03/wp_008/DSP_004_PATH_B_PREPARATION_INCREMENT_REV2.json` |
| 本增量 JSON SHA-256 | `BFAFB7A0867156E164EACD8FEB76DF9655F658B6F33FF42A892675BB6356EBED` |
| 本增量 JSON 字节 | 2578 |

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。REV1 已经记下的 FA-02、FA-03 与 FA-05 事实保持原样。本增量不改它们。

## 1. 新增筹备事实：REV3 两份候选的在库复核

FA-04 先前只清点了这两份候选，没有独立复核。该复核现已写入仓库。复核结论是文档结构和身份核对，`Signed` 与 `Accepted` 均为 false。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_B02_REV3_CANDIDATES_INDEPENDENT_STATIC_REVIEW.md` | 7806 | `4B627A2A3FAE41B32081FF8E0F0866B198CAF04E23496D30D5886FEEAEEE188B` |
| `validation/route_b_c03/wp_008/DSP_004_B02_REV3_CANDIDATES_INDEPENDENT_STATIC_REVIEW.json` | 11088 | `21D053CAD383598857F1DDCE170AB28759A035B85C7A3D967C5C20B9AC5AEEB0` |

被复核的物理候选仍是：

| 候选 | 字节 | SHA-256 | 本增量后的状态 |
| --- | --- | --- | --- |
| 类型合同 REV3 | 29240 | `AAD3921DEFCF62DF63F4A575F67B4DB1C5766414828128DB101D325D9A09DE1F` | 已复核，未接受为正式合同 |
| 数组政策 REV3 | 16317 | `39F0FDC37CD8C8C52B0ABD8754BF1173C698E7F846530BFDB0DF032EF3A88123` | 已复核，未接受为正式合同 |

复核所见：顶层 11 组与 32 条路径政策互相可对上；`AP-006`、`AP-009`、`AP-020`、`AP-021`、`AP-022` 仍没有实际序列来源；六项 REV3 修订对会话原文的保真尚未在库内建立。

## 2. 本增量故意不做的事

- 不把上述两个 REV3 SHA 接受为正式 B-02 合同。
- 不完成 `DSP004-FA-04`。B-02 保持 `OPEN`。
- 不创建 `validation/route_b_c03/wp_008/PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`。
- 不生成 Manifest，不授权正式运行，不完成 `DSP004-FA-08`，不关闭 DSP-004。
- 不为来源与根候选 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份设计复核文件。
- 不执行受测模块，不改商业 P0。

## 3. 仍须以后的资产级决定

路径 B 没有代替下列决定：

- 是否对两个 REV3 SHA 作固定 SHA 接受
- 五条 ORDERED 路径的实际来源、唯一定位和逐场景登记
- 四根、具体输入、排除成员关系、装载分支和运行验证
- Manifest、正式运行和 DSP-004 关闭
