# Dasharo Compatibility: Dmidecode

## Test cases

### DMI001.001 Verify the serial number

**Test description**

This test aims to verify that the DUT serial number is the same as it is 
expected.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `BOOT_MENU_KEY` = `ESC`
3. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t baseboard`
1. Power off the DUT

**Expected result**

1. An output from the command should be similar to:

   ```
   TBD
   ```
1. The character string after `Serial Number:` should be the same as it is
   expected.

### DMI001.002 Verify the firmware version

**Test description**

This test aims to verify that the firmware version on the DUT is the same as in
the firmware filename.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BOOT_MENU_KEY` = `ESC`
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t bios`
1. Power off the DUT

**Expected result**

1. An output from the command should be similar to:

   ```
   TBD
   ```
1. The character string after `Version:` should be the same as the firmware 
   fileneme indicates.

### DMI001.003 Verify the product name

**Test description**

This test aims to verify that the DUT product name is the same as it is 
expected.

**Test configuration data**

1. `FIRMWARE` = coreboot
2. `BOOT_MENU_KEY` = `ESC`
3. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t system`
1. Power off the DUT

**Expected result**

1. Output from the command should be similar to:

   ```
   TBD
   ```
1. The character string after `Product Name:` should be the same as it is
   expected.

### DMI001.004 Verify the release date

**Test description**

This test aims to verify that the firmware release date on the DUT is the same 
as for the firmware file.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BOOT_MENU_KEY` = `ESC`
1. `OPERATING_SYSTEM` = `Debian 11.0`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t bios`
1. Power off the DUT

**Expected result**

1. Output from the command should be similar to:

   ```
   TBD
   ```
1. The character string after `Release date:` should be the same as it is
   expected.
