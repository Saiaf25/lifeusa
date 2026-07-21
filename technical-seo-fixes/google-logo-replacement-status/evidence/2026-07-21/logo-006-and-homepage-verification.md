# LOGO-006 and homepage live verification

Verified July 21, 2026 against cache-busted, logged-out public pages and the direct Wix media URLs.

## Owned logo placements

| Placement | Live source | Dimensions | SHA-256 | Result |
|---|---|---:|---|---|
| Header logo | `6df904_1fd130d48c554b8c8109e6acd206c435~mv2.png` | 4101 by 1201 | `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` | Byte-for-byte identical to the approved canonical horizontal master |
| Footer logo | `6df904_1fd130d48c554b8c8109e6acd206c435~mv2.png` | 4101 by 1201 | `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` | Uses the same verified horizontal source as the header |
| Favicon source | `6df904_3ba0b63af7e945f0a92fbe9978934569~mv2.png` | 1800 by 1800 | `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb` | Byte-for-byte identical to the approved canonical square master |

All four direct files used for comparison returned HTTP `200`. The rendered header and footer images both expose the descriptive alternative text `Life for Relief and Development logo`.

## Homepage H1 correction

The cache-busted public homepage exposed exactly one `h1` element:

`Life for Relief and Development`

The heading was visible in the rendered accessibility tree. This verifies the duplicate-homepage-H1 correction as a technical and on-page SEO fix; it is not classified as a logo correction.

## Brand Resources navigation

The public homepage navigation contains `Brand Resources` in the expanded `About` submenu and resolves it to:

`https://www.lifeusa.org/brand-resources`

The destination returned HTTP `200` and loaded with the public title `Brand Resources | Life USA Logos`.

## Decision

- `LOGO-006`: **Done**. The favicon, header, and footer placements use approved current assets and the visible logo images have descriptive alternative text.
- Homepage duplicate H1: **Done**, logged under technical/on-page SEO rather than the logo program.
- Brand Resources navigation link: **Done** and publicly reachable.
- `APR-007`: remains approved and partially executed only because the two homepage `WebSite` nodes still require consolidation.
- Stable monitoring count remains **0 of 3**. This ad hoc owned-site verification is not a scheduled regression check and does not prove a Google refresh.
