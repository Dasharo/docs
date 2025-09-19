# Dasharo Security: Boot Guard support

## BGS001.001 Boot Guard support (Ubuntu)

**Test description**

Intel Boot Guard is a hardware-based technology intended to protect the device
against executing non-genuine firmware, which could happen when a possible
attacker has bypassed protection against modification of BIOS. This test aims
to verify that the implemented Boot Guard mechanism works correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).
1. Download `cbmem` from the
    [cloud](https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd) to the DUT.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command:

    ```bash
    sudo ./cbmem -1 | grep CBnT
    ```

1. Analyze the output from the command.

**Expected result**

The output of the command should indicate the state of the Boot Guard.

Example output:

```bash
CBnT: SACM INFO MSR (0x13A) raw: 0x000000130000007d
CBnT:   NEM status:                 1
CBnT:   TPM type:                   TPM 2.0
CBnT:   TPM success:                1
CBnT:   FACB:                       1
CBnT:   measured boot:              1
CBnT:   verified boot:              1
CBnT:   revoked:                    0
CBnT:   BtG capable:                1
CBnT:   Server TXT capable:         0
CBnT: BOOTSTATUS (0xA0) raw: 0x1840000080000000
CBnT:   TXT startup success:        0
CBnT:   BtG startup success:        1
CBnT:   Block boot enabled:         0
CBnT:   PFR startup success:        0
CBnT:   Memory power down executed: 0
CBnT:   BtG thread sync failed:     0
CBnT:   Bios trusted:               1
CBnT:   TXT disabled by policy:     1
CBnT:   Bootguard startup error:    0
CBnT:   TXT ucode or ACM error:     0
CBnT:   S-ACM success:              0
CBnT: ERRORCODE (0x30) raw: 0x00000000
CBnT: TXT disabled in Policy
CBnT: BIOSACM_ERRORCODE (0x328) raw: 0xc000acf0
CBnT: BIOSACM_ERRORCODE: TXT ucode or ACM error
CBnT:   AC Module Type:          BIOS ACM Error
CBnT:   class:                   0xf
CBnT:   major:                   0xb
CBnT:   External:                0x1
```

During the analyzing process, the main thing is to pay attention to the
following:

1. The field `NEM status` should have the value 1.
1. If the Boot Guard profile is 4 or 5, the field `FACB` should have the value
    1.
1. If the Boot Guard profile is 3 or 5, the fields `measured boot` and
    `verified boot` should have the value 1.
1. If TPM is physically mounted on the platform, the `TPM type` field should
    contain information about the type of the mounted TPM; also, in that
    situation, field `TPM success` should have the value 1.
