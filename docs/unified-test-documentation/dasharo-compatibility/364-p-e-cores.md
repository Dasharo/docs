# Dasharo Compatibility: CPU cores enabling and disabling

## Test cases common documentation

**Important notice**

If both are technically supported, as is the case for NovaCustom NV4x, the
test should be carried out separately for both the default Intel network card
and the Atheros one.

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## CCC001.001 CPU Hyper-Threading disabled (Ubuntu)

**Test description**

This test aims to verify that the Hyper-Threading can be disabled and the change
can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep "Thread(s) per core: "
    ```

1. Compare the number with expected value.

**Expected result**

For disabled Hyper-Threading expected value is 1.

## CCC001.002 CPU Hyper-Threading enabled (Ubuntu)

**Test description**

This test aims to verify that the Hyper-Threading can be enabled and the change
can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep "Thread(s) per core: "
    ```

1. Compare the number with expected value.

**Expected result**

For disabled Hyper-Threading expected value is 2.

## CCC002.001 CPU E-cores none active, Hyper-Threading enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select 0.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of logical P-cores.

## CCC002.002 CPU E-cores all active, Hyper-Threading enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select All active.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "CPU(s):"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all logical cores.

## CCC002.003 CPU E-cores none active, Hyper-Threading disabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select 0.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:"  
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all physical P-cores.

## CCC002.004 CPU E-cores all active, Hyper-Threading disabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select All active.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all physical cores.

## CCC003.001 CPU P-cores only one active, Hyper-Threading enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all physical E-cores + 2.

## CCC003.002 CPU P-cores all active, Hyper-Threading enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "CPU(s):"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all logical cores.

## CCC003.003 CPU P-cores only one active, Hyper-Threading disabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all physical E-cores + 1.

## CCC003.004 CPU P-cores all active, Hyper-Threading disabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "Core(s) per socket:"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all physical cores.

## CCC004.001 P-cores only one active, E-cores disabled, HT disabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is not chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select 0.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "CPU(s):"
    ```

1. Compare the number with expected value.

**Expected result**

We should get a number 1.

## CCC004.002 P-cores only one active, E-cores disabled, HT enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select 0.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select 1.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "CPU(s):"
    ```

1. Compare the number with expected value.

**Expected result**

We should get a number 2.

## CCC005.001 P-cores all active, E-cores all active, HT enabled (Ubuntu)

1. Power on the DUT.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Press `F9` to reset settings to default values and press `Y` to accept.
1. Restart the system
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Verify that the `Hyper-Threading` option is chosen - if
    so, press `Space` and then `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active E-cores` option and select All active.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. While the DUT is booting, hold the `BIOS_SETUP_KEY` to enter the UEFI Setup
    Menu.
1. Enter the `Dasharo System Features` menu using the arrow keys and Enter.
1. Enter the `CPU Configuration` submenu.
1. Enter the `Number of active P-cores` option and select All active.
1. Press `F10` to save the changes.
1. If necessary - press `Y` to confirm saving the changes.
1. Go back to the main menu using the `ESC` key.
1. Select the `Reset` option to apply the settings and reboot.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Detect or install a required os package: 'util-linux'
1. Execute the following command in the terminal to check platform core count
    conditions:

    ```bash
    lscpu | grep -v "NUMA" | grep "CPU(s):"
    ```

1. Compare the number with expected value.

**Expected result**

We should get the number of all logical cores.
