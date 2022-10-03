# Dasharo Compatibility: Firmware building locally

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).

## FWB001.001 Build firmware locally

**Test description**

This test aims to verify whether it's possible to build firmware locally.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Proceed with the
    [Install Docker Engine on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
    instruction.
1. Proceed with the
    [Post-installation steps for Linux](https://docs.docker.com/engine/install/linux-postinstall/)
    instruction.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window.
1. Obtain the Docker image:

    ```bash
    docker pull coreboot/coreboot-sdk:0ad5fbd48d
    ```

1. Clone the coreboot repository:

    ```bash
    git clone https://review.coreboot.org/coreboot.git
    ```

1. Navigate to the source code directory and checkout to the desired revision:

    > Replace the REVISION with one of the:
    > - `novacustom_nv4x/release` for the latest released version
    > - `novacustom_nv4x_vVERSION` (e.g. `v1.2.1`) for the given release

    ```bash
    cd coreboot
    git remote add dasharo https://github.com/dasharo/coreboot.git
    git submodule update --init --recursive --checkout
    git fetch dasharo
    git checkout REVISION
    ```

1. Start the coreboot-sdk Docker container:

    ```bash
    docker run --rm -it -u $UID \
       -v $PWD:/home/coreboot/coreboot \
       -w /home/coreboot/coreboot \
       coreboot/coreboot-sdk:0ad5fbd48d /bin/bash
    ```

1. Build the firmware:

    ```bash
    cp configs/config.novacustom_ns5x .config
    make olddefconfig
    make
    ```

**Expected result**

The resulting coreboot image is placed in
`build/coreboot.rom`.

## FWB002.001 Flash locally built firmware

**Test description**

This test aims to verify whether it's possible to flash locally built firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Make yourself familiar with
    [SPI hardware write protection](../../../variants/asus_kgpe_d16/spi-wp/).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Localise loaclly built the `ROM` file (eg. `coreboot/build/coreboot.rom`)
1. Use below procedure to flash firmware on `nv4x` with the `ROM` file:
    [Link to procedure](https://docs.dasharo.com/variants/novacustom_nv4x/flashing_internal/)
1. Run the following command to check firmware version:

    ```bash
    dmidecode -t 0
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about current
firmware. The current firmware version should be equal to the binary version,
which you were flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```
