#!/usr/bin/env python3
"""
Fail if a commit adds Dasharo Openness Score chart(s) for a platform/version that
already has a row in docs/variants/overview.md's "Openness comparison" table,
without that row being updated to reference the new version.

How it works:
- Checks if a changed file is an "*_openness_chart.png".
- For each table row, resolves its ROM filename to a variant directory.
- Skips rows whose directory wasn't touched by this commit.
- Flags a row if its own filename pattern now has a newer chart, or if a
  different pattern in the same directory (that no other row matches to) does.

Usage:
    check_openness_score_freshness.py <changed-file-path>

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


def newest_other_family(
    directory, own_family, row_version, claimed_families=frozenset()
):
    """Return the newest (family, version) other than `own_family` in
    `directory` that beats `row_version`, ignoring `claimed_families` -
    families another row already tracks (e.g. a sibling DDR4/DDR5 row) -
    else None.
    """
    best = None
    for chart in directory.glob(f"*{CHART_SUFFIX}"):
        rom_name = chart.name[: -len(CHART_SUFFIX)]
        family, version = parse_version_family(rom_name)
        if family is None or family == own_family or version is None:
            continue
        if family in claimed_families:
            continue
        if best is None:
            best = (family, version)
        else:
            a, b = normalize(version, best[1])
            if a > b:
                best = (family, version)

    if best is None:
        return None
    a, b = normalize(best[1], row_version)
    return best if a > b else None


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


def resolve_row_directory(rom_filename, family):
    """Resolve a table row's ROM filename to its variant directory, or None
    if it can't be resolved unambiguously.

    Prefers an exact chart match; falls back to matching the prefix before
    the version number, but only when that prefix resolves to exactly one
    directory (sibling variants, e.g. a TU/TNX split, can share a prefix).
    """
    exact_matches = sorted(
        REPO_ROOT.glob(f"docs/variants/*/{rom_filename}{CHART_SUFFIX}")
    )
    if exact_matches:
        return exact_matches[0].parent

    prefix = family.split("_v{VER}")[0]
    prefix_matches = REPO_ROOT.glob(f"docs/variants/*/{prefix}*_v*{CHART_SUFFIX}")
    prefix_dirs = {m.parent for m in prefix_matches}
    if len(prefix_dirs) != 1:
        return None
    return next(iter(prefix_dirs))


def main(changed_files):
    changed_charts = [REPO_ROOT / f for f in changed_files if f.endswith(CHART_SUFFIX)]
    if not changed_charts:
        return 0

    changed_dirs = {chart.parent for chart in changed_charts}

    rows = []
    claimed_families_by_dir = {}
    for line_no, platform, rom_filename in parse_overview_rows():
        family, row_version = parse_version_family(rom_filename)
        if family is None:
            continue
        directory = resolve_row_directory(rom_filename, family)
        if directory is None:
            continue
        rows.append((line_no, platform, rom_filename, family, row_version, directory))
        claimed_families_by_dir.setdefault(directory, set()).add(family)

    failures = []
    for line_no, platform, rom_filename, family, row_version, directory in rows:
        if directory not in changed_dirs:
            continue

        latest = latest_version_on_disk(directory, family)
        if latest is not None:
            row_norm, latest_norm = normalize(row_version, latest)
            if row_norm < latest_norm:
                failures.append(
                    f"docs/variants/overview.md:{line_no}: row '{platform}' "
                    f"references {rom_filename} "
                    f"(v{'.'.join(map(str, row_version))}), but "
                    f"{directory.relative_to(REPO_ROOT)} now has an openness "
                    f"score for v{'.'.join(map(str, latest))}."
                )

        claimed = claimed_families_by_dir.get(directory, set())
        other = newest_other_family(directory, family, row_version, claimed)
        if other is not None:
            other_family, other_version = other
            other_filename = other_family.replace(
                "_v{VER}", "_v" + ".".join(map(str, other_version))
            )
            failures.append(
                f"docs/variants/overview.md:{line_no}: row '{platform}' "
                f"references {rom_filename} "
                f"(v{'.'.join(map(str, row_version))}), but "
                f"{directory.relative_to(REPO_ROOT)} now has a newer "
                f"openness score under {other_filename}."
            )

    if failures:
        print("Openness comparison table (docs/variants/overview.md) is out of date:\n")
        for failure in failures:
            print(f" - {failure}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
