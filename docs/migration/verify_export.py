"""Check this repository against the original ChatGPT Sites export snapshot.

Run from anywhere: python3 docs/migration/verify_export.py
Two original notes files were moved into docs/ in this repository; they are
checked at their new location.
"""
from pathlib import Path
import argparse
import hashlib
import json
import sys

MOVED = {
    'README.md': 'docs/ORIGINAL_README.md',
    'CHECKLIST_STATUS.md': 'docs/CHECKLIST_STATUS.md',
}

def main():
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project', type=Path, default=here.parents[1])
    args = parser.parse_args()
    rows = json.loads((here / 'original-file-manifest.json').read_text(encoding='utf-8'))
    failed = []
    for row in rows:
        path = args.project / MOVED.get(row['path'], row['path'])
        if not path.is_file():
            failed.append('MISSING: ' + row['path'])
            continue
        data = path.read_bytes()
        if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
            failed.append('CHANGED: ' + row['path'])
    if failed:
        print('\n'.join(failed))
        return 1
    print(f'PASS: all {len(rows)} original files match the recorded source snapshot.')
    print('This verifies file integrity, not browser behavior or external-service delivery.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
