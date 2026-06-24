# Product Legal（中国大陆产品合规版）

`product-legal` 面向中国企业产品法务、合规、产品经理和营销团队，用于产品功能上线前审查、营销宣传审查、消费者权益、电商与平台责任、质量安全与召回、未成年人保护、个人信息、算法和 AI 触点的首轮合规把关。

> 本模块输出均为内部法律分析初稿 / 保密文件 / 合规工作底稿。中国大陆法下不承诺任何可对抗司法、仲裁或行政监管机关调取的证据特权。所有上线、投放、下架、召回、整改或对外回复决定，必须由中国执业律师或企业法务复核确认。

## Phase 1 技能范围

第一阶段仅保留 5 个核心技能：

| 命令 | 定位 |
|---|---|
| `/product-legal:cold-start-interview` | 中国产品画像访谈，作为唯一初始化入口 |
| `/product-legal:launch-review` | 中国大陆产品上线前合规审查矩阵 |
| `/product-legal:marketing-claims-review` | 广告、促销、直播带货、达人种草与宣传用语审查 |
| `/product-legal:feature-risk-assessment` | 单项高风险功能穿透评估 |
| `/product-legal:is-this-a-problem` | 产品经理快速合规分诊 |

以下能力不作为 Phase 1 正式主线：

| 项目 | 处理 |
|---|---|
| `/product-legal:customize` | 已并入 `cold-start-interview`，仅保留兼容提示 |
| `/product-legal:matter-workspace` | 降级为 Phase 2，多客户外部律师场景再启用 |
| `launch-watcher` | 降级为 Phase 2，国内协同系统自动监控暂不默认开启 |
| `currency-watch.md` | 仅作为人工更新清单，不作为自动化法律动态源 |

## 上线审查矩阵

`launch-review` 默认执行中国大陆“六合一”产品合规审查：

1. 用户权益与消费者保护：七日无理由退货、三包、格式条款、自动续费、预付费、欺诈赔偿。
2. 电商与平台责任：商家资质、自营与非自营区分、搜索排序、广告标识、押金退款、搭售与默认勾选。
3. 网络安全与个人信息门槛：最小必要、告知同意、第三方 SDK、敏感个人信息、未满 14 周岁儿童信息、数据出境。
4. 算法与 AI 触点：自动化决策、大数据杀熟、算法推荐、深度合成、生成式 AI 标识和备案触发。
5. 质量标准与召回：强制标准、CCC、产品说明、警示标识、缺陷报告、消费品召回。
6. 监管责任与整改路径：市场监管、网信、工信、消协、平台治理、行政处罚、下架和限期整改。

质量安全与召回是默认必检栏目，不只在硬件或特殊行业中触发。数据、算法和 AI 由本模块先做门槛筛查；触发高风险时，再转交 `privacy-legal` 或 `ai-governance-legal` 做专项深审。

## 默认连接器

本模块与中国版 `.mcp.json` 保持一致：

| 连接器 | 用途 |
|---|---|
| `npc-law-database` | 国家法律法规数据库 / 中国人大网法条检索 |
| `gov-regulatory-sites` | 国务院、部委、地方监管官网动态核验 |
| `wps-cloud-docs` | WPS / 金山文档云端材料同步 |

未配置云端连接器时，默认使用 Local File Mode：用户可直接上传 PRD、产品截图、营销文案、价格页、售后政策、隐私政策、数据流程图、检测报告或认证文件。

## 快速开始

```bash
/product-legal:cold-start-interview
```

初始化后可运行：

```bash
/product-legal:launch-review
/product-legal:marketing-claims-review
/product-legal:is-this-a-problem "会员自动续费上线前需要法务看吗？"
```

## 输出要求

所有技能必须：

- 明确结论：`Block`、`Danger`、`Needs Review`、`Conditional Go` 或 `Clear`。
- 标注监管触点：市监局、网信办、工信部门、消协、平台规则或行业主管部门。
- 给出上线条件：可上线、整改后上线、暂缓上线、禁止上线。
- 对待查法条、地方口径或监管动态标注 `[待查证]`。
- 对未成年人、敏感个人信息、自动化决策、特殊广告、强制认证、质量缺陷和召回风险采用高风险默认值。
