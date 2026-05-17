#!/usr/bin/env python3
"""Validate deterministic file-level requirements for zine deck PDFs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def count_pages_with_library(path: Path) -> tuple[int | None, str | None]:
    for module_name in ("pypdf", "PyPDF2"):
        try:
            module = __import__(module_name)
        except ImportError:
            continue

        try:
            reader = module.PdfReader(str(path))
            return len(reader.pages), module_name
        except Exception:
            continue

    return None, None


def count_pages_by_marker(path: Path) -> tuple[int, str]:
    data = path.read_bytes()
    pages = len(re.findall(rb"/Type\s*/Page\b", data))
    return pages, "pdf-marker-scan"


def validate_pdf(path: Path, min_pages: int, max_pages: int, min_bytes: int) -> dict[str, object]:
    result: dict[str, object] = {
        "path": str(path),
        "ok": False,
        "errors": [],
    }

    errors: list[str] = []

    if not path.exists():
        errors.append("file does not exist")
        result["errors"] = errors
        return result

    if path.suffix.lower() != ".pdf":
        errors.append("file extension is not .pdf")

    size = path.stat().st_size
    result["bytes"] = size
    if size < min_bytes:
        errors.append(f"file is too small: {size} bytes < {min_bytes} bytes")

    try:
        header = path.read_bytes()[:5]
    except OSError as exc:
        errors.append(f"cannot read file: {exc}")
        result["errors"] = errors
        return result

    if header != b"%PDF-":
        errors.append("file does not start with a PDF header")

    page_count, method = count_pages_with_library(path)
    if page_count is None:
        page_count, method = count_pages_by_marker(path)

    result["page_count"] = page_count
    result["page_count_method"] = method

    if page_count < min_pages or page_count > max_pages:
        errors.append(f"expected {min_pages}-{max_pages} pages, found {page_count}")

    result["ok"] = not errors
    result["errors"] = errors
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a zine deck PDF file.")
    parser.add_argument("pdf", type=Path, help="Path to the generated PDF deck.")
    parser.add_argument("--min-pages", type=int, default=7)
    parser.add_argument("--max-pages", type=int, default=8)
    parser.add_argument("--min-bytes", type=int, default=1024)
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    args = parser.parse_args()

    result = validate_pdf(args.pdf, args.min_pages, args.max_pages, args.min_bytes)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    elif result["ok"]:
        print(f"ok: {result['path']} has {result['page_count']} PDF pages")
    else:
        print(f"invalid: {result['path']}", file=sys.stderr)
        for error in result["errors"]:
            print(f"- {error}", file=sys.stderr)

    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
