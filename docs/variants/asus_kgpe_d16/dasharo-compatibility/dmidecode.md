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
   [Generic test setup: firmware](generic-test-setup#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t baseboard`
1. Power off the DUT

**Expected result**

1. An output from the command should be similar to:

   ```
   root@debian:~# dmidecode -t baseboard
   # dmidecode 3.3
   Getting SMBIOS data from sysfs.
   SMBIOS 3.0 present.

   Handle 0x0002, DMI type 2, 14 bytes
   Base Board Information
        Manufacturer: ASUS
        Product Name: KGPE-D16
        Version: 1.0
        Serial Number: 123456789
        Asset Tag: Not Specified
        Features: None
        Location In Chassis: Not Specified
        Chassis Handle: 0x0003
        Type: Motherboard

   Handle 0x000A, DMI type 41, 11 bytes
   Onboard Device
        Reference Designation: SATA controller
        Type: SATA Controller
        Status: Enabled
        Type Instance: 0
        Bus Address: 0000:00:11.0

   Handle 0x000B, DMI type 41, 11 bytes
   Onboard Device
        Reference Designation: VGA compatible controller
        Type: Video
        Status: Enabled
        Type Instance: 0
        Bus Address: 0000:e8:01.0

   root@debian:~# 
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
   [Generic test setup: firmware](generic-test-setup#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t bios`
1. Power off the DUT

**Expected result**

1. An output from the command should be similar to:

   ```
   root@debian:~# dmidecode -t bios
   # dmidecode 3.3
   Getting SMBIOS data from sysfs.
   SMBIOS 3.0 present.

   Handle 0x0000, DMI type 0, 26 bytes
   BIOS Information
        Vendor: 3mdeb Embedded Systems Consulting
        Version: Dasharo (coreboot+SeaBIOS) v0.2.0
        Release Date: 12/09/2021
        ROM Size: 16 MB
        Characteristics:
                PCI is supported
                PC Card (PCMCIA) is supported
                BIOS is upgradeable
                Selectable boot is supported
                ACPI is supported
                Targeted content distribution is supported
        BIOS Revision: 4.14
        Firmware Revision: 0.0
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
   [Generic test setup: firmware](generic-test-setup#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t system`
1. Power off the DUT

**Expected result**

1. Output from the command should be similar to:

   ```
   root@debian:~# dmidecode -t system
   # dmidecode 3.3
   Getting SMBIOS data from sysfs.
   SMBIOS 3.0 present.

   Handle 0x0001, DMI type 1, 27 bytes
   System Information
        Manufacturer: ASUS
        Product Name: KGPE-D16
        Version: 1.0
        Serial Number: 123456789
        UUID: Not Settable
        Wake-up Type: Reserved
        SKU Number: Not Specified
        Family: Not Specified

   Handle 0x0009, DMI type 32, 11 bytes
   System Boot Information
        Status: No errors detected

   root@debian:~#
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
   [Generic test setup: firmware](generic-test-setup#firmware)

**Test steps**

1. Power on the DUT
1. Boot into OS
1. Run `dmidecode -t bios`
1. Power off the DUT

**Expected result**

1. Output from the command should be similar to:

   ```
   # dmidecode 3.3
   Getting SMBIOS data from sysfs.
   SMBIOS 3.0 present.

   Handle 0x0000, DMI type 0, 26 bytes
   BIOS Information
        Vendor: 3mdeb Embedded Systems Consulting
        Version: Dasharo (coreboot+SeaBIOS) v0.2.0
        Release Date: 12/09/2021
        ROM Size: 16 MB
        Characteristics:
                PCI is supported
                PC Card (PCMCIA) is supported
                BIOS is upgradeable
                Selectable boot is supported
                ACPI is supported
                Targeted content distribution is supported
        BIOS Revision: 4.14
        Firmware Revision: 0.0
   ```
2. The character string after `Release date:` should point to the date of the
   tag on the repository of given Dasharo version.
