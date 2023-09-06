# Firmware update

## Introduction

This document describes the process for updating firmware on devices running
Dasharo firmware. Some steps specific to each device will be described in their
respective documentation, but the generic process outlined here will apply to
all devices.

## Firmware Update Mode

For enhanced firmware security, Dasharo uses a number of security mechanisms to
prevent overwriting firmware. Depending on device, these may be some or all of
the following:

- SPI flash write-protection - prevents overwriting the initial bootblock and
  Verified Boot code
- SMM BIOS write protection - prevents all writes to BIOS flash memory outside
  of privileged code running in System Management Mode
- UEFI Secure Boot - in combination with Linux Kernel Lockdown, prevents direct
  access to the SPI flash controller from the OS

If you are interested, see the
[Dasharo System Features](../dasharo-menu-docs/dasharo-system-features.md)
section for more details.

To allow updating firmware by the end user, these protections must be disabled
first. To facilitate this, Dasharo has a Firmware Update Mode option that
**temporarily** disables firmware security measures for the duration of one
boot.

To enter Firmware Update Mode:

1. Enter the Setup Menu:
![](./images/setup_menu_dsf.png)
1. Navigate to `Dasharo System Features`:
![](./images/setup_menu_dsc.png)
1. Navigate to `Dasharo Security Options`:
![](./images/setup_menu_lbm.png)
1. Select the `Enter Firmware Update Mode` option:
![](./images/setup_menu_fum.png)
1. When prompted, press Enter to accept. The device will reboot in Firmware
  Update Mode.
1. After reboot, when prompted, press the indicated key on the keyboard.
  Alternatively, to abort Firmware Update Mode, press Enter instead or simply
  wait for the timeout to expire.

Once in Firmware Update Mode, proceed with the firmware update steps outlined
in device-specific documentation.

## Firmware Update Mode flowchart

```mermaid
flowchart TD
    power_on[Power on] --> setup
    subgraph setup [Setup UI]
    setup1[Enter Dasharo Setup]
    setup2[Go to Dasharo System Features]
    setup3[Go to Dasharo Security Options]
    setup4[Choose Firmware Update Mode]
    setup5[Press ENTER to continue]
    setup1 --> setup2 --> setup3 --> setup4 --> setup5
    end
    setup --> reboot[Reboot]
    reboot --> coreboot
    subgraph coreboot
    cb1{{Firmware Update Mode EFI variable found and set?}}
    cb1 -- False --> cb2[Enable firmware lockdown]
    cb1 -- True --> cb3[Skip firmware lockdown]
    cb2 --> cb4{{Boot payload}}
    cb3 --> cb4
    end

    coreboot --> securitypkg
    subgraph securitypkg [SecurityPkg]
    sec1{{Firmware Update Mode EFI variable found and set?}}
    sec1 -- False --> sec2[Enable Secure Boot]
    sec1 -- True --> sec3[Skip enabling Secure Boot]
    sec2 --> sec4[Continue booting]
    sec3 --> sec4
    end

    securitypkg --> bootmanager
    subgraph bootmanager [PlatformBootManagerLib]
    bm1{{Firmware Update Mode EFI variable found and set?}}
    bm1 -- True --> bm3[Remove Firmware Update Mode EFI variable]
    bm3 --> bm4[Display Firmware Update Mode warning dialog]
    bm4 --> bm5[Confirm user presence]
    bm5 --> bm6{{User presence confirmed?}}
    bm5 -- True --> bm7[Boot to OS]
    bm6 -- False --> bm8[Reboot]
    bm1 -- False --> bm7
    end
```
