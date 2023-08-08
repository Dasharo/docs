# Dasharo Security: TCG OPAL disk password support

## DMP001.001 TCG OPAL disk password set and check

**Test description**

This suite tests disk password that can be set on the disk. After setting it up
it is required to type in the password at every boot. The test password used is
`123` and after setting it up it is removed.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md).

**Test steps**

1. Power on the DUT.
1. Enter Setup Menu Tianocore
1. Open `Device manager`
1. Open `TCG Drive Management`
1. Select the disk
1. Check `Enable Feature` option
1. Save and restart
1. Type in the new password
1. Confirm the password
1. Restart to test if password is set
1. Type in the password - it should be successful

**Removing the password**

1. Open `Device manager`
1. Open `TCG Drive Management`
1. Select the disk
1. Check `Admin Revert to factory default and Disable`
1. Save and restart
1. Type in the password to unlock
1. Type in the password to remove it

**Expected result**

Password prompt should show up:

* after setting up the password option
* after reboot
* after removing the password
