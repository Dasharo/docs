# Building manual

## Intro

This documents describes the procedure for compiling Dasharo firmware
for QEMU Q35.

## Requirements

* `Ubuntu 20.04/21.04/22.04` as a host OS was tested
* Internet connection
* Docker installed
    - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
* Git, wget, unzip installed

Alternatively Fedora can be used instead of Ubuntu by following the same steps except:
[Install Docker Engine on Fedora](https://docs.docker.com/engine/install/fedora/)

```bash
sudo apt install git unzip wget
```

## Procedure

Obtain Dasharo source code:

> Replace the `REVISION` with one of the:
>
> * `qemu_q35_vVERSION` (e.g. `qemu_q35_v0.1.0`) for the given release
> * `qemu_q35_vVERSION-rcN` (e.g. `qemu_q35_v0.1.0-rc1`) for the given release
>   candidate

Clone Dasharo coreboot fork:

```bash
git clone https://github.com/Dasharo/coreboot.git -b REVISION --depth 1
```

Change directory:

```bash
cd coreboot
```

Compile:

```bash
./build.sh qemu
```

The resulting coreboot image will be placed in the current directory as
`qemu_q35_<version>.rom`.

> To build a QEMU image with all features and menus enabled, invoke:
>
> `./build.sh qemu_full`
>
> These builds are mainly for testing purposes and not all features have a
> working implementation under emulated environment.

## Initial Deployment

Now you can proceed with initial deployment scenario according to your needs:

* [Dasharo initial deployment](initial-deployment.md) if you want to use this
  image for manual testing or everyday use
* [Dasharo validation](https://github.com/Dasharo/open-source-firmware-validation#qemu-workflow)
  if you want to use binaries for validation purposes
