# LifeUSA Google property audit

Audit date: July 15, 2026

Locale: English, United States

Desktop viewport: 1280 by 720 pixels

## Executive finding

Google already has a local Business Profile for Life for Relief & Development at the correct Southfield address. The profile should not be recreated. It must be updated through the existing owner or manager account.

The exact branded entity query also exposed an older blue-globe logo in a sponsored LifeUSA result. A separate nonprofit Knowledge Panel did not appear in this check.

## Search surface

Repeatable query:

`https://www.google.com/search?q=Life+for+Relief+and+Development+Southfield+MI&hl=en&gl=us&pws=0`

Observed state:

- A sponsored LifeUSA result used the older blue-globe logo.
- The right-hand entity surface was the local Google Business Profile, not a separate organization Knowledge Panel.
- The profile showed 4.3 stars and 20 Google reviews.
- The category was Non-Profit organization.
- The address was 17300 W 10 Mile Rd, Southfield, MI 48075.
- The website destination was the stale HTTP URL `http://www.lifeusa.org/`.
- Instagram, YouTube, Facebook, and TikTok profile links were present.

Evidence: [Google entity-surface capture](google-search-lifeusa-entity-surface-2026-07-15.jpg)

## Google Business Profile ownership

The existing listing was selected from the Google Business Profile claim flow. Google reported that it is currently managed by a masked `li...@gmail.com` account. The Google account available in this working session does not manage LifeUSA.

No access request was sent. Sending it would notify the current manager and disclose the requester’s Google identity, so that action requires an approved organizational account and intentional authorization.

Evidence: [Business Profile claim-state capture](google-business-profile-claim-state-2026-07-15.jpg)

Required next step:

1. Identify the internal owner of the masked manager account.
2. Add an authorized LifeUSA organizational account as owner or manager.
3. Replace the logo, cover, and outdated profile media with the approved current asset set.
4. Change the website link from HTTP to `https://www.lifeusa.org/`.
5. Recheck the public profile after Google finishes processing the edits.

## Google Maps photo surface

The public Maps listing resolves to the established Southfield location:

- Google place identifier: `/g/1ttdnlzz`
- Google Maps CID: `0xd5173b8aa5409446`
- Rating and review count: 4.3 from 20 reviews
- Public website link: `http://www.lifeusa.org/`

The photo gallery includes a contribution associated with a Google Maps contributor account using an older blue Life logo as its avatar. Contributor profile ID: `115898584427846492369`.

This contributor avatar is a separate Google account identity signal. It should be replaced by that account owner if the account is controlled by LifeUSA; it cannot be changed from the Business Profile itself.

Evidence:

- [Maps photo-gallery capture](google-maps-lifeusa-photo-gallery-2026-07-15.jpg)
- [Older contributor avatar](legacy-blue-google-maps-contributor-avatar.png)

## Google Ads and Ad Grants

The public sponsored result proves that a LifeUSA advertiser is currently serving the older blue-globe logo. The logo may come from account-level business information, a campaign-level brand asset, or a Google-generated dynamic asset.

The local Google Ads CLI was checked read-only on July 15. Its accessible customer and manager hierarchy contains TTP/TMD advertising accounts and no LifeUSA customer. No LifeUSA Ads or Ad Grants asset could therefore be inspected or changed from the available credentials.

Required next step for the LifeUSA Ads administrator:

1. Open account-level Business information in Google Ads.
2. Inventory business name and square and landscape logo assets.
3. Check campaign-level brand guidelines, especially Performance Max.
4. Disable or replace any dynamic or manually uploaded older-logo asset.
5. Upload the approved current square logo from the LifeUSA Wix asset set.
6. Verify asset approval and capture the post-change sponsored result.

## Knowledge Panel conclusion

No separate nonprofit Knowledge Panel appeared in the exact entity query. The right-hand result was the local Business Profile. LOGO-012 remains active as a monitoring and claim task in case a distinct organization panel appears in another locale, device, or future result set.

## Published evidence files

| File | Purpose |
|---|---|
| `google-search-lifeusa-entity-surface-2026-07-15.jpg` | Sponsored old-logo result and local profile |
| `google-business-profile-claim-state-2026-07-15.jpg` | Existing-profile manager dependency |
| `google-maps-lifeusa-photo-gallery-2026-07-15.jpg` | Public Maps media inventory |
| `legacy-blue-google-maps-contributor-avatar.png` | Older contributor-account avatar |
