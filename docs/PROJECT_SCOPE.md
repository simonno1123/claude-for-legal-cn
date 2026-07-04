# Project Scope

This document defines the governance baseline for `claude-for-legal-cn`.

## v1 Goal: Complete Chinese Port / Faithful Port

Version 1 is a faithful China-law port of the upstream `claude-for-legal` project.
The goal is structural and functional parity first:

- preserve the upstream directory, plugin, skill, agent, workflow, prompt, and documentation concepts wherever possible;
- map each upstream capability to the best China Mainland legal implementation;
- replace legal substance, examples, sources, citations, and review gates with China-law equivalents;
- keep enough structural compatibility to make future upstream diffs reviewable.

Faithful Port does not mean literal translation. Each upstream component should be
evaluated by responsibility:

1. What problem does the upstream component solve?
2. What is the China-law implementation that solves the same problem?

## v1 Non-Goals

Version 1 should not prioritize one practice setting or create new product layers.
In particular, v1 does not do the following:

- no enterprise-legal-first priority over law firm, clinic, student, regulatory, or other upstream use cases;
- no personal practice preference or maintainer-specific business priority as the organizing principle;
- no specialized practice packs beyond what is needed to port upstream capabilities;
- no built-in commercial legal database dependency;
- no claim that PKULAW, Yuandian, Wolters Kluwer, Faxin, Alpha, court systems, OCR, company search, or enforcement intelligence is production-integrated;
- no architecture rewrite whose main purpose is optimization rather than faithful porting.

## v2+ Expansion Boundary

Capabilities beyond upstream parity belong to later versions:

- MCP provider integrations for PKULAW, Yuandian, Wolters Kluwer, Faxin, Alpha, official legal databases, and enterprise data systems;
- specialized Practice Packs for industries, transaction types, litigation workflows, employment subdomains, privacy/data, IP portfolios, or regulatory verticals;
- OCR, company search, judgment search, enforcement intelligence, business registry, public records, and workflow automation;
- reusable China legal capability layers such as `legal-core-cn`.

The v1 baseline may contain placeholder connector interfaces and local smoke-test
servers, but these must be documented as infrastructure placeholders, not as
production provider integrations.

## Acceptance Rule

v1 is complete only when the upstream-to-China mapping matrix is reviewed and all
upstream modules, skills, agents, workflows, and documentation concepts are either:

- faithfully ported;
- intentionally preserved as external/vendor content;
- explicitly marked with an unresolved mapping decision.

