# LOGO-004 live brand-resources page verification

Verified July 20, 2026 against the logged-out public page and direct Wix media URLs. A second cache-busted check recorded the final published state after the initial verification identified a derived horizontal JPG.

## Public page

| Check | Verified result |
|---|---|
| URL | `https://www.lifeusa.org/brand-resources` |
| HTTP state | `200` |
| Page title | `Brand Resources | Life USA` |
| Canonical URL | `https://www.lifeusa.org/brand-resources` |
| Meta description | `Have a look at Brand Resources by Life USA` |
| Page construction | Native Wix heading, introductory text, and Wix Pro Gallery; not an embedded HTML page |

The public page identifies itself as the official LifeUSA brand-resources page and states that its logos are approved for publisher, partner, directory, and media use.

## Logo asset verification

| Placement | Live gallery file | Dimensions | SHA-256 | Comparison with approved master |
|---|---|---:|---|---|
| Square logo | `https://static.wixstatic.com/media/af2a6c_f5d2d0c72329434cb1b4bcdf64a17820~mv2.png` | 1800 by 1800 | `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb` | Byte-for-byte identical to the approved square master |
| Horizontal logo, initial check | `https://static.wixstatic.com/media/af2a6c_fd3df82a213a4509bda08d3b4b7257ef~mv2.jpg` | 3000 by 879 | `424849bce4861cdff4942f2b5e1bd09b9da8a70a746a2b9b94afc7981959fd14` | Derived edited JPG; subsequently replaced |
| Horizontal logo, final check | `https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png` | 4101 by 1201 | `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867` | Approved canonical horizontal master |

The approved canonical horizontal PNG remains healthy at:

`https://static.wixstatic.com/media/af2a6c_1bd1137d792b44c3855d26ee4cfcced0~mv2.png`

It returns `200`, measures 4101 by 1201, and has SHA-256 `14819312d534ee94bcb625a87a15ab76cd05ad77ec9d09a2b514bf8c308cd867`.

## Final acceptance decision

- The second live check proves that the approved horizontal PNG replaced the derived JPG.
- The square gallery image has descriptive alt text. The horizontal title is visible, although its image alt field remains empty in the rendered source.
- The project owner explicitly confirmed that direct download links are not required for this page.
- The project owner confirmed the page is complete and accepted its current public guidance and metadata for the LOGO-004 scope.

## Decision

The public page returns `200` and now displays both approved canonical logo files. Under the project owner's explicit acceptance decision that direct download links are not required, `LOGO-004` is **Done**. This proves the owned-source publication only; it does not prove that Google has refreshed its logo selection or complete the broader monitoring program.
