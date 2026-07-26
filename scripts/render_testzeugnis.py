#!/usr/bin/env python3
"""Render deterministic, professional A4 PDFs for the generated test files."""

from __future__ import annotations

import html
import re
import textwrap
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from reproducible_test_artifacts import normalize_pdf


ACCENTS = (
    colors.HexColor("#1F4E5F"),
    colors.HexColor("#435A3F"),
    colors.HexColor("#73424C"),
    colors.HexColor("#3F5574"),
    colors.HexColor("#625071"),
)
STAMP_PREFIXES = (
    "Dienstsiegel:",
    "Dienststempel:",
    "Firmenstempel:",
    "Kanzleistempel:",
    "Konzernstempel:",
)
SIGNATURE_ROLE_MARKERS = (
    "Chief ",
    "Geschäftsführer",
    "Geschäftsführerin",
    "Head of ",
    "Institutsdirektor",
    "Kanzleiinhaber",
    "Lehrstuhlinhaber",
    "Lehrstuhlinhaberin",
    "Leiterin des Arbeitsbereichs",
    "Managing Partner",
    "Partner Germany",
    "Partnerin",
    "Personal Deutschland",
    "People Partner",
    "Vorstand Personal",
    "Vorstandsvorsitzender",
    "Vorsitzende der Geschäftsführung",
)

# The source fixtures predate the Unicode renderer and deliberately used
# German ASCII transliterations. Apply only unambiguous stems and proper names.
GERMAN_REPLACEMENTS = (
    ("UNIVERSITAET", "UNIVERSITÄT"),
    ("Universitaet", "Universität"),
    ("FAKULTAET", "FAKULTÄT"),
    ("Fakultaet", "Fakultät"),
    ("RECHTSANWAELTE", "RECHTSANWÄLTE"),
    ("Rechtsanwaelt", "Rechtsanwält"),
    ("rechtsanwaelt", "rechtsanwält"),
    ("SOEHNE", "SÖHNE"),
    ("Soehne", "Söhne"),
    ("FUER", "FÜR"),
    ("Ueber", "Über"),
    ("ueber", "über"),
    ("fuer", "für"),
    ("Fuehr", "Führ"),
    ("fuehr", "führ"),
    ("Entwuerf", "Entwürf"),
    ("entwuerf", "entwürf"),
    ("Erfuell", "Erfüll"),
    ("erfuell", "erfüll"),
    ("Verfueg", "Verfüg"),
    ("verfueg", "verfüg"),
    ("Bemueh", "Bemüh"),
    ("bemueh", "bemüh"),
    ("Wuensch", "Wünsch"),
    ("wuensch", "wünsch"),
    ("Spuer", "Spür"),
    ("spuer", "spür"),
    ("Puenkt", "Pünkt"),
    ("puenkt", "pünkt"),
    ("Kuenft", "Künft"),
    ("kuenft", "künft"),
    ("Buendel", "Bündel"),
    ("buendel", "bündel"),
    ("Laender", "Länder"),
    ("laender", "länder"),
    ("Behoer", "Behör"),
    ("behoer", "behör"),
    ("Unterstuetz", "Unterstütz"),
    ("unterstuetz", "unterstütz"),
    ("Syndikusrechtsanwaelt", "Syndikusrechtsanwält"),
    ("syndikusrechtsanwaelt", "syndikusrechtsanwält"),
    ("Taet", "Tät"),
    ("taet", "tät"),
    ("Beschaeft", "Beschäft"),
    ("beschaeft", "beschäft"),
    ("Geschaeft", "Geschäft"),
    ("geschaeft", "geschäft"),
    ("Faeh", "Fäh"),
    ("faeh", "fäh"),
    ("Verhaeltnis", "Verhältnis"),
    ("verhaeltnis", "verhältnis"),
    ("verhaelt", "verhält"),
    ("Verstaend", "Verständ"),
    ("verstaend", "verständ"),
    ("Veraender", "Veränder"),
    ("veraender", "veränder"),
    ("Vollstaend", "Vollständ"),
    ("vollstaend", "vollständ"),
    ("Eigenstaend", "Eigenständ"),
    ("eigenstaend", "eigenständ"),
    ("selbststaend", "selbstständ"),
    ("Staend", "Ständ"),
    ("staend", "ständ"),
    ("Zuverlaess", "Zuverläss"),
    ("zuverlaess", "zuverläss"),
    ("Verlaess", "Verläss"),
    ("verlaess", "verläss"),
    ("Praez", "Präz"),
    ("praez", "präz"),
    ("Schaetz", "Schätz"),
    ("schaetz", "schätz"),
    ("Schaer", "Schär"),
    ("schaer", "schär"),
    ("Oeff", "Öff"),
    ("oeff", "öff"),
    ("Loes", "Lös"),
    ("loes", "lös"),
    ("Gehoer", "Gehör"),
    ("gehoer", "gehör"),
    ("Benoet", "Benöt"),
    ("benoet", "benöt"),
    ("Moeg", "Mög"),
    ("moeg", "mög"),
    ("Foerder", "Förder"),
    ("foerder", "förder"),
    ("Pruef", "Prüf"),
    ("pruef", "prüf"),
    ("Rueck", "Rück"),
    ("rueck", "rück"),
    ("Buerger", "Bürger"),
    ("buerger", "bürger"),
    ("Gruend", "Gründ"),
    ("gruend", "gründ"),
    ("Jueng", "Jüng"),
    ("jueng", "jüng"),
    ("Laeng", "Läng"),
    ("laeng", "läng"),
    ("Naech", "Näch"),
    ("naech", "näch"),
    ("Jaehr", "Jähr"),
    ("jaehr", "jähr"),
    ("Waehr", "Währ"),
    ("waehr", "währ"),
    ("Zaeh", "Zäh"),
    ("zaeh", "zäh"),
    ("Traeg", "Träg"),
    ("traeg", "träg"),
    ("Gaest", "Gäst"),
    ("gaest", "gäst"),
    ("Gaeng", "Gäng"),
    ("gaeng", "gäng"),
    ("Kraeft", "Kräft"),
    ("kraeft", "kräft"),
    ("Ablaeuf", "Abläuf"),
    ("ablaeuf", "abläuf"),
    ("Faell", "Fäll"),
    ("faell", "fäll"),
    ("Betriebsraet", "Betriebsrät"),
    ("betriebsraet", "betriebsrät"),
    ("Beraet", "Berät"),
    ("beraet", "berät"),
    ("Buero", "Büro"),
    ("buero", "büro"),
    ("Beduerf", "Bedürf"),
    ("beduerf", "bedürf"),
    ("Europae", "Europä"),
    ("europae", "europä"),
    ("Geaend", "Geänd"),
    ("geaend", "geänd"),
    ("Interdisziplinaer", "Interdisziplinär"),
    ("interdisziplinaer", "interdisziplinär"),
    ("Kaufmaenn", "Kaufmänn"),
    ("kaufmaenn", "kaufmänn"),
    ("Haeus", "Häus"),
    ("haeus", "häus"),
    ("Klaer", "Klär"),
    ("klaer", "klär"),
    ("Praes", "Präs"),
    ("praes", "präs"),
    ("Staer", "Stär"),
    ("staer", "stär"),
    ("Verguet", "Vergüt"),
    ("verguet", "vergüt"),
    ("Einschraenk", "Einschränk"),
    ("einschraenk", "einschränk"),
    ("Saetz", "Sätz"),
    ("saetz", "sätz"),
    ("Aktivitaet", "Aktivität"),
    ("aktivitaet", "aktivität"),
    ("itaeten", "itäten"),
    ("itaet", "ität"),
    ("Persoen", "Persön"),
    ("persoen", "persön"),
    ("Ausser", "Außer"),
    ("ausser", "außer"),
    ("Ausgepraeg", "Ausgepräg"),
    ("ausgepraeg", "ausgepräg"),
    ("Regelmaess", "Regelmäß"),
    ("regelmaess", "regelmäß"),
    ("Zulaess", "Zuläss"),
    ("zulaess", "zuläss"),
    ("Schliess", "Schließ"),
    ("schliess", "schließ"),
    ("Sorgfaelt", "Sorgfält"),
    ("sorgfaelt", "sorgfält"),
    ("Gross", "Groß"),
    ("gross", "groß"),
    ("Strasse", "Straße"),
    ("Muenchen", "München"),
    ("Muenchener", "Münchener"),
    ("Duesseldorf", "Düsseldorf"),
    ("Goettingen", "Göttingen"),
    ("Tuebingen", "Tübingen"),
    ("Krueger", "Krüger"),
    ("Kuettenhafen", "Küttenhafen"),
    ("kuettenhafen", "küttenhafen"),
    ("KUETTENHAFEN", "KÜTTENHAFEN"),
    ("Maerz", "März"),
    ("Roessler", "Rössler"),
    ("Lueg", "Lüg"),
    ("Muelder", "Mülder"),
)


def germanize(text: str) -> str:
    """Restore unambiguous German characters in legacy fixture text."""
    for source, replacement in GERMAN_REPLACEMENTS:
        text = text.replace(source, replacement)
    return text


def split_blocks(text: str) -> list[list[str]]:
    """Split an indented fixture into logical blocks while preserving lines."""
    normalized = textwrap.dedent(text).strip()
    raw_blocks = re.split(r"\n\s*\n", normalized)
    return [
        [germanize(line.strip()) for line in block.splitlines() if line.strip()]
        for block in raw_blocks
    ]


def is_signature_block(lines: list[str]) -> bool:
    joined = " ".join(lines)
    return len(joined) <= 140 and any(
        marker in joined for marker in SIGNATURE_ROLE_MARKERS
    )


def collapse_lines(lines: list[str]) -> str:
    """Join legacy wrapped lines without retaining artificial word breaks."""
    result = ""
    for line in lines:
        if not result:
            result = line
        elif result.endswith("-"):
            if line[0].islower():
                result = result[:-1] + line
            else:
                result += line
        else:
            result += " " + line
    return result


def parse_fixture(text: str) -> dict[str, object]:
    blocks = split_blocks(text)
    if len(blocks) < 7:
        raise ValueError("testimony fixture needs header, date, title, body and signature")

    stamp: str | None = None
    if blocks[-1][0].startswith(STAMP_PREFIXES):
        stamp = " ".join(blocks.pop())

    signatures: list[list[str]] = []
    while len(blocks) > 4 and is_signature_block(blocks[-1]):
        signatures.insert(0, blocks.pop())
    if not signatures:
        raise ValueError("testimony fixture has no detectable signature block")

    return {
        "header": blocks[0],
        "date": collapse_lines(blocks[1]),
        "title": collapse_lines(blocks[2]),
        "body": [collapse_lines(block) for block in blocks[3:]],
        "signatures": signatures,
        "stamp": stamp,
    }


def acronym(organization: str) -> str:
    tokens = re.findall(r"[A-ZÄÖÜ][A-ZÄÖÜ&-]+", organization)
    letters = "".join(token[0] for token in tokens if token != "&")
    return (letters[:3] or "AZ").upper()


def escaped(text: str) -> str:
    return html.escape(text, quote=False)


def _canvasmaker(*args: object, **kwargs: object) -> Canvas:
    kwargs["invariant"] = 1
    kwargs["pageCompression"] = 1
    return Canvas(*args, **kwargs)


def write_testimony_pdf(
    text: str,
    pdf_path: Path,
    *,
    case_number: str,
    document_title: str,
) -> None:
    """Render one fixture and normalize its metadata for byte reproducibility."""
    fixture = parse_fixture(text)
    accent = ACCENTS[(int(case_number) - 1) % len(ACCENTS)]
    styles = getSampleStyleSheet()
    body = ParagraphStyle(
        "Body",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.35,
        leading=13.15,
        textColor=colors.HexColor("#20252B"),
        spaceAfter=4.2 * mm,
        allowWidows=0,
        allowOrphans=0,
    )
    meta = ParagraphStyle(
        "Meta",
        parent=body,
        fontSize=7.6,
        leading=10.2,
        textColor=colors.HexColor("#525B66"),
        spaceAfter=0,
    )
    brand = ParagraphStyle(
        "Brand",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=11.3,
        leading=13.2,
        textColor=colors.HexColor("#17212B"),
        spaceAfter=1.2 * mm,
    )
    mark = ParagraphStyle(
        "Mark",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=15,
        leading=18,
        alignment=TA_CENTER,
        textColor=colors.white,
        spaceAfter=0,
    )
    date_style = ParagraphStyle(
        "Date",
        parent=body,
        fontSize=8.7,
        alignment=TA_RIGHT,
        textColor=colors.HexColor("#3F4852"),
        spaceAfter=7 * mm,
    )
    title_style = ParagraphStyle(
        "Title",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=17,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#17212B"),
        spaceAfter=8 * mm,
    )
    signature_name = ParagraphStyle(
        "SignatureName",
        parent=body,
        fontName="Helvetica-Bold",
        fontSize=8.7,
        leading=11,
        spaceAfter=0.8 * mm,
    )
    signature_role = ParagraphStyle(
        "SignatureRole",
        parent=meta,
        fontSize=7.8,
        leading=10,
    )
    stamp_style = ParagraphStyle(
        "Stamp",
        parent=meta,
        fontName="Helvetica-Oblique",
        fontSize=7.2,
        leading=9,
        textColor=colors.HexColor("#68737D"),
    )

    page_width, _ = A4
    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=A4,
        leftMargin=19 * mm,
        rightMargin=19 * mm,
        topMargin=22 * mm,
        bottomMargin=18 * mm,
        title=document_title,
        author="Arbeitszeugnis-Prüfer Testakten",
        subject=f"Fiktive Testakte, Fall {case_number}",
    )

    header_lines = fixture["header"]
    organization = header_lines[0]
    details = "<br/>".join(escaped(line) for line in header_lines[1:])
    logo = Table(
        [[Paragraph(escaped(acronym(organization)), mark)]],
        colWidths=[17 * mm],
        rowHeights=[17 * mm],
    )
    logo.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), accent),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("BOX", (0, 0), (-1, -1), 0.6, accent),
            ]
        )
    )
    header_copy = [
        Paragraph(escaped(organization), brand),
        Paragraph(details, meta),
    ]
    header = Table(
        [[logo, header_copy]],
        colWidths=[21 * mm, page_width - doc.leftMargin - doc.rightMargin - 21 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 4 * mm),
                ("RIGHTPADDING", (1, 0), (1, 0), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )

    story: list[object] = [
        header,
        Spacer(1, 4 * mm),
        HRFlowable(width="100%", thickness=1.1, color=accent),
        Spacer(1, 5 * mm),
        Paragraph(escaped(fixture["date"]), date_style),
        Paragraph(escaped(fixture["title"]), title_style),
    ]
    body_paragraphs = fixture["body"]
    closing_body_count = min(2, len(body_paragraphs))
    story.extend(
        Paragraph(escaped(paragraph), body)
        for paragraph in body_paragraphs[:-closing_body_count]
    )

    signature_cells = []
    for lines in fixture["signatures"]:
        signature_cells.append(
            [
                HRFlowable(width=54 * mm, thickness=0.55, color=colors.HexColor("#606A73")),
                Spacer(1, 1.5 * mm),
                Paragraph(escaped(lines[0]), signature_name),
                Paragraph("<br/>".join(escaped(line) for line in lines[1:]), signature_role),
            ]
        )
    signature_table = Table(
        [signature_cells],
        colWidths=[
            (page_width - doc.leftMargin - doc.rightMargin) / len(signature_cells)
        ]
        * len(signature_cells),
    )
    signature_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, -1), 0),
                ("RIGHTPADDING", (-1, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    closing = [
        Paragraph(escaped(paragraph), body)
        for paragraph in body_paragraphs[-closing_body_count:]
    ]
    closing.extend([Spacer(1, 5 * mm), signature_table])
    if fixture["stamp"]:
        closing.extend(
            [
                Spacer(1, 5 * mm),
                Table(
                    [[Paragraph(escaped(fixture["stamp"]), stamp_style)]],
                    colWidths=[82 * mm],
                    style=TableStyle(
                        [
                            ("BOX", (0, 0), (-1, -1), 0.5, colors.HexColor("#A8B0B8")),
                            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#F6F7F8")),
                            ("LEFTPADDING", (0, 0), (-1, -1), 3 * mm),
                            ("RIGHTPADDING", (0, 0), (-1, -1), 3 * mm),
                            ("TOPPADDING", (0, 0), (-1, -1), 2 * mm),
                            ("BOTTOMPADDING", (0, 0), (-1, -1), 2 * mm),
                        ]
                    ),
                ),
            ]
        )
    story.append(KeepTogether(closing))

    def decorate_page(canvas: Canvas, document: SimpleDocTemplate) -> None:
        canvas.saveState()
        canvas.setTitle(document_title)
        canvas.setAuthor("Arbeitszeugnis-Prüfer Testakten")
        canvas.setSubject(f"Fiktive Testakte, Fall {case_number}")
        if document.page > 1:
            canvas.setFillColor(colors.HexColor("#4E5963"))
            canvas.setFont("Helvetica-Bold", 7.4)
            canvas.drawString(
                doc.leftMargin,
                A4[1] - 12 * mm,
                organization,
            )
            canvas.setFont("Helvetica", 7.2)
            canvas.drawRightString(
                A4[0] - doc.rightMargin,
                A4[1] - 12 * mm,
                f"Fortsetzung {fixture['title']}",
            )
            canvas.setStrokeColor(accent)
            canvas.setLineWidth(0.6)
            canvas.line(
                doc.leftMargin,
                A4[1] - 15 * mm,
                A4[0] - doc.rightMargin,
                A4[1] - 15 * mm,
            )
        canvas.setStrokeColor(colors.HexColor("#C7CDD2"))
        canvas.setLineWidth(0.45)
        canvas.line(doc.leftMargin, 12.8 * mm, A4[0] - doc.rightMargin, 12.8 * mm)
        canvas.setFont("Helvetica", 7)
        canvas.setFillColor(colors.HexColor("#6D7680"))
        canvas.drawString(doc.leftMargin, 9.2 * mm, f"Fiktive Testakte | Fall {case_number}")
        canvas.drawRightString(
            A4[0] - doc.rightMargin,
            9.2 * mm,
            f"Seite {document.page}",
        )
        canvas.restoreState()

    doc.build(
        story,
        onFirstPage=decorate_page,
        onLaterPages=decorate_page,
        canvasmaker=_canvasmaker,
    )
    normalize_pdf(pdf_path, expected_date_count=2)
