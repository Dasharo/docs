# Dasharo firmware building guide

## Intro

This guide shows how to build Dasharo firmware compatible with Gigabyte
MZ33-AR1.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
    + `sudo apt-get install git`

## Building

To build Dasharo (coreboot+UEFI) firmware image, first clone the coreboot
repository:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

then follow the steps below:

1. To build a specific version checkout to the version's tag.
    Skip this step otherwise.

    ```bash
    cd coreboot
    git checkout gigabyte_mz33_ar1_<version>
    ```

    For example

    ```bash
    git checkout gigabyte_mz33_ar1_v0.9.0
    ```

2. Checkout submodules:

    ```bash
    git submodule update --init --checkout
    ```

3. Download the package with necessary blobs and put it in proper directory:

{{ tos_checkbox("gigabyte-mz33-ar1-v090-blobs") }}

<div id="gigabyte-mz33-ar1-v090-blobs"
     class="tos-gate-content" markdown="1"
     style="display: none">

- Download the [blobs
package](https://dl.3mdeb.com/open-source-firmware/Dasharo/gigabyte_mz33_ar1/uefi/v0.9.0/Turin.zip).
- Then unzip it to the following directory:

    ```bash
    unzip Turin.zip -d 3rdparty/blobs/soc/amd/
    ```

</div>

Now build the firmware:

```bash
./build.sh mz33_ar1
```

The resulting coreboot image will be placed in the coreboot directory as
`gigabyte_mz33_ar1_<version>.rom` and `gigabyte_mz33_ar1_<version>.rbu`.
