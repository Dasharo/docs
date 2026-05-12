# Firmware update

**Please read the [overview page](overview.md) first!**

Following documentation describe process of Dasharo open-source firmware
distribution update.

## Prerequisites

Your firmware version can be checked by entering the
[Dasharo Setup Menu](../../dasharo-menu-docs/overview.md#dasharo-menu-guides)
using the ++DEL++ key while booting.

### Capsule Update via fwupd

Using fwupd is the recommended and simplest way to perform Dasharo
firmware updates on supported devices.

```sh
sudo fwupdtool install-blob gigabyte_mz33_ar1_v0.9.x.cap
```

Once asked which firmware to update from a list of options, choose the option
with `System Firmware` and proceed. Then `fwupdtool` will ask you to reboot
the system to perform an update.

After the initial reboot, the firmware will reset itself once to disable all
locks that would prevent the update. After the reset you shall be greeted with
a firmware update screen, asking you to not power off the computer.

!!! note "Note"

    Capsule updates via `/dev/efi_capsule_loader` on Linux are not supported
    because capsules can not survive resets see [issue](TBD). Only Capsule on
    Disk is supported.

### Updating via BMC

Use the same procedure as in [Flashing via BMC in Recovery
section](recovery.md#flashing-via-bmc).

!!! note "Note"

    This method flashes whole chip and will wipe out all firmware variables
    and settings.

### Manual update

This update method is for advanced users only and is not recommended for
regular end users.

```sh
sudo flashrom -p internal -w gigabyte_mz33_ar1_v0.9.x.rom --fmap -i COREBOOT -N
```

!!! note "Note"

    The SMM BIOS Write protection has to be disabled
