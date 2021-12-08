# Dasharo Compatibility: Memtest

## Test cases

### MEM001.001 Memtest availability

**Test description**

This test aims to verify that the Memtest entry is available in DUT.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Check if `Payload [memtest]` is available in the boot menu.

**Expected result**

The `Payload [memtest]` option should be visible under `Select boot device:`.

### MEM001.002 Enter Memtest

**Test description**

This test aims to verify that the DUT enters the Memtest boot option.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Check if `Memtest86+` is available.

**Expected result**

The `Memtest86+` is visible at the top of the output.

### MEM001.003 Memtest stability

**Test description**

This test aims to verify that the Memtest starts does not hang under DUT.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**   

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Check if `State: - Running...` is available.

**Expected result**

The `State: - Running...` is visible after a few seconds and confirms that the 
the test is in progress.

### MEM001.004 Memtest refreshing

**Test description**

This test aims to verify that DUT refreshes Memtest properly.

**Test configuration data**

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `BOOT_MENU_ENTRY`.
5. Press the `l` key.
6. Check if `l` refreshes output.
7. Press the `L` key.
8. Check if `L` refreshes output.

**Expected result**

The `Memtest86+` is visible before and after pressing `l` and
`L`.

### MEM001.005 Memtest completing

**Test description**

This test aims to verify that DUT completes Memtest.

1. `BOOT_MENU_KEY` = `ESC`
2. `BOOT_MENU_STRING` = `Press ESC for boot menu`

**Test setup**

1. Proceed with the [Generic test setup: firmware](../generic-test-setup.md/#firmware).

**Test steps**

1. Power on the DUT.
2. Wait for boot until `BOOT_MENU_STRING` appears.
3. Press `BOOT_MENU_KEY` to enter the boot menu.
4. Select the key with a proper number for `Payload [memtest]`.
5. Make sure that `State: - Running...` is available.
6. Wait until `** Pass complete, no errors, press Esc to exit **` appears.

**Expected result**

After some time depending on DUT RAM memory capacity the 
`** Pass complete, no errors, press Esc to exit **` is visible.
