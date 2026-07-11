#!/usr/bin/env python3
"""Build leadership employment-reference test files.

The script mirrors the other generated test sets: individual PDFs, one combined
PDF, a ZIP archive and public copies for GitHub Pages.
"""

from __future__ import annotations

import shutil
import subprocess
import textwrap
from pathlib import Path

from reproducible_test_artifacts import normalize_pdf, write_reproducible_zip


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "testakten" / "arbeitszeugnisse-leitungsfunktionen"
DOCS_TESTAKTEN = ROOT / "docs" / "testakten"
WIDTH = 76
PROCESS_TIMEOUT_SECONDS = 120


CASES = [
    {
        "nr": "21",
        "slug": "dr-martin-rehfeld-leiter-rechtsabteilung",
        "name": "Dr. Martin Rehfeld",
        "role": "Leiter der Rechtsabteilung",
        "sector": "Mitteldeutscher Mischkonzern",
        "type": "Endzeugnis",
        "reason": "Wechsel in eine internationale Unternehmensgruppe",
        "expected": "🟢🟠; starke Leitungsrolle, aber Schaufenster-Drift zwischen Einzelprojekten und Gesamtformel",
        "text": """
        HALDENWERK INDUSTRIEGRUPPE AG
        Energie - Baustoffe - Maschinenkomponenten - Logistik
        Konzernzentrale Mitteldeutschland, Vorstandsstab Recht und Compliance
        Augustusplatz 18, 04109 Leipzig, Tel. 0341 7000-0
        HR Executive Files: LEG-DR/2026-03-RHF, Handelsregister Leipzig HRB 118820 (fiktiv)

        Leipzig, den 31. Maerz 2026

        ARBEITSZEUGNIS

        Herr Dr. Martin Rehfeld, geboren am 4. Februar 1978 in Halle (Saale), war vom
        1. Juli 2016 bis zum 31. Maerz 2026 als Leiter der Rechtsabteilung der
        Haldenwerk Industriegruppe AG beschaeftigt. Die Unternehmensgruppe buendelt
        mittelstaendisch gewachsene Aktivitaeten in den Bereichen Energie, Baustoffe,
        Maschinenkomponenten und Logistik mit rund 8.400 Mitarbeitenden im In- und
        Ausland.

        Herr Dr. Rehfeld berichtete unmittelbar an den Vorstandsvorsitzenden und
        verantwortete die konzernweite Rechtsfunktion. Zu seinem Bereich gehoerten
        Gesellschaftsrecht, Vertragsrecht, M&A, Litigation, Arbeitsrecht, Kartellrecht,
        Versicherungen, Governance, externe Kanzleisteuerung und die Schnittstelle zur
        Compliance-Organisation. Er fuehrte ein Team aus Syndikusrechtsanwaeltinnen und
        Syndikusrechtsanwaelten, Legal Operations und Assistenzkraeften an drei
        Standorten.

        In seiner Amtszeit begleitete Herr Dr. Rehfeld unter anderem mehrere
        Beteiligungserwerbe und Desinvestitionen, die Neuordnung der Konzernstruktur,
        Rahmenvertraege fuer Rohstoff- und Energiebezug, ein internationales
        Schiedsverfahren, die Einfuehrung eines Contract-Lifecycle-Managements sowie
        die juristische Flankierung eines mehrjaehrigen Restrukturierungsprogramms.
        Er koordinierte den Aufsichtsrat in rechtlichen Fragen, bereitete Beschluss-
        vorlagen vor und sorgte fuer eine belastbare Dokumentation wesentlicher
        Unternehmensentscheidungen.

        Herr Dr. Rehfeld verfuegte ueber sehr umfassende und sichere Rechtskenntnisse
        sowie ein ausgepraegtes wirtschaftliches Verstaendnis. Besonders hervorzuheben
        sind seine strategische Urteilskraft, seine Verhandlungssicherheit und seine
        Faehigkeit, komplexe rechtliche Risiken fuer Vorstand und operative
        Geschaeftsfuehrungen handhabbar aufzubereiten. In anspruchsvollen Projekten
        arbeitete er sehr strukturiert, loyal und mit grosser persoenlicher
        Einsatzbereitschaft.

        Die ihm uebertragenen Aufgaben erledigte Herr Dr. Rehfeld stets zu unserer
        vollen Zufriedenheit. Bei hohem Zeitdruck und divergierenden Interessen der
        Sparten fand er regelmaessig pragmatische und tragfaehige Loesungen. Die
        Modernisierung der Rechtsabteilung kam in wesentlichen Teilen erfolgreich voran;
        die vollstaendige Standardisierung der internationalen Vertragsprozesse blieb
        aufgrund der heterogenen Spartenstruktur anspruchsvoll.

        Herr Dr. Rehfeld fuehrte seine Mitarbeitenden sachlich, verbindlich und mit
        hohem Qualitaetsanspruch. Sein Verhalten gegenueber Vorstand, Aufsichtsrat,
        Geschaeftsfuehrungen, Mitarbeitenden, Verhandlungspartnern, Behoerden und
        externen Beraterinnen und Beratern war jederzeit einwandfrei.

        Herr Dr. Rehfeld verlaesst unser Unternehmen auf eigenen Wunsch, um eine
        internationale Leitungsfunktion zu uebernehmen. Wir danken ihm fuer die sehr
        gute und vertrauensvolle Zusammenarbeit und wuenschen ihm beruflich wie privat
        weiterhin viel Erfolg und alles Gute.

        Dr. Eva Markwardt
        Vorstand Personal und Recht

        Kai Roessler
        Vorstandsvorsitzender

        Konzernstempel: Haldenwerk Industriegruppe AG
        """,
    },
    {
        "nr": "22",
        "slug": "sabine-krueger-kaufmaennische-leiterin",
        "name": "Sabine Krüger",
        "role": "Kaufmännische Leiterin / CFO",
        "sector": "Familiengeführter Anlagenbauer",
        "type": "Endzeugnis",
        "reason": "Ruhestand nach geordneter Nachfolge",
        "expected": "🟢; sehr starkes Fuehrungszeugnis mit klarer Note 1-2 und sauberer Schlussformel",
        "text": """
        WERTHER & SOEHNE ANLAGENBAU GMBH
        Sondermaschinen - Prozessanlagen - Service
        Robert-Bosch-Strasse 6, 59423 Unna, Tel. 02303 9100-0
        Geschaeftsfuehrung: Lukas Werther, Anne Werther
        Personalzeichen: GF/CFO-SK-2026-06, Handelsregister Dortmund HRB 44218 (fiktiv)

        Unna, den 30. Juni 2026

        ARBEITSZEUGNIS

        Frau Sabine Krueger, geboren am 19. September 1963 in Dortmund, war vom
        1. Januar 2009 bis zum 30. Juni 2026 als kaufmaennische Leiterin und Mitglied
        der erweiterten Geschaeftsleitung in unserem Unternehmen taetig. Die Werther &
        Soehne Anlagenbau GmbH ist ein familiengefuehrter Anlagenbauer mit rund 620
        Mitarbeitenden, internationalem Projektgeschaeft und eigenen Serviceeinheiten.

        Frau Krueger verantwortete Finanzen, Controlling, Rechnungswesen, Treasury,
        Einkauf, Versicherungen, Vertragsadministration, kaufmaennisches Projekt-
        controlling, IT-Budgetsteuerung und die kaufmaennische Personalplanung. Sie
        fuehrte die Bereichsleitungen Rechnungswesen, Controlling, Einkauf und
        IT-Administration und berichtete unmittelbar an die Geschaeftsfuehrung.

        Zu ihren wesentlichen Leistungen zaehlten der Aufbau eines mehrstufigen
        Projektcontrollings, die Neuverhandlung der Betriebsmittellinien, die
        Stabilisierung des Working Capital, die Einfuehrung eines Risikokomitees fuer
        Grossprojekte, die Digitalisierung der Eingangsrechnungsverarbeitung sowie die
        kaufmaennische Begleitung zweier Werkserweiterungen. In schwierigen Marktphasen
        hielt sie Liquiditaet, Margenentwicklung und Investitionsfaehigkeit jederzeit
        transparent und belastbar steuerbar.

        Frau Krueger verfuegte ueber ausserordentlich breite und tiefe kaufmaennische
        Kenntnisse. Sie verband analytische Schaerfe mit grosser unternehmerischer
        Besonnenheit und hoher Umsetzungsstaerke. Ihre Vorlagen fuer Geschaeftsfuehrung,
        Beirat und Banken waren stets sehr gut strukturiert, entscheidungsreif und von
        hohem praktischen Nutzen. Auch in angespannten Projekt- und Finanzierungslagen
        blieb sie jederzeit souverain, loyal und loesungsorientiert.

        Frau Krueger erledigte die ihr uebertragenen Aufgaben stets zu unserer vollsten
        Zufriedenheit. Sie fuehrte ihre Teams vorbildlich, foerderte Nachwuchskraefte,
        schuf verlaessliche Stellvertretungsstrukturen und war fuer operative
        Projektleitungen eine geschaetzte, klare und verbindliche Ansprechpartnerin.

        Ihr Verhalten gegenueber Geschaeftsfuehrung, Beirat, Vorgesetzten,
        Kolleginnen und Kollegen, Mitarbeitenden, Banken, Pruefern, Lieferanten und
        Kunden war stets vorbildlich. Frau Krueger scheidet nach planvoller
        Nachfolgeuebergabe auf eigenen Wunsch in den Ruhestand aus. Wir bedauern ihr
        Ausscheiden sehr, danken ihr fuer die stets hervorragende und ausserordentlich
        loyale Zusammenarbeit und wuenschen ihr fuer den neuen Lebensabschnitt
        persoenlich alles Gute.

        Lukas Werther
        Geschaeftsfuehrer

        Anne Werther
        Geschaeftsfuehrerin

        Firmenstempel: Werther & Soehne Anlagenbau GmbH
        """,
    },
    {
        "nr": "23",
        "slug": "nicole-walter-leiterin-personal-arbeitsrecht",
        "name": "Nicole Walter",
        "role": "Leiterin Personal und Arbeitsrecht",
        "sector": "Kommunaler Klinikverbund",
        "type": "Endzeugnis",
        "reason": "Aufhebungsvertrag nach Reorganisation",
        "expected": "🔴/🟠; schwache Gesamtformel, Fuehrungs-/Sozialverhalten, Konflikt- und Auslassungspruefung",
        "text": """
        KLINIKVERBUND SAALERAND GGMBH
        Maximalversorgung - Fachkliniken - Pflegeakademie
        Zentrale Personalverwaltung, Am Klinikum 1, 06120 Halle (Saale)
        Personalzeichen: GL-PERS/NW-2026-04, Traegerakte: KVS-REORG-2025

        Halle (Saale), den 30. April 2026

        ARBEITSZEUGNIS

        Frau Nicole Walter, geboren am 8. Januar 1975 in Magdeburg, war vom
        1. August 2018 bis zum 30. April 2026 als Leiterin Personal und Arbeitsrecht
        unseres Klinikverbunds beschaeftigt. Der Klinikverbund Saalerand gGmbH betreibt
        drei Krankenhaeuser, zwei Medizinische Versorgungszentren und eine Pflegeakademie
        mit insgesamt rund 4.900 Beschaeftigten.

        Frau Walter verantwortete Recruiting, Personalbetreuung, Entgelt- und
        Dienstplanprozesse, arbeitsrechtliche Grundsatzfragen, Betriebsrats-
        und Einigungsstellenverfahren, Tarifumsetzung, Fuehrungskraefteberatung,
        Personalcontrolling, betriebliches Eingliederungsmanagement und die Begleitung
        von Restrukturierungs- und Digitalisierungsprojekten. Sie fuehrte ein Team aus
        HR Business Partnern, Entgeltabrechnung, Arbeitsrecht und Personalservice.

        In ihren Aufgabenbereich fielen insbesondere die Harmonisierung von
        Arbeitsvertraegen, die Begleitung einer Stationsneuordnung, Verhandlungen zu
        Dienstvereinbarungen, die Vorbereitung arbeitsgerichtlicher Verfahren, die
        Koordination externer Kanzleien sowie die Einfuehrung eines digitalen
        Bewerbermanagements. In einer Phase hoher Personalfluktuation hielt sie die
        wesentlichen HR-Prozesse aufrecht und stellte die operative Bearbeitung sicher.

        Frau Walter verfuegte ueber gute arbeitsrechtliche Kenntnisse und kannte die
        Besonderheiten des Krankenhausbetriebs. Sie arbeitete engagiert und war bereit,
        auch schwierige Themen zu uebernehmen. Die ihr uebertragenen Aufgaben erledigte
        sie im Wesentlichen zu unserer Zufriedenheit. In klar strukturierten
        Personalprozessen erzielte sie brauchbare Ergebnisse; bei komplexen
        Interessenausgleichsfragen, Kommunikation mit mehreren Gremien und nachhaltiger
        Befriedung belasteter Konfliktlagen war eine engere Abstimmung mit der
        Geschaeftsfuehrung erforderlich.

        Frau Walter fuehrte ihre Mitarbeitenden mit Nachdruck und achtete auf die
        Einhaltung vorgegebener Prozesse. Gegenueber Betriebsrat und externen
        Verhandlungspartnern vertrat sie die Interessen des Klinikverbunds bestimmt.
        Ihr Verhalten gegenueber Mitarbeitenden, Kolleginnen und Kollegen sowie der
        Geschaeftsfuehrung war insgesamt korrekt.

        Das Arbeitsverhaeltnis endet aufgrund einer einvernehmlichen Aufhebung im Zuge
        der Neuordnung der Zentralbereiche. Wir danken Frau Walter fuer die Mitarbeit
        und wuenschen ihr fuer ihren weiteren beruflichen Weg alles Gute.

        Dr. Henrik Salomon
        Geschaeftsfuehrer

        Mara Thalheim
        Vorsitzende der Geschaeftsfuehrung

        Dienststempel: Klinikverbund Saalerand gGmbH
        """,
    },
    {
        "nr": "24",
        "slug": "alexander-kunze-leiter-compliance-datenschutz",
        "name": "Alexander Kunze",
        "role": "Leiter Compliance, Datenschutz und Interne Untersuchungen",
        "sector": "Automobilzulieferer / Maschinenbau",
        "type": "Zwischenzeugnis",
        "reason": "Berichtslinienwechsel nach Konzernintegration",
        "expected": "🟢🟠; starke Projektleistung, Zwischenzeugnis-/Selbstbindung, Berichtslinie und weiche Einschraenkungen pruefen",
        "text": """
        ROTHENBURG MOTION SYSTEMS SE
        Automotive Components - Industrial Drives - Sensors
        Group Compliance Office, Gewerbepark 12, 99817 Eisenach
        compliance@rothenburg-motion.test, Personalzeichen: GCO-AK-ZW-2026-02

        Eisenach, den 28. Februar 2026

        ZWISCHENZEUGNIS

        Herr Alexander Kunze, geboren am 12. Dezember 1982 in Erfurt, ist seit dem
        1. Mai 2020 als Leiter Compliance, Datenschutz und Interne Untersuchungen bei
        der Rothenburg Motion Systems SE taetig. Dieses Zwischenzeugnis wird auf seinen
        Wunsch aus Anlass einer geaenderten Berichtslinie nach der Integration in die
        neue Konzernstruktur erteilt.

        Herr Kunze verantwortet das Compliance-Management-System, Datenschutz-
        organisation, Hinweisgebersystem, interne Untersuchungen, Schulungen, Third-
        Party-Due-Diligence, Exportkontrollschnittstellen, Richtlinienmanagement und
        Berichterstattung an Vorstand und Pruefungsausschuss. Er fuehrt ein kleines
        interdisziplinaeres Team und koordiniert lokale Compliance-Ansprechpersonen in
        sieben Laendergesellschaften.

        Seit seinem Eintritt hat Herr Kunze das Hinweisgebersystem neu aufgesetzt,
        Datenschutzfolgeabschaetzungen standardisiert, ein risikobasiertes
        Lieferantenpruefprogramm eingefuehrt, Schulungen fuer Vertrieb und Einkauf
        entwickelt und mehrere interne Untersuchungen diskret und nachvollziehbar
        gesteuert. Zudem bereitete er Vorstandsberichte auf, koordinierte externe
        Forensic-Dienstleister und begleitete die Umsetzung neuer Konzernrichtlinien.

        Herr Kunze verfuegt ueber sehr gute Kenntnisse in Compliance, Datenschutz und
        Untersuchungsfuehrung. Er arbeitet sehr gruendlich, strukturiert und mit
        ausgepraegtem Verantwortungsbewusstsein. Seine Risikoanalysen sind praezise,
        seine Berichte klar und seine Empfehlungen fuer operative Einheiten gut
        umsetzbar. Bei besonders eiligen internationalen Eskalationen bewahrte er Ruhe
        und stellte eine geordnete Dokumentation sicher.

        Die ihm uebertragenen Aufgaben erledigt Herr Kunze stets zu unserer vollen
        Zufriedenheit. Er ist ein verlaesslicher Ansprechpartner fuer Vorstand,
        Fuehrungskraefte und Fachbereiche. Die weitere Verzahnung mit Exportkontrolle
        und IT-Security befindet sich noch im Aufbau und wird durch die neue
        Konzernstruktur fortgefuehrt.

        Herr Kunze fuehrt sein Team klar, fair und fachlich ueberzeugend. Sein
        Verhalten gegenueber Vorgesetzten, Kolleginnen und Kollegen, Mitarbeitenden,
        Betriebsrat, externen Beraterinnen und Beratern sowie Behoerden ist jederzeit
        einwandfrei. Wir danken ihm fuer die bisherige sehr gute Zusammenarbeit und
        freuen uns auf die weitere Fortsetzung.

        Dr. Carola Meng
        Chief Legal & Compliance Officer

        Jens Hartenstein
        Chief Human Resources Officer

        Konzernstempel: Rothenburg Motion Systems SE
        """,
    },
    {
        "nr": "25",
        "slug": "thomas-seidel-werkleiter-industriepark",
        "name": "Thomas Seidel",
        "role": "Werkleiter / Standortleiter",
        "sector": "Chemie- und Verpackungsindustrie",
        "type": "Endzeugnis",
        "reason": "Nichtverlängerung nach Transformationsprogramm",
        "expected": "🟠 mit 🔴-Risiken; Ergebnisdruck, Sicherheit/Qualitaet, Fuehrungsverhalten und Schlussformel pruefen",
        "text": """
        ELBTAL PACKAGING & CHEMICALS GMBH
        Folien - Spezialverpackungen - Chemische Vorprodukte
        Werk Bitterfeld, Industriestrasse 40, 06749 Bitterfeld-Wolfen
        Standortakte: WL-TS/2026-01, Arbeitssicherheit: HSE-Site-Review 2025

        Bitterfeld-Wolfen, den 31. Januar 2026

        ARBEITSZEUGNIS

        Herr Thomas Seidel, geboren am 24. Juni 1971 in Dessau, war vom 1. Februar
        2017 bis zum 31. Januar 2026 als Werkleiter und Standortleiter unseres Werks
        Bitterfeld taetig. Am Standort werden Verpackungsfolien und chemische
        Vorprodukte fuer industrielle Kunden hergestellt; im Berichtszeitraum waren
        dort rund 780 Mitarbeitende beschaeftigt.

        Herr Seidel verantwortete Produktion, Instandhaltung, Arbeitssicherheit,
        Qualitaet, Werkslogistik, Investitionsplanung, Energieversorgung,
        Umweltauflagen, Produktionscontrolling und die operative Abstimmung mit
        Vertrieb, Einkauf, Betriebsrat und Konzernfunktionen. Ihm unterstanden die
        Bereichsleitungen Produktion, Technik, HSE, Qualitaet und Logistik.

        Zu den wesentlichen Projekten gehoerten die Stabilisierung einer neuen
        Extrusionslinie, ein mehrjaehriges Energieeffizienzprogramm, die Neuordnung der
        Schichtfuehrung, Investitionen in Brandschutz und Abwassertechnik sowie die
        Vorbereitung einer Automatisierungsinitiative. Herr Seidel setzte
        Ergebnisvorgaben mit Nachdruck um und erreichte in mehreren Jahren spuerbare
        Produktivitaetsverbesserungen. Gleichzeitig blieben Anlagenverfuegbarkeit,
        Reklamationsquote und die nachhaltige Einbindung der zweiten Fuehrungsebene
        wiederholt Gegenstand enger Abstimmung mit der Geschaeftsfuehrung.

        Herr Seidel verfuegte ueber breite technische und betriebswirtschaftliche
        Kenntnisse des Produktionsbetriebs. Er arbeitete zielorientiert, belastbar und
        mit hoher Praesenz am Standort. Die ihm uebertragenen Aufgaben erledigte er zu
        unserer vollen Zufriedenheit. In Phasen hohen Kostendrucks zeigte er grosse
        Einsatzbereitschaft; bei kommunikativer Begleitung von Veraenderungen und
        laengerfristiger Fuehrungskraefteentwicklung bestanden unterschiedliche
        Erwartungen.

        Herr Seidel fuehrte seine Mitarbeitenden konsequent und achtete auf die
        Einhaltung von Vorgaben. Sein Verhalten gegenueber Vorgesetzten, Kolleginnen
        und Kollegen, Mitarbeitenden, Betriebsrat, Lieferanten und Behoerden war
        einwandfrei.

        Das Arbeitsverhaeltnis endet mit Ablauf der vereinbarten Vertragsverlaengerung
        im Zusammenhang mit der Neuausrichtung des Standorts. Wir danken Herrn Seidel
        fuer die geleistete Arbeit und wuenschen ihm fuer die Zukunft alles Gute.

        Dr. Renate Wirth
        Geschaeftsfuehrerin Operations

        Holger Mertens
        Leiter Personal Deutschland

        Firmenstempel: Elbtal Packaging & Chemicals GmbH
        """,
    },
]


def wrapped(text: str) -> str:
    lines: list[str] = []
    for raw in textwrap.dedent(text).strip().splitlines():
        line = raw.strip()
        if not line:
            lines.append("")
            continue
        if line.isupper() and len(line) < 90:
            lines.append(line)
            continue
        lines.extend(textwrap.wrap(line, width=WIDTH, break_long_words=False) or [""])
    return "\n".join(lines) + "\n"


def write_pdf(text: str, pdf_path: Path, title: str) -> None:
    txt_path = pdf_path.with_suffix(".txt")
    txt_path.write_text(wrapped(text), encoding="utf-8")
    try:
        with pdf_path.open("wb") as out:
            subprocess.run(
                [
                    "cupsfilter",
                    "-i",
                    "text/plain",
                    "-m",
                    "application/pdf",
                    "-o",
                    "media=A4",
                    "-t",
                    title,
                    str(txt_path),
                ],
                stdout=out,
                stderr=subprocess.DEVNULL,
                check=True,
                timeout=PROCESS_TIMEOUT_SECONDS,
            )
    finally:
        txt_path.unlink(missing_ok=True)
    normalize_pdf(pdf_path)


def write_expectations() -> None:
    rows = "\n".join(
        f"| {c['nr']} | {c['name']} | {c['expected']} |"
        for c in CASES
    )
    text = f"""# Erwartungshorizont und Pruefpunkte — Leitungsfunktionen

Diese Liste ist kein Loesungsschluessel, sondern ein Pruefhorizont. Die Skill-Ausgabe darf abweichen, wenn sie die Abweichung aus Zeugnistext, Rolle und rechtlichem Anker begruendet.

| Nr. | Fall | Erwartete Hauptpruefung |
| --- | --- | --- |
{rows}

## Besondere Lernziele

- **Leitungsrollen:** Berichtslinie, Fuehrungsspanne, Budget, Gremiennaehe und Entscheidungsbefugnis sauber auswerten.
- **Schaufenster-Drift:** Einzelprojekte und Spitzensaetze gegen Gesamtformel, Schlussformel und Fuehrungsbeurteilung lesen.
- **Stakeholder:** Vorstand, Geschaeftsfuehrung, Aufsichtsrat, Betriebsrat, Behoerden, Banken, Kunden und externe Berater rollenbewusst beruecksichtigen.
- **Transformation:** Restrukturierung, Integration, Digitalisierung und Standortprogramme nicht automatisch als Mangel oder Erfolg ueberbewerten.
- **Beendigungsgrund:** Ruhestand, Eigenwechsel, Reorganisation, Aufhebungsvertrag, Nichtverlaengerung und Zwischenzeugnisanlass getrennt pruefen.
"""
    (OUT / "90-erwartungshorizont-und-pruefpunkte.md").write_text(text, encoding="utf-8")


def main() -> None:
    for tool in ("cupsfilter", "pdfunite"):
        if not shutil.which(tool):
            raise SystemExit(f"missing required tool: {tool}")

    OUT.mkdir(parents=True, exist_ok=True)
    for child in OUT.iterdir():
        is_generated_case = (
            child.is_dir()
            and len(child.name) > 3
            and child.name[:2].isdigit()
            and child.name[2] == "-"
        )
        if is_generated_case:
            shutil.rmtree(child)
    combined_dir = OUT / "gesamt-pdf"
    if combined_dir.exists():
        shutil.rmtree(combined_dir)
    combined_dir.mkdir()
    DOCS_TESTAKTEN.mkdir(parents=True, exist_ok=True)

    pdfs: list[Path] = []
    for case in CASES:
        folder = OUT / f"{case['nr']}-{case['slug']}"
        folder.mkdir(parents=True)
        pdf = folder / f"Arbeitszeugnis_{case['nr']}-{case['slug']}.pdf"
        write_pdf(case["text"], pdf, f"Arbeitszeugnis {case['nr']} {case['name']}")
        pdfs.append(pdf)

    combined = combined_dir / "arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"
    subprocess.run(
        ["pdfunite", *map(str, pdfs), str(combined)],
        check=True,
        timeout=PROCESS_TIMEOUT_SECONDS,
    )
    normalize_pdf(combined)

    zip_path = OUT / "arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"
    write_reproducible_zip(zip_path, OUT, pdfs)

    write_expectations()

    shutil.copy2(zip_path, DOCS_TESTAKTEN / zip_path.name)
    shutil.copy2(combined, DOCS_TESTAKTEN / combined.name)

    print(f"wrote {len(pdfs)} PDFs")
    print(f"wrote {combined.relative_to(ROOT)}")
    print(f"wrote {zip_path.relative_to(ROOT)}")
    print("copied public downloads to docs/testakten/")


if __name__ == "__main__":
    main()
