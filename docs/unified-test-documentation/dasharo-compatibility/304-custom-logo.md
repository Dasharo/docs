# Dasharo compatibility: Custom Logo

## CLG001.001 Custom boot logo

**Test description**

This test aims to verify that the DUT is configured to display the specified
(customized) logo at boot.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).

**Test steps**

1. Power on the DUT.
1. Wait for the boot logo to appear.

**Expected result**

The displayed logo should depend on the Dasharo variant:

* if the Dasharo variant is NovaCustom - the NovaCustom logo should be displayed,
* if the Dasharo variant is Protectli - the Protectli logo should be displayed,
* if the Dasharo variant is Tuxedo - the Tuxedo logo should be displayed,
* for all other variants Dasharo custom logo should be displayed.

Keep in mind that the end-user's customized boot logo might also be displayed -
if before the custom logo checking procedure described in the
[Logo customization](../../guides/logo-customization.md)
documentation has been performed.
