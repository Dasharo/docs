# Standardized firmware update changelog titles

When a variant's `releases.md` gains one of the firmware update features
tracked in [`docs/guides/firmware-update-method-support-table.csv`](../docs/guides/firmware-update-method-support-table.csv),
announce it under that version's `### Added` section using one of these
exact bracketed titles:

- `Firmware Update Mode`
- `Capsule Update V1`
- `FWUPD support`
- `LVFS support`
- `Capsule Update V2`

Example:

```markdown
### Added

- [Capsule Update V1](https://docs.dasharo.com/kb/capsule-updates-overview/)
- [FWUPD support](https://docs.dasharo.com/kb/fwupd/)
```

Any other wording (e.g. "Firmware update mode", "UEFI Capsule Update
support") won't be picked up.

`generate_firmware_update_support_table.py` scans every
`docs/variants/*/releases.md` for these exact titles and regenerates the CSV
from them. It runs as a pre-commit hook, so committing a changelog change
with one of these bullets will automatically update the support table.

# Openness score freshness check

`check_openness_score_freshness.py` cross-checks the "Openness comparison"
table in [`docs/variants/overview.md`](../docs/variants/overview.md)
against the `*_openness_chart.png` files under `docs/variants/*/`. It runs
as a pre-commit hook when a commit touches a chart PNG.

It fails the commit when, for a row whose directory was touched:

- the row's own chart filename pattern (e.g.
  `msi_ms7d25_v{VER}_ddr5.rom`) has a newer version on disk than the row
  references, or
- some _other_ filename pattern in the same directory has a newer chart,
  and no row in the table tracks that other pattern either.

Whenever you add a new openness score chart, update the matching row in
`overview.md` in the same commit.
