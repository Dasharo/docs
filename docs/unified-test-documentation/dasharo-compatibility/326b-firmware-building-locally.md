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
1. Proceed with the
    [Building manual for NV4x](../../variants/novacustom_nv4x/building.md),
    or [Building manual for NV5x/NV7x](../../variants/novacustom_ns5x_7x/building-manual.md)
    appropriate for DUT.

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
1. Flash DUT with built firmware accordingly to
    [Flashing instructions for NV4x](../../variants/novacustom_nv4x/flashing_internal.md),
    or with [Flashing instructions for NV5x/NV7x](../../variants/novacustom_ns5x_7x/firmware-update.md)
    appropriate for DUT.
1. Reboot platform.
1. Use below command to get firmware info:

    ```bash
    sudo dmidecode
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about current
firmware. The current firmware version should be equal to the binary version,
which you were building and flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```
