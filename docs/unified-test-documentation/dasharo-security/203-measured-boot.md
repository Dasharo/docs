# Dasharo Security: Measured Boot support

## Test cases

### MBO001.001 Measured Boot support (Ubuntu 20.04)

**Test description**

Measured Boot is a method for detecting changes to firmware by storing hashes
of each firmware component into the TPM PCR registers. If a PCR changes value
across reboots, a change to the firmware has been made. This test aims to
verify that Measured Boot is functional and measurements are stored in the
TPM.a.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Ubuntu 20.04

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Download `cbmem` and `flashrom` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.
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

The output of the command should indicate that measurements of the coreboot
components have been made:

```text
TPM: Digest of FMAP: FW_MAIN_A CBFS: fallback/romstage to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fspm.bin to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fallback/postcar to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fallback/ramstage to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: cpu_microcode_blob.bin to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fsps.bin to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: vbt.bin to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fallback/dsdt.aml to PCR 2 measured
TPM: Digest of FMAP: FW_MAIN_A CBFS: fallback/payload to PCR 2 measured
```

The output should also not contain the following message:

```text
TPM: Extending hash into PCR failed.
```
