# What is Dasharo?

Dasharo is registered trademark and product developed by [3mdeb](https://3mdeb.com).

Dasharo is an open-source firmware distribution focusing on
[seamless deployment](#dasharo-seamless-deployment),
[clean and simple code](#dasharo-clean-and-simple-code),
[long-term maintenance](#dasharo-long-term-maintenance),
[professional support](#dasharo-support-package),
[transparent validation](#dasharo-transparent-validation),
[extensive and structured documentation](https://github.com/Dasharo/docs#navigation-menu),
[privacy-respecting implementation](#dasharo-privacy-respecting-implementation),
[liberty for the owners](#dasharo-liberty-for-the-owners) and
[trustworthiness for all](#dasharo-trustworthiness-for-all).

Dasharo consists of [productized services](TBD), set of
[open-source repositories](https://github.com/orgs/Dasharo/repositories),
and [quality control](TBD) which help to provide scalable, modular, easy to
combine open-source BIOS, UEFI, and firmware solutions. It offers the
components that are needed to develop and maintain a high quality, and modular
firmware, for the stability and security of your platform.

Dasharo provides optional features in subscription model called
[Supporters Entrance](../ways-you-can-help-us.md#become-a-dasharo-supporter).

## Why 3mdeb created Dasharo?

From our experience to be considered as serious player on firmware market there
is a need for a recognized brand with a proved history of successful
integrations. We were asked about that multiple times, by various parties over
years of providing services related to open-source firmware. Finally we decided
we have to make a move and create marketing vehicle under which we can deliver
added value like transparent validation, long-term maintenance, bleeding edge
integration for modern hardware and other products requested by community and
customers.

We also plan to provide a camp for all coreboot refugees e.g. platforms moved
to branch because of the need for code evolution. For more information please
read about [Intel Quark SoC deprecation][intel-quark],
[LEGACY_SMP_INIT & RESOURCE_ALLOCATOR_V3][legacy-smp].
More elaborate explanation of our position you can find
[below](#why-dasharo-team-is-against-moving-code-to-branches-in-coreboot).

Dasharo typically may get support for fully open platforms like
[Raptor Computing Systems Talos II][raptor] family, [ASUS KGPE-D16][kgpe-d16]
and other (not so open), but also very new stuff like [MSI Z690A DDR4][msi-z690a].

## What Dasharo provides?

For every supported hardware Dasharo Team provides:

* [Source code](https://github.com/Dasharo) with building procedures.
* Initial deployment, update and recovery procedures.
* Test Plan
* Hardware Configuration Matrix, which explain what hardware configuration we
  use in our labs for testing.
* [GPG keys](https://github.com/3mdeb/3mdeb-secpack/tree/master/dasharo)
* Signed binaries in release section

## What is Dasharo binary blob policy?

Modern x86 platforms' firmware requires closed source blobs to be integrated
into the image to properly initialize the silicon. The ecosystem is shifting
towards designs and technologies with a lot of small microcontrollers and
intellectual property (IP) blocks specialized in a very thin range of tasks.
Those microcontrollers and IP blocks typically require firmware blobs as well.
Some of the blobs are clearly visible, some may be obfuscated and hidden inside
the silicon or other firmware blobs (e.g. Intel Management Engine region
contains multiple other blobs besides the ME firmware -
[more about Intel ME blob](me.md)).

So Dasharo's binary blob policy is as follows:

> Integrate only the necessary amount of blobs required for proper platform
> operation and minimize the amount of blobs that are optional whenever
> possible by providing open equivalent implementations or removing them if
> there is no functional impact on the platform operation.

Dasharo also works without blobs on platforms that allow that. For example,
ASUS KGPE-D16 can run without any blobs (officially there is no PSP on that
hardware, and Opteron 6200 series CPUs can run without microcode patches).
