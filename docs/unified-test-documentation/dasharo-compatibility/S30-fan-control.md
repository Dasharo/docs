# Dasharo Compatibility: custom fan curve

## Test cases

### FAN001.001 Custom fan curve: CPU fan

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly and the fan spins up and down
according to the defined values.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BOOT_MENU_KEY` = `F7`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk)
1. Install `lm-sensors` and `stress-ng` on the DUT

**Test steps**

1. Open the terminal window and execute the following command:

        sensors | grep 'Package id 0'

1. Verify using `sensors` that the temperature is below 40°C
1. If the temperature is above 40, enable fan turbo mode (Fn + 1) until it cools
   down
1. Flip the laptop over and check if the CPU fan (located under the Backspace
   key) is spinning
1. In the terminal window, run following command:

        stress-ng -c 8

1. Verify using `sensors` that the temperature increases above 40
1. Flip the laptop over and check if the CPU fan is spinning

**Expected result**

1. The fan should not be spinning while the temperature is below 40 degrees
1. The fan should be spinning while the temperature is above 40 degrees

### FAN002.001 Custom fan curve: GPU fan (NV41MB)

**Test description**

The fan has been configured to follow a custom curve. This test aims to verify
that the fan curve is configured correctly and the fan spins up and down
according to the defined values.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `BOOT_MENU_KEY` = `F7`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#ps-installer)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk)
1. Install `nvidia-smi` and `mesa-utils` on the DUT

**Test steps**

1. Open the terminal window and execute the following command:

        watch -n1 nvidia-smi

1. Verify using that the temperature is below 40°C
1. If the temperature is above 40, enable fan turbo mode (Fn + 1) until it cools
   down
1. Flip the laptop over and check if the GPU fan (located under the Escape
   key) is spinning
1. In another terminal window, run following command:

        _NV_PRIME_RENDER_OFFLOAD=1 __GLX_VENDOR_LIBRARY_NAME=nvidia __GL_SYNC_TO_VBLANK=0 glxgears

1. Verify that the temperature increases above 40
1. Flip the laptop over and check if the GPU fan is spinning

**Expected result**

1. The fan should not be spinning while the temperature is below 40 degrees
1. The fan should be spinning while the temperature is above 40 degrees
