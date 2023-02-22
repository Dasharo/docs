# Device Manager

The Device Manager is a EDKII standard submenu which collects various device
setups like TPM, UEFI Secure Boot, TCG OPAL Drive Password, SATA Password and
others.

![](/images/menus/dev_mgr.jpeg){ class="center" }

## TCG Drive Management

This menu allows one to set up TCG OPAL disk password and manage other TCG OPAL
feature settings. The main view of the submenu looks as follows:

![](/images/menus/tcg_opal.jpeg){ class="center" }

The submenu will list all the TCG OPAL capable disks. Selecting one of them
with `ENTER` will cause entering the disk specific submenu:

![](/images/menus/tcg_opal2.jpeg){ class="center" }

Here one can enable the TCG OPAL security feature or restore factory default
with the PSID (Physical Security ID). Physical Security ID is a drive specific
key which is used to revert to factory default mode. The PSID can be typically
found on the sticker present on the disk.

Besides the feature enablement and factory restore options there is an action
interactive entry on the main TCG Drive Management page:

![](/images/menus/tcg_opal3.jpeg){ class="center" }

It is used to perform TCG OPAL specific operations when the security feature is
enabled. Enable/disable BlockSID will set/unset "freeze locking" of the drive
features as requested by OS. One may also enable or disable physical presence
(firmware popup confirmation of actions requested by OS) when switching
BlockSID.

To set up the password enter the desired disk submenu and enable the feature by
selecting the checkbox. Note that not all disks support the security feature of
TCG OPAL. Reset is required to apply changes. After reset you will be prompted
to set admin password. When the admin password is set, more options become
available for the disk:

![](/images/menus/tcg_opal3.jpeg){ class="center" }

All below options require reset to apply changes.

* `Update Drive Admin Password` - to update current admin password. Prompt
  window appears after reset to enter current and new password
* `Set Drive User Password` - is used to set an optional user password.
* `Secure Erase User Data` - performs secure erase of the data after reset.
* `Admin Revert to factory default and Disable` - disables the admin password
  (prompt will no longer appear during boot o unlock the drive) and the
  security feature after reset. Optionally one may select to keep or discard
  user data.
* `PSID Revert to factory default and Disable` - in case admin password has
  been forgotten PSID can be used to disable the security feature and admin
  password after reset. This will also erase user data.
* `Disable User` - disables the user functionality (and so the user password)
  after reset.

For more details about TCG OPAL please refer to
[TCG Storage Specifications and Key Management](https://trustedcomputinggroup.org/resource/tcg-storage-specifications-and-key-management/).

## Driver Health Manager

This submenu is informational only and displays the status of drivers that
install UEFI driver health protocol. Typically it is installed by 3rdparty
applications such as OptionROMs on graphics devices or network controllers for
example.

![](/images/menus/health_mgr.jpeg){ class="center" }

## Secure Boot Configuration

This submenu allows configuring UEFI Secure Boot functionality. By default
Dasharo firmware released after October 2022 has Secure Boot disabled by
default with no keys and certificates provisioned.

![](/images/menus/secure_boot.jpeg){ class="center" }

Option to enable Secure Boot (`Attempt Secure Boot`) will be grayed out as long
as there are missing keys and certificates in UEFI variables. In order to
provision default keys embedded into firmware image, select the
`Reset Secure Boot keys`. This will provision the default keys and unlock the
`Attempt Secure Boot` (which will be selected by default when all keys are
provisioned). The keys which are embedded in the firmware image come from
Microsoft:

* [Microsoft KEK certificate](https://go.microsoft.com/fwlink/?LinkId=321185)
* Microsoft Signature Database (db) consisting of:
    - [Microsoft Windows Production PCA 2011](https://go.microsoft.com/fwlink/p/?linkid=321192)
      to allow Windows OS Loader to load
    - [Microsoft Corporation UEFI CA 2011](https://go.microsoft.com/fwlink/p/?linkid=321194)
      to load OEM-approved UEFI drivers and applications (e.g. [shim](https://github.com/rhboot/shim))
* Microsoft Forbidden Signature Database (dbx) published as
 [UEFI Revocation List File on uefi.org](https://www.uefi.org/revocationlistfile)

To learn more, please visit
[Windows Secure Boot Key Creation and Management Guidance](https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/windows-secure-boot-key-creation-and-management-guidance?view=windows-11)

There is also a Dasharo PK certificate which is a certificate derived from a
randomly generated key by Dasharo Team. End user is expected to replace the PK
with their own key if UEFI driver or application signing is required.

One may also choose `Custom Mode` in `Secure Boot Mode` and provision own keys
and certificates:

![](/images/menus/secure_boot_custom.jpeg){ class="center" }

If `Custom Mode` is selected an additional entry appears
`Custom Secure Boot Options`. It is an advanced menu to manipulate Secure Boot
keys and certificates manually:

![](/images/menus/secure_boot_custom.jpeg){ class="center" }

Here one may delete and enroll particular keys, certificates and database
signatures.

## TCG2 Configuration

TCG2 Configuration submenu is responsible for displaying TPM 2.0 information
and managing the module.

![](/images/menus/tcg2_config.jpeg){ class="center" }

The basic information displayed are the TPM device family, interface, but also
information about supported hashing algorithms.

![](/images/menus/tcg2_config2.jpeg){ class="center" }

![](/images/menus/tcg2_config3.jpeg){ class="center" }

It is also possible to perform various TPM2 physical presence operations
(`TPM2 Operation`) and enable or disable PCR banks.

![](/images/menus/tcg2_actions.jpeg){ class="center" }

The supported TPM2 operations are:

* Disabling or enabling Owner and Endorsement hierarchies
* `TPM ClearControl(NO) + Clear` - performs TPM clear
* PCR Allocation - used to enable additional PCR banks
* `LogAllDigests` - on next reboot (and only on next reboot), add digests for
  all supported hashing algorithms to log file
* `ChangeEPS` - clears the TPM and changes its identity

For more details about the TPM operations see
[TCG Physical Presence Interface Specification](https://trustedcomputinggroup.org/wp-content/uploads/PC-Client-Platform-Physical-Presence-Interface-Specification-V1.4-R15_22July22.pdf)

## HDD Security Configuration

HDD Security Configuration allows one to set SATA disk password. Note that
all SATA disks will be displayed, even these that don't support the feature.

![](/images/menus/hdd_passwd.jpeg){ class="center" }

To check if the disk supports password feature, enter the specific disk submenu
to see if `Security Supported` displays `Yes`:

![](/images/menus/hdd_passwd2.jpeg){ class="center" }

If one scrolls down a bit, more information is displayed about current state of
the disk password feature:

![](/images/menus/hdd_passwd3.jpeg){ class="center" }

![](/images/menus/hdd_passwd4.jpeg){ class="center" }

At the bottom of the page there are two checkboxes:

* `Request to set User Password` - this is the option to set the password on
  the disk. Requires reset, after which the prompt windows will appear to set
  the password. From now on the prompt will appear on each boot.
* `Request to set Master Password` - this options changes the disk master
  password. Master password is used to recover from forgotten User Password.

Typically Master Password is provisioned during disk manufacturing and it will
not be possible to change it without knowing what the master password is.

To disable the User Password simply request to set the User Password again via
the menu. After reset you will be asked to unlock the driver with current
password and then type new password. To disable the password simply leave the
field empty and confirm it twice by pressing `ENTER`. After that the password
prompt will not appear again.

## Network Device List

This submenu is displayed when [Network Boot](dasharo-system-features.md#networking-options)
is enabled and the network controller driver installs the necessary UEFI
protocols. The menu lists the network devices with the UEFI protocol installed.
One may check out the network controller information, like MAC address,
driver used and link status. Example view with MAC address blurred:

![](/images/menus/net_dev_list.jpeg){ class="center" }

![](/images/menus/net_dev_list2.jpeg){ class="center" }

![](/images/menus/net_dev_list3.jpeg){ class="center" }
