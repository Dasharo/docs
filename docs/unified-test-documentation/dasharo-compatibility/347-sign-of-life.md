# Dasharo compatibility: Sign of life

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).

## SOL001.001 SOL string shows Dasharo firmware and EC version

**Test description**

This test aims to verify that the information about the version of Dasharo
firmware and Dasharo EC firmware is recognized correctly and displayed during
the boot phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `EC firmware` = Dasharo

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the Sign of life string.
1. Note the results.

**Expected result**

During the boot phase, the information about the version of Dasharo firmware and
Dasharo EC firmware should be displayed.

Example output:

```bash
Firmware version: Dasahro (coreboot+UEFI) v1.5.0
EC firmware version: 2023-03-20_c398446
```

## SOL002.001 SOL string shows information about proprietary EC

**Test description**

This test aims to verify that the information about the version of Dasharo
firmware and proprietary EC firmware is recognized correctly and displayed
during the boot phase.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `EC firmware` = Proprietary

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Wait for the Sign of life string.
1. Note the results.

**Expected result**

During the boot phase, the information about the version of Dasharo firmware and
proprietary EC firmware should be displayed. In addition, the prompt asking for
updated EC firmware should be displayed also.

Example output:

```bash
Firmware version: Dasahro (coreboot+UEFI) v1.5.0
EC firmware version: 1.07.02
Proprietary EC firmware detected!
Please update your EC firmware per docs.dasharo.com instructions!
```
