# El Dato del Día: plan de trabajo

## 1. Concepto
**Del video de 60 segundos a la historia completa.** Cada TikTok tiene un artículo que profundiza en el dato: fuentes, contexto, curiosidades extra y datos relacionados.
El usuario llega desde TikTok, lee el artículo, sigue con otros datos y ve más anuncios.

## 2. Stack técnico recomendado
| Pieza | Elección | Por qué |
|---|---|---|
| Framework | **Astro** + MDX | Carga muy rápida (SEO y Core Web Vitals), escribir artículos en Markdown |
| Estilos | Tailwind CSS | Rapidez y consistencia |
| Hosting | **Vercel** o Cloudflare Pages | Gratis, CDN global, HTTPS |
| Dominio | `eldatodeldia.com` / `.lat` / `.co` (~10–15 USD/año) | AdSense exige dominio propio |
| Analítica | Google Analytics 4 + Search Console | Medir tráfico por video |
| Contenido | Archivos MDX en el repo (más adelante un CMS como Decap o Sanity) | Sin coste y sin base de datos |

## 3. Estructura del sitio
- **Inicio**: "Dato de hoy" destacado, últimos datos y categorías.
- **Artículo** (`/datos/[slug]`): video de TikTok incrustado, desarrollo, fuentes, "¿Sabías también…?" y 3–6 datos relacionados.
- **Categorías**: Historia, Ciencia, Animales, Cuerpo humano, Espacio, Geografía, Tecnología…
- **Buscador** (Pagefind, estático y gratuito).
- **Páginas obligatorias para AdSense**: Sobre nosotros, Contacto, Política de privacidad, Términos, Política de cookies.
- **Aviso de cookies/consentimiento** (Google exige una CMP certificada para visitantes de la UE/Reino Unido).
- **"Link en bio"**: una página `/tiktok` optimizada para móvil con los últimos datos y un buscador ("busca el dato del video").

## 4. Estrategia TikTok → web (clave para la monetización)
1. Cada video termina con **"la historia completa está en el link de mi perfil"** y un código corto (ej. "Dato #127").
2. La página `/tiktok` permite buscar por número o palabra clave.
3. En el artículo, el primer párrafo contesta lo del video y enseguida abre una pregunta nueva ("pero lo más raro es…") para que la gente siga leyendo.
4. Enlazado interno fuerte: más páginas vistas por visita = más ingresos.
5. Newsletter semanal ("Los 5 datos de la semana") para tener tráfico recurrente que no dependa de TikTok.

> Ojo: el tráfico de TikTok es 90 % móvil y suele tener un RPM bajo. El **SEO de Google** es lo que multiplica los ingresos a largo plazo, así que cada artículo se escribe también para responder búsquedas ("¿por qué los flamencos son rosas?").

## 5. Requisitos de Google AdSense
- **Contenido original y extenso**: mínimo 20–30 artículos de 800–1500 palabras antes de solicitar.
- Nada de texto copiado ni generado en masa sin revisión (Google lo penaliza).
- Navegación clara, páginas legales, sitio rápido y apto para móvil.
- Colocación de anuncios: uno tras la introducción, otros en medio del texto, uno al final y un sticky en móvil. Hay que reservar su espacio para no romper el diseño (CLS).
- A futuro: Ezoic o Mediavine/Raptive (desde ~50k sesiones al mes), que pagan 2–4 veces más que AdSense.

## 6. Diseño
- Identidad: logo, paleta, tipografía editorial (serif para titulares, sans para el texto) y un "sello" visual para el número del dato.
- Lectura cómoda en móvil: 18px, líneas cortas, imágenes grandes.
- Microinteracciones sutiles (estilo Emil Kowalski): transiciones de página, hover en tarjetas y animación al revelar el dato.
- Revisión con Impeccable: jerarquía, espaciado, contraste y accesibilidad.
- Imágenes: propias, de Unsplash/Wikimedia (con licencia) o generadas. Imagen OG automática para compartir.

## 7. SEO técnico
Sitemap, robots.txt, datos estructurados (`Article` y `FAQPage`), meta y OG por artículo, URLs limpias, imágenes WebP/AVIF, Lighthouse > 90.

## 8. Fases
| Fase | Semana | Entregable |
|---|---|---|
| 0. Preparación | 1 | Dominio, marca, lista de los 30 primeros datos, instalar skills |
| 1. MVP | 1–2 | Sitio Astro: inicio, artículo, categorías, páginas legales, deploy en Vercel |
| 2. Contenido | 2–5 | 30 artículos profundos + `/tiktok` + link en bio |
| 3. Analítica y SEO | 3 | GA4, Search Console, sitemap, schema |
| 4. AdSense | 5–6 | Solicitud, CMP, ubicación de anuncios |
| 5. Crecimiento | continuo | 3–5 artículos por semana, newsletter, A/B de ubicaciones, pasar a Ezoic/Mediavine |

## 9. Métricas
Visitas desde TikTok por video, páginas por sesión (objetivo > 2), tiempo en página, RPM, crecimiento orgánico en Search Console.
