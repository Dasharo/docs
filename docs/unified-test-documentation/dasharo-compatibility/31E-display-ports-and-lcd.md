# Dasharo Compatibility: Display ports and LCD support

## Test cases

### Common

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk)

### DSP001.001 Internal LCD in firmware

**Test description**

This test verifies initialization of the laptop's embedded LCD screen during
firmware execution phase.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power ON the DUT
1. Observe the internal LCD during firmware execution phase
1. Power OFF the DUT

**Expected result**

1. Logo appears on the screen during firmware execution phase

### DSP001.002 Internal LCD in OS (Ubuntu 20.04)

**Test description**

This test verifies initialization of the laptop's embedded LCD in the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Observe the internal LCD after the `OPERATING_SYSTEM` has booted

**Expected result**

1. Either the login screen or the `OPERATING_SYSTEM` installer appears on the
   internal LCD

### DSP001.003 Internal LCD in OS (Windows 10)

**Test description**

This test verifies initialization of the laptop's embedded LCD in the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Observe the internal LCD after the `OPERATING_SYSTEM` has booted

**Expected result**

1. Either the login screen or the `OPERATING_SYSTEM` installer appears on the
   internal LCD

### DSP002.001 External HDMI display in OS (Ubuntu 20.04)

**Test description**

This test verifies initialization of the external HDMI display in the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Switch the display mode between `Mirror` and `Join Displays`

**Expected result**

1. The image should be displayed on the internal LCD and an external HDMI display
   in `Mirror` and `Join Displays` modes

### DSP002.002 External HDMI display in OS (Windows 10)

**Test description**

This test verifies initialization of the external HDMI display in the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BIOS_SETUP_KEY` = `F2`
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Switch the display mode between `Duplicate` and `Extend`

**Expected result**

1. The image should be displayed on the internal LCD and an external HDMI display
   in `Duplicate` and `Extend` modes
