# Setup, editing and independent hosting

These instructions were added for this export. All paths below refer to the extracted ZIP; no commands in this guide publish to ChatGPT Sites.

## Requirements

- To host the supplied `dist/`: an HTTP(S) static file host with directory indexes and correct MIME types.
- To edit/rebuild page content: Python 3; the original generator was verified with Python 3.12.14. It uses only the standard library (`pathlib`, `html`, `json`) and the included `repair_gallery.py`.
- Node.js is optional, solely for `node --check dist/app.js`; no Node runtime, npm packages, package manifest, lockfile, or `node_modules` is required by the application. The syntax check was performed with Node 24.19.0.
- Browser features used include native `<dialog>`, Fetch, FormData, CSS grid/flex, media queries, Intl with `America/New_York`, and dynamic viewport units. Preserve those behaviors; test your intended browsers before cutover.

## First local run

From the extracted export folder:

```bash
python3 migration/verify_export.py
python3 -m http.server 8000 --bind 127.0.0.1 --directory original-project/dist
```

On Windows substitute `py -3` for `python3`. Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/es/ . Stop the server with Ctrl+C. Use Python's server only for local development; production should use a static hosting service or production web server.

## Work from a copy

Copy `original-project/` to a new working directory, for example `somi-working/`, and open that directory in Claude Code. Initialize your own Git repository there if wanted. The original export intentionally omits the checkout's `.git/` directory, credentials, ignored caches and editor state; file contents and provenance are preserved.

The source of page content is `scripts/build-site.py`. Repair-gallery content is in `scripts/repair_gallery.py`. CSS layers load in this order: `assets/fonts.css`, `styles.css`, `updates.css`, `brand.css`. Frontend behavior lives in `dist/app.js`.

From the working project root, rebuild after editing generator content:

```bash
python3 -X utf8 scripts/build-site.py
node --check dist/app.js
```

The Node command is optional if Node is unavailable. Rebuilding regenerates 12 HTML pages, `sitemap.xml` and `robots.txt`; it preserves existing CSS, JavaScript, images and `site-config.json`. Direct edits to generated HTML will be overwritten by the next rebuild. The build does not read a `.env` file or contact ChatGPT.

## Change the domain only in your independent working copy

The original generator sets:

```python
ORIGIN = 'https://somicoachworks.jkalka28227.chatgpt.site'
```

Once you know the final HTTPS origin, change that one constant in the working copy of `scripts/build-site.py`, without a trailing slash, and run the build. It updates canonical URLs, language alternate URLs, social sharing URLs, structured data, the sitemap and robots file. The preserved export intentionally retains the original domain until you choose a replacement.

Assets and navigation are root-relative (`/assets/...`, `/es/...`), so deploy at the root of a domain or subdomain. A subdirectory such as `example.com/somi/` requires additional path changes and is not an identical drop-in deployment.

## Independent static hosting

Use these settings on the host of your choice:

| Setting | Value |
| --- | --- |
| Project directory | Your working copy of `original-project/` |
| Publish / document root | `dist/` |
| Build command | None for supplied output; `python3 -X utf8 scripts/build-site.py` only if the host has Python and should rebuild |
| Index document | `index.html` in each directory |
| Application runtime | None |
| Database / migrations | None |
| Environment variables | None |
| Public access | Normal public static access; no sign-in gate |
| Unknown routes | Return 404; do not rewrite every request to the homepage |

Upload all of `dist/`, including `assets/`, both language trees, JSON config, CSS, JS, sitemap and robots. Do not upload the whole export as the document root; only `dist/` should be public. HTTPS, certificates, DNS, caching and access logs are configured with your chosen hosting provider.

For an existing NGINX installation, `config-templates/nginx-static.conf.example` is an optional server-block example. Replace its hostname and filesystem path, include it in your server configuration, and run the host's configuration validation before enabling it. It is an HTTP template; arrange HTTPS using your host's certificate workflow. The template was not deployed or tested on a running NGINX instance in this export task.

## Optional estimate provider

`dist/site-config.json` is the current configuration and is included exactly. All three values are disabled/null. The public website uses phone and email contact by default.

The frontend already supports either a shop-owned Formspree form endpoint or a Jotform link. Examples are in `config-templates/`. They are not credentials, do not provision provider accounts, and are not active. Provider plans, verified recipients, file acceptance, anti-spam settings, CORS/origin acceptance and actual notification delivery must be checked when you connect a real account. Do not set `photoUploadsVerified: true` before confirming upload and delivery behavior. The custom form expects a successful HTTP response and a JSON `ok: true` result.

No environment variables are read. Do not put passwords, private tokens or API keys in the browser-readable `site-config.json`. Any future custom backend is new functionality, not part of this export.

## Cutover checklist — for a future deliberate migration

1. Keep the old Site live while testing the new host on a temporary hostname.
2. Verify all 12 routes, language switches, phone/email/map links, fonts and images.
3. Test desktop and mobile layout, reduced motion, tab keyboard navigation, gallery views, full-size photos, Escape/close focus return, privacy dialog and FAQ expansion.
4. Confirm that the contact fallback is visible and the unconfigured form stays hidden.
5. Choose the final domain, change `ORIGIN` in the working copy, rebuild and upload.
6. Configure HTTPS and any desired www/apex redirect at the new host.
7. Coordinate DNS with the domain owner. Preserve mail records. Only change web DNS after the owner approves cutover.
8. Keep the existing Sites publication until you explicitly choose to retire it.

Read-only platform inspection on 13 October 2026 found `www.somicoachworks.com` attached to Sites in `pending` status, with SSL `pending_validation`. These records were not refreshed or changed. This is the Sites control-plane status, not an independently verified DNS lookup. That pending binding will not configure independent hosting automatically.

## Official references consulted for the new guidance

- Python local preview server: https://docs.python.org/3.12/library/http.server.html
- NGINX static serving and directory indexes: https://docs.nginx.com/nginx/admin-guide/web-server/serving-static-content/
- NGINX index directive: https://nginx.org/en/docs/http/ngx_http_index_module.html

These references support the new setup guidance, not the provenance of the original site files.
