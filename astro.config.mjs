import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

// Cambia esto por tu dominio real cuando lo compres.
export default defineConfig({
  site: 'https://eldatodeldia.com',
  integrations: [mdx(), sitemap()],
});
