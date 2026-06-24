---
name: registry-browser
description: >
  Search watched registries for community legal skills, showing matches with
  descriptions and offering to show the full SKILL.md before install. Use when
  the user says "browse", "search skills", "find a skill for", "what's out
  there for", or wants to add a new registry to the watchlist.
argument-hint: "[search query]"
---
<!-- CHINA_LOCALIZATION_START -->
## 中国法域与引用规则（强制）

- 默认法域为中华人民共和国大陆地区法律；不得默认套用美国法、州法、普通法或欧盟法框架。
- 引述中国法律法规时，必须标注法律全称/缩略 + 条文序号（条/款/项）；无法确认时写 `[法条待查证]`，并停止编造式引用。
- 区分法律、行政法规、部门规章、司法解释、地方性法规、规范性文件、指导案例/典型案例的效力层级。
- 涉及地方差异（最低工资、社保、公积金、产假、监管口径、法院管辖等）时，必须标注适用省/市及 `[地方规定 — 待查证]`。
- 输出均为中文法律工作初稿，供执业律师或企业法务审阅；涉及发送、签署、备案、申报、起诉、仲裁、解除劳动合同等后果性动作前，必须设置人工确认门。
<!-- CHINA_LOCALIZATION_END -->


# /registry-browser

1. Load `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries.
2. Use the workflow below.
3. Search each registry. Show matches with descriptions.
4. Offer to show full SKILL.md for any match.

---

## Purpose

Find skills across the watched registries. Search, preview, decide.

## Load context

`~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries list.

## Workflow

### Step 1: Fetch registry indexes

For each watched registry:

- GitHub repos: fetch `skills/` directory listing and each `SKILL.md` frontmatter (name + description).
- Marketplace-style registries: fetch the index.

Cache the index locally (`references/registry-cache.json`) so browsing is fast. Refresh cache if >7 days old or on request.

### Step 2: Search

Match query against skill names and descriptions. Simple keyword match is fine — these are small enough that fuzzy search is overkill.

Also: browse by category if the registry organizes skills that way.

### Step 3: Present matches

```markdown
## Search: "[query]"

**Found [N] skills across [M] registries:**

### [skill-name]
**From:** [registry name]
**Description:** [from frontmatter]
[View full SKILL.md] [Install]

### [skill-name]
[...]
```

### Step 4: Preview

On "view full SKILL.md": fetch and show the whole file. User reads it before deciding to install. No surprises.

### Step 5: Add a registry

If the user has a URL to a registry not in the watchlist:

1. Fetch it, validate it's a skills repo (has `skills/` or `.claude-plugin/`)
2. Show what's in it
3. Add to `~/.claude/plugins/config/claude-for-legal/legal-builder-hub/CLAUDE.md` → watched registries on confirmation

## Default registries

- **lpm-skills** — 14 legal project management skills. Practice-agnostic. Good starting point.
- Space for others to be added as the ecosystem grows.

## What this skill does not do

- Install anything. It browses. skill-installer installs.
- Rate or review skills. It shows you the SKILL.md; you judge.
- Search the whole internet. Only watched registries.
