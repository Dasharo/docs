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

### FFF001.001 Update firmware using downloaded files

**Test description**

This test verify whether it is possible to update the firmware on the DUT.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. [Disable Secure Boot](../../unified-test-documentation/dasharo-security/206-secure-boot.md/#dasharo-security-uefi-secure-boot).
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and run the follwing commands:
    ```bash
    sudo wget --content-disposition \
     https://cloud.3mdeb.com/index.php/s/dFWpcAkEAqd9pHX/download \
     https://cloud.3mdeb.com/index.php/s/gLdfYX84a4yrLRm/download \
     https://cloud.3mdeb.com/index.php/s/XPn57kZeCSjk7iN/download \
     https://cloud.3mdeb.com/index.php/s/GRA4e7J5pT4oSt4/download -P etc/fwupd/remotes.d
    unzip fwupd-novacustom-v1.0.1.zip
    unzip flashrom-1.2-2-3mdeb.zip
    unzip fwupd-1.7.3.2-3mdeb.zip
    sudo apt install ./flashrom_1.2-2_amd64.deb \
                     ./libflashrom1_1.2-2_amd64.deb \
                     ./libflashrom-dev_1.2-2_amd64.deb \
                     ./fwupd_1.7.3+r70+ge720ed96_amd64.deb \
                     ./fwupd-doc_1.7.3+r70+ge720ed96_all.deb \
                     ./fwupd-tests_1.7.3+r70+ge720ed96_amd64.deb \
                     ./gir1.2-fwupd-2.0_1.7.3+r70+ge720ed96_amd64.deb \
                     ./gir1.2-fwupdplugin-1.0_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupd2_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupd-dev_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupdplugin4_1.7.3+r70+ge720ed96_amd64.deb \
                     ./libfwupdplugin-dev_1.7.3+r70+ge720ed96_amd64.deb
    sudo fwupdmgr refresh --force
    sudo fwupdmgr update
    ```
1. Reboot the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and run the following command to verify results:
    ```bash
    sudo fwupdmgr get-results
    ```
1. Select device, which was updating, and the results will be displayed.

**Expected result**

Below are present possible results after two last steps:

```bash
    Choose a device:
    0.  Cancel
    1.  4bde70ba4e39b28f9eab1628f9dd6e6244c03027 (11th Gen Intel Core™ i7-1165G7 @ 2.80GHz)
    2.  5792b48846ce271fab11c4a545f7a3df0d36e00a (Display controller)
    3.  073c01931cb0e9889bbfb2ea4a4c2fc558805fc6 (Display controller)
    4.  dbee8bd3b1ae0316ad143336155651eedb495a0e (NV4XMB,ME,MZ)
    5.  71b677ca0f1bc2c5b804fa1d59e52064ce589293 (SSD 980 PRO 1TB)
    6.  c6a80ac3a22083423992a3cb15018989f37834d6 (TPM)
    7.  eefcbd318bd31fc1eba6358e628b3f9dceb87206 (USB4 host controller)
``` 
```bash
    NV4XMB,ME,MZ:
      Device ID:            dbee8bd3b1ae0316ad143336155651eedb495a0e
      Previous version:     0.5.0
      Update State:         Success
      Last modified:        2022-01-13 11:09
      GUID:                 230c8b18-8d9b-53ec-838b-6cfc0383493a
      Device Flags:         • Internal device
                            • Updatable
                            • System requires external power source
                            • Needs shutdown after installation
                            • Cryptographic hash verification is available
```
