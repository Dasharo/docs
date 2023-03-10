# Dasharo Security: BIOS Setup password

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

## PSW001.001 Check Password Setup option availability and default state

**Test description**

This test aims to verify whether `User Password Management` submenu is
available and, whether all options in the submenu have correct default state.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `User Password Management` submenu using the arrow keys and Enter.
1. Verify the `Admin Password Status` field.
1. Verify the `Change Admin Password` field.

**Expected result**

1. The `Admin Password Status` field should be present and indicate, that
    password setup is currently disabled.
1. The `Change Admin Password` field should be present. After passing the
    cursor over this option, information about password minimum terms and
    conditions should be displayed.

## PSW002.001 Password setting mechanism correctness checking

**Test description**

This test aims to verify whether `Change Admin Password` option works
correctly - after restarting the device and trying to enter the `Setup Menu`,
a window to enter the password will be displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `User Password Management` submenu using the arrow keys and Enter.
1. Select the option `Change Admin Password` by using the arrow keys and Enter.
1. Set the password in accordance with the password minimum terms and
    conditions.
1. Restart the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Verify if the password window will be displayed.

**Expected result**

The password window should be displayed correctly.

## PSW003.001 Attempt to log in with a correct password

**Test description**

This test aims to verify whether, after entering the correct Setup password,
the `Setup menu` will be displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the correct password and note the result.

**Expected result**

After typing in the correct password `Setup menu` should be displayed.

## PSW004.001 Attempt to log in with an incorrect password

**Test description**

This test aims to verify whether, after entering the incorrect Setup password,
the message about the demand for re-entering the password will be displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display the boot menu.
1. Enter the incorrect password and note the result.

**Expected result**

After typing in the incorrect password the message about the demand for
re-entering the password will be displayed.

## PSW005.001 Attempt to log in with an incorrect password 3 times

**Test description**

This test aims to verify whether, after entering the incorrect Setup password
three times, the message about demand for rebooting the DUT will be displayed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT
1. Press `BOOT_MENU_KEY` key to display the boot menu.
1. Enter the incorrect password three times and note the result.

**Expected result**

After typing in the incorrect password three times the message about the demand
for rebooting the DUT will be displayed.

## PSW006.001 Attempt to turn off setup password functionality

**Test description**

This test aims to verify whether there is a possibility to turn off the Setup
Password functionality by entering empty password.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `User Password Management` submenu using the arrow keys and Enter.
1. Select the option `Change Admin Password` by using the arrow keys and Enter.
1. Set the empty password.
1. Restart the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Verify if the password window will be displayed.

**Expected result**

1. Password window should not be displayed.
1. The DUT should boot into `Setup Menu`.

## PSW007.001 Attempt to set non-compilant password

**Test description**

This test aims to verify whether the attempt to set a non-compilant password
will be rejected.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `User Password Management` submenu using the arrow keys and Enter.
1. Select the option `Change Admin Password` by using the arrow keys and Enter.
1. Set the password in non-accordance with the password minimum terms and
    conditions.

**Expected result**

1. The window with the information that requested password is not strong
    enough should be displayed.
1. The attempt to set the password should be rejected.

## PSW008.001 Attempt to set old password

**Test description**

BIOS setup password feature has been equipped with an additional functionality
that prevents re-setting one of the last 5 access passwords. This test aims to
verify whether the attempt to set old password again will be rejected.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Press `SETUP_MENU_KEY` to enter the `Setup Menu`.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `User Password Management` submenu using the arrow keys and Enter.
1. Select the option `Change Admin Password` by using the arrow keys and Enter.
1. Set the password identically as one of the 5 latest passwords.

**Expected result**

1. The window with the information that requested password has been found in
    the passwords history should be displayed.
1. The attempt to set the password should be rejected.
