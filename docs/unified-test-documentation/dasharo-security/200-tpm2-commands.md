# Dasharo Security: TPM2 commands

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
2. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
3. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
4. Proceed with th  e
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).
5. Install the `tpm2-tools` package:

   ```bash
   sudo apt install tpm2-tools
   ```

6. Check if SHA1 and SHA256 banks are enabled: `tpm2_getcap pcrs`
    Output should contain:

    ```bash
    sha1: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
    sha256: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
    ```

    If not, run `tpm2_pcrallocate` and reboot the system.

<!--
## TPMCMD001.001 Check if both SHA1 and SHA256 PCRs are enabled (Ubuntu 22.04)
## TPMCMD002.001 PCRREAD Function Verification (Ubuntu 22.04)
## TPMCMD003.001 PCREXTEND And PCRRESET Functions (Ubuntu 22.04)
## TPMCMD003.002 PCREXTEND And PCRRESET Functions - locality protections (Ubuntu
22.04)
## TPMCMD004.001 PCREVENT Function (Ubuntu 22.04)
## TPMCMD005.001 CREATEPRIMARY Function Verification (Ubuntu 22.04)
## TPMCMD006.001 NVDEFINE and NVUNDEFINE Functions Verification (Ubuntu 22.04)
## TPMCMD007.001 CREATE Function (Ubuntu 22.04)
## TPMCMD007.002 CREATELOADED Function (Ubuntu 22.04)
## TPMCMD008.001 Signing the file (Ubuntu 22.04)
## TPMCMD009.001 Encryption and Decryption of the file (Ubuntu 22.04)
## TPMCMD010.001 Hashing the file (Ubuntu 22.04)
##TPMCMD011.001 Performing HMAC operation on the file (Ubuntu 22.04)
-->

## TPMCMD012.001 Sealing and Unsealing the file without Policy (Ubuntu 22.04)

**Test description**

This test verifies TPM sealing functionality.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a file to seal by executing the following commands:

    ```bash
    tpm2_createprimary -c primary.ctx
    echo "my sealed data" > seal.dat
    ```

2. Seal the file:

    ```bash
    tpm2_create -C primary.ctx -i seal.dat -u key.pub -r key.priv
    tpm2_evictcontrol --hierarchy owner --object-context seal.ctx -o seal.handle
    ```

3. Unseal the file and check its contents:

    ```bash
    tpm2_unseal -c seal.handle > unsealed.dat
    cat unsealed.dat
    ```

**Expected result**

The output in step 3 should be the equal to the content of `seal.dat`.

## TPMCMD013.001 Sealing and Unsealing with Policy - Password Only (Ubuntu 22.04)

**Test description**

Check whether the TPM supports sealing and unsealing using password policy.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create the file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "password policy sealed data" > seal.dat
    ```

2. Seal the file using password policy:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat -p policypswd
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

3. Unseal the file and check its content:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_unseal -p session:session.dat+policypswd -c seal.ctx
    ```

**Expected result**

The output in step 3 should be the equal to the content of `seal.dat`.

## TPMCMD013.002 Sealing and Unsealing with Policy - PCR Only (Ubuntu 22.04)

**Test description**

Check whether the TPM supports sealing and unsealing using PCR policy.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "PCR policy sealed data" > seal.dat
    ```

2. Seal the file:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

3. Unseal the file:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_unseal -p session:session.dat -c seal.ctx
    ```

**Expected result**

The output in step 3 should be the equal to the content of `seal.dat`.

## TPMCMD013.003 Sealing and unsealing with Policy - Password and PCR (Ubuntu 22.04)

**Test description**

Check whether the TPM supports sealing and unsealing using PCR and password
policy at the same time.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "policy sealed data" > seal.dat
    ```

2. Seal the file:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat -p policypswd
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

3. Unseal the file:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_unseal -p session:session.dat+policypswd -c seal.ctx
    ```

**Expected result**

The output in step 3 should be the equal to the content of `seal.dat`.
