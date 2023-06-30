# Dasharo Stability: NVMe detection

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Proceed with the
   [Generic test setup: OS installer](../../generic-test-setup/#os-installer).
1. Proceed with the
   [Generic test setup: OS installation](../../generic-test-setup/#os-installation).
1. Proceed with the
   [Generic test setup: OS boot from disk](../../generic-test-setup/#os-boot-from-disk).
1. Install the `tpm2-tools` package: `sudo apt-get install tpm2-tools`.

## TPD001.001 TPM detection after cold boot

**Test description**

This test aims to verify that the TPM module is correctly detected after
performing a cold boot. The test should be performed in multiple iterations.

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
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

1. Disconnect the power source, and remove the battery if present.
1. Connect power and battery again.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

**Expected result**

1. The output of each `tpm2_pcrread` command should contain information about
    PCRS:

    Example output:

    ```bash
        0 : 0x2F69DFD9A789F47317B110DA698A5DF3A02F12878FF467E33C474C7E487DAE15
        1 : 0xCF9AEC0D919A26133F5802FE82FFE92DBAF4C2C9D5DB764531A1B9E027A4445F
        2 : 0x1573E2C07C01B429AE2CAA0027E2E41F22342CA9CBA8F70778449972F17FC1F9
        3 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        4 : 0xB23E42324EFE04AF98A835543314DCC5D3A30ADF853A7FD5A168C7FB808DA701
        5 : 0x276663B40D595416A4B58349EE91C2FBD8B1D9D8B8FD5F82DD3BC29931B034E0
        6 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        7 : 0x2FFE4BE876B04E0E8A539ED2E62F83627CAE8B57BA9BA22DAC8497B1B21FDEA4
        8 : 0x8F54ADFD4A146A400296665FD1B3BB19B85104831C17E61837004EA297461AD5
        9 : 0x6BA8A0F2BBD7D46CEF36371AA47F1E772F73FF318BC151FEDDD0725C28BA8DF8
        10: 0xB6B7F8415859D8B32325DCACC304166F5C33E0ED3F39F378348BCD29627F3A93
        11: 0x0000000000000000000000000000000000000000000000000000000000000000
        12: 0x0000000000000000000000000000000000000000000000000000000000000000
        13: 0x0000000000000000000000000000000000000000000000000000000000000000
        14: 0xD7C4CC7FF7933022F013E03BDEE875B91720B5B86CF1753CAD830F95E791926F
        15: 0x0000000000000000000000000000000000000000000000000000000000000000
        16: 0x0000000000000000000000000000000000000000000000000000000000000000
        17: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        18: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        19: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        20: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        21: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        22: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        23: 0x0000000000000000000000000000000000000000000000000000000000000000
    ```

1. PCRs should be subject to the following regularities:

    - PCR0 - PCR7 values should not be equal zero; they contains firmware
        measurements,
    - PCR8, PCR9 and PCR14 values should not be equal zero; they contains GRUB
        measurements,
    - PCR10 value should not be equal zero.

1. Between subsequent boots above mentioned PCRs values should remain unchanged.

## TPD002.001 TPM detection after warm boot

**Test description**

This test aims to verify that the TPM module is correctly detected after
performing a warm boot. The test should be performed in multiple iterations.

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
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

1. Power off the DUT using the power button.
1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

**Expected result**

1. The output of each `tpm2_pcrread` command should contain information about
    PCRS:

    Example output:

    ```bash
        0 : 0x2F69DFD9A789F47317B110DA698A5DF3A02F12878FF467E33C474C7E487DAE15
        1 : 0xCF9AEC0D919A26133F5802FE82FFE92DBAF4C2C9D5DB764531A1B9E027A4445F
        2 : 0x1573E2C07C01B429AE2CAA0027E2E41F22342CA9CBA8F70778449972F17FC1F9
        3 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        4 : 0xB23E42324EFE04AF98A835543314DCC5D3A30ADF853A7FD5A168C7FB808DA701
        5 : 0x276663B40D595416A4B58349EE91C2FBD8B1D9D8B8FD5F82DD3BC29931B034E0
        6 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        7 : 0x2FFE4BE876B04E0E8A539ED2E62F83627CAE8B57BA9BA22DAC8497B1B21FDEA4
        8 : 0x8F54ADFD4A146A400296665FD1B3BB19B85104831C17E61837004EA297461AD5
        9 : 0x6BA8A0F2BBD7D46CEF36371AA47F1E772F73FF318BC151FEDDD0725C28BA8DF8
        10: 0xB6B7F8415859D8B32325DCACC304166F5C33E0ED3F39F378348BCD29627F3A93
        11: 0x0000000000000000000000000000000000000000000000000000000000000000
        12: 0x0000000000000000000000000000000000000000000000000000000000000000
        13: 0x0000000000000000000000000000000000000000000000000000000000000000
        14: 0xD7C4CC7FF7933022F013E03BDEE875B91720B5B86CF1753CAD830F95E791926F
        15: 0x0000000000000000000000000000000000000000000000000000000000000000
        16: 0x0000000000000000000000000000000000000000000000000000000000000000
        17: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        18: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        19: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        20: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        21: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        22: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        23: 0x0000000000000000000000000000000000000000000000000000000000000000
    ```

1. PCRs should be subject to the following regularities:

    - PCR0 - PCR7 values should not be equal zero; they contains firmware
        measurements,
    - PCR8, PCR9 and PCR14 values should not be equal zero; they contains GRUB
        measurements,
    - PCR10 value should not be equal zero.

1. Between subsequent boots above mentioned PCRs values should remain unchanged.

## TPD003.001 TPM detection after cold reboot

**Test description**

This test aims to verify that the TPM module is correctly detected after
performing a reboot. The test should be performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../../generic-test-setup#firmware)

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

1. Execute the following command to reboot the system:

    ```bash
    reboot
    ```

1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

**Expected result**

**Expected result**

1. The output of each `tpm2_pcrread` command should contain information about
    PCRS:

    Example output:

    ```bash
        0 : 0x2F69DFD9A789F47317B110DA698A5DF3A02F12878FF467E33C474C7E487DAE15
        1 : 0xCF9AEC0D919A26133F5802FE82FFE92DBAF4C2C9D5DB764531A1B9E027A4445F
        2 : 0x1573E2C07C01B429AE2CAA0027E2E41F22342CA9CBA8F70778449972F17FC1F9
        3 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        4 : 0xB23E42324EFE04AF98A835543314DCC5D3A30ADF853A7FD5A168C7FB808DA701
        5 : 0x276663B40D595416A4B58349EE91C2FBD8B1D9D8B8FD5F82DD3BC29931B034E0
        6 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        7 : 0x2FFE4BE876B04E0E8A539ED2E62F83627CAE8B57BA9BA22DAC8497B1B21FDEA4
        8 : 0x8F54ADFD4A146A400296665FD1B3BB19B85104831C17E61837004EA297461AD5
        9 : 0x6BA8A0F2BBD7D46CEF36371AA47F1E772F73FF318BC151FEDDD0725C28BA8DF8
        10: 0xB6B7F8415859D8B32325DCACC304166F5C33E0ED3F39F378348BCD29627F3A93
        11: 0x0000000000000000000000000000000000000000000000000000000000000000
        12: 0x0000000000000000000000000000000000000000000000000000000000000000
        13: 0x0000000000000000000000000000000000000000000000000000000000000000
        14: 0xD7C4CC7FF7933022F013E03BDEE875B91720B5B86CF1753CAD830F95E791926F
        15: 0x0000000000000000000000000000000000000000000000000000000000000000
        16: 0x0000000000000000000000000000000000000000000000000000000000000000
        17: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        18: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        19: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        20: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        21: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        22: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        23: 0x0000000000000000000000000000000000000000000000000000000000000000
    ```

1. PCRs should be subject to the following regularities:

    - PCR0 - PCR7 values should not be equal zero; they contains firmware
        measurements,
    - PCR8, PCR9 and PCR14 values should not be equal zero; they contains GRUB
        measurements,
    - PCR10 value should not be equal zero.

1. Between subsequent boots above mentioned PCRs values should remain unchanged,
    except PCR10.

## TPD0004.001 TPM detection after suspension (Ubuntu 22.04)

**Test description**

This test aims to verify that the TPM module is correctly detected after
performing suspension. The test should be performed in multiple iterations.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the [Firmware test suite](https://wiki.ubuntu.com/FirmwareTestSuite)
   package.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

1. Execute the following command to suspend the system and automatically wake it
   up after 10 seconds:

    ```bash
    sudo fwts s3 --s3-sleep-delay=10
    ```

1. Log into the system by using the proper login and password.
1. Open a terminal window and run the following command:

    ```bash
    tpm2_pcrread
    ```

**Expected result**

1. The output of each `tpm2_pcrread` command should contain information about
    PCRS:

    Example output:

    ```bash
        0 : 0x2F69DFD9A789F47317B110DA698A5DF3A02F12878FF467E33C474C7E487DAE15
        1 : 0xCF9AEC0D919A26133F5802FE82FFE92DBAF4C2C9D5DB764531A1B9E027A4445F
        2 : 0x1573E2C07C01B429AE2CAA0027E2E41F22342CA9CBA8F70778449972F17FC1F9
        3 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        4 : 0xB23E42324EFE04AF98A835543314DCC5D3A30ADF853A7FD5A168C7FB808DA701
        5 : 0x276663B40D595416A4B58349EE91C2FBD8B1D9D8B8FD5F82DD3BC29931B034E0
        6 : 0x3D458CFE55CC03EA1F443F1562BEEC8DF51C75E14A9FCF9A7234A13F198E7969
        7 : 0x2FFE4BE876B04E0E8A539ED2E62F83627CAE8B57BA9BA22DAC8497B1B21FDEA4
        8 : 0x8F54ADFD4A146A400296665FD1B3BB19B85104831C17E61837004EA297461AD5
        9 : 0x6BA8A0F2BBD7D46CEF36371AA47F1E772F73FF318BC151FEDDD0725C28BA8DF8
        10: 0xB6B7F8415859D8B32325DCACC304166F5C33E0ED3F39F378348BCD29627F3A93
        11: 0x0000000000000000000000000000000000000000000000000000000000000000
        12: 0x0000000000000000000000000000000000000000000000000000000000000000
        13: 0x0000000000000000000000000000000000000000000000000000000000000000
        14: 0xD7C4CC7FF7933022F013E03BDEE875B91720B5B86CF1753CAD830F95E791926F
        15: 0x0000000000000000000000000000000000000000000000000000000000000000
        16: 0x0000000000000000000000000000000000000000000000000000000000000000
        17: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        18: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        19: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        20: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        21: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        22: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        23: 0x0000000000000000000000000000000000000000000000000000000000000000
    ```

1. PCRs should be subject to the following regularities:

    - PCR0 - PCR7 values should not be equal zero; they contains firmware
        measurements,
    - PCR8, PCR9 and PCR14 values should not be equal zero; they contains GRUB
        measurements,
    - PCR10 value should not be equal zero.

1. Between subsequent boots above mentioned PCRs values should remain unchanged.
