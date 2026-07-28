# LifeUSA mobile viewport responsiveness fix

Status: **confirmed live, remediation pending**

Severity: **critical / sitewide**

First confirmed: **2026-07-28**

## Executive finding

LifeUSA is not serving a responsive mobile layout. For mobile user agents, Wix sends:

```html
<meta name="viewport" content="width=980, user-scalable=yes" id="wixMobileViewport">
```

This forces a phone to render the 980 px desktop canvas and shrink it to fit. On the tested 390 px iPhone viewport, the scale was `0.397959`, or approximately **39.8%**. The site therefore appears as a miniature desktop page: the full desktop header and navigation remain, text and controls are too small, and multi-column content does not reflow for touch screens.

This is not a single overflowing component. The fixed desktop canvas is applied to the shared Wix site root, header, page container, sections, and page background.

## Confirmed scope

The same forced 980 px mobile viewport was found on three representative page types:

| Page type | URL | Mobile viewport response | Result |
|---|---|---:|---|
| Homepage | `https://www.lifeusa.org/` | `width=980, user-scalable=yes` | Failed |
| Standard page | `https://www.lifeusa.org/about` | `width=980, user-scalable=yes` | Failed |
| Wix Blog post | `https://www.lifeusa.org/post/orphan-education-after-loss-why-school-stability-matters` | `width=980, user-scalable=yes` | Failed |

The server returned the same `width=980` mobile viewport for both iPhone and Android mobile user agents. A desktop user agent received the expected `width=device-width, initial-scale=1`.

## Root-cause assessment

**High-confidence diagnosis:** Wix Editor's **Mobile Friendly** view is disabled.

The live runtime behavior matches Wix's documented disabled state exactly: the desktop version is displayed on mobile devices. The remaining authenticated check is to open the Wix Editor and confirm the toggle state before changing it.

Official Wix guidance:

- [About the mobile version of your Wix site](https://support.wix.com/en/article/wix-editor-about-the-mobile-version-of-your-site)
- [Troubleshooting layout issues on a Wix mobile site](https://support.wix.com/en/article/wix-editor-troubleshooting-layout-issues-on-your-mobile-site)

## Technical remediation

### Phase 1: restore Wix's mobile rendering

1. Open the current production site in Wix Editor.
2. Open **Settings** from the editor's top bar.
3. Open **Mobile Friendly**.
4. Confirm the toggle is currently disabled and record a screenshot.
5. Enable **Mobile Friendly**.
6. Close the dialog.
7. Switch to Wix's mobile editor. Do not publish immediately.

This setting change should replace the forced 980 px mobile viewport with a device-width mobile layout. It is the real repair for the sitewide root cause.

### Phase 2: repair the generated mobile layout

Review the generated mobile view before publication, starting with shared components:

1. Replace the desktop navigation bar with the Wix mobile menu.
2. Resize and reposition the logo, language selector, account action, donation action, search, and social icons.
3. Check the sticky header height and confirm it does not cover page content.
4. Reflow hero headings, counters, cards, image/text sections, galleries, forms, and footer columns into mobile-safe stacks.
5. Review Wix's **Hidden on Mobile** panel and restore any essential content or controls.
6. Correct overlaps, large gaps, elements outside mobile gridlines, clipped text, and touch targets smaller than 44 by 44 CSS px.
7. Check the Arabic view separately for RTL order, alignment, menu behavior, and clipping.

### Phase 3: publish and verify

Publish only after the unpublished mobile view passes the acceptance tests below. Test the public site again after publication with cache bypass.

## Acceptance tests

The fix is complete only when all of the following pass:

- Mobile HTML uses a device-width viewport, not `width=980`.
- At 320, 360, 375, 390, 412, and 430 CSS px, the page does not render as a scaled desktop canvas.
- `#site-root`, `#SITE_HEADER`, and `#PAGES_CONTAINER` match the device layout width instead of a fixed 980 px width.
- No unintended horizontal scrolling exists.
- Body text is readable without zooming.
- The mobile menu opens, closes, scrolls, and reaches every primary destination.
- Language, My Account, Donate Now, search, social, and form controls remain reachable and tappable.
- Homepage, About, Programs, Ways to Give, Blog listing, one Blog post, Donate flow entry, Privacy Policy, and Arabic homepage pass.
- Portrait and landscape layouts pass on iOS Safari and Android Chrome.
- Desktop at 1440 px remains visually unchanged.

## Rollback

If the generated mobile view has a release-blocking defect, do not publish it. If a published change must be reversed, restore the previous Wix site version. Disabling **Mobile Friendly** again is only an emergency rollback because it restores the confirmed nonresponsive desktop-on-mobile behavior.

## Rejected shortcut

Do not treat `overflow-x: hidden` as the fix. It can conceal clipped content but cannot make the fixed 980 px desktop layout responsive, restore readable sizing, create a mobile menu, or reflow sections.

## Evidence

- [Mobile iPhone screenshot](./evidence/2026-07-28/home-mobile-iphone-final-390x844.png)
- [Machine-readable measurements](./evidence/2026-07-28/runtime-measurements.json)
- [User-agent viewport response check](./evidence/2026-07-28/user-agent-viewport-check.txt)
