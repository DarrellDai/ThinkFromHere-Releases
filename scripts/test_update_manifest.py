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
        self.assertEqual(len(result['assets']), 12)
        self.assertNotIn('state', result['assets'][0])
        self.assertEqual(result['tag_name'], 'v1.2.3')

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
