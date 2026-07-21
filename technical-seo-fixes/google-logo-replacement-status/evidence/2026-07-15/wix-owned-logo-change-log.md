# LifeUSA Wix owned-logo change log

Executed and verified July 15, 2026.

## Change performed

The verified current 1800 by 1800 LifeUSA square logo was uploaded directly to the published `Life USA` Wix site and assigned to the site's Business Profile logo field.

| Field | Before | After |
|---|---|---|
| Wix Business Profile `logo` | Empty | `af2a6c_49a4190c354746b493c123d311222fb5~mv2.png` |
| Site Properties version | `41` | `42` |
| Public asset URL | Not assigned | `https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png` |

The asset URL was opened directly after upload and returned the intended 1800 by 1800 current square mark.

## Canonical horizontal upload

The approved 4101 by 1201 horizontal website logo was also uploaded to the same LifeUSA Wix Media Manager.

| Verification field | Result |
|---|---|
| Wix media ID | `af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png` |
| Public asset URL | `https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png` |
| Remote state | Ready; HTTP `200`; `image/png` |
| Dimensions | 4101 by 1201 |
| Local SHA-256 | `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` |
| Remote SHA-256 | `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` |

The identical checksums confirm that the live Wix asset is a byte-for-byte copy of the approved horizontal source. Together with the verified square file, this completes the canonical two-file asset kit.

## Fields preserved

- Site display name: `Life USA`
- Business name: `Life for Relief and Development`
- Business description: unchanged

The update used a field mask containing only `logo`, so no other Business Profile field was intentionally changed.

## Post-change homepage check

The live homepage was reloaded after the Business Profile update. Its existing custom `NGO` JSON-LD still references:

`https://static.wixstatic.com/media/6df904_2bb6857d9c8b49ae91789ad75efbc8b8~mv2.png`

This confirms the custom homepage structured data is managed separately from the Wix Business Profile logo. The business-profile correction is complete, while replacement of `NGO.logo`, addition of `@id` and `sameAs`, and duplicate `WebSite` cleanup remain active under LOGO-005.

The remaining homepage JSON-LD, visible header, favicon, and public brand-page changes require an approved Wix editor session. No supported Wix REST route was found for those specific existing-page edits.

## July 20 homepage NGO repair

The user explicitly approved `APR-007` and manually published the prepared homepage NGO markup. Public rendered-source verification confirmed that the live NGO node now uses the canonical colored 1800 by 1800 square, stable `@id`, `alternateName`, verified `sameAs`, address, and contact point. The former white-logo URL is absent from the fetched homepage HTML.

`LOGO-005` is complete. Two `WebSite` nodes remain, so duplicate-node cleanup and the other unverified APR-007 placements remain open. See [LOGO-005 live verification](../2026-07-20/logo-005-live-verification.md).

## July 20 brand-resources page publication

The user published `https://www.lifeusa.org/brand-resources`. Logged-out verification returned `200` and confirmed that the heading, introductory copy, and two-logo gallery are native Wix content.

The first check found an exact approved 1800 by 1800 square and a derived 3000 by 879 horizontal JPG. A second cache-busted check proved that the horizontal placement was replaced with the approved 4101 by 1201 canonical PNG. The square has descriptive alt text; the horizontal title is visible, although its image alt field remains empty.

The project owner explicitly confirmed that direct download links are not required and accepted the current page as complete. `LOGO-004` is done. See [LOGO-004 brand-page live verification](../2026-07-20/logo-004-brand-page-live-verification.md).

## July 21 header, footer, favicon, and navigation verification

The user reported completing the remaining visible owned-site work. Logged-out verification of the cache-busted public homepage confirmed that the header and footer both use the approved current horizontal source and expose the descriptive alt text `Life for Relief and Development logo`. Direct-file comparison proved that their 4101 by 1201 source is byte-for-byte identical to the canonical horizontal master.

The live favicon points to a 1800 by 1800 Wix source that is byte-for-byte identical to the canonical square master. All compared direct files returned HTTP `200`.

The live About submenu contains `Brand Resources`, linked to the public page, which returned `200`.

`LOGO-006` is done. `APR-007` remains partially executed only because two homepage `WebSite` nodes still require consolidation. See [July 21 live verification](../2026-07-21/logo-006-and-navigation-verification.md).
