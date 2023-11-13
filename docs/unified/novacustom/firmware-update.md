# Firmware update

The following documentation describes the process of Dasharo open-source
firmware update. The update process may be different, depending on which
firmware version is currently installed on your device.

You can check your current firmware version with the following Linux command.

```bash
sudo dmidecode -t bios | grep Version
```

Alternatively, it can be checked in the `BIOS Setup Menu`.

## Prerequisites

First, determine your device version with the following Linux command.

```bash
sudo dmidecode -t system | grep "Product Name"
```
Alternatively, this can be checked in the `BIOS Setup Menu` as well.

Note the `Device name` based on the previous output and the following table.

| Product Name output |  Device name  |
|---------------------|---------------|
| NV4XMB,ME,MZ        | NV4x-TGL      |
| NS50_70MU           | NS5x-TGL      |
| NV41PZ              | NV4x-ADL      |
| NS50_70PU           | NS5x-ADL      |

Depending on the firmware version, there may be manual steps required to ensure that the firmware can be updated. `-TGL` devices starting from version v1.5.0 and `-ADL` devices starting from version v1.7.0 have support for [Firmware Update Mode](#firmware-update-mode). For older versions, please continue with the [Updating older versions](#updating-older-versions) section.

> Advanced users can also [build](../building-manual.md) and/or flash the binaries themselves by following the steps under the [Manual update](#manual-update) section.

### Firmware Update Mode

If the currently installed Dasharo version supports Firmware Update Mode, follow
the steps outlined in
[generic Firmware Update documentation](../../guides/firmware-update.md#firmware-update-mode).

Check out our [YouTube video](https://www.youtube.com/watch?v=muWjhrQ7bQk) for a demonstration of Firmware Update Mode.

### Updating older versions

First, ensure that [UEFI Secure Boot](../../dasharo-tools-suite/documentation.md#disabling-secure-boot) has been disabled.

Boot to the [Dasharo Tools Suite](../../dasharo-tools-suite/documentation.md#bootable-over-a-network). We recommend the network boot option.

In the main menu of Dasharo Tools Suite, select option `5` to proceed with the installation of the firmware update.

In case you want to know more about the firmware update option in Dasharo Tools Suite, please check out the [features section](../../dasharo-tools-suite/documentation.md#firmware-update) of the dedicated Dasharo Tools Suite documentation page.

### Manual update

This update method is for advanced users only and is not recommended for regular end users.

Ensure that the firmware protections are disabled (1) in
[Dasharo Security Options](../../dasharo-menu-docs/dasharo-system-features.md).
Both `BIOS boot medium lock` and `Enable SMM BIOS write protection` should
be unchecked. [UEFI Secure Boot](../../dasharo-menu-docs/device-manager.md#secure-boot-configuration)
must be disabled as well (uncheck `Attempt Secure Boot` if
`Current Secure Boot State` does not say `Disabled`). To apply changes, you
will need to reboot.
{ .annotate }
1. These options were introduced in v1.5.0 for TGL models and v1.7.0 for ADL models. You can skip these steps if you are using an older firmware version.

* Follow the manual update procedure described in [DTS firmware update documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation/#local-firmware-update).

> Please make sure you that you update the BIOS firmware and the EC firmware respectively.
