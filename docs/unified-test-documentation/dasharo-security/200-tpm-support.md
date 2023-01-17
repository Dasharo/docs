# Dasharo Security: TPM Support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).

## TPM001.001 TPM Support (firmware)

**Test description**

This test aims to verify that the TPM is initialized correctly and the PCRs can
be accessed from the firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter the shell.
1. Run the following command in the shell:

    ```powershell
    cbmem -L
    ```

**Expected result**

The command should return information about the TPM log entries.

Example output:

```bash
TPM2 log:
    Specification: 2.00
    Platform class: PC Client
    No vendor information provided
TPM2 log entry 1:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: f78a530fb5a70afcffdc86a98529abd24a90bac9
    Event data: FMAP: FMAP
TPM2 log entry 2:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: 369155e6eab3b0a874140e591a4c0e992268b4b9
    Event data: FMAP: BOOTBLOCK
TPM2 log entry 3:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: 5e785c080264aa6e169f70c80ac40b556066292b
    Event data: FMAP: COREBOOT CBFS: fallback/romstage
TPM2 log entry 4:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: ba2a5af955811fbac58a5198545539596eb38c3e
    Event data: FMAP: COREBOOT CBFS: fallback/ramstage
TPM2 log entry 5:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: ba35d4ce29d7b633b5644e2a3206c6069cf7f24d
    Event data: FMAP: COREBOOT CBFS: fallback/payload
TPM2 log entry 6:
    PCR: 2
    Event type: Action
    Digests:
         SHA1: 47b49026133377e05193f8440c9a7cad239e883c
    Event data: FMAP: COREBOOT CBFS: 1-cpu.dtb
TPM2 log entry 7:
    PCR: 3
    Event type: Action
    Digests:
         SHA256: 6e7b06693452d997ac534e823b1ea79e5bb8ed19ba8a7af878abf10199c3d515
         SHA1: 6e7b06693452d997ac534e823b1ea79e5bb8ed19
    Event data: VERSION
TPM2 log entry 8:
    PCR: 2
    Event type: Action
    Digests:
         SHA256: de73053377e1ae5ba5d2b637a4f5bfaeb410137722f11ef135e7a1be524e3092
         SHA1: de73053377e1ae5ba5d2b637a4f5bfaeb4101377
    Event data: IMA_CATALOG
TPM2 log entry 9:
    PCR: 4
    Event type: Action
    Digests:
         SHA256: ba427f9349b1f9e589f98909e26086b0cfd5ced78a7fbcb140a70a506c38a8e5
         SHA1: ba427f9349b1f9e589f98909e26086b0cfd5ced7
    Event data: BOOTKERNEL
(...)
```

## TPM001.002 TPM Support (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM is initialized correctly and the PCRs can
be accessed from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check the version of installed tpm2-tools - execute the following command
    in the terminal:

    ```bash
    dpkg --list tpm2-tools
    ```

1. If your device is equipped with TPM2.0 and the version of `tpm2-tools`
    is 4.0 or higher - execute the following command in the terminal:

    ```bash
    tpm2_pcrread
    ```

1. If your device is equipped with TPM2.0 and the version of `tpm2-tools`
    is lower than 4.0 - execute the following command in the terminal:

    ```bash
    tpm2_pcrlist
    ```

1. If your device is equipped with TPM1.2 - execute the following command in the
    terminal:

    ```bash
    cat /sys/class/tpm/tpm0/pcrs
    ```

**Expected result**

The command should return a list of PCRs and their contents.

Output example for TPM2.0:

```text
sha1 :
  0  : 3a3f780f11a4b49969fcaa80cd6e3957c33b2275
  1  : 8a074fdf65a11e5dbf02d25e7f26b00c26c98b41
  2  : c36c2509d636c9cfa075d6d0a03b7a37bec14ee9
  3  : 3a3f780f11a4b49969fcaa80cd6e3957c33b2275
  4  : 2d247bb671ec17ded623ca45967df5482517291b
  5  : 49d543eb1d1df3439d9fca695ee47b8cdf4b9e2f
  6  : 3a3f780f11a4b49969fcaa80cd6e3957c33b2275
  7  : 3a3f780f11a4b49969fcaa80cd6e3957c33b2275
  8  : 0000000000000000000000000000000000000000
  9  : 0000000000000000000000000000000000000000
  10 : 0000000000000000000000000000000000000000
  11 : 0000000000000000000000000000000000000000
  12 : 0000000000000000000000000000000000000000
  13 : 0000000000000000000000000000000000000000
  14 : 0000000000000000000000000000000000000000
  15 : 0000000000000000000000000000000000000000
  16 : 0000000000000000000000000000000000000000
  17 : ffffffffffffffffffffffffffffffffffffffff
  18 : ffffffffffffffffffffffffffffffffffffffff
  19 : ffffffffffffffffffffffffffffffffffffffff
  20 : ffffffffffffffffffffffffffffffffffffffff
  21 : ffffffffffffffffffffffffffffffffffffffff
  22 : ffffffffffffffffffffffffffffffffffffffff
  23 : 0000000000000000000000000000000000000000
sha256 :
  0  : d27cc12614b5f4ff85ed109495e320fb1e5495eb28d507e952d51091e7ae2a72
  1  : b29a64bd6895966b777eb803f45e6bbffade81cc1b996a34f7cbd26f1d04028b
  2  : 3122422e43b9fbfc0cb70eb467b55e99ec61462370e6b15c515484f821e1d4d9
  3  : 909e4261938378c0556a4c335c38718d1c313bd151fdf222df674aabb7aeee97
  4  : 984763b42633ee11e5167e2f67c2e6879bd6efac683f1df1ef16d7ce96d4b49b
  5  : dab92c45eeb765e29784f8cc33f92d0a39afed173f2b07e0e328586c3c3b19ed
  6  : d27cc12614b5f4ff85ed109495e320fb1e5495eb28d507e952d51091e7ae2a72
  7  : d27cc12614b5f4ff85ed109495e320fb1e5495eb28d507e952d51091e7ae2a72
  8  : 0000000000000000000000000000000000000000000000000000000000000000
  9  : 0000000000000000000000000000000000000000000000000000000000000000
  10 : 0000000000000000000000000000000000000000000000000000000000000000
  11 : 0000000000000000000000000000000000000000000000000000000000000000
  12 : 0000000000000000000000000000000000000000000000000000000000000000
  13 : 0000000000000000000000000000000000000000000000000000000000000000
  14 : 0000000000000000000000000000000000000000000000000000000000000000
  15 : 0000000000000000000000000000000000000000000000000000000000000000
  16 : 0000000000000000000000000000000000000000000000000000000000000000
  17 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  18 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  19 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  20 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  21 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  22 : ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
  23 : 0000000000000000000000000000000000000000000000000000000000000000
```

Output example for TPM1.2:

```text
PCR-00: B3 F3 60 E1 D5 1F 82 D4 62 E6 B9 69 92 2F 65 F4 9F 1A 5F 8E
PCR-01: 21 9F 1F 4A C1 AD AD 4D F1 8B 9F AB 98 23 68 B1 73 A6 32 87
PCR-02: 40 CF E3 DC A7 FF 67 FB AA BB 20 85 A4 39 43 D8 54 A7 AB 98
PCR-03: E3 E7 E6 89 CA FB F5 75 38 95 D0 CD 83 96 F6 0C 38 04 DC D5
PCR-04: 01 7A 3D E8 2F 4A 1B 77 FC 33 A9 03 FE F6 AD 27 EE 92 BE 04
PCR-05: 93 6A 12 98 07 73 85 9D 91 27 61 82 E7 11 C5 1D 08 98 C4 28
PCR-06: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-07: 3A 3F 78 0F 11 A4 B4 99 69 FC AA 80 CD 6E 39 57 C3 3B 22 75
PCR-08: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-09: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-11: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-12: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-13: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-14: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-15: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-16: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
PCR-17: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-18: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-19: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-20: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-21: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-22: FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF
PCR-23: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
```

## TPM001.003 TPM Support (Windows 11)

**Test description**

This test aims to verify that the TPM is initialized correctly and the PCRs can
be accessed from the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a PowerShell as administrator and run the following command:

    ```PowerShell
    get-tpm
    ```

**Expected result**

The command should return information about the TPM state: if the TPM is
present, ready and enabled:

```powershell
TpmPresent     : True
TpmReady       : True
TpmEnabled     : True

```

## TPM002.001 Verify TPM version (firmware)

**Test description**

This test aims to verify that the TPM version is correctly recognized by the
firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter the shell.
1. Run the following command in the shell:

    ```powershell
    cbmem -L
    ```

**Expected result**

The output of the command should contain information about the TPM version.

Example output:

```bash
TPM2 log:
    Specification: 2.00
```

## TPM002.002 Verify TPM version (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM version is correctly recognized by the
operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check the version of installed tpm2-tools - execute the following command
    in the terminal:

    ```bash
    dmesg | grep -i tpm
    ```

**Expected result**

The command should return information about the TPM version.

Example output:

```bash
tpm_tis 00:07: 1.2 TPM (device-id 0x0, rev-id 78)
```

## TPM002.003 Verify TPM version (Windows 11)

**Test description**

This test aims to verify that the TPM version is correctly recognized by the
operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a PowerShell as administrator and run the following command:

    ```PowerShell
    wmic /namespace:\\root\cimv2\security\microsofttpm path win32_tpm get * /format:textvaluelist.xsl
    ```

**Expected result**

The command should return information about the TPM version.

Example output:

```text
SpecVersion=2.0
```

## TPM003.001 Check TPM Physical Presence Interface (firmware)

**Test description**

This test aims to verify that the TPM Physical Presence Interface is supported
by the firmware.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04
3. Download `cbmem` from <https://cloud.3mdeb.com/index.php/s/zTqkJQdNtJDo5Nd>
   to the DUT.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open the terminal and run the following command and note results:

    ```bash
    sudo cbmem -1 |grep PPI
    ```

**Expected result**

The `cbmem.log` should contain the following lines (the hex numbers may be
different per platform):

```txt
[DEBUG]  PPI: Pending OS request: 0x0 (0x0)
[DEBUG]  PPI: OS response: CMD 0x39073907 = 0x0
[DEBUG]    TPM PPI     8. 0x76ffe620 0x0000015a
```

If the above lines are present, the firmware supports TPM PPI.

## TPM003.002 Check TPM Physical Presence Interface (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM Physical Presence Interface is correctly
recognized by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04
3. Platform with TPM 2.0 module present.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open the terminal and run the following command to check the version of TPM
   PPI in sysfs:

    ```bash
    cat /sys/class/tpm/tpm0/ppi/version
    ```

**Expected result**

The command should return information about the TPM PPI version (only 1.3 is
valid). If PPI is not available the file will not be found and test fails.

Example output:

```bash
$ cat /sys/class/tpm/tpm0/ppi/version
1.3
```

## TPM003.003 Check TPM Physical Presence Interface (Windows 11)

**Test description**

This test aims to verify that the TPM Physical Presence Interface is correctly
recognized by the operating system.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Windows 11
3. Platform with TPM 2.0 module present.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
2. Boot into the system.
3. Log into the system by using the proper login and password.
4. Open a PowerShell as administrator and run the following command:

    ```PowerShell
    tpmtool getdeviceinformation
    ```

**Expected result**

The command should return information about the TPM PPI version (only 1.3 is
valid). If PPI is not available on the list, test fails.

Example output:

```PowerShell
tpmtool getdeviceinformation

-TPM Present: True
-TPM Version: 2.0
-TPM Manufacturer ID: INTC
-TPM Manufacturer Full Name: Intel
-TPM Manufacturer Version: 600.18.0.0
-PPI Version: 1.3
-Is Initialized: True
-Ready For Storage: True
-Ready For Attestation: True
-Is Capable For Attestation: True
-Clear Needed To Recover: False
-Clear Possible: True
-TPM Has Vulnerable Firmware: False
-Maintenance Task Complete: True
-Bitlocker PCR7 Binding State: Binding Not Possible
-TPM Spec Version: 1.38
-TPM Errata Date: Wednesday, December 18, 2019
-PC Client Version: 1.04
-Lockout Information:
	-Is Locked Out: False
	-Lockout Counter: 0
	-Max Auth Fail: 32
	-Lockout Interval: 7200s
	-Lockout Recovery: 86400s
```

## TPM003.004 Change active PCR banks with TPM PPI (firmware)

**Test description**

This test aims to verify that the TPM Physical Presence Interface is working
properly in the firmware by changing active TPM PCR banks.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. Platform with TPM 2.0 module present.
3. `TPM003.001` indicating that TPM PPI is supported.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
2. Boot into the firmware setup using the `BIOS_SETUP_KEY`.
3. Enter the `Device Manager` -> `TCG2 Configuration`.
4. Scroll down to the bottom of the page using arrow down key.
5. Switch active PCR banks depending on the currently active banks.:
   - if both SHA1 and SHA256 are active, deactivate SHA1
   - if SHA1 only is active, activate SHA256 and deactivate SHA1
   - if SHA256 only is active, activate SHA1 and deactivate SHA256
6. Press `F10` to save and go back to the main setup page using `ESC` key.
7. Use the `Reset` option on the main setup page to reboot the DUT.
8. After reset a prompt should appear explaining a TPM state change request has
   been made. Press `F12` as instructed to apply changes. The DUT will need to
   reboot again.
9. After the reboot enter the `Device Manager` -> `TCG2 Configuration` again.
10. Scroll down to the bottom of the page using arrow down key.
11. Verify the active PCR banks were changed according to the choice made in
    step 5.

NOTE: Certain TPMs like Intel PTT (fTPM) do not allow to set more than one
active PCR bank at a given time, that is why the test case keeps only one bank
active. Discrete TPMs may have multiple banks enabled simultaneously, but it is
TPM module and TPM firmware dependent.

**Expected result**

1. The prompt appears at step 8.
2. The requested changes are applied as verified in step 11.

The prompt seen on the DUT screen has the following format (example change from
SHA256 to SHA1):

```txt
A configuration change was requested to PCR bank(s) of this computer's TPM
(Trusted Platform Module)

WARNING: Changing the PCR bank(s) of the boot measurements may prevent the
Operating System from properly processing the measurements. Please check if
your Operating System supports the new PCR bank(s).
WARNING: Secrets in the TPM that are bound to the boot state of your machine
may become unusable.
Current PCRBanks is 0x2. (SHA256)
New PCRBanks is 0x1. (SHA1)

Press F12 change the boot measurements to use PCR bank(s) of the TPM
Press ESC to reject this change request and continue
```

## TPM009.001 CREATEPRIMARY Function Verification (Ubuntu 22.04)

**Test description**

This test aims to verify that CREATEPRIMARY function works as expected. This
command is used to create a primary object under one of the hierarchies: Owner,
Platform, Endorsement, NULL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `tpm2-tools` using:

    ```bash
    sudo apt-get install tpm2-tools
    ```

    Alternativley, use:
    [building from source](https://tpm2-tools.readthedocs.io/en/latest/INSTALL/)
    .

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute command in the terminal:

    ```bash
    sudo tpm2_createprimary -c primary.ctx --format=pem --output=public.pem
    ```

1. Note the result

**Expected result**

1. Output should contain information abou created primary object, and look
    similar as below:

    ```bash
    name-alg:
      value: sha256
      raw: 0xb
    attributes:
      value: fixedtpm|fixedparent|sensitivedataorigin|userwithauth|restricted|decrypt
      raw: 0x30072
    type:
      value: rsa
      raw: 0x1
    exponent: 65537
    bits: 2048
    scheme:
      value: null
      raw: 0x10
    scheme-halg:
      value: (null)
      raw: 0x0
    sym-alg:
      value: aes
      raw: 0x6
    sym-mode:
      value: cfb
      raw: 0x43
    sym-keybits: 128
    rsa: b24f8e578d946a2157b1b442940fd5236bcc5041cfae37a56515eb28be8d7c06435d7356ce6c635c17cfc98031217fb462d94dc62821f0e0f2912012660305279a12a9359f23ba25cddb47f1e18d17b4af7bf8ef16d8daf65b9a5df8d669366ba2c9f7b187c64f59d6a79a3bb5b5f96e54529e69b3235311a87bf49c84b71cde1df5c6f82bf468653d9013c430044eb44ece988fecb59d4cfc37d4575d0dca1b68ad0893aa85eb8159c8c71dca0482e5915a28da456668a07a55dc5691e9c8863125e58d41de1cf7b6b97f35148a08c241a20571dfce16522b95f04a5be0fb5fff05c5075fb6d7921d87056169bb02adc31af257fbc512ebe0d95b18a3f94dad
    ```

## TPM010.001 NVDEFINE and NVUNDEFINE Functions Verification (Ubuntu 22.04)

**Test description**

This test aims to verify that NVDEFINE and NVUNDEFINE functions are working as
expected. Those functions are used to define and undefine a TPM Non-Volatile
(NV) index.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `tpm2-tools` using:

    ```bash
    sudo apt-get install tpm2-tools
    ```

    Alternativley, use:
    [building from source](https://tpm2-tools.readthedocs.io/en/latest/INSTALL/)
    .

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute commands in the terminal:

    ```bash
    sudo tpm2_nvdefine -C o -s 32 -a "ownerread|policywrite|ownerwrite" 1
    echo "nvtest" > nv.dat
    sudo tpm2_nvwrite -C o -i nv.dat 1
    sudo tpm2_nvread -C o -s 32 1
    ```

1. Note the result
1. Execute commands in the terminal:

    ```bash
    sudo tpm2_nvundefine -C o 1
    tpm2_nvread -C o -s 32 1
    ```

1. Note the result

**Expected result**

1. First output should show newly created NV index contents and look similar as
    below:

    ```bash
    nvtest
    ```

1. Second output should throw error indicating that object doesn't exist and it
    should look similar as below:

    ```bash
    WARNING:esys:src/tss2-esys/api/Esys_NV_ReadPublic.c:309:Esys_NV_ReadPublic_Finish() Received TPM Error
    ERROR:esys:src/tss2-esys/esys_tr.c:209:Esys_TR_FromTPMPublic_Finish() Error NV_ReadPublic ErrorCode (0x0000018b)
    ERROR:esys:src/tss2-esys/esys_tr.c:320:Esys_TR_FromTPMPublic() Error TR FromTPMPublic ErrorCode (0x0000018b)
    ERROR: Esys_TR_FromTPMPublic(0x18B) - tpm:handle(1):the handle is not correct for the use
    ERROR: Unable to run tpm2_nvread
    ```

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute command in the terminal:

    ```bash
    sudo tpm2_nvundefine 0x1500016
    ```

1. Note the result

**Expected result**

1. Output should be empty. If region was undefined or error occurred output
    should look like this:

    ```bash
    WARNING:esys:src/tss2-esys/api/Esys_NV_ReadPublic.c:309:Esys_NV_ReadPublic_Finish() Received TPM Error
    ERROR:esys:src/tss2-esys/esys_tr.c:209:Esys_TR_FromTPMPublic_Finish() Error NV_ReadPublic ErrorCode (0x0000018b)
    ERROR:esys:src/tss2-esys/esys_tr.c:320:Esys_TR_FromTPMPublic() Error TR FromTPMPublic ErrorCode (0x0000018b)
    ERROR: Esys_TR_FromTPMPublic(0x18B) - tpm:handle(1):the handle is not correct for the use
    ERROR: Failed to read the public part of NV index 0x1500016
    ERROR: Unable to run tpm2_nvundefine
    ```

## TPM011.001 CREATE Function (Ubuntu 22.04)

**Test description**

This test aims to verify that CREATE function works as expected. It will create
an object using all the default values and store the TPM sealed private and
public portions to the paths specified via `-u` and `-r` respectively.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install `tpm2-tools` using:

    ```bash
    sudo apt-get install tpm2-tools
    ```

    Alternativley, use:
    [building from source](https://tpm2-tools.readthedocs.io/en/latest/INSTALL/)
    .

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Execute command in the terminal:

    ```bash
    sudo tpm2_create -C primary.ctx -u obj.pub -r obj.priv
    ```

1. Note the result

**Expected result**

1. Output should contain information about newly created object, and look
similar as below:

    ```bash
    name-alg:
      value: sha256
      raw: 0xb
    attributes:
      value: fixedtpm|fixedparent|sensitivedataorigin|userwithauth|decrypt|sign
      raw: 0x60072
    type:
      value: rsa
      raw: 0x1
    exponent: 65537
    bits: 2048
    scheme:
      value: null
      raw: 0x10
    scheme-halg:
      value: (null)
      raw: 0x0
    sym-alg:
      value: null
      raw: 0x10
    sym-mode:
      value: (null)
      raw: 0x0
    sym-keybits: 0
    rsa: ae99d4e1d6cebe30c3b26b891e63965af65d82ff10fe2e476b961e23df4a60f5b42472dae9abe4c8462b172c06b2017ec3883292b91078c488ce3c7ef6b5089b62120cb85eb4a36cf6573e09fbc4b06c27c37ea35044f71825ff6735da039d0d3d16325c11183194be2eb1ca3cf05e8fd96ae8086034650a21298c081cad51dfce7334e2fef70c4be0eff62c1eb1cef39433b90f93fd653d9ef5e2ad9769c303f4645579f12691fbd112260da3f9615f73af43edc8bf537748be1507e5f878f52eed2161986ac066cc35216e6ea1a6da0a8f192a341c9d383c420c5c2172805a45afb34a9ce3a6f262acb8ece5351206c9b520909a579ba221c4cdd587f9502f
    ```

## TPM013.001 Signing the file (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM supports file signing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal and run the following command to clear TPM:

    ```bash
    sudo tpm2_clear
    ```

1. Run the following set of commands to generate the required keys and files:

    ```bash
    sudo tpm2_createprimary -c primary_key.ctx
    sudo tpm2_create -u key.pub -r key.priv -C primary_key.ctx
    sudo tpm2_load -C primary_key.ctx -u key.pub -r key.priv -c key.ctx
    echo "my secret" > secret.data
    ```

1. Run the following command to sign the file:

    ```bash
    sudo tpm2_sign -c key.ctx -o sig.rssa secret.data
    ```

1. Run the following command to verify the signed file:

    ```bash
    sudo tpm2_verifysignature -c key.ctx -s sig.rssa -m secret.data
    ```

**Expected result**

The output of the last command shouldn't display any warnings and errors.

## TPM014.001 Encryption and Decryption of the file (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM supports the encryption and decryption of
the file.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal and run the following command to clear TPM:

    ```bash
    sudo tpm2_clear
    ```

1. Run the following set of commands to generate the required keys and files:

    ```bash
    sudo tpm2_createprimary -c primary_key.ctx
    sudo tpm2_create -u key.pub -r key.priv -C primary_key.ctx
    sudo tpm2_load -C primary_key.ctx -u key.pub -r key.priv -c key.ctx
    echo "my secret" > secret.data
    ```

1. Run the following command to encrypt the file:

    ```bash
    sudo tpm2_encryptdecrypt -c key.ctx -o secret.enc secret.data
    ```

1. Run the following command to decrypt the file:

    ```bash
    sudo tpm2_encryptdecrypt -d -c key.ctx -o secret.dec secret.enc
    ```

1. Run the following command to check the file content:

    ```bash
    cat secret.dec
    ```

**Expected result**

The output of the last command should display the content of the `secret.data`
file, in this case, it should be `my secret`.

## TPM015.001 Hashing the file (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM supports file hashing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal and run the following command to clear TPM:

    ```bash
    sudo tpm2_clear
    ```

1. Run the following set of commands to hash the file:

    ```bash
    echo "my secret" > secret.data
    sudo tpm2_hash -o hash.out -t ticket.out secret.data
    ```

**Expected result**

1. The output of the last command shouldn't display any warnings and errors.
1. Files `hash.out` and `ticket.out` should be correctly created and shouldn't
   be empty.

## TPM016.001 Performing HMAC operation on the file (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM supports HMAC operation. HMAC (Hash-based
message authentication code) is a cryptographic authentication technique that
uses a hash function and a secret key.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal and run the following command to clear TPM:

    ```bash
    sudo tpm2_clear
    ```

1. Run the following set of commands to generate the required keys and files:

    ```bash
    sudo tpm2_createprimary -c primary_key.ctx
    sudo tpm2_create -G hmac -c hmac.key -C primary_key.ctx
    echo "my secret" > secret.data
    ```

1. Run the following command to perform the HMAC operation:

    ```bash
    sudo tpm2_hmac -c hmac.key -o hmac.out secret.data
    ```

**Expected result**

1. The output of the last command shouldn't display any warnings and errors.
1. The `hmac.out` file should be correctly created and shouldn't be empty.
