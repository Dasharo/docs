# Dasharo Compatibility: Windows booting

## Common

**Test setup**

1. Proceed with the
   [Generic test setup: Firmware](../../generic-test-setup#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../../generic-test-setup#os-installation).

## WBT001.001 Windows 11 installation and boot

**Test description**

This test aims to verify that Windows 11 OS could be installed on the DUT
and works properly.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The Windows 11 login screen should be displayed.

## WBT002.001 Windows 10 installation and boot

**Test description**

This test aims to verify that Windows 10 OS could be installed on the DUT
and works properly.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The Windows 10 login screen should be displayed.
