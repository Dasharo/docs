# Dasharo compatibility: SMBIOS

## Common

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).
1. Install the `dmidecode` package: `sudo apt-get install dmidecode`.

## DMI001.001 Verify the serial number

**Test description**

This test aims to verify that the serial number field is filled in correctly
according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t system
    ```

1. In the `BIOS Information` section, check the `Serial number` field against the
    [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The fields should be filled in according to the Dasharo SMBIOS guidelines.

## DMI002.001 Verify the firmware version

**Test description**

This test aims to verify that the firmware version field is filled in correctly
according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t bios
    ```

1. In the `BIOS Information` section, check the `Version` field against the
    [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The fields should be filled in according to the Dasharo SMBIOS guidelines.

## DMI003.001 Verify the firmware product name

**Test description**

This test aims to verify that the firmware product name fields are filled in
correctly according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t system
    ```

1. In the `System Information` section, check the `Product Name` field against
    the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).
1. Execute the following command in the terminal:

    ```bash
    dmidecode -t baseboard
    ```

1. In the `Base Board Information` section, check the `Product Name` field
    against the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The fields should be filled in according to the Dasharo SMBIOS guidelines.

## DMI004.001 Verify the firmware release date

**Test description**

This test aims to verify that the firmware release date field are filled in
correctly according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t bios
    ```

1. In the `System Information` section, check the `Release Date` field
    against the
    [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The field should be filled in according to the Dasharo SMBIOS guidelines.

## DMI005.001 Verify the firmware manufacturer

**Test description**

This test aims to verify that the firmware manufacturer fields are filled in
correctly according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t system
    ```

1. In the `System Information` section, check the `Manufacturer` field against
   the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).
1. Execute the following command in the terminal:

    ```bash
    dmidecode -t baseboard
    ```

1. In the `Base Board Information` section, check the `Manufacturer` field
    against the
    [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The fields should be filled in according to the Dasharo SMBIOS guidelines.

## DMI006.001 Verify the firmware vendor

**Test description**

This test aims to verify that the firmware vendor field is filled in correctly
according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t bios
    ```

1. In the `BIOS Information` section, check the `Vendor` field against the
    [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The field should be filled in according to the Dasharo SMBIOS guidelines.

## DMI007.001 Verify the firmware family

**Test description**

This test aims to verify that the firmware family field is filled in correctly
according to the
[Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t system
    ```

1. In the `System Information` section, check the `Family` field against the
   [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The field should be filled in according to the Dasharo SMBIOS guidelines.

## DMI008.001 Verify the firmware type

**Test description**

This test aims to verify that the firmware type field is filled in correctly
according to the [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Open a terminal window and execute the following command:

    ```bash
    dmidecode -t chassis
    ```

1. In the `Chassis Information` section, check the `Type` field against the
   [Dasharo SMBIOS guidelines](https://docs.dasharo.com/dev-proc/smbios-rules/).

**Expected result**

1. The field should be filled in according to the Dasharo SMBIOS guidelines.
