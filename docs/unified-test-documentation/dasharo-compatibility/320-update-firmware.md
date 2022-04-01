# Dasharo Compatibility: Update Firmware

## Test cases

### Common

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

### FFF001.001 Update firmware using downloaded files

**Test description**

This test verify whether it is possible to update the firmware on the DUT, and
check the firmware version is correct.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md/#dasharo-security-uefi-secure-boot).

**Test steps**

1. Power on the DUT.

1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and run the follwing commands to download and extract
   required files:
    ```bash
    sudo wget --content-disposition \
     https://cloud.3mdeb.com/index.php/s/RHRtf72d6MoMdy2/download \
     https://cloud.3mdeb.com/index.php/s/DqXD2So3eYrNf2y/download \
     https://cloud.3mdeb.com/index.php/s/FqH7akAq6XPaweF/download \
     https://cloud.3mdeb.com/index.php/s/GRA4e7J5pT4oSt4/download -P 
     etc/fwupd/remotes.d
    unzip fwupd-novacustom-v1.0.1.zip
    unzip flashrom-1.2-2-3mdeb.zip
    unzip fwupd-1.7.3.2-3mdeb.zip
    ```
1. Install requird packages:
    ```bash
    sudo apt install ./flashrom_1.2-2_amd64.deb \
                     ./libflashrom1_1.2-2_amd64.deb \
                     ./libflashrom-dev_1.2-2_amd64.deb \
                     ./libgusb2_0.3.5-1_amd64.deb \
                     ./libgusb-dev_0.3.5-1_amd64.deb
                     ./fwupd_1.7.3+r70+ge720ed96_amd64.deb \
                     ./fwupd-doc_1.7.3+r70+ge720ed96_all.deb \
                     ./fwupd-tests_1.7.3+r70+ge720ed96_amd64.deb \
                     ./gir1.2-fwupd-2.0_1.7.3+r70+ge720ed96_amd64.deb \
                     ./gir1.2-fwupdplugin-1.0_1.7.3+r70+ge720ed96_amd64.deb \
                     ./gir1.2-gusb-1.0_0.3.5-1_amd64.deb \
                     ./libfwupd2_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupd-dev_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupdplugin4_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupdplugin-dev_1.7.3+r70+ge720ed96_amd64.deb \                
    ```
1. Start update firmware:
    ```bash
        sudo fwupdtool update --verbose
    ```
1. Reboot the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and run the following command to verify results:
    ```bash
    sudo dmidecode -t bios
    ```

**Expected result**

Below are present possible results after last step. Line with version should 
contain the correct firmware version.

    ```bash
    BIOS Information
    	Vendor: 3mdeb Embedded Systems Consulting
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
