#!/usr/bin/env python3
"""Generate the eight category pages from the curated JSON catalog (stdlib only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {
    "foundations": (
        "FOUNDATIONS.md", "Governance foundations",
        "Start with the frameworks and institutional references that define governance responsibilities, risk management, and accountability. Read each source in its own jurisdiction and scope.",
    ),
    "agentic": (
        "AGENTIC.md", "Agentic AI governance",
        "Govern systems that can plan, use tools, delegate work, and take actions. Focus on delegated authority, meaningful oversight, approval boundaries, and evidence.",
    ),
    "security": (
        "SECURITY.md", "AI and agent security",
        "Use these references to identify threats, design controls, test assumptions, and translate security findings into governance decisions.",
    ),
    "tools": (
        "TOOLS.md", "Projects and practical tools",
        "Use these projects to organize governance work or generate evidence through inspection, testing, and evaluation. A tool's output still needs interpretation; installation alone does not establish compliance.",
    ),
    "research": (
        "RESEARCH.md", "Essential research and evidence",
        "Read the research that helps explain what governance needs to measure and prove. Distinguish empirical findings from proposals, benchmarks, and the authors' interpretations.",
    ),
    "learning": (
        "LEARNING.md", "Courses, videos, and podcasts",
        "Learn from substantial courses, recorded talks, and focused conversations. Choose by the task you need to perform, then return to the primary references for exact requirements.",
    ),
    "books": (
        "BOOKS.md", "Books worth reading",
        "Longer treatments for readers who need sustained context on accountability, institutions, and the limits of AI. Access labels describe the linked edition or source.",
    ),
    "updates": (
        "UPDATES.md", "Sources to follow",
        "Follow a small set of primary sources for material changes. Publication feeds are ongoing references, not endorsements of every item they publish.",
    ),
}


def escape_label(value: str) -> str:
    return value.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def render_category(category: str, resources: list[dict]) -> str:
    _, title, intro = CATEGORIES[category]
    entries = [item for item in resources if item["category"] == category]
    lines = [
        f"# {title}", "", "[← Resource hub](../README.md) · [Start here](START-HERE.md)", "",
        intro, "",
        f"**{len(entries)} selected resources**", "",
    ]
    lines.extend(f'- [{escape_label(item["title"])}](#{item["id"]})' for item in entries)
    lines.append("")
    for item in entries:
        lines.extend([
            f'<a id="{item["id"]}"></a>', "", f'### [{escape_label(item["title"])}](<{item["url"]}>)', "",
            f'**Publisher:** {item["publisher"]}  ',
            f'**Format:** {item["format"]} · **Access:** {item["access"]}  ',
            f'**For:** {item["audience"]}', "",
            f'**Why it matters:** {item["why"]}', "",
            f'**Put it into practice:** {item["use"]}', "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root")
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    args = parser.parse_args()
    catalog = json.loads((args.root / "catalog/resources.json").read_text(encoding="utf-8"))
    changed = []
    for category, (filename, _, _) in CATEGORIES.items():
        path = args.root / "docs" / filename
        expected = render_category(category, catalog["resources"])
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != expected:
            changed.append(f"docs/{filename}")
            if not args.check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8")
    if args.check and changed:
        print("Generated pages are out of date: " + ", ".join(changed))
        print("Run: python scripts/generate_catalog.py")
        return 1
    print(f"Category pages {'verified' if args.check else 'generated'}: {len(CATEGORIES)} pages; {len(changed)} changed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
