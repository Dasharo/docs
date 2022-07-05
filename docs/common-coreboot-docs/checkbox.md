# Checkbox usage (Ubuntu 22.04)

## Install Ubuntu ???

## Download and install Checkbox

1. Open terminal and type in below-described commands to install Checkbox and
all its dependencies:

    ```bash
    $ sudo add-apt-repository ppa:hardware-certification/public
    $ sudo apt-get update
    $ sudo apt-get install checkbox-ng plainbox-provider-resource-generic \
    plainbox-provider-certification-client plainbox-provider-checkbox \ 
    canonical-certification-client
    ```

## Set up testing environment

Fill all slots - TBD

We need to set up automatic login so that a password is not required during
testing reboot etc.
1. Press the `SUPER_KEY`, type in `Users` and click Enter. Window with options to
change should appear.
1. Next click the user name you want to enable and disable automatic login. 
1. Then on the top right side of the window click `Unlock...` button.
1. You will be required to enter your user password to continue.
1. You should now be able to toggle Automatic Login button to enable.
1. Restart your system for changes to take effect.

## Run automatic validation

1. Start checkbox. To do this, open terminal and run the following command:

    ```bash
    $ sudo checkbox-cli
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

1. Select test suites (`SPACE` - select, `ARROWS` - navigation, `Enter` -
go to the next test suite), which you want to run. If you check all the test
suites, the checkbox menu should look as follows:

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

1. When testing end, menu with test results should appear. Press `R` to rerun
test cases, or `F` to finish.

1. Links to the test results should be displayed in the terminal. - Should be 
updated after tests.TBD

## Aditional options

1. `run` lets you run particular test plan or a set of jobs, but it not save any
   results. Example of run one test plan:

    ```bash
    sudo checkbox-cli run com.canonical.certification::smoke
    ```

2. `launcher` command lets you customize checkbox experience. To use it, you 
   need to create `config_file.ini` and start run checbox like bellow:

    ```bash
    checkbox-cli launcher config_file.ini
    ```
    
For more details about this commands and also other visit 
[checkboc-cli](https://checkbox.readthedocs.io/en/latest/using.html#).
