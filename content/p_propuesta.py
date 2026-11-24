from .base import *  # noqa: F401,F403
from .base import OFF

T = [("/propuesta/index.html", "Propuesta")]


def O(path, label=None):
    return a(OFF + path, label or path)


# ---------- Portada para la Junta ----------
HALLAZGOS = [
    ("La línea IMC no aparece en ninguna página del sitio. Sí aparece en los estados financieros que el mismo sitio publica.", O("/wp-content/uploads/2026/04/Estados-Financieros-Powwi-2025.pdf", "Estados financieros 2025")),
    ("El portal de empresas muestra una portada de plantilla que ofrece crédito, invita a hacerse socio y habla de “la cooperativa”.", a("https://banking.powwi.co/odigemp/", "banking.powwi.co/odigemp")),
    ("En el dominio está alojado un documento de términos y condiciones de Buda.com, una casa de cambio de criptomonedas.", O("/wp-content/uploads/2022/03/Terminos-y-condiciones.pdf", "Documento")),
    ("La fecha de la autorización de funcionamiento no coincide: 26 de julio de 2017 en “Sobre nosotros” y 25 de julio de 2018 en los estados financieros y los contratos.", O("/sobre-nosotros/")),
    ("Hay páginas de prueba publicadas y dentro del sitemap: la página de ejemplo de WordPress, dos avisos de mantenimiento y una con un código sin procesar.", O("/sample-page/") + ", " + O("/mantenimiento/") + ", " + O("/book-now/")),
    ("“Trabaja con nosotros” lleva a una dirección privada de LinkedIn que no muestra vacantes.", "Pie de todas las páginas"),
    ("No hay sección de accionistas, junta directiva ni directivos. La historia de la entidad termina en 2019.", O("/sobre-nosotros/")),
    ("No hay versión en inglés.", "Todo el sitio"),
    ("La página del consumidor financiero no trae los datos del Defensor. Su correo solo está en “Llámanos”.", O("/consumidor-financiero/")),
    ("Las preguntas frecuentes están desactualizadas: dan el tope de Powwi Ágil de 2025 y enlazan tarifas y topes de 2022.", O("/preguntas-frecuentes/")),
    ("Dos cifras de puntos y dos listas de redes aliadas: más de 20.000 puntos en una página y más de 22.000 en otra.", O("/recarga-tu-powwi-2/") + ", " + O("/puntos-de-ubicacion/")),
    ("Las tarifas se publican como imagen, y existe una segunda página de tarifas titulada 2022.", O("/tarifas-2022/")),
    ("La política de datos publicada deja ver una ruta interna de archivos y una dirección distinta de la del pie del sitio.", O("/politica-de-tratamiento-de-datos/")),
    ("La recarga de cuentas de apuestas está entre los servicios destacados del inicio, sin operadores, condiciones ni avisos.", O("/apuestas/")),
    ("Bre-B se explica dentro de la página de Transfiya.", O("/transfiya/")),
]

MEJORAS = [
    ("Una entrada por público",
     "Una sola experiencia para todos: el mismo inicio, el mismo menú y el mismo pie. De las 40 páginas, 16 son para personas, 2 para empresas y ninguna para divisas o para instituciones financieras.",
     "Seis públicos con entrada, menú de sección, tono y acción propios. El inicio presenta a la entidad y distribuye.", "/index.html", "Ver el inicio"),
    ("La línea de divisas existe",
     "Ninguna mención de la línea IMC en el sitio.",
     "Sección Divisas en el menú principal, con la estructura lista para el contenido que valide Powwi. Sin texto inventado.", "/divisas/index.html", "Ver Divisas"),
    ("Un expediente para bancos y aliados",
     "Dos certificaciones y un PDF de estados financieros, enlazados desde el pie.",
     "Perfil institucional, gobierno corporativo, cumplimiento e información financiera, en español y en inglés.", "/instituciones/index.html", "Ver Instituciones"),
    ("Bre-B con sección propia",
     "El contenido de Bre-B vive en la página de Transfiya.",
     "Una página de Bre-B para personas y otra para empresas, con llaves, costo y topes.", "/personas/bre-b.html", "Ver Bre-B"),
    ("Cada depósito con su página",
     "Powwi Ágil, Powwi Más y Powwi Inclusivo se explican dentro de la página de inicio.",
     "Una página por depósito y una tabla que los compara, con los topes en texto.", "/personas/index.html#depositos", "Ver los depósitos"),
    ("Todos los servicios, ordenados por tarea",
     "Doce botones en imagen con el mismo peso; páginas duplicadas y vacías.",
     "Los servicios vigentes agrupados por lo que la persona quiere hacer: recibir y enviar, meter y sacar plata, pagar, ahorrar.", "/personas/index.html", "Ver Personas"),
    ("Empresas con sección propia",
     "Una página larga, llamada “Portal Jurídico”, que conserva el menú de personas y repite cuatro formularios.",
     "Menú de empresas, una página por solución y los accesos a portales explicados.", "/empresas/index.html", "Ver Empresas"),
    ("Tarifas y topes en texto",
     "Tarifas en imágenes PNG, topes en un PDF y una página titulada 2022.",
     "Topes en tabla, legibles en el celular, y una sola página de tarifas y topes.", "/legal/tarifas-y-topes.html", "Ver tarifas y topes"),
    ("Centro legal y regulatorio",
     "Nueve enlaces en el pie de todas las páginas, sin formato, versión ni fecha.",
     "Centro de documentos por categoría. Cada sección enlaza solo los suyos.", "/legal/index.html", "Ver el centro legal"),
    ("Ayuda por tarea",
     "74 preguntas en una sola lista, con datos de 2022 y 2025. Contacto repartido en dos páginas.",
     "Centro de ayuda con lo urgente arriba, preguntas por tema, canales, horario y tiempos de respuesta.", "/ayuda/index.html", "Ver Ayuda"),
    ("Identidad y sistema de diseño",
     "Sin sistema: muchos elementos por pantalla, botones en imagen y estilos distintos entre páginas.",
     "Fondo blanco, el azul actual como único acento, una sola familia tipográfica y componentes documentados.", "/propuesta/sistema-de-diseno.html", "Ver el sistema de diseño"),
    ("Direcciones limpias y contenido saneado",
     "Páginas de prueba en el sitemap, direcciones duplicadas y enlaces truncados.",
     "Mapa de cada página actual a su nueva ubicación, con su redirección.", "/propuesta/arquitectura.html", "Ver el mapa del sitio"),
]

mej_html = '<ol class="mejoras">' + "".join(
    f'<li><h3>{t}</h3><p class="hoy"><span class="lbl">Hoy en powwi.co</span>{hoy}</p><p class="prop"><span class="lbl">En la propuesta</span>{prop}</p><p class="ver">{a(href, label)}</p></li>'
    for t, hoy, prop, href, label in MEJORAS) + "</ol>"

hall_html = table("Lo que encuentra hoy un banco al revisar powwi.co", ["Hallazgo", "Dónde verlo"], HALLAZGOS, prose=True,
                  note="Verificado sobre el sitio público el 24 de noviembre de 2026. Los enlaces abren el sitio oficial.")

page("propuesta/index.html",
     title="Propuesta de rediseño del sitio web de Powwi",
     desc="Propuesta navegable de rediseño de powwi.co para la Junta Directiva: mejoras frente al sitio actual, mapa del sitio, sistema de diseño y decisiones pendientes.",
     sec="propuesta", reg="inst",
     body=phero("Propuesta de rediseño del sitio web de Powwi",
                "Un sitio navegable que muestra cómo quedaría powwi.co: una entrada por público, la línea de divisas visible, la información que pide un banco corresponsal y todos los servicios vigentes. No modifica el sitio actual ni sus sistemas.",
                acts(btn("/index.html", "Entrar al sitio propuesto", "light"), btn("/propuesta/index.html#mejoras", "Ver las mejoras", "ghost")),
                ficha("Qué contiene", [("Páginas del prototipo", "__NPAG__"), ("Públicos con entrada propia", "6"), ("Mejoras principales", str(len(MEJORAS))),
                                       ("Hallazgos del sitio actual", str(len(HALLAZGOS))), ("Verificado", "24 de noviembre de 2026")]))
     + sec("Por qué ahora", split(
         p("Un banco de Estados Unidos, contactado para abrir cuentas de corresponsalía, revisó powwi.co y lo describió como “crudo”. Esas cuentas sostienen la operación en dólares de la línea IMC.",
           "Para un banco, el sitio web es la primera pieza de la debida diligencia. Antes de cualquier reunión busca quién es la entidad, quién la vigila, quiénes son sus dueños y directivos, cómo previene el lavado de activos y dónde están sus estados financieros. Si no lo encuentra en minutos, no avanza.",
           "Al banco se le informó que Powwi está rediseñando su sitio. Hay que asumir que volverá a mirarlo."),
         block("Lo que busca un banco", checks(["Denominación legal y tipo de entidad.", "Quién la autoriza y la vigila.", "Accionistas y directivos.", "Líneas de negocio.",
                                               "Prevención de lavado de activos.", "Estados financieros auditados.", "Contacto de cumplimiento."]))))
     + sec("Qué encuentra hoy", hall_html, tone="sec-tint")
     + sec("Las mejoras", mej_html, "Doce cambios, cada uno con lo que hay hoy y lo que propone el prototipo. En cada página del sitio propuesto, el botón «Mejoras de esta página» de la barra superior muestra además lo que cambia en esa página.", id="mejoras")
     + sec("Lo que no cambia", cols2(
         checks(["Los sistemas transaccionales, las APIs y los portales de empresas.", "El contenido jurídico de reglamentos, contratos y políticas: se enlazan, no se reescriben.",
                 "Las integraciones existentes: formularios, chat y pasarelas."]),
         checks(["Las direcciones actuales: cada una se conserva o se redirige.", "Las cifras y afirmaciones regulatorias: solo se publica lo que valide Powwi.",
                 "El nombre y la marca: la propuesta es del sitio, no de la denominación."])), tone="sec-tint")
     + sec("Lo urgente no necesita esperar al rediseño", checks([
         "Despublicar las páginas de prueba y de mantenimiento y sacarlas del sitemap.",
         "Corregir el enlace de “Trabaja con nosotros”.",
         "Actualizar el año del copyright y retirar del pie el enlace promocional de la agencia.",
         "Decidir qué hacer con el documento de Buda.com alojado en el dominio.",
         "Corregir la fecha de la autorización de funcionamiento en “Sobre nosotros”.",
         "Pedir al proveedor del portal de empresas que retire la portada de plantilla.",
         "Unificar las cifras de puntos, convenios y países.",
         "Actualizar las preguntas frecuentes con los topes y enlaces vigentes.",
     ]) + p(a("/propuesta/pendientes.html", "Ver decisiones e insumos que se necesitan de Powwi")), "Ocho correcciones que se pueden hacer en días sobre el sitio actual.")
     + sec("Cómo recorrer el sitio propuesto", cols2(
         ll([("/index.html", "Inicio", "La entidad y una puerta por público."), ("/personas/index.html", "Personas", "Depósitos y servicios por tarea."),
             ("/empresas/index.html", "Empresas", "Una página por solución."), ("/divisas/index.html", "Divisas", "La línea IMC.")]),
         ll([("/instituciones/index.html", "Instituciones financieras y aliados", "El expediente para la debida diligencia."), ("/ayuda/index.html", "Ayuda", "Por tarea, con lo urgente arriba."),
             ("/legal/index.html", "Legal y regulatorio", "Documentos con formato y versión."), ("/en/index.html", "Versión en inglés", "Borrador de la capa institucional.")])), tone="sec-tint")
     + sec("Qué falta para publicarlo", cols3(
         block("Contenido que valida Powwi", p("Operaciones de la línea IMC, gobierno corporativo, documentos de cumplimiento, tarifas en texto y traducción al inglés. En el prototipo están marcados como pendientes.")),
         block("Decisiones", p("Qué hacer con Transfiya, con la recarga de cuentas de apuestas, con el contenido heredado y con la herramienta de gestión de archivos.")),
         block("Accesos", p("Administrador del sitio actual, hosting y un ambiente de pruebas. Con ellos el prototipo se lleva al gestor de contenidos de Powwi.")))))

# ---------- Mapa del sitio ----------
R = "Redirección 301"
MAPA = [
    ("/", "Todos", "/index.html", "/", "Se conserva"),
    ("/sample-page/", "Ninguno", None, "", "Retirar y sacar del sitemap"),
    ("/mantenimiento/", "Ninguno", None, "", "Retirar y sacar del sitemap"),
    ("/book-now/", "Ninguno", None, "", "Retirar y sacar del sitemap"),
    ("/mantenimiento-powwi/", "Ninguno", None, "", "Retirar y sacar del sitemap"),
    ("/politica-de-cookies/", "Legal", "/legal/index.html#datos", "/politica-de-cookies/", "Se conserva"),
    ("/escribenos/", "Ayuda", "/ayuda/contacto.html", "/ayuda/contacto/", R),
    ("/encuesta_powwi/", "Ayuda", None, "", "Decisión de Powwi: retirar o actualizar"),
    ("/noticias/", "Corporativo", "/nosotros/noticias.html", "/nosotros/noticias/", R),
    ("/remesas/", "Personas", "/personas/remesas.html", "/personas/remesas/", R + " (duplicada)"),
    ("/envia-en-linea/", "Personas", "/personas/enviar-dinero.html#retiro-en-corresponsal", "/personas/enviar-dinero/", R + " (vacía)"),
    ("/pago-de-facturas/", "Personas", "/personas/pagos.html#facturas", "/personas/pagos/", R),
    ("/contenido-digital/", "Personas", "/personas/pagos.html#contenido-digital", "/personas/pagos/", R),
    ("/apuestas/", "Personas", "/personas/pagos.html#apuestas", "/personas/pagos/", R + "; ubicación a decisión de Powwi"),
    ("/envia-dinero-a-otros-powwi/", "Personas", "/personas/enviar-dinero.html#otros-powwi", "/personas/enviar-dinero/", R + " (duplicada)"),
    ("/envia-dinero-a-otros-bancos/", "Personas", "/personas/enviar-dinero.html#otros-bancos", "/personas/enviar-dinero/", R),
    ("/bolsillos/", "Personas", "/personas/bolsillos.html", "/personas/bolsillos/", R),
    ("/descarga-tu-powwi-app/", "Personas", "/personas/descarga-la-app.html", "/personas/descarga-la-app/", R),
    ("/enviar-dinero-a-otro-powwi/", "Personas", "/personas/enviar-dinero.html#otros-powwi", "/personas/enviar-dinero/", R),
    ("/aviso-de-privacidad/", "Legal", "/legal/index.html#datos", "/aviso-de-privacidad/", "Se conserva"),
    ("/sobre-nosotros/", "Corporativo", "/nosotros/index.html", "/nosotros/", R),
    ("/recarga-tu-powwi/", "Personas", "/personas/recargas-y-retiros.html", "/personas/recargas-y-retiros/", R + " (duplicada)"),
    ("/educacion-financiera/", "Corporativo", "/nosotros/educacion-financiera.html", "/nosotros/educacion-financiera/", R),
    ("/tips-de-seguridad/", "Ayuda", "/nosotros/seguridad.html", "/nosotros/seguridad/", R),
    ("/consumidor-financiero/", "Legal", "/legal/consumidor-financiero.html", "/legal/consumidor-financiero/", R),
    ("/remesas-2/", "Personas", "/personas/remesas.html", "/personas/remesas/", R),
    ("/certificados-de-riesgos/", "Legal", "/instituciones/cumplimiento.html#certificaciones", "/instituciones/cumplimiento/", R),
    ("/tarifas-2022/", "Legal", "/legal/tarifas-y-topes.html", "/legal/tarifas-y-topes/", R),
    ("/retira-dinero/", "Personas", "/personas/recargas-y-retiros.html#retiros", "/personas/recargas-y-retiros/", R),
    ("/recarga-tu-powwi-2/", "Personas", "/personas/recargas-y-retiros.html#recargas", "/personas/recargas-y-retiros/", R),
    ("/envia-dinero-para-retirar-en-un-corresponsal/", "Personas", "/personas/enviar-dinero.html#retiro-en-corresponsal", "/personas/enviar-dinero/", R),
    ("/puntos-de-ubicacion/", "Ayuda", "/ayuda/puntos.html", "/ayuda/puntos/", R),
    ("/transfiya/", "Personas", "/personas/bre-b.html", "/personas/bre-b/", R + "; Transfiya a decisión de Powwi"),
    ("/accesoportalempresas/", "Empresas", "/empresas/acceso.html", "/empresas/acceso/", R),
    ("/puntos-de-ubicacion/nuestros-corresponsales/", "Ayuda", "/ayuda/puntos.html#departamentos", "/ayuda/puntos/", R),
    ("/llamanos/", "Ayuda", "/ayuda/contacto.html", "/ayuda/contacto/", R),
    ("/portal-juridico/", "Empresas", "/empresas/index.html", "/empresas/", R),
    ("/preguntas-frecuentes/", "Ayuda", "/ayuda/preguntas-frecuentes.html", "/ayuda/preguntas-frecuentes/", R),
    ("/politica-de-tratamiento-de-datos/", "Legal", "/legal/index.html#datos", "/politica-de-tratamiento-de-datos/", "Se conserva"),
    ("/reglamento-de-depositos/", "Legal", "/legal/index.html#productos", "/reglamento-de-depositos/", "Se conserva"),
]
mapa_rows = [(actual, pub, a(proto, nueva) if proto else "Sin página nueva", accion) for actual, pub, proto, nueva, accion in MAPA]
_cuenta = {}
for _m in MAPA:
    _cuenta[_m[1]] = _cuenta.get(_m[1], 0) + 1

NUEVAS = [
    ("/divisas/index.html", "Divisas: la línea IMC", "No existe hoy."), ("/divisas/como-operar.html", "Divisas: cómo operar", "No existe hoy."),
    ("/instituciones/index.html", "Perfil institucional", "No existe hoy."), ("/instituciones/gobierno-corporativo.html", "Gobierno corporativo", "No existe hoy."),
    ("/instituciones/cumplimiento.html", "Cumplimiento", "Hoy solo hay dos certificaciones."), ("/instituciones/informacion-financiera.html", "Información financiera", "Hoy solo hay un PDF en el pie."),
    ("/personas/powwi-agil.html", "Powwi Ágil", "Hoy se describe en el inicio."), ("/personas/powwi-mas.html", "Powwi Más", "Hoy se describe en el inicio."),
    ("/personas/powwi-inclusivo.html", "Powwi Inclusivo", "Hoy se describe en el inicio."), ("/empresas/powwi-negocios.html", "Powwi Negocios", "Hoy es un bloque de la página de empresas."),
    ("/empresas/bre-b.html", "Bre-B para empresas", "Hoy es un bloque de la página de empresas."), ("/empresas/dispersion-y-recaudo.html", "Dispersión y recaudo", "Hoy son dos bloques de la página de empresas."),
    ("/empresas/banking-as-a-service.html", "Banking as a Service", "Hoy es un bloque de la página de empresas."), ("/empresas/solicita-una-reunion.html", "Solicita una reunión", "Reemplaza cuatro formularios repetidos."),
    ("/ayuda/index.html", "Centro de ayuda", "No existe hoy."), ("/legal/index.html", "Centro legal y regulatorio", "Hoy es una lista en el pie."),
    ("/nosotros/trabaja-con-nosotros.html", "Trabaja con nosotros", "Hoy es un enlace roto."), ("/en/index.html", "Versión en inglés", "Seis páginas en borrador."),
]

page("propuesta/arquitectura.html",
     title="Mapa del sitio: de las páginas actuales a la propuesta | Powwi",
     desc="Cada página actual de powwi.co, el público al que le habla, su nueva ubicación en la propuesta y qué pasa con su dirección.",
     sec="propuesta", reg="inst",
     body=phero("Mapa del sitio", "Cada página actual, el público al que le habla hoy, su nueva ubicación y qué pasa con su dirección.", trail=T + [(None, "Mapa del sitio")])
     + sec("Las 40 páginas del sitemap actual", table("De la página actual a la propuesta", ["Página actual", "Público", "Nueva ubicación", "Qué pasa con la dirección"], mapa_rows,
           note="Resumen por público: " + ", ".join(f"{k} {v}" for k, v in _cuenta.items()) + ". Línea IMC 0. Instituciones financieras 0."),
           "Ninguna página indexada se elimina sin redirección. Las que se retiran son páginas de prueba.")
     + sec("Seis públicos, seis entradas", table("Separación por públicos", ["Público", "Qué viene a hacer", "Experiencia", "Acción principal"], [
         ("Personas", "Entender el depósito, abrirlo y usar los servicios", "Cercana, simple, pensada para el celular", "Descargar la app"),
         ("Empresas", "Evaluar recaudo, dispersión, Bre-B y Banking as a Service", "Comercial y consultiva", "Solicitar una reunión"),
         ("Clientes de divisas", "Entender la línea, sus requisitos y cómo operar", "Institucional y precisa", "Contactar al equipo de la línea"),
         ("Instituciones financieras y aliados", "Hacer debida diligencia", "Sobria y documental, en español y en inglés", "Consultar documentos y contactar a cumplimiento"),
         ("Clientes que necesitan ayuda", "Resolver un problema o encontrar un punto", "Directa, orientada a la tarea", "Autogestión y canales de atención"),
         ("Consumidor financiero y reguladores", "Encontrar la información legal y regulatoria", "Completa y ordenada, con versiones", "Consultar y descargar"),
     ]), tone="sec-tint")
     + sec("Páginas nuevas", ll(NUEVAS), "Lo que la propuesta agrega o separa.")
     + sec("Entradas del blog", p("Las cinco entradas publicadas conservan su dirección y pasan al archivo de " + a("/nosotros/noticias.html", "Noticias") + ". Powwi debe revisar su vigencia."), tone="sec-tint")
     + sec("Subdominios y propiedades externas", table("Lo que rodea al sitio", ["Propiedad", "Qué es", "En la propuesta"], [
         ("banking.powwi.co", "Oficina Digital Empresas, portal transaccional", "Se enlaza sin cambios. Su portada de plantilla depende del proveedor."),
         ("servicesapp.powwi.co", "Portal Bre-B y Taquilla PSE", "Se enlaza sin cambios."),
         ("Google Apps Script", "Gestión de archivos de empresas", "Se enlaza sin cambios. Queda a decisión de Powwi."),
         ("helpvoz.com", "Chat de atención", "Integración que se conserva al migrar."),
         ("Tiendas de aplicaciones", "Powwi App", "Se enlazan las fichas oficiales."),
         ("pagosgde.com", "Dominio citado en la política de datos", "Por revisar: no se verificó su contenido."),
     ])))

# ---------- Contraste de color (lo usa p_sistema) ----------
def _lum(hexc):
    r, g, b = (int(hexc[i:i + 2], 16) / 255 for i in (1, 3, 5))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contraste(c1, c2):
    l1, l2 = sorted((_lum(c1), _lum(c2)), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)



# ---------- Decisiones e insumos ----------
page("propuesta/pendientes.html",
     title="Decisiones e insumos que necesita la propuesta | Powwi",
     desc="Lo que Powwi debe validar, decidir y entregar para llevar la propuesta de rediseño a producción.",
     sec="propuesta", reg="inst",
     body=phero("Decisiones e insumos", "Lo que Powwi debe validar, decidir y entregar para llevar la propuesta a producción.", trail=T + [(None, "Decisiones e insumos")])
     + sec("Insumos y validaciones", table("Lo que entrega Powwi", ["Insumo", "Para qué página", "Quién"], prose=True, rows=[
         ("Redacción regulatoria aprobada: tipo de entidad, vigilancia, seguro de depósitos, condición de IMC. En español y en inglés.", "Todo el sitio", "Jurídica y cumplimiento"),
         ("Operaciones de cambio autorizadas y ofrecidas, con condiciones y tarifas.", a("/divisas/index.html", "Divisas"), "Jurídica y cumplimiento"),
         ("Catálogo de servicios vigentes, incluido el estado de Transfiya y del código QR de Bre-B.", a("/personas/index.html", "Personas") + " y " + a("/empresas/index.html", "Empresas"), "Producto"),
         ("Composición accionaria, junta directiva y directivos que se publican.", a("/instituciones/gobierno-corporativo.html", "Gobierno corporativo"), "Junta Directiva"),
         ("Documentos de cumplimiento que se publican y los que se entregan bajo solicitud.", a("/instituciones/cumplimiento.html", "Cumplimiento"), "Cumplimiento"),
         ("Estados financieros de 2023 y 2024 con sus notas.", a("/instituciones/informacion-financiera.html", "Información financiera"), "Financiera"),
         ("Fecha y número correctos de la autorización de funcionamiento.", a("/instituciones/index.html", "Perfil institucional"), "Jurídica"),
         ("Cifras vigentes de puntos, convenios y países.", "Varias", "Producto"),
         ("Tarifas vigentes de persona natural y jurídica, en texto.", a("/legal/tarifas-y-topes.html", "Tarifas y topes"), "Producto"),
         ("Datos del Defensor del Consumidor Financiero.", a("/ayuda/contacto.html", "Contacto"), "Cumplimiento"),
         ("Contactos institucionales, de la línea de divisas y de cumplimiento.", a("/instituciones/index.html", "Instituciones"), "Administración"),
         ("Clientes y aliados que pueden nombrarse.", a("/empresas/index.html", "Empresas"), "Comercial"),
         ("Traducción al inglés validada.", a("/en/index.html", "Versión en inglés"), "Jurídica"),
     ]))
     + sec("Decisiones", table("Lo que decide Powwi", ["Tema", "Opciones", "Recomendación de la propuesta"], [
         ("Transfiya", "Retirarla del sitio o mantenerla", "Retirarla si Bre-B ya la reemplazó, con redirección"),
         ("Recarga de cuentas de apuestas", "Destacarla, llevarla a segundo nivel o retirarla del sitio", "Segundo nivel, con información legal validada"),
         ("Documento de Buda.com en el dominio", "Retirarlo o mantenerlo", "Retirarlo, salvo que exista una razón vigente"),
         ("Gestión de archivos en Google Apps Script", "Mantenerla o llevarla a un dominio propio", "Llevarla a un dominio de Powwi"),
         ("Encuesta de 2023 y páginas vacías", "Retirar o actualizar", "Retirar"),
         ("Documentos de debida diligencia", "Publicarlos o entregarlos bajo solicitud", "Publicar los generales; el resto, bajo solicitud"),
         ("Nombre comercial de la línea de divisas", "Divisas, u otro", "El que defina Powwi"),
     ]), tone="sec-tint")
     + sec("Lo que depende de proveedores o de sistemas", table("Hallazgos fuera del alcance del sitio", ["Hallazgo", "De quién depende", "Solución propuesta"], [
         ("Portada de plantilla en banking.powwi.co/odigemp", "Proveedor del portal de empresas", "Reemplazar el contenido o redirigir la portada al sitio"),
         ("Títulos técnicos en el Portal Bre-B y la Taquilla PSE", "Equipo que mantiene esos portales", "Títulos con el nombre del servicio"),
         ("Buscador de puntos corresponsales", "Sistemas y redes aliadas", "Entregar los puntos en formato estructurado"),
         ("Ruta interna y dirección en la política de datos", "Dueño del documento", "Corregir y publicar una nueva versión"),
     ]))
     + sec("Accesos para llevarlo a producción", checks([
         "Administrador del sitio actual, que funciona sobre WordPress con Elementor.", "Hosting y un ambiente de pruebas con copia de seguridad.",
         "Contacto de la agencia que administra hoy el sitio.", "Contacto de los proveedores de los portales de empresas."]), tone="sec-tint"))
