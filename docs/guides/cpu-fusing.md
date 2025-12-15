# Dasharo TrustRoot - Fusing vendor keys to the CPU

In order to take use of the Dasharo TrustRoot feature on supported Devices,
the device vendor key hashes need to be physically burned into the SoC.

This document describes the steps for fusing vendor keys into your device.
For more details check [Glossary / Dasharo TrustRoot](../glossary.md#dasharo-trustroot)

!!! warning

    Fusing device vendor keys is a feature targeted for advanced security
    freaks. This operation permanently modifies your CPU. Reverting it
    is only possible by replacing the CPU in the device.
    Fusing vendor keys onto your CPU makes it impossible to:
    - Use custom firmware not authorized by the vendor
    - Update the firmware to a custom one if the support for your device ends

    Be careful and make sure you understand the consequences before
    proceeding with fusing your device.

## Fusing the device vendor keys using Dasharo Tools Suite

It's the recommended way of fusing your device. For details refer
to [Dasharo Tools Suite documentation](../dasharo-tools-suite/documentation/features.md#fuse-platform)

## Fusing the device using an EOM capsule (ADVANCED!)

!!! warning

    This method does not include any confirmations and guards from fusing the
    device by a mistake. It is __NOT RECOMMENDED__ to perform the fusing
    using a manual capsule update described here. Please consider doing it
    [using DTS](#fusing-the-device-vendor-keys-using-dasharo-tools-suite)
    instead.

1. Locate the EOM capsule file of the desired Dasharo version. EOM firmware is
   marked with `.eom` suffix, like `novacustom_v56x_mtl_igpu_v1.0.0_btg_provisioned.cap.eom`.
   Make sure the firmware version is equal or higher than the currently used.
2. Boot Dasharo Tools Suite. On how to, refer to [Running DTS](../dasharo-tools-suite/documentation/running.md)
3. Enter the shell by pressing the `S` key as instructed in the main screen.
4. Get the capsule file onto the running DTS by any means: `wget`, `scp` etc.
5. Run `cat <your_eom_capsule_file> > /dev/efi_capsule_loader` to load the capsule.
6. Reboot the device to perform the capsule update and fuse the device in the process.
