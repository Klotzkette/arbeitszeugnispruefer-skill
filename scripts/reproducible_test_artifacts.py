#!/usr/bin/env python3
"""Helpers for byte-reproducible PDF and ZIP test artifacts."""

from __future__ import annotations

import hashlib
import re
import zipfile
from pathlib import Path
from typing import Iterable


CANONICAL_PDF_DATE = b"D:20000101000000Z00'00'"
ZIP_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
ZIP_FILE_MODE = 0o100644
_PDF_DATE_RE = re.compile(
    rb"/(CreationDate|ModDate) \(D:\d{14}(?:Z00'00'|[+-]\d{2}'\d{2}')\)"
)
_HEX_ID_RE = re.compile(
    rb"/ID\s*\[\s*<([0-9a-fA-F]{32})>\s*<([0-9a-fA-F]{32})>\s*\]"
)


def _replace_hex_pdf_id(data: bytes) -> bytes | None:
    matches = list(_HEX_ID_RE.finditer(data))
    if not matches:
        return None
    if len(matches) != 1:
        raise ValueError(f"expected one hexadecimal PDF ID, found {len(matches)}")

    match = matches[0]
    normalized = bytearray(data)
    for group in (1, 2):
        start, end = match.span(group)
        normalized[start:end] = b"0" * (end - start)
    stable_id = hashlib.sha256(normalized).hexdigest()[:32].encode("ascii")
    for group in (1, 2):
        start, end = match.span(group)
        normalized[start:end] = stable_id
    return bytes(normalized)


def _replace_literal_pdf_id(data: bytes) -> bytes | None:
    starts = [match.start() for match in re.finditer(rb"/ID \[", data)]
    if not starts:
        return None
    if len(starts) != 1:
        raise ValueError(f"expected one literal PDF ID, found {len(starts)}")
    start = starts[0]
    root = data.rfind(b"/Root")
    xref = data.rfind(b"\nxref", 0, start)
    if xref < 0 or root < start:
        raise ValueError("literal PDF ID is not in a classic trailer")

    placeholder = b"0" * 16
    canonical_id = b"/ID [(" + placeholder + b") (" + placeholder + b") ] "
    canonical = data[:start] + canonical_id + data[root:]
    stable_id = hashlib.sha256(canonical).hexdigest()[:16].encode("ascii")
    stable = b"/ID [(" + stable_id + b") (" + stable_id + b") ] "
    return data[:start] + stable + data[root:]


def normalize_pdf(path: Path, *, expected_date_count: int | None = None) -> None:
    """Remove volatile timestamps and derive a stable PDF file identifier."""

    data = path.read_bytes()
    date_count = len(_PDF_DATE_RE.findall(data))
    if expected_date_count is not None and date_count != expected_date_count:
        raise ValueError(
            f"expected {expected_date_count} PDF date fields in {path}, found {date_count}"
        )
    data = _PDF_DATE_RE.sub(
        lambda match: b"/" + match.group(1) + b" (" + CANONICAL_PDF_DATE + b")",
        data,
    )
    normalized = _replace_hex_pdf_id(data)
    if normalized is None:
        normalized = _replace_literal_pdf_id(data)
    if normalized is None:
        raise ValueError(f"no supported PDF file identifier found in {path}")
    if normalized.count(CANONICAL_PDF_DATE) != date_count:
        raise ValueError(f"PDF dates were not normalized completely in {path}")
    path.write_bytes(normalized)


def write_reproducible_zip(path: Path, root: Path, files: Iterable[Path]) -> None:
    """Write files in a stable order with fixed ZIP metadata."""

    root = root.resolve()
    entries: list[tuple[Path, Path]] = []
    seen: set[str] = set()
    for source in files:
        resolved = source.resolve()
        if not resolved.is_file():
            raise ValueError(f"ZIP input is not a file: {source}")
        try:
            relative = resolved.relative_to(root)
        except ValueError as exc:
            raise ValueError(f"ZIP input is outside {root}: {source}") from exc
        archive_name = relative.as_posix()
        if archive_name in seen:
            raise ValueError(f"duplicate ZIP input: {archive_name}")
        seen.add(archive_name)
        entries.append((relative, resolved))
    if not entries:
        raise ValueError("refusing to write an empty ZIP archive")

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for relative, source in sorted(entries, key=lambda item: item[0].as_posix()):
            info = zipfile.ZipInfo(
                relative.as_posix(),
                date_time=ZIP_TIMESTAMP,
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = ZIP_FILE_MODE << 16
            archive.writestr(
                info,
                source.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )
