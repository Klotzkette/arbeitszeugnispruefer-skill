#!/usr/bin/env python3
"""Check release-critical repository invariants.

The script is intentionally dependency-light. It validates the things that tend
to break during a release: version drift, stale docs copies, broken local links,
legal-citation drift, oversized mini skill files and missing public test artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REPOSITORY = "Klotzkette/arbeitszeugnispruefer-skill"
MINI_LIMIT = 7500
PROCESS_TIMEOUT_SECONDS = 30
INTEGRITY_WORKFLOW = Path(".github/workflows/verify-integrity.yml")

MARKDOWN_WITH_ANCHORS = [
    Path("README.md"),
    Path("CHANGELOG.md"),
    Path("skill/SKILL.md"),
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md"),
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
]

RELEASE_ASSET_CANDIDATES = CHECKSUM_ASSET_CANDIDATES + [
    Path("docs/SHA256SUMS.txt"),
]

COMBINED_PDF_DETAILS = [
    (
        Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/gesamt-pdf/arbeitszeugnis-analyse-bluehendes-leben_gesamt.pdf"),
        "Allgemeine Branchen",
        10,
        9,
        10,
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
    "8 AZR 293/18": "28.11.2019",
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


def read_text(rel: Path) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


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

    case_pattern = re.compile(r"\d+\s+(?:AZR|AZB|Ta|Ca)\s+\d+(?:\s+b)?/\d+(?:\s+\([A-Z]\))?")
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
                pdfs = [name for name in archive.namelist() if name.endswith(".pdf")]
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


def sha256_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
        checker.require(path.read_text(encoding="utf-8") == expected_release_checksums(), f"{rel} matches release assets")


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
    for rel, label, minimum_pages, expected_headings, expected_attachments in COMBINED_PDF_DETAILS:
        combined = ROOT / rel
        if not combined.exists():
            checker.fail(f"{label} combined PDF is missing")
            continue

        if pdfinfo:
            info = subprocess.run(
                [pdfinfo, str(combined)],
                text=True,
                capture_output=True,
                check=True,
                timeout=PROCESS_TIMEOUT_SECONDS,
            ).stdout
            checker.require("Encrypted:       no" in info, f"{label} combined PDF is not encrypted")
            page_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
            checker.require(
                bool(page_match and int(page_match.group(1)) >= minimum_pages),
                f"{label} combined PDF has at least {minimum_pages} pages",
            )
        else:
            checker.warn("pdfinfo not found; skipped detailed PDF metadata check")

        if pdftotext:
            text = subprocess.run(
                [pdftotext, str(combined), "-"],
                text=True,
                capture_output=True,
                check=True,
                timeout=PROCESS_TIMEOUT_SECONDS,
            ).stdout
            headings = sum(
                1
                for line in text.splitlines()
                if line.strip() in {"ARBEITSZEUGNIS", "ZWISCHENZEUGNIS", "Arbeitszeugnis"}
            )
            checker.require(
                headings == expected_headings,
                f"{label} combined PDF contains {expected_headings} certificate headings (found {headings})",
            )
            if expected_attachments is not None:
                attachments = sum(1 for line in text.splitlines() if line.strip().startswith("PDF-Anhang:"))
                checker.require(
                    attachments == expected_attachments,
                    f"{label} combined PDF contains {expected_attachments} PDF attachment markers (found {attachments})",
                )
        else:
            checker.warn("pdftotext not found; skipped PDF text extraction check")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--github-release",
        metavar="TAG",
        help="also verify the published GitHub release assets for TAG, e.g. v3.0.19",
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
        check_markdown_anchors(checker)
        check_markdown_local_links(checker)
        check_html_links(checker)
        check_public_artifacts(checker)
        check_release_checksums(checker)
        check_release_asset_candidates(checker)
        check_pdf_details(checker)
        if args.github_release:
            check_github_release_assets(checker, args.github_release, version)
    except Exception as exc:  # pragma: no cover - top-level diagnostics
        checker.fail(f"unexpected check error: {exc}")
        version = "unknown"

    print(f"release integrity check for version {version}")
    for note in checker.notes:
        print(note)
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
