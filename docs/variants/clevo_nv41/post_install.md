# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality.

## Touchpad hotkey enablement (Linux)

The touchpad hotkey needs extra setup to function correctly under Linux. To
enable the touchpad hotkey to work under Linux, follow the steps below:

1. Create a file `/etc/udev/hwdb.d/60-keyboard.hwdb` with the following contents:
   ```
   evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnNV4XMB,ME,MZ:*
           KEYBOARD_KEY_f7=191
           KEYBOARD_KEY_f8=191
   ```
1. Execute the following commands:
   ```
   sudo systemd-hwdb update
   sudo udevadm trigger
   ```

After executing these steps, it should be possible to enable and disable the
touchpad using the touchpad hotkey (Fn+F1) on the keyboard when using GNOME.
