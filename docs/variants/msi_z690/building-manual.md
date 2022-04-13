# coreboot building

## Intro

The document describes the procedure for compiling Dasharo compatible with MSI PRO Z690-A WIFI
DDR4.

## Requirements

- Docker
  + follow [Install Docker Engine](https://docs.docker.com/engine/install/)
  + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git
- network connection
- wget
- unzip

## Procedure

Download and install UEFIExtract

```
wget https://github.com/LongSoft/UEFITool/releases/download/A59/UEFIExtract_NE_A59_linux_x86_64.zip
unzip UEFIExtract_NE_A59_linux_x86_64.zip
sudo cp ./UEFIExtract /usr/bin
```

Obtain Dasharo source code compatible with MSI PRO Z690-A WIFI DDR4:

```bash
git clone https://github.com/Dasharo/coreboot.git -b msi_ms7d25/release
```

Navigate to the source code directory and checkout to the desired revision:

> Replace the REVISION with one of the:
> - `msi_ms7d25/release` for the latest released version
> - `msi_ms7d25/rel_vVERSION` (e.g. `rel_v0.1.0`) for the given release

```bash
$ cd coreboot
$ git checkout REVISION
```

```bash
$ ./build.sh
```
The resulting coreboot image will be placed in
`build/coreboot.rom`.
