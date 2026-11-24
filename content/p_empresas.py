from .base import *  # noqa: F401,F403
from .datos import DOC, PORTAL_POWWI, PORTAL_BREB, ACCESO_OFICIAL, CANALES, topes_de

T = [("/index.html", "Inicio"), ("/empresas/index.html", "Empresas")]
REUNION = btn("/empresas/solicita-una-reunion.html", "Solicita una reunión")
CTA = sec("", cta("Hablemos de tu empresa", "Un asesor revisa contigo qué solución encaja y cómo se contrata.",
                  btn("/empresas/solicita-una-reunion.html", "Solicita una reunión", "light")))

page("empresas/index.html",
     title="Soluciones para empresas y aliados | Powwi",
     desc="Powwi Negocios, pagos inmediatos con Bre-B, dispersión y recaudo y Banking as a Service, con una entidad vigilada por la Superintendencia Financiera.",
     sec="empresas", reg="comercial", canon="/empresas/", alt="/en/business.html",
     body=phero("Soluciones para empresas y aliados",
                "Un depósito para tu negocio, recaudo y dispersión en los canales de Powwi, pagos inmediatos con Bre-B y servicios financieros integrados a tu plataforma.",
                acts(REUNION, btn("/empresas/acceso.html", "Acceso a portales", "line")),
                ficha("Powwi para empresas", [("Entidad", "Pagos GDE S.A."), ("Tipo", "SEDPE vigilada"), ("Depósito", "Powwi Negocios"),
                                               ("Integración", "APIs de consultas y movimientos"), ("Efectivo", "Red de corresponsales")]))
     + sec("Soluciones", ll([
         ("/empresas/powwi-negocios.html", "Powwi Negocios", "El depósito ordinario para tu empresa, sin tope de saldo ni de retiros."),
         ("/empresas/bre-b.html", "Bre-B para empresas", "Pagos inmediatos entre bancos, billeteras y depósitos, a cualquier hora."),
         ("/empresas/dispersion-y-recaudo.html", "Dispersión y recaudo", "Paga a muchos destinatarios y recauda con referencia."),
         ("/empresas/dispersion-y-recaudo.html#as-a-service", "Dispersión y recaudo as a Service", "Lo mismo, conectado a tu ERP por APIs."),
         ("/empresas/banking-as-a-service.html", "Banking as a Service", "Servicios financieros dentro de tu plataforma, con la licencia de Powwi."),
     ]), "Cada solución tiene su página, con lo que incluye, cómo se contrata y sus documentos.")
     + sec("Qué buscamos con las empresas", cols3(
         block("Menos efectivo", p("Recaudos y pagos por canales electrónicos, con el efectivo donde todavía hace falta: en la red de corresponsales.")),
         block("Más inclusión", p("Depósitos que se abren desde el celular para tus clientes, empleados y beneficiarios.")),
         block("Interoperabilidad", p("Pagos entre entidades con Bre-B y conexión con tus sistemas por APIs."))), tone="sec-tint")
     + sec("También para tu operación internacional", split(
         p("Powwi opera como Intermediario del Mercado Cambiario. Si tu empresa compra o vende divisas, conoce la línea."),
         p(a("/divisas/index.html", "Ir a Divisas"))))
     + sec("Clientes", pend("Logos y casos de clientes", p("Se publican los que Powwi confirme, con autorización de cada cliente.")), tone="sec-tint")
     + sec("Documentos", docs([
         ("Contrato de adhesión de Dispersión y recaudo", "PDF. Versión 2026.", DOC["contrato_dr"], "Abrir"),
         ("Contrato de adhesión de Dispersión y recaudo as a Service", "PDF. Versión 01.2026.", DOC["contrato_draas"], "Abrir"),
         ("Tarifas de persona jurídica", "Hoy publicadas como imagen.", "/legal/tarifas-y-topes.html", "Ver tarifas y topes"),
     ]))
     + CTA,
     mejoras=[
         ("Una sola página larga, llamada “Portal Jurídico”, que conserva el menú de personas.", "Sección propia, con menú de empresas y una página por solución."),
         ("Cuatro formularios idénticos repetidos a lo largo de la página.", "Un solo punto de contacto, conectado al formulario existente."),
         ("No menciona la línea de divisas.", "Enlace a Divisas desde la sección de empresas."),
     ])

page("empresas/powwi-negocios.html",
     title="Powwi Negocios: depósito ordinario para empresas | Powwi",
     desc="Powwi Negocios es el depósito ordinario para empresas: recaudo con referencia, transferencias masivas, pago de nómina y proveedores, Bre-B y PSE.",
     sec="empresas", reg="comercial", canon="/empresas/powwi-negocios/",
     body=phero("Powwi Negocios", "El depósito ordinario para tu empresa o negocio, sin tope de saldo ni de retiros.", acts(REUNION),
                ficha("Powwi Negocios", [("Tipo", "Depósito ordinario"), ("Saldo", "Sin límite"), ("Canal", "Portal de empresas"),
                                          ("Exención de 4×1000", "Posible hasta 350 UVT")]),
                T + [(None, "Powwi Negocios")])
     + sec("Qué puedes hacer", cols2(
         checks(["Recibir y enviar con Bre-B.", "Recaudar con referencia en corresponsales y en la app.", "Transferir a uno o a muchos destinatarios.", "Pagar nómina y proveedores."]),
         checks(["Pagar y recargar por PSE.", "Consultar saldos y movimientos.", "Asignar roles a tu equipo.", "Descargar extractos."])))
     + sec("Cómo se contrata", p("La vinculación se hace con un asesor comercial.") + acts(REUNION), tone="sec-tint")
     + sec("Topes por operación", topes_de(3, "Topes de Powwi Negocios"))
     + sec("Documentos", docs([
         ("Contrato de adhesión de Dispersión y recaudo", "PDF. Regula la creación del depósito Powwi Negocios.", DOC["contrato_dr"], "Abrir"),
         ("Reglamento del depósito de dinero electrónico", "PDF. Versión 4.", DOC["reglamento"], "Abrir"),
     ]), tone="sec-tint"),
     mejoras=[
         ("No tiene página propia: es un bloque dentro de la página de empresas.", "Página con funciones, topes, contratación y documentos."),
         ("Las preguntas frecuentes remiten a una dirección que no está en el sitemap (/powwi-para-tu-negocio/).", "Enlaces a la página vigente."),
     ])

page("empresas/bre-b.html",
     title="Bre-B para empresas: pagos interoperables | Powwi",
     desc="Recibe y envía pagos inmediatos con Bre-B desde tu depósito Powwi Negocios, a cualquier hora.",
     sec="empresas", reg="comercial", canon="/empresas/bre-b/",
     body=phero("Bre-B para empresas", "Recibe y envía pagos inmediatos entre bancos, billeteras y depósitos, a cualquier hora y todos los días.",
                acts(REUNION, btn(PORTAL_BREB, "Entrar al Portal Bre-B", "line")), trail=T + [(None, "Bre-B para empresas")])
     + sec("Cómo funciona", cols2(
         block("Pagos con llave", p("Quien paga no necesita el número de tu depósito: usa tu llave. El dinero queda disponible de inmediato.")),
         block("Portal Bre-B", p("Desde el portal administras la operación de Bre-B de tu empresa.") + p(a("/empresas/acceso.html", "Ver todos los accesos")))))
     + sec("Por confirmar", cols2(
         pend("Condiciones para persona jurídica", p("Los términos publicados de Bre-B (versión 1.0, julio de 2025) describen las funciones para persona natural. Falta el documento o la redacción que cubre a las empresas.")),
         pend("Pago con código QR", p("La página actual de empresas lo ofrece; los términos lo dan como función futura. Se publica cuando Powwi confirme que está activo."))), tone="sec-tint")
     + sec("Tope", p("El tope por envío es de $3.000.000, según Montos y topes 2026. " + a("/legal/tarifas-y-topes.html", "Ver todos los topes")))
     + CTA,
     mejoras=[
         ("Es un bloque dentro de la página de empresas, con formulario propio.", "Página propia, con el acceso al Portal Bre-B explicado."),
         ("Ofrece el código QR, que los términos del servicio dan como función futura.", "Solo se publica lo que Powwi confirme como activo."),
     ])

page("empresas/dispersion-y-recaudo.html",
     title="Dispersión y recaudo para empresas | Powwi",
     desc="Dispersa pagos a depósitos Powwi y a cuentas de otras entidades, y recauda con referencia en los canales de Powwi. También como servicio por APIs.",
     sec="empresas", reg="comercial", canon="/empresas/dispersion-y-recaudo/",
     body=phero("Dispersión y recaudo", "Paga a muchos destinatarios y recauda con referencia en los canales físicos y virtuales de Powwi.",
                acts(REUNION), trail=T + [(None, "Dispersión y recaudo")])
     + sec("Qué resuelve", cols2(
         block("Dispersión", p("Transfiere a depósitos Powwi o a cuentas de ahorros y corrientes de otras entidades, de a una operación o en lote. Sirve para nómina, proveedores y pagos a beneficiarios.")),
         block("Recaudo", p("Tus clientes pagan con un número de referencia en la red de corresponsales o en los canales virtuales. Tú sigues el recaudo con reportes en línea."))))
     + sec("Dos modalidades", table("Básico y as a Service", ["", "Básico", "As a Service"], [
         ("Dispersión individual y en lote", "Sí", "Sí"),
         ("Recaudo con referencia", "Sí", "Sí"),
         ("Reportes en línea", "Sí", "Sí"),
         ("APIs de consultas y de movimientos", "No", "Sí"),
         ("Conexión con tu ERP u otras plataformas", "No", "Sí"),
         ("Contrato", a(DOC["contrato_dr"], "Contrato de adhesión básico"), a(DOC["contrato_draas"], "Contrato de adhesión as a Service")),
     ]), "La modalidad as a Service suma APIs para seguir las operaciones desde tus propios sistemas.", id="as-a-service", tone="sec-tint")
     + sec("Por confirmar", pend("Número de puntos de recaudo", p("La página actual de empresas habla de más de 22 mil puntos y la de recargas de más de 20.000. Se publica la cifra que valide Powwi.")))
     + CTA,
     mejoras=[
         ("Dos bloques casi iguales en la misma página, cada uno con su formulario.", "Una página que compara las dos modalidades y enlaza cada contrato."),
         ("La cifra de puntos de recaudo no coincide con la de otras páginas.", "Una sola cifra, validada."),
     ])

page("empresas/banking-as-a-service.html",
     title="Banking as a Service | Powwi",
     desc="Ofrece servicios financieros dentro de tu plataforma con las APIs de Powwi. Powwi es la entidad licenciada y administra los depósitos.",
     sec="empresas", reg="comercial", canon="/empresas/banking-as-a-service/",
     body=phero("Banking as a Service", "Ofrece servicios financieros dentro de tu propia plataforma. Powwi pone la licencia y administra los depósitos; tú pones la experiencia.",
                acts(REUNION), trail=T + [(None, "Banking as a Service")])
     + sec("Cómo funciona", cols3(
         block("Tu plataforma", p("Integras las APIs de Powwi a tu aplicación o a tu ecosistema digital.")),
         block("La licencia", p("Pagos GDE S.A. es la entidad vigilada y la administradora de los depósitos de tus usuarios.")),
         block("Transparencia", p("Tus usuarios ven a Pagos GDE S.A. o a Powwi en sus extractos y en sus llaves, porque es la entidad que custodia su dinero."))))
     + sec("Qué gana tu negocio", checks(["Retención de clientes.", "Un portafolio más amplio.", "Información para decidir.", "Nuevas fuentes de ingreso."]), tone="sec-tint")
     + sec("Por confirmar", pend("Documentación técnica y casos de aliados", p("Powwi define qué se publica: documentación de las APIs, requisitos de vinculación de aliados y casos con autorización del aliado.")))
     + CTA,
     mejoras=[
         ("Es el último bloque de la página de empresas, más una entrada de blog de 2022.", "Página propia, pensada para aliados tecnológicos."),
         ("No explica quién es la entidad licenciada frente al usuario final.", "Lo dice de forma expresa."),
     ])

page("empresas/acceso.html",
     title="Acceso a portales de empresas | Powwi",
     desc="Entra al Portal Powwi, al Portal Bre-B y a la gestión de archivos de tu empresa.",
     sec="empresas", reg="comercial", canon="/empresas/acceso/",
     body=phero("Acceso a portales", "Entra a los portales de tu empresa. Estos enlaces llevan a los sistemas oficiales de Powwi: esta página no pide usuario ni contraseña.",
                trail=T + [(None, "Acceso a portales")])
     + sec("", ll([
         (PORTAL_POWWI, "Portal Powwi", "Oficina Digital Empresas: saldos, movimientos, transferencias y dispersiones."),
         (PORTAL_BREB, "Portal Bre-B", "Administración de la operación Bre-B de tu empresa."),
         (ACCESO_OFICIAL, "Gestión de archivos", "Carga y descarga de archivos de tu operación."),
     ]))
     + sec("Antes de entrar", checks(["Escribe la dirección tú mismo o entra desde esta página.", "Comprueba que la dirección empiece por https y muestre el candado.",
                                      "No entres desde redes wifi públicas.", "No guardes tus claves en el navegador.", "Cierra la sesión al terminar."]), tone="sec-tint")
     + sec("Por decidir", pend("Gestión de archivos", p("Hoy funciona sobre Google Apps Script, fuera de los dominios de Powwi. Powwi debe decidir si se mantiene así o pasa a un dominio propio."), tag="Decisión de Powwi")),
     mejoras=[
         ("Tres botones en imagen con una sigla interna sin explicar (APC).", "Cada portal con su nombre y para qué sirve."),
         ("Uno de los accesos lleva a una herramienta alojada en Google Apps Script.", "Queda señalado para decisión de Powwi."),
         ("La portada pública del Portal Powwi muestra una plantilla que ofrece crédito y habla de “la cooperativa”.", "Hallazgo reportado. Su corrección depende del proveedor del portal."),
     ])

FORM = '''<form onsubmit="return false"><fieldset class="form" disabled>
<div><label for="r-n">Nombre y apellido</label><input id="r-n" type="text" autocomplete="name"></div>
<div><label for="r-e">Correo electrónico</label><input id="r-e" type="email" autocomplete="email"></div>
<div><label for="r-t">Teléfono</label><input id="r-t" type="tel" autocomplete="tel"></div>
<div><label for="r-s">Solución de interés</label><select id="r-s"><option>Powwi Negocios</option><option>Bre-B para empresas</option><option>Dispersión y recaudo</option><option>Dispersión y recaudo as a Service</option><option>Banking as a Service</option></select></div>
<div class="full"><button class="btn btn-primary" type="button">Solicitar reunión</button></div>
</fieldset></form>'''

page("empresas/solicita-una-reunion.html",
     title="Solicita una reunión | Powwi para empresas",
     desc="Cuéntanos qué necesita tu empresa y un asesor de Powwi te contacta.",
     sec="empresas", reg="comercial", canon="/empresas/solicita-una-reunion/",
     body=phero("Solicita una reunión", "Cuéntanos qué necesita tu empresa y un asesor te contacta.", trail=T + [(None, "Solicita una reunión")])
     + sec("Datos de contacto", split(
         note(p("<strong>Formulario de muestra.</strong> En esta propuesta no envía datos. En producción se conecta al formulario actual de “Para tu empresa”, con los mismos campos."), "note-warn") + '<div class="mt">' + FORM + "</div>",
         block("O habla con nosotros", datos(CANALES)))),
     mejoras=[("Cuatro formularios idénticos en la misma página, uno por solución.", "Un formulario con selector de solución, conectado al envío existente.")])
