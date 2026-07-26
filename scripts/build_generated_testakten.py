#!/usr/bin/env python3
"""Regenerate all generated test-archive artifacts."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from reproducible_test_artifacts import write_reproducible_zip


ROOT = Path(__file__).resolve().parents[1]
BUILD_TIMEOUT_SECONDS = 300
BUILDERS = [
    Path("scripts/build_jura_und_wissenschaft_testakten.py"),
    Path("scripts/build_leitungsfunktionen_testakten.py"),
]
GENERATED_ROOTS = [
    Path("testakten/arbeitszeugnisse-jura-und-wissenschaft"),
    Path("testakten/arbeitszeugnisse-leitungsfunktionen"),
]
TESTAKTEN_ROOT = Path("testakten")
MASTER_ARCHIVE = TESTAKTEN_ROOT / "arbeitszeugnis-testpaket-komplett.zip"
PUBLIC_MASTER_ARCHIVE = Path("docs/testakten") / MASTER_ARCHIVE.name
CURATED_FILES = [
    TESTAKTEN_ROOT / "README.md",
    TESTAKTEN_ROOT / "TESTFALL-MATRIX.md",
    Path("testakten/arbeitszeugnis-analyse-bluehendes-leben/README.md"),
    *[root / "README.md" for root in GENERATED_ROOTS],
]
PUBLIC_ARTIFACTS = [
    Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft-einzel-pdfs.zip"),
    Path("docs/testakten/arbeitszeugnisse-jura-und-wissenschaft_gesamt.pdf"),
    Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen-einzel-pdfs.zip"),
    Path("docs/testakten/arbeitszeugnisse-leitungsfunktionen_gesamt.pdf"),
    PUBLIC_MASTER_ARCHIVE,
]


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def snapshot(paths: list[Path]) -> dict[str, str]:
    return {str(path): digest(ROOT / path) for path in paths}


def artifact_manifest() -> dict[str, str]:
    paths = [
        path.relative_to(ROOT)
        for rel in GENERATED_ROOTS
        for path in sorted((ROOT / rel).rglob("*"))
        if path.is_file()
    ]
    return snapshot(sorted(set(paths + PUBLIC_ARTIFACTS + [MASTER_ARCHIVE])))


def as_text(value: str | bytes | None) -> str:
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", errors="replace")
    return value


def run_builder(rel: Path) -> subprocess.CompletedProcess[str]:
    script = ROOT / rel
    command = [sys.executable, str(script)]
    try:
        return subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
            timeout=BUILD_TIMEOUT_SECONDS,
        )
    except subprocess.TimeoutExpired as exc:
        return subprocess.CompletedProcess(
            command,
            124,
            stdout=as_text(exc.stdout),
            stderr=(
                f"{as_text(exc.stderr)}\n" if exc.stderr else ""
            )
            + f"timed out after {BUILD_TIMEOUT_SECONDS} seconds",
        )
    except OSError as exc:
        return subprocess.CompletedProcess(command, 127, stdout="", stderr=str(exc))


def run_builders() -> None:
    missing = [rel for rel in BUILDERS if not (ROOT / rel).is_file()]
    if missing:
        raise SystemExit(f"missing build scripts: {', '.join(map(str, missing))}")

    for rel in BUILDERS:
        print(f"==> {rel}", flush=True)
    with ThreadPoolExecutor(max_workers=len(BUILDERS)) as executor:
        results = list(executor.map(run_builder, BUILDERS))

    failed: list[str] = []
    for rel, result in zip(BUILDERS, results, strict=True):
        if result.stdout:
            print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
        if result.returncode:
            if result.stderr:
                print(
                    result.stderr,
                    file=sys.stderr,
                    end="" if result.stderr.endswith("\n") else "\n",
                )
            failed.append(f"{rel} (exit {result.returncode})")
    if failed:
        raise SystemExit(f"builder failure: {', '.join(failed)}")


def build_master_archive() -> None:
    root = ROOT / TESTAKTEN_ROOT
    pdfs = sorted(root.glob("*/[0-9][0-9]-*/*.pdf"))
    support_files = sorted(root.glob("*/README.md"))
    support_files += sorted(root.glob("*/90-*.md"))
    support_files += [root / "README.md", root / "TESTFALL-MATRIX.md"]
    if len(pdfs) != 25:
        raise SystemExit(f"expected 25 individual test PDFs, found {len(pdfs)}")
    write_reproducible_zip(
        ROOT / MASTER_ARCHIVE,
        root,
        [*pdfs, *support_files],
    )
    (ROOT / PUBLIC_MASTER_ARCHIVE).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / MASTER_ARCHIVE, ROOT / PUBLIC_MASTER_ARCHIVE)
    print(f"wrote {MASTER_ARCHIVE}")
    print(f"copied {PUBLIC_MASTER_ARCHIVE}")


def build_all() -> None:
    run_builders()
    build_master_archive()


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--verify-reproducible",
        action="store_true",
        help="build twice and fail unless every generated byte is identical",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    curated_before = snapshot(CURATED_FILES)
    build_all()
    if snapshot(CURATED_FILES) != curated_before:
        raise SystemExit("builder changed a curated test-archive README")

    if args.verify_reproducible:
        first = artifact_manifest()
        build_all()
        second = artifact_manifest()
        changed = sorted(
            path
            for path in set(first) | set(second)
            if first.get(path) != second.get(path)
        )
        if changed:
            raise SystemExit(
                f"non-reproducible generated artifacts: {', '.join(changed)}"
            )
        print(f"reproducibility verified for {len(second)} generated files")

    print("all generated test archives rebuilt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
