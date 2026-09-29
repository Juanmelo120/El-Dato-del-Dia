"""Prepara una copia de dist/ para verla como página privada (Artifact).

Convierte las rutas absolutas en relativas, cambia las páginas de categoría
por el buscador de la portada (index.html#categoria) y comprueba que ningún
enlace interno quede roto.
Uso: python3 contenido/preview.py DESTINO
"""
import os, re, shutil, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
dst = sys.argv[1]
shutil.rmtree(dst, ignore_errors=True)
shutil.copytree(os.path.join(RAIZ, 'dist'), dst)
shutil.rmtree(os.path.join(dst, 'categoria'))
for f in ['sitemap-index.xml', 'sitemap-0.xml', 'robots.txt', 'ads.txt', 'favicon.svg']:
    if os.path.exists(os.path.join(dst, f)):
        os.remove(os.path.join(dst, f))

def fix(path, depth):
    pre = '../' * depth or './'
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'<link rel="(icon|sitemap|canonical|alternate)"[^>]*>', '', t)

    def rep(m):
        attr, url = m.group(1), m.group(2)
        if url.startswith('//'):
            return m.group(0)
        path_, _, frag = url[1:].partition('#')
        path_ = path_.split('?')[0]
        mc = re.match(r'categoria/([^/]+)/?$', path_)
        if mc:
            return f'{attr}="{pre}index.html#{mc.group(1)}"'
        if path_ == '' or path_.endswith('/'):
            path_ += 'index.html'
        elif '.' not in os.path.basename(path_):
            path_ += '/index.html'
        return f'{attr}="{pre}{path_}' + (('#' + frag) if frag else '') + '"'

    t = re.sub(r'(href|src)="(/[^"]*)"', rep, t)
    open(path, 'w', encoding='utf-8').write(t)

htmls = []
for d, _, fs in os.walk(dst):
    for f in fs:
        if f.endswith('.html'):
            p = os.path.join(d, f)
            fix(p, os.path.relpath(p, dst).count('/'))
            htmls.append(p)

rotos = set()
for p in htmls:
    base = os.path.dirname(p)
    for u in re.findall(r'(?:href|src)="([^"#:]+)(?:#[^"]*)?"', open(p, encoding='utf-8').read()):
        if not os.path.exists(os.path.normpath(os.path.join(base, u))):
            rotos.add(u)
n = sum(len(fs) for _, _, fs in os.walk(dst))
print(f'{n} archivos, enlaces rotos: {sorted(rotos)[:20]}')
