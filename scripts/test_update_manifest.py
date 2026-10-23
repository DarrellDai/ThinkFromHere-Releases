import copy
import importlib.util
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location('manifest', Path(__file__).with_name('write-update-manifest.py'))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        tag = 'v1.2.3'
        base = module.REPO_URL
        assets = []
        for suffix in module.SUFFIXES:
            for ending in ('', '.sha256'):
                name = f'ThinkFromHere-1.2.3-{suffix}{ending}'
                assets.append({'name': name, 'size': 123, 'state': 'uploaded',
                               'browser_download_url': f'{base}/releases/download/{tag}/{name}'})
        self.release = {'tag_name': tag, 'html_url': f'{base}/releases/tag/{tag}', 'assets': assets}

    def test_complete_release(self):
        result = module.manifest(self.release)
        self.assertEqual(len(result['assets']), 18)
        self.assertNotIn('state', result['assets'][0])
        self.assertEqual(result['tag_name'], 'v1.2.3')

    def test_legacy_release_remains_supported(self):
        tag = 'v0.4.13'
        release = {'tag_name': tag, 'html_url': f'{module.REPO_URL}/releases/tag/{tag}', 'assets': []}
        for suffix in module.LEGACY_SUFFIXES:
            for ending in ('', '.sha256'):
                name = f'ThinkFromHere-0.4.13-{suffix}{ending}'
                release['assets'].append({'name': name, 'size': 123, 'state': 'uploaded',
                    'browser_download_url': f'{module.REPO_URL}/releases/download/{tag}/{name}'})
        self.assertEqual(len(module.manifest(release)['assets']), 12)

    def test_every_new_architecture_is_required(self):
        for asset in self.release['assets']:
            release = copy.deepcopy(self.release)
            release['assets'] = [item for item in release['assets'] if item['name'] != asset['name']]
            with self.subTest(asset=asset['name']), self.assertRaises(ValueError):
                module.manifest(release)

    def test_incomplete_release_cannot_replace_feed(self):
        self.release['assets'].pop()
        with self.assertRaises(ValueError):
            module.manifest(self.release)

    def test_invalid_release_or_asset_is_rejected(self):
        variants = []
        for key, value in [('draft', True), ('prerelease', True), ('tag_name', 'bad')]:
            candidate = copy.deepcopy(self.release)
            candidate[key] = value
            variants.append(candidate)
        for key, value in [('size', 0), ('size', True), ('state', 'new'), ('browser_download_url', 'https://evil.example/file')]:
            candidate = copy.deepcopy(self.release)
            candidate['assets'][0][key] = value
            variants.append(candidate)
        for candidate in variants:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                module.manifest(candidate)


if __name__ == '__main__':
    unittest.main()
