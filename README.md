# El Dato del Día: sitio web

Sitio en [Astro](https://astro.build) con artículos que amplían los datos de los videos de TikTok. Preparado para Google AdSense.

## Comandos
```bash
npm install     # una sola vez
npm run dev     # verlo en http://localhost:4321
npm run build   # generar el sitio en dist/
```

## Publicar un dato nuevo
1. Crea `src/content/datos/mi-dato.mdx` copiando uno de los ejemplos.
2. Rellena `numero` (el "Dato #" del video), `title`, `description`, `hook`, `category`, `date`, `faq` y `sources`.
3. Opcional: `tiktokId`, el número final del link del video, para incrustarlo.
4. Pon `<Ad />` en la mitad del texto para un anuncio.
5. Haz commit y push. Vercel publica solo.

## Lo que debes configurar tú (`src/config.ts`)
- `tiktok`, `email`
- `gaId`: Google Analytics 4
- `adsenseClient`: cuando AdSense te apruebe, más `public/ads.txt`
- El dominio en `astro.config.mjs`

## Estructura
- `src/pages/`: inicio, `/datos/[slug]`, `/categoria/[cat]`, `/tiktok` (link en bio), páginas legales
- `src/components/`: Header, Footer, Card, AdSlot, CookieBanner
- `PLAN.md`: plan de trabajo · `PASOS-SIGUIENTES.md`: lo que te toca hacer · `GUIA-SKILLS-Y-MCP.md`: skills y MCP
