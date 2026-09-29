#!/bin/sh
# Regenera Word, JSON y artículos; compila y comprueba que todo está bien.
set -e
cd "$(dirname "$0")/.."
python3 contenido/generar_word.py
python3 contenido/generar.py
npm run build 2>&1 | grep -E "page\(s\) built|error" 
