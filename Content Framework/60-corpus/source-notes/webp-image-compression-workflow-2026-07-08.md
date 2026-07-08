# WebP Image Compression Workflow - 2026-07-08

## Source Trigger

Angela Joyce replied in the live Zoho `LifeUSA | Article Planning and Publishing | Ongoing Thread` asking for the image-compression program previously mentioned for reducing images at scale.

- Zoho account checked: `hello@saiaf.me`
- Account ID: `8911414000000002002`
- Relevant thread ID: `1782503110923013500`
- Relevant message ID: `1783386610791014000`
- Angela's ask: she implemented the agreed blog keywords, phrases, and internal links; the only open item was reducing images under the size target at scale.

## Published Resource

Primary technical resource:

https://saiaf25.github.io/lifeusa/technical-seo-fixes/windows-image-compression-workflow/

Technical index:

https://saiaf25.github.io/lifeusa/technical-seo-fixes/

Canonical local source:

`technical-seo-fixes/windows-image-compression-workflow/index.html`

Source handoff for the technical index:

`Content Framework/70-outputs/handoff/technical-seo-fixes-index.html`

## Final Script Constraint

The final page must give beginners one path and one script, not multiple alternatives.

The batch-file structure should stay close to the tested script:

- `set output_folder="output"`
- create `output` folder if missing
- loop over `*.png *.jpg *.jpeg *.bmp *.tiff *.gif`
- write WebP files to `%output_folder%\%%~nf.webp`
- keep image dimensions unchanged

The only functional ImageMagick addition for file-size control is:

```bat
-define webp:target-size=80000 -define webp:method=6
```

Do not add unrequested flags such as:

- `-resize`
- `-strip`
- `-auto-orient`

Reason: the user explicitly asked to control KB/MB file size, not image dimensions or orientation/metadata.

## Verification

Local ImageMagick syntax test on 2026-07-08:

- Input: `1600x1000`, `626900B`
- Output: `1600x1000`, `76358B`
- Command used the same `webp:target-size=80000` and `webp:method=6` parameters.

Public GitHub Pages verification after commit `91633b2` confirmed:

- live page contained `target-size=80000`
- live page did not contain `resize`, `strip`, or `auto-orient`
- live page retained copy buttons for code blocks

Later commit `3bf39ac` removed internal/meta copy from the client-facing page.

## Angela Reply Framing

Use this framing for the reply:

1. Recommend the local Windows workflow first because it is repeatable for weekly blog image batches.
2. Present TinyPNG and Squoosh as backup browser-based options for one-off work.
3. Keep the wording practical and non-technical; Angela does not need internal implementation notes or apology/explanation text.

Draft saved in:

`Content Framework/70-outputs/emails/lifeusa-angela-image-compression-options-draft-2026-07-08.md`

## Open Status

- Reply not sent from Zoho during this vault update.
- If sent later, verify the sent message in Zoho and update this note plus the changelog.
