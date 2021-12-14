# coreboot vboot signing

## Introduction

Verified Boot is a method of verifying that the firmware compents haven't been
tampered with. It uses cryptographic signatures to determine whether the
firmware comes from trusted source. This document covers the procedure for
generating vboot keys and configuring the coreboot build system to sign the
binaries with the generated keys.

## Preparation

Navigate to the coreboot tree.

## Generating keys

Start by updating git submodules:

```bash
git submodule update --init --checkout
```

Build and install vboot utilities:

```bash
cd 3rdparty/vboot
make
sudo make install
```

Navigate to the directory containing vboot key generation scripts:

```bash
cd scripts/keygeneration
```

Generate the scripts with the following command:

```bash
./create_new_keys.sh
```

The keys will be created in the directory `3rdparty/vboot/scripts/keygeneration`.

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
