# New migration configuration examples

These examples were created for the export and are not original application files. The original active configuration remains at `original-project/dist/site-config.json`.

- The disabled JSON preserves current behavior.
- Formspree/Jotform placeholders intentionally do not pass the frontend's endpoint validation. Replace them with your own verified provider values in a working copy only.
- Keep Formspree photo upload verification false until delivery of supported photo attachments is tested with the actual recipient.
- The NGINX example is optional and requires your server's normal MIME configuration and separate HTTPS setup.
- There is no `.env.example`, database schema or package lock because this original application uses none. Environment files are not read by its build or frontend.
