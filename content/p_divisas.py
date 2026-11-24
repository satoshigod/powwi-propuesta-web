from .base import *  # noqa: F401,F403
from .datos import DOC, CANALES

T = [("/index.html", "Inicio"), ("/divisas/index.html", "Divisas")]

page("divisas/index.html",
     title="Divisas: la línea IMC de Powwi | Pagos GDE S.A.",
     desc="Powwi opera como Intermediario del Mercado Cambiario. Conoce la línea de divisas, su marco regulatorio y a quién atiende.",
     sec="divisas", reg="inst", canon="/divisas/", alt="/en/fx.html",
     body=phero("Divisas: la línea IMC de Powwi",
                "Powwi opera como Intermediario del Mercado Cambiario. Esta sección presenta la línea a empresas, aliados e instituciones financieras.",
                acts(btn("/divisas/como-operar.html", "Cómo operar", "light"), btn("/instituciones/index.html", "Perfil institucional", "ghost")),
                ficha("La línea en datos públicos", [("Entidad", "Pagos GDE S.A."), ("Condición", "Intermediario del Mercado Cambiario"),
                                                      ("Marco", "Régimen cambiario colombiano"), ("Vigilancia", "Superintendencia Financiera"),
                                                      ("Inicio de la actividad", "2025"), ("Moneda principal", "Dólar estadounidense")],
                      foot="Fuente: notas a los estados financieros de 2022 y de 2025. Redacción por validar."))
     + sec("Qué es un Intermediario del Mercado Cambiario", split(
         p("Es una entidad autorizada para canalizar operaciones de cambio dentro del mercado cambiario colombiano, que regula el Banco de la República.",
           "No todos los intermediarios pueden hacer las mismas operaciones: el alcance depende del tipo de entidad y de su patrimonio. Por eso esta página publica solo las operaciones que Powwi está autorizado a realizar y que efectivamente ofrece."),
         block("Quién hace qué", datos([("Regula el régimen cambiario", "Banco de la República"), ("Vigila a la entidad", "Superintendencia Financiera"), ("Presta el servicio", "Pagos GDE S.A.")]))))
     + sec("Qué ofrece la línea", pend("Operaciones de cambio de Powwi", bullets([
         "Operaciones autorizadas y ofrecidas, con su descripción.", "Monedas.", "Tipos de cliente que atiende la línea.",
         "Condiciones, tarifas o forma de cotización.", "Horarios de operación y tiempos de liquidación."])
         + p("Lo entrega el área jurídica o de cumplimiento de Powwi. Esta propuesta no incluye texto provisional sobre operaciones de cambio.")), tone="sec-tint")
     + sec("A quién atiende", cols2(
         block("Empresas", p("Empresas que pagan o cobran en moneda extranjera.")) + block("Aliados tecnológicos", p("Plataformas de pagos que necesitan a un intermediario para formalizar la conversión de divisas de sus clientes.")),
         block("Instituciones financieras", p("Entidades que evalúan o sostienen una relación con Powwi.") + p(a("/instituciones/index.html", "Ir al perfil institucional")))
         + pend("Segmentos atendidos", p("La lista definitiva de segmentos, y si la línea atiende personas naturales, la confirma Powwi."))),
           "Estructura propuesta. El contenido de cada segmento lo valida Powwi.")
     + sec("Lo que debe quedar claro", checks([
         "Los depósitos electrónicos y las operaciones de cambio son dos líneas distintas de una misma entidad.",
         "Powwi no es un banco: es una SEDPE que opera además como Intermediario del Mercado Cambiario.",
         "Lo que el sitio dice sobre los depósitos, como el seguro de Fogafín, no se extiende a las operaciones de cambio sin validación.",
     ]), tone="sec-tint")
     + sec("Contacto de la línea", split(
         pend("Canal comercial de divisas", p("Powwi define el correo, el teléfono o el formulario existente por el que se atiende la línea.")),
         block("Mientras tanto", datos(CANALES)))),
     mejoras=[
         ("La línea IMC no aparece en ninguna de las 40 páginas del sitio.", "Sección propia en el menú principal, con la estructura lista para el contenido validado."),
         ("Los estados financieros publicados y la prensa sí la mencionan.", "El sitio dice lo mismo que los documentos de la entidad."),
         ("Un banco corresponsal no encuentra la línea que debe evaluar.", "La encuentra a un clic del inicio, en español y en inglés."),
     ])

page("divisas/como-operar.html",
     title="Cómo operar en divisas con Powwi | Pagos GDE S.A.",
     desc="El recorrido de una operación de cambio con Powwi: vinculación, documentación, negociación y liquidación.",
     sec="divisas", reg="inst", canon="/divisas/como-operar/",
     body=phero("Cómo operar", "El recorrido de una operación de cambio, desde la vinculación hasta la liquidación.",
                trail=T + [(None, "Cómo operar")])
     + sec("El recorrido", steps([
         ("Vinculación", "Conocimiento del cliente y firma de los documentos de la línea."),
         ("Documentación de la operación", "Los soportes que exige el régimen cambiario para cada operación."),
         ("Negociación", "Acuerdo de la tasa y de las condiciones."),
         ("Liquidación", "Entrega de los recursos en pesos o en divisas."),
     ]) + '<div class="mt">' + note(p("<strong>Estructura propuesta.</strong> Las cuatro etapas son el orden habitual de una operación de cambio. El detalle de cada una lo entrega Powwi."), "note-warn") + "</div>")
     + sec("Por completar", cols2(
         pend("Requisitos y documentos de vinculación", p("Para personas jurídicas y, si aplica, para personas naturales."))
         + '<div class="mt">' + pend("Tarifas y condiciones", p("Tarifas publicadas o, si la línea cotiza por operación, cómo se solicita una cotización.")) + "</div>",
         pend("Preguntas frecuentes de la línea", bullets(["¿Qué operaciones puedo hacer?", "¿Qué documentos necesito?", "¿Cómo se fija la tasa?", "¿Cuánto tarda una operación?", "¿Con quién hablo?"]))
         + '<div class="mt">' + pend("Documentos legales de la línea", p("Contratos, reglamentos y términos, con versión y fecha.")) + "</div>"), tone="sec-tint"),
     mejoras=[("No existe.", "Estructura completa de la página, sin texto provisional sobre operaciones de cambio.")])
