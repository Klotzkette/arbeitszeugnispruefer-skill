#!/usr/bin/env python3
"""Check release-critical repository invariants.

The script is intentionally dependency-light. It validates the things that tend
to break during a release: version drift, stale docs copies, broken local links,
oversized mini skill files and missing public test artifacts.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
MINI_LIMIT = 7500

MARKDOWN_WITH_ANCHORS = [
    Path("README.md"),
    Path("CHANGELOG.md"),
    Path("skill/SKILL.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/README.md"),
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft/90-erwartungshorizont-und-pruefpunkte.md"),
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
]


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


def frontmatter_version(rel: Path) -> str:
    match = re.search(r'^version:\s*["\']?([^"\'\n]+)', read_text(rel), re.MULTILINE)
    if not match:
        raise ValueError(f"missing frontmatter version in {rel}")
    return match.group(1).strip()


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
    return slug.strip("-")


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
    version = frontmatter_version(Path("skill/SKILL.md"))
    mini_version = frontmatter_version(Path("skill/SKILL-mini.md"))
    docs_version = frontmatter_version(Path("docs/SKILL.md"))
    docs_mini_version = frontmatter_version(Path("docs/SKILL-mini.md"))
    checker.require(
        len({version, mini_version, docs_version, docs_mini_version}) == 1,
        f"skill and docs versions agree at {version}",
    )

    readme = read_text(Path("README.md"))
    index = read_text(Path("docs/index.html"))
    changelog = read_text(Path("CHANGELOG.md"))
    checker.require(f"Version {version}" in readme, "README mentions current version")
    checker.require(f"Version {version}" in index, "download page mentions current version")
    checker.require(f"## [{version}]" in changelog, "CHANGELOG has current version entry")
    checker.require(f"[{version}]: https://github.com/" in changelog, "CHANGELOG has release link reference")
    return version


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


def check_html_links(checker: Checker) -> None:
    href_re = re.compile(r'href=["\']([^"\']+)["\']')
    for rel in HTML_FILES:
        text = read_text(rel)
        broken: list[str] = []
        checked = 0
        for href in href_re.findall(text):
            parsed = urlsplit(href)
            if parsed.scheme or href.startswith("#") or parsed.netloc:
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
    general_pdfs = sorted((ROOT / "testakten/arbeitszeugnis-analyse-bluehendes-leben").glob("[0-9][0-9]-*/Arbeitszeugnis_*.pdf"))
    checker.require(len(jura_pdfs) == 10, "Jura/Wissenschaft test set has 10 individual PDFs")
    checker.require(len(general_pdfs) == 10, "general test set has 10 individual PDFs")


def check_pdf_details(checker: Checker) -> None:
    pdfinfo = shutil.which("pdfinfo")
    pdftotext = shutil.which("pdftotext")
    combined = ROOT / "testakten/arbeitszeugnisse-jura-und-wissenschaft/gesamt-pdf/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"
    if not combined.exists():
        checker.fail("Jura/Wissenschaft combined PDF is missing")
        return

    if pdfinfo:
        info = subprocess.run([pdfinfo, str(combined)], text=True, capture_output=True, check=True).stdout
        checker.require("Encrypted:       no" in info, "Jura/Wissenschaft combined PDF is not encrypted")
        page_match = re.search(r"^Pages:\s+(\d+)$", info, re.MULTILINE)
        checker.require(bool(page_match and int(page_match.group(1)) >= 10), "Jura/Wissenschaft combined PDF has at least 10 pages")
    else:
        checker.warn("pdfinfo not found; skipped detailed PDF metadata check")

    if pdftotext:
        text = subprocess.run([pdftotext, str(combined), "-"], text=True, capture_output=True, check=True).stdout
        headings = len(re.findall(r"\b(?:ARBEITSZEUGNIS|ZWISCHENZEUGNIS)\b", text))
        checker.require(headings == 10, "Jura/Wissenschaft combined PDF contains 10 certificate headings")
    else:
        checker.warn("pdftotext not found; skipped PDF text extraction check")


def main() -> int:
    checker = Checker()
    try:
        version = check_versions(checker)
        check_docs_sync(checker)
        check_mini_size(checker)
        check_markdown_anchors(checker)
        check_html_links(checker)
        check_public_artifacts(checker)
        check_pdf_details(checker)
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
