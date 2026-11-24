"""Datos y direcciones oficiales reutilizados en varias páginas. Todo sale del sitio público actual."""
from .base import off, a

DOC = {
    "eeff2025": off("/wp-content/uploads/2026/04/Estados-Financieros-Powwi-2025.pdf"),
    "eeff2022": off("/wp-content/uploads/2023/08/NOTAS-EEFF-2022_DEFINITIIVAS-060823-REV-11-JUL-CORRe-1-1.pdf"),
    "sarlaft": off("/wp-content/uploads/2025/09/Certificacion-SARLAFT-2025.pdf"),
    "saro": off("/wp-content/uploads/2025/09/Certificacion-SARO-2025.pdf"),
    "reglamento": off("/wp-content/uploads/2026/11/GL-RG-008DepsitodeDineroElectrnicoV4.pdf"),
    "topes": off("/wp-content/uploads/2025/12/Montos-y-Topes-2026-Final.pdf"),
    "tarifas_pn": off("/wp-content/uploads/2026/01/Banner-De-Tarifas-V3.png"),
    "tarifas_pj": off("/wp-content/uploads/2025/12/Banner-De-TarifasJuridicaActualizado.png"),
    "tarifas_2022": off("/tarifas-2022/"),
    "breb": off("/wp-content/uploads/2025/08/TyC-Powwi-Bre-B.pdf"),
    "reversion": off("/wp-content/uploads/2026/09/GE-IN-005.pdf"),
    "infografia": off("/wp-content/uploads/2024/11/INFOGRAFIA_compressed.pdf"),
    "contrato_dr": off("/wp-content/uploads/2026/01/CONTRATO-DE-ADHN-DISPERSION-Y-RECAUDO-BASICO-Regular-VERSION-2026-2-2-1-1.pdf"),
    "contrato_draas": off("/wp-content/uploads/2026/01/CONTRATO-ADHN-DISPERSION-Y-RECAUDO-AS-A-SERVICE-Regular-version-01.2026-1-2-1-1.pdf"),
    "datos_pdf": off("/wp-content/uploads/2026/09/SI-MA-007PolticadeProteccindeDatosPersonalesV5.pdf"),
    "datos": off("/politica-de-tratamiento-de-datos/"),
    "privacidad": off("/aviso-de-privacidad/"),
    "cookies": off("/politica-de-cookies/"),
    "sfc_queja": "https://www.superfinanciera.gov.co/publicacion/20650",
    "linkedin": "https://www.linkedin.com/company/powwico/",
}

STORES = [
    ("https://play.google.com/store/apps/details?id=com.comppra.powwi", "Google Play", "Para celulares Android."),
    ("https://apps.apple.com/co/app/powwi/id1382825759", "App Store", "Para iPhone."),
    ("https://appgallery.huawei.com/#/app/C102427067", "AppGallery", "Para celulares Huawei."),
]

PORTAL_POWWI = "https://banking.powwi.co/odigemp/aplicacion/?id=20CEA5081E844B979766D786E70520EA#/login"
PORTAL_BREB = "https://servicesapp.powwi.co/portal-powwi/index.html"
ACCESO_OFICIAL = off("/accesoportalempresas/")

# Montos y topes 2026 (transcripción para la propuesta)
TOPES_HEAD = ["Operación", "Powwi Ágil", "Powwi Más", "Powwi Negocios"]
TOPES = [
    ("Recarga en corresponsal", "$1.000.000<br>hasta 3 operaciones", "$1.000.000<br>hasta 5 operaciones", "No aplica"),
    ("Recarga por PSE", "$11.024.727", "Sin límite", "Sin límite"),
    ("Envío a otros bancos", "$11.024.727", "Sin límite", "Sin límite"),
    ("Retiro en corresponsal", "$1.000.000<br>hasta 3 operaciones", "$1.000.000<br>hasta 5 operaciones", "No aplica"),
    ("Envío por Bre-B", "$3.000.000", "$3.000.000", "$3.000.000"),
]
NOTA_TOPES = ("Transcrito del documento " + a(DOC["topes"], "Montos y topes 2026") +
              " para esta propuesta: validar antes de publicar. El documento no indica a qué periodo corresponde el máximo de operaciones.")


def topes_de(col, caption):
    """Tabla de topes de un solo depósito. col: 1 Ágil, 2 Más, 3 Negocios."""
    from .base import table
    rows = [(r[0], r[col]) for r in TOPES]
    return table(caption, ["Operación", "Tope por operación"], rows, note=NOTA_TOPES)


PASOS_ABRIR = [
    ("Descarga Powwi App", "Desde la tienda oficial de tu celular."),
    ("Toca Crea tu Powwi", "Es la primera opción al abrir la app."),
    ("Escribe tu número de celular", "Debe ser una línea colombiana."),
    ("Ingresa el código que te llega por SMS", "Así confirmamos que la línea es tuya."),
    ("Crea y confirma tu contraseña", "La usarás cada vez que entres."),
    ("Completa tus datos", "Solo los que la app te pide."),
]

DEPTOS = [
    ("Amazonas", "AMAZONAS"), ("Antioquia", "ANTIOQUIA"), ("Arauca", "ARAUCA"), ("Atlántico", "ATLANTICO"),
    ("Bogotá", "BOGOTA-D.C."), ("Bolívar", "BOLIVAR"), ("Boyacá", "BOYACA"), ("Caldas", "CALDAS"),
    ("Caquetá", "CAQUETA"), ("Casanare", "CASANARE"), ("Cauca", "CAUCA"), ("Cesar", "CESAR"), ("Chocó", "CHOCO"),
    ("Córdoba", "CORDOBA"), ("Cundinamarca", "CUNDINAMARCA"), ("Guainía", "GUAINIA"), ("Guaviare", "GUAVIARE"),
    ("Huila", "HUILA"), ("La Guajira", "LA-GUAJIRA"), ("Magdalena", "MAGDALENA"), ("Meta", "META"),
    ("Nariño", "NARINO"), ("Norte de Santander", "NORTE-DE-SANTANDER"), ("Putumayo", "PUTUMAYO"),
    ("Quindío", "QUINDIO"), ("Risaralda", "RISARALDA"), ("San Andrés y Providencia", "SAN-ANDRES"),
    ("Santander", "SANTANDER"), ("Sucre", "SUCRE"), ("Tolima", "TOLIMA"), ("Valle del Cauca", "VALLE-DEL-CAUCA"),
    ("Vichada", "VICHADA"),
]


def depto_url(code):
    sep = "" if code.endswith(".") else "-"
    return off("/wp-content/uploads/2026/04/%s%sMARZO-2026.pdf" % (code, sep))


CANALES = [
    ("Bogotá", '<a href="tel:+576014030555">601 403 0555</a>'),
    ("Medellín", '<a href="tel:+576042040870">604 204 0870</a>'),
    ("WhatsApp", "310 414 5841"),
    ("Correo", '<a href="mailto:escribenos@powwi.co">escribenos@powwi.co</a>'),
    ("Horario", "Lunes a viernes, 7:00 a. m. a 5:00 p. m."),
]
