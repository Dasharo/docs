# coreboot vboot signing

## Introduction

Verified Boot is a method of verifying that the firmware compents haven't been
tampered with. It uses cryptographic signatures to determine whether the
firmware comes from trusted source. This document covers the procedure for
generating vboot keys and configuring the coreboot build system to sign the
binaries with the generated keys.

## Prerequisites

* Functional Docker installation
    - follow [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    - follow [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)

* Clone [dasharo-tools](https://github.com/Dasharo/dasharo-tools) repository

```bash
git clone https://github.com/Dasharo/dasharo-tools.git
```

## Generating keys

> Make sure that you are in the `dasharo-tools` repository

Generate the keys with the following command:

```bash
./vboot/generate_keys keys
```

The keys will be created in the directory `$PWD/keys`, i.e. in the `keys`
subdirectory in your current directory.

## Signing image without rebuilding

This is the default procedure that should be followed by users downloading
firmware from the `Release` section, who wishes to use their own keys for
vboot.

> Make sure that you are in the `dasharo-tools` repository

Be sure you have generated the keys as in [Generate keys](#generating-keys)
section. Assuming you have generated keys to the `keys/` directory:

```bash
./vboot/resign <released_firmware_file> keys
```

For example:

```bash
./vboot/resign protectli_vault_cml_v1.0.16_resigned.rom keys
```

The successful output can look like this:

```txt
...
INFO: sign_bios_at_end: BIOS image does not have FW_MAIN_B. Signing only FW_MAIN_A
 - import root_key from /.../keys/root_key.vbpubk: success
 - import recovery_key from /.../keys/recovery_key.vbpubk: success
successfully saved new image to: /.../protectli_vault_cml_v1.0.16_resigned.rom
The /.../protectli_vault_cml_v1.0.16.rom was resigned and saved as: /.../protectli_vault_cml_v1.0.16_resigned.rom
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
