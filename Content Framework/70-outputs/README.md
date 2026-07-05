# 70. Outputs

This folder holds operational outputs from the LifeUSA content pipeline.

## Structure

```text
70-outputs/
├── README.md
├── briefs/
├── outlines/
├── drafts/
└── handoff/
```

## Lifecycle

| Stage | Folder |
|---|---|
| Brief | `briefs/{cluster}/{slug}.md` |
| Outline | `outlines/{cluster}/{slug}.md` |
| Draft | `drafts/{cluster}/{slug}.md` |
| Final handoff | `handoff/{cluster}/{slug}.md` |

## Rewind rule

If a draft fails final review, return to the exact failed stage:

- Intent or duplicate problem: rewrite the brief.
- Bad structure: rewrite the outline.
- Unsupported claims: rewrite or source the draft.
- CTA or link problem: redo LifeUSA mention or internal links.
- Metadata problem: redo metadata only.

## Active orphan-cluster outputs

| Topic | Brief | Outline | Handoff | Live preview | Status |
|---|---|---|---|---|---|
| What Is an Orphan? Causes, Statistics, and How You Can Help | `briefs/orphans/what-is-an-orphan-causes-statistics-how-you-can-help.md` | `outlines/orphans/what-is-an-orphan-causes-statistics-how-you-can-help.md` | `handoff/orphans/what-is-an-orphan-causes-statistics-how-you-can-help.html` | `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-is-an-orphan-causes-statistics-how-you-can-help/` | Published live at `https://www.lifeusa.org/post/what-is-an-orphan`; Angela/Hany notified in Zoho on 2026-07-05 |
| How To Help Orphans | `briefs/orphans/how-to-help-orphans.md` | `outlines/orphans/how-to-help-orphans.md` | `handoff/orphans/how-to-help-orphans-brief-outline.html` | `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/how-to-help-orphans/` | Delivered to Angela/team; writer draft pending |
| Can Zakat Be Used To Sponsor an Orphan? | `briefs/orphans/can-zakat-be-used-to-sponsor-an-orphan.md` | `outlines/orphans/can-zakat-be-used-to-sponsor-an-orphan.md` | `handoff/orphans/can-zakat-be-used-to-sponsor-an-orphan.html` | `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/can-zakat-be-used-to-sponsor-an-orphan/` | Delivered to Angela/team; writer draft pending |
| What Does Orphan Sponsorship Cover? | `briefs/orphans/what-does-orphan-sponsorship-cover.md` | `outlines/orphans/what-does-orphan-sponsorship-cover.md` | `handoff/orphans/what-does-orphan-sponsorship-cover.html` | `https://saiaf25.github.io/lifeusa/article-plans-and-outlines/what-does-orphan-sponsorship-cover/` | Prepared and shared via user-confirmed scheduled Angela email for ~2026-07-05 05:53 Türkiye time; writer draft pending |
| Gaza Orphans: How War Leaves Children Without Care, Safety, and Support | `briefs/orphans/gaza-orphans-war-care-safety-support.md` | `outlines/orphans/gaza-orphans-war-care-safety-support.md` | `handoff/orphans/gaza-orphans-war-care-safety-support.html` | `article-plans-and-outlines/gaza-orphans-war-care-safety-support/` | Saiaf-owned enrichment plan for existing Gaza orphan article; not Angela-owned |
| Why Gifts for Orphans Matter: Joy, Dignity, and the Right to Childhood | `briefs/orphans/why-gifts-for-orphans-matter.md` | `outlines/orphans/why-gifts-for-orphans-matter.md` | `handoff/orphans/why-gifts-for-orphans-matter.html` | `article-plans-and-outlines/why-gifts-for-orphans-matter/` | Saiaf-owned enrichment plan for existing gift article; not a generic gift list |
| Orphan Education After Loss: Why School Stability Matters | `briefs/orphans/orphan-education-after-loss.md` | `outlines/orphans/orphan-education-after-loss.md` | `handoff/orphans/orphan-education-after-loss.html` | `article-plans-and-outlines/orphan-education-after-loss/` | Saiaf-owned new informational guide focused on school continuity |
| Mental Health Support for Orphaned Children | `briefs/orphans/mental-health-support-for-orphaned-children.md` | `outlines/orphans/mental-health-support-for-orphaned-children.md` | `handoff/orphans/mental-health-support-for-orphaned-children.html` | `article-plans-and-outlines/mental-health-support-for-orphaned-children/` | Saiaf-owned new informational guide with non-clinical psychosocial-support framing |

## What goes here

- Content briefs
- Content outlines
- Article drafts
- Metadata and schema sidecars
- Wix or client handoff files

## What does not go here

- Framework strategy
- Source corpus
- Raw exports
- Invoices
- Client communications
- Finished HTML deliverables unless explicitly tied to a content handoff
