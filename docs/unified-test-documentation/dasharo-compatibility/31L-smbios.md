# Dasharo Compatibility: SMBIOS

## Test cases
### DMI002.001 Verify the firmware version

**Test description**

This test aims to verify that the firmware version field is filled in correctly
according to the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t bios`
1. In the `BIOS Information` section, check the `Version` field against the
   [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/) and
   `dmidecode.log`

**Expected result**

1. The fields should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`

### DMI003.001 Verify the firmware product name

**Test description**

This test aims to verify that the firmware product name fields are filled in
correctly according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t system`
1. In the `System Information` section, check the `Product Name` field
   against the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)
   and `dmidecode.log`
1. Open a terminal window and run `sudo dmidecode -t baseboard`
1. In the `Base Board Information` section, check the `Product Name` field
   against the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)
   and `dmidecode.log`

**Expected result**

1. The fields should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`

### DMI005.001 Verify the firmware manufacturer

**Test description**

This test aims to verify that the firmware manufacturer fields are filled in
correctly according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t system`
1. In the `System Information` section, check the `Manufacturer` field against
   the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/) and
   `dmidecode.log`
1. Open a terminal window and run `sudo dmidecode -t baseboard`
1. In the `Base Board Information` section, check the `Manufacturer` field
   against the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)
   and `dmidecode.log`

**Expected result**

1. The fields should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`

### DMI006.001 Verify the firmware vendor

**Test description**

This test aims to verify that the firmware vendor field is filled in correctly
according to the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t bios`
1. In the `BIOS Information` section, check the `Vendor` field against
   the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/) and
   `dmidecode.log`

**Expected result**

1. The field should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`

### DMI007.001 Verify the firmware family

**Test description**

This test aims to verify that the firmware family field is filled in correctly
according to the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t system`
1. In the `System Information` section, check the `Family` field against
   the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/) and
   `dmidecode.log`

**Expected result**

1. The field should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`

### DMI008.001 Verify the firmware type

**Test description**

This test aims to verify that the firmware type field is filled in correctly
according to the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/)

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../dasharo-compatibility/generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../dasharo-compatibility/generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../dasharo-compatibility/generic-test-setup/#os-boot-from-disk)
1. Install the `dmidecode` package: `sudo apt install dmidecode`
1. Obtain the stock firmware dump from [cloud.3mdeb.com](https://cloud.3mdeb.com/index.php/f/391118)
1. Extract the dump and open the `dmidecode.log` file

**Test steps**

1. Open a terminal window and run `sudo dmidecode -t chassis`
1. In the `Chassis Information` section, check the `Type` field against
   the [guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/) and
   `dmidecode.log`

**Expected result**

1. The field should be filled in according to the Dasharo Guidelines and
   `dmidecode.log`
