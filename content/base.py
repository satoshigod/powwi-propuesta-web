"""Componentes y plantilla base del prototipo. Todo enlace interno se escribe como /ruta.html
y el generador lo convierte según el modo de salida (sitio de varias páginas o archivo único)."""

OFF = "https://powwi.co"
PAGES = {}

ICONS = {
    "chev": '<path d="M9 6l6 6-6 6"/>',
    "doc": '<path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5"/><path d="M10 13h6M10 17h6"/>',
    "phone": '<path d="M6 3h4l1.5 5-2.2 1.6a12 12 0 0 0 5.1 5.1L16 12.5l5 1.5v4a2 2 0 0 1-2 2A16 16 0 0 1 4 5a2 2 0 0 1 2-2z"/>',
    "chat": '<path d="M4 5h16v11H9l-5 4z"/>',
    "mail": '<path d="M3 6h18v12H3z"/><path d="M3 7l9 6 9-6"/>',
    "pin": '<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "flag": '<path d="M5 21V4h12l-2 4 2 4H5"/>',
}


def ico(name):
    return f'<svg class="ico" viewBox="0 0 24 24" aria-hidden="true" focusable="false">{ICONS[name]}</svg>'


def off(path=""):
    """Dirección en el sitio oficial actual."""
    return OFF + path


def _ext(href):
    return href.startswith("http")


def a(href, label, cls=""):
    """Enlace en línea. Los externos se marcan y abren el sitio oficial."""
    if _ext(href):
        c = ("ext " + cls).strip()
        return f'<a class="{c}" href="{href}" rel="noopener">{label}<span class="sr"> (sitio oficial)</span></a>'
    c = f' class="{cls}"' if cls else ""
    return f'<a{c} href="{href}">{label}</a>'


def btn(href, label, kind="primary"):
    if _ext(href):
        return f'<a class="btn btn-{kind} ext" href="{href}" rel="noopener">{label}<span class="sr"> (sitio oficial)</span></a>'
    return f'<a class="btn btn-{kind}" href="{href}">{label}</a>'


def acts(*buttons):
    return '<div class="acts">' + "".join(buttons) + "</div>"


def crumbs(items):
    """items: [(href, etiqueta)], la última sin enlace."""
    parts = []
    for href, label in items:
        parts.append(f'<a href="{href}">{label}</a>' if href else f"<span>{label}</span>")
    return '<p class="crumbs">' + " / ".join(parts) + "</p>"


def phero(h1, lead, actions="", aside="", trail=None):
    c = crumbs(trail) if trail else ""
    if aside:
        inner = f'<div class="ph"><div>{c}<h1>{h1}</h1><p class="lead">{lead}</p>{actions}</div><div>{aside}</div></div>'
    else:
        inner = f'<div class="ph-solo">{c}<h1>{h1}</h1><p class="lead">{lead}</p>{actions}</div>'
    return f'<section class="phero"><div class="wrap">{inner}</div></section>'


def sec(title, body, lead=None, id=None, tone=""):
    idattr = f' id="{id}"' if id else ""
    head = ""
    if title:
        l = f"<p>{lead}</p>" if lead else ""
        head = f'<div class="sec-head"><h2>{title}</h2>{l}</div>'
    cls = ("sec " + tone).strip()
    if not title:
        cls += " sec-slim"
    return f'<section class="{cls}"{idattr}><div class="wrap">{head}{body}</div></section>'


def ficha(title, rows, foot=None, tag="h2"):
    r = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    f = f'<p class="ficha-foot">{foot}</p>' if foot else ""
    t = f"<{tag}>{title}</{tag}>" if title else ""
    return f'<div class="ficha">{t}<dl class="ld">{r}</dl>{f}</div>'


def datos(rows):
    """Lista de datos con líneas finas, sin tarjeta."""
    r = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in rows)
    return f'<dl class="ld">{r}</dl>'


def ll(items):
    out = []
    for href, title, desc in items:
        extra = ' rel="noopener"' if _ext(href) else ""
        mark = '<span class="sr"> (sitio oficial)</span>' if _ext(href) else ""
        out.append(f'<li><a href="{href}"{extra}><b>{title}{mark}</b><span>{desc}</span>{ico("chev")}</a></li>')
    return '<ul class="ll">' + "".join(out) + "</ul>"


def steps(items):
    return '<ol class="steps">' + "".join(f"<li><b>{t}</b><span>{d}</span></li>" for t, d in items) + "</ol>"


def checks(items):
    return '<ul class="checks">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def bullets(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def table(caption, head, rows, note=None, num=(), prose=False):
    th = "".join(f'<th scope="col"{" class=num" if i in num else ""}>{h}</th>' for i, h in enumerate(head))
    body = []
    for row in rows:
        cells = [f'<th scope="row">{row[0]}</th>']
        for i, c in enumerate(row[1:], start=1):
            cells.append(f'<td{" class=num" if i in num else ""}>{c}</td>')
        body.append("<tr>" + "".join(cells) + "</tr>")
    cap = f"<caption>{caption}</caption>" if caption else ""
    n = f'<p class="tbl-note">{note}</p>' if note else ""
    cls = "tbl tbl-prose" if prose else "tbl"
    return f'<div class="{cls}" role="region" aria-label="{caption or "Tabla"}" tabindex="0"><table>{cap}<thead><tr>{th}</tr></thead><tbody>{"".join(body)}</tbody></table></div>{n}'


def docs(items):
    """items: (título, metadatos, href, etiqueta de acción)"""
    out = []
    for title, meta, href, label in items:
        link = a(href, label) if href else '<span class="tag">Por entregar</span>'
        out.append(f'<li>{ico("doc")}<div><b>{title}</b><small>{meta}</small></div>{link}</li>')
    return '<ul class="docs">' + "".join(out) + "</ul>"


def pend(title, body, tag="Pendiente de insumo de Powwi"):
    return f'<div class="pend"><span class="pend-tag">{tag}</span><h3>{title}</h3>{body}</div>'


def note(body, kind=""):
    return f'<div class="note {kind}">{body}</div>'


def acc(items):
    return '<div class="acc">' + "".join(
        f'<details><summary>{q}</summary><div class="acc-b">{ans}</div></details>' for q, ans in items
    ) + "</div>"


def cta(title, text, *buttons):
    return f'<div class="cta on-dark"><div><h2>{title}</h2><p>{text}</p></div>{acts(*buttons)}</div>'


def cols2(x, y):
    return f'<div class="cols-2"><div>{x}</div><div>{y}</div></div>'


def cols3(x, y, z):
    return f'<div class="cols-3"><div>{x}</div><div>{y}</div><div>{z}</div></div>'


def split(x, y):
    return f'<div class="split"><div>{x}</div><div>{y}</div></div>'


def block(title, body):
    return f'<div class="block"><h3>{title}</h3>{body}</div>'


def panel(title, body):
    return f'<div class="panel"><h3>{title}</h3>{body}</div>'


def linea(title, body, fx=False):
    return f'<div class="linea{" linea-fx" if fx else ""}"><h3>{title}</h3>{body}</div>'


def tabs(uid, items):
    tl, panels = [], []
    for i, (label, body) in enumerate(items):
        on = i == 0
        tl.append(
            f'<button role="tab" id="{uid}-t{i}" aria-controls="{uid}-p{i}" aria-selected="{"true" if on else "false"}" tabindex="{0 if on else -1}">{label}</button>'
        )
        panels.append(f'<div role="tabpanel" id="{uid}-p{i}" aria-labelledby="{uid}-t{i}"{"" if on else " hidden"}>{body}</div>')
    return f'<div class="tabs"><div role="tablist">{"".join(tl)}</div>{"".join(panels)}</div>'


def p(*paras):
    return "".join(f"<p>{x}</p>" for x in paras)


def page(path, *, title, desc, sec, reg, body, lang="es", canon=None, alt=None, mejoras=()):
    """Registra una página. mejoras: [(hoy, en la propuesta)] para las notas de la Junta."""
    PAGES[path] = dict(title=title, desc=desc, sec=sec, reg=reg, body=body, lang=lang,
                       canon=canon, alt=alt, mejoras=list(mejoras))


# ---------- Navegación ----------
NAV = [
    ("personas", "Personas", "/personas/index.html"),
    ("empresas", "Empresas", "/empresas/index.html"),
    ("divisas", "Divisas", "/divisas/index.html"),
    ("instituciones", "Instituciones", "/instituciones/index.html"),
    ("nosotros", "Nosotros", "/nosotros/index.html"),
    ("ayuda", "Ayuda", "/ayuda/index.html"),
]
NAV_EN = [
    ("en-business", "Business", "/en/business.html"),
    ("en-fx", "Foreign exchange", "/en/fx.html"),
    ("en-inst", "Institutions", "/en/institutions.html"),
    ("en-about", "About", "/en/about.html"),
    ("en-contact", "Contact", "/en/contact.html"),
]
SUB = {
    "personas": ("Personas", [
        ("/personas/index.html", "Resumen"), ("/personas/powwi-agil.html", "Powwi Ágil"),
        ("/personas/powwi-mas.html", "Powwi Más"), ("/personas/powwi-inclusivo.html", "Powwi Inclusivo"),
        ("/personas/bre-b.html", "Bre-B"), ("/personas/enviar-dinero.html", "Enviar dinero"),
        ("/personas/recargas-y-retiros.html", "Recargas y retiros"), ("/personas/pagos.html", "Pagos"),
        ("/personas/bolsillos.html", "Bolsillos"), ("/personas/remesas.html", "Remesas"),
        ("/personas/descarga-la-app.html", "Descarga la app")]),
    "empresas": ("Empresas", [
        ("/empresas/index.html", "Resumen"), ("/empresas/powwi-negocios.html", "Powwi Negocios"),
        ("/empresas/bre-b.html", "Bre-B para empresas"), ("/empresas/dispersion-y-recaudo.html", "Dispersión y recaudo"),
        ("/empresas/banking-as-a-service.html", "Banking as a Service"),
        ("/empresas/acceso.html", "Acceso a portales"), ("/empresas/solicita-una-reunion.html", "Solicita una reunión")]),
    "divisas": ("Divisas", [
        ("/divisas/index.html", "La línea IMC"), ("/divisas/como-operar.html", "Cómo operar")]),
    "instituciones": ("Instituciones financieras y aliados", [
        ("/instituciones/index.html", "Perfil institucional"), ("/instituciones/gobierno-corporativo.html", "Gobierno corporativo"),
        ("/instituciones/cumplimiento.html", "Cumplimiento"), ("/instituciones/informacion-financiera.html", "Información financiera")]),
    "nosotros": ("Nosotros", [
        ("/nosotros/index.html", "Sobre Powwi"), ("/nosotros/educacion-financiera.html", "Educación financiera"),
        ("/nosotros/seguridad.html", "Seguridad"), ("/nosotros/noticias.html", "Noticias"),
        ("/nosotros/trabaja-con-nosotros.html", "Trabaja con nosotros")]),
    "ayuda": ("Ayuda", [
        ("/ayuda/index.html", "Centro de ayuda"), ("/ayuda/preguntas-frecuentes.html", "Preguntas frecuentes"),
        ("/ayuda/puntos.html", "Puntos corresponsales"), ("/ayuda/contacto.html", "Contacto y PQRSF")]),
    "legal": ("Legal y regulatorio", [
        ("/legal/index.html", "Centro de documentos"), ("/legal/tarifas-y-topes.html", "Tarifas, montos y topes"),
        ("/legal/consumidor-financiero.html", "Consumidor financiero")]),
    "propuesta": ("Propuesta para la Junta", [
        ("/propuesta/index.html", "Resumen y mejoras"), ("/propuesta/arquitectura.html", "Mapa del sitio"),
        ("/propuesta/sistema-de-diseno.html", "Sistema de diseño"), ("/propuesta/pendientes.html", "Decisiones e insumos")]),
}


def _nav(items, current, path):
    lis = []
    for key, label, href in items:
        cur = ' aria-current="true"' if key == current else ""
        if href == "/" + path:
            cur = ' aria-current="page"'
        lis.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    return "".join(lis)


def render(path, pg):
    es = pg["lang"] == "es"
    sec_key = pg["sec"]
    # Barra del prototipo
    if es:
        proto = ('<div class="proto"><div class="wrap proto-in"><p><strong>Propuesta de rediseño para la Junta Directiva.</strong> '
                 'No es el sitio oficial de Powwi.</p><div class="proto-links">__JUNTA__'
                 '<a href="/propuesta/index.html">Resumen de la propuesta</a></div></div></div>')
    else:
        proto = ('<div class="proto"><div class="wrap proto-in"><p><strong>Redesign proposal for the Board of Directors.</strong> '
                 'Not the official Powwi website. Draft translation.</p><div class="proto-links">__JUNTA__'
                 '<a href="/propuesta/index.html">Proposal summary (Spanish)</a></div></div></div>')
    # Cabecera
    alt = pg.get("alt")
    if es:
        en_href = alt or "/en/index.html"
        lang = f'<div class="lang" role="group" aria-label="Idioma"><a href="/{path}" aria-current="true" lang="es">ES</a><a href="{en_href}" lang="en">EN</a></div>'
        nav = _nav(NAV, sec_key, path)
        actions = (f'{lang}<a class="plain" href="/empresas/acceso.html">Acceso empresas</a>'
                   f'{btn("/personas/descarga-la-app.html", "Descarga la app")}')
        brand_href, menu_label, nav_label = "/index.html", "Menú", "Principal"
    else:
        es_href = alt or "/index.html"
        lang = f'<div class="lang" role="group" aria-label="Language"><a href="{es_href}" lang="es">ES</a><a href="/{path}" aria-current="true" lang="en">EN</a></div>'
        nav = _nav(NAV_EN, sec_key, path)
        actions = f'{lang}{btn("/en/contact.html", "Contact us")}'
        brand_href, menu_label, nav_label = "/en/index.html", "Menu", "Main"
    header = (f'<header class="hdr"><div class="wrap hdr-in"><a class="brand" href="{brand_href}">Powwi<small>Pagos GDE S.A.</small></a>'
              f'<button class="menu-btn" type="button" aria-expanded="false">{menu_label}</button>'
              f'<nav aria-label="{nav_label}"><ul class="nav">{nav}</ul></nav><div class="hdr-acts">{actions}</div></div></header>')
    # Menú de sección
    subnav = ""
    if sec_key in SUB:
        t, items = SUB[sec_key]
        lis = "".join(
            f'<li><a href="{h}"{" aria-current=page" if h == "/" + path else ""}>{l}</a></li>' for h, l in items)
        subnav = f'<nav class="subnav" aria-label="{t}"><div class="wrap subnav-in"><span class="subnav-t">{t}</span><ul>{lis}</ul></div></nav>'
    # Notas para la Junta
    junta = ""
    notas = ""
    if pg["mejoras"]:
        items = "".join(f'<div class="junta-item"><p><span>Hoy en powwi.co</span>{h}</p><p><span>En la propuesta</span>{n}</p></div>' for h, n in pg["mejoras"])
        n = len(pg["mejoras"])
        notas = (f'<details class="junta"><summary>Mejoras de esta página <span class="junta-n">{n}</span></summary>'
                 f'<div class="junta-panel"><h2>Mejoras frente al sitio actual</h2>{items}</div></details>')
    proto = proto.replace("__JUNTA__", notas)
    main = f'<main id="contenido">{pg["body"]}</main>'
    footer = FOOTER_ES if es else FOOTER_EN
    skip = '<a class="skip" href="#contenido">' + ("Ir al contenido" if es else "Skip to content") + "</a>"
    html = f'<div class="page reg-{pg["reg"]}">{skip}{proto}{header}{subnav}{junta}{main}{footer}</div>'
    return html.replace("__NPAG__", str(len(PAGES)))


FOOTER_ES = '''<footer class="ftr"><div class="wrap">
<div class="ftr-top"><a class="brand" href="/index.html">Powwi</a>
<nav class="ftr-nav" aria-label="Pie de página">
<a href="/legal/index.html">Legal y regulatorio</a><a href="/legal/tarifas-y-topes.html">Tarifas y topes</a>
<a href="/legal/consumidor-financiero.html">Consumidor financiero</a><a href="/legal/index.html#datos">Tratamiento de datos</a>
<a href="/instituciones/informacion-financiera.html">Estados financieros</a><a href="/ayuda/contacto.html">Contacto</a></nav></div>
<div class="ftr-end"><p>Pagos GDE S.A., NIT 901.077.411-3. Sociedad Especializada en Depósitos y Pagos Electrónicos. Vigilada por la Superintendencia Financiera de Colombia. Depósitos con seguro de Fogafín.</p>
<p>Prototipo de propuesta. Los documentos, portales y tiendas enlazados son los del sitio oficial.</p></div>
</div></footer>'''

FOOTER_EN = '''<footer class="ftr"><div class="wrap">
<div class="ftr-top"><a class="brand" href="/en/index.html">Powwi</a>
<nav class="ftr-nav" aria-label="Footer">
<a href="/en/institutions.html">Institutions and partners</a><a href="/en/institutions.html#financials">Financial statements</a>
<a href="/en/institutions.html#compliance">Compliance</a><a href="/legal/index.html">Legal centre (Spanish)</a>
<a href="/en/contact.html">Contact</a><a href="/index.html" lang="es">Sitio en español</a></nav></div>
<div class="ftr-end"><p>Pagos GDE S.A., tax ID (NIT) 901.077.411-3. Colombian electronic deposit and payment company (SEDPE). Supervised by the Superintendencia Financiera de Colombia. Deposits insured by Fogafín.</p>
<p>Proposal prototype. Linked documents and portals are those of the official site. Legal documents are binding in Spanish.</p></div>
</div></footer>'''
