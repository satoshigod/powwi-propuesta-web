from .base import *  # noqa: F401,F403
from .base import PAGES
from .datos import CANALES

hero = f'''<section class="hero-home"><div class="wrap hh"><div>
<h1>Depósitos, pagos y divisas en una sola entidad financiera</h1>
<p class="lead">Powwi es la marca de Pagos GDE S.A., entidad vigilada por la Superintendencia Financiera de Colombia.</p>
{acts(btn("/personas/descarga-la-app.html", "Abre tu Powwi"), btn("/instituciones/index.html", "Conoce la entidad", "line"))}
</div><div class="hero-art" aria-hidden="true"><i class="c1"></i><i class="c2"></i></div></div></section>
<div class="trust"><div class="wrap"><ul>
<li>Sociedad Especializada en Depósitos y Pagos Electrónicos</li><li>Depósitos con seguro de Fogafín</li>
<li>Intermediario del Mercado Cambiario</li><li>NIT 901.077.411-3</li></ul></div></div>'''


def door(title, text, href, label):
    return f'<article class="door"><h3>{title}</h3><p>{text}</p><a class="more" href="{href}">{label}</a></article>'


doors = '<div class="doors">' + "".join([
    door("Personas", "Abre tu depósito desde el celular y úsalo para recibir, enviar, pagar y ahorrar.", "/personas/index.html", "Ver Personas"),
    door("Empresas", "Recauda, dispersa y paga desde un depósito para tu negocio, o integra los servicios de Powwi a tu plataforma.", "/empresas/index.html", "Ver Empresas"),
    door("Divisas", "Operaciones de cambio con un Intermediario del Mercado Cambiario.", "/divisas/index.html", "Ver Divisas"),
    door("Instituciones financieras y aliados", "La información que necesita un banco, un aliado o un regulador para conocer a la entidad.", "/instituciones/index.html", "Ver el perfil institucional"),
]) + "</div>"

lineas = cols2(
    linea("Depósitos y pagos electrónicos",
          p("Como SEDPE, Powwi recibe recursos del público en depósitos electrónicos y presta servicios de pagos, transferencias y giros. No otorga crédito.")
          + p(a("/personas/index.html", "Personas") + " y " + a("/empresas/index.html", "Empresas"))),
    linea("Divisas",
          p("Como Intermediario del Mercado Cambiario, Powwi realiza operaciones de cambio dentro del régimen cambiario colombiano.")
          + p(a("/divisas/index.html", "La línea de divisas"))),
)


def uso(href, title, text):
    return f'<div class="uso"><h3><a href="{href}">{title}</a></h3><p>{text}</p></div>'


usos = '<div class="cols-4">' + "".join([
    uso("/personas/bre-b.html", "Bre-B", "Envía y recibe al instante con tu llave."),
    uso("/personas/recargas-y-retiros.html", "Recargas y retiros", "Por PSE o en efectivo, en la red de corresponsales."),
    uso("/personas/pagos.html", "Pagos", "Facturas, recargas a celular y contenido digital."),
    uso("/personas/remesas.html", "Remesas", "Giros internacionales directo a tu Powwi."),
]) + "</div>"

ayuda = split(
    ll([
        ("/ayuda/index.html", "Centro de ayuda", "Respuestas por tema y lo urgente primero."),
        ("/ayuda/puntos.html", "Puntos corresponsales", "Dónde recargar y retirar en efectivo."),
        ("/ayuda/contacto.html", "Peticiones, quejas y reclamos", "Canales y tiempos de respuesta."),
    ]),
    ficha("Canales de atención", CANALES, tag="h3"),
)

body = (
    hero
    + sec("¿A qué vienes hoy?", doors)
    + sec("Dos líneas, una entidad", lineas, "Powwi presta dos tipos de servicios regulados bajo una misma sociedad.", tone="sec-tint")
    + sec("Tan sencillo como el efectivo", usos, "Lo que más se hace con Powwi desde el celular.")
    + sec("¿Necesitas ayuda?", ayuda, tone="sec-tint")
)

page("index.html",
     title="Powwi: depósitos, pagos electrónicos y divisas | Pagos GDE S.A.",
     desc="Powwi es la marca de Pagos GDE S.A., entidad vigilada por la Superintendencia Financiera de Colombia. Depósitos electrónicos, pagos con Bre-B, soluciones para empresas y divisas.",
     sec="inicio", reg="cercano", body=body, canon="/", alt="/en/index.html",
     mejoras=[
         ("La página de inicio reúne la presentación institucional, tres depósitos, las tarifas en imagen, doce botones de servicios y la ayuda.",
          "Una idea por pantalla: quién es Powwi, cuatro entradas por público, sus dos líneas y la ayuda."),
         ("No menciona la línea IMC.", "La condición de IMC está en la primera pantalla y tiene sección propia."),
         ("La denominación legal solo aparece en el pie de página.", "Denominación y supervisor en la primera frase; tipo de entidad, seguro de depósitos, condición de IMC y NIT en una línea bajo la portada."),
         ("Los botones de servicios son imágenes sin texto alternativo, y la recarga de cuentas de apuestas está entre los destacados.",
          "Cuatro servicios en texto. Los demás viven en su sección."),
         ("El título de la página es “Inicio - Powwi”.", "Título y descripción propios, y datos estructurados de la organización con la denominación legal."),
     ])

PAGES["index.html"]["jsonld"] = {
    "@context": "https://schema.org", "@type": "FinancialService", "name": "Powwi", "legalName": "Pagos GDE S.A.",
    "taxID": "901.077.411-3", "url": "https://powwi.co/", "email": "escribenos@powwi.co", "telephone": "+57 601 403 0555",
    "address": {"@type": "PostalAddress", "streetAddress": "Ac. 26 # 69D-91, piso 9", "addressLocality": "Bogotá", "addressCountry": "CO"},
    "sameAs": ["https://www.linkedin.com/company/powwico/", "https://www.facebook.com/PowwiCo", "https://www.instagram.com/PowwiCo/"],
}

page("404.html", title="Página no encontrada | Powwi", desc="La página que buscas no existe o cambió de dirección. Estas son las entradas principales del sitio.",
     sec="inicio", reg="cercano",
     body=phero("No encontramos esa página", "Puede que la dirección haya cambiado. Estas son las entradas principales del sitio.",
                acts(btn("/index.html", "Ir al inicio"), btn("/ayuda/index.html", "Ir a Ayuda", "line"))))
