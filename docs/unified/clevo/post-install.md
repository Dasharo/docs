# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality of your device.

## Linux

This section covers Linux post-install steps tested on Ubuntu 22.04. It is
likely thas similar procedures would for others Linux distributions as well.

### Touchpad hotkey enablement

The touchpad hotkey needs extra setup to function correctly under Linux. To
enable the touchpad hotkey to work under Linux, follow the steps below:

1. Execute fixup script:

```bash
curl -sSf https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/touchpad-fixup | sudo sh
```

After executing these steps, it should be possible to enable and disable the
touchpad using the touchpad hotkey (Fn+F1) on the keyboard when using GNOME.

### Touchpad multi-touch support

On NS7x an additional fix is necessary to enable multi-touch on Linux. Create
a file `/etc/modprobe.d/blacklist-psmouse.conf` with the following contents:

```bash
blacklist psmouse
```

and then run the following commands:

```bash
sudo depmod -a
sudo update-initramfs -u
```

### Updated kernel

On Gen 12 (Alder Lake), it's recommended to install the ubuntu-oem kernel which
is a newer version than the default Ubuntu kernel. This version contains
additional fixes for newer hardware which helps with power management and
suspend on Gen 12 laptops. To install the ubuntu-oem kernel, run the following
command:

```bash
sudo apt install linux-oem-22.04a
```

and reboot to use the new kernel.

### Nvidia drivers

> It is only necessary to follow this step if your device has Nvidia GPU

For proper working of the sleep mode on Ubuntu 22.04, it is required to
install additional Nvidia drivers.

1. Install drivers by executing the following command in the terminal:

    ```bash
    sudo apt install nvidia-driver-535 nvidia-dkms-535
    ```

1. Reboot the device to apply changes by executing the following command in the
    terminal:

    ```bash
    sudo reboot
    ```

1. (Optional) For power saving while the card is not in use, enable On-Demand
   mode in NVIDIA Control Panel:

![](/images/nv4x_nvidia_panel.jpg){ class="center" }

### Suspend fix for SATA disks

Only affects laptops with M.2 SATA disks experiencing sleep issues (the power
LED not blinking while the laptop is suspended)

Windows and certain Linux distros such as Ubuntu do not enable the necessary
power saving tweaks to enable sleep mode while a SATA disk is installed.

1. Execute fixup script:

    ```bash
    curl -sSf https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/sata-suspend-fixup | sudo sh
    ```

### Headset jack fix for NV4x 12th Gen

The headset jack in NV4x 12th Gen (Alder Lake) needs a fix that is available
starting with kernel version v6.0 (patch
[be561ffad708f0cee18aee4231f80ffafaf7a419](https://github.com/torvalds/linux/commit/be561ffad708f0cee18aee4231f80ffafaf7a419)).
If you are using an older kernel, you need to add the fix manually:

1. Execute fixup script:

    ```bash
    curl -sSf https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/nv4x-audio-fixup | sudo sh
    ```

1. Reboot. The audio jack will now work correctly.

## Windows 11

### Updates and drivers installation

Several features on Windows 11 (i. e. suspending the device) may not work or
work unexpectedly without installing all of the updates and drivers.

To install all of them, log into the system, connect the device to the mains
and Internet, then follow the steps below:

1. Press the `Windows` button on the keypad.
1. Type `Windows Update Settings` in the search and press `Enter`.
1. Select the `Check for updates` bar to start installing available updates and
    drivers. During this process previously selected bar might be changed to
    `Restart now` or `Retry`, so click them if something hasn't been installed
    yet, something has gone wrong or a restart is just required. The entire
    process may take up to 30 minutes.
1. Select the `Advanced options` option in the `Windows Update Settings` window.
1. Locate the `Optional updates` option and click on it.
1. Select all displayed updates and drivers.
1. Select the `Download & Install` bar to start installing additional updates
    and drivers. During this process previously selected bar might be changed
    to `Restart now` or `Retry`, so click them if something hasn't been
    installed yet, something has gone wrong or a restart is just required.
    The entire process may take up to 30 minutes.
1. Repeat all steps until all updates have been installed.

### Suspend fix for SATA disks

Only affects laptops with M.2 SATA disks experiencing sleep issues (the power
LED not blinking while the laptop is suspended)

Windows and certain Linux distros such as Ubuntu do not enable the necessary
power saving tweaks to enable sleep mode while a SATA disk is installed.

1. Download the script: [link](https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/sata-suspend-fixup.bat)
2. Double click on the script to install the tweak

### Unrecognized USB Controller device in device manager

Windows Update may sometimes fail to automatically install drivers for the
Thunderbolt DMA controller device. The driver may be installed manually from
the Windows Update Catalog:

1. Download the update cabinet: [Windows Update link](https://catalog.s.download.windowsupdate.com/d/msdownload/update/driver/drvs/2023/10/12081e68-169e-483b-9180-87f40ecc6904_8aa1088bc7bd88105d5c4e4a504bfb9bdcd01078.cab)
2. Right-click on the cabinet and select `Install` to install the driver

After the update, Thunderbolt Control Center will become available and the
warning in device manager will disappear.
