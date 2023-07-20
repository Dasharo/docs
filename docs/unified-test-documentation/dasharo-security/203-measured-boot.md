# Dasharo Security: Measured Boot support

## MBO001.001 Measured Boot support (Ubuntu 22.04)

**Test description**

Measured Boot is a method for detecting changes to the firmware by storing
hashes of each firmware component in the TPM PCR registers. If a PCR changes
value across reboots, a change to the firmware has been made. This test aims to
verify that Measured Boot is functional and that measurements are stored in the
TPM.a.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

```bash
sudo ./cbmem -c | grep -i PCR
```

**Expected result**

1. The output of the command should indicate that measurements of the coreboot
    components have been made.

    Example output:

    ```text
    TPM: Extending digest for `VBOOT: boot mode` into PCR 0
    TPM: Digest of `VBOOT: boot mode` to PCR 0 measured
    TPM: Extending digest for `VBOOT: GBB HWID` into PCR 1
    TPM: Digest of `VBOOT: GBB HWID` to PCR 1 measured
    TPM: Extending digest for `FMAP: FMAP` into PCR 2
    TPM: Digest of `FMAP: FMAP` to PCR 2 measured
    TPM: Extending digest for `CBFS: bootblock` into PCR 2
    TPM: Digest of `CBFS: bootblock` to PCR 2 measured
    TPM: Extending digest for `CBFS: fallback/romstage` into PCR 2
    TPM: Digest of `CBFS: fallback/romstage` to PCR 2 measured
    TPM: Extending digest for `CBFS: fspm.bin` into PCR 2
    TPM: Digest of `CBFS: fspm.bin` to PCR 2 measured
    TPM: Extending digest for `CBFS: fallback/postcar` into PCR 2
    TPM: Digest of `CBFS: fallback/postcar` to PCR 2 measured
    TPM: Extending digest for `CBFS: fallback/ramstage` into PCR 2
    TPM: Digest of `CBFS: fallback/ramstage` to PCR 2 measured
    ...
    ```

1. The output shouldn't contain the following message:

    ```text
    TPM: Extending hash into PCR failed.
    ```
