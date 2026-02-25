# fwupd

## Introduction

[fwupd][fwupd website] is an open-source project, that
is widely used to make firmware updates almost as seamless and simple
as updating system packages. Most hardware vendors support it
and Linux distributions.

The `fwupd` daemon relies on the Linux Vendor Firmware Service (LVFS)
for distributing and managing the firmware binaries to the users.

!!! note
     `fwupd` depends on
     [Capsule Updates](../guides/capsule-update.md)
     support. Refer to the "Firmware update" section of your device
     documentation (like [this one](../unified/novacustom/firmware-update.md)).

## Firmware Update Prerequisites

### Intel ME

This only applies to devices with an Intel Management Engine that are not fused
using the [Dasharo Trust Root](../glossary.md#dasharo-trustroot)
technology, and use Dasharo versions released before 2026. Check your release
notes to verify if the step is required.

Intel Management Engine needs to be disabled manually to successfully perform an
fwupd update. Failing to do so won't do any harm to the system, but the update
will be rejected.

Intel ME needs to be switched to the `Disabled (HAP)` state using the Setup Menu
to perform the update. It cannot be done automatically by fwupd. Afterwards,
Intel ME needs to be manually turned back on if desired.

Check [Intel Management Engine Options](../dasharo-menu-docs/dasharo-system-features.md#intel-management-engine-options)
documentation for details on how to set ME mode to `Disabled (HAP)`.
See this [Intel ME/CSME FAQ page](../osf-trivia-list/me.md)
for information about disabling the ME, or [Issue #1302](https://github.com/Dasharo/dasharo-issues/issues/1302)
for more context.

### Charger connected

On battery-powered devices (laptops), the AC charger must be connected
before running fwupdmgr to start the update. It must be connected
for the whole duration of the update, until the device boots back up normally.

## Usage

### Desktop Environments

The most popular Desktop Environments, like Gnome and KDE, automatically
look for firmware updates on LVFS and suggest performing them with a
simple button press.

|![Firmware update available in Gnome Software](./images/fwupd-gnome.png)|
|--|
|Firmware update available in Gnome Software|

Before starting the update, check whether the [prerequisites](#firmware-update-prerequisites)
are met.

### CLI

For more advanced users or in a more lightweight
DEs/WMs `fwupdmgr` can be used in the terminal.

#### Installation

Most Operating Systems come with fwupd preinstalled and use
it to perform firmware updates.

=== "Windows"
    Dasharo Capsule Updates using fwupdmgr are not currently supported on
    Windows. If that is the only Operating System you wish to use, other update
    methods need to be considered.

=== "Ubuntu"
    Check if fwupdmgr is installed. Executing the command should
    print the versions of all fwupdmgr components:

    ```bash
    $ fwupdmgr --version
    ```

    <details><summary>Example output</summary>
        ```
        $ fwupdmgr --version
        compile   org.freedesktop.fwupd         1.9.31
        compile   com.hughsie.libxmlb           0.3.18
        compile   com.hughsie.libjcat           0.2.0
        runtime   org.freedesktop.fwupd-efi     1.4
        compile   org.freedesktop.gusb          0.4.8
        runtime   com.hughsie.libxmlb           0.3.x
        runtime   com.hughsie.libjcat           0.2.0
        runtime   org.freedesktop.gusb          0.4.8
        runtime   org.freedesktop.fwupd         1.9.31
        runtime   org.kernel                    6.17.0-14-generic
        ```
    </details>


    If not, install it using:

    ```bash
    $ sudo apt update
    $ sudo apt install fwupdmgr
    ```

=== "Fedora"
    Check if fwupdmgr is installed. Executing the command should
    print the versions of all fwupdmgr components:

    ```bash
    $ fwupdmgr --version
    ```

    <details><summary>Example output</summary>
        ```
        $ fwupdmgr --version
        compile   org.freedesktop.fwupd         1.9.31
        compile   com.hughsie.libxmlb           0.3.18
        compile   com.hughsie.libjcat           0.2.0
        runtime   org.freedesktop.fwupd-efi     1.4
        compile   org.freedesktop.gusb          0.4.8
        runtime   com.hughsie.libxmlb           0.3.x
        runtime   com.hughsie.libjcat           0.2.0
        runtime   org.freedesktop.gusb          0.4.8
        runtime   org.freedesktop.fwupd         1.9.31
        runtime   org.kernel                    6.17.0-14-generic
        ```
    </details>

    If not, install it using:

    ```bash
    $ sudo dnf install fwupdmgr
    ```

=== "QubesOS"

    To use fwupdmgr on QubesOS, the program needs to be run on
    the `dom0` qube, and it requires an internet connection.
    For that reason, a fwupdmgr wrapper for QubesOS exists,
    that sets up the network tunnels for the firmware update
    downloads to be possible from dom0.
    The qubes-fwupdmgr package should be installed out of the box.
    Executing the command should print the help screen:

    ```bash
    $ sudo qubes-fwupdmgr
    ```

    <details><summary>Example output</summary>
        ```
        $ sudo qubes-fwupdmgr
        ======================================================================
        Usage:
        ======================================================================
            Command:			qubes-fwupdmgr [OPTION…][FLAG..]
            Example:			qubes-fwupdmgr refresh --whonix --url=<url>

        Options:
        ======================================================================
            get-devices:			Get all devices that support firmware updates
            get-updates:			Get the list of updates for connected hardware
            refresh:			Refresh metadata from remote server
            update:				Update chosen device to latest firmware version
            update-heads:			Updates heads firmware to the latest version (EXPERIMENTAL, not fully supported yet)
            downgrade:			Downgrade chosen device to chosen firmware version
            clean:				Delete all cached update files

        Flags:
        ======================================================================
            --whonix:			Download firmware updates via Tor
            --device:			Specify device for heads update (default - x230)
            --url:				Address of the custom metadata remote server

        Help:
        ======================================================================
            -h --help:			Show help options
        ```
    </details>

### Checking the current firmware version

=== "Ubuntu, Fedora"
    To check the currently used firmware version, run the following command

    ```bash
    $ fwupdmgr get-devices
    ```

    Look for `System Firmware` or `UEFI Device Firmware` in the output.
    <details><summary>Example of a firmware version entry:</summary>
        ```
        ├─UEFI Device Firmware:
        │     Device ID:          204ce525ed4dbc468e789eb029f3627dd13d6cf4
        │     Summary:            UEFI System Resource Table device (updated via NVRAM)
        │     Current version:    1.0.1
        │     Minimum Version:    1.0.1
        │     Vendor:             NovaCustom (DMI:3mdeb)
        │     GUID:               f4deb4f3-f673-48fe-a481-627357b00b6a
        │     Device Flags:       • Internal device
        │                         • System requires external power source
        │                         • Supported on remote server
        │                         • Needs a reboot after installation
        │                         • Device is usable for the duration of the update
        │                         • Updatable
        │     Device Requests:    • Message
        ```
    </details>

=== "QubesOS"
    To check for available updates for your device, run the following command

    ```bash
    $ sudo qubes-fwupdmgr get-devices
    ```

    Look for `System Firmware` or `UEFI Device Firmware` in the output.

    <details><summary>Example of get-devices output</summary>
        ```
        ======================================================================
        System Firmware
        ======================================================================
            DeviceId:           204ce525ed4dbc468e789eb029f3627dd13d6cf4
            Guid:               ·f4deb4f3-f673-48fe-a481-627357b00b6a
            Summary:            UEFI System Resource Table device (updated via NVRAM)
            Plugin:             uefi_capsule
            Protocols:          ·org.uefi.capsule
            Flags:              ·internal
                                ·updatable
                                ·require-ac
                                ·needs-reboot
                                ·can-verify
                                ·usable-during-update
            RequestFlags:       ·allow-generic-message
            Checksums:          ·914872cd28744aacad621b8a95e02171b7854b79cf61c59eec939868a33de07d
            Vendor:             Notebook
            VendorIds:          ·DMI:3mdeb
            Version:            16777344
            VersionRaw:         16777344
            Created:            1771420572
            UpdateState         2
        ```
        As of QubesOS R4.2.3, the firmware version is not interpreted correctly
        by fwupdmgr.
        As a fallback on Dasharo firmware, use `dmidecode` to verify the firmware version.
        Run:
        ```bash
        $ sudo dmidecode -t bios | grep Version:
        ```
        Example output:
        ```txt
        Version: Dasharo (coreboot+UEFI) v1.0.0
        ```
    </details>

### Checking for updates

=== "Ubuntu, Fedora"
    To check for available updates for your device, run the following commands

    ```bash
    $ fwupdmgr refresh
    $ fwupdmgr get-updates
    ```

    <details><summary>Example of a possible update from v1.0.0 to v1.0.1:</summary>
        ```
        $ fwupdmgr get-updates
        Devices with no available firmware updates:
        • UEFI dbx
        • SSDPR-PX600-250-80
        Notebook V54x_6x_TU
        │
        └─System Firmware:
        │   Device ID:          204ce525ed4dbc468e789eb029f3627dd13d6cf4
        │   Summary:            UEFI System Resource Table device (updated via NVRAM)
        │   Current version:    1.0.0
        │   Minimum Version:    1.0.0
        │   Vendor:             NovaCustom (DMI:3mdeb)
        │   Update State:       Success
        │   GUID:               f4deb4f3-f673-48fe-a481-627357b00b6a
        │   Device Flags:       • Internal device
        │                       • Updatable
        │                       • System requires external power source
        │                       • Supported on remote server
        │                       • Needs a reboot after installation
        │                       • Cryptographic hash verification is available
        │                       • Device is usable for the duration of the update
        │   Device Requests:    • Message
        │
        └─V54x_6x_TU System Update:
                New version:      1.0.1
                Remote ID:        lvfs
                Release ID:       135872
                Summary:          V54x_6x_TU V540TU system firmware
                License:          Proprietary
                Size:             34.0 MB
                Created:          2026-01-29
                Urgency:          High
                Tested by NovaCustom:
                Tested:         2026-01-29
                Distribution:   ubuntu 24.04
                Old version:    1.0.1
                Version[fwupd]: 1.9.31
                Vendor:           NovaCustom
                Release Flags:    • Trusted metadata
                                • Is upgrade
                                • Tested by trusted vendor
                Description:
                New Dasharo firmware release for the NovaCustom Meteor Lake laptops

                with integrated graphics, featuring numerous bug fixes, performance

                improvements and stability fixes.
                Checksum:         178be21614286811e95484118e06b4b39c91fe401b234639d4aa73cd7d6f63d6
        ```
    </details>

=== "QubesOS"
    To check for available updates for your device, run the following commands

    ```bash
    $ qubes-fwupdmgr refresh
    $ qubes-fwupdmgr get-updates
    ```

    !!! warning
        As of QubesOS R4.3 on 02-2026, qubes-fwupdmgr might not work correctly
        and the updates on LVFS may not be found using this tool. Refer to
        [troubleshooting](#no-updates-available-qubesos).

### Updating the firmware

#### Preparation / Prerequisites

Before starting the update, check whether the [prerequisites](#firmware-update-prerequisites)
are met.

#### Update instructions

=== "Ubuntu, Fedora"
    To update your firmware, run the following commands:

    ```bash
    $ fwupdmgr refresh
    $ sudo fwupdmgr update
    ```

    <details><summary>Example of an update process:</summary>
        ```
        $ fwupdmgr update
        Devices with no available firmware updates:
        • UEFI dbx
        • SSDPR-PX600-250-80
        ╔══════════════════════════════════════════════════════════════════════════════╗
        ║ Upgrade System Firmware from 1.0.0 to 1.0.1?                                 ║
        ╠══════════════════════════════════════════════════════════════════════════════╣
        ║ New Dasharo firmware release for the NovaCustom Meteor Lake laptops          ║
        ║                                                                              ║
        ║ with integrated graphics, featuring numerous bug fixes, performance          ║
        ║                                                                              ║
        ║ improvements and stability fixes.                                            ║
        ║                                                                              ║
        ║ V54x_6x_TU must remain plugged into a power source for the duration of the   ║
        ║ update to avoid damage.                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════╝
        Perform operation? [Y|n]: y
        Authenticating…          [***************************************]
        ==== AUTHENTICATING FOR org.freedesktop.fwupd.update-internal-trusted ====
        Authentication is required to update the firmware on this machine
        Authenticating as: ubuntu
        Password:
        ==== AUTHENTICATION COMPLETE ====
        Waiting…                 [***************************************]
        Successfully installed firmware
        Do not turn off your computer or remove the AC adapter while the update is in progress.
        An update requires a reboot to complete. Restart now? [y|N]: y
        ==== AUTHENTICATING FOR org.freedesktop.login1.reboot ====
        Authentication is required to reboot the system.
        Authenticating as: ubuntu
        Password:
        ==== AUTHENTICATION COMPLETE ====
        ```
    </details>

=== "QubesOS"

    To update your firmware, run the following commands:

    ```bash
    $ sudo qubes-fwupdmgr refresh
    $ sudo qubes-fwupdmgr update
    ```

    !!! warning
        As of QubesOS R4.3 on 02-2026, qubes-fwupdmgr might not work correctly
        and the updates on LVFS may not be found using this tool. Refer to
        [troubleshooting](#no-updates-available-qubesos).

!!! warning
    After the command finishes, fwupd will instruct the device to reboot.
    The fwupd UEFI application that performs the update will be booted
    automatically after a reboot, unless there's user interaction
    Entering the Setup Menu, Boot Manager, or interfering in any other way will
    abort the update.
    Allow the device to reboot freely, and do not press any buttons until the
    update finishes.

    Devices that have an Embedded Controller
    [might stay powered off after the update][dts-ec-update] and need to be
    powered on.

[dts-ec-update]: ../dasharo-tools-suite/documentation/features.md#ec-update

#### Local Update

If using LVFS is undesirable or not possible, a fwupd firmware update can be
performed using a locally available cabinet (.cab) file downloaded from any
source. We will use `novacustom_v54x_mtl_igpu_v1.0.1_btg_prod.cab` downloaded from
[dl.3mdeb.com][cabinet_file] as an example.
[cabinet_file]: https://dl.3mdeb.com/open-source-firmware/Dasharo/novacustom_v5x0_mtl/novacustom_mtl_igpu/novacustom_v540tu_mtl/uefi/v1.0.1/

=== "Ubuntu, Fedora, QubesOS"
    To update your firmware using a locally available cabinet file, follow the
    steps:

    1. Allow updates from untrusted sources
        ```bash
        $ printf '[fwupd]\nOnlyTrusted=false\n' | sudo tee /etc/fwupd/fwupd.conf
        ```
    2. Perform a local install
        ```bash
        $ sudo fwupdmgr local-install novacustom_v54x_mtl_igpu_v1.0.1_btg_prod.cab
        ```

#### Update troubleshooting

##### No output from fwupdmgr update

Depending on the version of fwupdmgr, issues like the AC being disconnected on
battery-powered devices might not be printed explicitly right away after
trying to perform an update. In such a case, try running the `get-devices` command
and look for the `Problems` header and red text under device entries.
<details><summary>Example, update rejected, AC was not connected.</summary>
    ```
    ├─System Firmware:
    │ │   Device ID:          204ce525ed4dbc468e789eb029f3627dd13d6cf4
    │ │   Summary:            UEFI System Resource Table device (updated via NVRAM)
    │ │   Current version:    1.0.0
    │ │   Minimum Version:    1.0.0
    │ │   Vendor:             NovaCustom (DMI:3mdeb)
    │ │   Update State:       Success
    │ │   Problems:           • Device requires AC power to be connected
    │ │   GUID:               f4deb4f3-f673-48fe-a481-627357b00b6a
    │ │   Device Flags:       • Internal device
    │ │                       • System requires external power source
    │ │                       • Supported on remote server
    │ │                       • Needs a reboot after installation
    │ │                       • Cryptographic hash verification is available
    │ │                       • Device is usable for the duration of the update
    │ │                       • Updatable
    │ │   Device Requests:    • Message
    ```
    Note that `Update State` is `Success` despite a failure, as it reports
    the status of the last correctly initiated Update. Without an AC connected,
    the update did not even start keeping the previous value of `Update State`.
</details>

To verify if the problem really occurs, you can run the command in verbose mode:

```bash
$ sudo fwupdmgr update -v
```

The output might suggest what the issue is, for example:
<!-- markdownlint-disable MD013 -->
<details><summary>Example of fwupdmgr update -v</summary>
    ```txt
    $ sudo fwupdmgr update -v
    (pkttyagent:4378): GLib-GIO-DEBUG: 11:44:32.011: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.019: _g_io_module_get_default: Found default implementation dconf (DConfSettingsBackend) for ‘gsettings-backend’
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.019: watch_fast: "/system/proxy/" (establishing: 0, active: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: watch_fast: "/system/proxy/http/" (establishing: 0, active: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: watch_fast: "/system/proxy/https/" (establishing: 0, active: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: watch_fast: "/system/proxy/ftp/" (establishing: 0, active: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: watch_fast: "/system/proxy/socks/" (establishing: 0, active: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: unwatch_fast: "/system/proxy/" (active: 0, establishing: 1)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: unwatch_fast: "/system/proxy/http/" (active: 0, establishing: 1)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: unwatch_fast: "/system/proxy/https/" (active: 0, establishing: 1)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: unwatch_fast: "/system/proxy/ftp/" (active: 0, establishing: 1)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.020: unwatch_fast: "/system/proxy/socks/" (active: 0, establishing: 1)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.021: watch_established: "/system/proxy/" (establishing: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.021: watch_established: "/system/proxy/http/" (establishing: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.021: watch_established: "/system/proxy/https/" (establishing: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.021: watch_established: "/system/proxy/ftp/" (establishing: 0)
    (fwupdmgr:4376): dconf-DEBUG: 11:44:32.021: watch_established: "/system/proxy/socks/" (establishing: 0)
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.021: _g_io_module_get_default: Found default implementation local (GLocalVfs) for ‘gio-vfs’
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021: px_config_sysconfig_set_config_file: Could not read file /etc/sysconfig/proxy
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021: Active config plugins:
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021:  - config-env
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021:  - config-kde
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021:  - config-gnome
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.021:  - config-sysconfig
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.023: Failed to initialize portal (GNetworkMonitorPortal) for gio-network-monitor: Not using portals
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.024: Using cross-namespace EXTERNAL authentication (this will deadlock if server is GDBus < 2.73.3)
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.026: _g_io_module_get_default: Found default implementation networkmanager (GNetworkMonitorNM) for ‘gio-network-monitor’
    (fwupdmgr:4376): pxbackend-DEBUG: 11:44:32.026: px_manager_constructed: Up and running
    (fwupdmgr:4376): GLib-GIO-DEBUG: 11:44:32.026: _g_io_module_get_default: Found default implementation libproxy (GLibproxyResolver) for ‘gio-proxy-resolver’
    (fwupdmgr:4376): Fwupd-DEBUG: 11:44:32.028: Emitting ::status-changed() [idle]
    Devices with no available firmware updates:
    • SSDPR-PX600-250-80
    • UEFI dbx
    (fwupdmgr:4376): FuMain-DEBUG: 11:44:32.043: ignoring 204ce525ed4dbc468e789eb029f3627dd13d6cf4: System Firmware is not currently updatable: Device requires AC power to be connected
    ```
</details>
<!-- markdownlint-enable MD013 -->

At the end of the verbose output, we can see the line

```txt
(fwupdmgr:4376): FuMain-DEBUG: 11:44:32.043: ignoring 204ce525ed4dbc468e789eb029f3627dd13d6cf4: System Firmware is not currently updatable: Device requires AC power to be connected
```

Which tells us that the update was rejected, because there's no AC adapter
connected.

If you see any errors during the update, check the [Troubleshooting](../guides/capsule-update.md#troubleshooting)
section of the Capsule Update guide.

##### fwupdmgr asks for AC despite it being connected

The check for an AC charger being connected in Linux fails when the firmware
configures a [charging threshold](http://127.0.0.1:8000/unified/novacustom/features/#charge-thresholds)
for the battery that disconnects the charger once the battery reaches the threshold.
If the battery is considered full and not charging at the moment, the check in
fwupdmgr will think the charger is disconnected.

There are two options to work around this issue:

- Deplete battery charge a couple of percent, so that it
    doesn't stop charging for the duration of fwupdmgr running the checks.
- Disable battery charging thresholds in the firmware.

##### No updates available (QubesOS)

As of QubesOS R4.3 on 02-2026
[qubes-fwupdmgr does not work correctly][qubes-fwupdmgr-issue]
and the updates on LVFS might not be found using this tool.
In such a case, there are still a few options to perform the update.
Either use a different update method according to the `Firmware Update`
page for your device in the `Supported hardware` tab, or perform
a [Local Update](#local-update) using a fwupd cabinet (.cab) file downloaded
manually from fwupd.org.

[qubes-fwupdmgr-issue]: https://github.com/fwupd/fwupd/issues/9933

#### Verifying the firmware update result

=== "Ubuntu, Fedora"
    To check the result of your firmware update, run the following command:

    ```bash
    $ fwupdmgr get-results
    ```

    You will be prompted to select a device. For Dasharo firmware updates, select
    `System Firmware` or `UEFI Device Firmware`.

    <details><summary>Example of `fwupdmgr get-results` output after a successful update</summary>
        ```
        $ fwupdmgr get-results
        0.	Cancel
        1.	597c1adb5fa5096f1949ae7535b85dc6ddd34f80 ((null))
        2.	4bde70ba4e39b28f9eab1628f9dd6e6244c03027 (Core™ Ultra 7 155H)
        3.	aec1a869eb0df71b7cea6b3ac71d39b830faf164 (MNE007QS1-4)
        4.	5792b48846ce271fab11c4a545f7a3df0d36e00a (Meteor Lake-P [Intel Graphics])
        5.	71b677ca0f1bc2c5b804fa1d59e52064ce589293 (SSDPR-PX600-250-80)
        6.	204ce525ed4dbc468e789eb029f3627dd13d6cf4 (System Firmware)
        7.	c6a80ac3a22083423992a3cb15018989f37834d6 (TPM)
        8.	6924110cde4fa051bfdc600a60620dc7aa9d3c6a (UEFI Platform Key)
        9.	362301da643102b9f38477387e2193e57abaa590 (UEFI dbx)
        Choose device [0-9]: 6
        System Firmware:
        Device ID:            204ce525ed4dbc468e789eb029f3627dd13d6cf4
        Previous version:     1.0.0
        Update State:         Success
        Last modified:        2026-02-18 14:01
        GUID:                 f4deb4f3-f673-48fe-a481-627357b00b6a
        Device Flags:         • Internal device
                                • Updatable
                                • System requires external power source
                                • Supported on remote server
                                • Needs a reboot after installation
                                • Cryptographic hash verification is available
                                • Device is usable for the duration of the update
        ```
    </details>

    This output means the firmware version has changed to the expected one.
    To manually verify this has really happened, refer to
    [Checking The Current Firmware Version](#checking-the-current-firmware-version).

=== "QubesOS"
    To update your firmware, run the following commands:

    ```bash
    $ sudo qubes-fwupdmgr refresh
    $ sudo qubes-fwupdmgr update
    ```

#### Update result troubleshooting

##### Failed to run update on reboot: expected ... and got

This Update Error is most often caused by failing to set the Intel ME
to `Disabled (HAP)` mode before running the update.

<details><summary>Example of fwupdmgr get-results output when that happens</summary>
```
$ fwupdmgr get-results
0. Cancel
1. 597c1adb5fa5096f1949ae7535b85dc6ddd34f80 ((null))
2. 4bde70ba4e39b28f9eab1628f9dd6e6244c03027 (Core™ Ultra 7 155H)
3. aec1a869eb0df71b7cea6b3ac71d39b830faf164 (MNE007QS1-4)
4. 5792b48846ce271fab11c4a545f7a3df0d36e00a (Meteor Lake-P [Intel Graphics])
5. 71b677ca0f1bc2c5b804fa1d59e52064ce589293 (SSDPR-PX600-250-80)
6. 204ce525ed4dbc468e789eb029f3627dd13d6cf4 (System Firmware)
7. c6a80ac3a22083423992a3cb15018989f37834d6 (TPM)
8. 6924110cde4fa051bfdc600a60620dc7aa9d3c6a (UEFI Platform Key)
9. 362301da643102b9f38477387e2193e57abaa590 (UEFI dbx)
Choose device [0-9]: 6
System Firmware:
Device ID:            204ce525ed4dbc468e789eb029f3627dd13d6cf4
Previous version:     1.0.0
Update State:         Failed
Update Error:         failed to run update on reboot: expected 1.0.1 and got 1.0.0
Last modified:        2026-02-18 13:45
GUID:                 f4deb4f3-f673-48fe-a481-627357b00b6a
Device Flags:         • Internal device
                        • Updatable
                        • System requires external power source
                        • Supported on remote server
                        • Needs a reboot after installation
                        • Cryptographic hash verification is available
                        • Device is usable for the duration of the update
```
</details>

When that happens after rebooting, instead of am update
progress bar, a message like this will appear on top of the screen:

```txt
[FIRMWARE WARNING] Capsule Updates are only supported while Intel ME is in HAP mode!
```

Make sure the Intel ME mode in the Setup menu is `Disabled (HAP)`. Refer to the
[prerequisites section](#firmware-update-prerequisites) and try again.

## References

- [fwupd website][fwupd website]
- [fwupd github repository][fwupd github repository]
- [fwupd documentation][fwupd documentation]

[fwupd website]: https://fwupd.org
[fwupd github repository]: https://github.com/fwupd/fwupd
[fwupd documentation]: https://lvfs.readthedocs.io
