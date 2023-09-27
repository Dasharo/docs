# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device. The currently installed
firmware version can be checked with the following command in a Linux
environment:

```bash
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

## Prerequisites

Depending on firmware version (1) there may be manual steps required to ensure
that the firmware can be updated.
{ .annotate }

1. v1.5.0 for TGL-U models and v1.7.0 for ADL-P introduced support for Firmware
   Update Mode

### Firmware Update Mode

If the currently installed Dasharo version supports Firmware Update Mode, follow
the steps outlined in
[generic Firmware Update documentation](../../guides/firmware-update.md#firmware-update-mode).

### Manual

Ensure that the firmware protections are disabled in
[Dasharo Security Options](../../dasharo-menu-docs/dasharo-system-features.md).
Both `BIOS boot medium lock` and `Enable SMM BIOS write protection` should
be unchecked. [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration)
must be disabled as well (uncheck `Attempt Secure Boot` if
`Current Secure Boot State` does not say `Disabled`). To apply changes you
will need to reboot.

### Update using Dasharo Tools Suite

* Boot into
  [Dasharo Tools Suite](/dasharo-tools-suite/documentation/#running)

* Follow the procedure described in [DTS firmware update documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation/#firmware-update)
