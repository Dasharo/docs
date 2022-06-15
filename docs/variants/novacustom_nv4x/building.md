# coreboot building

## Intro

This documents describes the procedure for compiling coreboot for NovaCustom NV4X.

## Requirements

- Docker
    + follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    + follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
- Git

## Procedure

The easiest way to build coreboot is to use the official Docker image.

Obtain the image:

```bash
docker pull coreboot/coreboot-sdk:0ad5fbd48d
```

Obtain coreboot source code for NovaCustom NV4X:

```bash
git clone https://github.com/Dasharo/coreboot.git
```

Navigate to the source code directory and checkout to the desired revision:

> Replace the REVISION with one of the:
> - `novacustom_nv4x/release` for the latest released version
> - `novacustom_nv4x/vVERSION` (e.g. `v1.0.1`) for the given release

```bash
cd coreboot
git checkout REVISION
git submodule update --init --recursive --checkout
```

Enter the Docker container:

```bash
docker run -u $UID --rm -it -v $PWD:/home/coreboot/coreboot -w /home/coreboot/coreboot \
    coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
```

_Warning: Do not run `docker` as root. This command should be executed as your
current user. If you're having trouble running `docker` on your user account,
follow the steps outlined in [Requirements](#requirements)._

You should be inside the Docker container. Now run following script to build
the image:

```bash
./build.sh build
```

The resulting coreboot image will be placed in

`artifacts/dasharo_novacustom_nv4x_VERSION.rom`

or:

`artifacts/dasharo_clevo_nv41mz_VERSION.rom`.

for versions before v1.2.0.
