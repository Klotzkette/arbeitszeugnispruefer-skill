#!/usr/bin/env python3
"""Build the ten general-industry employment-reference test files."""

from __future__ import annotations

import re
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from render_testzeugnis import SECTION_HEADINGS, collapse_lines, write_testimony_pdf
from reproducible_test_artifacts import normalize_pdf, write_reproducible_zip


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "testakten" / "arbeitszeugnis-analyse-bluehendes-leben"
SOURCES = OUT / "quellen"
DOCS_TESTAKTEN = ROOT / "docs" / "testakten"
PROCESS_TIMEOUT_SECONDS = 120
PDF_WORKERS = 4
DATE_RE = re.compile(r".+, den \d{1,2}\. .+ \d{4}$")


CASES = [
    {
        "nr": "01",
        "slug": "gunhilde-brachvogel-riemenschneider-pta",
        "name": "Gunhilde Brachvogel-Riemenschneider",
        "role": "Pharmazeutisch-technische Assistentin",
        "grade": "1",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "konsistentes Spitzenzeugnis mit konkreten Erfolgen, Beständigkeit und vorbildlichem Verhalten",
        "must_find": "Spitzenformel, außergewöhnliche Fach- und Ergebnisbelege sowie vorbildliches Sozialverhalten tragen gemeinsam die Note 1.",
        "guardrail": "Aus der warmen Schlussformel keinen selbstständigen gesetzlichen Anspruch und aus der Weiterempfehlung keine zusätzliche Notenstufe ableiten.",
        "output": "Positive Einordnung; ohne falsche Tatsachen oder Formmängel kein Berichtigungsverlangen erzeugen.",
    },
    {
        "nr": "02",
        "slug": "volkmar-eitel-hartung-rechtsanwalt",
        "name": "Volkmar Eitel-Hartung",
        "role": "Angestellter Rechtsanwalt",
        "grade": "2",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "stimmige gute Bewertung mit eigenständiger Mandatsarbeit und erfolgreicher Dezernatsentwicklung",
        "must_find": "„Stets zur vollen Zufriedenheit“, sehr gute Einzelleistungen und einwandfreies Verhalten ergeben ein gutes Gesamtzeugnis.",
        "guardrail": "Kanzleigründung, Eigenwechsel und unternehmerische Selbstständigkeit nicht als versteckte Kritik behandeln.",
        "output": "Gute Gesamtnote verständlich erklären; nur konkrete Tatsachen- oder Formfehler zur Korrektur stellen.",
    },
    {
        "nr": "03",
        "slug": "edelgard-schwerdtfeger-mta-radiologie",
        "name": "Edelgard Schwerdtfeger",
        "role": "Medizinisch-technische Radiologieassistentin",
        "grade": "3",
        "logo_lines": 4,
        "organization_lines": 2,
        "expected": "durchschnittliche Gesamtformel mit mehreren blassen Einzelbewertungen und knappem Sozialverhalten",
        "must_find": "„Zur vollen Zufriedenheit“, erwartete Qualität und das zurückhaltende Team-/Verhaltensbild ergeben eine mittlere Bewertung.",
        "guardrail": "„Hat sich in das Team integriert“ nicht isoliert als gerichtlich festgelegten Geheimcode oder konkrete Konflikttatsache ausgeben.",
        "output": "Durchschnittstendenz erklären; eine bessere Bewertung nur mit konkreten Leistungsbelegen verlangen.",
    },
    {
        "nr": "04",
        "slug": "friedhelm-poettering-lagermeister",
        "name": "Friedhelm Pöttering",
        "role": "Lagermeister",
        "grade": "4",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "unterdurchschnittliches Gesamtbild aus Bemühens-, Anweisungs-, Belastbarkeits- und Verhaltensaussagen",
        "must_find": "„Stets bemüht“, nur ausreichende Belastbarkeit und korrektes Verhalten schwächen die scheinbar neutrale Erwartungsformel erheblich.",
        "guardrail": "Die ausdrücklich betriebsbedingte Kündigung nicht als persönliche Leistungs- oder Verhaltensursache umdeuten.",
        "output": "Deutliche Warnung; bei abweichender Leistungsakte beweisgebundene Zieltexte und ein Berichtigungsverlangen formulieren.",
    },
    {
        "nr": "05",
        "slug": "walpurga-dietrichsen-hofstaetter-zfa",
        "name": "Walpurga Dietrichsen-Hofstätter",
        "role": "Zahnmedizinische Fachangestellte",
        "grade": "5",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "sehr schwaches Zeugnis mit Bemühenssatz, Anwesenheitsbezug und mehrfachen Einschränkungen",
        "must_find": "Grundkenntnisse, „stets bemüht“, „im Wesentlichen“, Anwesenheitsbezug und nur grundsätzlich korrektes Verhalten ergeben ein sehr negatives Bild.",
        "guardrail": "Geselligkeit nicht als Alkoholbehauptung und das neutrale Enddatum nicht als sicheren Kündigungs- oder Fehlverhaltenscode behandeln.",
        "output": "Kritische Einordnung und bei Gegenbelegen ein präzises Berichtigungsverlangen zu Leistung und Verhalten liefern.",
    },
    {
        "nr": "06",
        "slug": "reinhilde-eisentraeger-filialleiterin-sparkasse",
        "name": "Reinhilde Eisenträger",
        "role": "Filialleiterin",
        "grade": "2",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "gutes Zwischenzeugnis mit überzeugender Fach-, Ergebnis- und Führungsbewertung",
        "must_find": "Beständige gute Leistung und ein stimmiges Führungsprofil tragen Note 2; das Zwischenzeugnis ist als spätere Vergleichsbasis zu sichern.",
        "guardrail": "Elternzeit weder als Leistungsminus noch ohne Einzelfallprüfung als unzulässige Zeugnisangabe behandeln.",
        "output": "Positive Einordnung und Empfehlung, das Zwischenzeugnis für einen späteren Driftvergleich aufzubewahren.",
    },
    {
        "nr": "07",
        "slug": "dietram-auerwald-bornhoeft-spedition",
        "name": "Dietram Auerwald-Bornhöft",
        "role": "Sachbearbeiter Speditionsdisposition",
        "grade": "3 bis 4",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "gemischtes Zeugnis mit mittlerer Hauptformel und mehreren einschränkenden Nebenbewertungen",
        "must_find": "„In der Regel zuverlässig“, bloß genutzte Möglichkeiten, Anwesenheitsbezug und überwiegend ordnungsgemäßes Verhalten ziehen die Note-3-Formel nach unten.",
        "guardrail": "Einvernehmliche Beendigung nicht ohne weitere Tatsachen als Konflikt, Aufhebungsdruck oder Fehlverhalten darstellen.",
        "output": "Gesamtspanne 3 bis 4 begründen und Korrekturpunkte nur mit Leistungs- und Verhaltensbelegen verfolgen.",
    },
    {
        "nr": "08",
        "slug": "hartmut-greifenklau-hotel-empfangsleiter",
        "name": "Hartmut Greifenklau",
        "role": "Leiter des Empfangs",
        "grade": "4",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "schwache Leistungsbewertung und auffällig inhaltsarme Führungs- und Verhaltensaussagen",
        "must_find": "„Zur Zufriedenheit“, ausreichende Belastbarkeit und die tautologische Führungsaussage ergeben ein unterdurchschnittliches Leitungszeugnis.",
        "guardrail": "Gästewortlaut, fehlender Beendigungsgrund und knapper Schluss nicht als sichere Geheimcodes oder Tatsachenbehauptungen ausgeben.",
        "output": "Warnung und bei belastbaren Führungsbelegen konkrete Ergänzungs- und Aufwertungsvorschläge formulieren.",
    },
    {
        "nr": "09",
        "slug": "ortrud-falckenstein-altenpflegerin",
        "name": "Ortrud Falckenstein",
        "role": "Altenpflegerin und Wohnbereichsleitung",
        "grade": "2",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "überwiegend gutes Langzeitzeugnis mit konkreter Verantwortung und einer begrenzten Dokumentationsschwäche",
        "must_find": "Beständige gute Leistung, Zusatzdienste, langjähriger Vertrauensaufbau und wertschätzendes Verhalten überwiegen vereinzelte Verzögerungen.",
        "guardrail": "Ruhestand, Gesundheitswunsch und lange Betriebszugehörigkeit nicht als Krankheits-, Alters- oder Belastbarkeitscode lesen.",
        "output": "Gute Gesamtbewertung mit transparenter Einschränkung erklären; ohne Tatsachenfehler kein Streit erzeugen.",
    },
    {
        "nr": "10",
        "slug": "burchard-holzapfel-industriemechaniker",
        "name": "Burchard Holzapfel",
        "role": "Industriemechaniker und Schichtführer",
        "grade": "5",
        "logo_lines": 3,
        "organization_lines": 1,
        "expected": "sehr schwaches Führungszeugnis mit zahlreichen Begrenzungen und fehlender belastbarer Erfolgsfeststellung",
        "must_find": "„Im Großen und Ganzen“, Anweisungsorientierung, Anwesenheitsbezug, ausreichende Belastbarkeit und nur grundsätzlich korrektes Verhalten ergeben Note 5.",
        "guardrail": "Ehrlichkeit und direkte Kommunikation nicht ohne Kontext in Diebstahls-, Konflikt- oder sonstige Negativtatsachen übersetzen.",
        "output": "Sehr schwache Tendenz klar benennen und bei Gegenbelegen ein beweisgebundenes Berichtigungsverlangen erstellen.",
    },
]


def source_lines(case: dict[str, object]) -> list[str]:
    source = SOURCES / f"{case['nr']}-{case['slug']}.txt"
    if not source.is_file():
        raise ValueError(f"missing fixture source: {source}")
    return [line.strip() for line in source.read_text(encoding="utf-8").splitlines() if line.strip()]


def body_blocks(lines: list[str]) -> list[str]:
    blocks: list[str] = []
    current: list[str] = []
    bullet_mode = False

    def flush() -> None:
        nonlocal current
        if current:
            blocks.append(collapse_lines(current))
            current = []

    for line in lines:
        if line in SECTION_HEADINGS:
            flush()
            blocks.append(line)
            bullet_mode = False
        elif line.startswith("• "):
            flush()
            current = [line]
            bullet_mode = True
        else:
            current.append(line)
            if bullet_mode and line.endswith("."):
                flush()
                bullet_mode = False
    flush()
    return blocks


def renderer_text(case: dict[str, object]) -> str:
    lines = source_lines(case)
    date_indexes = [index for index, line in enumerate(lines) if DATE_RE.fullmatch(line)]
    if len(date_indexes) != 1:
        raise ValueError(f"case {case['nr']} needs exactly one issue-date line")
    date_index = date_indexes[0]

    logo_lines = int(case["logo_lines"])
    organization_lines = int(case["organization_lines"])
    header = lines[logo_lines:date_index]
    if organization_lines > 1:
        header = [
            " ".join(header[:organization_lines]),
            *header[organization_lines:],
        ]
    if len(header) < 4:
        raise ValueError(f"case {case['nr']} has an incomplete letterhead")

    signature_indexes = [
        index for index, line in enumerate(lines) if line.startswith("_____")
    ]
    if not signature_indexes:
        raise ValueError(f"case {case['nr']} has no signature separator")

    signatures: list[list[str]] = []
    stamp: str | None = None
    for position, start in enumerate(signature_indexes):
        end = (
            signature_indexes[position + 1]
            if position + 1 < len(signature_indexes)
            else len(lines)
        )
        group = lines[start + 1 : end]
        stamp_lines = [
            line for line in group if line.startswith("(Stempel:") and line.endswith(")")
        ]
        if stamp_lines:
            if stamp is not None or len(stamp_lines) != 1:
                raise ValueError(f"case {case['nr']} has ambiguous stamp data")
            stamp = stamp_lines[0][1:-1]
            group = [line for line in group if line not in stamp_lines]
        if len(group) < 2:
            raise ValueError(f"case {case['nr']} has an incomplete signature")
        signatures.append(group)

    title_index = date_index + 1
    body = body_blocks(lines[title_index + 1 : signature_indexes[0]])
    parts = [
        "\n".join(header),
        lines[date_index],
        lines[title_index],
        *body,
        *["\n".join(signature) for signature in signatures],
    ]
    if stamp:
        parts.append(stamp)
    return "\n\n".join(parts)


def build_case(case: dict[str, object]) -> Path:
    folder = OUT / f"{case['nr']}-{case['slug']}"
    folder.mkdir(parents=True)
    pdf = folder / f"Arbeitszeugnis_{case['nr']}-{case['slug']}.pdf"
    try:
        write_testimony_pdf(
            renderer_text(case),
            pdf,
            case_number=str(case["nr"]),
            document_title=f"Arbeitszeugnis {case['nr']} {case['name']}",
        )
    except Exception as exc:
        raise RuntimeError(f"failed to build case {case['nr']}-{case['slug']}") from exc
    return pdf


def write_expectations() -> None:
    rows = "\n".join(
        f"| {case['nr']} | {case['name']} | {case['grade']} | {case['expected']} |"
        for case in CASES
    )
    details = "\n\n".join(
        f"""### Fall {case['nr']}: {case['name']}

- **Muss erkannt werden:** {case['must_find']}
- **Nicht überdehnen:** {case['guardrail']}
- **Erwarteter One-Shot-Ausgang:** {case['output']}"""
        for case in CASES
    )
    text = f"""# Erwartungshorizont und Prüfpunkte — Allgemeine Branchen

Dieser Erwartungshorizont dient als kalibrierbare Ground Truth für die
vollständig fiktiven Fälle 01 bis 10. Zuerst wird nur das jeweilige PDF geprüft;
dieser Lösungstext und die zentrale Fallmatrix werden erst danach geöffnet.
Eine vertretbare Abweichung muss am vollständigen Wortlaut, am beruflichen
Kontext und an der verfügbaren Beleglage begründet werden.

## Schnellmatrix

| Nr. | Fall | Sollkorridor | Erwartete Hauptprüfung |
| --- | --- | --- | --- |
{rows}

## Fallbezogene Mindestbefunde

{details}

## Besondere Lernziele

- **Notenskala vollständig abdecken:** Die Sammlung reicht von einem
  konsistenten Spitzenzeugnis bis zu mehrfach begrenzten Bewertungen der
  Stufe 5.
- **Fach- und Führungsrollen trennen:** Fachleistung, Belastbarkeit,
  Sozialverhalten und Führung werden jeweils eigenständig gewichtet.
- **Codehypothesen begrenzen:** Geselligkeit, Anwesenheit, Ehrlichkeit,
  Beendigungsgrund und Gesundheitswunsch dürfen keine unbelegten negativen
  Tatsachen erzeugen.
- **Zwischenzeugnis sichern:** Fall 06 ist Vergleichsbasis für eine spätere
  Driftprüfung, nicht automatisch Anlass für ein Aufforderungsschreiben.
- **Beendigungsgründe neutral halten:** Eigenwechsel, betriebsbedingte
  Kündigung, Aufhebung und Ruhestand sind nur zusammen mit weiteren Signalen
  bewertbar.

## Auswertungsregel

Ampel, Sollkorridor und rechtliche Durchsetzbarkeit bleiben getrennt. Eine
unterdurchschnittliche Sprachbewertung ist klar zu erklären, eine bessere
Fassung aber nur anhand der Tatsachen- und Beleglage zu verlangen.
Arbeitnehmer- und Kanzleiperspektive erhalten bei belastbarem Punkt ein
ausformuliertes Gegenseitenschreiben; ohne solchen Punkt wird kein künstlicher
Streit erzeugt.
"""
    (OUT / "90-erwartungshorizont-und-pruefpunkte.md").write_text(
        text,
        encoding="utf-8",
    )


def main() -> None:
    if not shutil.which("pdfunite"):
        raise SystemExit("missing required tool: pdfunite")

    OUT.mkdir(parents=True, exist_ok=True)
    for case in CASES:
        folder = OUT / f"{case['nr']}-{case['slug']}"
        if folder.exists():
            shutil.rmtree(folder)
    combined_dir = OUT / "gesamt-pdf"
    if combined_dir.exists():
        shutil.rmtree(combined_dir)
    combined_dir.mkdir()
    DOCS_TESTAKTEN.mkdir(parents=True, exist_ok=True)

    with ThreadPoolExecutor(max_workers=min(PDF_WORKERS, len(CASES))) as executor:
        pdfs = list(executor.map(build_case, CASES))

    combined = combined_dir / "arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"
    subprocess.run(
        ["pdfunite", *map(str, pdfs), str(combined)],
        check=True,
        timeout=PROCESS_TIMEOUT_SECONDS,
    )
    normalize_pdf(combined, expected_date_count=0)

    zip_path = OUT / "arbeitszeugnis-testakten-einzel-pdfs.zip"
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
