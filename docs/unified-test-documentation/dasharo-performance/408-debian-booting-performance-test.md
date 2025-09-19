# Dasharo Performance: Debian booting performance test

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

## BDE001.001 Boot Debian LTS from disk after cold-boot

**Test description**

This test aims to verify that Debian LTS could be booted from the disk
on the DUT after cold-boot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11.6

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Cut the power off while DUT is turned on.
1. Restore power and power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the disk on which the system was previously
   installed or boot entry with the name of `OPERATING_SYSTEM`.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## BDE002.001 Boot Debian LTS from disk after warm-boot

**Test description**

This test aims to verify that Debian LTS could be booted from the disk
on the DUT after warm-boot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11.6

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the disk on which the system was previously
   installed or boot entry with the name of `OPERATING_SYSTEM`.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.

## BDE003.001 Boot Debian LTS from disk after reboot

**Test description**

This test aims to verify that Debian LTS could be booted from the disk
on the DUT after reboot. The test is performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Debian 11.6

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    sudo reboot
    ```

1. Press `BOOT_MENU_KEY` to enter the boot menu.
1. In the `Boot Menu`, select the disk on which the system was previously
   installed or boot entry with the name of `OPERATING_SYSTEM`.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
