from .base import *  # noqa: F401,F403
from .datos import DOC, CANALES

T = [("/index.html", "Inicio"), ("/nosotros/index.html", "Nosotros")]
PV = '<span class="tag tag-new">Por validar</span>'

historia = table("Historia de Powwi", ["Año", "Hito", "Estado"], [
    ("2015", "Registro de la marca Pagos GDE ante la Superintendencia de Industria y Comercio.", "Publicado"),
    ("2017", "Autorización de constitución de la Superintendencia Financiera, escritura de constitución y matrícula mercantil. Solicitud de la marca Powwi.", "Publicado"),
    ("2018", "Autorización de funcionamiento de la Superintendencia Financiera.", PV),
    ("2019", "Inicio de operaciones.", "Publicado"),
    ("2020", "Condición de Intermediario del Mercado Cambiario.", PV),
    ("2025", "Bre-B reemplaza a Transfiya e inicia la actividad de la línea de divisas.", PV),
], note="Los hitos por validar salen de las notas a los estados financieros publicados, no de la página actual.")

page("nosotros/index.html",
     title="Sobre Powwi | Pagos GDE S.A.",
     desc="Powwi es la marca de Pagos GDE S.A., entidad financiera digital colombiana. Misión, visión, historia y líneas de negocio.",
     sec="nosotros", reg="comercial", canon="/nosotros/", alt="/en/about.html",
     body=phero("Sobre Powwi", "Somos una entidad financiera digital colombiana. Trabajamos para que más personas y negocios usen servicios financieros, con menos efectivo y menos informalidad.",
                acts(btn("/instituciones/index.html", "Ver el perfil institucional", "ink")),
                ficha("En breve", [("Sociedad", "Pagos GDE S.A."), ("Marca", "Powwi"), ("Tipo de entidad", "SEDPE"), ("Desde", "2017"), ("Sede", "Bogotá")]))
     + sec("Misión y visión", cols2(
         block("Misión", p("Dar a nuestros clientes soluciones financieras con las que construyan sus ecosistemas digitales, con la inclusión financiera como propósito.")),
         block("Visión", p("Ser el aliado financiero de referencia en el desarrollo digital de nuestros clientes.")))
         + '<div class="mt">' + note(p("Al migrar se conserva la redacción oficial vigente de la misión y la visión.")) + "</div>")
     + sec("Historia", historia, tone="sec-tint")
     + sec("Qué hacemos", cols2(
         linea("Depósitos y pagos electrónicos", p("Depósitos para personas y negocios, pagos inmediatos, recaudo, dispersión y servicios para aliados.")
               + p(a("/personas/index.html", "Personas") + " y " + a("/empresas/index.html", "Empresas"))),
         linea("Divisas", p("Operaciones de cambio como Intermediario del Mercado Cambiario.") + p(a("/divisas/index.html", "Divisas")), fx=True))),
     mejoras=[
         ("La historia termina el 25 de enero de 2019 y no está en orden cronológico.", "Línea de tiempo ordenada y actualizada, con los hitos por validar marcados."),
         ("No dice qué tipo de entidad es ni menciona sus dos líneas.", "Presenta a la entidad y enlaza el perfil institucional."),
     ])

page("nosotros/educacion-financiera.html",
     title="Educación financiera | Powwi",
     desc="Qué es una SEDPE, qué significa estar vigilado por la Superintendencia Financiera, qué cubre el seguro de depósitos de Fogafín y cómo usar tu depósito.",
     sec="nosotros", reg="cercano", canon="/nosotros/educacion-financiera/",
     body=phero("Educación financiera", "Lo básico para usar tu depósito con confianza.", trail=T + [(None, "Educación financiera")])
     + sec("La entidad", acc([
         ("¿Qué es una SEDPE?", p("Es una Sociedad Especializada en Depósitos y Pagos Electrónicos, un tipo de entidad financiera creado por la Ley 1735 de 2014. No es un banco ni una cooperativa y no presta dinero: ofrece depósitos, pagos y transferencias.")),
         ("¿Qué significa estar vigilado por la Superintendencia Financiera?", p("La Superintendencia autoriza y supervisa a las entidades que reciben dinero del público. Su tarea es cuidar la confianza y la estabilidad del sistema financiero.")),
         ("¿Qué cubre el seguro de depósitos de Fogafín?", p("Si una entidad inscrita es liquidada, el seguro devuelve los ahorros hasta 50 millones de pesos por persona y por entidad. No tiene costo y lo tienes desde que abres un producto cubierto.")),
     ]))
     + sec("Tu depósito y tu plata", acc([
         ("¿Qué es un depósito de dinero?", p("Es una cuenta digital que manejas desde el celular para recibir, enviar, pagar y retirar.")),
         ("Palabras que vas a encontrar", bullets(["<strong>Saldo:</strong> la plata que tienes disponible.", "<strong>Movimientos:</strong> el registro de lo que entra y sale.",
                                                  "<strong>UVT:</strong> unidad de valor tributario. Cambia cada año y con ella se calculan los topes.",
                                                  "<strong>GMF o 4×1000:</strong> impuesto a los movimientos financieros. Puedes marcar un producto como exento."])),
         ("Ahorro formal e informal", p("Ahorrar en una entidad vigilada protege tu plata con el seguro de depósitos. En Powwi puedes separar plata en " + a("/personas/bolsillos.html", "bolsillos") + ".")),
     ]), tone="sec-tint")
     + sec("Tus derechos", ll([
         ("/legal/consumidor-financiero.html", "Derechos del consumidor financiero", "Y los deberes de Powwi contigo."),
         ("/ayuda/contacto.html", "Cómo presentar una petición, queja o reclamo", "Canales y tiempos de respuesta."),
         (DOC["sfc_queja"], "Cómo quejarse ante la Superintendencia Financiera", "Procedimiento oficial."),
         ("/nosotros/seguridad.html", "Seguridad", "Cuidados para tus operaciones."),
     ])),
     mejoras=[("Buena parte del contenido está en imágenes e infografías.", "Texto accesible, organizado por temas, con enlaces a las fuentes oficiales.")])

page("nosotros/seguridad.html",
     title="Seguridad: cuida tu plata y tus datos | Powwi",
     desc="Recomendaciones de seguridad para usar Powwi App y Powwi web, y canales para reportar operaciones que no reconoces.",
     sec="nosotros", reg="cercano", canon="/nosotros/seguridad/",
     body=phero("Seguridad", "Trece cuidados para proteger tu plata y tus datos.", trail=T + [(None, "Seguridad")])
     + sec("Cuidados por situación", cols2(
         block("Tu celular y tu computador", checks(["Mantenlos libres de virus y archivos infectados.", "Usa un antivirus actualizado.", "Descarga programas solo de sitios oficiales.",
                                                     "Mantén al día las herramientas de seguridad del equipo."]))
         + block("Tus operaciones", checks(["Revisa cada mensaje de confirmación y reporta lo que no reconozcas.", "No dejes que otra persona haga operaciones por ti.", "No abras adjuntos de mensajes en cadena."])),
         block("Cuando entras a Powwi web", checks(["Escribe la dirección powwi.co tú mismo.", "Comprueba que empiece por https y muestre el candado.", "No entres desde redes wifi públicas ni cafés internet.",
                                                    "No guardes tus contraseñas en el navegador.", "Cierra la sesión al terminar."]))
         + block("Si pierdes el celular", checks(["Pide a tu operador que bloquee la línea y llama a la línea de Powwi para bloquear tu depósito."]))))
     + sec("Reporta de inmediato", cols2(
         block("Operaciones que no reconoces o celular perdido", datos(CANALES[:3])),
         block("Canal de denuncias", p('<a href="mailto:denuncias@powwi.co">denuncias@powwi.co</a>'))), tone="sec-tint"),
     mejoras=[("Una lista única de trece recomendaciones, sin agrupar.", "Recomendaciones agrupadas por situación, con los canales de reporte a la vista.")])

page("nosotros/noticias.html",
     title="Noticias y sala de prensa | Powwi",
     desc="Comunicados, novedades y archivo de noticias de Powwi, la marca de Pagos GDE S.A.",
     sec="nosotros", reg="comercial", canon="/nosotros/noticias/",
     body=phero("Noticias", "Comunicados y novedades de Powwi.", trail=T + [(None, "Noticias")])
     + sec("Archivo", docs([
         ("Powwi se potencia y SuRed se convierte en su accionista", "Entrada del blog. Última modificación en marzo de 2022.", off("/powwi-se-potencia-y-sured-se-convierte-en-su-accionista/"), "Leer"),
         ("Banking as a Service, foco para las empresas colombianas", "Entrada del blog. Última modificación en marzo de 2022.", off("/banking-as-a-service-nuestro-foco-para-las-empresas-colombianas/"), "Leer"),
         ("Powwi le apuesta a reducir el uso del dinero en efectivo", "Entrada del blog. Última modificación en marzo de 2022.", off("/powwi-le-apuesta-a-reducir-el-uso-del-dinero-en-efectivo/"), "Leer"),
         ("Powwi movilizó más de 117.000 millones de pesos en 2020", "Entrada del blog. Última modificación en febrero de 2022.", off("/powwi-movilizo-mas-de-117-000-millones-de-pesos-en-2020-y-asume-grandes-retos-con-la-llegada-de-su-nuevo-presidente/"), "Leer"),
         ("Retiros en efectivo y pagos digitales durante la cuarentena", "Entrada del blog. Última modificación en febrero de 2022.", off("/retiros-en-efectivo-cayeron-un-10-y-los-pagos-digitales-crecieron-un-25-en-cuarentena/"), "Leer"),
     ]), "Las cinco entradas publicadas hoy. Powwi debe revisar su vigencia antes de migrarlas.")
     + sec("Por entregar", pend("Sala de prensa", bullets(["Comunicados recientes: Bre-B y la línea de divisas.", "Contacto de prensa.", "Recursos de marca para medios."])), tone="sec-tint"),
     mejoras=[("La página “Noticias” está vacía y las cinco entradas del blog son de 2020 a 2022.", "Sala de prensa con archivo fechado y espacio para comunicados nuevos.")])

page("nosotros/trabaja-con-nosotros.html",
     title="Trabaja con nosotros | Powwi",
     desc="Conoce las vacantes de Powwi y cómo es trabajar en una entidad financiera digital colombiana.",
     sec="nosotros", reg="comercial", canon="/nosotros/trabaja-con-nosotros/",
     body=phero("Trabaja con nosotros", "Conoce las vacantes de Powwi.", acts(btn(DOC["linkedin"], "Ver Powwi en LinkedIn", "ink")), trail=T + [(None, "Trabaja con nosotros")])
     + sec("Lo que tendrá esta página", pend("Contenido de la página", bullets(["Cómo es trabajar en Powwi.", "Proceso de selección.", "Vacantes vigentes o enlace a la bolsa de empleo que use Powwi."]))),
     mejoras=[("El enlace del pie de todas las páginas lleva a una dirección privada de LinkedIn, que no muestra vacantes.", "Enlace a la página de empresa de Powwi en LinkedIn y espacio para vacantes propias.")])
