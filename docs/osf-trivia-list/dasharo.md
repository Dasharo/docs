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

[coreboot-scope]: https://doc.coreboot.org/#scope-of-the-coreboot-project
[dtsos]: ../../dasharo-tools-suite/overview/
[lvfs]: https://fwupd.org/lvfs/docs/consulting
[gerrit-review]: https://review.coreboot.org/c/homepage/+/63402
[cb-distro]: https://doc.coreboot.org/distributions.html
[intel-quark]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/YRJQIPVK5WHACT64TH42CLGD4TXG3XTS/#PZUIFZZHRK7M3NLBNLI6VUBD4O52245B
[legacy-smp]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/EEEBFATYHWIPRDXLCUEFNDZ4FYYVA4QM/#QHIYXYTVOGXENJXUOWOXUZOTLV5OS4LB
[raptor]: ../../variants/talos_2/releases/
[kgpe-d16]: ../../variants/asus_kgpe_d16/releases
[msi-z690a]: ../../variants/msi_z690/overview/
[vpub]: https://vpub.dasharo.com/
