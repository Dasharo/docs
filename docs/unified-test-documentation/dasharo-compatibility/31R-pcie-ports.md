# Dasharo Compatibility: PCI Express ports support

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

## PEX001.001 PCI Express card detection (Ubuntu)

**Test description**

This test aims to verify that the PCI Express extension card is enumerated
correctly and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Plug the PCI Express extension card to the tested slot.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open a terminal window and execute the following command:

```bash
lspci
```

**Expected result**

The output of the command should contain the plugged device name:

```bash
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Turks PRO [Radeon HD 7570]
```

The exact name and revision may be different depending on hardware configuration.

## PEX001.002 PCI Express card detection (Windows)

**Test description**

This test aims to verify that the Wi-Fi/Bluetooth card is enumerated correctly
and can be detected from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
2. Plug the PCI Express extension card to the tested slot.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open Device Manager and find the plugged device
5. Note the device status.

**Expected result**

The device status in the Device Manager should indicate that the device is
working properly and has no problems.
