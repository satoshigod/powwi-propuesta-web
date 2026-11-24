from .base import *  # noqa: F401,F403
from .datos import DOC

DRAFT = note("<p><strong>Draft translation.</strong> Regulated terms (SEDPE, IMC, supervised entity, electronic deposit) must be validated by Powwi before publication.</p>", "note-warn")
PEND = "Pending input from Powwi"


def pend_en(title, body):
    return pend(title, body, tag=PEND)


FICHA = ficha("Entity record", [
    ("Legal name", "Pagos GDE S.A."), ("Tax ID (NIT)", "901.077.411-3"), ("Entity type", "SEDPE"),
    ("Supervisor", "Superintendencia Financiera de Colombia"), ("Deposit insurance", "Fogafín"), ("FX status", "IMC"),
], foot='From the website and the published financial statements. <a href="/en/institutions.html">Open the institutional profile</a>')

page("en/index.html", lang="en",
     title="Powwi: electronic deposits, payments and FX | Pagos GDE S.A.",
     desc="Powwi is the brand of Pagos GDE S.A., a Colombian electronic deposit and payment company supervised by the Superintendencia Financiera. It also operates as an FX market intermediary.",
     sec="en-home", reg="inst", canon="/en/", alt="/index.html",
     body=f'''<section class="hero-home on-dark"><div class="wrap hh"><div>
<h1>Electronic deposits, payments and foreign exchange under one supervised entity</h1>
<p class="lead">Powwi is the brand of Pagos GDE S.A., a Colombian electronic deposit and payment company (SEDPE) supervised by the Superintendencia Financiera de Colombia. It also operates as a foreign exchange market intermediary (IMC).</p>
{acts(btn("/en/institutions.html", "Institutional profile", "light"), btn("/en/fx.html", "Foreign exchange", "ghost"))}
</div>{FICHA}</div></section>'''
     + sec("", DRAFT)
     + sec("Where to go", ll([
         ("/en/institutions.html", "Institutions and partners", "Authorisations, governance, compliance and financial statements."),
         ("/en/fx.html", "Foreign exchange", "The IMC line: regulatory framework and how to engage."),
         ("/en/business.html", "Business solutions", "Business deposit, instant payments, collections, payouts and Banking as a Service."),
         ("/en/about.html", "About Powwi", "Who we are and how we got here."),
         ("/en/contact.html", "Contact", "Phone lines, email and office address."),
     ]))
     + sec("Two business lines, one entity", cols2(
         linea("Electronic deposits and payments", p("As a SEDPE, Powwi takes funds from the public in electronic deposits and provides payments, transfers and remittances. It does not grant credit.")),
         linea("Foreign exchange", p("As a foreign exchange market intermediary, Powwi carries out exchange operations under Colombia's foreign exchange regime.") + pend_en("Scope of the line", p("Authorised operations and conditions are published with the wording Powwi validates.")), fx=True)), tone="sec-tint")
     + sec("Personal products", p("Deposits and services for individuals are offered in Colombia and described in Spanish.") + p(a("/personas/index.html", "Personas (Spanish)"))))

page("en/institutions.html", lang="en",
     title="Institutional profile | Pagos GDE S.A. (Powwi)",
     desc="Institutional profile of Pagos GDE S.A. (Powwi): entity type, authorisations, supervisors, governance, compliance and financial statements.",
     sec="en-inst", reg="inst", canon="/en/institutions/", alt="/instituciones/index.html",
     body=phero("Institutional profile", "What a bank, a partner or a regulator needs to know about Pagos GDE S.A., in one place.",
                acts(btn("/en/institutions.html#compliance", "Compliance", "light"), btn("/en/institutions.html#financials", "Financial statements", "ghost")),
                ficha("Pagos GDE S.A.", [("Brand", "Powwi"), ("Tax ID (NIT)", "901.077.411-3"), ("Entity type", "SEDPE"),
                                          ("Domicile", "Bogotá, Colombia"), ("Incorporated", "27 April 2017"), ("Operating since", "25 January 2019")]))
     + sec("", DRAFT)
     + sec("Authorisations and supervision", table("Incorporation and authorisations", ["Milestone", "Date", "Status"], [
         ("Authorisation to incorporate. Superintendencia Financiera, Resolution 0546", "7 April 2017", "Published"),
         ("Deed of incorporation No. 729, Notary 41 of Bogotá", "27 April 2017", "Published"),
         ("Operating licence. Superintendencia Financiera, Resolution 0943", "25 July 2018", "To be validated"),
         ("Start of operations", "25 January 2019", "Published"),
         ("Foreign exchange market intermediary status. Banco de la República", "February 2020 (official letter)", "To be validated"),
         ("Start of IMC activity", "2025", "To be validated"),
     ]))
     + sec("Supervisors and protection", cols3(
         block("Superintendencia Financiera de Colombia", p("Authorises and supervises the entity.")),
         block("Fogafín", p("Deposits are covered by deposit insurance, up to COP 50 million per depositor.")),
         block("Banco de la República", p("Regulates the foreign exchange regime under which the FX line operates."))), tone="sec-tint")
     + sec("Governance", pend_en("Ownership, board and senior management", bullets(["Shareholders and beneficial owners.", "Board of directors and committees.", "Senior management.", "Compliance officer.", "Statutory auditor."])), id="governance")
     + sec("Compliance", docs([
         ("SARLAFT certification 2025", "PDF, in Spanish. Anti-money laundering and counter-terrorist financing risk system.", DOC["sarlaft"], "Open"),
         ("SARO certification 2025", "PDF, in Spanish. Operational risk system.", DOC["saro"], "Open"),
         ("Wolfsberg questionnaire (CBDDQ), USA PATRIOT Act certification, W-8BEN-E", "If they exist and apply. Published or provided on request.", None, ""),
     ]), id="compliance", tone="sec-tint")
     + sec("Financial statements", docs([
         ("Financial statements 2025", "PDF, in Spanish. With notes and the statutory auditor's opinion.", DOC["eeff2025"], "Open"),
         ("English summary of the financial statements", "Not available today.", None, ""),
     ]), id="financials")
     + sec("Institutional contact", split(
         pend_en("Institutional relations and compliance", p("Name, role, email and phone of the person who serves financial institutions, and of the compliance officer.")),
         block("Head office", datos([("Address", "Ac. 26 # 69D-91, 9th floor, Bogotá"), ("Phone", '<a href="tel:+576014030555">+57 601 403 0555</a>'), ("Email", '<a href="mailto:escribenos@powwi.co">escribenos@powwi.co</a>')]))), tone="sec-tint"))

page("en/fx.html", lang="en",
     title="Foreign exchange: Powwi's IMC line | Pagos GDE S.A.",
     desc="Powwi operates as a foreign exchange market intermediary (IMC) in Colombia. Regulatory framework and how to engage.",
     sec="en-fx", reg="inst", canon="/en/fx/", alt="/divisas/index.html",
     body=phero("Foreign exchange: Powwi's IMC line", "Powwi operates as a foreign exchange market intermediary in Colombia. This section presents the line to businesses, partners and financial institutions.",
                aside=ficha("The line in public records", [("Entity", "Pagos GDE S.A."), ("Status", "Foreign exchange market intermediary"), ("Framework", "Colombian FX regime"),
                                                              ("Supervision", "Superintendencia Financiera"), ("Activity started", "2025"), ("Main currency", "US dollar")],
                             foot="Source: notes to the 2022 and 2025 financial statements. Wording to be validated."))
     + sec("", DRAFT)
     + sec("What an IMC is", p("A foreign exchange market intermediary is an entity authorised to channel exchange operations within Colombia's foreign exchange market, which is regulated by Banco de la República.",
                               "Not every intermediary can carry out the same operations: the scope depends on the type of entity and its capital. This page only lists the operations Powwi is authorised to carry out and actually offers."))
     + sec("What the line offers", pend_en("Powwi's exchange operations", bullets(["Authorised operations offered.", "Currencies.", "Client segments.", "Conditions, fees or quotation process.", "Operating hours and settlement times."])), tone="sec-tint")
     + sec("How to engage", steps([("Onboarding", "Know-your-customer and signing of the line's documents."), ("Operation documents", "The supporting documents required by the FX regime."),
                                   ("Negotiation", "Agreement on rate and conditions."), ("Settlement", "Delivery of funds in pesos or foreign currency.")])
           + '<div class="mt">' + note("<p><strong>Proposed structure.</strong> Powwi provides the detail of each stage.</p>", "note-warn") + "</div>"))

page("en/business.html", lang="en",
     title="Business solutions | Powwi",
     desc="Powwi business deposit, instant payments with Bre-B, collections and payouts, and Banking as a Service.",
     sec="en-business", reg="inst", canon="/en/business/", alt="/empresas/index.html",
     body=phero("Business solutions", "A business deposit, collections and payouts through Powwi's channels, instant payments with Bre-B, and financial services embedded in your platform.",
                acts(btn("/en/contact.html", "Contact us", "light")))
     + sec("", DRAFT)
     + sec("Solutions", cols2(
         block("Powwi Negocios", p("An ordinary deposit for businesses, with no balance or withdrawal cap.")) + block("Bre-B for business", p("Instant payments between banks, wallets and deposits, at any time.")),
         block("Collections and payouts", p("Pay many recipients and collect with a reference number. Also available with APIs to connect your ERP.")) + block("Banking as a Service", p("Offer financial services inside your platform. Pagos GDE S.A. is the licensed entity and administers the deposits."))))
     + sec("Details in Spanish", ll([("/empresas/index.html", "Empresas", "Full description of each solution, contracts and portal access.")]), tone="sec-tint"))

page("en/about.html", lang="en",
     title="About Powwi | Pagos GDE S.A.",
     desc="Powwi is the brand of Pagos GDE S.A., a Colombian digital financial entity. Purpose, history and business lines.",
     sec="en-about", reg="inst", canon="/en/about/", alt="/nosotros/index.html",
     body=phero("About Powwi", "We are a Colombian digital financial entity. We work so that more people and businesses use financial services, with less cash and less informality.")
     + sec("", DRAFT)
     + sec("History", table("Milestones", ["Year", "Milestone", "Status"], [
         ("2015", "Pagos GDE trademark registered.", "Published"),
         ("2017", "Authorisation to incorporate, deed of incorporation and commercial registration.", "Published"),
         ("2018", "Operating licence from the Superintendencia Financiera.", "To be validated"),
         ("2019", "Start of operations.", "Published"),
         ("2020", "Foreign exchange market intermediary status.", "To be validated"),
         ("2025", "Bre-B instant payments and start of the FX activity.", "To be validated"),
     ]))
     + sec("More", ll([("/en/institutions.html", "Institutional profile", "Authorisations, governance, compliance and financials."), ("/en/fx.html", "Foreign exchange", "The IMC line.")]), tone="sec-tint"))

page("en/contact.html", lang="en",
     title="Contact | Powwi",
     desc="Phone lines, email and office address of Powwi (Pagos GDE S.A.).",
     sec="en-contact", reg="inst", canon="/en/contact/", alt="/ayuda/contacto.html",
     body=phero("Contact", "Phone lines, email and office address.",
                aside=ficha("Channels", [("Bogotá", '<a href="tel:+576014030555">+57 601 403 0555</a>'), ("Medellín", '<a href="tel:+576042040870">+57 604 204 0870</a>'),
                                         ("Email", '<a href="mailto:escribenos@powwi.co">escribenos@powwi.co</a>'), ("Hours", "Mon to Fri, 7:00 a.m. to 5:00 p.m."), ("Office", "Ac. 26 # 69D-91, 9th floor, Bogotá")]))
     + sec("", DRAFT)
     + sec("For financial institutions", pend_en("Institutional and compliance contact", p("A named contact for correspondent banks and partners, with email and phone.")))
     + sec("Whistleblowing channel", p('<a href="mailto:denuncias@powwi.co">denuncias@powwi.co</a>'), tone="sec-tint"))
