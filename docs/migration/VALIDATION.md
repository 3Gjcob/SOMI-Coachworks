# Export verification

Performed on 13 October 2026.

- Native Sites records identify saved version 3 at source commit `415b4feb176efa49c3000d5ed8c2bf8906372a56`, with a successful public publication. The local original repository has that exact HEAD and a clean working tree.
- Every one of the 44 exported original files was compared byte-for-byte against its Git blob at that commit. The export was made from `git archive`, not a reconstruction of rendered pages.
- The original generator was run only in a disposable copy. All 44 original files still matched afterward: the generated 12 pages, sitemap and robots output were byte-identical to the original source snapshot.
- JavaScript syntax passed `node --check`.
- All 12 pages passed duplicate-ID, one-H1, image-alt, JSON-data, local-resource and anchor checks; 408 local HTML references were checked. Local CSS asset references resolved and the sitemap parsed successfully.
- The active form configuration remains exactly disabled/null. All new example JSON configurations parsed successfully.
- The exported ZIP is checked for CRC integrity, duplicate/unsafe entry names and byte identity of every original file before delivery.
- The original checkout remained clean at the same commit. No source push, site version save, deployment, unpublication, authentication change, environment change or DNS/domain mutation was performed.

## Limits

Browser-based visual/interaction tests and phone/device tests were unavailable in this environment. No independent host was deployed; the new NGINX template was not run against an NGINX instance. No email or estimate submission was sent. External account behavior, Google/Instagram availability, certificate issuance and DNS cutover remain outside these checks.

The native saved deployment archive's registered hash is recorded as metadata in `provenance.json`; the remote stored archive was not downloaded to validate that hash. Original-source verification is against the exact saved source commit and its complete Git tree.

The ZIP contains the source as it exists, including unused historical assets and original notes. The included integrity checker can be rerun without installing Python packages:

```bash
python3 migration/verify_export.py
```

It intentionally reports changes if you run it against a modified migration working copy.
