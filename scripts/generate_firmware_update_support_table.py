#!/usr/bin/env python3
"""
Regenerate docs/guides/firmware-update-method-support-table.csv from docs/variants/*/releases.md

Each releases.md is scanned for bullets, under a "### Added" heading, whose
link text is exactly one of these bullet titles: "Firmware Update Mode",
"Capsule Update V1", "FWUPD support", "LVFS support", "Capsule Update V2".
"""

import csv
import io
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
VARIANTS_DIR = REPO_ROOT / "docs/variants"
CSV_PATH = REPO_ROOT / "docs/guides/firmware-update-method-support-table.csv"

# Not real hardware
EXCLUDED_VARIANTS = {"qemu_q35"}

FEATURES = [
    ("Firmware Update Mode", "[Firmware Update Mode][fum]"),
    ("Capsule Update V1", "[Capsule Update V1][cup1]"),
    ("FWUPD support", "[FWUPD][fwupd]"),
    ("LVFS support", "[LVFS][lvfs]"),
    ("Capsule Update V2", "[Capsule Update V2][cup2]"),
]
FEATURE_NAMES = {name for name, _ in FEATURES}
HEADER = ["Manufacturer", "Device"] + [column for _, column in FEATURES]

VERSION_HEADING_RE = re.compile(r"^##\s+v(\d+(?:\.\d+)*)\b")
SECTION_HEADING_RE = re.compile(r"^###\s+(.+)$")
BULLET_RE = re.compile(r"^-\s*\[([^\]]+)\]")
TITLE_RE = re.compile(r"^#\s+(.+?)\s+Dasharo Release Notes\s*$", re.IGNORECASE)


def normalize(a, b):
    n = max(len(a), len(b))
    return a + (0,) * (n - len(a)), b + (0,) * (n - len(b))


def parse_manufacturer_device(text):
    for line in text.splitlines():
        if not line.startswith("#"):
            continue
        match = TITLE_RE.match(line.strip())
        if not match:
            return None, None
        words = match.group(1).split(None, 1)
        return (words[0], words[1]) if len(words) == 2 else (words[0], "")
    return None, None


def parse_feature_versions(text):
    """Return {feature_name: version_tuple} for the lowest version
    each searched bullet appears under in this file.
    """
    best = {}
    current_version = None
    in_added_section = False
    for line in text.splitlines():
        match = VERSION_HEADING_RE.match(line)
        if match:
            current_version = tuple(int(x) for x in match.group(1).split("."))
            in_added_section = False
            continue
        match = SECTION_HEADING_RE.match(line)
        if match:
            in_added_section = match.group(1).strip().lower() == "added"
            continue
        if not in_added_section or current_version is None:
            continue
        match = BULLET_RE.match(line.strip())
        if not match or match.group(1).strip() not in FEATURE_NAMES:
            continue
        title = match.group(1).strip()
        previous = best.get(title)
        if previous is None:
            best[title] = current_version
        else:
            a, b = normalize(current_version, previous)
            if a < b:
                best[title] = current_version
    return best


def format_version(version):
    return "v" + ".".join(map(str, version))


def collect_rows():
    rows = []
    for releases_md in sorted(VARIANTS_DIR.glob("*/releases.md")):
        if releases_md.parent.name in EXCLUDED_VARIANTS:
            continue
        text = releases_md.read_text()
        manufacturer, device = parse_manufacturer_device(text)
        if manufacturer is None:
            continue
        versions = parse_feature_versions(text)
        if not versions:
            continue
        row = [manufacturer, device]
        row.extend(
            format_version(versions[name]) if name in versions else "-"
            for name, _ in FEATURES
        )
        rows.append(row)
    rows.sort(key=lambda row: (row[0].lower(), row[1].lower()))
    return rows


def render_csv(rows):
    buf = io.StringIO()
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(HEADER)
    writer.writerows(rows)
    return buf.getvalue()


def main():
    new_content = render_csv(collect_rows())
    old_content = CSV_PATH.read_text() if CSV_PATH.exists() else None
    if new_content == old_content:
        return 0
    CSV_PATH.write_text(new_content)
    print(f"Regenerated {CSV_PATH.relative_to(
        REPO_ROOT)} from releases.md changelogs.")
    print("Review the change and stage the file, then commit again.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
