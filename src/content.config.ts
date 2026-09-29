import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';
import { CATEGORIES } from './config';

const datos = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/datos' }),
  schema: z.object({
    numero: z.number(), // "Dato #127" que se menciona en el video
    title: z.string(),
    description: z.string(), // 150-160 caracteres, sale en Google
    hook: z.string(), // la frase corta del video
    category: z.enum(Object.keys(CATEGORIES) as [string, ...string[]]),
    date: z.coerce.date(),
    tiktokUrl: z.string().url().optional(),
    tiktokId: z.string().optional(), // número final del link del video
    faq: z.array(z.object({ q: z.string(), a: z.string() })).default([]),
    sources: z.array(z.object({ title: z.string(), url: z.string().url() })).default([]),
  }),
});

export const collections = { datos };
