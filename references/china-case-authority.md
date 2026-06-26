# China Case Authority Layer

This file defines how `claude-for-legal-cn` should use guiding cases, reference cases, typical cases, gazette cases, and ordinary judgments in China Mainland legal workflows.

## Purpose

China is a statute-centered legal system. Cases improve judgment accuracy, but they must not be treated as common-law precedent.

Use cases to:

- identify adjudication rules and judicial reasoning patterns;
- compare similar facts and distinguish different facts;
- calibrate burden of proof, remedy risk, damages, procedure, and local court practice;
- reduce hallucinated legal conclusions where statutes are open-textured.

Do not use cases to:

- override statutes, administrative regulations, judicial interpretations, or valid mandatory rules;
- claim binding precedent in the common-law sense;
- invent case numbers, holding text, or court reasoning;
- present ordinary judgments as universal national rules.

## Authority Tiers

| Tier | Source type | Use |
|---|---|---|
| A | Laws, administrative regulations, judicial interpretations | Direct normative basis |
| B | Guiding cases released by the Supreme People's Court | Strong adjudication reference for similar disputes |
| C | People's Court Case Library reference cases | Similar-case reference, rule extraction, reasoning calibration |
| D | Gazette cases, typical cases, regulator/court selected cases | Supplementary practice reference, especially for emerging issues |
| E | Ordinary public judgments | Trend and sample only; never universalize without corroboration |

## Required Output Fields

When a skill uses cases, include:

```markdown
## Case Authority Check

Statutory basis:
- [law / article / paragraph]

Guiding cases / reference cases:
- [case name, source, case number if available, authority tier]

Similarity:
- [facts that match]

Distinctions:
- [facts that differ]

Usability:
- [strong / medium / weak / not comparable]

Warning:
- China Mainland cases are references for reasoning and similar-case review. They are not common-law precedent and do not replace statutes or judicial interpretations.
```

## Trigger Gate

Run a case authority check when any of the following appears:

- litigation, arbitration, enforcement, preservation, jurisdiction, limitation, evidence, or damages risk;
- labor dismissal, employee handbook validity, social insurance, non-compete, or wage-hour dispute;
- corporate governance, capital contribution, shareholder liability, equity transfer, or M&A dispute;
- contract validity, seal/legal representative authority, liquidated damages adjustment, standard terms, or electronic signature dispute;
- IP infringement, platform takedown, unfair competition, trade secret, or patent/trademark validity dispute;
- consumer/product/advertising/platform enforcement risk;
- privacy/data/AI governance issues where judicial or regulatory cases clarify standards;
- local court practice, conflicting interpretations, or high-stakes risk scoring.

## Citation Rules

Every case citation must state:

- source platform;
- case category: guiding case, reference case, typical case, gazette case, ordinary judgment;
- court or issuing body;
- case name and case number if available;
- retrieval date or update timestamp;
- whether the text was retrieved from a connector, user upload, or manual research.

If the case text is unavailable, write `[case text not retrieved - verify]` and do not summarize the holding as fact.

## Update Interface

Case law changes over time. Skills must read the newest available case source through `references/case-authority-sources.json` or a configured MCP connector.

Update policy:

- guiding cases: check monthly;
- People's Court Case Library reference cases: check weekly for active modules and monthly for inactive modules;
- typical cases and regulator/court selected cases: check monthly;
- ordinary judgments: check only when a matter requires similar-case research.

Freshness tags:

| Tag | Meaning |
|---|---|
| `[case-current]` | Retrieved through a connected source during the current session |
| `[case-cache]` | Retrieved from local cache or stored reference; verify before relying |
| `[case-stale]` | Older than the configured freshness window |
| `[case-missing]` | No case source connected or no comparable case found |

## Fallback

If no connector is available:

1. Ask the user to upload case search results or relevant judgments.
2. Use statutory and judicial-interpretation analysis as the main answer.
3. Add: `No live case authority source is connected. Similar-case conclusions are incomplete and should be checked against the People's Court Case Library or another authoritative database.`

