# Dasharo Performance: Custom fan curve

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

## CFC001.001 CPU fan

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly and the fan spins up and down
according to the defined values.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `lm-sensors` and `stress-ng` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command:

    ```bash
    stress-ng --cpu 16 --timeout 30m
    ```

1. Open the terminal window and run the following command to get the
   temperature:

    ```bash
    sensors | grep 'Package id 0'
    ```

1. In the terminal window run the following command to get the PWM value of the
   CPU fan:

    ```bash
    cat /sys/devices/LNXSYSTM:00/LNXSYBUS:00/17761776:00/hwmon/hwmon3/pwm1
    ```

1. Repeat steps 5-6 a couple of times.
1. Note the results.

**Expected result**

[Defined curve](https://github.com/Dasharo/ec/blob/d7a9890b4cc7915837dcef13bde5cc91d2ba1e0d/src/board/system76/galp5/board.mk#L40-L44)

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

expected_speed = ((30-25)/(65-0))*(30-0)+25 ≈ 27
actual_speed = 70/2.55 ≈ 27

expected_speed ≈ actual_speed which is correct.
