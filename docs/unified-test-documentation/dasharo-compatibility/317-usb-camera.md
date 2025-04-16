# Dasharo Compatibility: USB Camera

## CAM001.201 USB Camera (Ubuntu)

**Test description**

This test aims to verify that the integrated USB camera is initialized
correctly and can be accessed from the operating system

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).
1. Install ffprobe: `sudo apt install ffmpeg`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following commands:

```bash
ffprobe /dev/video0
ffprobe /dev/video2
```

**Expected result**

1. The output from the first command should contain the lines:

    ```bash
    Input #0, video4linux2,v4l2, from '/dev/video0':
        Stream #0:0: Video: rawvideo (YUY2 / 0x32595559), yuyv422, 640x480, 147456 kb/s, 30 fps, 30 tbr, 1000k tbn, 1000k tbc
    ```

1. The output from the second command should contain the lines:

    ```bash
    Input #0, video4linux2,v4l2, from '/dev/video2':
        Stream #0:0: Video: rawvideo (Y800 / 0x30303859), gray, 640x360, 55296 kb/s, 30 fps, 30 tbr, 1000k tbn, 1000k tbc
    ```

## CAM001.301 USB Camera (Windows)

**Test description**

This test aims to verify that the integrated USB camera is initialized
correctly and can be accessed from the operating system

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run PowerShell as administrator.
1. Execute below command and note the result:

    ```powershell
    Get-PnpDevice -PresentOnly | Where-Object { $_.InstanceId -match '^USB' }
    ```

**Expected result**

1. Output should contain `Chicony USB2.0 Camera`. Example output:

    ```powershell
    Status     Class           FriendlyName
    ------     -----           ------------
    OK         Camera          Chicony USB2.0 Camera
    OK         Bluetooth       Intel(R) Wireless Bluetooth(R)
    OK         Camera          IR Camera
    OK         USB             USB Root Hub (USB 3.0)
    OK         USB             USB Root Hub (USB 3.0)
    OK         USB             USB Composite Device
    ```
