# Dasharo Compatibility: Sleep mode

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

## SLM001.001 Sleep mode - battery monitoring (Ubuntu)

**Test description**

This test verifies how quickly the battery discharges while in sleep mode in
the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Charge the battery fully (note: due to the manufacturer's settings the
    maximum battery charge level is limited to 90%; also, the battery charging
    process can only be started if the current battery level is less than 80%).
1. Disconnect the power supply.
1. Close the lid.
1. Wake up the DUT in the following timestamps and note the battery level:
    * 1 hour from fully charging,
    * 2 hours from fully charging,
    * 3 hours from fully charging,
    * 6 hours from fully charging,
    * (optional) 24 hours from fully charging.

**Expected result**

1. The battery should discharge at a similar rate as in the table below (take
   the battery wear into account).

| Time           | Battery level    |
| :------------: |:----------------:|
| 0h             | 90%              |
| 1h             | 88%              |
| 2h             | 86%              |
| 3h             | 84%              |
| 6h             | 80%              |
| 24h (optional) | 57%              |

## SLM000.002 Sleep mode - battery monitoring (Windows)

**Test description**

This test verifies how quickly the battery discharges while in sleep mode in
the OS.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Charge the battery fully (note: due to the manufacturer's settings the
    maximum battery charge level is limited to 90%; also, the battery charging
    process can only be started if the current battery level is less than 80%).
1. Wait 30 seconds for the system to load fully.
1. Disconnect the power supply.
1. Close the lid.
1. Wake up the DUT in the following timestamps and note the battery level:
    * 1 hour from fully charging,
    * 2 hours from fully charging,
    * 3 hours from fully charging,
    * 6 hours from fully charging,

**Expected result**

1. The battery should discharge at a similar rate as in the table below (take
   the battery wear into account).

| Time           | Battery level    |
| :------------: |:----------------:|
| 0h             | 90%              |
| 1h             | 79%              |
| 2h             | 69%              |
| 3h             | 58%              |
| 6h             | 26%              |
