# Dasharo Compatibility: ESP Partition Scanning

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).

The purpose of this test is to verify that the EFI partition is scanned for
any OS-specific folders and .efi files, and that corresponding boot menu
entries are created for them. The list of supported .efi files and their boot
menu entries is as follows:

* \EFI\Microsoft\Boot\bootmgfw.efi - Windows Boot Manager (on `<disk_name>`)
* \EFI\Suse\elilo.efi - Suse Boot Manager (on `<disk_name>`)
* \EFI\Ubuntu\grubx64.efi Ubuntu (on `<disk_name>`)
* \EFI\Ubuntu\shimx64.efi - Ubuntu (on `<disk_name>`)
* \EFI\Redhat\elilo.efi - RedHat Boot Manager (on `<disk_name>`)
* \EFI\Redhat\grubx64.efi - RedHat (on `<disk_name>`)
* \EFI\Redhat\shimx64.efi - RedHat (on `<disk_name>`)
* \EFI\Fedora\shimx64.efi - Fedora (on `<disk_name>`)
* \EFI\Fedora\grub64.efi - Fedora (on `<disk_name>`)
* \EFI\Centos\shimx64.efi - CentOS (on `<disk_name>`)
* \EFI\Centos\grubx64.efi - CentOS (on `<disk_name>`)
* \EFI\opensuse\grubx64.efi - OpenSuse (on `<disk_name>`)
* \EFI\debian\grubx64.efi - Debian (on `<disk_name>`)
* \EFI\qubes\shimx64.efi - Qubes OS (on `<disk_name>`)
* \EFI\qubes\grubx64.efi - Qubes OS (on `<disk_name>`)
* \EFI\DTS\grubx64.efi" - Dasharo Tools Suite (on `<disk_name>`) (populated
 regardless of removable media state)

## ESP001.001 ESP Scan with OS-specific .efi files added

**Test description**

This test aims to verify that any properly added .efi files will have boot menu
entries created for them.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Place some OS-specific folders and .efi files in /EFI/, as listed in
common test documentation above
1. Power on the DUT.
1. Enter Boot Menu
1. Note all the listed entries

**Expected result**

Systems corresponding with the newly added files should be listed in boot menu.

## ESP002.001 ESP Scan after deleting additional .efi files

**Test description**

This test aims to verify that none of the systems linger on in the boot menu
after we've deleted their files from /EFI/.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Delete any additional boot folders and files in the /EFI partition.
1. Power on the DUT.
1. Enter Boot Menu.
1. Note all the listed entries.

**Expected result**

None of the formerly added and now removed entries should still be listed
as available to boot.

## ESP003.001 ESP Scan ignores OSes on removable media

**Test description**

This test aims to verify that the bootable /EFI partitions of removable media are
ignored by the scan and aren't listed in boot menu.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug in a USB flash disk containing boot files in its /EFI partition
1. Power on the DUT.
1. Enter Boot Menu.
1. Note all the listed entries.

**Expected result**

None of the listed boot entries should be related to the USB stick - except DTS.

## ESP004.001 ESP Scan does not create duplicate entries

**Test description**

This test aims to verify that the firmware will not create duplicate entries,
for example, if both shimx64 and grubx64 are present for a single OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a distro folder in /EFI/ and place both the shimx64 and grubx64 files
there.
1. Power on the DUT.
1. Enter Boot Menu.
1. Note all the listed entries.

**Expected result**

Despite there being two files for a single distribution, there shouldn't be any
duplicate entries in the boot menu.

## ESP005.001 ESP Scan detects Dasharo Tools Suite

**Test description**

This test aims to verify that the firmware detects Dasharo Tools Suite boot
media and creates a corresponding boot menu entry

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Plug in a DTS flash stick to the DUT.
1. Power on the DUT.
1. Enter Boot Menu.
1. Note all the listed entries.

**Expected result**

Dasharo Tools Suite should be listed in the boot menu.
