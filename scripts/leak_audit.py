#!/usr/bin/env python3
"""Simple leak audit for the public NLM Researcher skill repo.

This is intentionally conservative. Add project-specific private terms before publishing.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

DEFAULT_PATTERNS = [
    r"/Users/[A-Za-z0-9._-]+",
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    r"ghp_[A-Za-z0-9_]+",
    r"github_pat_[A-Za-z0-9_]+",
    r"sk-[A-Za-z0-9_-]{20,}",
    r"AIza[A-Za-z0-9_-]+",
    r"(?i)csrf[_ -]?token\s*[:=]",
    r"(?i)session[_-]?id\s*[:=]",
    r"(?i)password\s*[:=]",
    r"(?i)secret\s*[:=]",
    r"(?i)private[_ -]?key\s*[:=]",
]

# Terms that are not necessarily secrets, but should not appear in this publicized template.
PRIVATE_CONTEXT_TERMS = [
    "AI PMO",
    "AIPMO",
    "Apple Notes",
    "WhatsApp",
    "K0",
    "T-017",
    "aqantive",
    "enkay",
    "Nirav",
    "Medha-private",
]

SKIP_DIRS = {".git", "__pycache__", ".cache", "node_modules"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".html", ".css", ".js", ""}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in TEXT_SUFFIXES:
            yield path


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    findings = []
    compiled = [(p, re.compile(p)) for p in DEFAULT_PATTERNS]
    for path in iter_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        rel = path.relative_to(root)
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, regex in compiled:
                if regex.search(line):
                    # Allow this script to mention its own generic patterns.
                    if rel.as_posix() == "scripts/leak_audit.py" and label in line:
                        continue
                    findings.append((rel, lineno, label, line.strip()))
            for term in PRIVATE_CONTEXT_TERMS:
                if term.lower() in line.lower():
                    if rel.as_posix() == "scripts/leak_audit.py" and term in line:
                        continue
                    findings.append((rel, lineno, f"private-context:{term}", line.strip()))
    if findings:
        print("Leak audit failed. Review these lines:")
        for rel, lineno, label, line in findings:
            print(f"{rel}:{lineno}: {label}: {line[:180]}")
        return 1
    print("Leak audit passed: no configured private patterns found.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
