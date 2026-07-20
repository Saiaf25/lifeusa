# LOGO-005 live structured-data verification

Verified July 20, 2026 at 16:01 Europe/Istanbul after the user reported publishing the prepared homepage NGO markup under approved action `APR-007`.

## Public verification result

The cache-busted public homepage `https://www.lifeusa.org/?verify=20260720-logo005` returned successfully and exposed three parseable `application/ld+json` blocks with zero JSON parse errors.

The rendered source contains one `NGO` node with:

- `@id`: `https://www.lifeusa.org/#organization`
- `name`: `Life for Relief and Development`
- `alternateName`: `LifeUSA`
- canonical organization URL: `https://www.lifeusa.org/`
- the approved colored 1800 by 1800 square logo
- the verified Southfield postal address
- the public customer-support telephone number
- eight verified official `sameAs` destinations

The canonical square file returned HTTP `200` as `image/png`, measured 1800 by 1800 pixels, contained 29,393 bytes, and retained SHA-256 `d3d830b08effb1202b1ded8bc26bec91f78dfb8b89c97ef59f892b2ea88a77cb`.

## Removed defect

The old white-logo asset `6df904_2bb6857d9c8b49ae91789ad75efbc8b8~mv2.png` is absent from the fetched homepage HTML. The public NGO node now references only the canonical colored square asset `af2a6c_49a4190c354746b493c123d311222fb5~mv2.png`.

## Remaining Wix work

The homepage still emits two `WebSite` nodes. This does not reverse the verified NGO repair, but duplicate-`WebSite` consolidation remains open. The public brand-resources page and any unverified header, favicon, or footer alignment work also remain assigned to LOGO-004, LOGO-006, and the approved but not fully completed APR-007 package.

## Decision

- `LOGO-005`: **Done**. The live Organization/NGO identity node now passes the prepared acceptance checks.
- `APR-007`: **Approved and partially executed**, not completed.
- `GATE-E`: **Done** because the user explicitly approved APR-007 on July 20.
- Stable monitoring count remains **0 of 3**. This ad hoc source correction is not a scheduled regression check.
