import hashlib
import io
import json
import os
import re
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

version = os.environ['RELEASE_VERSION']
if not re.fullmatch(r'\d+\.\d+\.\d+', version):
    raise ValueError('Invalid version')
suffixes = ['windows-x64.exe', 'macos-universal.dmg', 'linux-amd64.deb',
            'linux-x64.tar.gz', 'android.apk', 'ios-simulator.zip']
packages = {f'ThinkFromHere-{version}-{suffix}' for suffix in suffixes}
expected = packages | {name + '.sha256' for name in packages}
destination = Path('release')
destination.mkdir()
for artifact in json.loads(os.environ['RELEASE_ARTIFACTS']):
    url = artifact['url']
    print('::add-mask::' + url, flush=True)
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != 'https' or not parsed.hostname or not parsed.hostname.endswith(('.blob.core.windows.net', '.actions.githubusercontent.com')):
        raise ValueError('Unexpected artifact host')
    archive = urllib.request.urlopen(url, timeout=180).read()
    digest = 'sha256:' + hashlib.sha256(archive).hexdigest()
    if digest != artifact['digest']:
        raise ValueError('Artifact SHA-256 mismatch: ' + artifact['name'])
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        for member in bundle.infolist():
            if member.is_dir():
                continue
            name = member.filename
            if name not in expected or (destination / name).exists():
                raise ValueError('Unexpected or duplicate artifact member: ' + name)
            with bundle.open(member) as source, (destination / name).open('wb') as output:
                import shutil
                shutil.copyfileobj(source, output)
    print('Verified artifact: ' + artifact['name'], flush=True)
if {p.name for p in destination.iterdir() if not p.name.endswith('.sha256')} != packages:
    raise ValueError('Incomplete platform set')
for name in sorted(packages):
    digest = hashlib.file_digest((destination / name).open('rb'), 'sha256').hexdigest()
    checksum = destination / (name + '.sha256')
    if checksum.exists():
        parts = checksum.read_text().strip().split(maxsplit=1)
        if len(parts) != 2 or parts[0] != digest or parts[1].lstrip('*') != name:
            raise ValueError('Package checksum mismatch: ' + name)
    checksum.write_text(f'{digest}  {name}\n')
    print(f'{digest}  {name}', flush=True)
