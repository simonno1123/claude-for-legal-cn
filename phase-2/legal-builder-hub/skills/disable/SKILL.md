---
name: disable
description: >
  Disable a community skill installed through the hub without removing its
  files. Use when the user wants to temporarily quiet a community skill
  ("disable [skill]"), stop its hooks from firing while keeping its config,
  or re-enable a previously disabled skill.
argument-hint: "[skill name]"
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# /disable

Run the `disable` workflow from the skill-manager reference skill against the
named skill.

What disable does:

- Renames the skill's `SKILL.md` to `SKILL.md.disabled` so Claude no longer
  discovers it as an active skill. Files, references, templates, and config
  stay in place.
- If the skill ships hooks in `hooks/hooks.json`, also rename that file to
  `hooks.json.disabled` so no automatic triggers fire while the skill is
  disabled.
- Logs the action to
  `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/install-log.yaml`.

Safety rules:

1. **Only disable community skills installed through this hub.** Same check
   as uninstall — consult the install log and CLAUDE.md installed table.
2. **Never disable a first-party plugin's skill.** Off-limits.
3. **Confirm before renaming.** Show the paths, get explicit `yes`.

Re-enable by running the command again with the same skill name — the
skill-manager workflow recognizes a disabled skill and flips the rename back.

> Detailed uninstall, disable, and re-enable workflows live in the
> `skill-manager` reference skill — load it before doing substantive work.
