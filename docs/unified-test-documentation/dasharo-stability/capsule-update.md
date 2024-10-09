# Dasharo Stability: Capsule Update

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

## CUP001.001 Capsule Update With Wrong Keys (UEFI Shell)

**Test description**

This test aims to verify that the Device Under Test (DUT) rejects flashing a
capsule that is signed with an invalid certificate.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into UEFI Shell.
1. Obtain the current BIOS version by executing the following command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${original_bios_version}`.
1. Perform a capsule update using an invalid certificate file by executing:

    ```bash
    CapsuleApp.efi -U wrong_cert.cap
    ```

1. Reboot the system and select the UEFI Shell boot option.
1. After the system boots, verify the BIOS version by running the following
   command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${updated_bios_version}`.
1. Check that the BIOS version has not changed by verifying that
   `${original_bios_version}` is equal to `${updated_bios_version}`.
1. Enter the Capsule Testing folder and execute the following command to check
   the status:

    ```bash
    CapsuleApp.efi -S
    ```

1. Verify that the output contains the following:

    ```bash
    Capsule Status: Security Violation
    ```

**Expected result**

1. The BIOS version should not change after attempting the capsule update.
1. The output of the command `CapsuleApp.efi -S` should contain `Capsule
   Status: Security Violation`, indicating that the update was rejected due to
   the invalid certificate.

---

## CUP002.001 Capsule Update With Wrong GUID (UEFI Shell)

**Test description**

This test aims to verify that the Device Under Test (DUT) rejects flashing a
capsule with an invalid GUID.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into UEFI Shell.
1. Obtain the current BIOS version by executing the following command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${original_bios_version}`.
1. Perform a capsule update using an invalid GUID file by executing:

    ```bash
    CapsuleApp.efi -U invalid_guid.cap
    ```

1. Reboot the system and select the UEFI Shell boot option.
1. After the system boots, verify the BIOS version by running the following
   command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${updated_bios_version}`.
1. Check that the BIOS version has not changed by verifying that
   `${original_bios_version}` is equal to `${updated_bios_version}`.
1. Enter the Capsule Testing folder and execute the following command to check
   the status:

    ```bash
    CapsuleApp.efi -S
    ```

1. Verify that the output contains the following:

    ```bash
    Capsule Status: Not Ready
    ```

**Expected result**

1. The BIOS version should not change after attempting the capsule update.
1. The output of the command `CapsuleApp.efi -S` should contain `Capsule Status:
   Not Ready`, indicating that the update was rejected due to the invalid GUID.

---

## CUP130.001 Verifying BIOS Settings Persistence After Update - PART 1

**Test description**

This test aims to verify that BIOS settings persist after a Capsule Update.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the Setup Menu.
1. Navigate to the "Dasharo System Features" menu.
1. Enter the "Networking Options" submenu.
1. Enable the "Network Boot" option.
1. Save the settings and reboot the system.
1. Boot into UEFI Shell.
1. Perform a capsule update using the following command:

    ```bash
    CapsuleApp.efi -U max_fw_ver.cap
    ```

**Expected result**

1. The network boot option should remain enabled after the system reboots and
   the capsule update is applied.

---

## CUP150.001 Capsule Update

**Test description**

This test verifies a successful capsule update and ensures the correct user
experience (UX) during the update.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Custom logo firmware image

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into UEFI Shell.
1. Obtain the current BIOS version by executing the following command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${original_bios_version}`.
1. Perform a capsule update using the following command:

    ```bash
    CapsuleApp.efi -U valid_capsule.cap
    ```

1. Reboot the system and select the UEFI Shell boot option.
1. After the system boots, verify the BIOS version by running the following
   command:

    ```bash
    CapsuleApp.efi -V
    ```

    Save the BIOS version as `${updated_bios_version}`.
1. Ensure that the BIOS version has changed.
1. Enter the Capsule Testing folder and execute the following command to check
   the status:

    ```bash
    CapsuleApp.efi -S
    ```

1. Verify that the output contains `CapsuleMax` and does not contain
   `CapsuleLast`.

**Expected result**

1. The BIOS version should change after the update.
1. The output of `CapsuleApp.efi -S` should contain `CapsuleMax` and should not
   contain `CapsuleLast`.

---

## CUP160.001 Verifying BIOS Settings Persistence After Update - PART 2

**Test description**

This test aims to verify the persistence of BIOS settings after a capsule
update.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the Setup Menu.
1. Navigate to the "Boot Maintenance Manager" menu.
1. Check the value of the "Auto Boot Time-out" option.

**Expected result**

1. The "Auto Boot Time-out" option should retain the previously set value.

---

## CUP170.001 Verifying UUID (Ubuntu)

**Test description**

This test checks if the UUID persists after a capsule update.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Log in to Ubuntu.
1. Check the current UUID.
1. Perform the capsule update using the following command:

    ```bash
    fwupdmgr install max_fw_ver.cap
    ```

1. After the update, verify the UUID.

**Expected result**

1. The UUID should remain unchanged after the update.

---

## CUP180.001 Verifying Serial Number (Ubuntu)

**Test description**

This test checks if the serial number persists after a capsule update.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Log in to Ubuntu.
1. Check the current serial number.
1. Perform the capsule update using the following command:

    ```bash
    fwupdmgr install max_fw_ver.cap
    ```

1. After the update, verify the serial number.

**Expected result**

1. The serial number should remain unchanged after the update.

---

## CUP190.001 Verifying If Custom Logo Persists Across Updates (Ubuntu)

**Test description**

This test checks if the custom logo persists after a capsule update.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu
1. Custom logo firmware image

**Test setup**

1. Ensure that the DUT is running the firmware with a custom logo.
1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Log in to Ubuntu.
1. Check the current custom logo's SHA-256 hash.
1. Perform the capsule update using the following command:

    ```bash
    fwupdmgr install max_fw_ver.cap
    ```

1. After the update, verify the custom logo's SHA-256 hash.

**Expected result**

1. The custom logo should remain unchanged after the update.

---

## CUP250.001 Capsule Update Progress Bar - Default Logo

**Test description**

This test verifies that the Capsule Update screen displays the correct user
experience (UX) when using a default logo, including the progress bar.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Default logo firmware image

**Test setup**

1. Ensure that the DUT is running the firmware with the default logo.
1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Power on the DUT.
1. Boot into UEFI Shell.
1. Perform a capsule update using the following command:

    ```bash
    CapsuleApp.efi -U valid_capsule.cap
    ```

1. Observe the Capsule Update screen during the update to ensure the progress
   bar scales properly with the default logo.

**Expected result**

1. The Capsule Update screen should display the progress bar correctly, and the
   default logo should appear without scaling issues.
