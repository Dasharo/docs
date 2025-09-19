# Dasharo Performance: Custom fan curve

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

## CFC001.001 Custom fan curve silent profile measure (Ubuntu)

**Test description**

This test aims to verify that the fan curve is configured correctly in silent
profile and the fan spins up and down according to the defined values.

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
    stress-ng --cpu $(nproc --all) --cpu-load 100 --timeout 1m
    ```

1. Make a couple of measurements of the temperature and fan speeds
   in a [device specific way](#measuring-the-temperature-and-fan-speeds).
   The `--cpu-load` parameter specifies the approximate percentage usage of
   the cpu. Change it to values in range \[1, 100\] to measure the fan speeds
   in all the working points of the fan curve.
1. Note the results.

**Expected result**
The values of CPU temperature and fan speeds should match the
[device specific instructions](#verifying-the-temperature-and-fan-speeds)
on verifying the `Silent` fan curve.

## CFC002.001 Custom fan curve performance profile measure (Ubuntu)

**Test description**

This test aims to verify that the fan curve is configured correctly in the
performance profile and the fan spins up and down according to the defined
values.

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
    stress-ng --cpu $(nproc --all) --cpu-load 100 --timeout 1m
    ```

1. Make a couple of measurements of the temperature and fan speeds
   in a [device specific way](#measuring-the-temperature-and-fan-speeds).
   The `--cpu-load` parameter specifies the approximate percentage usage of
   the cpu. Change it to values in range \[1, 100\] to measure the fan speeds
   in all the working points of the fan curve.
1. Note the results.

**Expected result**
The values of CPU temperature and fan speeds should match the
[device specific instructions](#verifying-the-temperature-and-fan-speeds)
on verifying the `Performance` fan curve.

## CFC003.001 Custom fan curve OFF profile measure (Ubuntu)

**Test description**

This test aims to verify that the fan curve is configured correctly in the OFF
profile and the fan does not spin, or barely spins, which depends on the type
of the fan.

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
1. Verify that the `Fan profile` field is set to `Off` - if not, using
   the arrow keys and `Enter`, choose the `Off` option.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and run the following command:

    ```bash
    stress-ng --cpu $(nproc --all) --cpu-load 100 --timeout 1m
    ```

1. Make a couple of measurements of the temperature and fan speeds
   in a [device specific way](#measuring-the-temperature-and-fan-speeds).
   The `--cpu-load` parameter specifies the approximate percentage usage of
   the cpu. Change it to values in range \[1, 100\] to measure the fan speeds
   in all the working points of the fan curve.
1. Note the results.

**Expected result**
The values of CPU temperature and fan speeds should match the
[device specific instructions](#verifying-the-temperature-and-fan-speeds)
on verifying the `Off` fan curve.

## Measuring the temperature and fan speeds

=== "Protectli"
    === "VP66xx & VP32xx"
        1. Run the following command to load the kernel module required for
           measuring the fan RPM
           ```bash
           sudo modprobe it87 force_id=0x8786
           ```
        1. Run the following command to detect available sensors
           ```bash
           sudo sensors-detect
           ```
        1. Run the following command to read the temperature and RPM
           ```bash
           watch -n1 "sensors it8786-isa-* | grep -E 'fan|temp1'"
           ```

## Verifying the temperature and fan speeds

=== "Protectli"
    === "VP66xx"
        The fans have a minimal RPM of `~200 RPM`, and a maximum of up to
        `~3200 RPM`. When in `off` state they still spin at `~200 RPM`.

        === "Silent"
            The fans:

            - start spinning up from the minimal RPM at 50 degrees
              and slow down to the minimal RPM at 40 degrees (hysteresis)
            - spin up proportionally to the CPU temperature, reaching the
              maximum RPM at 85 degrees

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Silent\" fan curve for Protectli VP66xx",
               "data": {
                     "values": [
                     {"t1": 0, "r": 200, "h": 0}, {"t1": 40, "r": 200, "h": 0},
                     {"t1": 85, "r": 3200, "h": 0}, {"t1": 100, "r": 3200, "h": 0},

                     {"t1": 0, "r": 200, "h": 1}, {"t1": 50, "r": 200, "h": 1},
                     {"t1": 85, "r": 3200, "h": 1}, {"t1": 100, "r": 3200, "h": 1}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {"field": "r", "type": "quantitative", "title": "Fan speed [RPM]"},
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```

        === "Performance"
            The fans:

            - start spinning up from the minimal RPM at 40 degrees
              and slow down to the minimal RPM at 30 degrees (hysteresis)
            - spin up proportionally to the CPU temperature, reaching the
              maximum RPM at 75 degrees

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Performance\" fan curve for Protectli VP66xx",
               "data": {
                     "values": [
                     {"t1": 0, "r": 200, "h": 0}, {"t1": 30, "r": 200, "h": 0},
                     {"t1": 75, "r": 3200, "h": 0}, {"t1": 100, "r": 3200, "h": 0},

                     {"t1": 0, "r": 200, "h": 1}, {"t1": 40, "r": 200, "h": 1},
                     {"t1": 75, "r": 3200, "h": 1}, {"t1": 100, "r": 3200, "h": 1}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {"field": "r", "type": "quantitative", "title": "Fan speed [RPM]"},
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```

        === "Off"
            The fan RPM value should be constant and oscillate around the minimum
            of `~200 RPM` regardless of the CPU temperature.

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Off\" fan curve for Protectli VP66xx",

               "data": {
                     "values": [
                        {"t1": 0, "r": 200, "h": 0}, {"t1": 100, "r": 200, "h": 0}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {
                        "field": "r",
                        "type": "quantitative",
                        "title": "Fan speed [RPM]",
                        "scale": {"domain": [0, 300]}
                     },
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```

    === "VP32xx"
        The fan from the modular extension bay have a minimal RPM of `0 RPM`,
        and a maximum up to `~2100 RPM`.
        When in `off` state they stop spinning and remain at constant `0 RPM`.

        === "Silent"
            The fans:

            - start spinning at 50 degrees and stop spinning at 40 degrees
              (hysteresis)
            - spin up proportionally to the CPU temperature, reaching the
              maximum RPM at 85 degrees

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Silent\" fan curve for Protectli VP66xx",
               "data": {
                     "values": [
                     {"t1": 0, "r": 0, "h": 0}, {"t1": 40, "r": 0, "h": 0},
                     {"t1": 85, "r": 2100, "h": 0}, {"t1": 100, "r": 2100, "h": 0},

                     {"t1": 0, "r": 0, "h": 1}, {"t1": 50, "r": 0, "h": 1},
                     {"t1": 85, "r": 2100, "h": 1}, {"t1": 100, "r": 2100, "h": 1}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {
                        "field": "r",
                        "type": "quantitative",
                        "title": "Fan speed [RPM]",
                        "scale": {"domain": [-100, 2200]}
                     },
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```

        === "Performance"
            The fans:

            - start spinning at 40 degrees and stop spinning at 30 degrees
              (hysteresis)
            - spin up proportionally to the CPU temperature, reaching the
              maximum RPM at 75 degrees

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Performance\" fan curve for Protectli VP66xx",
               "data": {
                     "values": [
                     {"t1": 0, "r": 0, "h": 0}, {"t1": 30, "r": 0, "h": 0},
                     {"t1": 75, "r": 2100, "h": 0}, {"t1": 100, "r": 2100, "h": 0},

                     {"t1": 0, "r": 0, "h": 1}, {"t1": 40, "r": 0, "h": 1},
                     {"t1": 75, "r": 2100, "h": 1}, {"t1": 100, "r": 2100, "h": 1}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {
                        "field": "r",
                        "type": "quantitative",
                        "title": "Fan speed [RPM]",
                        "scale": {"domain": [-100, 2200]}
                     },
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```

        === "Off"
            The fan RPM value should be constant at the minimum of `0 RPM`
            regardless of the CPU temperature.

            ```vegalite
            {
               "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
               "title": "The \"Off\" fan curve for Protectli VP66xx",

               "data": {
                     "values": [
                        {"t1": 0, "r": 0, "h": 0}, {"t1": 100, "r": 0, "h": 0}
                     ]
               },
               "mark": {"type": "line", "tooltip": true},
               "encoding": {
                     "x": {"field": "t1", "type": "quantitative", "title": "CPU Temperature [°C]"},
                     "y": {
                        "field": "r",
                        "type": "quantitative",
                        "title": "Fan speed [RPM]",
                        "scale": {"domain": [-100, 100]}
                     },
                     "color": {"field": "h", "type": "nominal", "legend": null}
               }
            }
            ```
