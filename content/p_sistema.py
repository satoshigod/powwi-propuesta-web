"""Página del sistema de diseño de la propuesta."""
from .base import *  # noqa: F401,F403
from .p_propuesta import contraste

T = [("/propuesta/index.html", "Propuesta"), (None, "Sistema de diseño")]

COL = [("Blanco", "#FFFFFF", "Fondo de todo el sitio"), ("Tinta", "#12163B", "Texto y pie de página"), ("Azul Powwi", "#3F59E2", "Único acento: acciones y enlaces"),
       ("Papel", "#F6F7FA", "Tarjetas y franjas alternas"), ("Línea", "#E7E9F1", "Divisiones finas"), ("Efectivo", "#FFC83D", "Solo en la figura de la portada")]
sw = '<ul class="swatches">' + "".join(f'<li><i style="background:{h}"></i><strong>{n}</strong><br>{h}<br>{u}</li>' for n, h, u in COL) + "</ul>"
PARES = [("Tinta sobre blanco", "#12163B", "#FFFFFF"), ("Texto secundario sobre blanco", "#3A3F63", "#FFFFFF"), ("Texto de apoyo sobre blanco", "#62688A", "#FFFFFF"),
         ("Texto de apoyo sobre Papel", "#62688A", "#F6F7FA"), ("Azul Powwi sobre blanco", "#3F59E2", "#FFFFFF"), ("Azul Powwi sobre Papel", "#3F59E2", "#F6F7FA"),
         ("Blanco sobre Azul Powwi", "#FFFFFF", "#3F59E2"), ("Blanco sobre Tinta", "#FFFFFF", "#12163B"), ("Texto del pie sobre Tinta", "#A9AED0", "#12163B")]
CONTRASTES = [(n, contraste(x, y)) for n, x, y in PARES]
contr = table("Contraste de color", ["Combinación", "Relación", "Texto normal (mínimo 4,5)"], [
    (n, ("%.1f a 1" % c).replace(".", ","), "Cumple" if c >= 4.5 else "Solo texto grande") for n, c in CONTRASTES], num=(1,))

page("propuesta/sistema-de-diseno.html",
     title="Sistema de diseño de la propuesta | Powwi",
     desc="Paleta, tipografía y componentes del sitio propuesto para Powwi: fondo blanco, un solo acento y una familia tipográfica.",
     sec="propuesta", reg="inst",
     body=phero("Sistema de diseño", "Fondo blanco, un solo color de acento, una familia tipográfica y una idea por pantalla.", trail=T)
     + sec("Principios", cols3(
         block("Blanco primero", p("El sitio descansa en el blanco y en el espacio. El color aparece para indicar una acción, no para decorar.")),
         block("Una idea por pantalla", p("Cada sección dice una cosa y ofrece una acción. El detalle vive un nivel más abajo.")),
         block("Datos en texto", p("Cifras, topes, fechas y versiones se escriben, no se pegan como imagen. Lo que falta por validar se marca en voz baja."))))
     + sec("Color", sw + '<div class="mt">' + contr + "</div>", "Se conserva el azul actual de Powwi como único acento. Todo lo demás es blanco, tinta y gris.", tone="sec-tint")
     + sec("Tipografía", cols2(
         '<p class="specimen">Figtree</p>' + p("Una sola familia para títulos, texto e interfaz. Títulos grandes y apretados; texto de 17 px con interlínea amplia; cifras tabulares en las tablas."),
         table("Escala", ["Uso", "Tamaño", "Peso"], [("Título de portada", "44 a 82 px", "600"), ("Título de página", "40 a 68 px", "600"), ("Título de sección", "30 a 42 px", "600"),
                                                      ("Subtítulo", "21 px", "600"), ("Texto", "17 px", "400"), ("Notas y metadatos", "14 a 15 px", "400 a 500")])))
     + sec("Componentes", cols2(
         block("Ficha de datos", ficha("Ficha", [("Dato", "Valor"), ("Otro dato", "Otro valor")], foot="Para lo que una persona o un banco busca primero.", tag="h4"))
         + block("Botones", acts(btn("/propuesta/sistema-de-diseno.html", "Principal"), btn("/propuesta/sistema-de-diseno.html", "Secundario", "line")))
         + block("Documentos", docs([("Nombre del documento", "Formato. Versión y fecha.", "/legal/index.html", "Abrir")])),
         block("Pasos", steps([("Primer paso", "Solo para secuencias reales."), ("Segundo paso", "La numeración informa el orden.")]))
         + block("Pendiente de validar", pend("Contenido por validar", p("Marca lo que falta. No forma parte del sitio final.")))
         + block("Preguntas", acc([("¿Cómo se ve una pregunta?", p("Se abre y se cierra sin recargar la página."))]))), tone="sec-tint")
     + sec("Lo que cambia entre públicos", table("Una identidad para todos", ["Público", "Qué cambia", "Qué no cambia"], [
         ("Personas y ayuda", "Lenguaje cotidiano, pasos y cifras a la vista", "Color, tipografía y componentes"),
         ("Empresas", "Lenguaje comercial y una acción: solicitar una reunión", "Color, tipografía y componentes"),
         ("Divisas, instituciones y legal", "Lenguaje exacto, tablas y documentos con versión", "Color, tipografía y componentes"),
     ]))
     + sec("Accesibilidad y rendimiento", checks([
         "Objetivo: WCAG 2.2 nivel AA.", "Un título principal por página y jerarquía de títulos ordenada.", "Enlace para saltar al contenido y foco visible con el teclado.",
         "Tablas con encabezados y título; formularios con etiquetas.", "Información en texto, no en imágenes.", "Sin animaciones automáticas.",
         "Sin dependencias externas: una tipografía alojada en el sitio, una hoja de estilos y un guion pequeño."]), tone="sec-tint")
     + sec("Lo que falta decidir", pend("Fotografía y logotipo", p("El prototipo no usa fotografía ni el logotipo de Powwi. Los referentes internacionales se apoyan en imagen propia: es la siguiente decisión de marca."), tag="Decisión de Powwi")))
