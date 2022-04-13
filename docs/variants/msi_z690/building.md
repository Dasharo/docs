# coreboot building

## Intro

This documents describes the procedure for compiling coreboot for MSI PRO Z690-A WIFI DDR4.

## Requirements

- Docker
  + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Procedure

Download and install UEFIExtract

```
sudo apt install wget
wget https://github.com/LongSoft/UEFITool/releases/download/A59/UEFIExtract_NE_A59_linux_x86_64.zip
unzip UEFIExtract_NE_A59_linux_x86_64.zip
cp ./UEFIExtract /usr/bin
```

Obtain coreboot source code for MSI PRO Z690-A WIFI DDR4:

```bash
git clone https://github.com/Dasharo/coreboot.git -b msi_ms7d25/rel_v0.1.0
```

Navigate to the source code directory and checkout to the desired revision:

```bash
$ git clone https://github.com/Dasharo/coreboot.git
```
Navigate to the source code directory and checkout to the desired revision:

> Replace the REVISION with one of the:
> - `msi_ms7d25/release` for the latest released version
> - `msi_ms7d25/rel_vVERSION` (e.g. `rel_v0.1.0`) for the given release

```bash
$ cd coreboot
$ git checkout REVISION
$ git submodule update --init --recursive --checkout
```

```bash
$ ./build.sh build
```
The resulting coreboot image will be placed in
`artifacts/dasharo_clevo_nv41mz_VERSION.rom`.
