# Dasharo Compatibility: USB Camera

## Test cases

### CAM001.001 USB Camera (Ubuntu 20.04)

**Test description**

This test aims to verify that the integrated USB camera is initialized
correctly and can be accessed from the operating system

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk).
1. Install ffprobe: `sudo apt install ffmpeg`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a terminal window and run the following commands:

```
ffprobe /dev/video0
ffprobe /dev/video2
```

**Expected result**

1. The output from the first command should contain the lines:

```
Input #0, video4linux2,v4l2, from '/dev/video0':
    Stream #0:0: Video: rawvideo (YUY2 / 0x32595559), yuyv422, 640x480, 147456 kb/s, 30 fps, 30 tbr, 1000k tbn, 1000k tbc
```

1. The output from the second command should contain the lines:

```
Input #0, video4linux2,v4l2, from '/dev/video2':
    Stream #0:0: Video: rawvideo (Y800 / 0x30303859), gray, 640x360, 55296 kb/s, 30 fps, 30 tbr, 1000k tbn, 1000k tbc
```

### CAM001.002 USB Camera (Windows 10)

**Test description**

This test aims to verify that the integrated USB camera is initialized
correctly and can be accessed from the operating system

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 10

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware)
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer)
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation)
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk)

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open `Camera` app and note the result

**Expected result**

1. In the `Camera` app, an image from the integrated USB camera should be shown.
