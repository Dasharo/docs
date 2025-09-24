# Dasharo Stability: Capsule Update

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
1. Boot into Ubuntu and note down the original
    - UUID (via `dmidecode`)
    - Serial number (also via `dmidecode`)
    - BGRT bootsplash logo hash (located in `/sys/firmware/acpi/bgrt`)

## CUP001.001 Capsule Update With Wrong Keys (UEFI Shell)

**Test description**

This test aims to verify that the Device Under Test (DUT) rejects flashing a
capsule that is signed with an invalid certificate.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Obtain and save the current BIOS version as `${original_bios_version}`.
1. Perform a capsule update using an invalid certificate file
1. Reboot the system and select the UEFI Shell boot option.
1. After the system boots, verify the BIOS version and save it as
   `${updated_bios_version}`.
1. Check that the BIOS version has not changed by verifying that
   `${original_bios_version}` is equal to `${updated_bios_version}`.
1. Verify that there is a status note about a security violation.

**Expected result**

1. The BIOS version should not change after attempting the capsule update.
1. The status should contain a note indicating that the update was rejected due
   to the invalid certificate.

---

## CUP002.001 Capsule Update With Wrong GUID (UEFI Shell)

**Test description**

This test aims to verify that the Device Under Test (DUT) rejects flashing a
capsule with an invalid GUID.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Obtain and save the BIOS version as `${original_bios_version}`.
1. Perform a capsule update using an invalid GUID file.
1. Reboot the system and select the UEFI Shell boot option.
1. After the system boots, verify and save the BIOS version as
   `${updated_bios_version}`.
1. Check that the BIOS version has not changed by verifying that
   `${original_bios_version}` is equal to `${updated_bios_version}`.
1. Verify that the status contains a `Not Ready` indication.

**Expected result**

1. The BIOS version should not change after attempting the capsule update.
1. The status should contain a note indicating that the update was rejected due
   to the invalid GUID.

---

## CUP130.001 Verifying BIOS Settings Persistence After Update - PART 1

**Test description**

This test aims to verify that BIOS settings persist after a Capsule Update.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Enter the Setup Menu.
1. Navigate to Boot Maintenance Manager.
1. Change the Auto Boot Time-out value to an arbitrary custom one, such as
   32123
1. Save the settings and reboot the system.

**Expected result**

1. The custom Auto Boot Time-out value should remain set after the reboot.

---

## CUP150.001 Capsule Update

**Test description**

This test verifies a successful capsule update and ensures the correct user
experience (UX) during the update.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Custom logo firmware image

**Test setup**

1. Ensure the DUT is connected and the UEFI shell is available.
1. Proceed with the common test setup steps as described in the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Obtain and save the BIOS version as `${original_bios_version}`.
1. Perform a capsule update using a valid capsule.
1. Verify that the update screen looks as expected.
1. After the system boots, select the UEFI shell boot option.
1. Verify the BIOS version and save it as `${updated_bios_version}`.
1. Ensure that the BIOS version has changed.
1. Verify that the status contains `CapsuleMax` and does not contain
   `CapsuleLast`.

**Expected result**

1. The update screen should look exactly as presented in the
   [Capsule Update documentation](../../guides/capsule-update.md).
1. The BIOS version should change after the update.
1. The status should contain `CapsuleMax` and should not contain `CapsuleLast`.

---

## CUP160.001 Verifying BIOS Settings Persistence After Update - PART 2

**Test description**

This test aims to verify the persistence of BIOS settings after a capsule
update.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

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

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Log in to Ubuntu.
1. Check the UUID after the update.

**Expected result**

1. The UUID should remain unchanged after the update.

---

## CUP180.001 Verifying Serial Number (Ubuntu)

**Test description**

This test checks if the serial number persists after a capsule update.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu

**Test setup**

1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Log in to Ubuntu.
1. Check the serial number after the update.

**Expected result**

1. The serial number should remain unchanged after the update.

---

## CUP190.001 Verifying If Custom Logo Persists Across Updates (Ubuntu)

**Test description**

This test checks if the custom logo persists after a capsule update.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

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
1. After the update, verify the custom logo's SHA-256 hash.

**Expected result**

1. The custom logo should remain unchanged after the update.

---

## CUP250.001 Capsule Update Progress Bar - Default Logo

**Test description**

This test verifies that the Capsule Update screen displays the correct user
experience (UX) when using a default logo, including the progress bar.

Each step in this test case should be executed in accordance with the
instructions given in our
[Capsule Update documentation](../../guides/capsule-update.md).

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. Default logo firmware image

**Test setup**

1. Ensure that the DUT is running the firmware with the default logo.
1. Proceed with the [Test cases common documentation](#test-cases-common-documentation)
   section.

**Test steps**

1. Perform a capsule update using a valid capsule.
1. Verify that the update screen looks as expected.

**Expected result**

1. The update screen should look exactly as presented in the
   [Capsule Update documentation](../../guides/capsule-update.md).
