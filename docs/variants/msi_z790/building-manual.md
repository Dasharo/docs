# Building manual

## Intro

This documents describes the procedure for compiling Dasharo firmware
compatible with MSI PRO Z790-P WIFI DDR4.

## Requirements

* `Ubuntu 20.04/21.04/22.04` as a host OS was tested
* Internet connection
* Docker installed
    - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
* Git, wget, unzip installed

```bash
sudo apt install git unzip wget
```

* UEFIExtract installed
    - this tool is used in the `build.sh` script to extract CPU microcode from
      the original MSI firmware

```bash
sudo apt install wget
wget https://github.com/LongSoft/UEFITool/releases/download/A59/UEFIExtract_NE_A59_linux_x86_64.zip
unzip UEFIExtract_NE_A59_linux_x86_64.zip
sudo cp ./UEFIExtract /usr/local/bin
```

## Procedure

Obtain Dasharo source code for MSI PRO Z790-P:

> Replace the `REVISION` with one of the:
>
> * `msi_ms7d25/release` for the latest released version
> * `msi_ms7e06_vVERSION` (e.g. `msi_ms7e06_v0.9.0`) for the given release

```bash
git clone https://github.com/Dasharo/coreboot.git -b REVISION
```

Navigate to the source code directory and start the build process:

* DDR4 variant

```bash
cd coreboot
./build.sh z790_ddr4
```

* DDR5 variant

```bash
cd coreboot
./build.sh z790_ddr5
```

The resulting Dasharo firmware image will be placed at `build/coreboot.rom`.
