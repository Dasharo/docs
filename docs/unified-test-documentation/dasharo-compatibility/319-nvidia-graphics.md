
# Dasharo Compatibility: NVIDIA Graphics support

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

## NVI001.201 NVIDIA Graphics detect (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NVI001.301 NVIDIA Graphics detect (Windows)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NVI002.201 NVIDIA Graphics power management (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## NVI002.301 NVIDIA Graphics power management (Windows)

**Test description**

This test aims to verify that the NVIDIA graphics power management is functional
and the card powers on only while it's used.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the driver for the graphics card (GTX 1650) from
    [the official page](https://www.nvidia.com/).
1. Download and extract `gputest` from [Geeks3D](https://geeks3d.com/gputest).

**Test steps**

1. Open the NVIDIA Control Panel window.
1. In the menu bar, open the Desktop menu.
1. Enable the `Display GPU Activity Icon in Notification Area` option.
1. Open the system tray located in the bottom right corner of the screen
   and locate the GPU activity icon:

![GPU activity icon](../../images/gpu_activity_win10.jpg)

1. Open the previously extracted gputest directory and open the `GPUTest_GUI`
   application.
1. Click on the `Run stress test` button to start the test application.
1. Locate the GPU activity icon and check that it indicates that the GPU has
   powered on.
1. Close the test application.
1. Locate the GPU activity icon and check that it indicates that the GPU has
   powered off again.

**Expected result**

1. The GPU activity icon should indicate that the GPU is OFF when no application
   is using the GPU.
1. The GPU activity icon should indicate that the GPU is ON when an application
   is using the GPU.
1. The GPU activity icon should indicate that the GPU is OFF again after the
   test application is closed.
