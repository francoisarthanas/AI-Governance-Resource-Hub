# Contributing

Help keep this hub focused on resources that support useful AI governance decisions and practical work.

## What belongs here

- **Practical value:** Identify the decision, skill, evidence, or work product the resource supports.
- **Credible source:** Prefer the original regulator, standards body, research team, project maintainer, publisher, or speaker.
- **Distinct contribution:** Explain what it adds beyond the collection. Replace a weaker or superseded resource when appropriate.
- **Relevant scope:** Focus on governance, accountability, oversight, risk management, assurance, and agent security.
- **Clear access:** State costs, registration requirements, software licensing, and hosting or usage fees where applicable. Free documentation does not imply a free product.

Read the source before submitting. Check its title, publisher, destination, and access conditions. Distinguish drafts and proposals from adopted requirements, and identify jurisdiction where it affects the reader's use. Vendor resources can qualify when they offer a substantial method or usable project. Disclose commercial interests; avoid affiliate links, promotional lists, copied chapters, and confidential material.

## Suggest a resource or correction

[Open a suggestion or correction](https://github.com/francoisarthanas/AI-Governance-Resource-Hub/issues/new?template=resource.yml). For a new resource, include its primary URL, intended audience, practical value, and what it adds to the collection. For a correction, identify the link or description that needs to change. You can also submit a pull request.

## Update the catalog

1. Edit [catalog/resources.json](catalog/resources.json). Keep `schema_version` at `3.0`. Each resource requires these nonempty strings: `id`, `title`, `url`, `publisher`, `category`, `format`, `access`, `audience`, `why`, and `use`. The optional `starter` field is a boolean.
2. Use a stable lowercase, hyphenated `id` and one canonical HTTPS URL. Preserve existing IDs when updating resources so bookmarked links continue to work.
3. Choose one category: `foundations`, `agentic`, `security`, `tools`, `research`, `learning`, `books`, or `updates`.
4. Keep `why` and `use` concise: explain why the resource matters and what readers can accomplish with it. Update README counts and [Start here](docs/START-HERE.md) when the collection or starting selection changes.
5. Regenerate category pages, then run validation:

```bash
python scripts/generate_catalog.py
python scripts/generate_catalog.py --check
python scripts/validate.py
```

Commit the catalog and regenerated pages together. Edit the catalog rather than individual category pages. The checks use Python's standard library and validate required fields, unique IDs and URLs, category coverage, generated content, and internal links and anchors.

## Maintain the collection

Review the weekly link report and reassess the collection periodically for relevance, source changes, access, and overlap. Replace superseded resources with their primary successors unless the older work has a clear historical purpose. Remove resources that no longer offer distinctive value.

Run an external link check when needed:

```bash
python scripts/check_links.py --json reports/link-check.json --markdown reports/link-check.md
```

The command fails for HTTP 404 or 410 and flags other failures for review. Scheduled runs publish a report in GitHub Actions. A successful HTTP response confirms reachability only; restricted access and network errors require manual inspection.
