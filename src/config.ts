// Configuración central del sitio. Rellena los valores marcados con TODO.
export const SITE = {
  name: 'El Dato del Día',
  tagline: 'Del video de 60 segundos a la historia completa.',
  description:
    'Datos curiosos de ciencia, historia, animales y el universo, explicados a fondo. La versión completa de los videos de El Dato del Día en TikTok.',
  tiktok: 'https://www.tiktok.com/@eldatodeldia', // TODO: confirma tu usuario
  email: 'contacto@eldatodeldia.com', // TODO: tu correo de contacto
  // TODO: tu ID de AdSense (ca-pub-XXXXXXXXXXXXXXXX). Vacío = no se cargan anuncios.
  adsenseClient: '',
  // TODO: tu ID de Google Analytics 4 (G-XXXXXXXXXX). Vacío = sin analítica.
  gaId: '',
};

export const CATEGORIES: Record<string, { name: string; emoji: string }> = {
  ciencia: { name: 'Ciencia', emoji: '🔬' },
  historia: { name: 'Historia', emoji: '🏛️' },
  animales: { name: 'Animales', emoji: '🦩' },
  'cuerpo-humano': { name: 'Cuerpo humano', emoji: '🫀' },
  espacio: { name: 'Espacio', emoji: '🪐' },
  geografia: { name: 'Geografía', emoji: '🌍' },
  tecnologia: { name: 'Tecnología', emoji: '💡' },
};
