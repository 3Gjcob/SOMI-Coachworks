# South Miami Coach Works / SOMI Coachworks

Public static website. Existing Site identity and audience are preserved. Customers do not need to sign in.

## Source and publishing

- `scripts/build-site.py` generates 12 static pages: English and Spanish homepages, four service pages per language, and an insurance-claims page per language.
- `dist/` is the deployable directory. Run `python scripts/build-site.py` after changing page content.
- `dist/styles.css` supplies the base layout; `dist/updates.css` contains the checklist refinements and `dist/brand.css` applies the red, white and blue identity.
- `scripts/repair_gallery.py` supplies the bilingual repair folio with vehicle tabs, paired photos and individual before/after views.
- `dist/app.js` handles the mobile menu, local-time opening indicator, dialogs, repair gallery, full-screen photo viewer and optional estimate integration.
- `.openai/hosting.json` preserves project `appgprj_6acd445ebbd881919b949fe40369e5a5`.
- Previous published source is preserved in Git at `5ff6caf7eaa8fc9d9d0ff721fd5a49ef6bef70e6`.

## Estimate delivery: connection still required

The former two-step mailto composer was removed. The live default is a clear phone/email contact card, including instructions to attach photos by email. There is no unconnected Submit button and no pretend successful submission.

The bilingual photo-upload interface is implemented but intentionally hidden until a verified provider is connected. It has contact and vehicle fields, optional insurer, consent, a honeypot, up to five 5 MB JPG/PNG/WebP files, file previews, validation, duplicate-submit prevention, and failure/success states. It does not persist anything locally.

Configure `dist/site-config.json` with either:

1. A verified shop-owned Formspree URL in `formspreeEndpoint`, then set `photoUploadsVerified: true` only after confirming the provider plan accepts files and the shop is the verified recipient.
2. An existing public `https://form.jotform.com/<numeric-form-id>` in `jotformUrl`, which exposes a secure external form link.

No service was connected in this session. No emails, test submissions, external profile changes or purchases were made. Never put an API key in this public configuration file. Formspree file uploads are on its Personal, Professional and Business plans, not the free tier, per https://help.formspree.io/articles/building-your-form/file-uploads . Destination, provider spam controls, server-side validation, notification delivery and photo receipt require end-to-end verification before activation. The custom form uses the provider's JSON endpoint; a confirmed `ok: true` response is required before success is shown.

## Content sources and deliberate limits

- Address/phone and Google review excerpts were preserved from the user-supplied listing screenshots documented in the previous version.
- Business name is standardized to **South Miami Coach Works**, with SOMI Coachworks retained as an alternate brand name.
- Profile: https://www.instagram.com/somicoachworks/ . Public metadata read on 2026-10-12 states “Paint and body shop located in South Miami”, “20+ years of experience”, and “3.7K vehicles repaired”. The experience statement is used as team experience, not a founding date. The changing vehicle count is not published.
- Instagram did not expose post media or testimonials in this session. The repair gallery links directly to the real profile. Additional client testimonials still require accessible source material.
- The user-uploaded `somilogo.png` is now the header/footer logo, favicon and structured-data brand image, stored as `dist/assets/somi-brand.png`. The theme uses the logo's red, white and blue palette.
- The four uploaded repair photos are stored in `dist/assets/repairs/`: Mustang before/after and Bronco before/after. The paired folio preserves their separate viewpoints and supports individual-photo views and a full-size dialog. Originals are byte-identical to the uploads.
- Official contact: https://somicoachworks.com/ . Several old WordPress pages currently fail with plugin errors; their stock images were not mislabeled as real projects.
- Services, all-makes statement, insurance assistance and Spanish: https://www.carwise.com/auto-body-shops/south-miami-coach-works-llc-south-miami-fl-33143/560420 and existing official Spanish pages at https://somicoachworks.com/es/tag/auto-body/ . No ADAS, paintless dent repair, frame, rust, certification, direct-repair affiliation or owner claim was invented.
- Hours remain the Google-derived schedule from the original build: Monday 7:30–17:00, Tuesday–Friday 7:30–17:30, weekends closed. Other listings disagree. Ask the shop to confirm before replacing them. The opening indicator explicitly describes listed hours.
- Reviews: existing Nelson Colon, Andrew Gamil and Martin Thiry excerpts; 5.0 / 14 is labeled an October 2026 snapshot, not a live feed. The repeated review-card labels and odd footer disclaimer were removed. Rating schema is omitted until reliably maintained.
- The “Leave us a review” link opens the correct Google Maps search/listing; the adjacent instruction tells visitors to choose “Write a review”. It does not claim to open a direct review-composer without a verified place ID.
- Florida choice-of-shop guidance: https://www.myfloridacfo.com/docs-sf/consumer-services-libraries/consumerservices-documents/understanding-coverage/consumer-guides/english---automobile-insurance-toolkit.pdf?sfvrsn=6b999793_9 . Coverage and cost caveats are retained.
- The uploaded shop exterior is the homepage hero and social-sharing image, stored as `dist/assets/shop-exterior.png`. Mobile layouts show the complete exterior photo above the heading. No stock photography is displayed; the obsolete stock-photo disclosure was removed.

## Validation

All 12 pages checked for HTML structure, duplicate IDs, local resources, anchors, canonical/hreflang links, structured-data JSON, one H1, image alt text, external-link safety and sitemap validity. JavaScript syntax checked with `node --check dist/app.js`. CSS braces and static responsive rules inspected. Browser, iPhone/Android, actual email delivery and iMessage/WhatsApp preview checks remain unverified: the required managed browser-control capability was unavailable. No preview server was started.

## Shop-dependent next steps

See `CHECKLIST_STATUS.md`. The source and deployable pages are complete for the supported changes; form delivery, additional testimonials, owner details, DNS/email, Search Console and Business Profile work remain pending access or confirmation.
