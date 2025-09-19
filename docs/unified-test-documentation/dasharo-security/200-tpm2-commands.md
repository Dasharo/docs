# Dasharo Security: TPM2 commands

## Test cases common documentation

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
   [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
   [Generic test setup: OS preparation](../generic-test-setup.md#os-preparation).
1. Proceed with the
   [Generic test setup: OS post installation steps](../generic-test-setup.md#post-installation).
1. Install the `tpm2-tools` package:

   ```bash
   sudo apt install tpm2-tools
   ```

1. Check if SHA1 and SHA256 banks are enabled: `tpm2_getcap pcrs`
    Output should contain:

    ```bash
    sha1: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
    sha256: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
    ```

    If not, run `tpm2_pcrallocate` and reboot the system.

## TPMCMD001.001 Check if both SHA1 and SHA256 PCRs are enabled (Ubuntu)

**Test description**

This test aims to verify that `PCRALLOCATE` function works properly. It allows
the user to specify a PCR allocation for the TPM.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command in the shell:

    ```bash
    tpm2_getcap pcrs
    ```

**Expected result**

The output should contain a list of SHA1 and SHA256 PCR registers, example:

```bash
selected-pcrs:
  - sha1: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
  - sha256: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
  - sha384: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
  - sha512: [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23 ]
```

## TPMCMD002.001 PCRREAD Function Verification (Ubuntu)

**Test description**

This test aims to verify that PCRREAD function works properly. The function
reads PCR banks and returns them to the terminal.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Run the following command in the shell:

    ```bash
    tpm2_pcrread
    ```

**Expected result**

The output should contain values of various PCR registers, example:

```bash
  sha1:
    0 : 0x5E29B8750345DF1698B7024690C421BB72196992
    1 : 0xEB9A154B08553DD29370A22A2DB24E13C90E2880
    2 : 0x15FDC991BF9C14D090E7EBAF843B08B1F4C60F4A
    3 : 0xB2A83B0EBF2F8374299A5B2BDFC31EA955AD7236
    4 : 0x19EC12B10FCA38B3FD69C394D1DDDAE64DC91B10
    5 : 0x53F9145E792EBB289142E1DB6DB850353C120E1E
    6 : 0xB2A83B0EBF2F8374299A5B2BDFC31EA955AD7236
    7 : 0x704687C3C9FF69601B0AEAF8DA88DCC903B1FEF5
    8 : 0x0BFB7AD3F77F5ABDAE34B842CCA06EAD23433AED
    9 : 0x2AE892DEC99C2DD4E1FC626EBAB0A9E352AFE97C
    10: 0xD236A7BDC845310C2878EDF6F9B9D2567764DB07
    11: 0x0000000000000000000000000000000000000000
    12: 0x0000000000000000000000000000000000000000
    13: 0x0000000000000000000000000000000000000000
    14: 0xA482A15E112717D6A915B989A0EA6140A507E3E6
    15: 0x0000000000000000000000000000000000000000
    16: 0x0000000000000000000000000000000000000000
    17: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    18: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    19: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    20: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    21: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    22: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
    23: 0x0000000000000000000000000000000000000000
(...)
```

## TPMCMD003.001 PCREXTEND And PCRRESET Functions (Ubuntu)

**Test description**

This test aims to verify that PCREXTEND and PCRRESET functions are working
properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Reset the twenty-third PCR bank with the following command:

    ```bash
    tpm2_pcrreset 23
    ```

1. Check whether bank the twenty-third has been reset using the following
    command:

    ```bash
    tpm2_pcrread | grep 23:
    ```

1. Enroll some `sha1` and `sha256` checksums into the twenty-third PCR bank with
    the following command:

    ```bash
    tpm2_pcrextend 23:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15,sha256=b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c
    ```

1. Check whether the bank has been set to right `sha1` and `sha256` values using
    the following command:

    ```bash
    tpm2_pcrread | grep 23:
    ```

1. Reset the twenty-third PCR bank with the following command:

    ```bash
    tpm2_pcrreset 23
    ```

1. Check whether the bank has been reset using the following command:

    ```bash
    tpm2_pcrread | grep 23:
    ```

**Expected result**

The twenty-third PCR bank should change its `sha1` and `sha256` values
accordingly.

<!-- markdownlint-disable MD013 -->

## TPMCMD003.002 PCREXTEND And PCRRESET Functions - locality protections (Ubuntu)

<!-- markdownlint-enable MD013 -->

**Test description**

This test aims to verify that PCREXTEND and PCRRESET functions are working
properly when trying to modify protected PCRs.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Reset the eighteenth PCR bank with the following command:

    ```bash
    tpm2_pcrreset 18
    ```

1. Enroll some `sha1` and `sha256` checksums into the eighteenth PCR bank with
    the following command:

    ```bash
    tpm2_pcrextend 18:sha1=f1d2d2f924e986ac86fdf7b36c94bcdf32beec15,sha256=b5bb9d8014a0f9b1d61e21e796d78dccdf1352f23cd32812f4850b878ae4944c
    ```

1. Read the eighteenth bank to check whether the checksums have been enrolled
    using the following command:

    ```bash
    tpm2_pcrread | grep 18:
    ```

**Expected result**

Warning should appear after the first step and second step, the eighteenth bank
should contain `0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF` after the third
step.

## TPMCMD004.001 PCREVENT Function (Ubuntu)

**Test description**

This test aims to verify that the PCREVENT function is working properly.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Reset the twenty-third PCR bank with the following command:

    ```bash
    tpm2_pcrreset 23
    ```

1. Make sure it has been reset using the following command:

    ```bash
    tpm2_pcrread | grep 23:
    ```

1. Create some file with some data to be hashed using the following command:

    ```bash
    echo "foo" > data
    ```

1. Execute command `tpm2_pcrevent` using the twenty-third PCR bank and file with
    data to be hashed:

    ```bash
    tpm2_pcrevent 23 data
    ```

1. Calculate hashes for the data manually using commands `sha1sum` and
    `sha256sum`:

    ```bash
    sha1sum data
    sha256sum data
    ```

1. Compare manually calculated hashes with those from the twenty-third PCR bank:

    ```bash
    tpm2_pcrread | grep 23:
    ```

**Expected result**

Hashes calculated manually should match those calculated by `tpm2_event`.

## TPMCMD005.001 CREATEPRIMARY Function Verification (Ubuntu)

**Test description**

This test aims to verify that CREATEPRIMARY function works as expected. This
command is used to create a primary object under one of the hierarchies: Owner,
Platform, Endorsement, NULL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary.ctx
    ```

**Expected result**

This test aims to verify that NVDEFINE and NVUNDEFINE functions are working as
expected. Those functions are used to define and undefine a TPM Non-Volatile
index. Example output of given command is presented below:

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
rsa: a463fa1da7b5515481ad7171cad9402d1a4a0864cb918035733dc9095daa9798279cbf82facadf7661ed9aca42a1af6b0150080a4e862af1c671b62402ac0b97025a92c209bb80cd1192788c0dd572e91a3e86ecdef9ffb6382b57d7d5c569c0242926cd373c27c385da8c204dba4a0f83c19ce4c
289c9af6d3d319f049b60e3ae1f7e6b66d5c4371cc409b1a49f837dbad80f6184b7ab37c7c8118d12de502bbb3c4a38fdfad5a12a03d496079d3b97d25d0bb05bc0b00a6b4c34df02d02ba31861e68aa188e0394df57bb84a0a1fb46b41d53ec008f40e272d50b16ec5f7cbd8f8a92a72bcff7a2f17d6e122c6539b62f51c8b4881f412c4de814362725895
```

## TPMCMD006.001 NVDEFINE and NVUNDEFINE Functions Verification (Ubuntu)

**Test description**

This test aims to verify that CREATEPRIMARY function works as expected. This
command is used to create a primary object under one of the hierarchies: Owner,
Platform, Endorsement, NULL.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Define TPM a Non-Volatile index using the following command:

    ```bash
    tpm2_nvdefine -C o -s 32 -a "ownerread|policywrite|ownerwrite" 1
    ```

1. Write the data into the Non-Volatile index using the following commands:

    ```bash
    echo "nvtest" > nv.dat
    tpm2_nvwrite -C o -i nv.dat 1
    ```

1. Read the data from the Non-Volatile index using the following command:

    ```bash
    tpm2_nvread -C o -s 32 1 | tr '\\377' '\\000'
    ```

1. Undefine the defined TPM Non-Volatile index using the following command:

    ```bash
    tpm2_nvundefine -C o 1
    ```

1. Check whether, after the imdex has been undefined, it can be read using the
    following command:

    ```bash
    tpm2_nvread -C o -s 32 1 2>&1
    ```

**Expected result**

The data should be successfully written and read using TPM Non-Volatile index
but it also should not be read successfully after the TPM Non-Volatile index has
been undefined.

## TPMCMD007.001 CREATE Function (Ubuntu)

**Test description**

This test aims to verify that the CREATE function works as expected. It will
create an object using all the default values and store the TPM sealed private
and public portions to the paths specified via `-u` and `-r` respectively.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary.ctx
    ```

1. Seal some public and secret portions in TPM using the following command:

    ```bash
    tpm2_create -C primary.ctx -u obj.pub -r obj.priv
    ```

**Expected result**

The public and secret portions should be sealed without any issues.

## TPMCMD007.002 CREATELOADED Function (Ubuntu)

**Test description**

This test aims to verify that the CREATELOADED function works as expected. It
will create an object using all the default values and store key context to the
path specified via `-c`.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary.ctx
    ```

1. Store some key in TPM using the following command:

    ```bash
    tpm2_create -C primary.ctx -c obj.key
    ```

**Expected result**

The key should be stored in TPM without any issues.

## TPMCMD008.001 Signing the file (Ubuntu)

**Test description**

Check whether the TPM supports file signing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary_key.ctx
    ```

1. Seal some public and secret portions in TPM using the following command:

    ```bash
    tpm2_create -u key.pub -r key.priv -C primary_key.ctx
    ```

1. Store some key in TPM using the following command:

    ```bash
    tpm2_load -C primary_key.ctx -u key.pub -r key.priv -c key.ctx
    ```

1. Sign a file using TPM and the following commands:

    ```bash
    echo "my secret" > secret.data
    tpm2_sign -c key.ctx -o sig.rssa secret.data
    ```

1. Verify the signature using the following command:

    ```bash
    tpm2_verifysignature -c key.ctx -s sig.rssa -m secret.data
    ```

**Expected result**

The file should be signed successfully.

## TPMCMD009.001 Encryption and Decryption of the file (Ubuntu)

**Test description**

Check whether the TPM supports the encryption and decryption of the file.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Check for the presence of the TPM command for encryption/decryption.

    ```bash
    tpm2_getcap commands | grep TPM2_EncryptDecrypt
    ```

1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary_key.ctx
    ```

1. Create a key for the file encryption/decryption and store it in TPM using the
    following commands:

    ```bash
    tpm2_create -u key.pub -r key.priv -C primary_key.ctx -Gaes128
    tpm2_load -C primary_key.ctx -u key.pub -r key.priv -c key.ctx
    ```

1. Encrypt and decrypt the file using the following commands:

    ```bash
    echo "my secret" > secret.data
    dd if=/dev/zero bs=1 count=16 of=iv.bin
    tpm2_encryptdecrypt -c key.ctx -o secret.enc secret.data -t iv.bin
    tpm2_encryptdecrypt -d -c key.ctx -o secret.dec secret.enc -t iv.bin
    ```

**Expected result**

The file should be encrypted and then decrypted successfully. Content of
`secret.data` and `secret.dec` should be the same.

## TPMCMD010.001 Hashing the file (Ubuntu)

**Test description**

Check whether the TPM supports file hashing.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Hash a file using the following commands:

    ```bash
    echo "my secret" > secret.data
    tpm2_hash -o hash.out -t ticket.out secret.data
    ```

1. Check whether the hashes have been created.

**Expected result**

The hashes should be created successfully.

## TPMCMD011.001 Performing HMAC operation on the file (Ubuntu)

**Test description**

Check whether the TPM supports HMAC operation.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a primary object using the following command:

    ```bash
    tpm2_createprimary -c primary_key.ctx
    ```

1. Seal some public and secret portions in TPM using the HMAC key algorithm with
    the following command:

    ```bash
    tpm2_create -u key.pub -r key.priv -C primary_key.ctx -G hmac
    ```

1. Create a key for the file encryption/decryption and store it in TPM using the
    following command:

    ```bash
    tpm2_load -C primary_key.ctx -u key.pub -r key.priv -c hmac.key
    ```

1. Perform an HMAC operation on some data and record it results in some file
    using the following commands:

    ```bash
    echo "my secret" > secret.data
    tpm2_hmac -c hmac.key -o hmac.out secret.data
    ```

**Expected result**

Verify that HMAC operation ended successfully.

## TPMCMD012.001 Sealing and Unsealing the file without Policy (Ubuntu)

**Test description**

This test verifies TPM sealing functionality.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a file to seal by executing the following commands:

    ```bash
    tpm2_createprimary -c primary.ctx
    echo "my sealed data" > seal.dat
    ```

1. Seal the file:

    ```bash
    tpm2_create -C primary.ctx -i seal.dat -u key.pub -r key.priv
    tpm2_evictcontrol --hierarchy owner --object-context seal.ctx -o seal.handle
    ```

1. Unseal the file and check its contents:

    ```bash
    tpm2_unseal -c seal.handle > unsealed.dat
    cat unsealed.dat
    ```

**Expected result**

The output in step 6 should be the equal to the content of `seal.dat`.

## TPMCMD013.001 Sealing and Unsealing with Policy - Password Only (Ubuntu)

**Test description**

Check whether the TPM supports sealing and unsealing using password policy.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create the file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "password policy sealed data" > seal.dat
    ```

1. Seal the file using password policy:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat -p policypswd
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

1. Unseal the file and check its content:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_unseal -p session:session.dat+policypswd -c seal.ctx
    ```

**Expected result**

The output in step 6 should be the equal to the content of `seal.dat`.

## TPMCMD013.002 Sealing and Unsealing with Policy - PCR Only (Ubuntu)

**Test description**

Check whether the TPM supports sealing and unsealing using PCR policy.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "PCR policy sealed data" > seal.dat
    ```

1. Seal the file:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

1. Unseal the file:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_unseal -p session:session.dat -c seal.ctx
    ```

**Expected result**

The output in step 6 should be the equal to the content of `seal.dat`.

## TPMCMD013.003 Sealing and unsealing with Policy - Password and PCR (Ubuntu)

**Test description**

Check whether the TPM supports sealing and unsealing using PCR and password
policy at the same time.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Create a file to seal:

    ```bash
    tpm2_createprimary -C e -g sha256 -G ecc -c primary.ctx
    echo "policy sealed data" > seal.dat
    ```

1. Seal the file:

    ```bash
    tpm2_startauthsession -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_create -Q -u key.pub -r key.priv -C primary.ctx -L policy.dat -i seal.dat -p policypswd
    tpm2_load -C primary.ctx -u key.pub -r key.priv -n seal.name -c seal.ctx
    ```

1. Unseal the file:

    ```bash
    tpm2_startauthsession --policy-session -S session.dat
    tpm2_policypassword -S session.dat -L policy.dat
    tpm2_policypcr -S session.dat -l "sha1:0,1,2,3,7" -L policy.dat
    tpm2_unseal -p session:session.dat+policypswd -c seal.ctx
    ```

**Expected result**

The output in step 6 should be the equal to the content of `seal.dat`.
