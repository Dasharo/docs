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

### Nvidia drivers

> It is only necessary to follow this step if your device has Nvidia GPU

For proper working of the sleep mode on Ubuntu 22.04, it is required to
install additional Nvidia drivers.

1. Install drivers by executing the following command in the terminal:

    ```bash
    sudo apt install nvidia-driver-515 nvidia-dkms-515
    ```

1. Reboot the device to apply changes by executing the following command in the
    terminal:

    ```bash
    sudo reboot
    ```

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

## Suspend fix for SATA disks (Windows and Linux)

Only affects laptops with M.2 SATA disks experiencing sleep issues (the power
LED not blinking while the laptop is suspended).

Windows and certain Linux distros such as Ubuntu do not enable the necessary
power saving tweaks to enable sleep mode while a SATA disk is installed. To
apply the fix, run the following scripts

### Windows:

- Download the script: [link](https://cloud.3mdeb.com/index.php/s/nNQwDEKryCHGJ5n)
- Double click on the script to install the tweak

### Linux

- Download the script: [link](https://cloud.3mdeb.com/index.php/s/ms9Dd7NtcXTj8KL)
- Execute as root:

    ```bash
    chmod +x install_dipm_service.sh
    sudo ./install_dipm_service.sh
    ```
