import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync } from 'node:fs';

// Artículos marcados con noindex (los cortos): fuera del sitemap hasta que se amplíen.
const ocultos = new Set(
  readdirSync('./src/content/datos')
    .filter((f) => /^noindex: true$/m.test(readFileSync(`./src/content/datos/${f}`, 'utf8').split('\n---')[0]))
    .map((f) => `/datos/${f.replace(/\.mdx?$/, '')}/`),
);

export default defineConfig({
  site: 'https://eldatodeldia.online',
  integrations: [mdx(), sitemap({ filter: (page) => !ocultos.has(new URL(page).pathname) })],
  build: { inlineStylesheets: 'always' },
});
