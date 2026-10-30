# DSP-004 路径 B 范围签署记录 REV1

本记录只保存 Project Owner 已经发出的这一句，并固定它指向的决定包。生效范围等于该句：继续正式验收筹备，不接受资产，不关闭 DSP-004。

## 1. 原句

`签署路径 B：只继续正式验收筹备，不接受资产、不关闭 DSP-004。`

| 项目 | 值 |
| --- | --- |
| 决定权 | Project Owner |
| 记入时间（UTC） | `2026-10-30T08:18:53Z` |
| 时间含义 | 本代理收到该句的时间。原句自身没有时钟。 |
| 机器记录 | `validation/route_b_c03/wp_008/DSP_004_PATH_B_SCOPE_SIGNING_RECORD_REV1.json` |
| 机器记录 SHA-256 | `E92CAD5CBA87D974430735B53491B85F837BF5FECCE0AEBF629ADE1BAB05E025` |
| 机器记录字节 | 2242 |
| 当时分支 HEAD | `4710fe9b09eb9e4e91e748baf7a025f42c2a91f8` |
| 拉取请求 | https://github.com/simonno1123/claude-for-legal-cn/pull/2 |

该句在记入本仓库时对路径范围生效。本文件是这句话的分离副本。不需要先把本文件接受为资产，路径范围才生效。本文件也没有把任何既有 SHA 接受为资产。

## 2. 所指向的未签署决定包

决定包在该句发出前已经固定。本记录不改写它。

| 文件 | 字节 | SHA-256 |
| --- | --- | --- |
| `docs/phase2/route-b/TASK_PHASE2_ROUTE_B_C03_WP_008_DSP_004_FORMAL_ACCEPTANCE_OWNER_DECISION_PACKET_REV1.md` | 8630 | `9B0A3C048E479B714083952E76CF6620A2AE046EA23D2CC95192D967CF5A6736` |
| `validation/route_b_c03/wp_008/DSP_004_FORMAL_ACCEPTANCE_OWNER_DECISION_PACKET_REV1.json` | 15824 | `3E6773EF54B6F6F1E253B42FAF92D5714C4BDE36EA6B7CFCF4E5A73359AC3BDC` |

决定包第 6 节把同一句标成“尚未签署、可复述”。本记录把该句改为已经签署。决定包字节保持原样。

## 3. 范围

本签署解锁的只有正式验收筹备，而且筹备产物本身仍不是资产接受。

一并确认的筹备事实：两文件缺失记录与决定包 FA-02 建议一致，因为它只确认负面存在性，不接受环境资产。缺失记录 JSON `D8142F5B8CFF55BE0AE26F652A7A09D86BC2E6172DC592D62D9230260A115E97`（1965 字节）因此作为本次筹备事实被确认。`VENV_ROOT` 仍是 `NOT_ESTABLISHED`。`DSP004-FA-02` 仍未完成。

本签署不包含：

- 任何固定 SHA 的资产接受，包括 FA-01 的在库复核
- 来源准入
- Manifest，或 `PYTHON_RUNTIME_DEPENDENCY_MANIFEST.json`
- 正式运行授权
- `DSP004-FA-08` 或 DSP-004 关闭
- 为 SHA `57BAF161E3C2616F15F576F07D9BC106C0103B57710DCAF9727E6033A75C7D93` 新增第二份来源与根设计复核文件

DSP-004 保持 `OPEN / HOLD`。B-01、B-02 保持 `OPEN`。
