from .base import *  # noqa: F401,F403
from .datos import DOC

T = [("/index.html", "Inicio"), ("/instituciones/index.html", "Instituciones financieras y aliados")]
PV = '<span class="tag tag-new">Por validar</span>'

hitos = table("Constitución y autorizaciones", ["Hito", "Fecha", "Estado"], [
    ("Autorización de constitución. Superintendencia Financiera, Resolución 0546", "7 de abril de 2017", "Publicado"),
    ("Escritura de constitución n.º 729, Notaría 41 de Bogotá", "27 de abril de 2017", "Publicado"),
    ("Matrícula mercantil 0002813114, Cámara de Comercio de Bogotá", "5 de mayo de 2017", "Publicado"),
    ("Autorización de funcionamiento. Superintendencia Financiera, Resolución 0943", "25 de julio de 2018", PV),
    ("Inicio de operaciones", "25 de enero de 2019", "Publicado"),
    ("Condición de Intermediario del Mercado Cambiario. Banco de la República", "Oficio de febrero de 2020", PV),
    ("Inicio de la actividad como IMC", "2025", PV),
], note="La fecha de la autorización de funcionamiento es la de los estados financieros y los contratos. La página actual “Sobre nosotros” indica 26 de julio de 2017: Powwi debe confirmar cuál es la correcta.")

page("instituciones/index.html",
     title="Perfil institucional de Pagos GDE S.A. | Powwi",
     desc="Perfil institucional de Pagos GDE S.A. (Powwi): tipo de entidad, autorizaciones, supervisores, líneas de negocio y contacto para instituciones financieras y aliados.",
     sec="instituciones", reg="inst", canon="/instituciones/", alt="/en/institutions.html",
     body=phero("Perfil institucional", "Lo que un banco, un aliado o un regulador necesita saber de Pagos GDE S.A., en un solo lugar.",
                acts(btn("/instituciones/cumplimiento.html", "Cumplimiento", "light"), btn("/instituciones/informacion-financiera.html", "Estados financieros", "ghost")),
                ficha("Pagos GDE S.A.", [("Marca", "Powwi"), ("NIT", "901.077.411-3"), ("Tipo de entidad", "SEDPE"),
                                          ("Domicilio", "Bogotá, Colombia"), ("Constitución", "27 de abril de 2017"), ("Inicio de operaciones", "25 de enero de 2019")]))
     + sec("Autorizaciones y supervisión", hitos)
     + sec("Supervisores y protección", cols3(
         block("Superintendencia Financiera de Colombia", p("Autoriza y vigila a la entidad.")),
         block("Fogafín", p("Los depósitos están cubiertos por el seguro de depósitos, hasta 50 millones de pesos por depositante.")),
         block("Banco de la República", p("Regula el régimen cambiario bajo el que opera la línea de divisas."))), tone="sec-tint")
     + sec("Líneas de negocio", cols2(
         linea("Depósitos y pagos electrónicos", p("Depósitos electrónicos para personas y negocios, pagos, transferencias, recaudo, dispersión y Banking as a Service. La entidad no otorga crédito.")
               + p(a("/personas/index.html", "Personas") + " y " + a("/empresas/index.html", "Empresas"))),
         linea("Divisas", p("Operaciones de cambio como Intermediario del Mercado Cambiario.") + p(a("/divisas/index.html", "La línea IMC")), fx=True)))
     + sec("El expediente", ll([
         ("/instituciones/gobierno-corporativo.html", "Gobierno corporativo", "Accionistas, junta directiva, alta gerencia y órganos de control."),
         ("/instituciones/cumplimiento.html", "Cumplimiento", "Prevención de lavado de activos, certificaciones y documentación de debida diligencia."),
         ("/instituciones/informacion-financiera.html", "Información financiera", "Estados financieros con notas y dictamen."),
         ("/legal/index.html", "Centro legal y regulatorio", "Reglamentos, contratos, políticas y tarifas."),
     ]), tone="sec-tint")
     + sec("Contacto institucional", split(
         pend("Relaciones institucionales y cumplimiento", p("Nombre, cargo, correo y teléfono de quien atiende a entidades financieras, y del oficial de cumplimiento.")),
         block("Sede", datos([("Dirección", "Ac. 26 # 69D-91, piso 9, Bogotá"), ("Teléfono", '<a href="tel:+576014030555">+57 601 403 0555</a>'),
                              ("Correo", '<a href="mailto:escribenos@powwi.co">escribenos@powwi.co</a>')])))),
     mejoras=[
         ("No existe una sección para instituciones financieras.", "Perfil institucional con autorizaciones, supervisores, líneas de negocio y contacto."),
         ("“Sobre nosotros” da el 26 de julio de 2017 como fecha de la licencia de operación. Los estados financieros y los contratos, el 25 de julio de 2018.", "Una sola fecha, la que valide Powwi, con su número de resolución."),
         ("No hay versión en inglés.", "Versión en inglés de toda la sección."),
     ])

page("instituciones/gobierno-corporativo.html",
     title="Gobierno corporativo | Pagos GDE S.A. (Powwi)",
     desc="Composición accionaria, junta directiva, alta gerencia y órganos de control de Pagos GDE S.A.",
     sec="instituciones", reg="inst", canon="/instituciones/gobierno-corporativo/",
     body=phero("Gobierno corporativo", "Quiénes son los dueños de la entidad, quién la dirige y quién la controla.", trail=T + [(None, "Gobierno corporativo")])
     + sec("Propiedad y dirección", cols2(
         pend("Composición accionaria", p("Accionistas con su participación y beneficiarios finales, según lo que Powwi decida publicar. Las notas a los estados financieros de 2025 ya traen información de capital y accionistas.")),
         pend("Junta directiva", p("Miembros, calidad de independientes, comités y periodicidad."))))
     + sec("Alta gerencia y control", table("Cargos y órganos de control", ["Cargo u órgano", "Dato público hoy", "Estado"], [
         ("Representante legal", "Juan Carlos Cubides Garzón, según los estados financieros de 2025", PV),
         ("Alta gerencia", "Sin información en el sitio", "Por entregar"),
         ("Revisoría fiscal", a(DOC["eeff2025"], "Dictamen en los estados financieros de 2025"), "Publicado"),
         ("Oficial de cumplimiento", "Sin información en el sitio", "Por entregar"),
         ("Defensor del Consumidor Financiero", "Correo publicado: reclamaciones@defensorialg.com.co", "Faltan nombre, suplente, dirección y horario"),
     ]), tone="sec-tint")
     + sec("Documentos de gobierno", pend("Por entregar", bullets(["Estatutos sociales.", "Código de buen gobierno.", "Código de ética y conducta.", "Política de conflictos de interés.", "Informe de gestión."]))),
     mejoras=[
         ("El sitio no tiene una sección de accionistas, junta directiva ni directivos.", "Página de gobierno corporativo lista para el contenido que apruebe la Junta."),
         ("La única referencia a accionistas es una entrada de blog de 2022.", "Información vigente, con fecha de actualización."),
     ])

page("instituciones/cumplimiento.html",
     title="Cumplimiento | Pagos GDE S.A. (Powwi)",
     desc="Prevención de lavado de activos y financiación del terrorismo, certificaciones de riesgo y documentación de debida diligencia de Pagos GDE S.A.",
     sec="instituciones", reg="inst", canon="/instituciones/cumplimiento/",
     body=phero("Cumplimiento", "Cómo gestiona Powwi el riesgo de lavado de activos, el riesgo operacional, la protección de datos y la conducta.",
                trail=T + [(None, "Cumplimiento")])
     + sec("Certificaciones de riesgo", docs([
         ("Certificación SARLAFT 2025", "PDF. Sistema de administración del riesgo de lavado de activos y de la financiación del terrorismo.", DOC["sarlaft"], "Abrir"),
         ("Certificación SARO 2025", "PDF. Sistema de administración del riesgo operacional.", DOC["saro"], "Abrir"),
     ]), id="certificaciones")
     + sec("Programa de prevención de lavado de activos", pend("Descripción del programa", bullets([
         "Políticas y estructura del SARLAFT.", "Conocimiento del cliente y debida diligencia, incluida la reforzada.",
         "Monitoreo de operaciones y reportes.", "Listas restrictivas y sanciones.", "Capacitación y auditoría.", "Oficial de cumplimiento y su suplente."])), tone="sec-tint")
     + sec("Documentación para entidades financieras", docs([
         ("Cuestionario Wolfsberg de debida diligencia (CBDDQ)", "Si existe. Se publica o se entrega bajo solicitud.", None, ""),
         ("Certificación USA PATRIOT Act", "Si aplica.", None, ""),
         ("Formulario W-8BEN-E", "Si aplica.", None, ""),
         ("Política de sanciones y política anticorrupción", "Si existen como documentos públicos.", None, ""),
     ]) + '<div class="mt">' + note(p("Powwi decide cuáles documentos se publican y cuáles se entregan bajo solicitud. Ninguno se crea ni se simula en esta propuesta.")) + "</div>", id="debida-diligencia")
     + sec("Datos personales, seguridad y denuncias", cols3(
         block("Protección de datos", p("Manual de política de tratamiento de datos personales, código SI-MA-007, versión 5 del 22 de junio de 2026.") + p(a(DOC["datos"], "Abrir la política"))),
         block("Seguridad", p("Recomendaciones para los clientes y canales para reportar operaciones no reconocidas.") + p(a("/nosotros/seguridad.html", "Ver seguridad"))),
         block("Canal de denuncias", p('<a href="mailto:denuncias@powwi.co">denuncias@powwi.co</a>'))), tone="sec-tint")
     + sec("Servicios que un banco revisa con más detalle", pend("Explicación de Powwi", p("Cómo presenta la entidad la recarga de cuentas de apuestas, las remesas y las operaciones de cambio ante una entidad financiera: controles, aliados y alcance."), tag="Decisión de Powwi")),
     mejoras=[
         ("Dos enlaces con el texto “Haz clic aquí”, sin fecha de emisión.", "Certificaciones con nombre, año y formato, dentro de una página de cumplimiento."),
         ("No hay documentación de debida diligencia para bancos.", "Lista de documentos lista para publicar o entregar bajo solicitud."),
         ("La certificación SARLAFT de 2024 sigue indexada junto a la de 2025.", "Una sola versión vigente por documento."),
     ])

page("instituciones/informacion-financiera.html",
     title="Información financiera | Pagos GDE S.A. (Powwi)",
     desc="Estados financieros de Pagos GDE S.A. con sus notas y el dictamen del revisor fiscal.",
     sec="instituciones", reg="inst", canon="/instituciones/informacion-financiera/",
     body=phero("Información financiera", "Estados financieros con sus notas y el dictamen del revisor fiscal.", trail=T + [(None, "Información financiera")])
     + sec("Estados financieros", docs([
         ("Estados financieros 2025", "PDF. Con notas y dictamen del revisor fiscal.", DOC["eeff2025"], "Abrir"),
         ("Estados financieros 2024", "Sin enlace en el sitio actual.", None, ""),
         ("Estados financieros 2023", "Sin enlace en el sitio actual.", None, ""),
         ("Notas a los estados financieros 2022", "PDF. Alojado en el dominio, sin enlace desde el sitio.", DOC["eeff2022"], "Abrir"),
     ]))
     + sec("Por entregar", pend("Informes y calificaciones", bullets(["Informes de gestión.", "Calificaciones de riesgo, si existen.", "Estados financieros de 2023 y 2024 con sus notas."])), tone="sec-tint"),
     mejoras=[
         ("Solo se enlaza el año 2025, desde el pie de página.", "Archivo por años, con formato y contenido de cada documento."),
         ("Las notas de 2022 siguen en el dominio con un nombre de archivo de borrador.", "Nombres de archivo limpios y consistentes."),
     ])
