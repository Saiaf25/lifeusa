# Article Plans and Outlines

This folder contains shareable GitHub Pages previews for LifeUSA article briefs and outlines.

Do not edit live preview HTML manually unless the matching source handoff file is updated too.

## Publishing Rule

The index source is:

```text
Content Framework/70-outputs/handoff/article-plans-and-outlines-index.html
```

The live index is:

```text
article-plans-and-outlines/index.html
```

For the orphan pillar outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/how-to-help-orphans-brief-outline.html
```

The live preview is:

```text
article-plans-and-outlines/how-to-help-orphans/index.html
```

For the orphan definition rewrite outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/what-is-an-orphan-causes-statistics-how-you-can-help.html
```

The live preview is:

```text
article-plans-and-outlines/what-is-an-orphan-causes-statistics-how-you-can-help/index.html
```

For the orphan sponsorship coverage outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/what-does-orphan-sponsorship-cover.html
```

The live preview is:

```text
article-plans-and-outlines/what-does-orphan-sponsorship-cover/index.html
```

For the Gaza orphans enrichment outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/gaza-orphans-war-care-safety-support.html
```

The live preview is:

```text
article-plans-and-outlines/gaza-orphans-war-care-safety-support/index.html
```

For the gifts for orphans enrichment outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/why-gifts-for-orphans-matter.html
```

The live preview is:

```text
article-plans-and-outlines/why-gifts-for-orphans-matter/index.html
```

For the orphan education guide outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/orphan-education-after-loss.html
```

The live preview is:

```text
article-plans-and-outlines/orphan-education-after-loss/index.html
```

For the orphan mental-health support guide outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/mental-health-support-for-orphaned-children.html
```

The live preview is:

```text
article-plans-and-outlines/mental-health-support-for-orphaned-children/index.html
```

For the zakat and orphan sponsorship outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/can-zakat-be-used-to-sponsor-an-orphan.html
```

The live preview is:

```text
article-plans-and-outlines/can-zakat-be-used-to-sponsor-an-orphan/index.html
```

For the charitable-giving cluster hub outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/giving/why-donate-to-charity-benefits-of-giving.html
```

The live preview is:

```text
article-plans-and-outlines/why-donate-to-charity-benefits-of-giving/index.html
```

This is the hub of the U.S. charitable giving cluster and the first outline outside the orphan cluster. Its keyword source is the `LifeUSA USA Charitable Giving Keyword Cluster - 2026-07-28` sheet, whose local build lives at:

```text
outputs/019fa866-9acf-74f0-8379-305525f38efa/LifeUSA-USA-Charitable-Giving-Keyword-Cluster-2026-07-28.xlsx
```

The `Topic Gaps` tab in that workbook was added 2026-08-07 and records the cluster expansion from 5 owned pages to 10, grounded in the Google Ads pull stored at `Content Framework/80-Keywords/giving-cluster-gaps-2026-08-07/`. The Google Drive copy of that sheet is a separate file and does not update automatically; re-upload the local workbook when the tab needs to reach the client.

The educational outline-template source is:

```text
Content Framework/70-outputs/handoff/article-outline-template.html
```

The live template preview is:

```text
article-plans-and-outlines/article-outline-template/index.html
```

## Songs for Gaza UI review page

The client-facing comparison page is:

```text
article-plans-and-outlines/songs-for-gaza-ui-approaches/index.html
```

Its design-record source is:

```text
prototypes/songs-for-gaza-landing-page/
```

The public noindex review URL is:

```text
https://saiaf25.github.io/lifeusa/article-plans-and-outlines/songs-for-gaza-ui-approaches/?variant=A
```

The A/B/C query state switches among the documentary title card, split-screen film poster, and theatre premiere directions while keeping all three approaches under one client-review slug. This page is a design-review artifact, not the production LifeUSA landing page. The user confirmed the page and worldwide English keyword sheet were emailed to Dr. Hany Saqr and Angela Joyce on 2026-08-04; client selection is pending.

After editing the source file, run:

```bash
python3 tools/sync_article_outline.py
```

Then commit both files together.

The sync script:

- copies the source handoff HTML to the live GitHub Pages path;
- keeps the live page `noindex`;
- removes internal-only review sections from the client-facing page;
- fails if required client-facing sections are missing.
