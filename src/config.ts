// Configuración central del sitio. Rellena los valores marcados con TODO.
export const SITE = {
  name: 'El Dato del Día',
  tagline: 'Del video de 60 segundos a la historia completa.',
  description:
    'Datos curiosos de ciencia, historia, animales y el universo, explicados a fondo. La versión completa de los videos de El Dato del Día en TikTok.',
  tiktok: 'https://www.tiktok.com/@eldatodeldia03',
  tiktokHandle: '@eldatodeldia03',
  email: 'contacto@eldatodeldia.com', // TODO: tu correo de contacto
  // TODO: tu ID de AdSense (ca-pub-XXXXXXXXXXXXXXXX). Vacío = no se cargan anuncios.
  adsenseClient: 'ca-pub-9237733209875674',
  // TODO: tu ID de Google Analytics 4 (G-XXXXXXXXXX). Vacío = sin analítica.
  gaId: '',
  // Número del carrusel que se muestra como "Dato de hoy" en la portada.
  datoDeHoy: 1,
};

export const CATEGORIES: Record<string, { name: string; icon: string }> = {
  ciencia: { name: 'Ciencia', icon: 'flask-conical' },
  historia: { name: 'Historia', icon: 'landmark' },
  animales: { name: 'Animales', icon: 'paw-print' },
  'cuerpo-humano': { name: 'Cuerpo humano', icon: 'heart-pulse' },
  espacio: { name: 'Espacio', icon: 'orbit' },
  geografia: { name: 'Geografía', icon: 'globe' },
  tecnologia: { name: 'Tecnología', icon: 'cpu' },
  naturaleza: { name: 'Naturaleza', icon: 'leaf' },
  mente: { name: 'Mente', icon: 'brain' },
  comida: { name: 'Comida', icon: 'utensils' },
  cultura: { name: 'Cultura', icon: 'palette' },
  deportes: { name: 'Deportes', icon: 'trophy' },
};
