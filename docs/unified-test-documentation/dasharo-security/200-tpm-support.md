# Dasharo Security: TPM Support

## Test cases

### TPM001.001 TPM Support (Ubuntu 20.04)

**Test description**

This test aims to verify that the TPM is initialized correctly and the PCRs can
be accessed from the operating system.

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
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. If your device is equipped with TPM2.0 - execute the following command
    in terminal:

```bash
tpm2_pcrread
```

1. If your device is equipped with TPM1.2 - execute the following command
    in terminal:

```bash
cat /sys/class/tpm/tpm0/pcrs
```

**Expected result**

1. The command should return a list of PCRs and their contents.

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

### TPM001.002 TPM Support (Windows 11)

**Test description**

This test aims to verify that the TPM is initialized correctly and the PCRs can
be accessed from the operating system.

**Test configuration data**

1. `FIRMWARE` = coreboot
1. `OPERATING_SYSTEM` = Windows 11

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into system by using the proper login and password.
1. Open a PowerShell and execute following command:

```PowerShell
get-tpm
```

**Expected result**

1. The command should return informations about TPM state: if the TPM is
    present, ready and enabled:

```text
TpmPresent     : True
TpmReady       : True
TpmEnabled     : True
```
