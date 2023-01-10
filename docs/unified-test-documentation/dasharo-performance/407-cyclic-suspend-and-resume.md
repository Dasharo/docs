# Dasharo Performance: Cyclic platform suspend and resume

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Install the [Firmware test suite](https://wiki.ubuntu.com/FirmwareTestSuite)
    package.

## CPS001.001 Cyclic platform suspend and resume (Ubuntu 22.04)

**Test description**

This test aims to verify that the DUT platform suspend and resume procedure
performed cyclically works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    sudo fwts s3 --results-output=stderr
    ```

    > Note: suspend test duration is set defaultly to 30 seconds. After
    that time the device should be woken up automatically.

1. Log into the system again.
1. Note the results.
1. Repeat steps 4-6 to determine the stability of suspend and resume procedure.

**Expected result**

Each time, the suspend and resume procedure is performed, the output of the
command should contain information about test results (section
`Test Failure Summary`).

The test case passes only if after every iteration of the suspend and resume
procedure the summary section shows that all minor tests included in `s3` test
have been passed.

Example output for one iteration:

```bash
Test Failure Summary
================================================================================

Critical failures: NONE

High failures: NONE

Medium failures: NONE

Low failures: NONE

Other failures: NONE

Test           |Pass |Fail |Abort|Warn |Skip |Info |
---------------+-----+-----+-----+-----+-----+-----+
s3             |    9|     |     |     |     |     |
---------------+-----+-----+-----+-----+-----+-----+
Total:         |    9|    0|    0|    0|    0|    0|
---------------+-----+-----+-----+-----+-----+-----+
```
