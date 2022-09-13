# Building manual

## Building coreboot

To build coreboot image, follow the steps below:

1. Clone the coreboot repository:

    ```bash
    git clone https://review.coreboot.org/coreboot.git
    ```

2. Get the submodules:

    ```bash
    cd coreboot
    git submodule update --init --recursive --checkout
    ```

3. Checkout Dasharo development branch for KGPE-D16:

    ```bash
    git remote add dasharo https://github.com/dasharo/coreboot.git
    git fetch dasharo
    git checkout asus_kgpe-d16/release
    ```

4. Start docker container:

    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

5. Inside of the container, configure and start the build process:

    ```bash
    (docker)cp configs/config.asus_kgpe_d16_<variant> .config
    (docker)make olddefconfig
    (docker)make
    ```

This will produce a debug binary placed in `build/coreboot.rom` for a 2MB flash
chip. In order to build for 8MB or 16MB chip use the `configs/config.asus_kgpe_d16_8M`
and `configs/config.asus_kgpe_d16_16M` respectively.

Dasharo v0.1.0 for KGPE-D16 supports only 8MB target with `configs/config.asus_kgpe_d16`.

To flash coreboot refer to [Flashing section in the hardware setup page.](setup.md#flashing)

## Other variants

Since the Dasharo v0.3.0 release the firmware comes in two more variatns: with
TPM 1.2 and TPM 2.0 support. Now the possible confis to use are:

- `configs/config.asus_kgpe_d16_vboot_tpm12` - 2MB target with vboot and TPM 1.2
- `configs/config.asus_kgpe_d16_vboot_tpm2` - 2MB target with vboot and TPM 2.0
- `configs/config.asus_kgpe_d16_8M_vboot_tpm12` - 8MB target with vboot and TPM 1.2
- `configs/config.asus_kgpe_d16_8M_vboot_tpm2` - 8MB target with vboot and TPM  2.0
- `configs/config.asus_kgpe_d16_16M_vboot_tpm12` - 16MB target with vboot and
  TPM 1.2
- `configs/config.asus_kgpe_d16_16M_vboot_tpm2` - 16MB target with vboot and
  TPM 2.0
