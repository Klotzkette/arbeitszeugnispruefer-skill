#!/usr/bin/env python3
"""Check release-critical repository invariants.

The script is intentionally dependency-light. It validates the things that tend
to break during a release: version drift, stale docs copies, broken local links,
legal-citation drift, oversized mini skill files and missing public test artifacts.
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from concurrent.futures import Future, ThreadPoolExecutor
from functools import lru_cache
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

from reproducible_test_artifacts import (
    CANONICAL_PDF_DATE,
    ZIP_FILE_MODE,
    ZIP_TIMESTAMP,
)


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Klotzkette/arbeitszeugnispruefer-skill"
MINI_LIMIT = 7500
PROCESS_TIMEOUT_SECONDS = 30
INTEGRITY_WORKFLOW = Path(".github/workflows/verify-integrity.yml")
QUALITY_AUDIT = Path("QUALITY-AUDIT-100.md")

MARKDOWN_WITH_ANCHORS = [
    Path("README.md"),
    Path("CHANGELOG.md"),
    QUALITY_AUDIT,
    Path("skill/SKILL.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/90-erwartungshorizont-und-pruefpunkte.md"),
    Path("testakten/README.md"),
    Path("testakten/TESTFALL-MATRIX.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen/README.md"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md"),
]

HTML_FILES = [
    Path("docs/index.html"),
    Path("docs/download-skill.html"),
    Path("docs/download-mini.html"),
]

PUBLIC_ARTIFACTS = [
    (
        Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/arbeitszeugnis-testakten-einzel-pdfs.zip"),
        Path("docs/testakten/arbeitszeugnis-testakten-einzel-pdfs.zip"),
        10,
    ),
    (
        Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"),
        Path("docs/testakten/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"),
        None,
    ),
    (
        Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"),
        Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"),
        10,
    ),
    (
        Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/gesamt-pdf/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"),
        Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"),
        None,
    ),
    (
        Path("testakten/arbeitszeugnisse-leitungsfunktionen/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"),
        Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"),
        5,
    ),
    (
        Path("testakten/arbeitszeugnisse-leitungsfunktionen/gesamt-pdf/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"),
        Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"),
        None,
    ),
    (
        Path("testakten/arbeitszeugnis-testpaket-komplett.zip"),
        Path("docs/testakten/arbeitszeugnis-testpaket-komplett.zip"),
        25,
    ),
]

CHECKSUM_ASSET_CANDIDATES = [
    Path("docs/SKILL.md"),
    Path("docs/SKILL-mini.md"),
    Path("docs/testakten/arbeitszeugnis-testakten-einzel-pdfs.zip"),
    Path("docs/testakten/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"),
    Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"),
    Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"),
    Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"),
    Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"),
    Path("docs/testakten/arbeitszeugnis-testpaket-komplett.zip"),
]

RELEASE_ASSET_CANDIDATES = CHECKSUM_ASSET_CANDIDATES + [
    Path("docs/SHA256SUMS.txt"),
]

LATEST_RELEASE_URL = f"https://github.com/{REPOSITORY}/releases/latest"

README_NAVIGATION_TARGETS = [
    Path("skill/SKILL.md"),
    Path("skill/SKILL-mini.md"),
    Path("docs/index.html"),
    Path("docs/download-skill.html"),
    Path("docs/download-mini.html"),
    Path("docs/SHA256SUMS.txt"),
    Path("requirements-build.txt"),
    Path("testakten/README.md"),
    Path("testakten/TESTFALL-MATRIX.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/90-erwartungshorizont-und-pruefpunkte.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/90-ergaenzende-korrespondenz-und-vollvermerke.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen/README.md"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md"),
    Path("scripts/check_release_integrity.py"),
    Path("scripts/build_generated_testakten.py"),
    Path("scripts/render_testzeugnis.py"),
    Path("scripts/reproducible_test_artifacts.py"),
    Path("scripts/build_allgemeine_testakten.py"),
    Path("scripts/build_jura_und_wissenschaft_testakten.py"),
    Path("scripts/build_leitungsfunktionen_testakten.py"),
    Path("CHANGELOG.md"),
    QUALITY_AUDIT,
    Path(".github/workflows/verify-integrity.yml"),
    Path("LICENSE-APACHE"),
    Path("LICENSE-MIT"),
]

TEST_READMES = [
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen/README.md"),
]

COMBINED_PDF_DETAILS = [
    (
        Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"),
        "Allgemeine Branchen",
        10,
        10,
        None,
    ),
    (
        Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/gesamt-pdf/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"),
        "Jura/Wissenschaft",
        10,
        10,
        None,
    ),
    (
        Path("testakten/arbeitszeugnisse-leitungsfunktionen/gesamt-pdf/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"),
        "Leitungsfunktionen",
        5,
        5,
        None,
    ),
]

CANONICAL_DECISION_DATES = {
    "9 AZR 12/03": "14.10.2003",
    "9 AZR 584/13": "18.11.2014",
    "9 AZR 44/00": "20.02.2001",
    "9 AZR 227/11": "11.12.2012",
    "9 AZR 146/21": "25.01.2022",
    "9 AZR 352/04": "21.06.2005",
    "9 AZR 248/07": "16.10.2007",
    "9 AZR 632/07": "12.08.2008",
    "9 AZR 386/10": "15.11.2011",
    "9 AZR 893/98": "21.09.1999",
    "9 AZR 507/04": "04.10.2005",
    "9 AZR 8/15": "14.06.2016",
    "9 AZR 262/20": "27.04.2021",
    "9 AZR 272/22": "06.06.2023",
    "9 AZR 48/24": "28.01.2025",
    "8 AZR 293/18": "28.11.2019",
    "8 AZR 838/13": "11.12.2014",
    "7 AZR 292/17": "17.04.2019",
    "3 AZR 121/11": "12.02.2013",
    "2 AZR 96/24 (B)": "18.06.2025",
    "9 AZB 40/21": "08.02.2022",
    "9 AZB 49/16": "14.02.2017",
    "8 AZB 25/25": "07.05.2026",
    "5 AZR 848/93": "08.03.1995",
    "12 Ta 475/16": "14.11.2016",
    "4 Ta 118/16": "27.07.2016",
    "9 Ta 319/25": "19.02.2026",
    "6 SLa 25/24": "05.12.2024",
    "5 Ca 80 b/13": "18.04.2013",
}


class Checker:
    def __init__(self) -> None:
        self.failures: list[str] = []
        self.warnings: list[str] = []
        self.notes: list[str] = []

    def ok(self, message: str) -> None:
        self.notes.append(f"OK: {message}")

    def warn(self, message: str) -> None:
        self.warnings.append(f"WARN: {message}")

    def fail(self, message: str) -> None:
        self.failures.append(f"FAIL: {message}")

    def require(self, condition: bool, message: str) -> None:
        if condition:
            self.ok(message)
        else:
            self.fail(message)


class AnchorCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[dict[str, str | None]] = []

    def handle_starttag(
        self,
        tag: str,
        attrs: list[tuple[str, str | None]],
    ) -> None:
        if tag == "a":
            self.anchors.append(dict(attrs))


@lru_cache(maxsize=None)
def read_text(rel: Path) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def html_anchors(text: str) -> list[dict[str, str | None]]:
    parser = AnchorCollector()
    parser.feed(text)
    parser.close()
    return parser.anchors


def markdown_section(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(?P<body>.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group("body") if match else ""


def first_markdown_table(text: str) -> str:
    rows: list[str] = []
    for line in text.splitlines():
        if line.startswith("|"):
            rows.append(line)
        elif rows:
            break
    return "\n".join(rows)


def frontmatter_fields(rel: Path) -> dict[str, str]:
    lines = read_text(rel).splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"missing YAML frontmatter in {rel}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise ValueError(f"unclosed YAML frontmatter in {rel}") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([a-zA-Z][a-zA-Z0-9_-]*):\s*(.+)$", line)
        if not match:
            raise ValueError(f"unsupported YAML frontmatter line in {rel}: {line}")
        fields[match.group(1)] = match.group(2).strip().strip('"')
    return fields


def skill_version(rel: Path) -> str:
    match = re.search(r'^Version:\s*([^\n]+)', read_text(rel), re.MULTILINE)
    if not match:
        raise ValueError(f"missing visible version in {rel}")
    return match.group(1).strip()


def check_skill_frontmatter(checker: Checker) -> None:
    expected_names = {
        Path("skill/SKILL.md"): "arbeitszeugnis-pruefer",
        Path("skill/SKILL-mini.md"): "mini-arbeitszeugnis-pruefer",
    }
    for rel, expected_name in expected_names.items():
        fields = frontmatter_fields(rel)
        checker.require(set(fields) == {"name", "description"}, f"{rel} frontmatter has only name and description")
        checker.require(fields.get("name") == expected_name, f"{rel} has the expected skill name")
        checker.require(len(fields.get("description", "")) >= 80, f"{rel} has a substantive trigger description")


def github_slug(text: str) -> str:
    text = re.sub(r"<[^>]*>", "", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.strip().lower()
    chars: list[str] = []
    for char in text:
        if char.isalnum() or char in {" ", "-", "_"}:
            chars.append(char)
        elif unicodedata.category(char).startswith("M"):
            chars.append(char)
    slug = "".join(chars)
    slug = re.sub(r"\s", "-", slug)
    return slug


def markdown_headings(text: str) -> set[str]:
    slugs: set[str] = set()
    counts: dict[str, int] = {}
    for line in text.splitlines():
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        base = github_slug(match.group(2).strip().rstrip("#").strip())
        count = counts.get(base, 0)
        slug = base if count == 0 else f"{base}-{count}"
        counts[base] = count + 1
        slugs.add(slug)
    return slugs


def check_versions(checker: Checker) -> str:
    version = skill_version(Path("skill/SKILL.md"))
    mini_version = skill_version(Path("skill/SKILL-mini.md"))
    docs_version = skill_version(Path("docs/SKILL.md"))
    docs_mini_version = skill_version(Path("docs/SKILL-mini.md"))
    checker.require(
        len({version, mini_version, docs_version, docs_mini_version}) == 1,
        f"skill and docs versions agree at {version}",
    )

    readme = read_text(Path("README.md"))
    index = read_text(Path("docs/index.html"))
    changelog = read_text(Path("CHANGELOG.md"))
    checker.require(f"Version {version}" in readme, "README mentions current version")
    checker.require(f"--github-release v{version}" in readme, "README release-check command uses current version")
    checker.require(f"Stand: Version {version}" in index, "download page identifies the current version")
    checker.require(f"## [{version}]" in changelog, "CHANGELOG has current version entry")
    checker.require(f"[{version}]: https://github.com/" in changelog, "CHANGELOG has release link reference")
    return version


def check_ci_workflow(checker: Checker) -> None:
    path = ROOT / INTEGRITY_WORKFLOW
    checker.require(path.exists(), f"{INTEGRITY_WORKFLOW} exists")
    checker.require(not (ROOT / ".github/workflows/sync-docs.yml").exists(), "legacy mutating docs workflow is absent")
    if not path.exists():
        return

    workflow = path.read_text(encoding="utf-8")
    checkout_action = re.search(r"uses:\s*actions/checkout@v(\d+)", workflow)
    python_action = re.search(r"uses:\s*actions/setup-python@v(\d+)", workflow)
    checker.require("pull_request:" in workflow and "branches: [main]" in workflow, "integrity CI covers pull requests and main")
    checker.require("python3 scripts/check_release_integrity.py" in workflow, "integrity CI runs the repository checker")
    checker.require(
        "pip install --requirement requirements-build.txt" in workflow
        and "build_generated_testakten.py --verify-reproducible" in workflow,
        "integrity CI installs pinned PDF dependencies and rebuilds artifacts twice",
    )
    checker.require("contents: read" in workflow, "integrity CI uses read-only repository permissions")
    checker.require("git push" not in workflow and "contents: write" not in workflow, "integrity CI cannot mutate main")
    checker.require(
        checkout_action is not None and int(checkout_action.group(1)) >= 5,
        "integrity CI uses a Node 24-compatible checkout action",
    )
    checker.require(
        python_action is not None and int(python_action.group(1)) >= 6,
        "integrity CI uses a Node 24-compatible Python setup action",
    )


def check_docs_sync(checker: Checker) -> None:
    pairs = [
        (Path("skill/SKILL.md"), Path("docs/SKILL.md")),
        (Path("skill/SKILL-mini.md"), Path("docs/SKILL-mini.md")),
    ]
    for source, copy in pairs:
        checker.require((ROOT / source).read_bytes() == (ROOT / copy).read_bytes(), f"{copy} mirrors {source}")


def check_mini_size(checker: Checker) -> None:
    for rel in (Path("skill/SKILL-mini.md"), Path("docs/SKILL-mini.md")):
        size = len(read_text(rel))
        checker.require(size <= MINI_LIMIT, f"{rel} has {size} characters <= {MINI_LIMIT}")


def check_legal_citations(checker: Checker) -> None:
    full = read_text(Path("skill/SKILL.md"))
    mini = read_text(Path("skill/SKILL-mini.md"))
    readme = read_text(Path("README.md"))
    index = read_text(Path("docs/index.html"))

    case_pattern = re.compile(
        r"\d+\s+(?:AZR|AZB|AZN|ABR|ABN|SLa|Sa|Ta|Ca)\s+"
        r"\d+(?:\s+b)?/\d+(?:\s+\([A-Z]\))?"
    )
    anchored_cases = {
        match
        for line in full.splitlines()
        if line.startswith("| **")
        for match in case_pattern.findall(line)
    }
    checker.require(
        anchored_cases == set(CANONICAL_DECISION_DATES),
        "canonical date map covers every decision-table entry",
    )

    missing_dates = [
        f"{date} – {case}"
        for case, date in CANONICAL_DECISION_DATES.items()
        if f"{date} – {case}" not in full
    ]
    if missing_dates:
        checker.fail(f"missing canonical decision citations: {', '.join(missing_dates)}")
    else:
        checker.ok(f"all {len(CANONICAL_DECISION_DATES)} canonical decision dates are present")

    dated_case_pattern = re.compile(
        r"(?P<date>\d{2}\.\d{2}\.\d{4})\s*[–-]\s*"
        r"(?P<case>\d+\s+(?:AZR|AZB|AZN|ABR|ABN|SLa|Sa|Ta|Ca)\s+"
        r"\d+(?:\s+b)?/\d+"
        r"(?:\s+\([A-Z]\))?)"
    )
    citation_conflicts: list[str] = []
    dated_citation_count = 0
    legal_surfaces = sorted((*ROOT.rglob("*.md"), *ROOT.rglob("*.html")))
    for path in legal_surfaces:
        if ".git" in path.parts:
            continue
        for match in dated_case_pattern.finditer(path.read_text(encoding="utf-8")):
            dated_citation_count += 1
            case = match.group("case")
            date = match.group("date")
            canonical = CANONICAL_DECISION_DATES.get(case)
            if canonical is None:
                citation_conflicts.append(f"{path.relative_to(ROOT)}: untracked {date} – {case}")
            elif canonical != date:
                citation_conflicts.append(
                    f"{path.relative_to(ROOT)}: {date} – {case}, expected {canonical}"
                )
    if citation_conflicts:
        checker.fail("conflicting dated legal citations: " + "; ".join(citation_conflicts))
    else:
        checker.ok(
            f"all {dated_citation_count} dated case citations across Markdown/HTML use canonical dates"
        )

    all_case_mentions: set[str] = set()
    mention_locations: dict[str, set[str]] = {}
    for path in legal_surfaces:
        if ".git" in path.parts:
            continue
        rel = path.relative_to(ROOT).as_posix()
        for case in case_pattern.findall(path.read_text(encoding="utf-8")):
            all_case_mentions.add(case)
            mention_locations.setdefault(case, set()).add(rel)
    untracked_mentions = sorted(all_case_mentions - set(CANONICAL_DECISION_DATES))
    if untracked_mentions:
        details = "; ".join(
            f"{case} in {', '.join(sorted(mention_locations[case]))}"
            for case in untracked_mentions
        )
        checker.fail(f"undated or otherwise untracked case citations found: {details}")
    else:
        checker.ok(
            f"all {len(all_case_mentions)} case identifiers across Markdown/HTML are canonical, including undated mentions"
        )

    required_full = [
        "§ 109 GewO und BAG-Linie",
        "§ 630 BGB",
        "§ 16 Abs. 1 und 2, § 26 BBiG",
        "§§ 280 Abs. 1 und 2, 286 BGB",
        "§ 5 Abs. 1 Satz 3 ArbGG",
        "Zwischenzeugnis kann ohne tarifliche Regelung als vertragliche Nebenpflicht",
    ]
    required_mini = [
        "§ 109 GewO/BAG-Linie: Arbeitnehmer-Endzeugnis",
        "§ 630 BGB: dauerndes Dienstverhältnis außerhalb des Arbeitnehmerstatus",
        "§ 16 Abs. 1/2 BBiG",
        "über § 26 BBiG",
        "Zwischenzeugnis bei triftigem Grund",
        "Rechtsweg statusabhängig",
        "Betroffenenperspektive",
    ]
    checker.require(all(item in full for item in required_full), "full skill keeps status-specific legal anchors")
    checker.require(all(item in mini for item in required_mini), "mini skill keeps status-specific legal anchors")
    checker.require(
        "bei Organpersonen Status und" in readme and "§§ 2, 5 ArbGG" in readme,
        "README keeps the organ-person jurisdiction gate",
    )
    official_links = [
        "https://www.gesetze-im-internet.de/gewo/__109.html",
        "https://www.gesetze-im-internet.de/bgb/__630.html",
        "https://www.gesetze-im-internet.de/bbig_2005/__16.html",
        "https://www.gesetze-im-internet.de/bbig_2005/__26.html",
        "https://www.gesetze-im-internet.de/arbgg/__2.html",
        "https://www.gesetze-im-internet.de/arbgg/__5.html",
        "https://www.gesetze-im-internet.de/arbgg/__12a.html",
    ]
    checker.require(all(link in readme for link in official_links), "README links every central statute to an official source")
    checker.require(
        "Perspektive der beurteilten Person" in index
        and "Arbeitgeber, Dienstgeber oder Ausbildende" in index,
        "download page keeps role and legal status separate",
    )

    forbidden = [
        "28.06.2016 – 9 AZR 8/15",
        "§§ 286, 288 BGB",
        "§ 288 BGB",
        "§ 16 Abs. 1 BBiG — Anspruch auf einfaches Zeugnis",
        "§ 13 BBiG — Pflichten des Auszubildenden",
        "Arbeitsgericht zuständig; Zeugnisberichtigung",
        "PATRIOT Act § 215",
        "typischerweise personenbezogene Daten besonderer Kategorien",
        "das **stärkste Signal** im Bewerbungsverkehr",
        "Verwirkung bei langem Zuwarten",
        "wer ohne nachvollziehbaren Grund lange zuwartet, riskiert den Anspruchsverlust",
        "wenn die Schlussformel z. B. unwahre Tatsachen suggeriert",
        "eine kalendermäßige Frist macht die Mahnung beweisbar",
        "mindestens eine 🔴- oder 🟠-Beanstandung",
        "mit 🔴/🟠 oder sonstigem Berichtigungspunkt",
        "Vier von fünf Bausteinen vorhanden | Note 2",
        "Drei Bausteine | Note 3",
        "Fehlt der Steigerer im gesamten Zeugnis, ist Note 1 nicht erreichbar",
        "signalisiert genau das Gegenteil",
        "bewusste Irreführung",
        "Karenz nicht erwähnt",
        "Sorglosigkeit oder Absicht",
        "fehlender Berufsschulabschnitt",
        "riskante Suchtmittel-Lesart",
        "riskante Alkohol-/Geselligkeitslesart",
        "riskante Annäherungs-/Belästigungslesart",
        "riskante Eigentums-/Vertrauenslesart",
        "riskante Belästigungs-Lesart",
        "Note 4–6",
        "Notentendenz 1 bis 6",
        "keine Pünktlichkeitsaussage",
        "es gab sonst nichts Positives zu sagen",
        "Verdacht auf Gefälligkeit",
        "Distanzsignal; Arbeitgeberkündigung",
        "Passivkonstruktion** („Das Arbeitsverhältnis endet\"): Distanzsignal",
        "Datumsangabe ohne weitere Worte** am Ende: Kalte Trennung",
        "Branchenüblichkeit guter Noten ist kein Argument vor Gericht",
    ]
    combined = "\n".join((full, mini, readme))
    stale = [item for item in forbidden if item in combined]
    if stale:
        checker.fail(f"stale or overbroad legal wording found: {', '.join(stale)}")
    else:
        checker.ok("known stale or overbroad legal wording is absent")

    decision_rows = {
        line.split("** |", 1)[0]: line
        for line in full.splitlines()
        if line.startswith("| **") and " – " in line
    }
    lag_12 = next((line for key, line in decision_rows.items() if "12 Ta 475/16" in key), "")
    lag_4 = next((line for key, line in decision_rows.items() if "4 Ta 118/16" in key), "")
    lag_9 = next((line for key, line in decision_rows.items() if "9 Ta 319/25" in key), "")
    lag_6 = next((line for key, line in decision_rows.items() if "6 SLa 25/24" in key), "")
    bag_3 = next((line for key, line in decision_rows.items() if "3 AZR 121/11" in key), "")
    bag_5 = next((line for key, line in decision_rows.items() if "5 AZR 848/93" in key), "")
    bag_8 = next((line for key, line in decision_rows.items() if "9 AZR 8/15" in key), "")
    bag_838 = next((line for key, line in decision_rows.items() if "8 AZR 838/13" in key), "")
    bag_48 = next((line for key, line in decision_rows.items() if "9 AZR 48/24" in key), "")
    bag_227 = next((line for key, line in decision_rows.items() if "9 AZR 227/11" in key), "")
    bag_248 = next((line for key, line in decision_rows.items() if "9 AZR 248/07" in key), "")
    bag_262 = next((line for key, line in decision_rows.items() if "9 AZR 262/20" in key), "")
    bag_352 = next((line for key, line in decision_rows.items() if "9 AZR 352/04" in key), "")
    checker.require(
        "Schlussformel" in bag_227 and "tabellar" not in bag_227,
        "9 AZR 227/11 remains assigned to closing formulas",
    )
    checker.require(
        "Zwischenzeugnis" in bag_248 and "Betriebsübergang" in bag_248,
        "9 AZR 248/07 carries intermediate-certificate self-binding",
    )
    checker.require(
        "tabellar" in bag_262 and "Schlussformel" not in bag_262,
        "9 AZR 262/20 remains assigned to tabular form",
    )
    checker.require(
        "Maßregelungsverbot" in bag_352 and "Empfängerhorizont" in bag_352,
        "9 AZR 352/04 keeps its verified correction rules",
    )
    checker.require(
        "Ironisch" in lag_12 and "Unterschrift" not in lag_12,
        "12 Ta 475/16 is limited to ironic over-fulfilment",
    )
    checker.require(
        "Unterschrift" in lag_4 and "quer" in lag_4,
        "4 Ta 118/16 carries the signature rule",
    )
    checker.require(
        "Briefkopf" in lag_9 and "Firmenbogen" in lag_9,
        "9 Ta 319/25 carries the letterhead rule",
    )
    checker.require(
        "tatsächlichen Ausfertigung" in lag_6 and "abweichende Vereinbarung" in lag_6,
        "6 SLa 25/24 carries the direct issue-date rule",
    )
    checker.require(
        "nicht als Arbeitsverhältnis" in bag_3
        and "§ 630 BGB" in bag_3
        and "§ 109 GewO" in bag_3,
        "3 AZR 121/11 keeps the concrete retraining status distinction",
    )
    checker.require(
        "Papierzeugnis" in bag_5 and "elektronischer Form" in bag_5,
        "5 AZR 848/93 remains limited to physical-certificate collection",
    )
    checker.require(
        "keine pauschale Regel" in bag_8 and "Prozessbeschäftigung" in bag_8,
        "9 AZR 8/15 is not misused as a general issue-date rule",
    )
    checker.require(
        "Zeitmoment" in bag_838
        and "Umstandsmoment" in bag_838
        and "bloßes Zuwarten" in bag_838
        and "besonderen Umständen" in bag_838,
        "8 AZR 838/13 carries both elements and the exceptional nature of forfeiture",
    )
    checker.require(
        "digitale Entgeltabrechnungen" in bag_48
        and "5 AZR 848/93" in bag_48
        and "nicht" in bag_48
        and "§ 126a BGB" in bag_48,
        "9 AZR 48/24 confirms work-paper collection without replacing certificate e-form rules",
    )
    checker.require(
        "Entfernung der gesamten Schlussformel" in full
        and "Unwahre objektive Tatsachenangaben" in full
        and "nur Entfernung, kein Wunschtext" in mini,
        "closing-formula remedies remain separated from factual corrections",
    )
    checker.require(
        "Verwirkung ist keine feste Monatsfrist" in full
        and "Zeit- und Umstandsmoment" in mini,
        "forfeiture is not reduced to delay or a fixed month threshold",
    )
    checker.require(
        "schriftliche, nachweisbar zugegangene Aufforderung" in full
        and "ersetzt aber weder Anspruchsgrundlage noch Prüfung der Verzugsvoraussetzungen" in full,
        "demand, provable receipt and default remain distinct",
    )
    checker.require(
        "Gegenseitenschreiben nur bei passender Rolle und passendem Rechtsstatus" in full
        and "Bei HR-, Arbeitgeber-, Betriebsrats- oder neutraler Schulungsperspektive"
        in full
        and "Bei HR-/Arbeitgeberperspektive: keine Droh- oder Aufforderungslogik"
        in mini
        and "Ohne belastbaren Punkt: kein Gegenseitenschreiben" in mini,
        "Codex review regression: autonomous demand letters remain role-gated",
    )
    checker.require(
        "Klarheit, Verständlichkeit und Verbot kodierter Negativaussagen gelten"
        " für jedes Zeugnis" in full
        and "Klarheit/Geheimzeichenverbot für jedes" in mini,
        "Codex review regression: section 109(2) remains applicable to every certificate",
    )
    checker.require(
        "Wahrheit und verständiges Wohlwollen" in mini,
        "Codex review regression: mini skill retains truth and goodwill",
    )
    checker.require(
        "Die Ampelfarbe allein löst kein Anspruchsschreiben aus" in full
        and "Ampel allein begründet keinen Anspruch" in mini
        and "freundliche Änderungsbitte ohne Rechtsverstoß, Anspruchsbehauptung oder Klageandrohung"
        in full,
        "finding colour, grade and legal enforceability remain separated",
    )
    checker.require(
        "sprachliche Prüfhypothesen, keine gerichtlich festgelegte Geheimcode-Liste" in full
        and "keine gerichtliche Phrase-zu-Note-Liste" in mini
        and "verwirft gerade die pauschale Umkehrung" in full,
        "code-word heuristics cannot masquerade as fixed case law",
    )
    checker.require(
        "Keine feste Übersetzungsregel" in full
        and "Keine Suchtmittelbehauptung ableiten" in full
        and "keine Belästigung ableiten" in full
        and "geschützte Betätigung nicht als Leistungsdefizit behandeln" in full,
        "sensitive-topic wording remains neutral and evidence-gated",
    )
    checker.require(
        "kein gesetzlicher Mindestmangel nach § 16 Abs. 2 BBiG" in full
        and "§ 16 Abs. 2 BBiG verlangt sie nicht automatisch" in full,
        "vocational-school assessment is not invented as mandatory BBiG content",
    )
    checker.require(
        "Notentendenz 1 bis 5" in full
        and "typischerweise Note 4–5" in full
        and "häufig Note 4-5" in mini,
        "full and mini skills use the same five-level grading scale",
    )
    checker.require(
        "weder gesetzlich festgelegt noch für sich ein BAG-Code" in full
        and "nur Sprachkonvention, kein fester Rechtscode" in mini,
        "social-behaviour ordering is not presented as a fixed legal code",
    )
    checker.require(
        "Seitenvollständigkeit und OCR-Treue" in full
        and "OCR-Fehler nicht als Zeugnisfehler" in mini
        and "Wortlaut nie stillschweigend korrigieren" in full,
        "PDF and OCR review remains source-faithful",
    )
    checker.require(
        "vollständige Kompaktmodus" in full
        and "Kompakt" in full
        and "Voll" in full
        and "Batch" in full
        and "Fortsetzungsmarke erst nach den geschuldeten Schreiben" in mini,
        "execution modes and mandatory-block continuation order remain coherent",
    )
    checker.require(
        "keine allgemeine Loyalitätsformel verlangen" in full
        and "Pünktlichkeitsaussage" not in full
        and "Geburtsdatum nur, wenn vorhanden und sachlich benötigt" in full,
        "omission and personal-data checks remain evidence-gated",
    )
    checker.require(
        "neutrale Tatsachenform; nur zusammen mit weiteren Signalen bewerten" in full
        and "keine gesetzliche Unvollständigkeit" in full
        and "keine isolierte Gesamtnote" in full,
        "closing-formula and isolated-integrity language remains non-mechanical",
    )
    checker.require(
        "maßregelnde Streichung" in full
        and "maßregelnde Streichung" in mini
        and "9 AZR 272/22" in full
        and "§ 612a BGB" in mini,
        "closing-formula rules preserve the anti-retaliation exception",
    )
    checker.require(
        "das tatsächliche Ausstellungsdatum trägt" in full
        and "Kunden, falls tatsächlicher Kundenkontakt bestand" in full
        and "Freiwillige Schlussformelwünsche" in full,
        "claim template keeps issue date, contact profile and voluntary closing wishes legally gated",
    )

    exercise = read_text(
        Path(
            "testakten/arbeitszeugnis-analyse-bluehendes-leben/"
            "90-ergaenzende-korrespondenz-und-vollvermerke.md"
        )
    )
    checker.require(
        "Floristin Wiebke Hagedorn und Arbeitgeberin" not in exercise
        and "Bescheide, Akteneinsicht" not in exercise
        and "Ausformulierte Erklärung an die Arbeitnehmerin" in exercise
        and "Entwurf an die Arbeitgeberin" in exercise,
        "supplemental exercise remains a role-consistent certificate workflow",
    )


def check_generated_build_contract(checker: Checker) -> None:
    aggregate = read_text(Path("scripts/build_generated_testakten.py"))
    checker.require(
        "--verify-reproducible" in aggregate and "CURATED_FILES" in aggregate,
        "aggregate builder verifies reproducibility and protects curated files",
    )
    checker.require(
        "ThreadPoolExecutor" in aggregate and "executor.map(run_builder, BUILDERS)" in aggregate,
        "aggregate builder runs independent test sets concurrently",
    )
    checker.require(
        "build_master_archive" in aggregate
        and "expected 25 individual test PDFs" in aggregate
        and "PUBLIC_MASTER_ARCHIVE" in aggregate,
        "aggregate builder creates and publishes the complete 25-case archive",
    )

    builders = [
        Path("scripts/build_allgemeine_testakten.py"),
        Path("scripts/build_jura_und_wissenschaft_testakten.py"),
        Path("scripts/build_leitungsfunktionen_testakten.py"),
    ]
    checker.require(
        all(rel.as_posix() in aggregate for rel in builders),
        "aggregate builder invokes all three test-set builders",
    )
    for rel in builders:
        source = read_text(rel)
        checker.require(
            "write_testimony_pdf" in source and "write_reproducible_zip" in source,
            f"{rel} uses the shared PDF renderer and canonical ZIP writer",
        )
        checker.require(
            "normalize_pdf(combined, expected_date_count=0)" in source,
            f"{rel} normalizes its combined PDF",
        )
        checker.require(
            "shutil.rmtree(OUT)" not in source,
            f"{rel} preserves curated archive files",
        )
        checker.require(
            "\n    write_readme()\n" not in source,
            f"{rel} does not overwrite its curated README",
        )
        checker.require(
            "ThreadPoolExecutor" in source
            and "max_workers=min(PDF_WORKERS, len(CASES))" in source,
            f"{rel} builds case PDFs with bounded concurrency",
        )
        checker.require(
            all(
                f'"{field}"' in source
                for field in ("grade", "must_find", "guardrail", "output")
            ),
            f"{rel} carries calibrated grade, finding, guardrail and output expectations",
        )

    general_sources = sorted(
        (
            ROOT / "testakten/arbeitszeugnis-analyse-bluehendes-leben/quellen"
        ).glob("[0-9][0-9]-*.txt")
    )
    checker.require(
        len(general_sources) == 10
        and [path.name[:2] for path in general_sources]
        == [f"{number:02d}" for number in range(1, 11)],
        "general test set has exactly the versioned source files 01 through 10",
    )

    helper = read_text(Path("scripts/reproducible_test_artifacts.py"))
    checker.require(
        "expected_date_count" in helper
        and "duplicate ZIP input" in helper
        and "outside" in helper
        and "empty ZIP archive" in helper,
        "artifact helper rejects incomplete PDF metadata and unsafe ZIP inputs",
    )
    renderer = read_text(Path("scripts/render_testzeugnis.py"))
    checker.require(
        "SimpleDocTemplate" in renderer
        and "invariant" in renderer
        and "normalize_pdf(pdf_path, expected_date_count=2)" in renderer
        and "Fiktive Testakte" in renderer,
        "shared renderer produces deterministic, visibly marked A4 test certificates",
    )
    checker.require(
        read_text(Path("requirements-build.txt")).strip() == "reportlab==5.0.0",
        "test-PDF renderer dependency is exactly pinned",
    )

    generated_case_pdfs = [
        *sorted(
            (ROOT / "testakten/arbeitszeugnis-analyse-bluehendes-leben").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
        *sorted(
            (ROOT / "testakten/arbeitszeugnisse-jura-und-wissenschaft").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
        *sorted(
            (ROOT / "testakten/arbeitszeugnisse-leitungsfunktionen").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
    ]
    checker.require(
        len(generated_case_pdfs) == 25
        and all(
            pdf.read_bytes().count(CANONICAL_PDF_DATE) == 2
            for pdf in generated_case_pdfs
        ),
        "all 25 generated case PDFs use canonical creation and modification dates",
    )
    checker.require(
        all(
            b"ReportLab PDF Library" in pdf.read_bytes()
            and b"/BaseFont /Helvetica" in pdf.read_bytes()
            for pdf in generated_case_pdfs
        ),
        "all 25 generated case PDFs use the shared proportional-font layout",
    )

    generated_zips = [
        Path(
            "testakten/arbeitszeugnis-analyse-bluehendes-leben/"
            "arbeitszeugnis-testakten-einzel-pdfs.zip"
        ),
        Path(
            "testakten/arbeitszeugnisse-jura-und-wissenschaft/"
            "arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"
        ),
        Path(
            "testakten/arbeitszeugnisse-leitungsfunktionen/"
            "arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"
        ),
        Path("testakten/arbeitszeugnis-testpaket-komplett.zip"),
    ]
    zip_metadata_is_stable = True
    zip_entries_are_sorted = True
    for rel in generated_zips:
        with zipfile.ZipFile(ROOT / rel) as archive:
            names = archive.namelist()
            zip_metadata_is_stable = zip_metadata_is_stable and all(
                info.date_time == ZIP_TIMESTAMP
                and info.external_attr >> 16 == ZIP_FILE_MODE
                for info in archive.infolist()
            )
            zip_entries_are_sorted = zip_entries_are_sorted and names == sorted(names)
    checker.require(
        zip_metadata_is_stable,
        "generated ZIP archives use canonical entry metadata",
    )
    checker.require(zip_entries_are_sorted, "generated ZIP entries use canonical order")

    master = ROOT / "testakten/arbeitszeugnis-testpaket-komplett.zip"
    with zipfile.ZipFile(master) as archive:
        names = archive.namelist()
    checker.require(
        len(names) == 34
        and sum(name.endswith(".pdf") for name in names) == 25
        and "README.md" in names
        and "TESTFALL-MATRIX.md" in names,
        "complete test archive contains 25 PDFs and all nine guidance files",
    )

    matrix = read_text(Path("testakten/TESTFALL-MATRIX.md"))
    matrix_numbers = re.findall(r"^\|\s*(\d{2})\s*\|", matrix, re.MULTILINE)
    checker.require(
        matrix_numbers == [f"{number:02d}" for number in range(1, 26)],
        "central test matrix covers cases 01 through 25 exactly once and in order",
    )
    matrix_grades = dict(
        re.findall(
            r"^\|\s*(\d{2})\s*\|[^|]*\|\s*([^|]+?)\s*\|",
            matrix,
            re.MULTILINE,
        )
    )
    builder_grades: dict[str, str] = {}
    for rel in builders:
        tree = ast.parse(read_text(rel), filename=str(rel))
        cases_assignment = next(
            node
            for node in tree.body
            if isinstance(node, ast.Assign)
            and any(
                isinstance(target, ast.Name) and target.id == "CASES"
                for target in node.targets
            )
        )
        for case in ast.literal_eval(cases_assignment.value):
            builder_grades[str(case["nr"])] = str(case["grade"])
    checker.require(
        builder_grades == matrix_grades,
        "all 25 builder grade corridors exactly match the central test matrix",
    )
    for rel, expected_cases in (
        (
            Path(
                "testakten/arbeitszeugnis-analyse-bluehendes-leben/"
                "90-erwartungshorizont-und-pruefpunkte.md"
            ),
            10,
        ),
        (
            Path(
                "testakten/arbeitszeugnisse-jura-und-wissenschaft/"
                "90-erwartungshorizont-und-pruefpunkte.md"
            ),
            10,
        ),
        (
            Path(
                "testakten/arbeitszeugnisse-leitungsfunktionen/"
                "90-erwartungshorizont-und-pruefpunkte.md"
            ),
            5,
        ),
    ):
        expectation = read_text(rel)
        checker.require(
            expectation.count("### Fall ") == expected_cases
            and expectation.count("**Muss erkannt werden:**") == expected_cases
            and expectation.count("**Nicht überdehnen:**") == expected_cases
            and expectation.count("**Erwarteter One-Shot-Ausgang:**")
            == expected_cases,
            f"{rel} has complete per-case finding, guardrail and output expectations",
        )


def check_quality_audit(checker: Checker) -> None:
    path = ROOT / QUALITY_AUDIT
    checker.require(path.exists(), f"{QUALITY_AUDIT} exists")
    if not path.exists():
        return

    row_pattern = re.compile(
        r"^\|\s*(\d{1,3})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*(Behoben)\s*\|$",
        re.MULTILINE,
    )
    rows = row_pattern.findall(read_text(QUALITY_AUDIT))
    numbers = [int(number) for number, _, _, _ in rows]
    checker.require(numbers == list(range(1, 101)), "quality audit has exactly the ordered findings 1 through 100")
    checker.require(
        all(finding.strip() and fix.strip() for _, finding, fix, _ in rows),
        "every quality-audit finding has a concrete remediation",
    )


def check_text_hygiene(checker: Checker) -> None:
    suffixes = {".html", ".md", ".py", ".txt", ".yaml", ".yml"}
    paths = sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in suffixes
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
    )
    problems: list[str] = []
    for path in paths:
        data = path.read_bytes()
        rel = path.relative_to(ROOT)
        if data.startswith(b"\xef\xbb\xbf"):
            problems.append(f"{rel}: UTF-8 BOM")
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            problems.append(f"{rel}: not UTF-8")
            continue
        if data and not data.endswith(b"\n"):
            problems.append(f"{rel}: missing final newline")
        if b"\r\n" in data:
            problems.append(f"{rel}: CRLF line endings")
    if problems:
        checker.fail("text hygiene problems: " + "; ".join(problems))
    else:
        checker.ok(f"all {len(paths)} text files are UTF-8/LF without BOM and end in a newline")

    git = shutil.which("git")
    if not git:
        checker.warn("git not found; skipped tracked-junk check")
        return
    result = subprocess.run(
        [git, "ls-files"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
        timeout=PROCESS_TIMEOUT_SECONDS,
    )
    tracked = result.stdout.splitlines()
    junk = [
        name
        for name in tracked
        if PurePosixPath(name).name == ".DS_Store"
        or "__pycache__" in PurePosixPath(name).parts
        or PurePosixPath(name).suffix in {".pyc", ".pyo"}
    ]
    checker.require(not junk, "repository tracks no OS metadata or Python cache files")


def check_markdown_table_shapes(checker: Checker) -> None:
    separator = re.compile(r"\s*\|(?:\s*:?-{3,}:?\s*\|)+\s*")
    malformed: list[str] = []
    checked = 0
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        index = 0
        while index < len(lines):
            if not lines[index].lstrip().startswith("|"):
                index += 1
                continue
            start = index
            block: list[str] = []
            while index < len(lines) and lines[index].lstrip().startswith("|"):
                block.append(lines[index])
                index += 1
            if len(block) < 2 or not separator.fullmatch(block[1]):
                continue
            checked += 1
            cell_counts = [
                len(re.split(r"(?<!\\)\|", line.strip())) - 2
                for line in block
            ]
            if len(set(cell_counts)) != 1:
                malformed.append(
                    f"{path.relative_to(ROOT)}:{start + 1} ({cell_counts})"
                )
    if malformed:
        checker.fail("malformed Markdown tables: " + ", ".join(malformed))
    else:
        checker.ok(f"all {checked} Markdown tables have consistent column counts")


def check_markdown_anchors(checker: Checker) -> None:
    link_re = re.compile(r"\[[^\]]+\]\(#([^)]+)\)")
    for rel in MARKDOWN_WITH_ANCHORS:
        text = read_text(rel)
        slugs = markdown_headings(text)
        missing = []
        for target in link_re.findall(text):
            slug = unquote(target).strip()
            if slug and slug not in slugs:
                missing.append(slug)
        if missing:
            checker.fail(f"{rel} missing anchors: {', '.join(sorted(set(missing)))}")
        else:
            checker.ok(f"{rel} internal markdown anchors resolve")


def check_markdown_local_links(checker: Checker) -> None:
    link_re = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    broken: list[str] = []
    checked = 0
    markdown_files = sorted(
        path.relative_to(ROOT)
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )

    for rel in markdown_files:
        for raw_target in link_re.findall(read_text(rel)):
            href = raw_target.strip().strip("<>").split(maxsplit=1)[0]
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc or href.startswith("#"):
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            checked += 1
            target_path = (ROOT / rel.parent / target).resolve()
            try:
                target_rel = target_path.relative_to(ROOT)
            except ValueError:
                broken.append(f"{rel}: {href}")
                continue
            if not target_path.exists():
                broken.append(f"{rel}: {href}")
                continue
            if parsed.fragment and target_path.suffix.lower() == ".md":
                fragment = unquote(parsed.fragment).strip()
                if fragment not in markdown_headings(read_text(target_rel)):
                    broken.append(f"{rel}: {href} (missing anchor)")

    if broken:
        checker.fail(f"broken local markdown links: {', '.join(broken)}")
    else:
        checker.ok(f"all local markdown links resolve ({checked} checked across {len(markdown_files)} files)")


def check_html_links(checker: Checker) -> None:
    href_re = re.compile(r'href=["\']([^"\']+)["\']')
    id_re = re.compile(r'id=["\']([^"\']+)["\']')
    for rel in HTML_FILES:
        text = read_text(rel)
        local_ids = set(id_re.findall(text))
        broken: list[str] = []
        checked = 0
        for href in href_re.findall(text):
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            if href.startswith("#"):
                checked += 1
                if unquote(parsed.fragment) not in local_ids:
                    broken.append(f"{href} (missing anchor)")
                continue
            target = unquote(parsed.path)
            if not target:
                continue
            checked += 1
            target_path = (ROOT / rel.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                broken.append(href)
                continue
            if not target_path.exists():
                broken.append(href)
                continue
            if parsed.fragment:
                anchor_file = target_path / "index.html" if target_path.is_dir() else target_path
                if anchor_file.suffix.lower() == ".html":
                    target_ids = set(id_re.findall(anchor_file.read_text(encoding="utf-8")))
                    if unquote(parsed.fragment) not in target_ids:
                        broken.append(f"{href} (missing anchor)")
        if broken:
            checker.fail(f"{rel} broken local links: {', '.join(broken)}")
        else:
            checker.ok(f"{rel} local links resolve ({checked} checked)")


def check_navigation_inventory(checker: Checker) -> None:
    readme = read_text(Path("README.md"))
    direct_section = markdown_section(readme, "Direktdownloads")
    download_table = first_markdown_table(direct_section)
    checker.require(bool(download_table), "README has a direct-download table")

    missing_readme_assets = []
    for rel in RELEASE_ASSET_CANDIDATES:
        url = f"{LATEST_RELEASE_URL}/download/{rel.name}"
        if url not in download_table:
            missing_readme_assets.append(rel.name)
    if missing_readme_assets:
        checker.fail(
            "README direct-download table misses release assets: "
            + ", ".join(missing_readme_assets)
        )
    else:
        checker.ok(
            f"README direct-download table lists all {len(RELEASE_ASSET_CANDIDATES)} release assets"
        )
    checker.require(
        f"https://github.com/{REPOSITORY}/archive/refs/heads/main.zip" in download_table,
        "README direct-download table includes the complete repository archive",
    )

    map_section = markdown_section(readme, "Repository-Landkarte")
    missing_targets = [
        rel.as_posix()
        for rel in README_NAVIGATION_TARGETS
        if f"({rel.as_posix()})" not in map_section
    ]
    if missing_targets:
        checker.fail(
            "README repository map misses critical files: "
            + ", ".join(missing_targets)
        )
    else:
        checker.ok(
            f"README repository map links all {len(README_NAVIGATION_TARGETS)} critical files"
        )

    index = read_text(Path("docs/index.html"))
    quick_start = index.find('id="schnellzugriff"')
    quick_end = index.find('id="skills"', quick_start + 1)
    quick_access = index[quick_start:quick_end] if quick_start >= 0 and quick_end > quick_start else ""
    checker.require(bool(quick_access), "download page has a bounded quick-access section")
    quick_anchors = html_anchors(quick_access)
    missing_page_assets = []
    for rel in RELEASE_ASSET_CANDIDATES:
        href = rel.relative_to("docs").as_posix()
        matches = [anchor for anchor in quick_anchors if anchor.get("href") == href]
        if not any("download" in anchor for anchor in matches):
            missing_page_assets.append(rel.name)
    if missing_page_assets:
        checker.fail(
            "download-page quick access misses direct assets: "
            + ", ".join(missing_page_assets)
        )
    else:
        checker.ok(
            f"download-page quick access exposes all {len(RELEASE_ASSET_CANDIDATES)} release assets"
        )

    index_targets = [
        "blob/main/README.md",
        "blob/main/skill/SKILL.md",
        "blob/main/skill/SKILL-mini.md",
        "blob/main/testakten/README.md",
        "blob/main/testakten/TESTFALL-MATRIX.md",
        "blob/main/testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md",
        "blob/main/testakten/arbeitszeugnis-analyse-bluehendes-leben/90-erwartungshorizont-und-pruefpunkte.md",
        "blob/main/testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md",
        "blob/main/testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md",
        "blob/main/testakten/arbeitszeugnisse-leitungsfunktionen/README.md",
        "blob/main/testakten/arbeitszeugnisse-leitungsfunktionen/90-erwartungshorizont-und-pruefpunkte.md",
        "tree/main/scripts",
        "blob/main/CHANGELOG.md",
        "blob/main/QUALITY-AUDIT-100.md",
        "blob/main/.github/workflows/verify-integrity.yml",
        "blob/main/scripts/check_release_integrity.py",
        "blob/main/scripts/build_generated_testakten.py",
        "blob/main/scripts/build_allgemeine_testakten.py",
        "blob/main/scripts/build_jura_und_wissenschaft_testakten.py",
        "blob/main/scripts/build_leitungsfunktionen_testakten.py",
        "blob/main/scripts/render_testzeugnis.py",
        "blob/main/scripts/reproducible_test_artifacts.py",
        "blob/main/LICENSE-APACHE",
        "blob/main/LICENSE-MIT",
    ]
    missing_index_targets = [target for target in index_targets if target not in index]
    if missing_index_targets:
        checker.fail(
            "download-page wayfinder misses critical destinations: "
            + ", ".join(missing_index_targets)
        )
    else:
        checker.ok(
            f"download-page wayfinder links all {len(index_targets)} critical destinations"
        )

    helper_expectations = {
        Path("docs/download-skill.html"): "SKILL.md",
        Path("docs/download-mini.html"): "SKILL-mini.md",
    }
    for rel, filename in helper_expectations.items():
        anchors = html_anchors(read_text(rel))
        checker.require(
            any(
                anchor.get("href") == filename and "download" in anchor
                for anchor in anchors
            ),
            f"{rel} keeps its visible direct-download fallback",
        )
        checker.require(
            any(anchor.get("href") == LATEST_RELEASE_URL for anchor in anchors)
            and any(
                anchor.get("href") == "SHA256SUMS.txt" and "download" in anchor
                for anchor in anchors
            ),
            f"{rel} links the release inventory and checksums",
        )

    readme_names = {rel.parent.name: rel for rel in TEST_READMES}
    common_test_links = [
        "../../README.md",
        "../README.md",
        "../TESTFALL-MATRIX.md",
        f"{LATEST_RELEASE_URL}/download/SKILL.md",
        f"{LATEST_RELEASE_URL}/download/SKILL-mini.md",
        f"{LATEST_RELEASE_URL}/download/SHA256SUMS.txt",
        f"{LATEST_RELEASE_URL}/download/arbeitszeugnis-testpaket-komplett.zip",
        LATEST_RELEASE_URL,
    ]
    for current_name, rel in readme_names.items():
        text = read_text(rel)
        sibling_links = [
            f"../{name}/README.md"
            for name in readme_names
            if name != current_name
        ]
        checker.require(
            all(link in text for link in [*common_test_links, *sibling_links]),
            f"{rel} links home, both skills, release inventory, checksums and sibling test sets",
        )


def check_public_artifacts(checker: Checker) -> None:
    for source, public, zip_count in PUBLIC_ARTIFACTS:
        source_path = ROOT / source
        public_path = ROOT / public
        checker.require(source_path.exists(), f"{source} exists")
        checker.require(public_path.exists(), f"{public} exists")
        if source_path.exists() and public_path.exists():
            checker.require(source_path.read_bytes() == public_path.read_bytes(), f"{public} mirrors {source}")
        if zip_count is not None and source_path.exists():
            with zipfile.ZipFile(source_path) as archive:
                infos = archive.infolist()
                names = [info.filename for info in infos]
                pdfs = [name for name in names if name.lower().endswith(".pdf")]
                corrupt = archive.testzip()
            checker.require(corrupt is None, f"{source} passes ZIP CRC validation")
            checker.require(len(names) == len(set(names)), f"{source} has no duplicate entries")
            checker.require(
                all(
                    name
                    and not name.startswith(("/", "\\"))
                    and ".." not in PurePosixPath(name).parts
                    for name in names
                ),
                f"{source} has no absolute or traversal entry names",
            )
            checker.require(
                all(info.file_size > 0 for info in infos),
                f"{source} has no empty entries",
            )
            checker.require(len(pdfs) == zip_count, f"{source} contains {zip_count} PDFs")
        if source.suffix == ".pdf" and source_path.exists():
            checker.require(source_path.read_bytes().startswith(b"%PDF"), f"{source} is a PDF file")

    jura_pdfs = sorted((ROOT / "testakten/arbeitszeugnisse-jura-und-wissenschaft").glob("[0-9][0-9]-*/Arbeitszeugnis_*.pdf"))
    leadership_pdfs = sorted((ROOT / "testakten/arbeitszeugnisse-leitungsfunktionen").glob("[0-9][0-9]-*/Arbeitszeugnis_*.pdf"))
    general_pdfs = sorted((ROOT / "testakten/arbeitszeugnis-analyse-bluehendes-leben").glob("[0-9][0-9]-*/Arbeitszeugnis_*.pdf"))
    checker.require(len(jura_pdfs) == 10, "Jura/Wissenschaft test set has 10 individual PDFs")
    checker.require(len(leadership_pdfs) == 5, "Leitungsfunktionen test set has 5 individual PDFs")
    checker.require(len(general_pdfs) == 10, "general test set has 10 individual PDFs")


def check_release_asset_candidates(checker: Checker) -> None:
    for rel in RELEASE_ASSET_CANDIDATES:
        path = ROOT / rel
        checker.require(path.exists() and path.stat().st_size > 0, f"{rel} is ready for release upload")


@lru_cache(maxsize=None)
def sha256_digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def expected_release_checksums() -> str:
    lines = []
    for rel in CHECKSUM_ASSET_CANDIDATES:
        digest = sha256_digest(ROOT / rel)
        lines.append(f"{digest}  {rel.name}")
    return "\n".join(lines) + "\n"


def check_release_checksums(checker: Checker) -> None:
    rel = Path("docs/SHA256SUMS.txt")
    path = ROOT / rel
    checker.require(path.exists(), f"{rel} exists")
    if path.exists():
        manifest = path.read_text(encoding="utf-8")
        entries: list[tuple[str, str]] = []
        malformed: list[str] = []
        for line_number, line in enumerate(manifest.splitlines(), 1):
            match = re.fullmatch(r"([0-9a-f]{64})  ([^/\\]+)", line)
            if match:
                entries.append((match.group(1), match.group(2)))
            else:
                malformed.append(f"line {line_number}")
        names = [name for _, name in entries]
        expected_names = [item.name for item in CHECKSUM_ASSET_CANDIDATES]
        checker.require(not malformed, f"{rel} uses strict SHA-256 manifest syntax")
        checker.require(len(names) == len(set(names)), f"{rel} has no duplicate filenames")
        checker.require(names == expected_names, f"{rel} lists exactly the release assets in canonical order")
        checker.require(manifest == expected_release_checksums(), f"{rel} matches release assets")


def github_commit_sha(gh: str, ref: str) -> str:
    result = subprocess.run(
        [gh, "api", f"repos/{REPOSITORY}/commits/{ref}", "--jq", ".sha"],
        text=True,
        capture_output=True,
        check=True,
        timeout=PROCESS_TIMEOUT_SECONDS,
    )
    return result.stdout.strip()


def check_github_release_assets(checker: Checker, tag: str, version: str) -> None:
    gh = shutil.which("gh")
    if not gh:
        checker.fail("gh not found; cannot verify published GitHub release assets")
        return

    try:
        result = subprocess.run(
            [
                gh,
                "release",
                "view",
                tag,
                "--repo",
                REPOSITORY,
                "--json",
                "assets,isDraft,isPrerelease,tagName,targetCommitish,url",
            ],
            text=True,
            capture_output=True,
            check=True,
            timeout=PROCESS_TIMEOUT_SECONDS,
        )
    except subprocess.CalledProcessError as exc:
        checker.fail(f"GitHub release {tag} could not be read: {exc.stderr.strip() or exc}")
        return

    release = json.loads(result.stdout)
    checker.require(tag == f"v{version}", f"requested GitHub release tag matches local version v{version}")
    checker.require(release.get("tagName") == tag, f"GitHub release tag is {tag}")
    checker.require(release.get("targetCommitish") == "main", "GitHub release targets main")
    checker.require(not release.get("isDraft"), "GitHub release is published, not draft")
    checker.require(not release.get("isPrerelease"), "GitHub release is not a prerelease")

    expected_assets = {
        rel.name: {
            "size": (ROOT / rel).stat().st_size,
            "digest": f"sha256:{sha256_digest(ROOT / rel)}",
        }
        for rel in RELEASE_ASSET_CANDIDATES
    }
    assets = {asset["name"]: asset for asset in release.get("assets", [])}
    missing = sorted(set(expected_assets) - set(assets))
    extra = sorted(set(assets) - set(expected_assets))
    checker.require(not missing, f"GitHub release has all expected assets ({len(expected_assets)})")
    checker.require(not extra, "GitHub release has no unexpected assets")

    for name, expected in sorted(expected_assets.items()):
        asset = assets.get(name)
        if not asset:
            continue
        checker.require(asset.get("state") == "uploaded", f"GitHub release asset {name} is uploaded")
        checker.require(asset.get("size") == expected["size"], f"GitHub release asset {name} size matches local file")
        checker.require(asset.get("digest") == expected["digest"], f"GitHub release asset {name} SHA-256 matches local file")

    try:
        tag_sha = github_commit_sha(gh, tag)
        main_sha = github_commit_sha(gh, "main")
    except subprocess.CalledProcessError as exc:
        checker.fail(f"GitHub commit target could not be verified: {exc.stderr.strip() or exc}")
    else:
        checker.require(tag_sha == main_sha, f"GitHub tag {tag} points to the current main commit")


def check_pdf_details(checker: Checker) -> None:
    pdfinfo = shutil.which("pdfinfo")
    pdftotext = shutil.which("pdftotext")
    pdffonts = shutil.which("pdffonts")
    if not pdfinfo:
        checker.warn("pdfinfo not found; skipped all detailed PDF metadata checks")
    if not pdftotext:
        checker.warn("pdftotext not found; skipped all PDF text extraction checks")
    if not pdffonts:
        checker.warn("pdffonts not found; skipped generated-PDF font checks")

    def run(command: list[str]) -> tuple[str | None, str | None]:
        try:
            result = subprocess.run(
                command,
                text=True,
                capture_output=True,
                check=True,
                timeout=PROCESS_TIMEOUT_SECONDS,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
            return None, str(exc)
        return result.stdout, None

    available = [detail for detail in COMBINED_PDF_DETAILS if (ROOT / detail[0]).exists()]
    for rel, label, *_ in COMBINED_PDF_DETAILS:
        if not (ROOT / rel).exists():
            checker.fail(f"{label} combined PDF is missing")

    futures: dict[tuple[str, Path], Future[tuple[str | None, str | None]]] = {}
    worker_count = max(1, min(6, len(available) * 2))
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for rel, _, *_ in available:
            combined = ROOT / rel
            if pdfinfo:
                futures[("info", rel)] = executor.submit(run, [pdfinfo, str(combined)])
            if pdftotext:
                futures[("text", rel)] = executor.submit(run, [pdftotext, str(combined), "-"])

    for rel, label, minimum_pages, expected_headings, expected_attachments in available:
        if pdfinfo:
            info, error = futures[("info", rel)].result()
            if error:
                checker.fail(f"{label} pdfinfo failed: {error}")
            else:
                assert info is not None
                checker.require("Encrypted:       no" in info, f"{label} combined PDF is not encrypted")
                page_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
                checker.require(
                    bool(page_match and int(page_match.group(1)) >= minimum_pages),
                    f"{label} combined PDF has at least {minimum_pages} pages",
                )

        if pdftotext:
            extracted, error = futures[("text", rel)].result()
            if error:
                checker.fail(f"{label} pdftotext failed: {error}")
                continue
            assert extracted is not None
            headings = sum(
                1
                for line in extracted.splitlines()
                if line.strip()
                in {
                    "ARBEITSZEUGNIS",
                    "ZWISCHENZEUGNIS",
                    "Arbeitszeugnis",
                    "Zwischenzeugnis",
                }
            )
            checker.require(
                headings == expected_headings,
                f"{label} combined PDF contains {expected_headings} certificate headings (found {headings})",
            )
            if expected_attachments is not None:
                attachments = sum(
                    1
                    for line in extracted.splitlines()
                    if line.strip().startswith("PDF-Anhang:")
                )
                checker.require(
                    attachments == expected_attachments,
                    f"{label} combined PDF contains {expected_attachments} PDF attachment markers (found {attachments})",
                )

    generated = [
        *sorted(
            (ROOT / "testakten/arbeitszeugnis-analyse-bluehendes-leben").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
        *sorted(
            (ROOT / "testakten/arbeitszeugnisse-jura-und-wissenschaft").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
        *sorted(
            (ROOT / "testakten/arbeitszeugnisse-leitungsfunktionen").glob(
                "[0-9][0-9]-*/Arbeitszeugnis_*.pdf"
            )
        ),
    ]
    detail_futures: dict[
        tuple[str, Path], Future[tuple[str | None, str | None]]
    ] = {}
    commands_per_pdf = sum(tool is not None for tool in (pdfinfo, pdftotext, pdffonts))
    with ThreadPoolExecutor(
        max_workers=max(1, min(12, len(generated) * commands_per_pdf))
    ) as executor:
        for pdf in generated:
            if pdfinfo:
                detail_futures[("info", pdf)] = executor.submit(
                    run, [pdfinfo, str(pdf)]
                )
            if pdftotext:
                detail_futures[("text", pdf)] = executor.submit(
                    run, [pdftotext, "-layout", str(pdf), "-"]
                )
            if pdffonts:
                detail_futures[("fonts", pdf)] = executor.submit(
                    run, [pdffonts, str(pdf)]
                )

    transliteration_pattern = re.compile(
        r"\b(?:fuer|ueber\w*|gegenueber|verfueg\w*|geschaeft\w*|"
        r"taetig\w*|qualitaet\w*|fuehr\w*|rueck\w*|persoen\w*|"
        r"arbeitsablaeuf\w*|besprechungsfaell\w*|betriebsraet\w*|"
        r"buero|beduerf\w*|europae\w*|geaendert\w*|"
        r"interdisziplinaer\w*|kaufmaenn\w*|krankenhaeus\w*|"
        r"perspektivklaer\w*|praesenz|umsetzungsstaerke|"
        r"verguet\w*|einschraenk\w*)\b",
        re.IGNORECASE,
    )
    for pdf in generated:
        relative = pdf.relative_to(ROOT)
        case_number = pdf.parent.name[:2]
        if pdfinfo:
            info, error = detail_futures[("info", pdf)].result()
            if error:
                checker.fail(f"{relative} pdfinfo failed: {error}")
            else:
                assert info is not None
                page_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
                page_count = int(page_match.group(1)) if page_match else 0
                checker.require(
                    1 <= page_count <= 2
                    and "(A4)" in info
                    and "Encrypted:       no" in info,
                    f"{relative} is an unencrypted one- or two-page A4 document",
                )
                checker.require(
                    "Producer:        ReportLab PDF Library" in info,
                    f"{relative} identifies the deterministic ReportLab renderer",
                )
        else:
            page_count = 0

        if pdftotext:
            extracted, error = detail_futures[("text", pdf)].result()
            if error:
                checker.fail(f"{relative} pdftotext failed: {error}")
            else:
                assert extracted is not None
                pages = [page for page in extracted.split("\f") if page.strip()]
                checker.require(
                    f"Fiktive Testakte | Fall {case_number}" in extracted
                    and extracted.count("Fiktive Testakte | Fall") == len(pages),
                    f"{relative} visibly marks every page as fictitious and case-specific",
                )
                checker.require(
                    all(len(page.strip()) >= 500 for page in pages),
                    f"{relative} has no empty or signature-only page",
                )
                checker.require(
                    transliteration_pattern.search(extracted) is None,
                    f"{relative} uses proper German typography instead of legacy ASCII transliteration",
                )
                if page_count:
                    checker.require(
                        len(pages) == page_count,
                        f"{relative} extracted page boundaries match PDF metadata",
                    )

        if pdffonts:
            fonts, error = detail_futures[("fonts", pdf)].result()
            if error:
                checker.fail(f"{relative} pdffonts failed: {error}")
            else:
                assert fonts is not None
                checker.require(
                    "Helvetica" in fonts and "Courier" not in fonts,
                    f"{relative} uses proportional standard fonts and no monospaced body font",
                )


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--github-release",
        metavar="TAG",
        help="also verify the published GitHub release assets for TAG, e.g. v3.0.21",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="skip external pdfinfo/pdftotext inspection for a fast edit loop",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="print every successful invariant instead of the compact summary",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    checker = Checker()
    try:
        check_skill_frontmatter(checker)
        version = check_versions(checker)
        check_ci_workflow(checker)
        check_docs_sync(checker)
        check_mini_size(checker)
        check_legal_citations(checker)
        check_generated_build_contract(checker)
        check_quality_audit(checker)
        check_text_hygiene(checker)
        check_markdown_table_shapes(checker)
        check_markdown_anchors(checker)
        check_markdown_local_links(checker)
        check_html_links(checker)
        check_navigation_inventory(checker)
        check_public_artifacts(checker)
        check_release_checksums(checker)
        check_release_asset_candidates(checker)
        if args.quick:
            checker.ok("quick mode skipped external PDF metadata/text inspection")
        else:
            check_pdf_details(checker)
        if args.github_release:
            check_github_release_assets(checker, args.github_release, version)
    except Exception as exc:  # pragma: no cover - top-level diagnostics
        checker.fail(f"unexpected check error: {exc}")
        version = "unknown"

    print(f"release integrity check for version {version}")
    if args.verbose:
        for note in checker.notes:
            print(note)
    else:
        print(f"{len(checker.notes)} invariants passed")
    for warning in checker.warnings:
        print(warning)
    for failure in checker.failures:
        print(failure)

    if checker.failures:
        print(f"{len(checker.failures)} failure(s)", file=sys.stderr)
        return 1
    print("all release integrity checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
