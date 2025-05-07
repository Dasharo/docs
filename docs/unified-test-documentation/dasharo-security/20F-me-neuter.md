# Dasharo Security: ME neuter/disable

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## MNE001.001 Intel ME mode option is available and has the correct default state

**Test description**

This test aims to verify that the `Intel ME mode` state after flashing the
platform with the Dasharo firmware is correct.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Intel Management Engine Options` submenu.
1. Verify the `Intel ME mode` field.

**Expected result**

The `Intel ME mode` field should inform that the current state is `Enabled`.

## MNE002.201 Intel ME mode option Enabled works correctly (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MNE004.201 Intel ME mode option Disable (HAP) works correctly (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## MNE005.201 PCI Express 5.0 port is functional when ME disabled (Ubuntu)

**Test description**

This test aims to verify that `Intel ME mode` option in state Disable (HAP) or
Disable (Soft) does not break the PCIe 5.0 port functionality and the caching
of PCIe 5.0 firmware by Dasharo works.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu
3. DUT (Alder Lake or newer) with PCIe 5.0 port and a PCIe device plugged to
   the port.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
2. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
3. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
4. Enter the `Intel Management Engine Options` submenu.
5. Verify that the `Intel ME mode` option is in state `Disable (HAP)` or
   `Disable (Soft)` - if not, using the arrow keys and `Enter`, choose option
   `Disable (HAP)` or `Disable (Soft)`.
6. Press `F10` to save the changes.
7. If necessary - press `Y` to confirm saving the changes.
8. Go back to the main menu using the `ESC` key.
9. Select the `Reset` option to apply the settings and reboot.
10. Boot into the system.
11. Log into the system by using the proper login and password.
12. Open a terminal window and run the following command:

    ```bash
    sudo cbmem -1 > cbmem.log
    lspci
    lspci -t
    ```

13. Note the results. Repeat all steps to cover both disable methods.

**Expected result**

The output of the command should contain the information about PCI Express 5.0
interface located at PCI 00:01.0. Also the device plugged to the PCI port
00:01.0 should be visible and functional.

Example of desired output:

```bash
lspci -t
-[0000:00]-+-00.0
           +-01.0-[01]--+-00.0
           |            \-00.1
           +-02.0
           +-06.0-[02]----00.0
           +-14.0
           +-14.2
           +-17.0
           +-1a.0-[03]----00.0
           +-1c.0-[04]--
           +-1c.2-[05]----00.0
           +-1c.4-[06-08]----00.0-[07-08]----00.0-[08]--+-00.0
           |                                            \-00.1
           +-1d.0-[09]----00.0
           +-1f.0
           +-1f.3
           +-1f.4
           \-1f.5

```

```bash
lspci
00:00.0 Host bridge: Intel Corporation Device 4648 (rev 02)
00:01.0 PCI bridge: Intel Corporation 12th Gen Core Processor PCI Express x16 Controller #1 (rev 02)
00:02.0 Display controller: Intel Corporation AlderLake-S GT1 (rev 0c)
00:06.0 PCI bridge: Intel Corporation 12th Gen Core Processor PCI Express x4 Controller #0 (rev 02)
00:14.0 USB controller: Intel Corporation Device 7ae0 (rev 11)
00:14.2 RAM memory: Intel Corporation Device 7aa7 (rev 11)
00:17.0 SATA controller: Intel Corporation Device 7ae2 (rev 11)
00:1a.0 PCI bridge: Intel Corporation Device 7ac8 (rev 11)
00:1c.0 PCI bridge: Intel Corporation Device 7ab8 (rev 11)
00:1c.2 PCI bridge: Intel Corporation Device 7aba (rev 11)
00:1c.4 PCI bridge: Intel Corporation Device 7abc (rev 11)
00:1d.0 PCI bridge: Intel Corporation Device 7ab0 (rev 11)
00:1f.0 ISA bridge: Intel Corporation Device 7a84 (rev 11)
00:1f.3 Audio device: Intel Corporation Device 7ad0 (rev 11)
00:1f.4 SMBus: Intel Corporation Device 7aa3 (rev 11)
00:1f.5 Serial bus controller: Intel Corporation Device 7aa4 (rev 11)
01:00.0 VGA compatible controller: NVIDIA Corporation GA106 [GeForce RTX 3060 Lite Hash Rate] (rev a1)
01:00.1 Audio device: NVIDIA Corporation Device 228e (rev a1)
02:00.0 Non-Volatile memory controller: Intel Corporation Device f1aa (rev 03)
03:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO
05:00.0 Ethernet controller: Intel Corporation Ethernet Controller I225-V (rev 03)
06:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Upstream Port of PCI Express Switch (rev c1)
07:00.0 PCI bridge: Advanced Micro Devices, Inc. [AMD/ATI] Navi 10 XL Downstream Port of PCI Express Switch
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 743f (rev c1)
08:00.1 Audio device: Advanced Micro Devices, Inc. [AMD/ATI] Navi 21 HDMI Audio [Radeon RX 6800/6800 XT / 6900 XT]
09:00.0 Non-Volatile memory controller: Samsung Electronics Co Ltd NVMe SSD Controller PM9A1/PM9A3/980PRO
```

The device that must be visible and working:

```txt
00:01.0 PCI bridge: Intel Corporation 12th Gen Core Processor PCI Express x16 Controller #1 (rev 02)
```

The device behind the port must also be visible, in this example it is:

```txt
01:00.0 VGA compatible controller: NVIDIA Corporation GA106 [GeForce RTX 3060 Lite Hash Rate] (rev a1)
01:00.1 Audio device: NVIDIA Corporation Device 228e (rev a1)
```

To verify the PCIe 5.0 firmware caching is working, check the `cbmem.log` for
the following string:

```text
[INFO ]  Loading HSPHY firmware from cache
```

If there are no errors printed nearby concerning the HSPHY, test pass.

## MNE006.201 Check Intel ME version (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
