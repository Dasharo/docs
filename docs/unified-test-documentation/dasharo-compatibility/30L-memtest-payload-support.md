# Dasharo Compatibility: Memtest payload support

## MEM001.001 Memtest availability

**Test description**

This test aims to verify that the Memtest entry is available in DUT boot
    menu.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `Payload [memtest]` is available in the boot menu.

**Expected result**

The `Payload [memtest]` option should be visible as the one of boot menu options.

## MEM002.001 Enter Memtest

**Test description**

This test aims to verify that the DUT enters the Memtestboot option.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Check if `Memtest86+` is available.

**Expected result**

The `Memtest86+` is visible at the top of the output.

## MEM003.001 Memtest stability

**Test description**

This test aims to verify that the Memtest starts does not hang under DUT.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Check if `State: - Running...` is available.

**Expected result**

The `State: - Running...` is visible after a few seconds and confirms that the
the test is in progress.

## MEM004.001 Memtest refreshing by 'L' key

**Test description**

This test aims to verify that DUT refreshes Memtest properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `BOOT_MENU_ENTRY`.
5. Press the `L` key.
6. Check if `L` refreshes output.

**Expected result**

The `Memtest86+` is visible before and after pressing `L`.

## MEM005.001 Memtest refreshing by 'l' key

**Test description**

This test aims to verify that DUT refreshes Memtest properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `BOOT_MENU_ENTRY`.
5. Press the `l` key.
6. Check if `l` refreshes output.

**Expected result**

The `Memtest86+` is visible before and after pressing `l`.

## MEM006.001 Memtest completing

**Test description**

This test aims to verify that DUT completes Memtest.

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Make sure that `State: - Running...` is available.
6. Wait until `** Pass complete, no errors, press Esc to exit **` appears.

**Expected result**

After the test completes without any errors
`** Pass complete, no errors, press Esc to exit **` message is visible on the
bottom of the screen.
