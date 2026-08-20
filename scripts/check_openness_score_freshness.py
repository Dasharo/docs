#!/usr/bin/env python3
"""
Fail if a commit adds Dasharo Openness Score chart(s) for a platform/version that
already has a row in docs/variants/overview.md's "Openness comparison" table,
without that row being updated to reference the new version.

Usage:
    check_openness_score_freshness.py <changed-file-path> [...]

Changed file paths should be relative to the repo root.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OVERVIEW = REPO_ROOT / "docs/variants/overview.md"
CHART_SUFFIX = "_openness_chart.png"
VERSION_RE = re.compile(r"_v(\d+(?:\.\d+){1,3})(?=[_.]|$)")


def parse_version_family(filename):
    """Split a ROM/chart filename into (family_key, version_tuple).

    The family key is the filename with its version number replaced by a
    placeholder, so e.g. "foo_v1.2.3_heads.rom" and "foo_v1.3.0_heads.rom"
    share the family "foo_v{VER}_heads.rom" while "foo_igpu_v1.2.3.rom" is a
    distinct family from "foo_v1.2.3.rom".
    """
    match = VERSION_RE.search(filename)
    if not match:
        return None, None
    version = tuple(int(x) for x in match.group(1).split("."))
    family = filename[: match.start()] + "_v{VER}" + filename[match.end() :]
    return family, version


def normalize(a, b):
    n = max(len(a), len(b))
    return a + (0,) * (n - len(a)), b + (0,) * (n - len(b))


def latest_version_on_disk(directory, family_key):
    best = None
    for chart in directory.glob(f"*{CHART_SUFFIX}"):
        rom_name = chart.name[: -len(CHART_SUFFIX)]
        family, version = parse_version_family(rom_name)
        if family != family_key or version is None:
            continue
        if best is None:
            best = version
        else:
            na, nb = normalize(version, best)
            if na > nb:
                best = version
    return best


def parse_overview_rows():
    """Yield (line_no, platform, rom_filename) for each data row of the
    "Openness comparison" table in overview.md."""
    if not OVERVIEW.exists():
        return
    lines = OVERVIEW.read_text().splitlines()
    try:
        start = next(
            i for i, l in enumerate(lines) if l.strip() == "## Openness comparison"
        )
    except StopIteration:
        return
    in_table = False
    for i in range(start, len(lines)):
        line = lines[i]
        if line.startswith("| Platform "):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            break
        if line.startswith("| ---") or line.startswith("|---"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 2:
            continue
        yield i + 1, cols[0], cols[1]


def main(changed_files):
    changed_charts = [REPO_ROOT / f for f in changed_files if f.endswith(CHART_SUFFIX)]
    if not changed_charts:
        return 0

    changed_dirs_families = set()
    for chart in changed_charts:
        rom_name = chart.name[: -len(CHART_SUFFIX)]
        family, _ = parse_version_family(rom_name)
        if family is None:
            continue
        changed_dirs_families.add((chart.parent, family))

    failures = []
    for line_no, platform, rom_filename in parse_overview_rows():
        family, row_version = parse_version_family(rom_filename)
        if family is None:
            continue

        matches = sorted(
            REPO_ROOT.glob(f"docs/variants/*/{rom_filename}{CHART_SUFFIX}")
        )
        if not matches:
            continue
        directory = matches[0].parent

        if (directory, family) not in changed_dirs_families:
            continue

        latest = latest_version_on_disk(directory, family)
        if latest is None:
            continue

        row_norm, latest_norm = normalize(row_version, latest)
        if row_norm < latest_norm:
            failures.append(
                f"docs/variants/overview.md:{line_no}: row '{platform}' "
                f"references {rom_filename} "
                f"(v{'.'.join(map(str, row_version))}), but "
                f"{directory.relative_to(REPO_ROOT)} now has an openness "
                f"score for v{'.'.join(map(str, latest))}."
            )

    if failures:
        print("Openness comparison table (docs/variants/overview.md) is out of date:\n")
        for failure in failures:
            print(f" - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
