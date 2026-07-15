# LifeUSA Wix logo implementation specification

Prepared July 15, 2026. This is an implementation-ready specification, not a claim that the changes are already live.

## Production asset contract

Publish these files on `lifeusa.org` under stable URLs that will not change when Wix media-library filenames change:

| Purpose | Proposed production URL | Source candidate | Requirement |
|---|---|---|---|
| Canonical square logo | `https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png` | `current-square-favicon-source.png` | Live, Wix-owned, 1800 by 1800, colored mark visible on white |
| Canonical horizontal logo | `https://www.lifeusa.org/brand/lifeusa-official-logo-horizontal.png` | `lifeusa-current-logo-source.png` | Current horizontal mark used in the live header |

The square URL is live and assigned to the Wix Business Profile logo field. The proposed custom-domain horizontal URL is not live yet. Confirm the final horizontal path before replacing the live header source.

## Consolidated NGO node

Use one stable entity identifier and one canonical square logo URL. Add only profiles confirmed as official LifeUSA properties.

```json
{
  "@context": "https://schema.org",
  "@type": "NGO",
  "@id": "https://www.lifeusa.org/#organization",
  "name": "Life for Relief and Development",
  "alternateName": "LifeUSA",
  "url": "https://www.lifeusa.org/",
  "logo": {
    "@type": "ImageObject",
    "url": "https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png",
    "contentUrl": "https://static.wixstatic.com/media/af2a6c_49a4190c354746b493c123d311222fb5~mv2.png",
    "width": 1800,
    "height": 1800,
    "caption": "Life for Relief and Development official logo"
  },
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "17300 W 10 Mile Rd",
    "addressLocality": "Southfield",
    "addressRegion": "MI",
    "postalCode": "48075",
    "addressCountry": "US"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "Customer Support",
    "telephone": "+1-800-827-3543"
  },
  "sameAs": [
    "https://www.facebook.com/Life4ReliefEN/",
    "https://www.instagram.com/life4relief/",
    "https://www.linkedin.com/company/life-for-relief-and-development",
    "https://linktr.ee/LIFEUSA"
  ]
}
```

The square logo URL and dimensions are verified live. The snippet is ready for the homepage custom structured-data control; validate the rendered source after publication.

## Website node cleanup

The homepage currently publishes two separate `WebSite` nodes. If Wix permits custom control, consolidate them into one node and connect it to the NGO:

```json
{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "@id": "https://www.lifeusa.org/#website",
  "url": "https://www.lifeusa.org/",
  "name": "LifeUSA",
  "publisher": {
    "@id": "https://www.lifeusa.org/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://www.lifeusa.org/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

If Wix automatically generates a `WebSite` node that cannot be removed, do not add another competing node. Preserve the Wix node and focus the custom markup on the NGO identity.

## Wix publication checklist

1. Keep the published square master at its verified Wix URL and publish the horizontal master at its final stable URL.
2. Confirm both files return `200` without authentication or a redirect chain. The square check already passes.
3. Use the square file for the favicon source, `NGO.logo`, Google Business Profile, and authority profiles.
4. Use the horizontal file for the site header and other wide placements.
5. Replace the current white-on-transparent `NGO.logo` source.
6. Add `@id`, `alternateName`, and the verified `sameAs` list.
7. Avoid adding unverified social profile URLs.
8. Validate the homepage with Google's Rich Results Test and Schema.org Validator.
9. Inspect the rendered homepage source to confirm only the intended entity nodes are present.
10. Request homepage recrawling in Google Search Console after the live verification passes.

## Acceptance evidence

- Final stable asset URLs
- Browser screenshots of the header and favicon
- Rendered JSON-LD copied from the live homepage
- Rich Results Test and Schema.org Validator results
- Search Console inspection and recrawl request date
