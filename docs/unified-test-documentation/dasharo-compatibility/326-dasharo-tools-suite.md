# Dasharo Compatibility: Dasharo Tools Suite

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Wired network connection.
1. Disable Secure Boot.
1. Prepare the [bootable USB stick](../../common-coreboot-docs/dasharo_tools_suite/#bootable-usb-stick)
1. Make yourself familiar with
    [Dasharo Tools Suite](../../common-coreboot-docs/dasharo_tools_suite).

## DTS001.001 Booting DTS from USB works correctly

**Test description**

This test aims to verify that DTS is properly booting from USB.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.

TBD

**Expected result**

SCREEN - TBD

## DTS002.001 DTS option Creating Dasharo HCL report works correctly

**Test description**

This test aims to verify that the option `Dasharo HCL report` in the DTS menu
properly creates the report.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Option `1)` - TBD

**Expected result**

TBD - output

## DTS003.001 DTS option power-off DUT works correctly

**Test description**

This test aims to verify that the option `Power off system` in the DTS menu
turns off the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Option `10)` - TBD

**Expected result**

The DUT should be turned off.

## DTS004.001 DTS option reboot DUT works correctly

**Test description**

This test aims to verify that the option `Reboot system` in the DTS menu reboots
the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Option `11)` - TBD

**Expected result**

The DUT should be restarted.

## DTS005.001 DTS drop-to-shell option works correctly

**Test description**

This test aims to verify that the option `Shell` in the DTS menu opens Shell.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Option `9)` - TBD

**Expected result**

TBD

## DTS006.001 Attempt to flash device from DTS shell by using flashrom works correctly

**Test description**

This test aims to verify whether is the possibility to flash the DUT firmware by
using flashrom in `DTS Shell`.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. `{PATH}` = individual path to a specific binary.

**Test steps**

TBD

1. Power on the DUT.
1. Wait for `Enter an option`.
1. Type 9 and click `Enter` to launch Shell.
1. Run the following command to obtain `coreboot.rom` binary:

    ```bash
    wget https://3mdeb.com/open-source-firmware/{PATH} -O /tmp/coreboot.rom
    ```

    > This is not only way to obtain binary. For example you can use `scp`.

1. Run the following command to flash firmware:

    ```bash
    flashrom -p internal -w /tmp/coreboot.rom
    ```

1. Power off the DUT.
1. Repeat steps 1-8.
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

## DTS007.001 Attempt to update device firmware from DTS Shell by using fwupd works correctly

**Test description**

This test aims to verify whether there is the possibility to update the DUT
firmware by using fwupd in DTS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

TBD

1. Power on the DUT.
1. Wait for `Enter an option`.
1. Type 9 and click `Enter` to launch into Shell.
1. Run the following commands to update firmware to the latest version:

    ```bash
    fwupdmgr refresh
    fwupdmgr update
    ```

1. Power off the DUT.
1. Repeat steps 1-8.
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

## DTS008.001 Attempt to flash device EC firmware by using DTS built-in script works correctly

**Test description**

This test aims to verify whether there is the possibility to flash the DUT EC
firmware by using the built-in script in DTS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. TBD

**Expected result**

TBD
