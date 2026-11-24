from .base import *  # noqa: F401,F403
from .datos import DOC, TOPES, TOPES_HEAD, NOTA_TOPES

T = [("/index.html", "Inicio"), ("/legal/index.html", "Legal y regulatorio")]

page("legal/index.html",
     title="Centro legal y regulatorio | Powwi",
     desc="Reglamentos, términos y condiciones, contratos, tarifas, topes, políticas de datos, estados financieros y certificaciones de Powwi, con su formato y su versión.",
     sec="legal", reg="inst", canon="/legal/",
     body=phero("Centro legal y regulatorio", "Todos los documentos de Powwi, con su formato y su versión, en un solo lugar.",
                acts(btn("/legal/tarifas-y-topes.html", "Tarifas, montos y topes", "light")))
     + sec("", note(p("Los documentos se abren desde el sitio oficial. Esta propuesta cambia cómo se encuentran y se presentan, no su contenido jurídico.")))
     + sec("Productos y servicios", docs([
         ("Reglamento del depósito de dinero electrónico", "PDF. Código GL-RG-008, versión 4.", DOC["reglamento"], "Abrir"),
         ("Términos y condiciones del servicio Bre-B", "PDF. Versión 1.0, julio de 2025.", DOC["breb"], "Abrir"),
         ("Montos y topes 2026", "PDF. También en tabla dentro del sitio.", "/legal/tarifas-y-topes.html", "Ver tabla"),
         ("Tarifas de persona natural", "Imagen PNG. Pendiente de pasar a tabla.", DOC["tarifas_pn"], "Abrir"),
         ("Tarifas de persona jurídica", "Imagen PNG. Pendiente de pasar a tabla.", DOC["tarifas_pj"], "Abrir"),
         ("Contrato de adhesión de Dispersión y recaudo", "PDF. Versión 2026.", DOC["contrato_dr"], "Abrir"),
         ("Contrato de adhesión de Dispersión y recaudo as a Service", "PDF. Versión 01.2026.", DOC["contrato_draas"], "Abrir"),
     ]), id="productos", tone="sec-tint")
     + sec("Datos personales y privacidad", docs([
         ("Política de tratamiento de datos personales", "Página y PDF. Código SI-MA-007, versión 5 del 22 de junio de 2026.", DOC["datos"], "Abrir"),
         ("Aviso de privacidad", "Página.", DOC["privacidad"], "Abrir"),
         ("Política de cookies", "Página.", DOC["cookies"], "Abrir"),
     ]), id="datos")
     + sec("Consumidor financiero", docs([
         ("Derechos y deberes del consumidor financiero", "Página del sitio.", "/legal/consumidor-financiero.html", "Ver"),
         ("Solicitud de reversión de pagos", "PDF. Instructivo GE-IN-005.", DOC["reversion"], "Abrir"),
         ("Peticiones, quejas y reclamos", "Canales, tiempos de respuesta y Defensor del Consumidor.", "/ayuda/contacto.html", "Ver"),
     ]), id="consumidor", tone="sec-tint")
     + sec("La entidad", docs([
         ("Estados financieros 2025", "PDF. Con notas y dictamen.", DOC["eeff2025"], "Abrir"),
         ("Certificación SARLAFT 2025", "PDF.", DOC["sarlaft"], "Abrir"),
         ("Certificación SARO 2025", "PDF.", DOC["saro"], "Abrir"),
     ]) + p(a("/instituciones/index.html", "Ver el perfil institucional")), id="entidad")
     + sec("Línea de divisas", pend("Documentos de la línea IMC", p("Contratos, reglamentos y términos de la línea, con versión y fecha.")), id="divisas", tone="sec-tint"),
     mejoras=[
         ("Nueve enlaces en el pie de todas las páginas, sin formato, fecha ni versión.", "Centro de documentos por categoría. Cada sección del sitio enlaza solo los suyos."),
         ("Varios documentos tienen nombres de archivo de borrador.", "Convención de nombres para los archivos públicos."),
         ("La política de datos publicada deja ver una ruta interna de archivos y una dirección distinta de la del pie del sitio.", "Hallazgo señalado para que Powwi lo corrija en el documento."),
     ])

topes = table("Montos y topes 2026", TOPES_HEAD, TOPES, note=NOTA_TOPES)

page("legal/tarifas-y-topes.html",
     title="Tarifas, montos y topes | Powwi",
     desc="Topes por operación de Powwi Ágil, Powwi Más y Powwi Negocios en 2026, exención del 4×1000 y tarifas.",
     sec="legal", reg="inst", canon="/legal/tarifas-y-topes/",
     body=phero("Tarifas, montos y topes", "Lo que cuesta cada operación y hasta cuánto puedes mover.", trail=T + [(None, "Tarifas, montos y topes")])
     + sec("Topes por operación", topes)
     + sec("Datos que explican la tabla", cols2(
         ficha("Powwi Ágil", [("Saldo máximo", "$11.024.727"), ("Salidas de dinero al mes", "$11.024.727"), ("Equivalencia", "210,5 UVT")], foot="Powwi Más y Powwi Negocios no tienen estos límites.", tag="h3"),
         ficha("Valores de 2026", [("UVT", "$52.374"), ("Tope general de Bre-B", "1.000 UVB")], foot="El documento estima el tope general de Bre-B en unos $11.552.000.", tag="h3")), tone="sec-tint")
     + sec("Exención del 4×1000", table("Gravamen a los movimientos financieros", ["Depósito", "Exención"], [
         ("Powwi Ágil", "Hasta 65 UVT: $3.404.310 en 2026"),
         ("Powwi Más", "Posible hasta 350 UVT: $18.330.900"),
         ("Powwi Negocios", "Posible hasta 350 UVT"),
     ], note="La exención hasta 350 UVT se solicita. " + a("/personas/powwi-mas.html", "Cómo pedirla")))
     + sec("Tarifas", tabs("tf", [
         ("Persona natural", pend("Tarifas de persona natural", p("Hoy están publicadas como imagen. Se pasan a tabla cuando Powwi confirme cuál es la fuente vigente: la imagen de enero de 2026 o la página “Tarifas 2022”, que dice regir desde el 1 de julio de 2025.")
                                  + p(a(DOC["tarifas_pn"], "Abrir la imagen de tarifas") + " o " + a(DOC["tarifas_2022"], "abrir la página “Tarifas 2022”")))),
         ("Persona jurídica", pend("Tarifas de persona jurídica", p("Hoy están publicadas como imagen. Se pasan a tabla con el contenido vigente que confirme Powwi.") + p(a(DOC["tarifas_pj"], "Abrir la imagen de tarifas")))),
     ]), tone="sec-tint"),
     mejoras=[
         ("Las tarifas se publican como imágenes PNG.", "Tablas de texto, legibles en el celular y por lectores de pantalla."),
         ("Hay dos fuentes de tarifas, una de ellas titulada 2022.", "Una sola página de tarifas y topes."),
         ("Los topes solo están en un PDF.", "Topes en tabla, con enlace al documento oficial."),
     ])

DERECHOS = ["Recibir información de tu estado de cuenta.", "Recibir el servicio con la seguridad y la calidad acordadas.", "Que tu información se mantenga en reserva.",
            "Conocer con claridad costos, cargos y tarifas.", "Presentar peticiones, quejas y reclamos, y recibir respuesta oportuna.", "Conocer la política de tratamiento de datos y pedir correcciones.",
            "Recibir publicidad transparente y comparable.", "Recibir educación financiera.", "Verificar que la entidad está vigilada.", "Revisar los contratos y conservar copia."]
DEBERES = ["Prestar el servicio en las condiciones ofrecidas.", "Dar información clara y publicidad veraz.", "Contar con un Sistema de Atención al Consumidor.", "No incluir cláusulas abusivas.",
           "Entregar contratos claros y copias.", "No cobrar cargos que no se hayan acordado.", "Guardar reserva de tu información.", "Dar constancia del estado de tus productos cuando la pidas.",
           "Responder a tiempo solicitudes, quejas y reclamos.", "Tener los recursos humanos, físicos y tecnológicos suficientes."]

page("legal/consumidor-financiero.html",
     title="Consumidor financiero: derechos, deberes y reclamos | Powwi",
     desc="Tus derechos como consumidor financiero, los deberes de Powwi y la ruta para reclamar ante Powwi, el Defensor del Consumidor y la Superintendencia Financiera.",
     sec="legal", reg="inst", canon="/legal/consumidor-financiero/",
     body=phero("Consumidor financiero", "Tus derechos, los deberes de Powwi y cómo reclamar.", trail=T + [(None, "Consumidor financiero")])
     + sec("Derechos y deberes", cols2(block("Tus derechos", checks(DERECHOS)), block("Deberes de Powwi", checks(DEBERES)))
           + '<div class="mt">' + note(p("Resumen para esta propuesta. Al migrar se conserva la lista completa vigente.")) + "</div>")
     + sec("Cómo reclamar", cols3(
         block("Ante Powwi", p("Radica tu petición, queja o reclamo por los canales de atención.") + p(a("/ayuda/contacto.html", "Ir a contacto y PQRSF"))),
         block("Ante el Defensor del Consumidor Financiero", p('Escribe a <a href="mailto:reclamaciones@defensorialg.com.co">reclamaciones@defensorialg.com.co</a>.')),
         block("Ante la Superintendencia Financiera", p(a(DOC["sfc_queja"], "Consulta el procedimiento oficial")))),
           "Puedes acudir a cualquiera de las tres instancias.", tone="sec-tint")
     + sec("Por completar", pend("Datos del Defensor del Consumidor Financiero", p("Nombre del defensor principal y del suplente, dirección, teléfono y horario de atención."))),
     mejoras=[("Tres listas largas sin estructura y sin los datos del Defensor del Consumidor.", "Derechos, deberes y ruta de reclamación en tres instancias, con el bloque del Defensor por completar.")])
