# FAQ

## Why MSI Z690-A (WIFI) (DDR4) was chosen for Dasharo ?

Please read [this extensive analysis][msi_port_analysis] contributed to Intel
Reddit.

## Why do you use the nomenclature `MSI Z690-A (WIFI) (DDR4)`?

This nomenclature is the result of the naming used by the producer. `MSI PRO
Z690-A` is the nomenclature used for naming the platform with DDR5 memory
slots. If the platform is also equipped with the WiFi module, its naming
nomenclature will additionally include the phrase `WIFI`. If instead of DDR5
memory slots, the platform is equipped with DDR4 memory slots, and its naming
nomenclature will additionally include the phrase `DDR4`.

## Will this work on my `MSI PRO Z690-A` (model with DDR5 support)?

Yes, during test procedures the Dasharo firmware work has been confirmed for
the DDR5 platform without WIFI.

## Will this work on my `MSI PRO Z690-A DDR4`?

Yes, during test procedures the Dasharo firmware work has been confirmed for
the DDR4 WIFI platform. In turn, Dasharo working correctness on `MSI PRO
Z690-A DDR4` has been confirmed by the community.

## Can I safely test this on my board?

Thanks to the introduction of FlashBIOS, it's now safe to experiment with this
on your board. If any issues arise, you can effortlessly revert to the stock
firmware without requiring special equipment. However, if you're unfamiliar
with [recovery processes](recovery.md) and feel apprehensive, please [contact
the Dasharo Matrix Community](https://matrix.to/#/#dasharo:matrix.org) for
assistance. We're continuously working to simplify the recovery process, and
our recommendations may be updated accordingly.

## Can I destroy my hardware by installing this firmware?

We give no warranty, although it is highly unlikely, provided that you use the
supported board model and follow the [Initial
Deployment](initial-deployment.md). In the worst scenario, you might "brick"
the board, rendering it unbootable. It can be fixed by following the [recovery
procedure](recovery.md). In case of concerns, we invite you to buy the
equipment directly in our [online
store](https://shop.3mdeb.com/product-category/dasharo-supported-hardware/)
with a subscription service, under which we perform the Dasharo installation
with the latest release, and offer full support through invite-only Matrix
channel.

## How can I know if the board is "bricked"?

In such a case, you would get stuck with a black screen on the display. There
will be no beeping sounds from the buzzer as well. The only way to get some
information on what's going on in that state is to use the [Serial
header](development.md#hardware-connection) to read out error information.

## What can be the reason for a board "bricking"?

The most common reason would be the fact that your DDR memory modules are not
initialized properly.

The other reason might be improper or interrupted installation. Please make
sure to follow the [Initial Deployment Manual](initial-deployment.md)
correctly.

## How can I "unbrick" my board?

Please follow the [recovery procedure](recovery.md).

## Which CPUs are supported?

We can say the "supported" one is the one that has been tested during
Validation Procedure or have been tested by the community.

The list of all supported CPUs is available in the [CPU HCL](hcl.md)
documentation.

In practice, any Alder Lake-S Processor should work.

## Is overclocking possible?

With Dasharo, overclocking via BIOS setup is not possible. Overclocking
capabilities are essentially limited to what Intel XTU can achieve on Windows.
Additionally, RAM XMP may pose challenges, as FSP lacks the flexibility to
properly tune the RAM training parameters.

## Which memory modules are supported?

We can say the "supported" one is the one that has been tested during
Validation Procedure or have been tested by the community.

The list of all supported memory modules is available in the [Memory
HCL](hcl.md) documentation.

## What is the memory profile?

Dasharo firmware currently picks the highest standard SPD Profile, with no
support for XMP ones. This means that the Kingston modules, it is actually
working at 2400 MHz, but it is expected to work all the way to 3200 MHz.

## Why my GPU doesn't work on `MSI PRO Z690-A (DDR4) (WIFI)`?

Due to the fact, that there's no possibility to insert all available GPU
drivers into the firmware, the solution in the form of the `Option ROM` is in
use. `Option ROMs` are the drivers flashed in the GPUs' non-volatile memory.
These drivers can be divided into `Legacy Option ROMs` and `EFI Option ROMs`.

`Legacy Option ROMs` are only supported on legacy BIOS, such as SeaBIOS.
Legacy BIOS checks the availability of `Option ROM` and if its signature
matches, it executes its entry point. This option ROM initializes the
graphics. The only way to support `Option ROM` in UEFI is through CSM, which
we do not have implemented.

`EFI Option ROMs` are nothing more than EFI drivers which have the same form
as the UEFI files (PE format). UEFI firmware scans the `Option ROM` space of
the graphics card and if it finds a potential `EFI Option ROM` with a PE
signature, it executes the file. This option ROM initializes the graphics.

Considering the above, the firmware might have a problem with initializing
older graphics cards - UEFI standard appeared about 15 years ago.

The problem might also be caused by an enabled `Secure boot` - because there
is no certainty that `EFI Option ROM` is signed correctly.

[msi_port_analysis]: https://www.reddit.com/r/intel/comments/subaro/how_many_people_are_interesed_in_seeing_coreboot/

## Which GPUs are supported?

We can say the "supported" one is the one that has been tested during
Validation Procedure or have been tested by the community.

The list of all supported memory modules is available in the [GPU HCL](hcl.md)
documentation.

## What does the obligatory Dasharo Subscription include?

The Dasharo Subscription includes:

* The latest Dasharo Pro Package release installed by the Dasharo Team
* Dasharo Updates – The number of updates depends on the number of Dasharo
  Subscriptions sold and the availability of other funding (e.g., NLNet,
  corporate sponsors, [community
  donations](https://docs.dasharo.com/ways-you-can-help-us/#donate-money))
* Priority support for Dasharo Subscribers through invite-only Matrix channel
* Influence on Dasharo features roadmap – you can have a real impact on
  Dasharo development by direct access with the developers or premium voting
  on GitHub. You will gain access to the dedicated channels on the matrix
  communicator. If you wish to share your GitHub nickname with us, the votes
  cast for the features that you would like to have implemented in the future
  will be treated with priority, i.e. they will have a higher priority than
  the votes of non-subscribers.
* By buying this product, you support open-source firmware and Dasharo
  distribution.

## What does the warranty condition "No signs of customer interference..." mean?

Full question: "In the Disclaimer, you wrote that one of the warranty
conditions is: "No signs of customer interference with the platform or
firmware." How would a user modify firmware without losing the warranty? Being
open source to be easy to modify, then saying "don't touch this" seems
contradictory. How would you add an exception?"

Playing with firmware parameters can result in damaging the mainboard. Such
action excludes the acceptance of the return.

You can improve Dasharo by contributing, and when it passes the Dasharo
Certification Program, can we release it in the next version.

## How should I inspect the package for any signs of potential damage upon delivery?

Inspecting Your Shipment: Before the shipment we take pictures of both the
hardware and packaging. After it leaves our office we do not have any control
over it. It is the consignee’s responsibility to inspect their shipment for
damages before the Freight driver leaves the delivery location.

Should the packaging display any signs of damage, open it immediately to check
the contents, requesting the driver's presence to inspect together. If your
shipment has been damaged, document the damages on the delivery receipt in
detail and have it signed by the driver. If possible, please take pictures of
the damages to the box and the damages to the item.

Please notify us immediately so that we can initiate a damage claim with
Freight. Failure to inspect for damages at the time of delivery could result
in Freight voiding any subsequent damage claims.

## Are MSI PRO Z690-A and Z790-P firmware releases production-ready?

Both platforms are still considered pre-production and have not been formally
promoted to production-level status. Older Z690-A releases use v1.x.x numbering,
but this alone does not indicate production-level maturity under the current
[Dasharo versioning
policy](https://docs.dasharo.com/dev-proc/versioning/#promotion-to-production-level-versioning-v100-and-up).
Stability issues have been reported with Z690-A v1.1.7 and Z790-P v0.9.5. Users
experiencing these issues may consider previous firmware versions while awaiting
fixes. For the latest information, check the [Z690-A release
notes](https://docs.dasharo.com/variants/msi_z690/releases/), [Z790-P release
notes](https://docs.dasharo.com/variants/msi_z790/releases/) and [known issues
on GitHub](https://github.com/Dasharo/dasharo-issues/issues).

## Which motherboard is recommended: MSI PRO Z690-A or Z790-P?

We generally recommend the [MSI PRO
Z790-P](https://shop.3mdeb.com/product/msi-pro-z790-p-wifi-ddr5-motherboard-with-dasharo-pro-package/).
It is a newer platform, better suited for high-performance 13th and
14th-generation Intel processors. Both motherboards offer similar functionality
with Dasharo, but the Z790-P chipset provides improvements in PCIe connectivity,
including PCIe Gen4 support for certain slots previously limited to Gen3.
Additionally, Z690-A motherboards are becoming increasingly difficult to obtain.

## Which motherboard offers better compatibility with Qubes OS?

Both MSI PRO Z690-A and Z790-P offer comparable compatibility with Qubes OS when
using Dasharo firmware. The Z690-A was previously offered in an officially
Qubes-certified configuration, although that product is no longer available. The
Z790-P can also run Qubes OS, but this should not be interpreted as official
certification of every hardware configuration.

## Can I use dedicated GPUs and PCIe passthrough with Qubes OS?

GPU compatibility depends on the selected Dasharo firmware variant and hardware
configuration. The Dasharo (coreboot+Heads) configuration has limitations
regarding dedicated GPU initialization and display output. See
[Issue #794](https://github.com/Dasharo/dasharo-issues/issues/794). Dasharo
(coreboot+UEFI) does not have this particular Heads limitation. However, PCIe
device passthrough may still encounter issues related to PCIe bus resets, as
described in [Issue #771](https://github.com/Dasharo/dasharo-issues/issues/771).
Users planning to use GPU passthrough should verify compatibility with their
specific GPU models and firmware version.

## Can reflashing Dasharo firmware remove potential tampering?

Reflashing Dasharo with a trusted firmware image can remove many software-based
firmware modifications, provided the affected flash regions are overwritten.
However, reflashing cannot guarantee the removal of all forms of tampering,
particularly physical hardware modifications. Some situations may require
external firmware programming or additional hardware inspection. Software
reflashing alone should not be considered a complete guarantee against
tampering.

## Can I selectively disable NVMe drives in Dasharo for secure dual boot?

No. Dasharo currently does not provide an option to selectively disable
individual NVMe drives through firmware settings. However, this does not prevent
dual boot configurations. Ubuntu and Windows dual boot has been successfully
validated with Dasharo. Please note that dual boot does not provide complete
isolation between operating systems, as both systems may still be able to access
connected storage devices.

# Dasharo (coreboot+Heads) variant (not supported by Dasharo)

## The TPM module is required to install Heads. Will this one work?

We do not recommend to buy any cheap replacement TPM chips. We observed board
malfunctions with such chips. We can only advise to buy original [MSI TPM
chips](https://www.msi.com/Motherboard/TPM-20-Module). Either TPM 2.0
(MS-4462) or TPM 2.0 (9672), both will work. Please pay attention to the
interface used and pin count, it must be SPI interface and 12-1 pin. You can
also find this product available in [our
shop](https://shop.3mdeb.com/shop/modules/tpm-2-0-msi-ms-4462/).

To be precise, TPM is required to run Dasharo (coreboot+Heads) properly.
Installation will succeed, but you will observe errors once you boot to heads.

## Is it better to install Qubes OS before switching to Dasharo (coreboot+Heads)?

If you ever want to transition back to Dasharo (coreboot+UEFI) and do not want
to reinstall Qubes OS, then yes, it is best to install Qubes OS on UEFI
firmware. In other cases reinstallation may be needed when switching between
firmware flavours.

## Will it work successfully once I get TPM, or is there some other issues?

The Nitrokey tokens had a security vulnerability, which required the firmware
on the token and heads to be both updated to fix this. Unfortunately, Dasharo
heads firmware compatible with MSI desktops was not updated to fix this
problem and it is not planned to have a new release. The community interest in
heads on MSI desktops was too low to justify expenses, development and
maintainership of this firmware flavour.

That said, Dasharo + Heads firmware is no longer recommended to be
installed/used with Nitrokeys on MSI desktops. For these particular reasons we
no longer offer heads DPP subscriptions for MSI desktops anymore in our shop.
