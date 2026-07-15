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

## Fields preserved

- Site display name: `Life USA`
- Business name: `Life for Relief and Development`
- Business description: unchanged

The update used a field mask containing only `logo`, so no other Business Profile field was intentionally changed.

## Post-change homepage check

The live homepage was reloaded after the Business Profile update. Its existing custom `NGO` JSON-LD still references:

`https://static.wixstatic.com/media/6df904_2bb6857d9c8b49ae91789ad75efbc8b8~mv2.png`

This confirms the custom homepage structured data is managed separately from the Wix Business Profile logo. The business-profile correction is complete, while replacement of `NGO.logo`, addition of `@id` and `sameAs`, and duplicate `WebSite` cleanup remain active under LOGO-005.
