# Firmware update

Following documentation describes the  process of Dasharo open-source firmware
update.

The process may be different, depending on the currently installed Dasharo
firmware version.

## Updating on Dasharo v1.0.16 or newer

Only the `RW_SECTION_A` partition of the flash needs to be updated. Flash it
using the following command:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.16.rom --fmap -i RW_SECTION_A
```

This command also preserves Dasharo UEFI settings and the boot order.

## Updating on older Dasharo versions

In this case, the whole `bios` region must be updated.

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.13.rom --ifd -i bios
```
