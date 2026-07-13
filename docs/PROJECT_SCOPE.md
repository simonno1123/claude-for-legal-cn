# Project Scope

Status: Phase 1 scope reclassified by `TASK_017_PHASE1_SCOPE_RECLASSIFICATION_DECISION` on 2026-07-13.

This document defines the governance baseline for `claude-for-legal-cn`.

## Phase 1 Goal: China-Law Baseline

Phase 1 freezes a usable foundation for Chinese licensed lawyers, in-house legal
teams, clinics, and legal learners. Its release condition is:

- 12 first-party root modules are discoverable and structurally valid;
- their core legal substance, sources, examples, citations, and review gates use China Mainland law;
- mandatory CI, command references, generated configuration, and documentation are internally consistent;
- every upstream responsibility is mapped to Phase 1, Phase 1.5, Phase 2, or an isolated external/vendor boundary;
- deferred capabilities are described truthfully and are not presented as implemented.

Faithful Port remains the responsibility-mapping method. It does not require
literal duplication, and the Phase 1 baseline does not require every stateful,
automated, cross-border, or provider-dependent upstream workflow to be implemented
before the baseline can freeze.

## Phase Model

| Phase | Scope | Examples |
|---|---|---|
| Phase 1 Baseline Recovery | China-law substantive alignment, root discoverability, static/local use, mandatory runtime validation, truthful documentation | Core legal reviews, local file mode, command routing, CI, MCP placeholder configuration |
| Phase 1.5 Legal Workflow Layer | Local, human-triggered persistence and lifecycle behavior | Matter workspaces, trackers, history, owner/status/deadline, local monitoring queues |
| Phase 2 Advanced Integration / External Capability | External providers, automatic monitoring, privileged ecosystem actions, and specialized cross-border expansion | Real MCP providers, WPS API, enterprise systems, outbound employment packs, skill install/update/rollback |

Phase assignment is not a value ranking. Law firm, in-house, clinic, student,
regulatory, and governance modules remain subject to the same Phase 1 quality bar
for the capabilities actually included in the baseline.

## Phase 1 Non-Goals

Phase 1 does not include:

- stateful matter-workspace implementation or automatic lifecycle management;
- automatic monitoring of product, contract, docket, registry, or enterprise systems;
- physical installation, update, rollback, disable, or uninstall of community skills;
- substantive foreign-law, EOR, foreign tax, or immigration advice for international expansion;
- production MCP providers for commercial legal databases, WPS, court systems, OCR, company search, or enforcement intelligence;
- specialized Practice Packs beyond the Phase 1 China-law baseline;
- an architecture rewrite whose main purpose is optimization.

The repository may preserve compatibility commands, planning templates, placeholder
connector interfaces, and the local sample `legal-data` server. Each must state its
actual operating boundary.

## Provider Boundary

PKULAW, Yuandian, Wolters Kluwer, Faxin, Alpha, court systems, WPS, OCR,
company search, judgment search, enforcement intelligence, business registries,
and enterprise systems are not production-integrated by the Phase 1 repository.
Deployments may connect authorized providers later without changing the Phase 1
legal-substance baseline.

## Acceptance Rule

Phase 1 is ready for Release Candidate review only when:

1. all Phase 1 Mandatory issues pass validation;
2. current paths, module counts, command names, and capability states are documented accurately;
3. `docs/UPSTREAM_MAPPING_MATRIX.md` records each deferred responsibility and target phase;
4. Phase 1.5 and Phase 2 items are not treated as Phase 1 blockers and are not claimed as implemented;
5. external/vendor content remains isolated from the default China marketplace.
