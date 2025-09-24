# Dasharo Security: Early Boot DMA Protection

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

## EDP001.001 Enable early Boot DMA Protection support

**Test description**

This test aims to verify that the early boot DMA protection might be activated.
If the functionality is enabled, the protection against malicious PCIe devices
DMA transactions by configuring VT-D/IOMMU should be active.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Enable early DMA protection` field is checked - if not, use
    `Spacebar` to change option settings.
1. Save the changes using `F10`, and exit from the menu using `Esc`.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY`  to enter Boot Menu.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

   ```bash
   sudo ./cbmem -1
   ```

1. Note the result.

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

## EDP002.001 Disable early Boot DMA Protection support

**Test description**

This test aims to verify that the early boot DMA protection might be
deactivated. If the functionality is disabled, the protection against malicious
PCIe devices DMA transactions by configuring VT-D/IOMMU should be non-active.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. While booting, press the `SETUP_MENU_KEY` to enter Setup Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Dasharo Security Options` submenu.
1. Verify that the `Enable early DMA protection` option is checked - if so, use
    `Spacebar` to change option settings.
1. Save the changes using `F10`, and exit from the menu using `Esc`.
1. Reboot the device.
1. While booting, press `BOOT_MENU_KEY`  to enter Boot Menu.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

   ```bash
   sudo ./cbmem -1
   ```

1. Note the result.

**Expected result**

The output of the cbmem utility should not contain the information, that the
DMA protection has been set up.

Example output with unwanted results:

```txt
[DEBUG]  VT-d @ 0xfed91000, version 5.0
[INFO ]  Setting DMA protection [0x0 - 0x46c00000]
[INFO ]  Setting DMA protection [0x100000000 - 0x00000008afc00000]
[INFO ]  Successfully enabled VT-d PMR DMA protection
```
