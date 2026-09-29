# Guía: instalar las skills de diseño y conectar Figma y Playwright

## 1. Skills (Impeccable, Emil Kowalski, Taste)

Una *skill* es una carpeta con un archivo `SKILL.md` y a veces otros archivos de apoyo.
Claude Code las lee de `.claude/skills/` en el repo (para todas las sesiones, incluidas las de la nube) o de `~/.claude/skills/` en tu computadora (solo en tu equipo).

### Opción A: desde GitHub en el navegador (sin programar)
1. Abre el repositorio de la skill en GitHub, por ejemplo buscando "impeccable skill claude", "emil kowalski skill" o "taste skill".
2. Busca la carpeta que contiene el archivo `SKILL.md`.
3. En **tu** repo `El-Dato-del-Dia` entra a **Add file → Create new file**.
4. Escribe como nombre `.claude/skills/impeccable/SKILL.md` (GitHub crea las carpetas solo).
5. Pega el contenido del `SKILL.md` original y haz **Commit**.
6. Si la skill trae más archivos (por ejemplo una carpeta `reference/`), créalos en la misma ruta.
7. Repite para `emil-kowalski` y `taste`.

### Opción B: con la terminal en tu computadora
```bash
git clone https://github.com/Juanmelo120/El-Dato-del-Dia.git
cd El-Dato-del-Dia
git clone <URL-del-repo-de-la-skill> /tmp/skill
cp -r /tmp/skill/<carpeta-que-tiene-SKILL.md> .claude/skills/impeccable
git add .claude/skills && git commit -m "Add design skills" && git push
```

### Opción C: como plugin en Claude Code (computadora)
Si el autor la publica como plugin, en Claude Code escribe `/plugin`, añade el marketplace del autor y elige **Install**.

**Para comprobar que funcionó:** abre una sesión nueva y escribe `/`. Deberían aparecer `impeccable`, `emil-kowalski` y `taste` en la lista.

## 2. MCP de Figma
El archivo `.mcp.json` del repo ya lo configura. Solo falta autorizarlo:
1. Abre Claude Code en este repo y acepta el servidor `figma` cuando te lo pregunte.
2. Escribe `/mcp`, elige **figma → Authenticate** e inicia sesión en Figma.
3. Pásame el link de un frame (clic derecho → *Copy link to selection*) y lo convierto en código.

Con la app de escritorio (solo en tu computadora): en Figma ve a **Preferences → Enable Dev Mode MCP Server** y luego ejecuta:
```bash
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
```

## 3. MCP de Playwright
También está en `.mcp.json`. Necesitas Node.js 18 o superior. Acéptalo cuando Claude Code lo pida y podré abrir el sitio, navegar y tomar capturas.
Si lo quieres para todos tus proyectos:
```bash
claude mcp add playwright -- npx @playwright/mcp@latest
```

## 4. Sesiones en la nube (claude.ai/code)
- Las skills del repo (`.claude/skills/`) se cargan solas.
- Los MCP que requieren iniciar sesión, como Figma, se conectan desde **claude.ai → Settings → Connectors**.
- El entorno de la nube ya trae Chromium para tomar capturas.
