# coreboot vboot signing

## Introduction

Verified Boot is a method of verifying that the firmware compents haven't been
tampered with. It uses cryptographic signatures to determine whether the
firmware comes from trusted source. This document covers the procedure for
generating vboot keys and configuring the coreboot build system to sign the
binaries with the generated keys.

## Prerequisites

1. Navigate to the coreboot tree.
2. Ensure submodules are up to date:

    ```bash
    git submodule update --init --checkout
    ```

3. Install vboot libraries and modules on the host system:

    ```bash
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

## Adding keys to the coreboot config

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

## Signing image without rebuilding

Be sure you have generated the keys as in [Generate keys](#generating-keys)
section. Assuming you have generated keys to the `keys/` directory:

```bash
./3rdparty/vboot/scripts/image_signing/sign_firmware.sh \
	./build/coreboot.rom \
	 keys/ \
	 coreoot_signed.rom
```

If in doubt what parameters you should pass, add `--help` as a parameter to the
script.

The successful output should look like this:

```txt
No dev firmware keyblock/datakey found. Reusing normal keys.
 - import root_key from keys//root_key.vbpubk: success
 - import recovery_key from keys//recovery_key.vbpubk: success
successfully saved new image to: coreoot_signed.rom
```

Now the image will be signed with your own keys. Be sure to save the keys in a
safe location, because you will need them to sign each firmware update.
Otherwise, the firmware updates to RW partitions will not be executed by vboot.
