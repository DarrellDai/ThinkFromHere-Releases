"""Convert authenticated GitHub release metadata to the public static update feed."""
import json
import re
import sys
from pathlib import Path

REPO_URL = 'https://github.com/DarrellDai/ThinkFromHere-Releases'
SUFFIXES = ('windows-x64.exe', 'macos-universal.dmg', 'linux-amd64.deb',
            'linux-x64.tar.gz', 'android.apk', 'ios-simulator.zip')


def manifest(release):
    tag = release.get('tag_name', '')
    if not re.fullmatch(r'v\d+\.\d+\.\d+', tag) or release.get('draft') or release.get('prerelease'):
        raise ValueError('Expected a published stable release')
    if release.get('html_url') != f'{REPO_URL}/releases/tag/{tag}':
        raise ValueError('Unexpected release URL')
    packages = {f'ThinkFromHere-{tag[1:]}-{suffix}' for suffix in SUFFIXES}
    expected = packages | {name + '.sha256' for name in packages}
    assets = []
    seen = set()
    for asset in release.get('assets', []):
        name = asset.get('name')
        if name not in expected:
            continue
        if name in seen:
            raise ValueError('Duplicate asset')
        seen.add(name)
        size = asset.get('size')
        url = f'{REPO_URL}/releases/download/{tag}/{name}'
        if type(size) is not int or size <= 0 or asset.get('state') != 'uploaded':
            raise ValueError('Asset upload is incomplete')
        if asset.get('browser_download_url') != url:
            raise ValueError('Unexpected asset URL')
        assets.append({'name': name, 'size': size, 'browser_download_url': url})
    if seen != expected:
        raise ValueError('Release must contain all six installers and their SHA-256 files')
    return {'schema_version': 1, 'tag_name': tag, 'html_url': release['html_url'],
            'assets': sorted(assets, key=lambda asset: asset['name'])}


if __name__ == '__main__':
    result = manifest(json.loads(Path(sys.argv[1]).read_text()))
    destination = Path(sys.argv[2])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2) + '\n')
