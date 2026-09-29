import { getCollection } from 'astro:content';

export async function getDatos() {
  const all = await getCollection('datos', ({ data }) => data.date <= new Date());
  return all.sort((a, b) => b.data.date.getTime() - a.data.date.getTime() || a.data.numero - b.data.numero);
}

export function readingTime(text = '') {
  return Math.max(1, Math.round(text.split(/\s+/).length / 220));
}
