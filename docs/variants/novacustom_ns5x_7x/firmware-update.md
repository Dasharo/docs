# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update.

## Update using flashrom

If Dasharo is currently installed, only the RW_SECTION_A partition of the flash
needs to be updated. Flash it using the following command:

```bash
flashrom -p internal -w [path] --fmap -i RW_SECTION_A
```

This command also preserves UEFI settings and the boot order.

## Update using fwupd

To update the firmware using fwupd follow
[this documentation](../../common-coreboot-docs/fwupd_usage.md).
