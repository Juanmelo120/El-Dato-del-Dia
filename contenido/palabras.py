"""Cuenta las palabras de cada dato. Uso: python3 contenido/palabras.py 1 10"""
import sys, re
sys.path.insert(0, 'contenido')
from generar import leer_articulos
a, b = int(sys.argv[1]), int(sys.argv[2])
arts = leer_articulos()
for n in range(a, b + 1):
    if n not in arts: continue
    cortos = {k: len(re.sub(r'<[^>]+>', ' ', v).split()) for k, v in arts[n]['datos'].items()}
    malos = {k: w for k, w in cortos.items() if w < 500}
    print(f'{n:03d}: min {min(cortos.values())}, total {sum(cortos.values())}' + (f'  <500: {malos}' if malos else ''))
