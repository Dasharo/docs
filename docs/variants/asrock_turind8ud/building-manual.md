# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware compatible with ASRock Rack
TURIND8UD-2T/X550.

Two firmware variants are available:

- coreboot+LinuxBoot: coreboot with LinuxBoot payload and u-root userland.
  Does not feature a setup menu. Compatible with Linux-based operating systems.
- coreboot+UEFI: coreboot with TianoCore EDK II as the payload. Exposes a
  standard UEFI boot loader and setup menu. Can boot UEFI-compatible OSes.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build a Dasharo firmware image, first clone the coreboot repository:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    === "LinuxBoot"

        ```bash
        cd coreboot
        git checkout asrock_turind8ud_linuxboot_<version>
        ```

        For example

        ```bash
        git checkout asrock_turind8ud_linuxboot_v0.9.0
        ```

    === "UEFI"

        ```bash
        cd coreboot
        git checkout asrock_turind8ud_uefi_<version>
        ```

        For example

        ```bash
        git checkout asrock_turind8ud_uefi_v0.9.0
        ```

2. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

3. Download the package with necessary blobs and put it in proper directory:

{{ tos_gated_downloads("gigabyte-mz33-ar1-v090-blobs",
  [{"label": "Turin.zip", "url": "https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/Turin.zip"}],
  prose_section_id="gigabyte-mz33-ar1-v090-blobs-prose") }}

<div data-prose-group="gigabyte-mz33-ar1-v090-blobs-prose"
     class="tos-gate-content" markdown="1"
     style="display: none">

- Unzip the package to the following directory:

    ```bash
    unzip Turin.zip -d 3rdparty/blobs/soc/amd/
    ```

</div>

Now build the firmware:

=== "LinuxBoot"

    ```bash
    ./build.sh asrock_turind8ud_linuxboot
    ```

    The resulting coreboot image will be placed in the coreboot directory as
    `asrock_turind8ud_linuxboot_<version>.rom`.

=== "UEFI"

    ```bash
    ./build.sh asrock_turind8ud_uefi
    ```

    The resulting coreboot image will be placed in the coreboot directory as
    `asrock_turind8ud_uefi_<version>.rom`.
