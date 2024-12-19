# Dasharo Performance: Custom fan curve

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

## CFC001.001 Custom fan curve silent profile measure (Ubuntu)

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly in silent profile and the fan spins
up and down according to the defined values.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `stress-ng` on the DUT.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Verify that the `Fan profile` field is set to `Silent` - if not, using the
   arrow keys and `Enter`, choose the `Silent` option.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command:

    ```bash
    stress-ng --cpu 16 --timeout 30m
    ```

1. Open the terminal window and run the following command to get the
   temperature:

    ```bash
    cat /sys/devices/LNXSYSTM:00/LNXSYBUS:00/17761776:00/hwmon/hwmon3/temp1_input
    ```

    > The last three digits of the output are the value of the number after the
      decimal point. Example output `47000` means 47°C.

1. In the terminal window run the following command to get the PWM value of the
   CPU fan:

    ```bash
    cat /sys/devices/LNXSYSTM:00/LNXSYBUS:00/17761776:00/hwmon/hwmon3/pwm1
    ```

1. Repeat steps 13-14 a couple of times.
1. Note the results.

**Expected result**

[Silent fan profile](https://docs.dasharo.com/unified/novacustom/features/)

Keep in mind that the EC firmware is smoothing, i.e. the fans will enter the
target speed with a delay.

The algorithm by which the EC calculates the speed is as follows:

* If the temperature is below the first one defined in the curve, set the speed
  to 0.
* If the temperature is above the last defined curve, set the maximum speed.
* If the temperature is equal to one of the temperatures of the points on the
  curve, set the speed from that point on the curve
* If the temperature is between points on the curve:

    ```bash
    slope = (right_point_speed - left_point_speed)/right_point_temperature - left_point_temperature)
    speed = slope*(temperature - left_point_temperature) + left_point_speed
    ```

Divide the PWM value by 2.55 to get the percentage to compare.

Example check for 30°C and 70 PWM values:

    ```text
    expected_speed = ((30-25)/(65-0))*(30-0)+25 ≈ 27
    actual_speed = 70/2.55 ≈ 27
    ```

Values `expected_speed` and `actual_speed` are strongly similar. This means
that the fan control is set correctly.

## CFC002.001 Custom fan curve performance profile measure (Ubuntu)

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly in the performance profile and the
fan spins up and down according to the defined values.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `stress-ng` on the DUT.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Verify that the `Fan profile` field is set to `Performance` - if not, using
   the arrow keys and `Enter`, choose the `Performance` option.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command:

    ```bash
    stress-ng --cpu 16 --timeout 30m
    ```

1. Open the terminal window and run the following command to get the
   temperature:

    ```bash
    cat /sys/devices/LNXSYSTM:00/LNXSYBUS:00/17761776:00/hwmon/hwmon3/temp1_input
    ```

    > The last three digits of the output are the value of the number after the
      decimal point. Example output `47000` means 47°C.

1. In the terminal window run the following command to get the PWM value of the
   CPU fan:

    ```bash
    cat /sys/devices/LNXSYSTM:00/LNXSYBUS:00/17761776:00/hwmon/hwmon3/pwm1
    ```

1. Repeat steps 13-14 a couple of times.
1. Note the results.

**Expected result**

[Performance fan profile](https://docs.dasharo.com/unified/novacustom/features/)

Keep in mind that the EC firmware is smoothing, i.e. the fans will enter the
target speed with a delay.

The algorithm by which the EC calculates the speed is as follows:

* If the temperature is below the first one defined in the curve, set the speed
  to 0.
* If the temperature is above the last defined curve, set the maximum speed.
* If the temperature is equal to one of the temperatures of the points on the
  curve, set the speed from that point on the curve
* If the temperature is between points on the curve:

    ```bash
    slope = (right_point_speed - left_point_speed)/right_point_temperature - left_point_temperature)
    speed = slope*(temperature - left_point_temperature) + left_point_speed
    ```

Divide the PWM value by 2.55 to get the percentage to compare.

Example check for 30°C and 79 PWM values:

    ```text
    expected_speed = ((35-25)/(55-0))*(35-0)+25 ≈ 31
    actual_speed = 79/2.55 ≈ 31
    ```

Values `expected_speed` and `actual_speed` are strongly similar. This means
that the fan control is set correctly.

## CFC003.001 Custom fan curve OFF profile measure (Ubuntu)

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly in the OFF profile and the
fan does not spin, or barely spins, which depends on the type of the fan.

The test requires the device to use have the IT87 EC. For example Protectli
VP66xx, VP32xx and VP2420.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `stress-ng` on the DUT.
1. Install `lm-sensors` on the DUT

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
   Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `Power Management Options` submenu.
1. Verify that the `Fan profile` field is set to `OFF` - if not, using
   the arrow keys and `Enter`, choose the `Performance` option.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command to load the EC sensor
kernel module:

    ```bash
    sudo modprobe it87 force_id=0x8786
    ```

1. Open the terminal window and run the following command to run a stress test
on the CPU:

    ```bash
    stress-ng --cpu 16 --timeout 30m
    ```

1. Open the terminal window and run the following command to get the
   temperature and fans' RPM:

    ```bash
    watch -n1 "sensors it8786-isa-0a20 | grep -E 'fan|temp1'"
    ```

1. Note the results.

**Expected result**

The fan PWM should be equal to `0` or be low and don't increase with temperature
, for example ~`250` RPM. This depends on the model of the fan used.
