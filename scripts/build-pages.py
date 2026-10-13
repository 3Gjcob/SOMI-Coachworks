"""Make a copy of dist/ that works under a URL subpath, e.g. GitHub Pages project sites.

dist/ uses root-relative links (/assets/..., /es/...) and the canonical ORIGIN from
build-site.py. This copies dist/ to an output folder and rewrites those links for a
site served at <origin><base>/. dist/ itself is not modified.

Usage: python3 scripts/build-pages.py --base /SOMI-Coachworks --origin https://3gjcob.github.io --out _site
"""
from pathlib import Path
import argparse
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'
SOURCE_ORIGIN = 'https://somicoachworks.jkalka28227.chatgpt.site'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', required=True, help='URL subpath without trailing slash, e.g. /SOMI-Coachworks')
    parser.add_argument('--origin', required=True, help='Scheme and host without trailing slash')
    parser.add_argument('--out', type=Path, default=ROOT / '_site')
    args = parser.parse_args()
    base = '/' + args.base.strip('/') if args.base.strip('/') else ''
    origin = args.origin.rstrip('/')
    out = args.out.resolve()
    if out == DIST.resolve():
        raise SystemExit('Refusing to overwrite dist/')
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(DIST, out)

    attr = re.compile(r'(\s(?:href|src)=")/(?!/)')
    for path in out.rglob('*'):
        if path.suffix not in {'.html', '.xml', '.txt', '.js'}:
            continue
        text = path.read_text(encoding='utf-8')
        new = text.replace(SOURCE_ORIGIN, origin + base)
        if path.suffix == '.html':
            new = attr.sub(r'\1' + base + '/', new)
        if path.name == 'app.js':
            new = new.replace("fetch('/site-config.json'", f"fetch('{base}/site-config.json'")
        if new != text:
            path.write_text(new, encoding='utf-8')
    (out / '.nojekyll').write_text('')
    print(f'Wrote {out} for {origin}{base}/')


if __name__ == '__main__':
    main()
