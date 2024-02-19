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

## TPMCMD001.001 Check if both SHA1 and SHA256 PCRs are enabled (Ubuntu 22.04)

**Test description**

This test aims to verify that `PCRALLOCATE` function works properly. It allows
the user to specify a PCR allocation for the TPM.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Run command `tpm2_getcap pcrs`.

**Expected result**

The output should contain a list of SHA1 and SHA256 PCR registers.

## TPMCMD002.001 PCRREAD Function Verification (Ubuntu 22.04)

**Test description**

This test aims to verify that PCRREAD function works properly. The function
reads PCR banks and returns them to the terminal.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Run command `tpm2_pcrread`

**Expected result**

The output should contain values of various PCR registers.

## TPMCMD003.001 PCREXTEND And PCRRESET Functions (Ubuntu 22.04)

**Test description**

This test aims to verify that PCREXTEND and PCRRESET functions are working
properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Reset the twenty-third PCR bank;
1. Check whether bank the twenty-third has been reset;
1. Enroll some `sha1` and `sha256` checksums into the twenty-third PCR bank;
1. Check whether the bank has been set to right `sha1` and `sha256` values;
1. Reset the twenty-third PCR bank;
1. Check whether the bank has been reset;

**Expected result**

The twenty-third PCR bank should change its `sha1` and `sha256` values
accordingly.

<!-- markdownlint-disable MD013 -->

## TPMCMD003.002 PCREXTEND And PCRRESET Functions - locality protections (Ubuntu22.04)

<!-- markdownlint-enable MD013 -->

**Test description**

This test aims to verify that PCREXTEND and PCRRESET functions are working
properly when trying to modify protected PCRs.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Reset the eighteenth PCR bank;
1. Enroll some `sha1` and `sha256` checksums into the eighteenth PCR bank;
1. Read the eighteenth bank to check whether the checksums have been enrolled.

**Expected result**

1. Warning should appear after the first step;
1. Warning should appear after the second step;
1. The eighteenth bank should contain
`0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF` after the third step.

## TPMCMD004.001 PCREVENT Function (Ubuntu 22.04)

**Test description**

This test aims to verify that the PCREVENT function is working properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Reset the twenty-third PCR bank;
1. Make sure it has been reset;
1. Create some file with some data to be hashed;
1. Execute command `tpm2_pcrevent` using the twenty-third PCR bank and file with
    data to be hashed;
1. Calculate hashes for the data manually using commands `sha1sum` and
    `sha256sum`;
1. Compare manually calculated hashes with those from the twenty-third PCR bank;

**Expected result**

Hashes calculated manually should match those calculated by `tpm2_event`.

## TPMCMD005.001 CREATEPRIMARY Function Verification (Ubuntu 22.04)

**Test description**

This test aims to verify that CREATEPRIMARY function works as expected. This
command is used to create a primary object under one of the hierarchies: Owner,
Platform, Endorsement, NULL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a primary object using the command `tpm2_createprimary -c
    primary.ctx`.

**Expected result**

This test aims to verify that NVDEFINE and NVUNDEFINE functions are working as
expected. Those functions are used to define and undefine a TPM Non-Volatile
index.

## TPMCMD006.001 NVDEFINE and NVUNDEFINE Functions Verification (Ubuntu 22.04)

**Test description**

This test aims to verify that CREATEPRIMARY function works as expected. This
command is used to create a primary object under one of the hierarchies: Owner,
Platform, Endorsement, NULL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Define TPM a Non-Volatile index;
1. Write the data into the Non-Volatile index:
1. Read the data from the Non-Volatile index;
1. Undefine the defined TPM Non-Volatile index;
1. Check whether, after the imdex has been undefined, it can be read.

**Expected result**

1. The data should be successfully writenn and read using TPM Non-Volatile
    index;
1. The data written should not be read successfully after the TPM Non-Volatile
    index has been undefined.

## TPMCMD007.001 CREATE Function (Ubuntu 22.04)

**Test description**

This test aims to verify that the CREATE function works as expected. It will
create an object using all the default values and store the TPM sealed private
and public portions to the paths specified via `-u` and `-r` respectively.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a primary object;
1. Seal some public and secret portions in TPM.

**Expected result**

 The public and secret portions should be sealed without any issues.

## TPMCMD007.002 CREATELOADED Function (Ubuntu 22.04)

**Test description**

This test aims to verify that the CREATELOADED function works as expected. It
will create an object using all the default values and store key context to the
path specified via `-c`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a primary object;
1. Store some key in TPM using the `-c` option with `tpm2_create`.

**Expected result**

The key should be stored in TPM without any issues.

## TPMCMD008.001 Signing the file (Ubuntu 22.04)

**Test description**

Check whether the TPM supports file signing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a primary object;
1. Seal some public and secret portions in TPM;
1. Store some key in TPM;
1. Sign a file using TPM

**Expected result**

The file should be signed successfully.

## TPMCMD009.001 Encryption and Decryption of the file (Ubuntu 22.04)

**Test description**

Check whether the TPM supports the encryption and decryption of the file.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Check for the presence of the TPM command for encryption/decryption;
1. Create a primary object;
1. Seal some public and secret portions in TPM;
1. Create a key for the file encryption/decryption and store it in TPM;
1. Encrypt and decrypt the file.

**Expected result**

The file should be encrypted and then decrypted successfully.

## TPMCMD010.001 Hashing the file (Ubuntu 22.04)

**Test description**

Check whether the TPM supports file hashing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Hash a file using `tpm2_hash`;
1. Check whether the hashes have been created.

**Expected result**

The hashes should be created successfully.

## TPMCMD011.001 Performing HMAC operation on the file (Ubuntu 22.04)

**Test description**

Check whether the TPM supports HMAC operation.

**Test configuration data**

1. `FIRMWARE` = Dasharo
2. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Create a primary object;
1. Seal some public and secret portions in TPM using the HMAC key algorithm;
1. Create a key for the file encryption/decryption and store it in TPM;
1. Perform an HMAC operation on some data and record it results in some file.

**Expected result**

Verify that HMAC operation ended successfully.

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
