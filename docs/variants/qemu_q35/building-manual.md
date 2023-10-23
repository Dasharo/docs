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

Clone Dasharo EDK II fork:

```bash
git clone https://github.com/Dasharo/edk2.git -b REVISION
```

Clone Dasharo EDK II Platforms fork:

```bash
git clone https://github.com/Dasharo/edk2-platforms.git -b REVISION
```

Initialize submodules:

```bash
cd edk2
```

Update the submodules in order get latest dependencies.

```bash
git submodule update --init --checkout --recursive
```

Obtain the docker image:

```bash
docker pull coreboot/coreboot-sdk:2021-09-23_b0d87f753c
```

Start the instance of the docker image under the Dasharo/edk2 repository:

```bash
docker run --rm -it -v $PWD:/home/coreboot/edk2 \
    -v $PWD/../edk2-platforms:/home/coreboot/edk2-platforms \
    -w /home/coreboot/edk2 coreboot/coreboot-sdk:2021-09-23_b0d87f753c \
    /bin/bash
```

Setup the environment variables with the following command

```bash
source edksetup.sh
```

Compile EDK II base tools:

```bash
make -C BaseTools
```

Update the PACKAGES_PATH variable

```bash
export EDK2_PLATFORMS_PATH="$HOME/edk2-platforms"
export PACKAGES_PATH="$WORKSPACE:\
$EDK2_PLATFORMS_PATH/Platform/Intel:\
$EDK2_PLATFORMS_PATH/Silicon/Intel:\
$EDK2_PLATFORMS_PATH/Features/Intel:\
$EDK2_PLATFORMS_PATH/Features/Intel/Debugging:\
$EDK2_PLATFORMS_PATH/Features/Intel/Network:\
$EDK2_PLATFORMS_PATH/Features/Intel/OutOfBandManagement:\
$EDK2_PLATFORMS_PATH/Features/Intel/PowerManagement:\
$EDK2_PLATFORMS_PATH/Features/Intel/SystemInformation:\
$EDK2_PLATFORMS_PATH/Features/Intel/UserInterface"
```

To build the image simply invoke the following command

```bash
build -a IA32 -a X64 -t GCC5 -b RELEASE -p OvmfPkg/OvmfPkgX64.dsc
```

Once the build is completed you should see output as follows:

```text
GUID cross reference file can be found at /home/coreboot/edk2/Build/OvmfX64/RELEASE_GCC5/FV/Guid.xref

FV Space Information
SECFV [5%Full] 212992 total, 11568 used, 201424 free
PEIFV [15%Full] 917504 total, 139640 used, 777864 free
DXEFV [46%Full] 12582912 total, 5849680 used, 6733232 free
FVMAIN_COMPACT [41%Full] 3440640 total, 1430512 used, 2010128 free

- Done -
  Build end time: 21:52:36, Oct.22 2023
  Build total time: 00:01:41
```

The Dasharo firmware image can be found below given path:

```bash
/home/coreboot/edk2/Build/OvmfX64/RELEASE_GCC5/FV/OVMF_CODE.fd
/home/coreboot/edk2/Build/OvmfX64/RELEASE_GCC5/FV/OVMF_VARS.fd
```

## Initial Deployment

Now you can proceed with initial deployment scenario according to you needs:

* Dasharo validation - if you want to use binaries for validation purposes.
* [Dasharo development](../development) - if you want to use binaries in development environment
