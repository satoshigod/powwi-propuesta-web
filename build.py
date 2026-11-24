#!/usr/bin/env python3
"""Genera el prototipo en dos formatos:
   dist/sitio/                      sitio de varias páginas, listo para migrar
   dist/Propuesta_Powwi.html        archivo único navegable, para enviar
"""
import base64
import importlib
import json
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)
from content import base  # noqa: E402

MODULES = ["p_inicio", "p_propuesta", "p_sistema", "p_personas", "p_empresas", "p_divisas", "p_instituciones",
           "p_nosotros", "p_ayuda", "p_legal", "p_en"]
for m in MODULES:
    if os.path.exists(os.path.join(ROOT, "content", m + ".py")):
        importlib.import_module("content." + m)
    else:
        print("  (aún sin módulo %s)" % m)

PAGES = base.PAGES
HREF = re.compile(r'href="/([^"#]*)(?:#([^"]*))?"')
INICIO_UNICO = "propuesta/index.html"
RESERVADAS = ("settings", "sidebar", "customize", "upgrade", "downloads")


def vista(path):
    """Nombre de la vista en el archivo único: solo letras, cifras y guiones (#nombre)."""
    if path == "index.html":
        return "inicio"
    name = path[:-len(".html")]
    if name.endswith("/index"):
        name = name[:-len("/index")]
    return name.replace("/", "-")


def check_links():
    bad = []
    for path, pg in PAGES.items():
        html = base.render(path, pg)
        ids = {}
        for m in HREF.finditer(html):
            target = m.group(1) or "index.html"
            if target not in PAGES:
                bad.append((path, "/" + target))
            elif m.group(2):
                tgt_html = ids.setdefault(target, base.render(target, PAGES[target]))
                if 'id="%s"' % m.group(2) not in tgt_html:
                    bad.append((path, "/%s#%s" % (target, m.group(2))))
    return bad


def links_multi(html, current):
    d = os.path.dirname(current) or "."

    def rep(m):
        target = m.group(1) or "index.html"
        rel = os.path.relpath(target, d)
        frag = "#" + m.group(2) if m.group(2) else ""
        return 'href="%s%s"' % (rel, frag)
    return HREF.sub(rep, html)


def links_single(html):
    def rep(m):
        target = m.group(1) or "index.html"
        frag = ' data-frag="%s"' % m.group(2) if m.group(2) else ""
        return 'href="#%s" data-v%s' % (vista(target), frag)
    return HREF.sub(rep, html)


def read(name):
    with open(os.path.join(ROOT, "src", name), encoding="utf-8") as f:
        return f.read()


def build_multi():
    out = os.path.join(ROOT, "dist", "sitio")
    shutil.rmtree(out, ignore_errors=True)
    os.makedirs(os.path.join(out, "assets", "fonts"))
    css = read("calma.css").replace("__FONT_BODY__", "fonts/figtree.woff2")
    with open(os.path.join(out, "assets", "site.css"), "w", encoding="utf-8") as f:
        f.write(css)
    shutil.copy(os.path.join(ROOT, "src", "site.js"), os.path.join(out, "assets", "site.js"))
    for fn in ("figtree.woff2",):
        shutil.copy(os.path.join(ROOT, "fonts", fn), os.path.join(out, "assets", "fonts", fn))
    for path, pg in PAGES.items():
        rel = os.path.relpath(".", os.path.dirname(path) or ".")
        rel = "" if rel == "." else rel + "/"
        body = links_multi(base.render(path, pg), path)
        prod = ""
        if pg.get("canon"):
            prod = "\n<!-- Metadatos propuestos para producción: canonical https://powwi.co%s" % pg["canon"]
            if pg.get("alt"):
                prod += " | hreflang alterno %s" % pg["alt"]
            prod += " | robots index,follow -->"
        ld = ""
        if pg.get("jsonld"):
            ld = '\n<script type="application/ld+json">%s</script>' % json.dumps(pg["jsonld"], ensure_ascii=False)
        html = f'''<!DOCTYPE html>
<html lang="{pg["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{pg["title"]}</title>
<meta name="description" content="{pg["desc"]}">
<meta name="robots" content="noindex, nofollow">{prod}
<meta property="og:title" content="{pg["title"]}">
<meta property="og:description" content="{pg["desc"]}">
<meta property="og:locale" content="{"es_CO" if pg["lang"] == "es" else "en_US"}">
<link rel="stylesheet" href="{rel}assets/site.css">{ld}
</head>
<body>
{body}
<script src="{rel}assets/site.js"></script>
</body>
</html>
'''
        dest = os.path.join(out, path)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(html)
    return out


def b64(fn):
    with open(os.path.join(ROOT, "fonts", fn), "rb") as f:
        return "data:font/woff2;base64," + base64.b64encode(f.read()).decode()


def build_single():
    css = read("calma.css").replace("__FONT_BODY__", b64("figtree.woff2"))
    data = {"inicio": vista(INICIO_UNICO), "paginas": {}}
    for path, pg in PAGES.items():
        name = vista(path)
        ok = re.fullmatch(r"[a-z0-9-]+", name) and name not in RESERVADAS and not name.startswith("comment-")
        if not ok or name in data["paginas"]:
            raise SystemExit("nombre de vista no válido o repetido: %s (%s)" % (name, path))
        data["paginas"][name] = {"title": pg["title"], "lang": pg["lang"], "html": links_single(base.render(path, pg))}
    blob = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Propuesta de rediseño del sitio web de Powwi</title>
<meta name="robots" content="noindex, nofollow">
<style>{css}</style>
</head>
<body>
<div id="app"></div>
<noscript><p style="padding:2rem">Este archivo necesita JavaScript para navegar entre páginas.</p></noscript>
<script type="application/json" id="paginas">{blob}</script>
<script>{read("site.js")}</script>
</body>
</html>
'''
    dest = os.path.join(ROOT, "dist", "Propuesta_Powwi.html")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(html)
    return dest


if __name__ == "__main__":
    os.makedirs(os.path.join(ROOT, "dist"), exist_ok=True)
    bad = check_links()
    out = build_multi()
    single = build_single()
    print("páginas: %d" % len(PAGES))
    print("sitio:   %s" % out)
    print("único:   %s (%.0f KB)" % (single, os.path.getsize(single) / 1024))
    if bad:
        print("ENLACES INTERNOS ROTOS: %d" % len(bad))
        for src, tgt in sorted(set(bad)):
            print("   %s -> %s" % (src, tgt))
    else:
        print("enlaces internos: sin roturas")
