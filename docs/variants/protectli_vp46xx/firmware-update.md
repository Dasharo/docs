# Firmware update

Following documentation describes the  process of Dasharo open-source firmware
update.

The process may be different, depending on the currently installed Dasharo
firmware version.

For simplicity we recommend using
[Dasharo Tools Suite](../../../common-coreboot-docs/dasharo_tools_suite).

## Updating to Dasharo v1.0.18 or v1.0.19

From v1.0.18 Dasharo firmware is rebased on the more up-to-date revision of
coreboot.

If the current version of the firmware on the device is older than v1.0.18 the
whole flash chip should be flashed as described in
[Initial Deployment](initial-deployment.md).

If the current version of the firmware on the device is v1.0.18 and it should
be updated to v1.0.19, only the `WP_RO` and `RW_SECTION_A` should be flashed.
To do this the following command should be used:

```bash
flashrom -p internal -w protectli_vault_cml_v1.0.19.rom --fmap -i WP_RO -i RW_SECTION_A
```

## Updating on Dasharo v1.0.16 or v1.0.17

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
