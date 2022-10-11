# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality.

## Touchpad hotkey enablement (Linux)

The touchpad hotkey needs extra setup to function correctly under Linux. To
enable the touchpad hotkey to work under Linux, follow the steps below:

1. Create a file `/etc/udev/hwdb.d/60-keyboard.hwdb` with the following contents:

   ```bash
   evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnNV4XMB,ME,MZ:*
           KEYBOARD_KEY_f7=191
           KEYBOARD_KEY_f8=191
   ```

1. Execute the following commands:

   ```bash
   sudo systemd-hwdb update
   sudo udevadm trigger
   ```

After executing these steps, it should be possible to enable and disable the
touchpad using the touchpad hotkey (Fn+F1) on the keyboard when using GNOME.

## Nvidia drivers (Ubuntu 22.04)

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

## Installing updates and drivers (Windows 11)

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
