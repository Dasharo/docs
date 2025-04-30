# Dasharo Security: TPM Support

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../generic-test-setup.md#os-boot-from-disk).

## TPM001.001 TPM Support (TPM events)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM001.201 TPM Support (Ubuntu)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM001.301 TPM Support (Windows)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM001.004 TPM Support (BIOS)

**Test description**

This test aims to verify that the TPM is initialized correctly.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Disable Secure Boot.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration

**Expected result**

`Current TPM Device` should contain `TPM 2.0` or `TPM 1.2`.

## TPM002.201 Verify TPM version (Ubuntu)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM002.301 Verify TPM version (Windows)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM003.001 Check TPM Physical Presence Interface (firmware)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM003.201 Check TPM Physical Presence Interface (Ubuntu)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM003.301 Check TPM Physical Presence Interface (Windows)

The test suite is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop

## TPM004.001 Check TPM Clear procedure

**Test description**

This test aims to verify whether the TPM Clear procedure works properly, starts
with running TPM Clear procedure to ensure correct state of ownership.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `tpm2-tools` package: `sudo apt install tpm2-tools`.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration.
1. Scroll down to TPM2 Operation and press Enter.
1. Choose `TPM2 ClearControl(NO) + Clear`.
1. Save and Reboot.
1. When prompted, press F12 to clear the TPM.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open the terminal and run the following commands to take ownership over TPM2:

    ```bash
    tpm2_changeauth --quiet -c owner pass
    tpm2_changeauth --quiet -c lockout pass
    tpm2_createprimary -Q --hierarchy=o --key-context=/tmp/test --key-auth=pass2 -P pass
    tpm2_evictcontrol -Q -C o -P pass -c /tmp/test 0x81000001
    rm /tmp/test
    ```

1. Execute the following commands to check that the ownership is taken:

    ```bash
    ! tpm2_changeauth --quiet -c owner 2>/dev/null
    echo $?
    ```

1. Reboot the DUT and enter BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration.
1. Scroll down to TPM2 Operation and press Enter.
1. Choose `TPM2 ClearControl(NO) + Clear`.
1. Save and Reboot.
1. When prompted, press F12 to clear the TPM.
1. Boot into the system and log in.
1. Execute the commands from step 11.

**Expected result**

1. The output in step 11 should be equal 1.
1. The output in step 21 should be 0.

## TPM005.001 Check TPM Hash Algorithm Support SHA1 (Firmware)

**Test description**

This test aims to verify that the TPM supports needed hash algorithm (SHA1).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration
1. Scroll down to `TPM2 Hardware Supported Hash Algorithm`

**Expected result**

The entry should contain `SHA1`.

## TPM006.001 Check TPM Hash Algorithm Support SHA256 (Firmware)

**Test description**

This test aims to verify that the TPM supports needed hash algorithm (SHA256).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration
1. Scroll down to `TPM2 Hardware Supported Hash Algorithm`

**Expected result**

The entry should contain `SHA256`.

## TPM007.001 Check TPM Hash Algorithm Support SHA384 (Firmware)

**Test description**

This test aims to verify that the TPM supports needed hash algorithm (SHA384).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration
1. Scroll down to `TPM2 Hardware Supported Hash Algorithm`

**Expected result**

The entry should contain `SHA384`.

## TPM008.001 Check TPM Hash Algorithm Support SHA512 (Firmware)

**Test description**

This test aims to verify that the TPM supports needed hash algorithm (SHA512).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter Device Manager.
1. Enter TCG2 Configuration
1. Scroll down to `TPM2 Hardware Supported Hash Algorithm`

**Expected result**

The entry should contain `SHA512`.

## TPM009.201 Encrypt and Decrypt non-rootfs partition (Ubuntu)

**Test description**

Test encrypting and decrypting non-rootfs partition using TPM.

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
1. Create ext4 formatted LUKS partition with `hello-world` named file on it
    using following commands:

    ```bash
    fallocate -l 20MB test-partition
    dd if=/dev/urandom bs=1 count=32 status=none > key
    cryptsetup luksFormat -q --key-file=key test-partition
    cryptsetup luksOpen --key-file=key test-partition test-partition
    mkfs.ext4 /dev/mapper/test-partition
    mount /dev/mapper/test-partition /mnt
    touch /mnt/hello-world
    umount /dev/mapper/test-partition
    cryptsetup luksClose test-partition
    ```

1. Create the sealing object by executing the following commands:

    ```bash
    tpm2_createprimary -Q -C o -c prim.ctx
    cat key | tpm2_create -Q -g sha256 -u seal.pub -r seal.priv -i- -C prim.ctx
    tpm2_load -Q -C prim.ctx -u seal.pub -r seal.priv -n seal.name -c seal.ctx
    tpm2_evictcontrol -C o -c seal.ctx 0x81010001
    tpm2_unseal -Q -c 0x81010001 > key
    ```

1. Check a file stored on the partition by executing the following commands:

    ```bash
    cryptsetup luksOpen ./test-partition --key-file=key test-partition
    mount /dev/mapper/test-partition /mnt
    ls /mnt | grep hello-world
    ```

1. Clean up by executing the following commands:

    ```bash
    umount /mnt
    cryptsetup luksClose test-partition
    rm -f key seal.* prim.* test-partition
    tpm2_evictcontrol -c 0x81010001
    ```

**Expected result**

The output in step 5 should contain `hello-world`.

## TPM010.201 Encrypt and Decrypt rootfs partition (Ubuntu)

**Test description**

Test encrypting and decrypting rootfs partition using TPM.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. This test assumes that there is another Ubuntu with encrypted
    rootfs connected to the system, so it can be booted and two partitions
    with specific labels: EFI partition with label `ubuntu-enc` and rootfs
    with label `encrypted-rootfs`.
1. Install needed packages: `sudo apt install tpm2-tools clevis clevis-luks
    clevis-tpm2 clevis-initramfs`

**Test steps**

1. Power on the DUT.
1. Boot into the BIOS.
1. Enter the Boot Maintenance Manager.
1. Enter Boot Options.
1. Enter Add Boot Option.
1. Enter the `ubuntu-enc` volume.
1. Go to `<EFI>/<ubuntu>` and select `shimx64.efi`.
1. Go to `Input the description` and enter `ubuntu-enc-rootfs`.
1. Go to `Commit Changes and Exit` and press Enter.
1. Save the changes and reset.
1. Enter the boot menu and choose the newly added option.
1. Unlock the rootfs with your password.
1. Log into the system by using the proper login and password.
1. Bind clevis by executing the following command:

    ```bash
    echo ${UBUNTU_PASSWORD} | clevis luks bind -d /dev/disk/by-label/encrypted-rootfs tpm2 '{"pcr_ids":"0,1,2,3,7"}' -s 1
    ```

    where `${UBUNTU_PASSWORD}` is your password.

1. Reboot the system.
1. Wait for the partition to be unlocked.
1. Log into the system.
1. Clean up by executing the following command:

    ```bash
    clevis luks unbind -d /dev/vda3 -f -s 1
    ```

**Expected result**

1. In step 12 you should be prompted to unlock the rootfs.
1. In step 16 the partition should the unlocked automatically.
