# Dasharo Compatibility: Sleep mode

## Test cases

### Common

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup/#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../generic-test-setup/#os-boot-from-disk).

### SLM001.001 Sleep mode - battery monitoring (Ubuntu 20.04)

**Test description**

This test verifies how quickly the battery discharges while in sleep mode in
the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
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

### SLM000.002 Sleep mode - battery monitoring (Windows 11)

**Test description**

This test verifies how quickly the battery discharges while in sleep mode in
the OS.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the [Common](#common) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
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
