# Dasharo Compatibility: USB A and C Always On ports

## Test cases common documentation

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
2. Refer to [docs.dasharo.com/variants](https://docs.dasharo.com/variants/overview/)
 and identify USB A  & USB C ports that are affected and not affected by
 "USB power and charging" option.
3. Let's define TIANOCORE_STRING as "ENTER to boot directly" (however, this is platform-dependant)

## USC001.001 "USB power and charging" option is present

**Test description**

This test aims to verify that "USB power and charging" option is present in
setup menu.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Note, if "USB ports power and charging" menu option is present
6. Enter value submenu, to check available values, but don't change anything.
7. Turn off DUT

**Expected results**

"USB ports power and charging" menu option present in Power Management Options
submenu, available option values: "While System is On", "Always On".

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC002.001 Power IS delivered thru always-on USB A ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to "
Always On " keeps electrical power supply on selected USB A ports, after DUT is
power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "Always On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB A ports marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

On each USB A port marked as "Always On USB", power meter should be working on
tested port supply, showing voltage >= 5.0V

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC003.001 Power IS delivered thru always-on USB C ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to "
Always On " keeps electrical power supply on selected USB C ports, after DUT is
power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "Always On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB C ports marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

On each USB C port marked as "Always On USB", power meter should be working on
tested port supply, showing voltage >= 5.0V

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC004.001 Power IS NOT delivered thru always-on USB A ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to
"While System is On" is disabling electrical power supply on selected USB A
ports, after DUT is power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "While System is On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB A ports marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

USB power meter not working (or, in case of DUT-independent power supply,
showing voltage close to 0V)

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC005.001 Power IS NOT delivered thru always-on USB C ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to
"While System is On" is disabling electrical power supply on selected USB A
ports, after DUT is power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "While System is On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB C ports marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

USB power meter not working (or, in case of DUT-independent power supply,
showing voltage close to 0V)

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC006.001 Power IS NOT delivered thru regular USB A ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to
"Always On" is NOT enabling electrical power supply to USB A ports that are
NOT marked as "Always On USB", after DUT is power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.
3. Make sure that there are USB A ports, that are not marked as "Always On USB",
 otherwise skip this test case.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "Always On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB A ports NOT marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

USB power meter not working (or, in case of DUT-independent power supply,
showing voltage close to 0V)

**Test configuration data**

1. `FIRMWARE` = Dasharo

## USC007.001 Power IS NOT delivered thru regular USB C ports

**Test description**

This test verifies, if setting "USB ports power and charging" menu option to
"Always On" is NOT enabling electrical power supply to USB C ports that are
NOT marked as "Always On USB", after DUT is power off.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Check if available USB power meter works without any additional
 devices attached.
3. Make sure that there are USB C ports, that are not marked as "Always On USB",
 otherwise skip this test case.

**Test steps**

1. Turn on DUT
2. Press F2 to enter setup menu
3. Enter Dasharo System Features submenu
4. Enter Power Management Options submenu
5. Set value of "USB ports power and charging" to "Always On"
6. Save setup configuration with F10 key, confirm with Y
7. Power off DUT
8. Power on DUT (this is when setup change takes effect)
9. Wait until TIANOCORE_STRING appears on screen
10. Power off DUT
11. Verify state of all USB C ports NOT marked in "Hardware configuration matrix"
as "Always On USB" using USB power meter

**Expected results**

USB power meter not working (or, in case of DUT-independent power supply,
showing voltage close to 0V)

**Test configuration data**

1. `FIRMWARE` = Dasharo
