# coreboot vboot signing

## Introduction

Verified Boot is a method of verifying that the firmware compents haven't been
tampered with. It uses cryptographic signatures to determine whether the
firmware comes from trusted source. This document covers the procedure for
generating vboot keys and configuring the coreboot build system to sign the
binaries with the generated keys.

## Prerequisites

1. Clone `Dasharo/coreboot` repository and checkout on corresponding `release`
   branch for your platform (please refer to the `Building manual` section):

    ```bash
    git clone https://github.com/Dasharo/coreboot.git
    cd coreboot
    git checkout <board_vendor>_<board_model>/release
    ```

2. Ensure submodules are up to date:

    ```bash
    git submodule update --init --checkout
    ```

3. Install the required libraries:

    ```bash
    sudo apt install libflashrom-dev libssl-dev uuid-dev
    ```

4. Build vboot environment and install it on the host system:

    ```bash
    make -C 3rdparty/vboot
    sudo make -C 3rdparty/vboot install
    ```

## Generating keys

Generate the keys with the following command:

```bash
./3rdparty/vboot/scripts/keygeneration/create_new_keys.sh --output keys/
```

The keys will be created in the directory `$PWD/keys`, i.e. in the coreboot
root directory in the `keys` subdirectory.

If in doubt what parameters you should pass, add `--help` as a parameter to the
script.

## Signing image without rebuilding

> This is the default procedure that should be followed by users downloading
> firmware from the `Release` section, who want to use their own keys for
> vboot.

Be sure you have generated the keys as in [Generate keys](#generating-keys)
section. Assuming you have generated keys to the `keys/` directory:

```bash
./3rdparty/vboot/scripts/image_signing/sign_firmware.sh \
  <released_firmware_file> \
  keys/ \
  dasharo_resigned.rom
```

If in doubt what parameters you should pass, add `--help` as a parameter to the
script.

The successful output should look like this:

```txt
...
 - import root_key from keys//root_key.vbpubk: success
 - import recovery_key from keys//recovery_key.vbpubk: success
successfully saved new image to: dasharo_resigned.rom
```

Now the image will be signed with your own keys. Be sure to save the keys in a
safe location, because you will need them to sign each firmware update.
Otherwise, the firmware updates to RW partitions will not be executed by vboot.

## Adding keys to the coreboot config

> This procedure is only meant for developers or when you are rebuilding
> firmware by yourself.

In the root of the coreboot tree, execute the following command:

```bash
make nconfig
```

Navigate to `Security` -> `Verified Boot (vboot)` -> `Vboot keys` and enter the
paths to the keys in the appropriate fields.

Exit `nconfig` by pressing `Esc` repeatedly and pressing `Enter` when prompted
to save the configuration.

Now, rebuild coreboot with this config to generate images signed with the chosen
vboot keys.
