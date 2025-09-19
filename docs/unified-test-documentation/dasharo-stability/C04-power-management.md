# Dasharo Stability: Power Management

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

## SPM001.001 2x S0ix suspend cycle (Battery) (Ubuntu)

**Test description**

This test aims to verify the stability of the S0ix / Modern Standby sleep state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to Idle (S0ix)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM001.002 2x S0ix suspend cycle (Battery) (Windows)

**Test description**

This test aims to verify the stability of the S0ix / Modern Standby sleep state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to Idle (S0ix)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM002.001 2x S0ix suspend cycle (AC) (Ubuntu)

**Test description**

This test aims to verify the stability of the S0ix / Modern Standby sleep state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to Idle (S0ix)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM002.002 2x S0ix suspend cycle (AC) (Windows)

**Test description**

This test aims to verify the stability of the S0ix / Modern Standby sleep state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to Idle (S0ix)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM003.001 2x S3 suspend cycle (Battery) (Ubuntu)

**Test description**

This test aims to verify the stability of the S3 / sleep-to-ram state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to RAM (S3)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM003.002 2x S3 suspend cycle (Battery) (Windows)

**Test description**

This test aims to verify the stability of the S3 / sleep-to-ram state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to RAM (S3)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM004.001 2x S3 suspend cycle (AC) (Ubuntu)

**Test description**

This test aims to verify the stability of the S3 / sleep-to-ram state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to RAM (S3)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM004.002 2x S3 suspend cycle (AC) (Windows)

**Test description**

This test aims to verify the stability of the S3 / sleep-to-ram state.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the setup menu.
1. Ensure that the sleep mode option is set to `Suspend to RAM (S3)`
1. Save and exit the setup menu.
1. Boot into OS.
1. Log into the system.
1. Put the DUT to sleep using the OS's UI
1. Ensure the sleep mode has been entered (i.e. power LED blinking or
   "breathing", depending on platform)
1. Wait at least 60 seconds
1. Wake up the DUT
1. Verify basic functionality remains functional
1. Repeat steps 7-11.

**Expected result**

Sleep mode should be entered correctly on each attempt.

Waking up should proceed without issues on each attempt. All basic functionality
(i.e. builtin keyboard, touchpad, display etc) should keep working.

## SPM005.001 2x warmboot cycle (Battery) (Ubuntu)

**Test description**

This test aims to verify the stability of the warmboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Shut down the DUT via the OS's UI.
1. Ensure DUT has shut down completely (i.e. Power LED turns off or changes
   color)
1. Wait least 60 seconds
1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Verify basic functionality remains functional
1. Repeat steps 4-10.

**Expected result**

Shutdown should proceed correctly on each attempt.

Powering on should proceed without issues on each attempt. All basic
functionality (i.e. builtin keyboard, touchpad, display etc) should keep
working.

## SPM005.002 2x warmboot cycle (Battery) (Windows)

**Test description**

This test aims to verify the stability of the warmboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Shut down the DUT via the OS's UI.
1. Ensure DUT has shut down completely (i.e. Power LED turns off or changes
   color)
1. Wait least 60 seconds
1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Verify basic functionality remains functional
1. Repeat steps 4-10.

**Expected result**

Shutdown should proceed correctly on each attempt.

Powering on should proceed without issues on each attempt. All basic
functionality (i.e. builtin keyboard, touchpad, display etc) should keep
working.

## SPM006.001 2x warmboot cycle (AC) (Ubuntu)

**Test description**

This test aims to verify the stability of the warmboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Shut down the DUT via the OS's UI.
1. Ensure DUT has shut down completely (i.e. Power LED turns off or changes
   color)
1. Wait least 60 seconds
1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Verify basic functionality remains functional
1. Repeat steps 4-10.

**Expected result**

Shutdown should proceed correctly on each attempt.

Powering on should proceed without issues on each attempt. All basic
functionality (i.e. builtin keyboard, touchpad, display etc) should keep
working.

## SPM006.002 2x warmboot cycle (AC) (Windows)

**Test description**

This test aims to verify the stability of the warmboot.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Shut down the DUT via the OS's UI.
1. Ensure DUT has shut down completely (i.e. Power LED turns off or changes
   color)
1. Wait least 60 seconds
1. Power on the DUT.
1. Boot into OS.
1. Log into the system.
1. Verify basic functionality remains functional
1. Repeat steps 4-10.

**Expected result**

Shutdown should proceed correctly on each attempt.

Powering on should proceed without issues on each attempt. All basic
functionality (i.e. builtin keyboard, touchpad, display etc) should keep
working.
