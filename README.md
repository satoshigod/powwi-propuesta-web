# Propuesta de rediseño del sitio web de Powwi

Prototipo navegable para la Junta Directiva de Pagos GDE S.A. **No es el sitio oficial de Powwi.**
No captura datos: los formularios son de muestra y están desactivados, y los botones de acceso,
las tiendas y los documentos abren powwi.co. Lo que depende de validación de Powwi está marcado
como pendiente.

## Qué hay aquí

| Ruta | Contenido |
| --- | --- |
| `build.py` | Genera el sitio a partir de `content/` y `src/`. |
| `content/` | Las 48 páginas, agrupadas por público (personas, empresas, divisas, instituciones, ayuda, legal, inglés) y la propuesta para la Junta. |
| `src/` | Hoja de estilos (`calma.css`) y guion (`site.js`). |
| `fonts/` | Figtree, con licencia SIL Open Font License. |
| rama `gh-pages` | El sitio ya generado. Es lo que publica GitHub Pages. |

## Generar

```bash
python3 build.py
```

Deja `dist/sitio/` (páginas separadas, lo que va a `gh-pages`) y `dist/Propuesta_Powwi.html`
(el mismo sitio en un solo archivo). El generador revisa que no haya enlaces internos rotos.

## Publicar un cambio

1. Editar `content/` o `src/` y volver a generar.
2. Reemplazar el contenido de la rama `gh-pages` por el de `dist/sitio/`.
