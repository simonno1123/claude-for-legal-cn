---
name: customize
description: >
  Guided customization of your AI governance practice profile — change one thing
  without re-running the whole cold-start interview. Adjust risk posture,
  escalation contacts, use-case registry entries, vendor AI positions,
  AI policy commitments, impact-assessment house style, or matter workspace
  paths. Use when the user says "change my [thing]", "update my profile",
  "edit my config", "tune my playbook", or "customize".
argument-hint: "[section name, or describe what you want to change]"
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# /customize

## When this runs

The user typed `/ai-governance-legal:customize`. They want to change something
in their practice profile — a risk posture, an escalation contact, a playbook
position, a jurisdiction, an output format — without re-running the whole
cold-start interview and without hand-editing YAML.

## What to do

1. **Read the config.** Read
   `~/.claude/plugins/config/claude-for-legal/ai-governance-legal/CLAUDE.md`
   (and `~/.claude/plugins/config/claude-for-legal/company-profile.md` one
   level up). If the plugin config does not exist or still contains
   `[PLACEHOLDER]` values, say:

   > You haven't run setup yet. Run `/ai-governance-legal:cold-start-interview`
   > first — customize is for adjusting a profile you already have.

2. **Show the customizable map.** List what's in the profile, grouped, with a
   one-line summary of the current value:

   - **Company / who you are** — name, industry, jurisdictions, stage, practice
     setting *(shared across all 12 plugins — changes flow through
     `company-profile.md`)*
   - **Regulatory footprint** — EU AI Act, state AI laws, sector regulators in
     scope
   - **Risk posture** — conservative / middle / aggressive, what each means for
     triage and AIA output
   - **People** — governance team, AI risk owner, escalation chain, approvers
   - **Use case registry** — approved / conditional / never entries, and
     conditions attached to each
   - **AI system inventory** — per-system role (provider / deployer / etc.) and
     tier under the EU AI Act. Run `/ai-governance-legal:ai-inventory` for
     the dedicated editor.
   - **Vendor AI governance** — training-on-data, liability, model-change
     notice, and other positions in your vendor AI playbook
   - **AI policy commitments** — the public or internal commitments your AI
     policy has made, that the plugin cross-checks against
   - **Impact assessment house style** — AIA section order, risk scoring
     format, stakeholder framing
   - **Workflow** — intake path, output format, matter workspace paths, review
     cadence for the policy monitor
   - **Integrations** — what's connected (Slack, document storage,
     scheduled-tasks), what falls back

3. **Ask what they want to change.**

   > What would you like to adjust? Pick a section, or describe the change in
   > your own words.

4. **Make the change.** Show the current value, ask for the new value, explain
   what changes downstream, confirm, write it to the config.

   Examples of downstream explanation:
   - *Risk posture middle → conservative:* "I'll flag more use cases as
     conditional rather than approved, surface more AIA follow-ups, and
     recommend more conservative vendor AI redlines."
   - *Adding an escalation contact:* "Every skill that routes escalations
     (`/use-case-triage`, `/vendor-ai-review`, `/reg-gap-analysis`) will now include this
     contact on the relevant risk bands."
   - *New use case registry entry:* "`/use-case-triage` will match against this entry
     on its next run. Existing AIAs aren't rewritten — re-run them if you want
     the new posture reflected."

5. **For shared-profile changes** (company name, industry, jurisdictions,
   practice setting, stage): write to
   `~/.claude/plugins/config/claude-for-legal/company-profile.md` and note:

   > This change affects all 12 plugins — any plugin that reads your
   > jurisdiction footprint now sees [new value].

6. **Close.**

   > Done. Your next output will reflect the change. Anything else? You can
   > run `/ai-governance-legal:customize` anytime.

## Guardrails

- **Never delete a section.** If the user wants to "remove" something, set it
  to `[Not configured]` and explain what that means for the plugin's behavior.
  ("Removing your escalation chain means `/use-case-triage` will flag escalation-worthy
  items but won't route them to a specific person.")
- **Flag internal inconsistency.** If the change would make the profile
  inconsistent (e.g., risk posture aggressive + escalation "everything goes to
  the GC"; or "EU AI Act in scope" + "no systems flagged for the EU"), flag
  the tension and ask which one they want.
- **Flag guardrail degradation.** If the user asks to turn off a guardrail
  ("stop adding the `[review]` flag," "drop the citations warning," "skip the
  privilege header"), explain what the guardrail protects against and confirm
  they understand the trade-off. Most guardrails are adjustable — a few are
  structural:
  - The `[review]` flag mechanism (tells the user when legal judgment is
    needed rather than a confident wrong answer) — load-bearing, don't
    remove.
  - Source attribution tags on retrieved content — load-bearing, don't remove.
  - `[verify]` tags on cited statutes/regulations — load-bearing, don't
    remove.
- **One change at a time.** Don't re-ask the whole interview. If the user
  wants multiple changes, handle them sequentially and confirm each before
  moving on.
