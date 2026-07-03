#!/usr/bin/env python3
"""Build the legal/academic employment-reference test files.

The script intentionally uses system tools already present on macOS:
`cupsfilter` for text-to-PDF and `pdfunite` for the combined PDF.
"""

from __future__ import annotations

import shutil
import subprocess
import textwrap
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "testakten" / "arbeitszeugnisse-jura-und-wissenschaft"
DOCS_TESTAKTEN = ROOT / "docs" / "testakten"
WIDTH = 88


CASES = [
    {
        "nr": "11",
        "slug": "johanna-kirchhoff-wissmit-zivilrecht",
        "name": "Johanna Kirchhoff",
        "role": "Wissenschaftliche Mitarbeiterin am juristischen Lehrstuhl",
        "sector": "Universität / Zivilrecht",
        "type": "Endzeugnis",
        "reason": "Promotionsabschluss und Wechsel ins Referendariat",
        "expected": "überwiegend 🟢; klare Note 1-2, aber Lehr-/Publikationsanteile sauber prüfen",
        "text": """
        UNIVERSITAET ALBSTADT - JURISTISCHE FAKULTAET
        Lehrstuhl fuer Buergerliches Recht, Handels- und Gesellschaftsrecht
        Parkring 12, 70199 Albstadt, Tel. 0711 4000-211, sekretariat.zivilrecht@uni-albstadt.test

        Albstadt, den 30. September 2025

        ARBEITSZEUGNIS

        Frau Johanna Kirchhoff, geboren am 14. Mai 1997 in Tuebingen, war vom
        1. Oktober 2021 bis zum 30. September 2025 als wissenschaftliche Mitarbeiterin
        an unserem Lehrstuhl fuer Buergerliches Recht, Handels- und Gesellschaftsrecht
        beschaeftigt.

        Zu ihren Aufgaben gehoerten die Vorbereitung und Nachbereitung von Vorlesungen
        und Arbeitsgemeinschaften, die Recherche fuer wissenschaftliche Publikationen,
        die Erstellung von Gutachtenvermerken, die Betreuung von Seminararbeiten sowie
        die organisatorische Unterstuetzung von Tagungen und Moot-Court-Formaten.

        Frau Kirchhoff verfuegte jederzeit ueber ausgezeichnete juristische Kenntnisse
        und verband dogmatische Praezision mit einem sicheren Blick fuer praktische
        Anschlussfragen. Neue Themen erschloss sie sich stets sehr schnell, gruendlich
        und selbststaendig. Ihre schriftlichen Vorarbeiten waren durchweg klar
        strukturiert, sprachlich sehr sorgfaeltig und wissenschaftlich belastbar.

        Auch bei hoher Fristendichte arbeitete Frau Kirchhoff stets sehr zuverlaessig,
        planvoll und mit bemerkenswerter Eigeninitiative. Die ihr uebertragenen Aufgaben
        erledigte sie stets zu unserer vollsten Zufriedenheit. In Lehrveranstaltungen
        trat sie sicher, freundlich und foerdernd auf; Studierende und Kollegium
        schaetzten ihre ruhige, verbindliche und fachlich praezise Art.

        Ihr Verhalten gegenueber Vorgesetzten, Kolleginnen und Kollegen, Studierenden
        sowie externen Gaesten war stets einwandfrei. Frau Kirchhoff verlaesst den
        Lehrstuhl nach erfolgreichem Abschluss ihres Promotionsvorhabens auf eigenen
        Wunsch, um in den juristischen Vorbereitungsdienst einzutreten. Wir bedauern
        ihr Ausscheiden sehr, danken ihr fuer die stets hervorragende Zusammenarbeit
        und wuenschen ihr beruflich und persoenlich weiterhin viel Erfolg und alles Gute.

        Prof. Dr. Miriam Hagedorn
        Lehrstuhlinhaberin
        """,
    },
    {
        "nr": "12",
        "slug": "tobias-rauch-wissmit-strafrecht",
        "name": "Tobias Rauch",
        "role": "Wissenschaftlicher Mitarbeiter am Lehrstuhl fuer Strafrecht",
        "sector": "Universität / Strafrecht",
        "type": "Endzeugnis",
        "reason": "Auslaufen der Projektbefristung",
        "expected": "🟠 mit einzelnen 🔴-Signalen; Auslassungen, Abschwaechungen und Schlussformel pruefen",
        "text": """
        RHEINISCHE UNIVERSITAET NORDSTADT - FAKULTAET FUER RECHTSWISSENSCHAFT
        Lehrstuhl fuer Strafrecht, Strafprozessrecht und Wirtschaftsstrafrecht
        Universitaetsallee 8, 41001 Nordstadt, Tel. 0211 7710-88

        Nordstadt, den 31. Maerz 2026

        ARBEITSZEUGNIS

        Herr Tobias Rauch, geboren am 3. Februar 1995 in Essen, war vom 1. April 2023
        bis zum 31. Maerz 2026 als wissenschaftlicher Mitarbeiter an unserem Lehrstuhl
        beschaeftigt.

        Herr Rauch unterstuetzte die Arbeit des Lehrstuhls insbesondere durch
        Rechtsprechungsrecherchen, Literaturauswertungen, Entwuerfe fuer Fallloesungen,
        die Pflege von Lehrmaterialien und die Mitwirkung an einem drittmittelgefoerderten
        Forschungsprojekt zum Unternehmensstrafrecht.

        Er verfuegte ueber solide strafrechtliche Kenntnisse und zeigte Interesse an
        komplexen wissenschaftlichen Fragestellungen. Die ihm uebertragenen Aufgaben
        bearbeitete er im Allgemeinen sorgfaeltig. Bei klar umrissenen Arbeitsauftraegen
        erzielte Herr Rauch brauchbare Ergebnisse; bei offenen Forschungsfragen benoetigte
        er gelegentlich eine engere Abstimmung.

        Herr Rauch erledigte seine Aufgaben zu unserer vollen Zufriedenheit. Er war
        belastbar, wenn Prioritaeten vorgegeben waren, und brachte sich in die laufende
        Lehrstuhlarbeit ein. Sein Verhalten gegenueber Vorgesetzten, Kolleginnen und
        Kollegen sowie Studierenden war einwandfrei.

        Das Arbeitsverhaeltnis endet mit Ablauf der vereinbarten Projektbefristung.
        Wir danken Herrn Rauch fuer die Mitarbeit und wuenschen ihm fuer seinen weiteren
        Berufsweg alles Gute.

        Prof. Dr. Armin Seefeld
        Lehrstuhlinhaber
        """,
    },
    {
        "nr": "13",
        "slug": "dr-eline-oster-wissmit-oeffentliches-recht",
        "name": "Dr. Eline Oster",
        "role": "Postdoktorale wissenschaftliche Mitarbeiterin",
        "sector": "Universität / Öffentliches Recht",
        "type": "Zwischenzeugnis",
        "reason": "Drittmittelantrag und Lehrstuhlwechsel",
        "expected": "🟢🟠; starke Forschung, aber Zwischenzeugnis-/Selbstbindungslogik und Schluss sauber einordnen",
        "text": """
        UNIVERSITAET KUETTENHAFEN - JURISTISCHE FAKULTAET
        Institut fuer Oeffentliches Recht und Europarecht
        Hafenstrasse 44, 24001 Kuettenhafen, europarecht@uni-kuettenhafen.test

        Kuettenhafen, den 15. Januar 2026

        ZWISCHENZEUGNIS

        Frau Dr. Eline Oster, geboren am 22. August 1992 in Bremen, ist seit dem
        1. Oktober 2022 als wissenschaftliche Mitarbeiterin in der Postdoc-Phase an
        unserem Institut taetig.

        Ihr Arbeitsgebiet umfasst europaeisches Verwaltungsrecht, Klimaschutzrecht,
        Forschungskoordination, Drittmittelantraege, Betreuung von Examensklausuren,
        Vorlesungsbegleitung und die fachliche Anleitung studentischer Hilfskraefte.

        Frau Dr. Oster besitzt sehr umfassende und jederzeit sichere Kenntnisse ihres
        Fachgebiets. Sie arbeitet wissenschaftlich eigenstaendig, methodisch ueberzeugend
        und mit sehr guter Urteilskraft. Ihre Entwuerfe fuer Antraege, Aufsaetze und
        Stellungnahmen sind inhaltlich praezise und sprachlich ausgezeichnet.

        Besonders hervorzuheben ist ihre Faehigkeit, mehrere Fristen, Publikationslinien
        und Lehrformate parallel zu steuern. Sie erfuellt die ihr uebertragenen Aufgaben
        stets zu unserer vollsten Zufriedenheit. Gegenueber Vorgesetzten, Kolleginnen
        und Kollegen, Studierenden sowie Projektpartnern verhaelt sie sich stets
        vorbildlich.

        Dieses Zwischenzeugnis wird auf Wunsch von Frau Dr. Oster aus Anlass eines
        anstehenden Drittmittelantrags und einer moeglichen Lehrstuhlvertretung erteilt.
        Wir freuen uns auf die weitere Zusammenarbeit und wuenschen ihr fuer die
        naechsten akademischen Schritte weiterhin viel Erfolg.

        Prof. Dr. Nils Achtermann
        Institutsdirektor
        """,
    },
    {
        "nr": "14",
        "slug": "salim-borchert-wissmit-legal-tech",
        "name": "Salim Borchert",
        "role": "Wissenschaftlicher Mitarbeiter Legal Tech / Zivilprozess",
        "sector": "Universität / Legal Tech",
        "type": "Endzeugnis",
        "reason": "Wechsel in die Justiz",
        "expected": "🟠; Schaufenster-Drift zwischen Projektlob und abgeschwaechter Gesamtformel",
        "text": """
        UNIVERSITAET WESTFELD - CENTER FOR LAW AND TECHNOLOGY
        Arbeitsbereich Zivilprozessrecht und digitale Justiz
        Campusbogen 3, 56001 Westfeld, Tel. 0261 9090-44

        Westfeld, den 31. Juli 2025

        ARBEITSZEUGNIS

        Herr Salim Borchert, geboren am 9. November 1994 in Mainz, war vom 1. August
        2020 bis zum 31. Juli 2025 als wissenschaftlicher Mitarbeiter im Arbeitsbereich
        Zivilprozessrecht und digitale Justiz beschaeftigt.

        Herr Borchert wirkte an Forschungsprojekten zu elektronischem Rechtsverkehr,
        Online-Verhandlungen, Datenaufbereitung fuer empirische Studien und didaktischen
        Formaten fuer die Schwerpunktbereichslehre mit. Daneben betreute er Workshops,
        koordinierte externe Referentinnen und Referenten und pflegte die Projektwebseite.

        In technischen Fragen arbeitete Herr Borchert sehr kreativ und loesungsorientiert.
        Er entwickelte mehrfach hilfreiche Arbeitshilfen und brachte wertvolle Impulse
        in die Projektgruppe ein. Juristische Texte bearbeitete er sorgfaeltig, wenn
        Gegenstand, Umfang und Erwartung zuvor abgestimmt waren.

        Die ihm uebertragenen Aufgaben erledigte Herr Borchert stets zu unserer vollen
        Zufriedenheit. Bei wechselnden Prioritaeten zeigte er Einsatzbereitschaft und
        fand sich in neue Themen ein. Sein Verhalten gegenueber Vorgesetzten,
        Kolleginnen und Kollegen, Studierenden sowie externen Partnern war jederzeit
        einwandfrei.

        Herr Borchert verlaesst uns auf eigenen Wunsch, um eine Taetigkeit in der Justiz
        aufzunehmen. Wir danken ihm fuer die gute Zusammenarbeit und wuenschen ihm fuer
        seinen weiteren Weg viel Erfolg und persoenlich alles Gute.

        Prof. Dr. Karen Muelder
        Leiterin des Arbeitsbereichs
        """,
    },
    {
        "nr": "15",
        "slug": "antonia-weber-wissmit-lehrstuhlorganisation",
        "name": "Antonia Weber",
        "role": "Wissenschaftliche Mitarbeiterin mit Lehrstuhlorganisation",
        "sector": "Universität / Arbeitsrecht",
        "type": "Endzeugnis",
        "reason": "Beendigung nach Befristungsablauf",
        "expected": "🔴/🟠; knappe Bewertung, fehlende Kernbereiche und auffaellige Sozialformel",
        "text": """
        UNIVERSITAET HELMBURG - FAKULTAET FUER RECHTSWISSENSCHAFT
        Lehrstuhl fuer Arbeitsrecht und Buergerliches Recht
        Schlossplatz 2, 99001 Helmburg, arbeitsrecht@uni-helmburg.test

        Helmburg, den 30. September 2025

        ARBEITSZEUGNIS

        Frau Antonia Weber, geboren am 6. Juni 1996 in Jena, war vom 1. Oktober 2021
        bis zum 30. September 2025 als wissenschaftliche Mitarbeiterin an unserem
        Lehrstuhl taetig.

        Frau Weber war mit Recherchen im Arbeitsrecht, der Vorbereitung von
        Lehrveranstaltungen, der organisatorischen Betreuung von Klausuren, der
        Kommunikation mit Studierenden sowie allgemeinen Aufgaben der Lehrstuhlverwaltung
        betraut.

        Sie zeigte Interesse an den ihr uebertragenen Aufgaben und verfuegte ueber
        brauchbare Kenntnisse im Arbeitsrecht. Die Aufgaben erledigte Frau Weber im
        Wesentlichen zu unserer Zufriedenheit. Sie bemuehte sich, auch bei umfangreichen
        organisatorischen Anforderungen den Ueberblick zu behalten.

        Im Umgang mit Studierenden war Frau Weber freundlich. Ihr Verhalten gegenueber
        Vorgesetzten und Kolleginnen und Kollegen war insgesamt korrekt. Das befristete
        Arbeitsverhaeltnis endet mit Ablauf der vereinbarten Zeit.

        Wir wuenschen Frau Weber fuer die Zukunft alles Gute.

        Prof. Dr. Ralf Neumayer
        Lehrstuhlinhaber
        """,
    },
    {
        "nr": "16",
        "slug": "markus-lentner-kanzleigeschaeftsfuehrer",
        "name": "Markus Lentner",
        "role": "Fremdgeschaeftsfuehrer / Kanzleileiter ohne Anwaltszulassung",
        "sector": "Große Wirtschaftskanzlei",
        "type": "Endzeugnis",
        "reason": "Aufhebungsvereinbarung",
        "expected": "🟠; Organ-/Arbeitnehmerrolle, Managementleistung und Schlussformel getrennt pruefen",
        "text": """
        ELLERBROOK RECHTSANWAELTE PARTG MBB
        Wirtschaftsrecht - Steuern - Compliance
        Kaiserring 17, 60311 Frankfurt am Main, Tel. 069 8800-0

        Frankfurt am Main, den 31. Dezember 2025

        ARBEITSZEUGNIS

        Herr Markus Lentner, geboren am 18. Januar 1978 in Kassel, war vom 1. Mai 2019
        bis zum 31. Dezember 2025 als angestellter Geschaeftsfuehrer der
        Verwaltungsgesellschaft und Kanzleileiter unserer deutschen Standorte taetig.
        Herr Lentner ist nicht als Rechtsanwalt zugelassen; seine Aufgabe lag in der
        kaufmaennischen, personellen und organisatorischen Leitung des Kanzleibetriebs.

        Zu seinem Verantwortungsbereich gehoerten Budgetplanung, Personalsteuerung,
        Standortorganisation, Dienstleistermanagement, IT- und Prozessprojekte,
        Controlling, Raumplanung, Honorardaten-Auswertungen und die Vorbereitung von
        Beschlussvorlagen fuer das Partnermanagement.

        Herr Lentner verfuegte ueber sehr gute betriebswirtschaftliche Kenntnisse und
        verstand die besonderen Anforderungen anwaltlicher Berufstraegerorganisationen.
        Er arbeitete strukturiert, diskret und wirtschaftlich umsichtig. Besonders bei
        der Einfuehrung neuer Controlling- und Recruiting-Prozesse erzielte er gute
        Ergebnisse.

        Die ihm uebertragenen Aufgaben erledigte Herr Lentner stets zu unserer vollen
        Zufriedenheit. Sein Verhalten gegenueber Partnerinnen und Partnern,
        Rechtsanwaltinnen und Rechtsanwaelten, Mitarbeitenden sowie externen
        Dienstleistern war jederzeit einwandfrei. Das Arbeitsverhaeltnis endet aufgrund
        einer einvernehmlichen Neuordnung der Geschaeftsfuehrungsstruktur.

        Wir danken Herrn Lentner fuer die gute Zusammenarbeit und wuenschen ihm fuer
        seinen weiteren beruflichen und privaten Weg alles Gute.

        Dr. Veit Sommerfeld
        Managing Partner
        """,
    },
    {
        "nr": "17",
        "slug": "lena-hartmann-junior-associate-probezeit",
        "name": "Lena Hartmann",
        "role": "Junior Associate",
        "sector": "Internationale Kanzlei / M&A",
        "type": "Endzeugnis",
        "reason": "Beendigung waehrend der Probezeit",
        "expected": "🔴; Probezeit, sehr kurze Dauer, Note 4-5 und knappe Schlussformel",
        "text": """
        BERGNER FIELDING LLP
        Rechtsanwaelte und Steuerberater
        Opernplatz 4, 80333 Muenchen, Tel. 089 7000-20

        Muenchen, den 15. Februar 2026

        ARBEITSZEUGNIS

        Frau Lena Hartmann, geboren am 27. April 1998 in Augsburg, war vom
        1. November 2025 bis zum 15. Februar 2026 als Associate im Bereich Corporate /
        Mergers & Acquisitions in unserem Muenchener Buero beschaeftigt.

        Frau Hartmann wurde in die laufende Transaktionsarbeit eingefuehrt. Zu ihren
        Aufgaben gehoerten die Unterstuetzung bei Due-Diligence-Pruefungen, die
        Recherche gesellschaftsrechtlicher Einzelfragen, die Erstellung von
        Zusammenfassungen, die Pflege von Signing-Listen und die Vorbereitung einfacher
        Entwurfsfassungen.

        Sie verfuegte ueber juristische Grundkenntnisse und zeigte Bereitschaft, sich
        in die Arbeitsweise einer internationalen Wirtschaftskanzlei einzuarbeiten. Die
        ihr uebertragenen Aufgaben erledigte sie zu unserer Zufriedenheit. Bei hoher
        Arbeitsbelastung bemuehte sie sich, die gesetzten Fristen einzuhalten.

        Ihr Verhalten gegenueber Vorgesetzten, Kolleginnen und Kollegen sowie
        Mandantenkontakten war korrekt. Das Arbeitsverhaeltnis endet waehrend der
        Probezeit. Wir wuenschen Frau Hartmann fuer ihren weiteren beruflichen Weg
        alles Gute.

        Dr. Friederike Kahl
        Partnerin
        """,
    },
    {
        "nr": "18",
        "slug": "claudia-renner-reno-fachangestellte",
        "name": "Claudia Renner",
        "role": "Rechtsanwaltsfachangestellte / ReNo-Fachkraft",
        "sector": "Kleine Kanzlei",
        "type": "Endzeugnis",
        "reason": "Eigenkuendigung",
        "expected": "🟠; Fristen-/Gebuehrenprofil, Reihenfolge im Sozialverhalten und Code-Lesarten pruefen",
        "text": """
        KANZLEI HANSEN & KOLLEGEN
        Rechtsanwaelte - Familienrecht - Mietrecht - Verkehrsrecht
        Marktgasse 9, 37073 Goettingen, Tel. 0551 4400-12

        Goettingen, den 31. Mai 2026

        ARBEITSZEUGNIS

        Frau Claudia Renner, geboren am 2. Dezember 1989 in Northeim, war vom
        1. August 2018 bis zum 31. Mai 2026 als Rechtsanwaltsfachangestellte in unserer
        Kanzlei beschaeftigt.

        Ihr Aufgabenbereich umfasste die Fristenkontrolle, Aktenanlage, Korrespondenz
        nach Diktat und Vorlage, beA-Versand, Telefonzentrale, Zwangsvollstreckung,
        Kostenfestsetzung, RVG-Abrechnungen, Terminskoordination und die Betreuung des
        Empfangs.

        Frau Renner verfuegte ueber gute Kenntnisse im Kanzleialltag und war mit den
        gaengigen Arbeitsablaeufen vertraut. Die ihr uebertragenen Aufgaben erledigte
        sie stets zu unserer vollen Zufriedenheit. Besonders in der Mandantenannahme
        und bei der telefonischen Kommunikation zeigte sie Freundlichkeit und Geduld.

        Frau Renner war ehrlich, puenktlich und ordnungsliebend. Ihr Verhalten gegenueber
        Kolleginnen, Mandantinnen und Mandanten sowie Vorgesetzten war einwandfrei. Sie
        verlaesst die Kanzlei auf eigenen Wunsch. Wir danken ihr fuer die Zusammenarbeit
        und wuenschen ihr fuer die Zukunft alles Gute.

        Rechtsanwalt Dr. Nils Hansen
        Kanzleiinhaber
        """,
    },
    {
        "nr": "19",
        "slug": "jonas-kemper-senior-associate-boutique",
        "name": "Jonas Kemper",
        "role": "Senior Associate",
        "sector": "Arbeitsrechtsboutique",
        "type": "Zwischenzeugnis",
        "reason": "Partnerperspektive / interner Wechsel",
        "expected": "🟢🟠; sehr starke Leistung, aber Partnertrack- und Akquiseauslassungen beachten",
        "text": """
        LINDENAU ARBEITSRECHT
        Boutique fuer Arbeitsrecht und Organhaftung
        Rheinpromenade 21, 40213 Duesseldorf, Tel. 0211 3300-77

        Duesseldorf, den 1. Juli 2026

        ZWISCHENZEUGNIS

        Herr Jonas Kemper, geboren am 11. Oktober 1990 in Wuppertal, ist seit dem
        1. Januar 2020 als Rechtsanwalt bei Lindenau Arbeitsrecht taetig, seit dem
        1. Januar 2024 in der Position eines Senior Associate.

        Herr Kemper beraet nationale und internationale Unternehmen in individual- und
        kollektivarbeitsrechtlichen Fragen. Zu seinen Aufgaben gehoeren die Fuehrung
        arbeitsgerichtlicher Verfahren, die Vorbereitung von Interessenausgleichs- und
        Sozialplanverhandlungen, die Beratung von Geschaeftsfuehrungen, die Erstellung
        von Gutachten sowie die Anleitung juengerer Kolleginnen und Kollegen.

        Herr Kemper verfuegt ueber sehr breite und sichere Kenntnisse im Arbeitsrecht.
        Seine Schriftsaetze sind praezise, taktisch durchdacht und sprachlich klar. Auch
        in eilbeduerftigen Verfahren arbeitet er sehr belastbar und loesungsorientiert.
        Mandanten schaetzen seine ruhige, verbindliche und wirtschaftlich fokussierte
        Beratung.

        Herr Kemper erledigt die ihm uebertragenen Aufgaben stets zu unserer vollsten
        Zufriedenheit. Sein Verhalten gegenueber Partnerinnen und Partnern, Kolleginnen
        und Kollegen, Mitarbeitenden, Gerichten, Betriebsraeten und Mandanten ist stets
        vorbildlich. Dieses Zwischenzeugnis wird auf seinen Wunsch aus Anlass einer
        internen Standort- und Perspektivklaerung erteilt. Wir freuen uns auf die
        weitere erfolgreiche Zusammenarbeit.

        Rechtsanwalt Dr. Clara Lindenau
        Partnerin
        """,
    },
    {
        "nr": "20",
        "slug": "dr-mira-voss-senior-associate-grosskanzlei",
        "name": "Dr. Mira Voss",
        "role": "Senior Associate",
        "sector": "Internationale Großkanzlei / Dispute Resolution",
        "type": "Endzeugnis",
        "reason": "Wechsel in ein Unternehmen",
        "expected": "🟠; starke Einzelsaetze, abgeschwaechte Team-/Fuerungsformeln und Schlussabgleich",
        "text": """
        WINTERBOURNE KELLER RECHTSANWAELTE PARTG MBB
        Litigation - Arbitration - Investigations
        Taunusanlage 3, 60329 Frankfurt am Main, Tel. 069 9900-100

        Frankfurt am Main, den 30. Juni 2026

        ARBEITSZEUGNIS

        Frau Dr. Mira Voss, geboren am 5. September 1988 in Hannover, war vom
        1. September 2018 bis zum 30. Juni 2026 als Rechtsanwaeltin in unserer Praxisgruppe
        Dispute Resolution taetig, seit dem 1. Januar 2023 als Senior Associate.

        Frau Dr. Voss bearbeitete nationale und internationale Streitigkeiten, leitete
        Workstreams in umfangreichen Schiedsverfahren, koordinierte Dokumentenreviews,
        entwarf Schriftsaetze in deutscher und englischer Sprache und bereitete
        Zeugen- sowie Sachverstaendigentermine vor. Zudem wirkte sie an internen
        Trainings und Knowledge-Management-Projekten mit.

        Fachlich verfuegte Frau Dr. Voss ueber sehr gute Kenntnisse des Prozess- und
        Schiedsverfahrensrechts. Ihre Analysen waren praezise, belastbar und mandatsnah.
        In arbeitsintensiven Phasen zeigte sie hohe Einsatzbereitschaft und erzielte
        sehr gute Arbeitsergebnisse.

        Die ihr uebertragenen Aufgaben erledigte Frau Dr. Voss stets zu unserer vollen
        Zufriedenheit. Sie fuehrte juengere Teammitglieder sachlich an und integrierte
        sich in wechselnde internationale Teams. Ihr Verhalten gegenueber Vorgesetzten,
        Kolleginnen und Kollegen, Mitarbeitenden, Gerichten, Schiedsgerichten und
        Mandanten war jederzeit einwandfrei.

        Frau Dr. Voss verlaesst uns auf eigenen Wunsch, um eine Position in einem
        Unternehmen zu uebernehmen. Wir danken ihr fuer die gute Zusammenarbeit und
        wuenschen ihr fuer die berufliche und private Zukunft weiterhin viel Erfolg.

        Rechtsanwalt Dr. Paul Winterbourne
        Partner
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
            )
    finally:
        txt_path.unlink(missing_ok=True)


def write_readme() -> None:
    rows = "\n".join(
        f"| {c['nr']} | {c['name']} | {c['role']} | {c['sector']} | {c['type']} | {c['reason']} |"
        for c in CASES
    )
    text = f"""# Testakte: Arbeitszeugnisse — Jura und Wissenschaft

Diese zweite Testakte begleitet den Skill [`arbeitszeugnispruefer`](../../skill/SKILL.md) als juristisch-akademisches Trainingsmaterial. Sie enthaelt zehn weitere fiktive Arbeitszeugnisse: fuenf aus dem akademischen Bereich juristischer Lehrstuehle und fuenf aus Kanzlei- beziehungsweise juristischen Praxisrollen. Alle Personen, Universitaeten, Kanzleien, Adressen und Kommunikationsdaten sind frei erfunden.

## Akte komplett lesen

| Was | Format | Datei |
| --- | --- | --- |
| Gesamt-PDF (alle zehn Zeugnisse) | PDF | [`gesamt-pdf/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf`](gesamt-pdf/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf) |
| Erwartungshorizont und Pruefpunkte | Markdown | [`90-erwartungshorizont-und-pruefpunkte.md`](90-erwartungshorizont-und-pruefpunkte.md) |

## Zweck der Akte

Die Zeugnisse trainieren Rollen, die im klassischen Zeugnisfundus oft fehlen: wissenschaftliche Mitarbeit an juristischen Lehrstuehlen, Postdoc-/Drittmittelkontexte, Probezeit in der Grosskanzlei, Kanzleileitung ohne Anwaltszulassung, ReNo-/Fristenarbeit und Senior-Associate-Bewertungen in kleinen und grossen Kanzleien.

Die Bewertungen sind absichtlich gemischt. Einige Zeugnisse sind sehr gut, andere enthalten typische Drift-, Auslassungs-, Rollen- oder Schlussformelprobleme. Der Skill soll nicht nur Codewoerter suchen, sondern Rolle, Zeugnisart, Aufgabenprofil, Beendigungsgrund und Erwartungshorizont zusammenfuehren.

## Aktenuebersicht

| Nr. | Name | Rolle | Umfeld | Zeugnistyp | Anlass |
| --- | --- | --- | --- | --- | --- |
{rows}

## Struktur

Jedes Zeugnis liegt als eigenes PDF in einem eigenen Unterordner. Der Dateiname folgt dem Schema `Arbeitszeugnis_<nr>-<slug>.pdf`.

## Mögliche Arbeitsauftraege an den Skill

- akademische und kanzleispezifische Aufgabenprofile vom Bewertungsinhalt trennen
- Besonderheiten von Zwischenzeugnis, Befristung, Probezeit und Kanzleileitung einordnen
- Schlussformel, Beendigungsgrund und Sozialverhalten rollenbewusst pruefen
- typische Auslassungen bei Lehrstuhl-, Associate-, ReNo- und Managementrollen erkennen
- bei Arbeitnehmerperspektive aus den Befunden Mandantenbericht und Berichtigungsverlangen erstellen
"""
    (OUT / "README.md").write_text(text, encoding="utf-8")


def write_expectations() -> None:
    rows = "\n".join(
        f"| {c['nr']} | {c['name']} | {c['expected']} |"
        for c in CASES
    )
    text = f"""# Erwartungshorizont und Pruefpunkte — Jura und Wissenschaft

Diese Liste ist kein Loesungsschluessel, sondern ein Pruefhorizont. Die Skill-Ausgabe darf abweichen, wenn sie die Abweichung aus Zeugnistext, Rolle und rechtlichem Anker begruendet.

| Nr. | Fall | Erwartete Hauptpruefung |
| --- | --- | --- |
{rows}

## Besondere Lernziele

- **Akademische Zeugnisse:** Forschungsleistung, Lehre, Drittmittel, Betreuung von Studierenden und Lehrstuhlorganisation getrennt auswerten.
- **Kanzleirollen:** anwaltliche Leistung, Mandantenkontakt, Teamfuehrung, Akquise, Kanzleiorganisation und Berufsrollen nicht vermischen.
- **Probezeit:** kurze Beschaeftigungsdauer nicht als Freibrief fuer unklare oder codierte Abwertung behandeln, aber Beweis- und Erwartungslage realistisch halten.
- **ReNo-/Kanzleibetrieb:** Fristen, beA, RVG, Kostenfestsetzung, Zwangsvollstreckung und Mandantenkontakt als Kernkompetenzen pruefen.
- **Fremdgeschaeftsfuehrung:** Organ- und Arbeitnehmerbezug, Managementaufgaben und fehlende Anwaltszulassung sauber im Zeugnistext abbilden.
"""
    (OUT / "90-erwartungshorizont-und-pruefpunkte.md").write_text(text, encoding="utf-8")


def main() -> None:
    for tool in ("cupsfilter", "pdfunite"):
        if not shutil.which(tool):
            raise SystemExit(f"missing required tool: {tool}")

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    (OUT / "gesamt-pdf").mkdir()
    DOCS_TESTAKTEN.mkdir(parents=True, exist_ok=True)

    pdfs: list[Path] = []
    for case in CASES:
        folder = OUT / f"{case['nr']}-{case['slug']}"
        folder.mkdir(parents=True)
        pdf = folder / f"Arbeitszeugnis_{case['nr']}-{case['slug']}.pdf"
        write_pdf(case["text"], pdf, f"Arbeitszeugnis {case['nr']} {case['name']}")
        pdfs.append(pdf)

    combined = OUT / "gesamt-pdf" / "arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"
    subprocess.run(["pdfunite", *map(str, pdfs), str(combined)], check=True)

    zip_path = OUT / "arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for pdf in pdfs:
            zf.write(pdf, arcname=str(pdf.relative_to(OUT)))

    write_readme()
    write_expectations()

    shutil.copy2(zip_path, DOCS_TESTAKTEN / zip_path.name)
    shutil.copy2(combined, DOCS_TESTAKTEN / combined.name)

    print(f"wrote {len(pdfs)} PDFs")
    print(f"wrote {combined.relative_to(ROOT)}")
    print(f"wrote {zip_path.relative_to(ROOT)}")
    print("copied public downloads to docs/testakten/")


if __name__ == "__main__":
    main()
