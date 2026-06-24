---
name: gaps
description: Open gaps tracker — what's flagged and not yet closed. Use when the user asks "what gaps are open", "gap tracker", "remediation status", or wants to close (--close GAP-ID) or risk-accept (--accept GAP-ID) a tracked gap.
argument-hint: "[optional: --close GAP-ID | --accept GAP-ID]"
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# /gaps

1. Read the gap tracker at `~/.claude/plugins/config/claude-for-legal/regulatory-legal/gap-tracker.yaml`.
2. If `--close`: mark gap closed with resolution note.
3. If `--accept`: record the risk-acceptance rationale and acceptor, status → risk-accepted.
4. Otherwise: report open gaps by age and materiality.

> Detailed tracker schema, status-report format, owner-notification logic (per-send confirmation, no exceptions), reminder cadence, the close/risk-accept modes, and the consequential-action gate live in the **gap-surfacer** reference skill — load it before doing substantive work.
