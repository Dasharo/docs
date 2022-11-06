# Dasharo Compatibility: Firmware update using fwupd

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
1. Install the `dmidecode` package: `sudo apt install dmidecode`.
1. Make yourself familiar with
    [Updating firmware using fwupd](/unified/novacustom/fwupd-usage.md)

## FFW001.001 Firmware update by using fwupd

**Test description**

This test verify whether it is possible to update the firmware on the DUT by
using fwupd demon.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the  system by using the proper login and password.
1. Configure environment in accordance with the
    [documentation](/unified/novacustom/fwupd-usage.md)
1. Start firmware updating procedure by executing the following command in
    the terminal:

    ```bash
        sudo fwupdmgr update
    ```

1. Reboot the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command to verify results:

    ```bash
    sudo dmidecode -t bios
    ```

**Expected result**

The output of `dmidecode` command should contain information about current
firmware. The current firmware version should be equal to the latest released
firmware version.

Example output:

```bash
BIOS Information
        Vendor: 3mdeb
        Version: Dasharo (coreboot+UEFI) v1.1.0
        Release Date: 03/24/2022
        ROM Size: 16 MB
        Characteristics:
            PCI is supported
            PC Card (PCMCIA) is supported
            BIOS is upgradeable
            BIOS shadowing is allowed
            Selectable boot is supported
            ACPI is supported
            USB legacy is supported
            Targeted content distribution is supported
            UEFI is supported
        BIOS Revision: 1.1
        Firmware Revision: 0.0
```
