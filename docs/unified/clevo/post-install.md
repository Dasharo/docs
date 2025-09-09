# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality of your device.

Select your operating system to view applicable instructions:

=== "Ubuntu"
    ### Touchpad hotkey enablement

    The touchpad hotkey may need extra setup to function correctly under Linux.
    If the key isn't working, execute the following command to apply a fix:

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

    and reboot to use the new kernel.

    ### NVIDIA drivers

    If your device comes with NVIDIA graphics, proprietary NVIDIA drivers are
    recommended for optimal performance and battery life.

    1. Install drivers according to
       [instructions provided by Ubuntu](https://ubuntu.com/server/docs/nvidia-drivers-installation)

    1. Reboot the device to apply changes

    1. (Optional) If you're suffering from poor battery life caused by the GPU
       not turning off, ensure On-Demand mode is enabled in NVIDIA Control
       Panel:

       ![](../../images/nv4x_nvidia_panel.jpg){ class="center" }

    1. (Optional) If the GPU is still not powering down, run the following
       command, and then reboot the laptop:

        ```bash
        echo options nvidia "NVreg_DynamicPowerManagement=0x02" | sudo tee /etc/modprobe.d/nvidia_rtd3.conf
        ```

    ### Suspend fix for SATA disks

    Only affects laptops with M.2 SATA disks experiencing sleep issues (the power
    LED not blinking while the laptop is suspended)

    Windows and certain Linux distros such as Ubuntu do not enable the necessary
    power saving tweaks to enable sleep mode while a SATA disk is installed.

    Execute fixup script:

    ```bash
    curl -sSf https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/sata-suspend-fixup | sudo sh
    ```

    ### Enable hibernation

    If you wish to use hibernation (S4) on your laptop, please follow
    [this guide](https://ubuntuhandbook.org/index.php/2021/08/enable-hibernate-ubuntu-21-10/)
    . Then, execute the following command:

    ```bash
    echo 259:3 | sudo tee /sys/power/resume
    ```
    It might also be necessary to create or increase your current swap
    partition/file - it should be slightly larger than the size of your RAM. In
     such case, please refer to the instructions provided
    [here](https://askubuntu.com/a/178726).

=== "Fedora"
    ### Touchpad hotkey enablement

    The touchpad hotkey may need extra setup to function correctly under Linux.
    If the key isn't working, execute the following command to apply a fix:

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

    and reboot to use the new kernel.

    ### NVIDIA drivers

    If your device comes with NVIDIA graphics, proprietary NVIDIA drivers are
    recommended for optimal performance and battery life.

    1. Install drivers according to
       [instructions by RPM fusion](https://rpmfusion.org/Howto/NVIDIA#Current_GeForce.2FQuadro.2FTesla)

    1. Reboot the device to apply changes

    1. (Optional) If you're suffering from poor battery life caused by the GPU
       not turning off, ensure On-Demand mode is enabled in NVIDIA Control
       Panel:

       ![](../../images/nv4x_nvidia_panel.jpg){ class="center" }

    1. (Optional) If the GPU is still not powering down, run the following
       command, and then reboot the laptop:

        ```bash
        echo options nvidia "NVreg_DynamicPowerManagement=0x02" | sudo tee /etc/modprobe.d/nvidia_rtd3.conf
        ```

    ### Suspend fix for SATA disks

    Only affects laptops with M.2 SATA disks experiencing sleep issues (the power
    LED not blinking while the laptop is suspended)

    Windows and certain Linux distros such as Ubuntu do not enable the necessary
    power saving tweaks to enable sleep mode while a SATA disk is installed.

    Execute fixup script:

    ```bash
    curl -sSf https://raw.githubusercontent.com/Dasharo/dasharo-tools/main/clevo/sata-suspend-fixup | sudo sh
    ```

    ### Enable hibernation

    If you wish to use hibernation (S4) on your laptop, please follow
    [this guide](https://discussion.fedoraproject.org/t/setup-hibernation-on-fedora-atomic-desktops/121534/3)
    . It might also be necessary to create or increase your current swap
    partition/file - it should be slightly larger than the size of your RAM. In
     such case, please refer to the instructions provided
    [here](https://superuser.com/questions/1778582/how-to-add-swap-space-on-fedora).

=== "Qubes OS"
    ### Touchpad hotkey enablement

    The touchpad hotkey may need extra setup to function correctly under Qubes.
    If the key isn't working, follow the steps below:

    1. Open dom0 terminal window

    1. Open /etc/udev/hwdb.d/60-keyboard.hwdb in your preferred text editor,
       e.g. nano:

        ```bash
        sudo nano /etc/udev/hwdb.d/60-keyboard.hwdb
        ```

    1. Type the following into the file:

        !!! note
            The following applies only to NV4x 12th Gen and V560TU, which are
            currently the only officially Qubes-certified models. If you use
            Qubes on any other model, you may need to adjust the SMBIOS product
            name in the section below.

        ```
        evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnNV4xPZ:*
        evdev:atkbd:dmi:bvn*:bvr*:svnNotebook:pnV54x_6x_TU:*
         KEYBOARD_KEY_f7=touchpad_toggle
         KEYBOARD_KEY_f8=touchpad_toggle
         KEYBOARD_KEY_81=micmute
        ```

    1. Execute the following command:

        ```bash
        sudo systemd-hwdb update
        sudo udevadm trigger
        ```

    1. Reboot to apply changes

    After executing these steps, the hotkey should generate the correct keycode.
    You may need to map it to the correct action in Xfce settings to ensure it
    disables the touchpad.

=== "Windows 11"
    ### Updates and drivers installation

    Several features on Windows 11 (i. e. suspending the device) may not work or
    work unexpectedly without installing all of the updates and drivers.

    ???+ info
        On NUC BOX, to provide basic network connectivity, Intel ethernet driver must
        be installed. Download link: [Intel® Network Adapter Driver for Microsoft Windows 11](https://www.intel.com/content/www/us/en/download/727998/intel-network-adapter-driver-for-microsoft-windows-11.html)
        After successful driver update on both ethernet ports, Windows Update should
        be able to install correct Wi-Fi diver.

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

    ### Enable hibernation

    If you wish to use hibernation (S4) on your laptop, run these commands in
    PowerShell as an Administrator:

    ```powershell
    powercfg /h on
    powercfg /h /type full
    ```
