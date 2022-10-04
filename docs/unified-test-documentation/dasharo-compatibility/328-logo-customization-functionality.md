# Dasharo Compatibility: Logo customization functionality

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## LCM001.001 Replace logo in existing image and flashing firmware

**Test description**

This test aims to verify whether it's possible to replace logo in existing
firmware image and flash this firmware on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Proceed with the
    [Replace logo in an existing image](../../common-coreboot-docs/custom_logo.md#replace-logo-in-an-existing-image)
    section.
1. Reboot DUT.

**Expected result**

1. While booting custom logo appears on screen.

## LCM002.001 Build image with custom logo and flashing firmware

**Test description**

This test aims to verify whether it's possible to build firmware image from the
source and flash it on the DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Proceed with the
    [Build image with custom logo](../../common-coreboot-docs/custom_logo.md#build-image-with-custom-logo)
    section.
1. Now you can flash the updated firmware image as usual. If you're not updating
firmware and just changing the logo, only the BOOTSPLASH region needs to be
updated. For example:

    ```bash
    sudo flashrom -p internal --fmap -i BOOTSPLASH -w [path]
    ```

1. Reboot DUT.

**Expected result**

1. While booting custom logo appears on screen.

## LCM003.001 Attempt to flash firmware with improper image

**Test description**

This test aims to verify whether after building firmware with inproper custom
logo fallback will occur.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Proceed with the
    [Build image with custom logo](../../common-coreboot-docs/custom_logo.md#build-image-with-custom-logo)
    section, but use image that doesn't meet
    [Prequsities](../../common-coreboot-docs/custom_logo.md#prerequisites).
1. Now you can flash the updated firmware image as usual. If you're not updating
firmware and just changing the logo, only the BOOTSPLASH region needs to be
updated. For example:

    ```bash
    sudo flashrom -p internal --fmap -i BOOTSPLASH -w [path]
    ```

1. Reboot DUT.

**Expected result**

Fallback to NovaCustom logo occurs, and during boot phase oroginal image is
shown.
