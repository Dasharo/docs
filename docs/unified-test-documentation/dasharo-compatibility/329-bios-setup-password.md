# Dasharo compatibility: BIOS setup password

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## PSW001.001 Check Password Setup option availability and default state

**Test description**

Check wether `User Password Management` option is avalible and default state.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Select `Dasharo System Features`.
1. Select `User Password Management`.
1. Check if below options are existing in submenu:
    - `Admin Password Status`
    - `Change Admin Password`

**Expected result**

1. All described options are avalible and navigating through menu doesn't cause
    any problems.

## PSW002.001 Check the mechanism of the password setting

**Test description**

Check wether the password changing mechanism works properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Select `Dasharo System Features`.
1. Select `User Password Management`.
1. Select `Change Admin Password`.
1. Set and confirm the password.
1. Restart DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Check if new password works.

**Expected result**

1. DUT after reboot and pressing `BOOT_MENU_KEY` demands password, and newly
    setted one works properly.

## PSW003.001 Attempt to log in with a correct password

**Test description**

Check wether proper password unlocks boot menu.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Use password to unlock boot menu and note the result.

**Expected result**

1. Menu unlocks properly and options are avalible.

## PSW004.001 Attempt to log in with an incorrect password

**Test description**

Check wether incorrect password is not unlocking boot menu.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.
1. Try to use incorrect password 3 times and note the results.

**Expected result**

1. After every attempt DUT informs that password is incorrect and is not
    unlocking boot menu.

1. After 3 failures DUT reboots.

## PSW005.001 Attempt to block password functionality

**Test description**

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.

**Expected result**

## PSW006.001 Attempt to set non-compilant password

**Test description**

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display boot menu.

**Expected result**
