# Dasharo Compatibility: Fan speed

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

## FAN001.001 CPU fan

**Test description**

This test aims to verify that the CPU fan RPM value is available to read.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `lm-sensors` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. In the terminal window run the following command to get the RPM value of the
   CPU fan:

    ```bash
    sensors | grep "CPU fan"
    ```

1. Note the results.

**Expected result**

The CPU fan RPM value is displayed and isn't zero.

Example output:

```bash
CPU fan:     4347 RPM
```

## FAN002.001 GPU fan

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly and the fan spins up and down
according to the defined values.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `nvidia-smi` and `mesa-utils` on the DUT.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal window and execute the following command:

    ```bash
    watch -n1 nvidia-smi
    ```

1. Verify using that the temperature is below 40°C.
1. If the temperature is above 40, enable the fan turbo mode (Fn + 1) until it
   cools down.
1. Flip the laptop over and check if the GPU fan (located under the Escape
   key) is spinning.
1. In another terminal window, run the following command:

    ```bash
    _NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __GL_SYNC_TO_VBLANK=0 glxgears
    ```

1. Verify that the temperature increases above 40.
1. Flip the laptop over and check if the GPU fan is spinning.

**Expected result**

1. The fan should not be spinning while the temperature is below 40 degrees.
1. The fan should be spinning while the temperature is above 40 degrees.
