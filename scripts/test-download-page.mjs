import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { runInNewContext } from 'node:vm'
import test from 'node:test'

const html = await readFile(new URL('../index.html', import.meta.url), 'utf8')
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1]

test('each desktop architecture receives its own installer and checksum', async () => {
  const suffixes = { 'macos-x64': 'macos-x64.dmg', 'macos-arm64': 'macos-arm64.dmg', 'linux-x64': 'linux-amd64.deb', 'linux-arm64': 'linux-arm64.deb' }
  const cards = Object.keys(suffixes).map(platform => {
    assert.ok(html.includes(`data-platform="${platform}"`))
    const elements = Object.fromEntries(['.download', '.checksum-link', '.status', '.platform-description'].map(key => [key, { removeAttribute() {}, hidden: true }]))
    return { dataset: { platform }, elements, querySelector: key => elements[key] }
  })
  const assets = Object.values(suffixes).flatMap(suffix => ['', '.sha256'].map(ending => {
    const name = `ThinkFromHere-1.2.3-${suffix}${ending}`
    return { name, browser_download_url: `https://www.thinkfromhere.ai/releases/download/v1.2.3/${name}` }
  }))
  runInNewContext(script, { document: { querySelectorAll: () => cards }, fetch: async () => ({ ok: true, json: async () => ({ assets }) }), console })
  await new Promise(resolve => setImmediate(resolve))
  for (const card of cards) {
    assert.ok(card.elements['.download'].href.endsWith(suffixes[card.dataset.platform]))
    assert.equal(card.elements['.checksum-link'].href, card.elements['.download'].href + '.sha256')
    assert.equal(card.elements['.checksum-link'].hidden, false)
    assert.equal(card.elements['.status'].textContent, 'v1.2.3')
  }
})
