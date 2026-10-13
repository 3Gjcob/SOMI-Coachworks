# Dependencies, export coverage and exact limits

Audit date: 13 October 2026. Evidence: original Git tree at commit `415b4feb176efa49c3000d5ed8c2bf8906372a56`, saved Sites version 3, successful publication record, and read-only Sites configuration inspection.

## Application files

All 44 tracked files from that original source commit are present unchanged. No frontend, generator, asset or tracked configuration file was replaced or reconstructed. `original-file-manifest.json` names every original file and records its byte size and SHA-256.

| Component | Original implementation | Export / migration result |
| --- | --- | --- |
| Frontend pages | 12 English/Spanish static HTML pages | All included |
| Page source | `scripts/build-site.py`, `scripts/repair_gallery.py` | Both original generators included |
| Styles / animation / responsiveness | Three site CSS layers plus local font CSS | All included unchanged |
| Frontend interactions | `dist/app.js` | Included unchanged |
| Assets | Logo, shop exterior, four repair photos, fonts, older unused stock/logo assets | All tracked assets included; no replacements |
| Backend API / server | No application backend in the original project | No backend code exists to export |
| Database / schema / migrations | No database configured or referenced | No schema, migration or database dump exists for this application |
| File upload storage | No active upload service; no D1/R2 bindings | No stored application uploads to migrate through this project |
| Package dependencies | Browser APIs plus Python standard library for generating pages | No npm/pip third-party packages, manifests, lockfiles or vendored dependencies exist |
| Runtime environment | Sites environment entries are empty, revision 0 | No application environment values or secrets to export |
| Authentication | Public site; no application login/session code | No end-user account store or OAuth implementation to migrate |
| Schedules / MCP / connected apps | No automations; deployment reports `has_mcp: false`; no connector bindings; `requires_byop: false` | No application integration or scheduled task replacement needed |

The Sites project has a platform auth-client record, but the public source does not use it and visitors are not required to sign in. Do not recreate a ChatGPT login flow for the independent site.

## ChatGPT Sites dependencies to replace or retire

| Sites dependency | Where it appears | Action on independent hosting |
| --- | --- | --- |
| Static hosting, CDN, TLS and routing | Managed service serving `dist/` | Replace with a static host; preserve directory routes and asset paths |
| Generated `chatgpt.site` origin | `ORIGIN` in the generator and generated metadata/sitemap/robots | Change the constant in a working copy and rebuild when the final origin is known |
| Sites manifest / project ID | `.openai/hosting.json` | Retain for provenance; independent host does not need it |
| Source repository, save-version/deploy workflow | Sites editor tooling; not browser runtime | Use your own repository/deployment process; no Sites tool is needed to serve or build these files |
| Platform authentication / administration | Sites control plane | Not portable as application code; not needed for this public frontend |
| Pending custom-domain binding | `www.somicoachworks.com`, pending / pending_validation | Configure ownership, DNS and TLS independently when you choose to migrate; nothing was changed here |

The old generated hostname cannot be moved to another provider through this ZIP. Continued service at that hostname remains controlled by ChatGPT Sites. Domain registrar access and DNS ownership are separate from the source code.

## External dependencies that remain external

| Service | Current use | State and migration effect |
| --- | --- | --- |
| Google Maps | Third-party map iframe, directions and listing/review links | Requires internet and Google availability; no Maps API key appears in the code |
| Instagram | External profile link | No Instagram API, live feed, login or token; supplied gallery photos are local |
| Google review text | Three static excerpts and a dated rating snapshot | Stored in generator/HTML; not refreshed by an API; original source attribution remains in README |
| Phone/email | `tel:` and `mailto:` links to the shop | Uses visitor device/apps; no email server or mailbox contents are included |
| Florida consumer guide | External PDF link | The linked third-party document is not part of the application source |
| Formspree | Optional multipart estimate submission code | Endpoint is null; upload verification false; not connected or tested end-to-end |
| Jotform | Optional secure external form link | URL is null; no provider form definition/account exists in this project |
| Fonts | Barlow Condensed and Manrope TTF files, local `fonts.css` | All eight original files included; no remote font request needed |

## What is not exportable from this project

- ChatGPT Sites' own hosting/CDN/dispatcher/platform service source, administration UI, platform authentication infrastructure, generated TLS private keys, operational log history and internal deployment machinery. These are managed platform systems rather than files in the application repository. No platform source export was available through the provided capabilities.
- Live third-party services or accounts: Google Maps/Instagram, mailbox service, optional form provider infrastructure, domain registrar account and DNS account. The integration links/code are included; their service backends and account data are not.
- The separate existing WordPress website at `somicoachworks.com`, its PHP files, database, plugins and hosting account. This is an export of the identified ChatGPT Sites project only; no WordPress export access was provided.
- Missing original authoring/licensing material: no Figma file, layered image source, font license text or separate asset-license manifest is tracked in the source repository. The actual site-used images/fonts are included unchanged. Existing source notes are retained; the export does not invent missing license or authoring files.

## Deliberate exclusions from the ZIP

The local `.git/` database and Git authentication configuration, credentials, ignored Python bytecode caches, transient build/QA files, and ChatGPT conversation transcripts are omitted. Git history is not bundled; the exact current source snapshot and commit provenance are included. None of these exclusions removes a required website source or runtime file.

New migration notes, checks and templates are explicitly separated from original source. The independent NGINX example is newly supplied, not an original production server configuration.

## Existing limitations preserved

- There is no active online estimate delivery backend. The phone/email fallback is the current working contact method. The form UI and client validation are preserved but remain hidden until a real provider is configured.
- No appointment booking system, payments, analytics or live review synchronization exists in this source. None has been silently added.
- The hours indicator uses the stored schedule in the browser's `America/New_York` timezone. It is not connected to live business hours.
- The gallery uses separate before/after viewpoints with vehicle tabs and a full-photo dialog; it is not a generated or image-aligned comparison.
- Exact source bytes preserve the authored design and behavior. Rendering still depends on the target browser and correct host configuration. Browser/device visual equivalence and an independent production deployment were not tested during this export.
