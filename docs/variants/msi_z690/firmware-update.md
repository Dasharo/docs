# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update.

## Updating Dasharo

If Dasharo is already installed on the device, the whole `bios` region must be
updated.

```bash
flashrom -p internal -w [path] --ifd -i bios
```
