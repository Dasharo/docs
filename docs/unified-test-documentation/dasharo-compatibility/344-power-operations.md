# Dasharo compatibility: Device power control operations

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

## DPC001.001 Reset button (QubesOS)

**Test description**

This test aims to verify that the reset button works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Observe the power LED and use the reset button.
1. Note the results.

**Expected result**

1. The DUT should perform a reset, the power LED should be on all the time.
1. The DUT shouldn't perform a power cycle, the power LED shouldn't be off even
   for a moment.
