# Dasharo Security: Early Boot DMA Protection

## EDP001.001 Early Boot DMA Protection support

**Test description**

Early Boot DMA protection feature enable Dasharo firmware to configure
VT-D/IOMMU to protect against malicious PCIe devices DMA transactions.
The test case verifies the DMA protection has been configured properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Disable Secure Boot.
1. Download `cbmem` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open a terminal window and execute the following command:

   ```bash
   sudo ./cbmem -1
   ```

5. Note the result.

**Expected result**

The output of the cbmem utility should contain the information, that the
DMA protection has been set up.

Example output:

```txt
[DEBUG]  VT-d @ 0xfed91000, version 5.0
[INFO ]  Setting DMA protection [0x0 - 0x46c00000]
[INFO ]  Setting DMA protection [0x100000000 - 0x00000008afc00000]
[INFO ]  Successfully enabled VT-d PMR DMA protection
```

Note the memory address ranges in square braces may differ per DUT.

If the DUT does not support serial redirection, it is also possible to
investigate UEFI Payload logs if VT-d is being used properly. Check for
following output:

```txt
EnableDmar
>>>>>>EnableDmar() for engine [0] BAR [0xFED90000]
RootEntryTable 0x4518C000
EnableDmar: waiting for RTPS bit to be set...
Set GCMD_REG bits 0x40000000.
EnableDmar: Waiting B_GSTS_REG_TE ...
Set GCMD_REG bits 0x80000000.
VTD (0) enabled!<<<<<<
>>>>>>EnableDmar() for engine [1] BAR [0xFED91000]
RootEntryTable 0x44FDD000
EnableDmar: waiting for RTPS bit to be set...
Set GCMD_REG bits 0x40000000.
EnableDmar: Waiting B_GSTS_REG_TE ...
Set GCMD_REG bits 0x80000000.
VTD (1) enabled!<<<<<<
DisablePmr
Pmr(0) not enabled
Pmr(1) disabled
```

The most important are `VTD (0) enabled!<<<<<<` and `VTD (1) enabled!<<<<<<`.
Also the following:

```txt
DisablePmr
Pmr(0) not enabled
Pmr(1) disabled
```

Indicate that VT-D engine 1 had PMR enabled earlier, which is expected.

If all above conditions are met, test pass.

## EDP002.001 Disable Early Boot DMA Protection (Firmware)

**Test description**

This test aims to verify if Early Boot DMA Protection can be disabled.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `SETUP_MENU_KEY` = F2

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Enter the `-----------` menu option.
1. Hover on checkbox next to `----------------` option, and make sure
    that `X` sign is NOT present between square brackets - `[ ]`. Use `Spacebar`
    to toggle.
1. Save using `F10`, and exit using `Esc`.
1. Reboot the device.
<!-- 1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `One Time Boot` menu option. -->

**Expected result**

--------------

## EDP003.001 Enable Early Boot DMA Protection (Firmware)

**Test description**

This test aims to verify if Early Boot DMA Protection can be enabled.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `SETUP_MENU_KEY` = F2

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu option.
1. Enter the `-----------` menu option.
1. Hover on checkbox next to `----------------` option, and make sure
    that `X` sign is present between square brackets - `[X]`. Use `Spacebar`
    to toggle.
1. Save using `F10`, and exit using `Esc`.
1. Reboot the device.
<!-- 1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `One Time Boot` menu option. -->

**Expected result**

--------------
