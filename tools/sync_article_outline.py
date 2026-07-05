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
        name="article-plans-and-outlines-index",
        source=Path("Content Framework/70-outputs/handoff/article-plans-and-outlines-index.html"),
        live=Path("article-plans-and-outlines/index.html"),
        required_text=(
            "LifeUSA Article Plans and Outlines",
            "LifeUSA Article Outline Template",
            "10 Ways To Help Orphans",
            "Can Zakat Be Used To Sponsor an Orphan?",
            "Do not publish as a new standalone article",
            "What Is an Orphan? Causes, Statistics, and How You Can Help",
            "What Does Orphan Sponsorship Cover? A Guide for Donors",
            "Gaza Orphans: How War Leaves Children Without Care, Safety, and Support",
            "Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood",
            "Orphan Education After Loss: Why School Stability Matters",
            "Mental Health Support for Orphaned Children: Routine, Safety, and Care After Trauma",
        ),
    ),
    OutlinePage(
        name="gaza-orphans-war-care-safety-support",
        source=Path("Content Framework/70-outputs/handoff/orphans/gaza-orphans-war-care-safety-support.html"),
        live=Path("article-plans-and-outlines/gaza-orphans-war-care-safety-support/index.html"),
        required_text=(
            "Gaza Orphans: How War Leaves Children Without Care, Safety, and Support",
            "war orphans",
            "gaza orphans",
            "Owner: Saiaf",
        ),
    ),
    OutlinePage(
        name="why-gifts-for-orphans-matter",
        source=Path("Content Framework/70-outputs/handoff/orphans/why-gifts-for-orphans-matter.html"),
        live=Path("article-plans-and-outlines/why-gifts-for-orphans-matter/index.html"),
        required_text=(
            "Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood",
            "gifts for orphans",
            "eid gifts for orphans",
            "Owner: Saiaf",
        ),
    ),
    OutlinePage(
        name="orphan-education-after-loss",
        source=Path("Content Framework/70-outputs/handoff/orphans/orphan-education-after-loss.html"),
        live=Path("article-plans-and-outlines/orphan-education-after-loss/index.html"),
        required_text=(
            "Orphan Education After Loss: Why School Stability Matters",
            "orphan education",
            "school continuity",
            "Writer: Angela",
        ),
    ),
    OutlinePage(
        name="mental-health-support-for-orphaned-children",
        source=Path("Content Framework/70-outputs/handoff/orphans/mental-health-support-for-orphaned-children.html"),
        live=Path("article-plans-and-outlines/mental-health-support-for-orphaned-children/index.html"),
        required_text=(
            "Mental Health Support for Orphaned Children: Routine, Safety, and Care After Trauma",
            "orphan mental health",
            "non-clinical",
            "Writer: Angela",
        ),
    ),
    OutlinePage(
        name="what-does-orphan-sponsorship-cover",
        source=Path("Content Framework/70-outputs/handoff/orphans/what-does-orphan-sponsorship-cover.html"),
        live=Path("article-plans-and-outlines/what-does-orphan-sponsorship-cover/index.html"),
        required_text=(
            "What Does Orphan Sponsorship Cover?",
            "orphans sponsorship",
            "Do not overpromise",
        ),
    ),
    OutlinePage(
        name="technical-seo-fixes-index",
        source=Path("Content Framework/70-outputs/handoff/technical-seo-fixes-index.html"),
        live=Path("technical-seo-fixes/index.html"),
        required_text=(
            "LifeUSA Technical SEO Fixes",
            "Old orphan article slug redirects to the new evergreen guide",
            "Blog article body spacing and link styling fixed through Wix Custom Code",
            "Robots.txt cleanup published through Wix SEO tools",
            "Copy-of gallery URL cleanup is mapped but waiting for client exception review",
        ),
    ),
    OutlinePage(
        name="what-is-an-orphan-causes-statistics-how-you-can-help",
        source=Path("Content Framework/70-outputs/handoff/orphans/what-is-an-orphan-causes-statistics-how-you-can-help.html"),
        live=Path("article-plans-and-outlines/what-is-an-orphan-causes-statistics-how-you-can-help/index.html"),
        required_text=("What Is an Orphan?", "Causes, Statistics, and How You Can Help"),
    ),
    OutlinePage(
        name="how-to-help-orphans",
        source=Path("Content Framework/70-outputs/handoff/orphans/how-to-help-orphans-brief-outline.html"),
        live=Path("article-plans-and-outlines/how-to-help-orphans/index.html"),
        required_text=("Why Do Orphans Need Help?",),
    ),
    OutlinePage(
        name="can-zakat-be-used-to-sponsor-an-orphan",
        source=Path("Content Framework/70-outputs/handoff/orphans/can-zakat-be-used-to-sponsor-an-orphan.html"),
        live=Path("article-plans-and-outlines/can-zakat-be-used-to-sponsor-an-orphan/index.html"),
        required_text=(
            "Can Zakat Be Used To Sponsor an Orphan?",
            "Policy caution",
            "Do not publish this as a new standalone article",
            "LIFE positioned as a relief organization",
        ),
    ),
    OutlinePage(
        name="article-outline-template",
        source=Path("Content Framework/70-outputs/handoff/article-outline-template.html"),
        live=Path("article-plans-and-outlines/article-outline-template/index.html"),
        required_text=("LifeUSA Article Outline Template", "SERP And Competition", "Information Gain"),
    ),
)

FORBIDDEN_CLIENT_TEXT = (
    "Adversarial Review",
    "Technical Appendix",
    "Ahrefs returned no populated SERP rows",
    "<strong>Do not use:</strong>",
    'id="adversarial-review"',
    'href="#adversarial-review"',
    'href="#appendix"',
)

INTERNAL_SECTION_IDS = (
    "adversarial-review",
    "appendix",
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
