# Dasharo Compatibility: Logo customization functionality

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Get familiar with
   [Logo customization procedure](../../guides/logo-customization.md)

## LCM001.001 Replace logo in existing image and flashing firmware

**Test description**

The test aims to verify whether replacing the logo in the existing image is
possible and, whether after flashing the DUT with the new image, the new logo
will be shown properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Current Dasharo firmware dedicated for the platform.

**Test steps**

1. Power on the DUT.
1. Hold the `BOOT_MENU_KEY` to enter the boot menu.
1. Select the `iPXE Network boot` option using the arrow keys and press `Enter`.
1. Select the `iPXE Shell` option using the arrow keys and press `Enter`.
1. Configure communication interface by using the following command:

    ```bash
    dhcp
    ```

1. Connect to the DTS ipxe menu by using the following command:

    ```bash
    chain http://boot.3mdeb.com/dts.ipxe
    ```

1. Wait for `Enter an option:`.
1. Type in `S` and press `Enter`.
1. Based on the
   [dedicated documentation](../../guides/logo-customization.md#boot-logo-replacement-instructions)
   replace the logo in an existing image.
1. Reboot the DUT and observe the boot logo.

**Expected result**

During the DUT booting process, custom logo should appear on the screen.

## LCM002.001 Build image with custom logo and flashing firmware

**Test description**

This test aims to verify whether building an image with the custom logo is
possible and, whether after flashing the DUT with the new image, the new logo
will be shown properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Based on the
    [dedicated documentation](../../guides/logo-customization.md#build-image-with-custom-logo)
    build firmware with the custom logo.
1. Flash the firmware by using the internal programmer and `flashrom` tool. If
    DUT is already flashed with the Dasharo firmware and only the logo should
    be replaced, the following command should be used:

    ```bash
    sudo flashrom -p internal --fmap -i BOOTSPLASH -w [path]
    ```

    If also the procedure of Dasharo firmware updating should be performed,
    the following command should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --fmap -i RW_SECTION_A
    ```

    In any other cases, the following command should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --ifd -i bios
    ```

1. Reboot DUT.

**Expected result**

During the DUT booting process, custom logo should appear on the screen.

## LCM003.001 Attempt to flash firmware with improper image

**Test description**

This test aims to verify whether the attempt to flash the DUT with firmware
with an improper logo is possible but will result in a fallback to the default
logo.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Based on the
    [dedicated documentation](../../guides/logo-customization.md#build-image-with-custom-logo)
    build firmware with the logo, that that does not meet the
    [Quality criteria](../../guides/logo-customization.md#prerequisites).
1. Flash the firmware by using the internal programmer and `flashrom` tool. If
    DUT is already flashed with the Dasharo firmware and only the logo should
    be replaced, the following command should be used:

    ```bash
    sudo flashrom -p internal --fmap -i BOOTSPLASH -w [path]
    ```

    If also the procedure of Dasharo firmware updating should be performed,
    the following command should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --fmap -i RW_SECTION_A
    ```

    In any other cases, the following command should be used:

    ```bash
    flashrom -p internal -w [path-to-binary] --ifd -i bios
    ```

1. Reboot DUT.

**Expected result**

During the DUT booting process, the default logo should appear on the screen.

## LCM004.001 Custom logo persists after firmware update

**Test description**

This test aims to verify whether after updating the platform's firmware with
the `fwupd` command, the custom added logo remains unaffected and continues to
display.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot `Dasharo Tools Suite`
1. Type in `9` to gain shell access.
1. Basing on the
   [dedicated documentation](../../guides/logo-customization.md#build-image-with-custom-logo)
   replace the logo in an existing image.
1. Run `dasharo-deploy update`
1. Reboot the DUT and observe the boot logo.

**Expected result**

During the DUT booting process, the custom logo replacement should be
displayed.
