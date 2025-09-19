# Dasharo Compatibility: Suspend mechanism switching (S0ix/S3)

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).

## SMS001.001 Suspend to Idle (S0ix) check (Ubuntu)

**Test description**

This test aims to verify whether the Suspend to Idle (S0ix) option selected in
the BIOS firmware is correctly recognised in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the BIOS setup using `BIOS_SETUP_KEY`.
1. Inside the BIOS setup, navigate to `Dasharo System Features` ->
    `Power Management Options` -> `Platform Sleep Type` and choose the option
    `Suspend to Idle (S0ix)`.
1. Press `F10` and confirm with `y` key to save selected settings.
1. Select `reset` option to reboot the system.
1. After the system reboots, log into the system by using the proper login and
    password.
1. Open a terminal window and execute the following command to confirm that
    Suspend to Idle (S0ix) mode is enabled and properly recognised in the OS:

    ```bash
    sudo cat /sys/power/mem_sleep
    ```

1. Note the results.

**Expected result**

The output from the command above should contain the phrase `s2idle` enclosed
in square brackets, indicating that the Suspend to Idle (S0ix) mode is
enabled.

Example output:

```bash
[s2idle] shallow
```

## SMS001.002 Suspend to RAM (S3) check (Ubuntu)

**Test description**

This test aims to verify whether the Suspend to RAM (S3) option selected in
the BIOS firmware is correctly recognised in the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the BIOS setup using `BIOS_SETUP_KEY`.
1. Inside the BIOS setup, navigate to `Dasharo System Features` ->
    `Power Management Options` -> `Platform Sleep Type` and choose the option
    `Suspend to RAM (S3)`.
1. Press `F10` and confirm with `y` key to save selected settings.
1. Select `reset` option to reboot the system.
1. After the system reboots, log into the system by using the proper login and
    password.
1. Open a terminal window and execute the following command to confirm that
    Suspend to RAM (S3) mode is enabled and properly recognised in the OS:

    ```bash
    sudo cat /sys/power/mem_sleep
    ```

1. Note the results.

**Expected result**

The output from the command above should contain the phrase `deep` enclosed
in square brackets, indicating that the Suspend to RAM (S3) mode is
enabled.

Example output:

```bash
s2idle [deep]
```
