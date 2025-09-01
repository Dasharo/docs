# Dasharo Tools Suite

## What is Dasharo Tools Suite?

Dasharo Tools Suite (DTS) is like a swiss army knife for Dasharo firmware: you
can execute initial deployment, firmware update and even dump machine logs for
debugging and development support.

Also refer to [DTS Overview](../dasharo-tools-suite/overview.md).

## How to get Dasharo Pro Package Releases using Dasharo Tools Suite?

Dasharo Pro Package Releases can be used to perform firmware updates
with DTS by providing Dasharo Pro Package credentials obtained after
buying a [Dasharo Pro Package](../ways-you-can-help-us.md#become-a-dasharo-pro-package-subscriber).

Commercial use of DTS should be discussed directly with
[3mdeb](mailto:leads@3mdeb.com) or [Dasharo Team](mailto:contact@dasharo.com).

### How can I use my Dasharo Pro Package credentials

<!-- Need to be replaced in case the menu changed. -->

After purchasing the Dasharo Pro Package, you should receive an email
with keys to use with [Dasharo Tools Suite](../dasharo-tools-suite/overview.md).
This section describes how to do it.

* Firstly, run DTS from a USB flash drive, documentation on this is included
  [here](../dasharo-tools-suite/documentation/running.md#bootable-usb-stick).

* After booting, you will see a text menu, choose option number 4,
  `Load your DPP keys`, by pressing `4` and `Enter`.

* Next, rewrite the credentials received in the following order:
    - `e-mail`,
    - `password`.

* Credentials will be verified by DTS attempting to connect to our server. If
  successful, the message `Verification of the Dasharo DPP was successful. They
  are valid and will be used.` will be displayed.

Below is a short demo that presents loading of the DPP keys.

```console hl_lines="24-29"
 Dasharo Tools Suite Script 2.6.0
 (c) Dasharo <contact@dasharo.com>
 Report issues at: https://github.com/Dasharo/dasharo-issues
*********************************************************
**                HARDWARE INFORMATION
*********************************************************
**    System Inf.: Emulation QEMU x86 q35/ich9
** Baseboard Inf.: Emulation QEMU x86 q35/ich9
**       CPU Inf.: QEMU Virtual CPU version 2.5+
**    RAM Virtual: Not Specified
*********************************************************
**                FIRMWARE INFORMATION
*********************************************************
** BIOS Inf.: 3mdeb Dasharo (coreboot+UEFI) v0.2.1-rc1
*********************************************************
**     1) Dasharo HCL report
**     2) Update Dasharo Firmware
**     4) Load your DPP keys
**     6) Transition Dasharo Firmware
*********************************************************
R to reboot  P to poweroff  S to enter shell
K to launch SSH server  L to enable sending DTS logs

Enter an option:
4

Enter DPP email:   you@example.com

Enter password:    password
Dasharo DPP credentials have been saved
```

## How to support us?

In general there are three ways to support us:

### I have more time than money and I can code

Please help us develop Dasharo influence on open-source firmware market and
spread the word about it. There are multiple ways to do that:

* [Join Dasharo Matrix
  Community](../ways-you-can-help-us.md#join-dasharo-matrix-community) and
  support other members of community
* [Join Dasharo open-source firmware
  vPub](../ways-you-can-help-us.md#join-dasharo-open-source-firmware-vpub) or
  other related event organized by 3mdeb or Dasharo Team.
* [Write a Google review](../ways-you-can-help-us.md#write-a-google-review)
* [Follow us on social
  media](../ways-you-can-help-us.md#follow-us-on-social-media) and help
  spreading the word about Dasharo.
* [Contribute](../ways-you-can-help-us.md#contribute-through-github)
  documentation, test results, [Dasharo Hardware Compatibility List
  Reports](https://docs.dasharo.com/dasharo-tools-suite/documentation/features/#hcl-report)

To get access to DTS SE you should [contact 3mdeb](mailto:leads@3mdeb.com) or
[Dasharo Team](mailto:contact@dasharo.com) and prove your contribution
regarding above areas of support and influence. If it would be meaningful we
would be glad to give you access to DTS SE for a year.

### I have more time than money and I can't code

Please [contribute](../ways-you-can-help-us.md#contribute-through-github)
ideas for new features, review documentation and help testing bug fixes.

If you would like to pursue that path please contact us on [Dasharo -
General](https://matrix.to/#/#dasharo-general:matrix.org) Matrix channel to
agree on scope of contribution to avoid any potential collision with other
developers. To get access to DTS SE you should contact
[3mdeb](mailto:leads@3mdeb.com) or [Dasharo Team](mailto:contact@dasharo.com)
with links to your contribution and we would be glad to provide one year of DTS
SE updates.

### I have more money than time

Please [donate](../ways-you-can-help-us.md#donate-money) using one of
available methods and contact [3mdeb](mailto:leads@3mdeb.com) or [Dasharo
Team](mailto:contact@dasharo.com) to let us know about your donation. Minimal
donating to access DTS SE with one year update support is 60EUR.

## How can I help the support team diagnose my problem faster?

If you are having issues with functionalities provided by the DTS start menu,
you can help by providing logs.

To do that, follow the instructions below:

1. Boot DTS.
2. Enable sending logs by pressing `L`.
3. Reproduce the problem.
4. The logs will be sent automatically after exiting from the menu (entering
   shell, powering off the system or rebooting using the options in DTS menu) or
   after successful or failed update/install or failed firmware restore.

If you haven't enabled sending logs, then in case of failed
update/install/restore you will be asked if you want to send them to 3mdeb:

```text
Do you want to send console logs to 3mdeb? [n/y]: y
```

!!! tip

    If the automatic log submission does not work in your case, you can view and
    copy the logs manually from `/tmp/logs/dts*.log`, `/var/local/dts-err*.log`
    and `/var/local/flashrom.log`. Depending on your platform configuration and
    connection method there might be different amount of files e.g.

    ```sh
    bash-5.2# ls /tmp/logs/
    dts-verbose_tty1.log  dts-verbose_ttyS0.log  dts_tty1.log  dts_ttyS0.log
    ```

After collecting or automatically submitting logs, please report the problem by
creating an issue on GitHub and/or "Dasharo Premier Support" Matrix channel. If
the logs contain sensitive information, such as credentials, please report the
issue via email instead.

Make sure to provide details that will help us reproduce the issue, such as the
machine model, Dasharo and DTS version, etc., in accordance with the sections of
the provided
[template](https://github.com/Dasharo/dasharo-issues/issues/new/choose) and in
case of automatically submitted logs please also include time and date when
those logs were sent.

## How can I verify DPP credentials logged in DTS?

After providing credentials and pressing "Enter", select the `s` option to enter
the console. Type the command:

```sh
cat /etc/cloud-pass
```

This command will print two lines. The first line will be the email, and the
second will be the password you provided. Verify the lines to ensure they match
your credentials.
