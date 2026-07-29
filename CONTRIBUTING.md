# Contributing

Corrections and high-signal additions are welcome. This repository is deliberately selective: more links do not automatically make it better.

## Curation policy

A resource must pass all of these tests:

1. **Authoritative owner.** Prefer laws, regulators, standards bodies, national institutes, established nonprofits, official specifications, or actively maintained open-source projects. Use vendor guidance only when it is concrete and reusable.
2. **Practitioner action.** State the decision, control, assessment, test, or evidence the reader should produce after using it.
3. **Material value.** It fills a real gap or is stronger than an existing entry. A generic principles page, thin marketing post, or duplicative list is insufficient.
4. **Current and traceable.** Link the canonical source, identify the publisher, label the version where material, and prefer maintained content.
5. **Transparent access.** Label paid, freemium, and mixed-access material. No affiliate or sponsored links.
6. **Safe claims.** Do not imply that a tool, mapping, certificate, or self-assessment proves safety or legal compliance.

Priority order:

1. official law, regulator, government, or standards source;
2. maintained multi-stakeholder or nonprofit practitioner resource;
3. maintained open-source implementation or testing tool;
4. unusually strong vendor engineering guidance, clearly labeled.

## Propose a resource

Open a resource issue or pull request. Include:

- canonical HTTPS URL, title, publisher, version/date, access model, and proposed tier;
- the concrete gap it fills;
- one sentence for **why it matters** and one for **what to do with it**;
- maintenance evidence and known conflicts of interest;
- which existing resource it replaces or complements.

Add accepted resources to `catalog/resources.json` and, only where useful, the relevant narrative guide. Run:

```bash
python scripts/validate.py
python scripts/check_links.py
```

## Propose a control or template change

Explain the failure mode, decision, or evidence gap. Keep control objectives technology-neutral. Mark organization-, sector-, and jurisdiction-specific requirements explicitly. Template changes should reduce ambiguity or produce better evidence; adding fields without a clear user is not enough.

## Review and maintenance

- Broken or superseded links: correct immediately; use an authoritative successor where possible.
- Material versions: update the catalog and affected guide, then change `last_verified`.
- Routine review: quarterly for essential resources; at least annually for the full catalog.
- Regulatory content: confirm against official sources and qualified counsel.
- Open-source tools: reassess maintenance, ownership, security posture, and fit before continued recommendation.

By contributing, you agree that your contribution is licensed under this repository's [CC BY 4.0 license](LICENSE). Do not submit confidential, personal, proprietary, or restricted information.

