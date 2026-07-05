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

The educational outline-template source is:

```text
Content Framework/70-outputs/handoff/article-outline-template.html
```

The live template preview is:

```text
article-plans-and-outlines/article-outline-template/index.html
```

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
