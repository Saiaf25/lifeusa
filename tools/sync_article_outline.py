#!/usr/bin/env python3
"""Sync LifeUSA article outline HTML from vault handoff to GitHub Pages.

This prevents the handoff HTML and shareable GitHub Pages URL from drifting.
Run from the repository root:

    python3 tools/sync_article_outline.py

The script copies the source handoff HTML to the live article URL, applies
client-facing sanitization, and validates that required sections are present.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class OutlinePage:
    name: str
    source: Path
    live: Path
    required_text: tuple[str, ...]


ROOT = Path(__file__).resolve().parents[1]

PAGES = (
    OutlinePage(
        name="how-to-help-orphans",
        source=Path("Content Framework/70-outputs/handoff/orphans/how-to-help-orphans-brief-outline.html"),
        live=Path("article-plans-and-outlines/how-to-help-orphans/index.html"),
        required_text=("Why Do Orphans Need Help?",),
    ),
)

FORBIDDEN_CLIENT_TEXT = (
    "Adversarial Review",
    'id="adversarial-review"',
    'href="#adversarial-review"',
)

INTERNAL_SECTION_IDS = (
    "adversarial-review",
)


def add_noindex(html: str) -> str:
    if 'name="robots" content="noindex"' in html:
        return html
    viewport = '<meta name="viewport" content="width=device-width, initial-scale=1">'
    return html.replace(viewport, viewport + '\n  <meta name="robots" content="noindex">', 1)


def remove_internal_sections(html: str) -> str:
    for section_id in INTERNAL_SECTION_IDS:
        html = re.sub(
            rf'\n\s*<section id="{re.escape(section_id)}">.*?\n\s*</section>\n',
            "\n",
            html,
            flags=re.DOTALL,
        )
        html = re.sub(
            rf'\n\s*<a href="#{re.escape(section_id)}">.*?</a>',
            "",
            html,
            flags=re.DOTALL,
        )
    return html


def validate(page: OutlinePage, html: str) -> list[str]:
    errors: list[str] = []
    for text in page.required_text:
        if text not in html:
            errors.append(f"{page.live}: missing required text: {text}")
    for text in FORBIDDEN_CLIENT_TEXT:
        if text in html:
            errors.append(f"{page.live}: forbidden client-facing text remains: {text}")
    if 'name="robots" content="noindex"' not in html:
        errors.append(f"{page.live}: missing noindex tag")
    return errors


def sync_page(page: OutlinePage) -> list[str]:
    source = ROOT / page.source
    live = ROOT / page.live
    if not source.exists():
        return [f"{page.source}: source file not found"]

    html = source.read_text(encoding="utf-8")
    html = remove_internal_sections(html)
    html = add_noindex(html)

    errors = validate(page, html)
    if errors:
        return errors

    live.parent.mkdir(parents=True, exist_ok=True)
    old = live.read_text(encoding="utf-8") if live.exists() else None
    if old != html:
        live.write_text(html, encoding="utf-8")
        print(f"synced: {page.source} -> {page.live}")
    else:
        print(f"ok: {page.live} already current")
    return []


def main() -> int:
    errors: list[str] = []
    for page in PAGES:
        errors.extend(sync_page(page))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
