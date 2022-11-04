# FAQ

## Why MSI Z690-A WIFI DDR4 was chosen for Dasharo ?

Please read [this extensive analysis][msi_port_analysis] contributed to Intel
Reddit.

## Will this work on my `MSI PRO Z690-A WIFI DDR5` or `MSI PRO Z690-A DDR5` ?

Not yet. The build is configured for the DDR4 only. But currently we work on the
DDR5 variant. **Do not try that**.

## Will this work on my `MSI PRO Z690-A DDR4` ?

Yes, it will work on your platform. Working on MSI PRO Z690-A DDR have been
confirmed during the test procedures.

## Can I safely try this on my board?

If you are afraid of bricking the board and have no means of [recovering from
failed installation](../recovery), we **do not recommend** trying it out until
at least the v1.0.0 is released. Recovery process is not suitable for
inexperienced users right now. We will be trying to make it easier, and if that
happens, we may change our recommendation here.

## Can I destroy my hardware by installing this firmware?

We give no warranty, although it is highly unlikely, provided that you use the
supported board model and follow the [Initial
Deployment](../initial-deployment). In the worst scenario, you might "brick" the
board, rendering it unbootable. It can be fixed by following the [recovery
procedure](../recovery). In case of concerns, we invite you to buy the equipment
directly in our [online
store](https://3mdeb.com/?s=msi&post_type=product&dgwt_wcas=1) with a
subscription service, under which we perform the Dasharo installation with the
latest release, and offer full support through invite-only Matrix channel.

## How can I know if the board is "bricked"?

In such a case, you would get stuck with black screen on the display. There will
be no beeping sounds from the buzzer as well. The only way to get some
information on what's going on in that state is to use the [Serial
header](../development/#hardware-connection) to read out error information.

## What can be the reason of board "bricking"?

The most common reason would be the fact that you DDR memory modules are not
initialized properly.

The other reason might be improper or interrupted installation. Please make sure
to follow the [Initial Deployment Manual](../initial-deployment) correctly.

## How can I "unbrick" my board?

Please follow the [recovery procedure](../recovery).

## Which CPUs are supported?

We can say the "supported" one is the one that have been tested during
Validation Procedure or have been tested by the community.

The list of all supported CPUs is available in the
[CPU HCL](../cpu-hcl) documentation.

In practice, any Alder Lake-S Processor should work.

12900KS is rather unknown at the moment, because it was released later and may
require more recent microcode.

## Which memory modules are supported?

We can say the "supported" one is the one that have been tested during
Validation Procedure or have been tested by the community.

The list of all supported memory modules is available in the
[Memory HCL](../memory-hcl) documentation.

## What is the memory profile?

Currently, Dasharo firmware picks the highest standard SPD Profile, no support
for XMP ones. This means that on the Kingston modules it is actually working at
2400 MHz, but it is expected to work all the way to 3200 MHz.

## Why my GPU doesn't work on `MSI PRO Z690-A DDR4` ?

Due to the fact, that there's no possibility to insert all available GPU drivers
into the firmware, the solution in the form of the `Option ROM` is in use.
`Option ROMs` are the drivers flashed in the GPUs non-volatile memory. These
types of drivers can be divided into `Legacy Option ROMs` and `EFI Option ROMs`.

`Legacy Option ROMs` are only supported on legacy BIOS, such as SeaBIOS. Legacy
BIOS checks the availability of `Option ROM` and if its signature matches, it
executes its entry point. This option ROM initializes the graphics. The only way
to support `Option ROM` in UEFI is through CSM, which we do not have
implemented.

`EFI Option ROMs` are nothing more than EFI drivers which have the same form as
the UEFI files (PE format). UEFI firmware scans the `Option ROM` space of the
graphics card and if it finds a potential `EFI Option ROM` with PE signature, it
executes the file. This option ROM initializes the graphics.

Considering the above, the firmware might have a problem with initializing older
graphics cards - UEFI standard appeared about 15 years ago.

The problem might also be caused by an enabled `Secure boot` - because there is
no certainty that `EFI Option ROM` is signed correctly.

[msi_port_analysis]:
    https://www.reddit.com/r/intel/comments/subaro/how_many_people_are_interesed_in_seeing_coreboot/

## Which GPUs are supported?

We can say the "supported" one is the one that have been tested during
Validation Procedure or have been tested by the community.

The list of all supported memory modules is available in the
[GPU HCL](../gpu-hcl) documentation.

## What does the obligatory Dasharo Subscripion includes?

The Dasharo Bronze Subscription includes:

* The latest Dasharo release installed by Dasharo Team
* Dasharo Updates – number of updates depends on the number of Dasharo
  Subscriptions sold and the availability of other funding (e.g., NLNet,
  corporate sponsors, [community
  donations](https://docs.dasharo.com/ways-you-can-help-us/#donate-money))
* Priority support for Dasharo Subscribers through invite-only Matrix channel
* Influence on Dasharo features roadmap – you can have a real impact on Dasharo
  development by direct access wit the developers or premium voting on github.
  You will gain the access to the dedicated channels on the matrix communicator.
  If you wish to share your Github nickname with us, the votes cast for the
  features that you would like to have implemented in the future will be treated
  with priority, i.e. they will have a higher priority than the votes of
  non-subscribers.
* By buying this product, you support open-source firmware and Dasharo
  distribution.

## In the Disclaimer, you wrote that one of the warranty conditions is: "No signs of customer interference with the platform or firmware." How would a user modify firmware without losing the warranty? Being open source to be easy to modify, then saying "don't touch this" seems contradictory. How would you add an exception?

Playing with firmware parameters can result in damaging the mainboard. Such
action excludes the acceptance of the return. You can improve the Dasharo by
contributing, so	we can pass Dasharo Certification Program and release it in
the next version.
