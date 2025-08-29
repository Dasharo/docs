# Frequently Asked Questions about Sovereign Boot Provisioning Wizard

## Why the key fingerprint is not showing when asked to trust a new bootloader?

If the fingerprint is not shown, then either the image is unsigned or there
was something wrong when parsing the image. In such case the Sovereign Boot
Provisioning Wizard may display empty data.

Also In the RC1 version of the Sovereign Boot Provisioning Wizard, the
signature parsing was not yet implemented. Thus the fingerprints were intended
to be empty.

## Will the enrolled keys change if the OS gets updated?

Enrolled keys will not change without the user explicit action, e.g.
modification through firmware setup or the Sovereign Boot Provisioning Wizard
itself.

Operating system will not be able to change the keys nor any Secure Boot
variable, because Sovereign Boot Provisioning Wizard removes KEK, and enrolls
an ephemeral PK. KEK and PK are the only keys that can sign an authorized
update to Secure Boot db/dbx variables.

## Will BIOS password prevent an attacker to trust a newly attached bootloader?

The only BIOS password feature currently available in Dasharo is the [BIOS
Setup Menu
password](../dasharo-menu-docs/overview.md#user-password-management). This
password prevents only unauthorized entrances to setup menu. It is not able to
protect against trusting a newly attached bootloader by using the Sovereign
Boot Provisioning Wizard capability to prompt to trust the bootloader when
bootloader. verification fails.

That is why besides enabling Sovereign Boot Provisioning Wizard, one should
also enable:

* Either [BIOS boot password](https://github.com/Dasharo/dasharo-issues/issues/1547)
  that will authorize the user before attempting to boot anything.
* Or [Sovereign Boot Provisioning Wizard lockdown
  mode](https://github.com/Dasharo/dasharo-issues/issues/1552) to disable the
  possibility to trust bootloaders that fail verification after Sovereign Boot
  Wizard is provisioned. Once lockdown mode is enabled, the BIOS Setup Menu
  should be enabled and set as well.

## Sovereign Boot password protection is not implemented yet?

The only BIOS password feature currently available in Dasharo is the [BIOS
Setup Menu
password](../dasharo-menu-docs/overview.md#user-password-management). This
password prevents only unauthorized entrances to setup menu. As the Sovereign
Boot Provisioning Wizard runs outside of the BIOS setup application, one needs
a BIOS Boot password feature.

BIOS Boot Password is currently at the feature request stage, which you may
track [here](https://github.com/Dasharo/dasharo-issues/issues/1547). This
password will be checked before the BIOS attempt to run any bootloader, thus
preventing the Wizard to be triggered by the bootloader verification failure
and potentially trust any bootloader without BIOS boot password owner's
consent.
