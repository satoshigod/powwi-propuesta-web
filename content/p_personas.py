from .base import *  # noqa: F401,F403
from .datos import DOC, STORES, TOPES, TOPES_HEAD, NOTA_TOPES, PASOS_ABRIR, topes_de

T = [("/index.html", "Inicio"), ("/personas/index.html", "Personas")]
APP = btn("/personas/descarga-la-app.html", "Descarga la app")

# ---------- Resumen ----------
comparar = table("Powwi Ágil y Powwi Más", ["", "Powwi Ágil", "Powwi Más"], [
    ("Tipo de depósito", "De bajo monto", "Ordinario"),
    ("Saldo máximo", "$11.024.727 en 2026 (210,5 UVT)", "Sin límite"),
    ("Salidas de dinero al mes", "$11.024.727 en 2026 (210,5 UVT)", "Sin límite"),
    ("Exención del 4×1000", "Hasta $3.404.310 en 2026 (65 UVT)", "Posible hasta $18.330.900 (350 UVT)"),
    ("Cómo se abre", "Desde la app, con seis datos personales", "Primero abres Powwi Ágil; luego firmas un formulario de vinculación y atiendes una entrevista"),
], note="Cifras de 2026 publicadas hoy en powwi.co. " + a("/legal/tarifas-y-topes.html", "Ver tarifas, montos y topes"))

tareas = cols2(
    block("Recibir y enviar", ll([
        ("/personas/bre-b.html", "Bre-B", "Al instante y con tu llave, a cualquier entidad."),
        ("/personas/enviar-dinero.html", "Enviar dinero", "A otro Powwi, a otros bancos o para retiro en corresponsal."),
        ("/personas/remesas.html", "Remesas", "Recibe giros internacionales en tu Powwi."),
    ])) + block("Meter y sacar plata", ll([
        ("/personas/recargas-y-retiros.html#recargas", "Recargar", "Por PSE o en efectivo en un corresponsal."),
        ("/personas/recargas-y-retiros.html#retiros", "Retirar", "En efectivo, con un código de retiro."),
    ])),
    block("Pagar", ll([
        ("/personas/pagos.html#facturas", "Facturas y convenios", "Servicios públicos, telefonía, educación, salud y seguros."),
        ("/personas/pagos.html#celular", "Recargas a celular", "A cualquier operador."),
        ("/personas/pagos.html#contenido-digital", "Contenido digital", "Streaming y videojuegos."),
        ("/personas/pagos.html#comercios", "Comercios", "Paga donde aceptan Powwi."),
    ])) + block("Ahorrar y controlar", ll([
        ("/personas/bolsillos.html", "Bolsillos", "Separa plata para una meta."),
        ("/ayuda/preguntas-frecuentes.html#deposito", "Saldo, movimientos y extractos", "Todo desde la app."),
    ])),
)

page("personas/index.html",
     title="Personas: abre tu depósito Powwi desde el celular | Powwi",
     desc="Depósitos Powwi Ágil, Powwi Más y Powwi Inclusivo. Envía y recibe con Bre-B, recarga, retira, paga y ahorra desde la app.",
     sec="personas", reg="cercano", canon="/personas/",
     body=phero("Tu plata en el celular, tan sencillo como el efectivo",
                "Abre un depósito Powwi desde la app, sin desplazarte, y úsalo para recibir, enviar, pagar y ahorrar.",
                acts(APP, btn("/personas/index.html#depositos", "Compara los depósitos", "line")),
                ficha("Para abrir tu Powwi", [("Edad mínima", "18 años"), ("Documento", "Cédula de ciudadanía"),
                                               ("Línea celular", "Colombiana"), ("Dónde se abre", "En Powwi App"),
                                               ("Datos que se piden", "Seis")]))
     + sec("Elige tu depósito", comparar
           + '<div class="acts">' + btn("/personas/powwi-agil.html", "Conoce Powwi Ágil", "ink") + btn("/personas/powwi-mas.html", "Conoce Powwi Más", "line") + "</div>"
           + '<div class="mt">' + note(p("<strong>¿Recibes subsidios o ayudas del Estado?</strong> Tu depósito se identifica como " + a("/personas/powwi-inclusivo.html", "Powwi Inclusivo") + " y esos recursos no pagan comisiones.")) + "</div>",
           "Los dos se abren desde la app. La diferencia está en cuánta plata puedes tener y mover.", id="depositos")
     + sec("Qué puedes hacer con tu Powwi", tareas, tone="sec-tint")
     + sec("", cta("Abre tu Powwi desde la app", "El depósito se abre y se maneja desde el celular. No se puede abrir desde el sitio web.", btn("/personas/descarga-la-app.html", "Descarga la app", "light"))),
     mejoras=[
         ("Los tres depósitos se explican en la página de inicio, uno debajo del otro.", "Comparación en tabla y una página por depósito."),
         ("Doce botones en imagen, todos con el mismo peso.", "Servicios agrupados por lo que la persona quiere hacer."),
         ("Las tarifas son una imagen dentro de la página.", "Enlace a tarifas, montos y topes en texto."),
     ])

# ---------- Powwi Ágil ----------
BENEFICIOS = [
    "Enviar y retirar en línea con Bre-B.",
    "Manejar tu depósito desde la app, donde estés.",
    "Ahorrar en bolsillos.",
    "Recargar y retirar en la red de corresponsales.",
    "Transferir a otros bancos.",
    "Enviar plata a otros Powwi.",
    "Pagar servicios públicos y privados.",
    "Comprar contenido digital y streaming.",
    "Cargar tu depósito por PSE y en corresponsales.",
    "Descargar extractos y movimientos.",
]

page("personas/powwi-agil.html",
     title="Powwi Ágil: depósito de bajo monto | Powwi",
     desc="Powwi Ágil es el depósito de bajo monto que abres desde el celular. Topes de 2026, beneficios y pasos de apertura.",
     sec="personas", reg="cercano", canon="/personas/powwi-agil/",
     body=phero("Powwi Ágil", "El depósito de bajo monto que abres desde el celular, con el mínimo de datos.", acts(APP),
                ficha("Powwi Ágil en 2026", [("Saldo máximo", "$11.024.727"), ("Salidas al mes", "$11.024.727"),
                                              ("Equivalencia", "210,5 UVT"), ("Exento de 4×1000 hasta", "$3.404.310")],
                      foot="La exención del 4×1000 equivale a 65 UVT."),
                T + [(None, "Powwi Ágil")])
     + sec("Qué puedes hacer", checks(BENEFICIOS))
     + sec("Cómo abrirlo", steps(PASOS_ABRIR), "Seis pasos en la app.", tone="sec-tint")
     + sec("Topes por operación", topes_de(1, "Topes de Powwi Ágil"))
     + sec("", cta("¿Necesitas mover más plata?", "Powwi Más no tiene límite de saldo ni de salidas de dinero.", btn("/personas/powwi-mas.html", "Conoce Powwi Más", "light"))),
     mejoras=[
         ("No tiene página propia: se describe dentro de la página de inicio.", "Página propia con topes, pasos de apertura y enlaces a los documentos."),
         ("Las preguntas frecuentes dan el tope de 2025 y la página de inicio el de 2026.", "Una sola cifra vigente, la misma del documento de topes."),
         ("Los topes por operación solo están en un PDF.", "Topes en tabla dentro de la página."),
     ])

# ---------- Powwi Más ----------
page("personas/powwi-mas.html",
     title="Powwi Más: depósito ordinario sin límites | Powwi",
     desc="Powwi Más es el depósito ordinario de Powwi: sin límite de saldo ni de salidas de dinero y sin cuota de manejo.",
     sec="personas", reg="cercano", canon="/personas/powwi-mas/",
     body=phero("Powwi Más", "El depósito ordinario sin límite de saldo ni de salidas de dinero.", acts(APP),
                ficha("Powwi Más en 2026", [("Saldo", "Sin límite"), ("Salidas al mes", "Sin límite"),
                                             ("Cuota de manejo", "No tiene"), ("Exención de 4×1000", "Posible hasta $18.330.900")],
                      foot="La exención del 4×1000 equivale a 350 UVT y se solicita."),
                T + [(None, "Powwi Más")])
     + sec("Cómo pasar de Powwi Ágil a Powwi Más", steps([
         ("Abre Powwi Ágil desde la app", "Es el punto de partida de todos los depósitos."),
         ("Diligencia y firma el formulario de vinculación", "Por seguridad pedimos datos adicionales."),
         ("Atiende la entrevista del Contact Center", "Con ella se completa la apertura de tu Powwi Más."),
     ]))
     + sec("Qué incluye", checks(BENEFICIOS + ["Pagar en comercios.", "Sin cuotas de manejo ni de administración."]), tone="sec-tint")
     + sec("Topes por operación", topes_de(2, "Topes de Powwi Más"))
     + sec("Cómo marcar tu depósito como exento del 4×1000",
           p("Primero pide a tu otra entidad financiera que retire la exención, si la tienes allí. Después solicítala por la línea de Powwi.")
           + p(a("/ayuda/contacto.html", "Ver canales de atención"))),
     mejoras=[
         ("No tiene página propia.", "Página propia con el paso a paso desde Powwi Ágil."),
         ("El proceso de vinculación está en una sola línea.", "Tres pasos explicados."),
     ])

# ---------- Powwi Inclusivo ----------
page("personas/powwi-inclusivo.html",
     title="Powwi Inclusivo: subsidios y ayudas del Estado | Powwi",
     desc="Si recibes subsidios o ayudas del Estado, tu depósito Powwi se identifica como Powwi Inclusivo y esos recursos no pagan comisiones.",
     sec="personas", reg="cercano", canon="/personas/powwi-inclusivo/",
     body=phero("Powwi Inclusivo", "Si recibes subsidios o ayudas del Estado, tu depósito queda identificado para que esos recursos no paguen comisiones.",
                acts(APP), trail=T + [(None, "Powwi Inclusivo")])
     + sec("Qué es", split(
         p("No es un depósito aparte. Es una identificación interna de tu Powwi Ágil o de tu Powwi Más, prevista en el Decreto 222 de 2020.",
           "Con ella, los recursos que vienen de programas del Estado no tienen cobros por transferencia, comisiones ni tarifas."),
         ficha("En resumen", [("Aplica a", "Powwi Ágil y Powwi Más"), ("Costo", "Sin comisiones sobre esos recursos"),
                              ("Exención de 4×1000", "Hasta 65 UVT")], tag="h3")))
     + sec("Cómo se activa", steps([
         ("Abre tu Powwi Ágil", "Desde la app, como cualquier otro depósito."),
         ("La entidad que paga el subsidio informa a Powwi", "Confirma que eres beneficiario de un programa."),
         ("Tu depósito queda identificado como Powwi Inclusivo", "No tienes que hacer ningún trámite adicional."),
     ]), tone="sec-tint"),
     mejoras=[("Es un párrafo dentro de la página de inicio.", "Página propia que explica qué es y cómo se activa.")])

# ---------- Bre-B ----------
page("personas/bre-b.html",
     title="Bre-B en Powwi: envía y recibe con tu llave | Powwi",
     desc="Bre-B en Powwi: registra tu llave y envía o recibe plata al instante, todos los días. Tipos de llave, costo y topes.",
     sec="personas", reg="cercano", canon="/personas/bre-b/",
     body=phero("Bre-B en Powwi", "Envía y recibe plata al instante con una llave, a cualquier hora y entre distintas entidades.",
                acts(APP, btn(DOC["breb"], "Términos y condiciones", "line")),
                ficha("Bre-B en datos", [("Disponibilidad", "24 horas, todos los días"), ("Costo", "Sin costo hoy"),
                                          ("Tope por envío", "$3.000.000"), ("Llaves", "Celular, documento, correo o código")],
                      foot="Según los términos de Bre-B (versión 1.0, julio de 2025) y Montos y topes 2026."),
                T + [(None, "Bre-B")])
     + sec("Tu llave", split(
         p("Una llave reemplaza el número de tu depósito: quien te paga solo necesita conocerla.",
           "Puedes usar como llave tu número de celular, tu número de documento, tu correo electrónico o un código alfanumérico.",
           "Después de registrar una llave, puedes empezar a recibir pagos hasta dos horas después de la confirmación.")
         , block("Lo que puedes hacer con tu llave", checks(["Registrarla.", "Consultarla.", "Modificarla.", "Bloquearla por un tiempo y reactivarla.", "Cancelarla."]))),
           id="llaves")
     + sec("Enviar y recibir", cols2(
         block("Enviar", p("Escribe la llave de quien recibe y confirma. El pago es inmediato y, una vez confirmado, no se puede reversar.")),
         block("Recibir", p("Comparte tu llave. No necesitas dar el número de tu depósito."))), tone="sec-tint")
     + sec("Costo", p("Bre-B no tiene costo hoy. Los términos prevén que, desde el cuarto año del servicio, pueda aplicar una tarifa por operación, anunciada con 45 días de anticipación."))
     + sec("Por confirmar", cols2(
         pend("Código QR y portabilidad de llaves", p("Los términos los describen como funciones futuras. Se publican como disponibles cuando Powwi lo confirme.")),
         pend("Transfiya", p("Sigue en la página de inicio y en las preguntas frecuentes. Las notas a los estados financieros de 2025 indican que Bre-B la reemplazó. Powwi debe confirmar si se retira."), tag="Decisión de Powwi")))
     + sec("Documentos", docs([
         ("Términos y condiciones del servicio Bre-B", "PDF. Versión 1.0, julio de 2025.", DOC["breb"], "Abrir"),
         ("Montos y topes 2026", "PDF. También en tabla dentro del sitio.", "/legal/tarifas-y-topes.html", "Ver tabla"),
     ]) + p("¿Tienes una empresa? " + a("/empresas/bre-b.html", "Conoce Bre-B para empresas")), tone="sec-tint"),
     mejoras=[
         ("El contenido de Bre-B vive en la dirección /transfiya/, con el título Transfiya.", "Página propia en /personas/bre-b/, con redirección desde la dirección actual."),
         ("No explica los tipos de llave ni cómo se administran.", "Llaves, envío, recepción, costo y tope en una sola página."),
         ("Dos botones del inicio, Bre-B y Transfiya, llevan a la misma página.", "Una sola entrada para Bre-B. Transfiya queda a decisión de Powwi."),
     ])

# ---------- Enviar dinero ----------
page("personas/enviar-dinero.html",
     title="Enviar dinero desde tu Powwi | Powwi",
     desc="Cuatro formas de enviar dinero desde Powwi: con Bre-B, a otro Powwi, a otros bancos o para retiro en efectivo en un corresponsal.",
     sec="personas", reg="cercano", canon="/personas/enviar-dinero/",
     body=phero("Enviar dinero", "Cuatro formas de mandar plata desde tu Powwi. Elige según a dónde va.", trail=T + [(None, "Enviar dinero")])
     + sec("", ll([
         ("/personas/bre-b.html", "Con Bre-B", "Al instante, con la llave de quien recibe, a cualquier entidad."),
         ("/personas/enviar-dinero.html#otros-powwi", "A otro Powwi", "Con el número de celular de quien recibe."),
         ("/personas/enviar-dinero.html#otros-bancos", "A otros bancos", "Transferencia a una cuenta de otra entidad financiera."),
         ("/personas/enviar-dinero.html#retiro-en-corresponsal", "Para retiro en corresponsal", "Para alguien que no tiene Powwi y quiere reclamar en efectivo."),
     ]))
     + sec("A otro Powwi", split(
         p("En la app entra a Envía plata, elige Envía plata a Powwi, escribe el celular de quien recibe y confirma.",
           "Si la persona todavía no tiene Powwi, recibe un mensaje de texto para registrarse. Si no reclama la plata en 48 horas, vuelve a tu depósito."),
         block("Favoritos", p("Inscribe en Mis favoritos a las personas a las que les envías seguido. Las buscas por tipo y número de documento y les pones un alias."))),
           id="otros-powwi", tone="sec-tint")
     + sec("A otros bancos", split(
         p("En la app entra a Envía plata, elige Transferencia a bancos y completa los datos de quien recibe. Antes de confirmar ves la tarifa.",
           "La plata llega a la cuenta de destino según los ciclos de ACH."),
         ficha("Tope por envío", [("Powwi Ágil", "$11.024.727"), ("Powwi Más", "Sin límite")], tag="h3")), id="otros-bancos")
     + sec("Para retiro en corresponsal", split(
         steps([
             ("En la app entra a Retira tu dinero y elige Envía $ en línea", "Es un envío para reclamar en efectivo."),
             ("Escribe la cédula y el celular de quien recibe, y el valor", "Quien recibe necesita cédula colombiana."),
             ("Entrégale los datos del retiro y el código", "Los necesita para reclamar."),
             ("La persona reclama en un corresponsal", "Con su número de cédula, su celular, el valor y el código."),
         ]),
         ficha("Valores", [("Mínimo", "$5.000"), ("Máximo", "$1.000.000")], foot="Según las preguntas frecuentes actuales: validar.", tag="h3")),
           id="retiro-en-corresponsal", tone="sec-tint"),
     mejoras=[
         ("Cuatro páginas para enviar dinero: dos duplicadas y una vacía (/envia-en-linea/).", "Una página que compara las formas de enviar y explica cada una."),
         ("Los enlaces de la página de inicio a estas páginas están truncados.", "Direcciones definitivas, con redirección desde las actuales."),
     ])

# ---------- Recargas y retiros ----------
page("personas/recargas-y-retiros.html",
     title="Recargas y retiros de tu Powwi | Powwi",
     desc="Recarga tu Powwi por PSE o en efectivo y retira en la red de corresponsales aliados. Topes por operación.",
     sec="personas", reg="cercano", canon="/personas/recargas-y-retiros/",
     body=phero("Recargas y retiros", "Mete y saca plata de tu Powwi por PSE o en efectivo, en la red de corresponsales aliados.",
                acts(btn("/ayuda/puntos.html", "Busca un punto", "ink")), trail=T + [(None, "Recargas y retiros")])
     + sec("Recargar", cols2(
         block("Por PSE", p("Desde cualquier banco colombiano, en la app o en el sitio de Powwi.")
               + datos([("Powwi Ágil", "Hasta $11.024.727"), ("Powwi Más", "Sin límite")])),
         block("En efectivo", p("En un punto de la red de corresponsales aliados.")
               + datos([("Por operación", "Hasta $1.000.000")]))), id="recargas")
     + sec("Retirar en efectivo", split(
         steps([
             ("Solicita el retiro en la app", "Indica cuánto vas a retirar."),
             ("Confirma con el código que llega por SMS", "Es la validación de seguridad."),
             ("Presenta el código de retiro en el corresponsal", "El código dura 15 minutos."),
         ]),
         ficha("Tope", [("Por operación", "$1.000.000")], foot=a("/legal/tarifas-y-topes.html", "Ver todos los topes"), tag="h3")),
           id="retiros", tone="sec-tint")
     + sec("La red de corresponsales", pend("Redes aliadas y número de puntos",
           p("La página de recargas habla de más de 20.000 puntos de SuRed, Punto de Pago y PTM. La de puntos de ubicación, de más de 22.000 puntos de Baloto, PTM, Reval y SuRed. Se publica una sola cifra y una sola lista, las que valide Powwi."))),
     mejoras=[
         ("Dos páginas de recarga y una de retiro, con cifras distintas de puntos y listas distintas de redes aliadas.", "Una sola página. La cifra y las redes se publican una vez validadas."),
         ("Los topes por operación solo están en un PDF.", "Topes a la vista, junto a cada operación."),
     ])

# ---------- Pagos ----------
page("personas/pagos.html",
     title="Pagos con Powwi: facturas, recargas y contenido digital | Powwi",
     desc="Paga facturas y convenios, recarga tu celular, compra contenido digital y paga en comercios desde Powwi App.",
     sec="personas", reg="cercano", canon="/personas/pagos/",
     body=phero("Pagos", "Paga tus facturas, recarga tu celular y compra contenido digital desde la app.", acts(APP), trail=T + [(None, "Pagos")])
     + sec("Facturas y convenios", split(
         p("Paga desde tu Powwi, sin filas y sin salir de casa.")
         + checks(["Servicios públicos.", "Telefonía móvil y fija.", "Administraciones.", "Instituciones educativas.", "Salud y seguros."]),
         pend("Número de convenios", p("El sitio actual publica una cifra de convenios. Se conserva la que valide Powwi."))), id="facturas")
     + sec("Recargas a celular", p("Recarga minutos y datos de cualquier operador."), id="celular", tone="sec-tint")
     + sec("Contenido digital", p("Compra acceso a plataformas de streaming y a videojuegos."), id="contenido-digital")
     + sec("Comercios", p("Paga en los comercios que aceptan Powwi. El pago se inicia desde la sección de compras de la app."), id="comercios", tone="sec-tint")
     + sec("Recarga de cuentas de apuestas", split(
         p("Recarga desde tu Powwi tu cuenta en operadores de apuestas."),
         pend("Información legal y ubicación", p("Operadores, condiciones y avisos legales: por validar. En la propuesta el servicio se conserva, pero sale de los destacados de la página de inicio."), tag="Decisión de Powwi")),
           id="apuestas"),
     mejoras=[
         ("Cuatro páginas de una o dos líneas cada una.", "Una página de pagos, con una sección por servicio."),
         ("La recarga de cuentas de apuestas tiene botón propio en el inicio. Su página no trae operadores, condiciones ni avisos.", "Pasa a un segundo nivel y queda lista para la información legal que valide Powwi."),
         ("La recarga a celular no tiene página.", "Tiene su propia sección."),
     ])

# ---------- Bolsillos ----------
page("personas/bolsillos.html",
     title="Bolsillos: separa plata para tus metas | Powwi",
     desc="Con los bolsillos de Powwi separas plata para una meta y la retiras cuando la necesites.",
     sec="personas", reg="cercano", canon="/personas/bolsillos/",
     body=phero("Bolsillos", "Separa plata para lo que quieres y retírala cuando la necesites.", acts(APP), trail=T + [(None, "Bolsillos")])
     + sec("Crea un bolsillo", split(
         steps([("Entra a Bolsillos en la app", "Está en el menú de tu depósito."), ("Toca el signo más", "Así empiezas un bolsillo nuevo."),
                ("Ponle un nombre", "El de tu meta."), ("Pásale plata", "La puedes retirar cuando quieras.")]),
         pend("Bolsillo individual y bolsillo colectivo", p("La página de inicio anuncia los dos, pero la del servicio no explica la diferencia. Falta ese texto.")))),
     mejoras=[("La página del servicio no explica el bolsillo colectivo que anuncia la página de inicio.", "Estructura lista para los dos tipos de bolsillo. El texto queda pendiente.")])

# ---------- Remesas ----------
page("personas/remesas.html",
     title="Remesas internacionales en tu Powwi | Powwi",
     desc="Recibe en tu Powwi los giros internacionales de Western Union, en alianza con Acciones & Valores. Sin costo por recibir.",
     sec="personas", reg="cercano", canon="/personas/remesas/",
     body=phero("Remesas internacionales", "Recibe en tu Powwi los giros que te envían desde el exterior por Western Union, en alianza con Acciones &amp; Valores.",
                acts(APP),
                ficha("Recibir un giro", [("Costo por recibir", "$0"), ("Inscripción", "$0, una sola vez"),
                                           ("Quién puede recibir", "Mayores con cédula colombiana"), ("Cuándo llega", "De inmediato")],
                      foot="Llega de inmediato si el envío sale de una agencia de Western Union."),
                T + [(None, "Remesas")])
     + sec("Cómo recibir", steps([
         ("Completa el formulario de registro en la app", "Se hace una sola vez."),
         ("Pide a quien envía que elija tu billetera Powwi", "Debe confirmar tu nombre y tu número de celular."),
         ("Recibe la plata en tu Powwi", "Después puedes usarla o retirarla en un corresponsal."),
     ]))
     + sec("Tasa de cambio y costo del envío", p("La tasa de cambio y el costo los conoce y acepta quien envía, al momento de hacer el giro. Dependen del valor, del destino y de la forma de pago.")
           + p(a("/personas/recargas-y-retiros.html#retiros", "Cómo retirar en efectivo")), tone="sec-tint")
     + sec("Por confirmar", pend("Países de origen", p("La página de remesas habla de más de 200 países y las preguntas frecuentes de más de 220. Se publica la cifra que valide Powwi."))),
     mejoras=[
         ("Dos páginas de remesas (/remesas/ y /remesas-2/) y doce preguntas dispersas.", "Una página con costos, requisitos y pasos."),
         ("Dos cifras distintas de países.", "Una sola cifra, validada."),
     ])

# ---------- Descarga la app ----------
page("personas/descarga-la-app.html",
     title="Descarga Powwi App | Powwi",
     desc="Descarga Powwi App desde la tienda oficial de tu celular y abre tu depósito en seis pasos.",
     sec="personas", reg="cercano", canon="/personas/descarga-la-app/",
     body=phero("Descarga Powwi App", "Tu depósito se abre y se maneja desde la app. No se puede abrir desde el sitio web.", trail=T + [(None, "Descarga la app")])
     + sec("Tiendas oficiales", ll(STORES), "Estos enlaces llevan a la ficha oficial de Powwi App en cada tienda.")
     + sec("Abre tu Powwi en seis pasos", split(steps(PASOS_ABRIR),
           ficha("Qué necesitas", [("Edad", "18 años o más"), ("Documento", "Cédula de ciudadanía"), ("Línea celular", "Colombiana")],
                 foot=a(DOC["infografia"], "Ver la guía de registro en PDF"), tag="h3")), tone="sec-tint"),
     mejoras=[
         ("La página tiene solo tres botones en imagen.", "Tiendas oficiales, requisitos y pasos de apertura en texto."),
         ("El enlace desde la página de inicio está truncado (/descarga-tu-powwi-a).", "Dirección definitiva."),
     ])
