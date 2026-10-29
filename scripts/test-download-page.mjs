import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { runInNewContext } from 'node:vm'
import test from 'node:test'

const html = await readFile(new URL('../index.html', import.meta.url), 'utf8')
const release = JSON.parse(await readFile(new URL('../updates/latest.json', import.meta.url), 'utf8'))
const script = html.match(/<script>([\s\S]*?)<\/script>/)[1]
const suffixes = { 'macos-x64': 'macos-x64.dmg', 'macos-arm64': 'macos-arm64.dmg', 'linux-x64': 'linux-amd64.deb', 'linux-arm64': 'linux-arm64.deb' }
function fixture(assets, fail = false) {
  const cards = ['macos', 'linux'].map(platform => {
    assert.equal(html.split(`data-platform="${platform}"`).length - 1, 1)
    assert.ok(!html.includes(`data-platform="${platform}-arm64"`))
    const elements = Object.fromEntries(['.download', '.checksum-link', '.status', '.platform-description'].map(key => [key, {
      removeAttribute(name) { delete this[name] }, setAttribute(name, value) { this[name] = value }, hidden: true,
    }]))
    elements['.architecture-select'] = { value: 'x64', addEventListener(event, handler) { this.change = handler } }
    return { dataset: { platform }, elements, querySelector: key => elements[key] }
  })
  runInNewContext(script, { document: { querySelectorAll: () => cards }, fetch: async () => ({ ok: !fail, status: 503, json: async () => ({ assets }) }), console: { warn() {} } })
  return cards
}
const assets = Object.values(suffixes).flatMap(suffix => ['', '.sha256'].map(ending => {
  const name = `ThinkFromHere-1.2.3-${suffix}${ending}`
  return { name, browser_download_url: `https://www.thinkfromhere.ai/releases/download/v1.2.3/${name}` }
}))

test('one card per system switches installer and checksum together in both directions', async () => {
  const cards = fixture(assets)
  await new Promise(resolve => setImmediate(resolve))
  for (const card of cards) {
    for (const arch of ['x64', 'arm64', 'x64']) {
      const select = card.elements['.architecture-select']
      select.value = arch
      select.change()
      const download = card.elements['.download']
      assert.ok(download.href.endsWith(suffixes[`${card.dataset.platform}-${arch}`]))
      assert.equal(card.elements['.checksum-link'].href, download.href + '.sha256')
      assert.equal(card.elements['.checksum-link'].hidden, false)
      assert.equal(card.elements['.status'].textContent, 'v1.2.3')
    }
  }
})

test('failed refresh keeps the current architecture-specific fallback links', async () => {
  const cards = fixture([], true)
  await new Promise(resolve => setImmediate(resolve))
  for (const card of cards) {
    for (const arch of ['arm64', 'x64']) {
      const select = card.elements['.architecture-select']
      select.value = arch
      select.change()
      const download = card.elements['.download']
      assert.ok(download.href.endsWith(suffixes[`${card.dataset.platform}-${arch}`]))
      assert.ok(download.href.includes(`/${release.tag_name}/`))
      assert.equal(card.elements['.checksum-link'].href, download.href + '.sha256')
      assert.equal(download['aria-disabled'], undefined)
    }
  }
})

test('switching to an asset without a checksum clears the previous checksum', async () => {
  const [card] = fixture(assets.filter(asset => !asset.name.endsWith('macos-arm64.dmg.sha256')))
  await new Promise(resolve => setImmediate(resolve))
  const select = card.elements['.architecture-select']
  select.value = 'arm64'
  select.change()
  assert.equal(card.elements['.checksum-link'].href, undefined)
  assert.equal(card.elements['.checksum-link'].hidden, true)
})
