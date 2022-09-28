# Dasharo Compatibility: FreeBSD support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).

## BSD001.001 FreeBSD installation and boot

**Test description**

This test verifies that FreeBSD distribution could be installed on
the DUT and works properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = FreeBSD 13

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the `OPERATING_SYSTEM` to boot and note the result.

**Expected result**

The `OPERATING_SYSTEM` login screen should be displayed.
