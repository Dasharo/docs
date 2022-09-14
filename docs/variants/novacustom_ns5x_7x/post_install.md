# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality.

## Touchpad hotkey enablement (Linux)

The touchpad hotkey needs extra setup to function correctly under Linux. To
enable the touchpad hotkey to work under Linux, follow the steps below:

1. Create a file `/etc/udev/hwdb.d/60-keyboard.hwdb` with the following contents:

    ```bash
    evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnNS50_70MU:*
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

## Touchpad multi-touch support (NS7x / 17-inch model, Linux)

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

Now reboot your computer to apply the changes.
