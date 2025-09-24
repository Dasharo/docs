# Dasharo Compatibility: Firmware locally building and flashing

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).
1. Make yourself familiar with Building manual procedure dedicated for
    the relevant platform:
    * [NovaCustom laptops](../../unified/novacustom/building-manual.md)

## FLB001.001 Firmware locally build

**Test description**

This test aims to verify whether there is a possibility to build firmware
on the local machine, based on `Build manual` procedure dedicated to the
platform.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Based on the dedicated documentation build firmware.
1. Check if the binary file, after finishing the building process, is available
    in the `build` location.

**Expected result**

The `build` location should contain the binary file, which size is equal to the
flash chip size.

## FLB002.001 Flash locally built firmware

**Test description**

This test aims to verify whether there is a possibility to flash the locally
built firmware to the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Localize the firmware, which was built in the `FLB001.001` test case.
1. Flash the firmware by using the internal programmer and `flashrom` tool. If
    DUT is already flashed with the Dasharo firmware, the following command
    should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --fmap -i RW_SECTION_A
    ```

    Otherwise, the following command should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --ifd -i bios
    ```

1. Reboot the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command to verify the results:

    ```bash
    sudo dmidecode -t bios | grep Version
    ```

**Expected result**

The output of `dmidecode` command should contain information about the current
firmware. The current firmware version should be equal to the latest released
firmware version.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```
