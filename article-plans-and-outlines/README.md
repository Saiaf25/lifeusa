# Article Plans and Outlines

This folder contains shareable GitHub Pages previews for LifeUSA article briefs and outlines.

Do not edit live preview HTML manually unless the matching source handoff file is updated too.

## Publishing Rule

For the orphan pillar outline, the source of truth is:

```text
Content Framework/70-outputs/handoff/orphans/how-to-help-orphans-brief-outline.html
```

The live preview is:

```text
article-plans-and-outlines/how-to-help-orphans/index.html
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

