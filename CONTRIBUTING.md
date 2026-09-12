# Contributing

This is a selective working library for AI governance and agentic AI governance. Each addition must help a reader make a better decision or perform a concrete task. More links are not the objective.

## The must-have test

A proposed resource should pass all of these checks:

- **Practical value:** Explain the specific decision, skill, evidence, or work product it supports. “Useful overview” is not enough.
- **Authority:** Prefer the original standard setter, regulator, research team, project maintainer, publisher, or speaker. Link to the source rather than a repost or an SEO summary.
- **Distinct contribution:** Explain what it adds beyond the existing collection. Replace a weaker or superseded entry when the new source serves the same need.
- **Scope fit:** The source should materially support governance, accountability, oversight, risk management, assurance, or agent security. General AI hype, undifferentiated tool lists, and promotion alone do not qualify.
- **Honest access:** Describe the linked resource precisely: open content, paid standard/book, registration requirement, open source software, paid hosting, or usage costs. Free documentation does not mean a free product.
- **Reviewable claims:** Check the title, publisher, version/status, access conditions, and destination. Separate proposals and draft standards from adopted requirements; identify jurisdiction when relevant. Disclose restrictions and unresolved checks.

Vendor material can qualify when it contributes a distinct, substantial method or a usable project. Disclose affiliation, sponsorship, and commercial interests. Do not submit affiliate links, pay-to-list offers, copied chapters, or confidential material.

## Submit or update a resource

1. Edit [catalog/resources.json](catalog/resources.json). Use one canonical HTTPS URL and one category per resource; avoid fragment-only or trailing-slash duplicates. Prefer stable landing pages over session URLs and temporary downloads.
2. Supply every schema field: `id`, `title`, `url`, `publisher`, `category`, `format`, `access`, `audience`, `why`, `use`, `version`, `verification_note`, and `last_reviewed`. All are nonempty strings. `starter` is an optional boolean reserved for the small starting selection.
3. Choose one category: `foundations`, `agentic`, `security`, `tools`, `research`, `learning`, `books`, or `updates`. Use a stable lowercase hyphenated `id`; existing anchors may be bookmarked.
4. Keep descriptions concise. Say why the source earns a place and what the reader should do with it. Use `verification_note` to describe what was actually checked and any limitation. Record real review dates as `YYYY-MM-DD`; never advance them because a link checker ran.
5. Keep catalog `schema_version` at `2.0`. Update catalog `last_reviewed` to the latest substantive entry review date. If you change the starting selection, update [Start here](docs/START-HERE.md) and the README where needed.
6. Generate category pages and run the checks below. Commit both the catalog and generated pages. Do not hand-edit generated category pages.
7. In your pull request, identify the reader's use case, the strongest existing alternative, the primary evidence you checked, and any replacement or removal. A maintainer reviews the decision before merging.

```bash
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python scripts/validate.py
```

The checks use Python's standard library. The validator checks metadata, real dates, duplicate canonical URLs, category-page anchors, and relative Markdown file/anchor targets. It does not establish factual accuracy, legal applicability, or a resource's quality.

## Keep the collection useful

| Cadence | Review |
| --- | --- |
| Weekly | Inspect the scheduled external-link report. Review 404/410 responses, redirects, restrictions, and network failures before changing an entry. |
| Monthly | Recheck agentic guidance, security references, active tools, and any entry marked draft, preview, restricted, or unresolved. |
| Quarterly | Reassess the full collection: unique value, source authority, access, version, relevance, and the starting selection. Verify legal and standards status at the original source. |
| When a material change occurs | Review the affected source promptly after a new edition, finalization, withdrawal, acquisition, project archival, or material access change. |

Replace a superseded source with its current primary successor unless the older source has a clearly stated historical purpose. Remove sources that lose their distinctive value or cannot be responsibly described. Preserve useful context in the pull request and Git history. Do not pad the catalog to a target count.

For a manual reachability report:

```bash
python scripts/check_links.py --json reports/link-check.json --markdown reports/link-check.md
```

The command exits unsuccessfully for HTTP 404 or 410. Other HTTP failures, restrictions, and network errors are reported for review. Scheduled runs use `--report-only` and publish the report in the workflow summary; they do not create issues, send messages, edit dates, or remove entries. A 200 response checks reachability only. A 403 or 429 is unverified access, not a passed content review.
