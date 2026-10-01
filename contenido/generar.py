"""Genera los artículos MDX de cada carrusel.

Une dos fuentes:
- src/data/carruseles.json: los textos exactos de las imágenes (titular y gancho).
- contenido/articulos/*.txt: la explicación de cada dato, escrita a mano.

Formato de cada carrusel en los .txt:

    =002 espacio
    Párrafo de introducción.
    10: Explicación del dato 10.
    ...
    1: Explicación del dato 1.
    ? Pregunta frecuente | Respuesta
    + Título de la fuente | https://url

Uso: python3 contenido/generar.py
"""
import glob, html, json, os, re, unicodedata, urllib.parse

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DESTINO = os.path.join(RAIZ, 'src/content/datos')
FECHA = '2026-09-29'


def slug(t):
    t = unicodedata.normalize('NFD', t.lower())
    t = ''.join(c for c in t if unicodedata.category(c) != 'Mn')
    t = re.sub(r'[^a-z0-9]+', '-', t).strip('-')
    return t[:70].rstrip('-')


def q(t):
    return json.dumps(t, ensure_ascii=False)


def imagen(l):
    """'! foto.jpg | descripción' -> <figure>. Si la foto no existe, avisa y no la pone."""
    archivo, _, texto = l[1:].partition('|')
    archivo, texto = archivo.strip(), texto.strip()
    if not os.path.isfile(os.path.join(RAIZ, 'public/imagenes', archivo)):
        print(f'AVISO: no encuentro public/imagenes/{archivo}; la imagen no se muestra')
        return None
    alt = html.escape(texto, quote=True)
    pie = f'<figcaption>{html.escape(texto)}</figcaption>' if texto else ''
    return (f'<figure class="foto"><img src="/imagenes/{urllib.parse.quote(archivo)}" alt="{alt}" '
            f'loading="lazy" decoding="async" />{pie}</figure>')


def leer_articulos():
    arts, cur, dato = {}, None, None
    for f in sorted(glob.glob(os.path.join(RAIZ, 'contenido/articulos/*.txt'))):
        for linea in open(f, encoding='utf-8'):
            l = linea.strip()
            if not l:
                continue
            if l.startswith('='):
                num, cat = l[1:].split()
                cur = arts[int(num)] = {'cat': cat, 'intro': [], 'datos': {}, 'faq': [], 'src': []}
                dato = None
            elif l.startswith('!'):
                fig = imagen(l)
                if fig and dato is not None:
                    cur['datos'][dato] += '\n\n' + fig
                elif fig:
                    cur['intro'].append(fig)
            elif l.startswith('?'):
                p, r = l[1:].split('|', 1)
                cur['faq'].append((p.strip(), r.strip()))
            elif l.startswith('+'):
                t, u = l[1:].rsplit('|', 1)
                cur['src'].append((t.strip(), u.strip()))
            elif re.match(r'^\d+:', l):
                n, txt = l.split(':', 1)
                dato = int(n)
                cur['datos'][dato] = txt.strip()
            elif l.startswith('»'):
                cur['datos'][dato] += '\n\n<p class="why"><strong>Por qué importa.</strong> ' + l[1:].strip() + '</p>'
            elif dato is not None:
                cur['datos'][dato] += '\n\n' + l
            else:
                cur['intro'].append(l)
    return arts


def main():
    carr = {c['n']: c for c in json.load(open(os.path.join(RAIZ, 'src/data/carruseles.json'), encoding='utf-8'))}
    arts = leer_articulos()
    for n, a in sorted(arts.items()):
        c = carr[n]
        faltan = [d['n'] for d in c['datos'] if d['n'] not in a['datos']]
        assert not faltan, f'Carrusel {n}: faltan los datos {faltan}'
        titulo = c['titulo'][0].upper() + c['titulo'][1:]
        nombres = [d['titular'] for d in c['datos'][:2]]
        desc = f'{titulo}: {nombres[0]}. Y 9 datos más, explicados a fondo y con fuentes.'
        if len(desc) > 160:
            desc = f'{titulo}. Los 10 datos del carrusel explicados a fondo y con fuentes.'
        num = f'{n:03d}'
        fm = ['---', f'numero: {n}', f'title: {q(titulo)}', f'description: {q(desc)}', f'hook: {q(c["gancho"])}',
              f'category: {a["cat"]}', f'date: {FECHA}', 'slides:']
        for d in c['datos']:
            fm.append(f'  - {{ n: {d["n"]}, id: "dato-{d["n"]}", titulo: {q(d["titular"])}, gancho: {q(d["gancho"])} }}')
        if a['faq']:
            fm.append('faq:')
            for p, r in a['faq']:
                fm += [f'  - q: {q(p)}', f'    a: {q(r)}']
        if a['src']:
            fm.append('sources:')
            for t, u in a['src']:
                fm += [f'  - title: {q(t)}', f'    url: {q(u)}']
        fm.append('---')
        cuerpo = ['\n\n'.join(a['intro']), '']
        for i, d in enumerate(c['datos']):
            cuerpo.append(f'<h2 id="dato-{d["n"]}"><span class="n">DATO {d["n"]}</span>{d["titular"]}</h2>\n')
            cuerpo.append(a['datos'][d['n']] + '\n')
            if i == 4:
                cuerpo.append('<Ad />\n')
        cuerpo.append('## Resumen de los 10 datos\n')
        cuerpo += [f'{d["n"]}. **{d["titular"]}.**' for d in sorted(c['datos'], key=lambda x: x['n'])]
        cuerpo.append(f'\n> ¿Viste este carrusel en TikTok? Es el **Dato #{num}**. Cuéntanos en los comentarios cuál te sorprendió más.')
        nombre = f'{num}-{slug(c["titulo"])}.mdx'
        for viejo in glob.glob(os.path.join(DESTINO, f'{num}-*.mdx')):
            os.remove(viejo)
        with open(os.path.join(DESTINO, nombre), 'w', encoding='utf-8') as f:
            f.write('\n'.join(fm) + '\n\n' + '\n'.join(cuerpo) + '\n')
    print(f'{len(arts)} artículos generados')


if __name__ == '__main__':
    main()
