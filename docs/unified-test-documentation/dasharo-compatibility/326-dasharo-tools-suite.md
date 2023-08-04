# Dasharo Compatibility: Dasharo Tools Suite

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Wired network connection.
1. Disable Secure Boot.
1. Prepare the [bootable USB stick](https://docs.dasharo.com/dasharo-tools-suite/documentation#bootable-usb-stick)
1. Make yourself familiar with
    [Dasharo Tools Suite](https://docs.dasharo.com/dasharo-tools-suite/overview).

## DTS001.001 Booting DTS from USB works correctly

**Test description**

This test aims to verify that DTS is properly booting from USB.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.

**Expected result**

After a while, the DTS menu should appear.

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

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `1` and press `Enter`.
1. Wait for the question: `Do you want to support Dasharo development by`
    `sending us logs with hardware configuration`?
1. Type in `y` and press Enter.

**Expected result**

The whole process may take a few minutes.

1. The report should be generated.
1. The report should be sent to the cloud.
1. In the summary should be displayed information that all calls exited without
    errors.

Example summary output:

```bash
SUMMARY
========

 > All Curl calls exited without errors
 > Attempt to send completed > <report_name>.tar.gz
Thanks you for supporting Dasharo!
```

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

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `10` and press `Enter`.

**Expected result**

The DUT should be turned off without any complications.

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

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `11` and press `Enter`.

**Expected result**

The DUT should be rebooted without any complications.

## DTS005.001 DTS drop-to-shell option works correctly

**Test description**

This test aims to verify that the option `Shell` in the DTS menu opens Shell.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `9` and press `Enter`.

**Expected result**

1. Information about entering the shell and how to exit should be displayed.
1. Shell command input should be activated.

Example output:

```bash
Entering shell, to leave type exit and press Enter or press LCtrl+D

bash-5.1#
```

## DTS006.001 Flash device from DTS shell by using flashrom works correctly

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

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type 9 and click `Enter` to launch Shell.
1. Run the following command to obtain `coreboot.rom` binary:

    ```bash
    wget https://3mdeb.com/open-source-firmware/{PATH} -O /tmp/coreboot.rom
    ```

    > The above-described command is not the only way to obtain binary. For
    > example, `scp` command might be used, too.

1. Run the following command to flash the firmware:

    ```bash
    flashrom -p internal -w /tmp/coreboot.rom
    ```

    > Additional parameters may be needed for the `flashrom` command depending
    > on the DUT. Documentation describing the exact command to flash the
    > specific platform is always available in localization:
    > `Supported hardware` -> `Platform name` -> `Initial Deployment`.

1. Power off the DUT.
1. Repeat steps 2-6.
1. Run the following command to check the firmware version:

    ```bash
    dmidecode -t 0
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about the current
firmware. The current firmware version should be equal to the binary version,
which you were flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```

## DTS007.001 Update device firmware from DTS Shell by using fwupd works correctly

**Test description**

This test aims to verify whether there is the possibility to update the DUT
firmware by using fwupd in DTS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `9` and press `Enter`.
1. Run the following commands to update the firmware to the latest version:

    ```bash
    fwupdmgr refresh
    fwupdmgr update
    ```

1. Power off the DUT.
1. Repeat steps 2-6.
1. Run the following command to check the firmware version:

    ```bash
    dmidecode -t 0
    ```

1. Note the results.

**Expected result**

The output of `dmidecode` command should contain information about the current
firmware. The current firmware version should be equal to the binary version,
which you were flashing.

Example output:

```bash
Version: Dasharo (coreboot+UEFI) v1.1.0
```

## DTS008.001 Flash device EC firmware by using DTS built-in script works correctly

**Test description**

This test aims to verify whether there is the possibility to flash the DUT EC
firmware by using the built-in script in DTS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Proceed with
    [Dasharo EC Transition](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-transition).

**Expected result**

1. After the flashing procedure itself, the DUT should be able to boot.
1. The EC firmware version, after checking the method described in the
    above-mentioned [documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-transition),
    should correspond to the latest version.

## DTS009.001 Update device EC firmware by using DTS works correctly

**Test description**

This test aims to verify whether there is the possibility to update the DUT EC
firmware by using system76_ectool in DTS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug the USB stick with DTS into the USB slot on the DUT.
1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the UEFI Boot Menu.
1. Select the USB stick with DTS using the arrow keys and press `Enter`.
1. Wait for `Enter an option:`.
1. Type in `9` and press `Enter`.
1. Proceed with
    [Dasharo EC Update](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-update).

**Expected result**

1. After the updating firmware procedure itself, the DUT should be able to boot.
1. The EC firmware version, after checking the method described in the
    above-mentioned [documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation#ec-update),
    should correspond to the binary version used.
