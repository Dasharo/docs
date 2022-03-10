# Dasharo Compatibility: generic test setup

## Test setup

Test setup is a set of procedures to be executed before the test execution.
Typically, the same setup can be reused by multiple test cases, so there is no
need to execute the setup actions before each independent case.

### Generic test setup

#### Firmware

1. Obtain `FIRMWARE` binary:
    1. you can download it from `release` document dedicated for platform which
        is used by you.
    1. or you can build one yourself as shown in the `building` document
        dedicated for platform which is used by you.
1. Flash `FIRMWARE` binary to the DUT:
    1. If coreboot is not yet installed: refer to
        `Flashing with external programmer` document dedicated for platform
        which is used by you.
    1. If coreboot is already installed: refer to
        `Flashing with internal programmer` document dedicated for platform
        which is used by you.

#### OS installer

1. Download `OPERATING_SYSTEM` installer image.
1. Attach USB stick to the PC.
1. Flash `OPERATING_SYSTEM` image to the USB stick.
1. Attach the USB stick to the `DUT`.

#### OS installation

1. Power ON the DUT
1. Enter the boot menu using the `BIOS_SETUP_KEY`.
1. Select the `Boot Menu` and press `Enter`.
1. Select the USB stick and press `Enter`.
    1. In case of the `Ubuntu 20.04`, select the `Ubuntu (safe graphics)` in the
       GRUB menu.
1. Wait for the `OPERATING_SYSTEM` installer to start.
1. Install `OPERATING_SYSTEM` on the disk.
1. In case of `Ubuntu 20.04` on `NV41MB`: Follow the steps outlined in
   [NVIDIA drivers - Ubuntu 20.04](./#nvidia-drivers-ubuntu-2004).
1. Power OFF the DUT.
1. Remove the installation media (USB stick with installer).

#### NVIDIA drivers - Ubuntu 20.04

1. Power ON the DUT.
1. Wait until the `OPERATING_SYSTEM` boots from disk.
1. Login into the `OPERATING_SYSTEM`.
1. Open a terminal window and execute the following commands:

```
sudo apt update
sudo apt install nvidia-driver-470
```

1. A password prompt for secure boot configuration will appear. Choose a
   password (you can use your system password) and press `Enter`.
1. Reboot the DUT.
1. Upon entry into MOKUtil, select `Enroll MOK` and enter the password you
   chose during driver installation.
1. Select the option `Continue boot`.
1. Wait until the `OPERATING_SYSTEM` boots from disk.
1. Login into the `OPERATING_SYSTEM`.
1. Open the `NVIDIA X Server Settings` application.
1. Open the `PRIME Profiles` section.
1. Select `NVIDIA On-demand` and apply.
1. Enter the `OPERATING_SYSTEM` password when prompted.

#### OS boot from disk

1. Power ON the DUT.
1. Wait until the `OPERATING_SYSTEM` boots from disk.
1. Login into the `OPERATING_SYSTEM`.
