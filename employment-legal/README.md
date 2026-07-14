# 劳动人事法务插件

面向中国企业法务和 HR 的劳动用工合规工作流：招聘审查、劳动合同解除/终止、N/N+1/2N 测算、员工手册与规章制度、工时休假、劳动争议、内部调查和政策起草。

> **专业提示：** 本插件输出均为法律工作初稿，必须由中国执业律师或企业内部专业法务复核。解除劳动合同、发出处分决定、签署协商解除协议、作出赔偿承诺或提交仲裁/诉讼材料前，必须人工确认。

## 适用对象

| 角色 | 主要工作流 |
|---|---|
| 企业法务 | 解除/终止审查、员工手册审计、劳动争议预案、政策起草 |
| HRBP / 员工关系 | 证据材料整理、流程检查、补偿金测算初稿 |
| 总法律顾问/管理层 | 高风险解除、群体性裁员、重大劳动争议升级 |

## 首次运行

运行冷启动访谈，建立企业劳动用工画像、审批路径和风险偏好：

```bash
/employment-legal:cold-start-interview
```

配置文件存放在：

```text
~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md
```

## 中国劳动法核心卡点

- 中国法不承认 `employment-at-will`。企业解除劳动合同必须落入法定事由并完成程序。
- 第39条过错解除需重点审查事实、证据、规章制度合法有效、严重性、工会通知。
- 第40条解除需审查医疗期满、不胜任、客观情况重大变化及培训/调岗/协商等前置程序。
- 第41条经济性裁员需审查人数/比例门槛、说明情况、听取意见、向劳动行政部门报告和优先留用规则。
- 补偿不得泛化为 `severance`，必须拆解为 N、N+1、2N。
- 员工手册和规章制度作为解除依据时，必须满足“内容合法 + 民主程序 + 公示告知”。

## 技能列表

| Skill | 用途 |
|---|---|
| `/employment-legal:cold-start-interview` | 冷启动访谈，学习用工地区、员工规模、审批路径、员工手册和解除风险偏好 |
| `/employment-legal:hiring-review` | 入职合规与试用期风控审查，覆盖录用条件、前单位关系、竞业限制、背调和双倍工资风险 |
| `/employment-legal:termination-review` | 中国劳动合同解除/终止审查，覆盖第39/40/41条、工会通知、证据和 N/N+1/2N 风险 |
| `/employment-legal:severance-calculator` | 测算 N、N+1、2N 的适用路径、工作年限折算、平均工资和三倍封顶 |
| `/employment-legal:policy-drafting [topic]` | 起草单项劳动人事制度，并附民主程序流转排期表与公示签收单模板 |
| `/employment-legal:handbook-audit` | 全量审计员工手册和规章制度的“内容合法 + 民主程序 + 公示告知” |
| `/employment-legal:handbook-updates` | 对员工手册或规章制度变更做 diff 审查，识别加重责任、剥夺权利和重新民主程序要求 |
| `/employment-legal:wage-hour-qa [question]` | 工时、加班、休假、最低工资、社保公积金等劳动用工问答初稿 |
| `/employment-legal:worker-classification` | 审查劳动关系、劳务关系、外包/承揽/灵活用工的错分风险 |
| `/employment-legal:social-insurance-audit` | 审计社保公积金缴纳基数、第38条被迫解除、异地/第三方代缴和假外包风险 |
| `/employment-legal:investigation-open` | 开启内部调查事项 |
| `/employment-legal:investigation-add` | 向调查事项加入材料、访谈记录或观察 |
| `/employment-legal:investigation-query` | 针对调查日志提问 |
| `/employment-legal:investigation-memo` | 起草或更新内部合规调查纪要，梳理违纪事实、员工申辩、证据清单和第39条证据链 |
| `/employment-legal:investigation-summary` | 按不同受众生成调查摘要初稿 |
| `/employment-legal:leave-tracker` | 跟踪病假、医疗期、产假、育儿假、工伤等休假事项 |
| `/employment-legal:log-leave` | 添加新的休假记录 |
| `/employment-legal:matter-workspace` | 管理员工、调查、解除、社保或制度事项的 opt-in 本地 YAML 生命周期 |

## Phase 1.5 本地事项工作区

企业单一用工画像默认关闭 matter workspace；需要隔离敏感员工、内部调查、解除、群体事项或外部律师客户时，可人工启用 `status/new/list/switch/update/close/reopen/none`。默认不跨事项读取，员工敏感个人信息和调查材料不得写入 slug 或隐式跨读。该能力不连接 HRIS/OA，也不自动解除、处分、付款、发送或提交材料。

## 数据和材料

优先提供：

- 劳动合同、岗位说明、offer、薪酬记录、考勤和绩效材料
- 员工手册、规章制度、民主程序材料、公示告知/签收/培训记录
- 违纪证据、沟通记录、工会通知材料
- 工作地点、社保缴纳地、当地社平工资和地方人社口径

未配置云端 MCP 时，可直接上传本地 `.docx`、`.xlsx`、`.pdf` 作为 Local File Mode 输入。

## 不做什么

- 不直接替企业作出解除、处分、裁员、调岗降薪或付款承诺。
- 不在缺少关键事实或地方口径时给出确定金额。
- 不把美国劳动法、州法或任意就业原则作为默认分析框架。

## 回归测试

中国劳动法 Prompt 验收用例见 `references/test-cases-cn.md`。重写技能后，至少抽取第39条解除、第40条不胜任解除、2N 测算、员工手册无民主程序、三期女职工解除等案例做人工回归。
