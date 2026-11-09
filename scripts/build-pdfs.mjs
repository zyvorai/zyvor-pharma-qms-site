#!/usr/bin/env node
/**
 * Print resources/src/*.html → resources/*.pdf with headless Chrome.
 * Usage: node scripts/build-pdfs.mjs
 */
import { execFileSync } from 'node:child_process'
import { existsSync, mkdirSync, readdirSync } from 'node:fs'
import { dirname, join, resolve } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..')
const SRC = join(ROOT, 'resources', 'src')
const OUT = join(ROOT, 'resources')

const CHROME = [
  '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
  '/Applications/Chromium.app/Contents/MacOS/Chromium',
  '/usr/bin/google-chrome',
  '/usr/bin/chromium',
  '/usr/bin/chromium-browser',
].find((p) => existsSync(p))

if (!CHROME) {
  console.error('Chrome/Chromium not found')
  process.exit(1)
}

mkdirSync(OUT, { recursive: true })
const files = readdirSync(SRC).filter((f) => f.endsWith('.html'))
if (!files.length) {
  console.error('no HTML in resources/src')
  process.exit(1)
}

for (const f of files) {
  const html = join(SRC, f)
  const pdf = join(OUT, f.replace(/\.html$/, '.pdf'))
  const url = pathToFileURL(html).href
  console.log('→', pdf.replace(ROOT + '/', ''))
  execFileSync(
    CHROME,
    [
      '--headless=new',
      '--disable-gpu',
      '--no-pdf-header-footer',
      '--print-to-pdf-no-header',
      `--print-to-pdf=${pdf}`,
      url,
    ],
    { stdio: 'inherit' },
  )
}
console.log(`built ${files.length} PDFs`)
