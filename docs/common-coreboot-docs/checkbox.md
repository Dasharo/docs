# Checkbox usage (Ubuntu 22.04)

## Introduction

Checkbox is a system testing platform for Ubuntu. It aims to provide a common
framework to run all types of tests, from hardware tests, to command line tests,
unit tests or desktop tests. This document describes the usage of Checkbox on
Ubuntu 22.04, but it can work on older versions of Ubuntu.

## Prerequisites

To achieve the best results from the tests and do many of them, we should fill
as many internal and external slots as possible. Before running the checkbox,
try to fill the slots if the DUT has one:

External:
* Memory Card Reader
* USB Ports
* Monitor Ports
* Ethernet Ports
* Headphone and Microphone Jacks
* Thunderbolt Ports
* Power Socket
* PCMCIA or ExpressCard slot

Internal:
* DIMM/RAM slots
* SATA ports
* PCI/PCIe slots
* M.2 slots
* TPM header
* Other slots

## Set up testing environment

In order for the tests to not require any interference after their startup,
perform the following steps:

To stop the screen from being locked on suspend, open the terminal and run the
following command:

```bash
 gsettings set org.gnome.desktop.lockdown disable-lock-screen 'true'
```

To execute all sudo commands without password, open the terminal and run the
following command:

```bash
sudo visudo
```

Append the following entry at the end of file to run ALL commands without a
password for a user:

```bash
user ALL=(ALL) NOPASSWD:ALL
```

To set up automatic login so that a password is not required during testing
reboot, poweroff etc.:

1. Press the `SUPER_KEY`, type in `Users` and click Enter. Window with options to
change should appear.
1. Next click the user name you want to enable and disable automatic login.
1. Then on the top right side of the window click `Unlock...` button.
1. You will be required to enter your user password to continue.
1. You should now be able to toggle Automatic Login button to enable.
1. Restart your system for changes to take effect.

## Download and install Checkbox

1. Disable Secure Boot. To do this you can follow steps described in
   [Secure Boot test](https://docs.dasharo.com/unified-test-documentation/dasharo-security/206-secure-boot/).

> Diable Secure boot is required to properly download packages.

1. Open the terminal and type in the below-described commands to install
Checkbox and all its dependencies:

    ```bash
    sudo add-apt-repository ppa:hardware-certification/public
    sudo apt-get update
    sudo apt-get install checkbox-ng plainbox-provider-resource-generic \
    plainbox-provider-certification-client plainbox-provider-checkbox \
    canonical-certification-client
    ```

## Run automatic validation

1. Start checkbox. To do this, open the terminal and run the following command:

    ```bash
    sudo checkbox-cli
    ```

    After using the above-mentioned command, the following menu should appear:

    ```bash
    ┌──────────────────────────────────────────────────────────────────────────────┐
    │    (X) (Deprecated) Fully Automatic Client Certification Tests               │
    │    ( ) After suspend Dock Cert blocker tests                                 │
    │    ( ) After suspend Dock Cert tests                                         │
    │    ( ) After suspend Dock Hot-plug Cert tests                                │
    │    ( ) After suspend Dock Hot-plug tests                                     │
    │    ( ) After suspend LED and oops tests (using special sleep key)            │
    │    ( ) After suspend LED and oops tests (using special sleep key, cert.      │
    │        blockers only)                                                        │
    │    ( ) After suspend automated USB 3 write/read/compare tests on storage     │
    │        devices                                                               │
    │    ( ) After suspend automated USB write/read/compare tests on storage       │
    │        devices                                                               │
    │    ( ) After suspend reference tests                                         │
    │    ( ) After suspend reference tests (automated)                             │
    │    ( ) After suspend reference tests (certification blockers only)           │
    │    ( ) After suspend tests (discrete GPU automated)                          │
    │    ( ) After suspend tests (discrete GPU manual)                             │
    │    ( ) After suspend tests (discrete GPU)                                    │
    │    ( ) After suspend tests (discrete GPU, certification blockers only)       |
            .
            .
            . etc.
    └──────────────────────────────────────────────────────────────────────────────┘
    ```

> Marking the first option starts the full automate check.

1. Select test suites (`SPACE` - select, `ARROWS` - navigation, `Enter` -
go to the next test suite), which you want to run. Marking the first option
starts the full automate check. After it all modules should be displayed and you
can manually uncheck some modules, which you don't want to test it.

    ```bash
    ┌──────────────────────────────────────────────────────────────────────────────┐
    │[X] + Audio tests                                                             │
    │[X] + Benchmarks tests                                                        │
    │[X] + Bluetooth tests                                                         │
    │[X] + CPU tests                                                               │
    │[X] + Camera tests                                                            │
    │[X] + Disk tests                                                              │
    │[X] + Ethernet Device tests                                                   │
    │[X] + Firmware tests                                                          │
    │[X] + Graphics tests                                                          │
    │[X] + Informational tests                                                     │
    │[X] + Input Devices tests                                                     │
    │[X] + Memory tests                                                            │
    │[X] + Miscellaneous tests                                                     │
    │[X] + Mobile broadband tests                                                  │
    │[X] + Non-device specific networking tests                                    │
    │[X] + Optical Drive tests                                                     │
    │[X] + Power Management tests                                                  │
    │[X] + Suspend tests                                                           │
    │[X] + TPM 2.0 (Trusted Platform Module)                                       │
    │[X] + Touchpad tests                                                          │
            .
            .
            . etc.
    └──────────────────────────────────────────────────────────────────────────────┘
    ```

1. Press `T` to start the testing procedure.
1. You can be asked about hardware in your machine. Just tick it truthfully and
press `T` again.

    ```bash
    ┌──────────────────────────────────────────────────────────────────────────────┐
    │Does this machine have this piece of hardware?                                │
    │    An Ethernet Port                              (X) YES  ( ) NO             │
    │    Camera/Capture Device                         (X) YES  ( ) NO             │
    │    USB Storage Device Connected                  (X) YES  ( ) NO             │
    └──────────────────────────────────────────────────────────────────────────────┘
    ```

1. When testing end, menu with test results should appear. Press `R` to rerun
test cases, or `F` to finish.

1. After all, paths to the tests results should be displayed in terminal.
By default, they are placed in `/home/user/.local/share/checkbox-ng`.

## Additional options

1. `run` lets you run particular test plan or a set of jobs, but it not save any
   results. Example of run one test plan:

    ```bash
    sudo checkbox-cli run com.canonical.certification::smoke
    ```

2. `launcher` command lets you customize checkbox experience. To use it, you
   need to create `config_file.ini` and start run checkbox like bellow:

    ```bash
    checkbox-cli launcher config_file.ini
    ```

For more details about this commands and also other visit
[checkboc-cli](https://checkbox.readthedocs.io/en/latest/using.html#).

## Troubleshooting

When somehow checkbox will stop work you can resume previous session.
To do this open terminal and run following command:

```bash
sudo checkbox-cli
```

If at least on machine is 1 incomplete session:

```bash
 Do you want to resume session 'session_title-2022-07-06T13.09.22'?
  r => resume this session
  n => next session
  c => create new session
  d => delete old sessions
[rncd]:
```

Type in `r` to resume stopped session. You can also create new session or
delete old session by typing the appropriate letter.

```bash
What do you want to do with that job?
  s => skip that job
  p => mark it as passed and continue
  f => mark it as failed and continue
  r => run it
[spfr]:
```

Decide what do you want with the last test and type in the appropriate letter.
After this your checkbox session will be resumed.
