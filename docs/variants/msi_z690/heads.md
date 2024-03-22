# Dasharo (coreboot + Heads) firmware variant

Heads-based variant of Dasharo firmware compatible with MSI PRO Z690-A boards
is offered as a Technology Preview Release.

Please consider to support the project financially by purchasing the
`Dasharo Heads Subscription for Desktop`.
With this subscription, you will get access to the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant)
feature in Dasharo Tools Suite and support from Dasharo directly via Matrix.
The subscription is not automatically renewed.

## Releases

Following Release Notes describe status of Dasharo (coreboot + Heads) firmware
development compatible with MSI PRO Z690-A boards.

## v0.9.0 - 2024-03-21

Test results for this release can be found
[here](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=5649308).

### Added

- [Dual TPM feature in coreboot. When ME is disabled, fTPM becomes inactive as well and chipset will route the TPM traffic to SPI bus. coreboot will now probe for all possible TPMs and initialize the one that is currently active.](https://github.com/Dasharo/dasharo-issues/issues/113)

### Changed

- [This is a Dasharo Entry Subscription release](https://docs.dasharo.com/dev-proc/versioning/#dasharo-entry-subscription-releases)
- Heads Linux is used as a payload
- [Updated Flash Descriptor to enlarge BIOS region; refer to SBOM section below](https://github.com/Dasharo/dasharo-blobs/tree/main/msi/ms7e06)
- ME hardcoded to be HAP disabled for heads builds. Discrete SPI TPM in JTPM1
  header is required to provide TPM functionality.

### Known issues

- [Cannot wake from suspend via RTC on QubesOS](https://github.com/Dasharo/dasharo-issues/issues/484)
- [Builds are not fully reproducible](https://github.com/linuxboot/heads/issues/1616)

### Binaries

[sha256][msi_ms7d25_v0.9.0_ddr4_heads.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v0.9.0_ddr4_heads.rom_sig]{.md-button}

[sha256][msi_ms7d25_v0.9.0_ddr5_heads.rom_hash]{.md-button}
[sha256.sig][msi_ms7d25_v0.9.0_ddr5_heads.rom_sig]{.md-button}

This is a Dasharo Entry Subscription Release. To obtain access to the pre-built
binaries you will have to
[become the Dasharo Entry Subscription subscriber](../../ways-you-can-help-us.md#become-a-dasharo-entry-subscription-subscriber).
You will get the access to all of the firmware updates for the duration of the
subscription via Dasharo Entry Subscription newsletter.

To verify binary integrity with hash and signature please follow the
instructions in [Dasharo release signature verification](/guides/signature-verification)
using [this key](https://raw.githubusercontent.com/3mdeb/3mdeb-secpack/master/dasharo/msi_ms7d25/dasharo-release-0.x-compatible-with-msi-ms-7d25-signing-key.asc)

### SBOM (Software Bill of Materials)

- [Dasharo heads fork based on v0.2.0 revision 13aa08ce](https://github.com/Dasharo/heads/tree/13aa08ce)
- [Dasharo coreboot fork based on 4.21 revision 38215f5a](https://github.com/Dasharo/coreboot/tree/38215f5a)
- [Intel Management Engine based on v16.1.30.2307 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/msi/ms7d25/me.bin)
- [Intel Flash Descriptor based on v1.2 revision d0b63476](https://github.com/Dasharo/dasharo-blobs/blob/d0b63476/msi/ms7d25/descriptor.bin)
- [Intel Firmware Support Package based on RPL-S C.0.BD.40 revision 481ea7cf](https://github.com/intel/FSP/tree/481ea7cf/RaptorLakeFspBinPkg/Client/RaptorLakeS)
- [Intel microcode based on ADL/RPL C0/H0 0x0000002e revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-97-05)
- [Intel microcode based on RPL B0 0x00000119 revision microcode-20230808](https://github.com/intel/Intel-Linux-Processor-Microcode-Data-Files/tree/microcode-20230808/intel-ucode/06-b7-01)

[newsletter]: https://newsletter.3mdeb.com/subscription/D7dQvGx6k
[msi_ms7d25_v0.9.0_ddr4_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/heads/v0.9.0/msi_ms7d25_v0.9.0_ddr4_heads.rom.sha256
[msi_ms7d25_v0.9.0_ddr4_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/heads/v0.9.0/msi_ms7d25_v0.9.0_ddr4_heads.rom.sha256.sig
[msi_ms7d25_v0.9.0_ddr5_heads.rom_hash]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/heads/v0.9.0/msi_ms7d25_v0.9.0_ddr5_heads.rom.sha256
[msi_ms7d25_v0.9.0_ddr5_heads.rom_sig]: https://dl.3mdeb.com/open-source-firmware/Dasharo/msi_ms7d25/heads/v0.9.0/msi_ms7d25_v0.9.0_ddr5_heads.rom.sha256.sig

## Hardware Configuration Matrix

Generally, the same [hardware configuration](hardware-matrix.md) as for the
UEFI variant applies.

A notable addition is usage of the
[Nitrokey 3A Mini](https://shop.nitrokey.com/shop/nk3am-nitrokey-3a-mini-149)
USB device, which is required for Heads installation and usage.

## Test Matrix

Please refer to the [tests results spreadsheet](https://docs.google.com/spreadsheets/d/1yWZ--zFPIsQhXZByf7nJIrasQYuRSf1yCi60lY_RGsQ/edit#gid=5649308).

## Building manual

This section presents the crucial steps required to build the Dasharo Heads
firmware. For more information, you may also refer to the official
[Heads building documentation](https://osresearch.net/general-building/).

### Requirements

This guide was verified on Ubuntu 22.04. In practice, any Linux distribution
with [Docker](https://www.docker.com/) support should be enough to complete it.

Make sure that you have following packages installed:

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

    ```bash
    sudo apt -y install git
    ```

### Building

1. Clone Dasharo Heads repository

    ```bash
     git clone https://github.com/Dasharo/heads.git
    ```

2. Navigate to the source code directory and checkout to the desired revision:

    ```bash
    cd heads
    git checkout msi_ms7d25_v0.9.0
    ```

3. Start docker container:

    ```bash
    docker run --rm -it -v $PWD:$PWD -w $PWD \
      3mdeb/heads-docker:3.0.0 /bin/bash
    ```

4. Inside of the container, start the build process:

=== "PRO Z690-A (WIFI) DDR4"

    ```bash
    BOARD=msi_z690a_ddr4 make
    ```

    This will produce a Dasharo binary placed in
    `build/x86/msi_z690a_ddr4/dasharo-msi_z690a_ddr4-*.rom`.

=== "PRO Z690-A (WIFI)"

    ```bash
    BOARD=msi_z690a_ddr5 make
    ```

    This will produce a Dasharo binary placed in
    `build/x86/msi_z690a_ddr5/dasharo-msi_z690a_ddr5-*.rom`.

## Transition from Dasharo UEFI to Heads variant

**Recommended**

Please use [Dasharo Tools Suite](../../dasharo-tools-suite/overview.md) with
Heads subscription credentials to transition to Heads.

**Manual**

Use [FlashBIOS](../../unified/msi/recovery.md#using-msi-flashbios-button)
method (recommended) or flash with flashrom in OS. To use FlashBIOS we
recommend to switch back to MSI UEFI firmware (if you don't have the desktop
Dasharo Entry Subscription or not running Dasharo v1.1.3) and then use
FlashBIOS with heads binary.

To transition to heads firmware with flashrom, whole binary has to be flashed:

```bash
flashrom -p internal -w <heads_fw_file>
```

!!! warning "ME has to be disabled to flash full file."

## Transition from Dasharo Heads back to UEFI

At the moment, Dasharo Tools Suite does not support switching from Heads back to
UEFI-based firmware. Use [FlashBIOS](../../unified/msi/recovery.md#using-msi-flashbios-button)
to restore a saved backup, stock, or Dasharo UEFI firmware.

!!! warning "Warning for Qubes OS users"

    If you installed Qubes OS under Heads, it has been installed in legacy BIOS
    boot mode and will not be bootable under UEFI. You will likely need to
    install Qubes OS again.

    Users who installed Qubes OS *before* switching to Heads are not affected.

## Logo customization

To replace the logo, one must rebuild the firmware. Other methods are not
supported as of now. You would need to replace the
`branding/Dasharo/bootsplash.jpg` in the heads repository with your own, and
proceed with the [Building manual](#building-manual).

## Initial deployment

The supported method is to follow the
[initial deployment](/unified/msi/initial-deployment.md), and then the
[Transition from Dasharo UEFI to Heads variant](#transition-from-dasharo-uefi-to-heads-variant).

## Firmware update

[Build](#building-manual) or download Dasharo Heads firmware, and proceed with
the official [Heads update documentation](https://osresearch.net/Updating).
