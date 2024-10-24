# Firmware transition

## Introduction

This document describes the process of transitioning from Dasharo UEFI to Heads
and the other way around.

## Transition from Dasharo UEFI to Heads variant

**Recommended**

Please use [Dasharo Tools Suite](../../dasharo-tools-suite/overview.md) with
Heads subscription credentials to transition to Heads.

**Manual**

Use [FlashBIOS](../../unified/msi/recovery.md#using-msi-flashbios-button)
method (recommended) or flash with flashrom in OS. To use FlashBIOS we
recommend to switch back to MSI UEFI firmware (if you don't have the desktop
Dasharo Pro Package or not running Dasharo v1.1.3) and then use
FlashBIOS with heads binary.

To transition to heads firmware with flashrom, whole binary has to be flashed:

```bash
flashrom -p internal -w <heads_fw_file>
```

!!! warning

    ME has to be disabled and descriptor unlocked to flash full file. MSI
    firmware began to ship the platforms with ME and flash descriptor regions
    read-only. Unlocking the descriptor is possible using Firmware Update Mode
    on Dasharo v0.9.1.

## Transition from Dasharo Heads back to UEFI

At the moment, Dasharo Tools Suite does not support switching from Heads back to
UEFI-based firmware. Use [FlashBIOS](../../unified/msi/recovery.md#using-msi-flashbios-button)
to restore a saved backup, stock, or Dasharo UEFI firmware.

!!! warning "Warning for Qubes OS users"

    If you installed Qubes OS under Heads, it has been installed in legacy BIOS
    boot mode and will not be bootable under UEFI. You will likely need to
    install Qubes OS again.

    Users who installed Qubes OS *before* switching to Heads are not affected.
