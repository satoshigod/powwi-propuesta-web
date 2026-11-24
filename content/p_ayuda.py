from .base import *  # noqa: F401,F403
from .datos import DOC, CANALES, DEPTOS, depto_url

T = [("/index.html", "Inicio"), ("/ayuda/index.html", "Ayuda")]
FQ = "/ayuda/preguntas-frecuentes.html"

page("ayuda/index.html",
     title="Centro de ayuda | Powwi",
     desc="Respuestas por tema, canales de atención, puntos corresponsales y radicación de peticiones, quejas y reclamos.",
     sec="ayuda", reg="cercano", canon="/ayuda/",
     body=phero("¿En qué te ayudamos?", "Encuentra la respuesta por tema o habla con nosotros.",
                acts(btn(FQ, "Preguntas frecuentes", "ink"), btn("/ayuda/contacto.html", "Contacto y PQRSF", "line")))
     + sec("Lo urgente", cols3(
         panel("Perdí mi celular", p("Llama a la línea de Powwi para bloquear tu depósito. Lo reactivas cuando recuperes el celular.") + p('<a href="tel:+576014030555">601 403 0555</a>')),
         panel("No reconozco una operación", p("Repórtala de inmediato por la línea o al canal de denuncias.") + p('<a href="mailto:denuncias@powwi.co">denuncias@powwi.co</a>')),
         panel("Quiero reversar un pago", p("Sigue el instructivo de solicitud de reversión de pagos.") + p(a(DOC["reversion"], "Abrir el instructivo")))))
     + sec("Respuestas por tema", cols2(
         ll([(FQ + "#deposito", "Abrir y manejar tu depósito", "Requisitos, saldo, datos y cierre."),
             (FQ + "#envios", "Enviar y recibir plata", "A otros Powwi, a bancos y con Bre-B."),
             (FQ + "#efectivo", "Recargar y retirar", "PSE, corresponsales y recargas a celular."),
             (FQ + "#remesas", "Remesas", "Giros internacionales en tu Powwi.")]),
         ll([(FQ + "#seguridad", "Contraseña, celular y seguridad", "Qué hacer si olvidas la clave o cambias de celular."),
             (FQ + "#empresas", "Para empresas", "Powwi Negocios, nómina y dispersiones."),
             ("/legal/tarifas-y-topes.html", "Tarifas y topes", "Lo que cuesta y hasta cuánto puedes mover."),
             ("/ayuda/puntos.html", "Puntos corresponsales", "Dónde recargar y retirar en efectivo.")])), tone="sec-tint")
     + sec("Habla con nosotros", split(datos(CANALES), p("Para peticiones, quejas, reclamos, sugerencias y felicitaciones, usa el formulario de PQRSF.") + acts(btn("/ayuda/contacto.html", "Radicar una PQRSF", "ink")))),
     mejoras=[
         ("La ayuda son cuatro botones en imagen al final de la página de inicio.", "Centro de ayuda por tarea, con lo urgente arriba."),
         ("Los horarios y los canales están repartidos en varias páginas.", "Canales y horario en un solo bloque."),
     ])

G = [
    ("deposito", "Tu depósito", [
        ("¿Quién puede abrir un Powwi?", "Personas mayores de 18 años con cédula de ciudadanía y una línea celular colombiana. Cada persona puede tener un solo depósito."),
        ("¿Puedo abrirlo desde el sitio web?", "No. El depósito se abre desde Powwi App. " + a("/personas/descarga-la-app.html", "Descarga la app")),
        ("¿Cómo paso de Powwi Ágil a Powwi Más?", "Diligencias un formulario de vinculación y atiendes una entrevista. " + a("/personas/powwi-mas.html", "Ver Powwi Más")),
        ("¿Cómo consulto mi saldo y mis movimientos?", "El saldo aparece al abrir la app. Los movimientos están en Mi Powwi."),
        ("¿Cómo actualizo mis datos?", "Llama a la línea de Powwi y pide la actualización."),
        ("¿Cómo cierro mi Powwi?", "Deja el saldo en cero y solicita el cierre por cualquier canal, con tu nombre completo, tu documento y tus datos de contacto. Por la línea telefónica es más rápido."),
        ("¿Mi plata está cubierta por el seguro de depósitos?", "Sí. Los depósitos de Powwi tienen el seguro de depósitos de Fogafín, hasta 50 millones de pesos por depositante. No tiene costo."),
    ]),
    ("envios", "Enviar y recibir", [
        ("¿Puedo enviar plata a alguien que no tiene Powwi?", "Sí. La persona recibe un mensaje de texto para registrarse. Si no reclama en 48 horas, la plata vuelve a tu depósito."),
        ("¿Cómo envío a otros bancos?", "En la app, en Envía plata, elige Transferencia a bancos. " + a("/personas/enviar-dinero.html#otros-bancos", "Ver cómo")),
        ("¿Cómo inscribo a un favorito?", "En Mis favoritos lo buscas por tipo y número de documento y le pones un alias."),
        ("¿Cómo uso Bre-B?", "Registra tu llave en la app y empieza a recibir y enviar. " + a("/personas/bre-b.html", "Ver Bre-B")),
    ]),
    ("efectivo", "Recargar y retirar", [
        ("¿Dónde recargo mi Powwi?", "Por PSE desde cualquier banco colombiano o en efectivo en un punto corresponsal. " + a("/personas/recargas-y-retiros.html", "Ver recargas y retiros")),
        ("¿Dónde retiro?", "En un punto de la red de corresponsales. " + a("/ayuda/puntos.html", "Busca un punto")),
        ("¿Puedo recargar celulares de cualquier operador?", "Sí."),
        ("¿Dónde veo las tarifas y los topes?", a("/legal/tarifas-y-topes.html", "En tarifas, montos y topes") + "."),
    ]),
    ("remesas", "Remesas", [
        ("¿Qué necesito para recibir un giro internacional?", "Completar una vez el formulario de registro en la app y pedir a quien envía que elija tu billetera Powwi."),
        ("¿Cuánto cuesta recibirlo?", "Nada. La inscripción y la recepción no tienen costo para ti."),
        ("¿Qué tasa de cambio me aplican?", "La que le informan a quien envía, al momento del giro."),
        ("¿Qué hago si no veo el giro en mi Powwi?", "Escribe a escribenos@powwi.co, llama a la línea o usa el chat de WhatsApp."),
    ]),
    ("seguridad", "Contraseña, celular y seguridad", [
        ("Olvidé mi contraseña", "En la app elige Olvidaste tu contraseña, ingresa el código que llega por SMS y crea una nueva."),
        ("Perdí mi celular", "Llama a la línea para bloquear tu depósito. Lo reactivas cuando recuperes el celular."),
        ("Cambié de celular", "Instala la app en el celular nuevo, llama a la línea y responde tus preguntas de seguridad."),
        ("Si cambio de operador, ¿cambia mi número de depósito?", "No, mientras conserves la misma línea."),
    ]),
    ("empresas", "Empresas", [
        ("¿Powwi es solo para personas?", "No. Powwi Negocios es el depósito para empresas. " + a("/empresas/powwi-negocios.html", "Ver Powwi Negocios")),
        ("¿Puedo pagar la nómina con Powwi?", "Sí, con la dispersión de fondos de Powwi Negocios."),
        ("¿Puedo dispersar a cuentas de otras entidades?", "Sí, a depósitos Powwi y a cuentas de ahorros o corrientes de otras entidades."),
        ("¿Por qué veo a Pagos GDE S.A. o a Powwi en los extractos de otra marca?", "Porque esa marca opera con la licencia de Powwi, que es la entidad que custodia los depósitos. Es el caso de TodoPay."),
    ]),
]

page("ayuda/preguntas-frecuentes.html",
     title="Preguntas frecuentes | Powwi",
     desc="Respuestas sobre tu depósito Powwi, envíos, recargas, retiros, remesas, seguridad y servicios para empresas.",
     sec="ayuda", reg="cercano", canon="/ayuda/preguntas-frecuentes/",
     body=phero("Preguntas frecuentes", "Respuestas cortas, organizadas por tema.", trail=T + [(None, "Preguntas frecuentes")])
     + "".join(sec(title, acc([(q, p(ans)) for q, ans in items]), id=key, tone=("sec-tint" if i % 2 else "")) for i, (key, title, items) in enumerate(G)),
     mejoras=[
         ("74 preguntas en una sola lista, escritas en mayúsculas.", "Preguntas agrupadas por tema, en lenguaje claro."),
         ("Dan el tope de Powwi Ágil de 2025 y enlazan tarifas y topes de 2022.", "Cifras vigentes y un solo enlace a tarifas y topes."),
         ("Anuncian como próximos servicios cuyo estado actual no se conoce.", "Se publica solo lo vigente. Lo demás queda para validar."),
     ])

deptos = '<ul class="deptos">' + "".join(f'<li>{a(depto_url(code), name)}</li>' for name, code in DEPTOS) + "<li>Vaupés: sin listado publicado</li></ul>"

page("ayuda/puntos.html",
     title="Puntos corresponsales | Powwi",
     desc="Encuentra dónde recargar y retirar en efectivo en la red de corresponsales aliados de Powwi.",
     sec="ayuda", reg="cercano", canon="/ayuda/puntos/",
     body=phero("Puntos corresponsales", "Recarga y retira en efectivo en la red de corresponsales aliados de Powwi.", trail=T + [(None, "Puntos corresponsales")])
     + sec("Listados por departamento", deptos, "Cada enlace abre el listado oficial en PDF, con corte a marzo de 2026.", id="departamentos")
     + sec("Por resolver", cols2(
         pend("Buscador de puntos", p("Hoy los puntos se publican en un PDF por departamento. Un buscador por municipio necesita los datos de la red en formato estructurado: es una necesidad de sistemas, que se documenta y no se implementa en esta propuesta."), tag="Requiere backend"),
         pend("Redes aliadas y número de puntos", p("El sitio actual da dos cifras y dos listas de redes. Se publica la que valide Powwi."))), tone="sec-tint"),
     mejoras=[
         ("32 PDF por departamento, con corte a marzo de 2026. Vaupés no tiene enlace.", "Listados presentados con su fecha de corte, y la necesidad de un buscador documentada."),
         ("Dos cifras de puntos y dos listas de redes aliadas.", "Una cifra y una lista, validadas."),
         ("El enlace “Encuentra tu punto” apunta a una dirección distinta de la que figura en el sitemap.", "Enlaces internos definitivos."),
     ])


def _form(prefix, empresa):
    f = []
    if empresa:
        f += [("Razón social", "text"), ("NIT, sin puntos ni guion", "text"), ("Nombre de quien escribe", "text"), ("Cargo", "text")]
    else:
        f += [("Nombres", "text"), ("Apellidos", "text")]
    f += [("Tipo de documento", "select"), ("Número de documento", "text"), ("Correo electrónico", "email"), ("Celular", "tel"), ("Dirección", "text"), ("Ciudad", "text"),
          ("Motivo", "select"), ("Sobre qué es tu solicitud", "select")]
    out = []
    for i, (label, kind) in enumerate(f):
        fid = f"{prefix}-{i}"
        ctrl = f'<select id="{fid}"><option>Selecciona</option></select>' if kind == "select" else f'<input id="{fid}" type="{kind}">'
        out.append(f'<div><label for="{fid}">{label}</label>{ctrl}</div>')
    out.append(f'<div class="full"><label for="{prefix}-d">Cuéntanos qué pasó</label><textarea id="{prefix}-d"></textarea><small>Puedes adjuntar un archivo.</small></div>')
    out.append('<div class="full"><small>Al enviar aceptas la política de tratamiento de datos personales.</small></div>')
    out.append('<div class="full"><button class="btn btn-primary" type="button">Enviar PQRSF</button></div>')
    return '<form onsubmit="return false"><fieldset class="form" disabled>' + "".join(out) + "</fieldset></form>"


page("ayuda/contacto.html",
     title="Contacto y PQRSF | Powwi",
     desc="Canales de atención de Powwi, radicación de peticiones, quejas, reclamos, sugerencias y felicitaciones, tiempos de respuesta y Defensor del Consumidor Financiero.",
     sec="ayuda", reg="cercano", canon="/ayuda/contacto/", alt="/en/contact.html",
     body=phero("Contacto y PQRSF", "Llámanos, escríbenos o radica una petición, queja, reclamo, sugerencia o felicitación.",
                aside=ficha("Canales", CANALES), trail=T + [(None, "Contacto y PQRSF")])
     + sec("Radica tu PQRSF", note(p("<strong>Formulario de muestra.</strong> En esta propuesta no envía datos. En producción conserva los campos y el destino del formulario actual de “Escríbenos”."), "note-warn")
           + '<div class="mt">' + tabs("pq", [("Persona natural", _form("pn", False)), ("Empresa", _form("pj", True))]) + "</div>")
     + sec("Tiempos de respuesta", table("Plazo máximo de respuesta", ["Tipo de solicitud", "Días hábiles"], [
         ("Petición", "15"), ("Queja o reclamo", "8"), ("Sugerencia", "8"), ("Felicitación", "10"), ("Derecho de petición", "10"), ("Solicitud sobre tus datos personales", "15")], num=(1,)), tone="sec-tint")
     + sec("Otras instancias", cols3(
         block("Defensor del Consumidor Financiero", p('<a href="mailto:reclamaciones@defensorialg.com.co">reclamaciones@defensorialg.com.co</a>')
               + pend("Datos del Defensor", p("Nombre del defensor principal y del suplente, dirección, teléfono y horario."))),
         block("Superintendencia Financiera", p("Puedes presentar tu queja directamente ante el supervisor.") + p(a(DOC["sfc_queja"], "Ver el procedimiento"))),
         block("Canal de denuncias", p("Para reportar fraudes o conductas irregulares.") + p('<a href="mailto:denuncias@powwi.co">denuncias@powwi.co</a>'))))
     + sec("Sede", datos([("Dirección de notificación", "Ac. 26 # 69D-91, piso 9, Bogotá")]), tone="sec-tint"),
     mejoras=[
         ("El contacto está repartido entre “Escríbenos” y “Llámanos”.", "Una página con canales, horario, formulario y tiempos de respuesta."),
         ("La página del consumidor financiero no trae los datos del Defensor. Su correo solo aparece en “Llámanos”.", "Bloque del Defensor del Consumidor Financiero, por completar con los datos oficiales."),
     ])
