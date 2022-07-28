# Recovery

---

## **Prequisitions**

To proceed with recovery `.rom` file with backup vendor firmware will be
neccesary eg. `backup.rom`.

Backup file should be generated before making any changes in device flash
chip according to documentation in
[Reading flash contents](initial-deployment.md#reading-flash-contents)
section.

---

## **Internal flashing**

If platform is booting properly it's possible to recover vendor firmware using
procedure described in
[Flashing Dasharo](initial-deployment.md#flashing-dasharo) section, setting path
to `backup.rom` with vendor firmware as `[path]` argument.
