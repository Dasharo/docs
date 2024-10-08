# FAQ

## Why MSI Z690-A (WIFI) (DDR4) was chosen for Dasharo ?

Please read [this extensive analysis][msi_port_analysis] contributed to Intel
Reddit.

## Why do you use the nomenclature `MSI Z690-A (WIFI) (DDR4)`?

This nomenclature is the result of the naming used by the producer.
`MSI PRO Z690-A` is the nomenclature used for naming the platform with
DDR5 memory slots. If the platform is also equipped with the WiFi module, its
naming nomenclature will additionally include the phrase `WIFI`. If instead of
DDR5 memory slots, the platform is equipped with DDR4 memory slots, and its naming
nomenclature will additionally include the phrase `DDR4`.

## Will this work on my `MSI PRO Z690-A` (model with DDR5 support)?

Yes, during test procedures the Dasharo firmware work has been confirmed for
the DDR5 platform without WIFI.

## Will this work on my `MSI PRO Z690-A DDR4`?

Yes, during test procedures the Dasharo firmware work has been confirmed for
the DDR4 WIFI platform. In turn, Dasharo working correctness on
`MSI PRO Z690-A DDR4` has been confirmed by the community.

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

In such a case, you would get stuck with a black screen on the display. There will
be no beeping sounds from the buzzer as well. The only way to get some
information on what's going on in that state is to use the [Serial
header](development.md#hardware-connection) to read out error information.

## What can be the reason for a board "bricking"?

The most common reason would be the fact that your DDR memory modules are not
initialized properly.

The other reason might be improper or interrupted installation. Please make sure
to follow the [Initial Deployment Manual](initial-deployment.md) correctly.

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

The list of all supported memory modules is available in the
[Memory HCL](hcl.md) documentation.

## What is the memory profile?

Dasharo firmware currently picks the highest standard SPD Profile, with no support
for XMP ones. This means that the Kingston modules, it is actually working at
2400 MHz, but it is expected to work all the way to 3200 MHz.

## Why my GPU doesn't work on `MSI PRO Z690-A (DDR4) (WIFI)`?

Due to the fact, that there's no possibility to insert all available GPU drivers
into the firmware, the solution in the form of the `Option ROM` is in use.
`Option ROMs` are the drivers flashed in the GPUs' non-volatile memory. These
drivers can be divided into `Legacy Option ROMs` and `EFI Option ROMs`.

`Legacy Option ROMs` are only supported on legacy BIOS, such as SeaBIOS. Legacy
BIOS checks the availability of `Option ROM` and if its signature matches, it
executes its entry point. This option ROM initializes the graphics. The only way
to support `Option ROM` in UEFI is through CSM, which we do not have
implemented.

`EFI Option ROMs` are nothing more than EFI drivers which have the same form as
the UEFI files (PE format). UEFI firmware scans the `Option ROM` space of the
graphics card and if it finds a potential `EFI Option ROM` with a PE signature, it
executes the file. This option ROM initializes the graphics.

Considering the above, the firmware might have a problem with initializing older
graphics cards - UEFI standard appeared about 15 years ago.

The problem might also be caused by an enabled `Secure boot` - because there is
no certainty that `EFI Option ROM` is signed correctly.

[msi_port_analysis]: https://www.reddit.com/r/intel/comments/subaro/how_many_people_are_interesed_in_seeing_coreboot/

## Which GPUs are supported?

We can say the "supported" one is the one that has been tested during
Validation Procedure or have been tested by the community.

The list of all supported memory modules is available in the
[GPU HCL](hcl.md) documentation.

## What does the obligatory Dasharo Subscription include?

The Dasharo Subscription includes:

* The latest Dasharo Pro Package release installed by the Dasharo Team
* Dasharo Updates – The number of updates depends on the number of Dasharo
  Subscriptions sold and the availability of other funding (e.g., NLNet,
  corporate sponsors, [community
  donations](https://docs.dasharo.com/ways-you-can-help-us/#donate-money))
* Priority support for Dasharo Subscribers through invite-only Matrix channel
* Influence on Dasharo features roadmap – you can have a real impact on Dasharo
  development by direct access with the developers or premium voting on GitHub.
  You will gain access to the dedicated channels on the matrix communicator.
  If you wish to share your GitHub nickname with us, the votes cast for the
  features that you would like to have implemented in the future will be treated
  with priority, i.e. they will have a higher priority than the votes of
  non-subscribers.
* By buying this product, you support open-source firmware and Dasharo
  distribution.

## What does the warranty condition "No signs of customer interference..." mean?

Full question:
"In the Disclaimer, you wrote that one of the warranty
conditions is: "No signs of customer interference with the platform or
firmware." How would a user modify firmware without losing the warranty? Being
open source to be easy to modify, then saying "don't touch this" seems
contradictory. How would you add an exception?"

Playing with firmware parameters can result in damaging the mainboard.
Such action excludes the acceptance of the return.

You can improve Dasharo by contributing, and when it passes the
Dasharo Certification Program, can we release it in the next version.

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
Freight. Failure to inspect for damages at the time of delivery could result in
Freight voiding any subsequent damage claims.
