# Pasos siguientes (lo que te toca a ti)

## 1. Publicar el sitio (15 min)
1. Crea una cuenta en https://vercel.com con tu GitHub.
2. **Add New → Project →** elige `El-Dato-del-Dia` (rama `main`, después de unir esta rama). Vercel detecta Astro solo. Pulsa **Deploy**.

## 2. Dominio (~10–15 USD/año)
1. Compra el dominio en Namecheap, Porkbun o Cloudflare (ej. `eldatodeldia.com`).
2. En Vercel ve a **Settings → Domains**, añádelo y copia los DNS que te indique.
3. Cambia `site` en `astro.config.mjs` por tu dominio.

## 3. Datos del sitio
Edita `src/config.ts`: tu usuario de TikTok y tu correo. En `sobre-nosotros.astro`, añade tu nombre y biografía.

## 4. Google Search Console y Analytics
1. https://search.google.com/search-console: añade el dominio y envía `https://tudominio/sitemap-index.xml`.
2. https://analytics.google.com: crea una propiedad GA4 y pon el ID `G-...` en `gaId`.

## 5. Contenido (lo más importante)
- Llega a **25–30 artículos** de 800–1500 palabras antes de solicitar AdSense.
- Cada video debe decir: **"Dato #N, la historia completa en el link de mi perfil"**.
- Pon `https://tudominio/tiktok` como link en tu bio de TikTok.
- Mándame los temas y los links de tus videos y yo te redacto los borradores. Revísalos antes de publicar.

## 6. AdSense
1. https://adsense.google.com: añade tu sitio.
2. Pon tu `ca-pub-...` en `adsenseClient` y actualiza `public/ads.txt`.
3. En AdSense, **Privacidad y mensajes → GDPR**: activa el mensaje de consentimiento de Google (CMP certificada).
4. Cuando te aprueben, crea unidades de anuncio y pon su "slot" id en `<AdSlot slot="..."/>`.

## 7. Skills y MCP
Sigue `GUIA-SKILLS-Y-MCP.md`. Cuando estén instaladas, avísame y hago una pasada de diseño con Impeccable, Emil Kowalski y Taste.

## 8. Imagen para compartir
Crea `public/og.png` (1200×630) con tu logo. Es la imagen que aparece al compartir un link en redes.
