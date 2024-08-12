# Frequenty Asked Questions about Capsule Update

## Q: Why was the traditional flashrom-based method replaced by capsule-based one?

A: There are many advantages of capsule-based update.
First of all, it's much easier[1]:

The steps to update efi firmware are:

1. `cat firmware.cap > /dev/efi_capsule_loader`
2. `reboot`

Not only is it simpler but also more efficient, because there is no need for
manual reset and disabling all of the protections before update, thus the whole
process takes less time. Speaking of protection the last but not least reason is
safety, the signed coalesced data can only be accessed after signatures are
verified by edk2, ensuring no unauthorized activity is allowed.

## Q: Is fwupd still Linux only?

A: No, fwupd isn't Linux only. Even the oldest release on GitHub (Feb 3, 2020)
has [fwupd-1.3.7-setup-x86_64.exe](https://github.com/fwupd/fwupd/releases/tag/1.3.7).
We also added support for BSD systems as part of
[fwdup-BSD](https://nlnet.nl/project/fwdup-BSD/) project.

However, this isn't the only software that uses capsules to perform the update,
Windows also uses it (although this would require creating and distributing
firmware as drivers through Windows Update, which is beyond the scope of this
project). Linux can also be compiled with
[EFI_CAPSULE_LOADER](https://lore.kernel.org/all/1454042394-21507-1-git-send-email-hock.leong.kweh@intel.com/T/)
which exposes an interface for sending capsules to the firmware by a simple
write to file.

## Q: Where in the process are signatures verified?

A: As mentioned above, signatures are verified by edk2, on coalesced data. There
are decisions made earlier based on presence of data, not on it's content. Hence
the focus on not allowing booting an OS with full access to flash enabled when
edk2 decides that the capsule isn't valid.

## Q: Why is coreboot needed while edk2 is gathering capsule chunks form memory?

- It is coreboot that applies flash write protections, which must
temporarily be lifted for edk2 to perform the update.
- coreboot also implements code for writing to flash (as an extension of
SMMSTORE_V2), so edk2 doesn't even need to be aware of each chipset's unique
way of interacting with the SPI controller.
