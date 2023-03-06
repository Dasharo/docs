# Frequenty Asked Questions about Dasharo

## What is Dasharo?

Dasharo is registered trademark and product developed by [3mdeb](https://3mdeb.com).

Dasharo is an open-source firmware distribution focusing on:

- [seamless deployment](#dasharo-seamless-deployment),
- [clean and simple code](#dasharo-clean-and-simple-code),
- [long-term maintenance](#dasharo-long-term-maintenance),
- [professional support](#dasharo-support-package),
- [transparent validation](#dasharo-transparent-validation),
- [extensive and structured documentation](#dasharo-documentation),
- [privacy-respecting implementation](#dasharo-privacy-respecting-implementation),
- [liberty for the owners](#dasharo-liberty-for-the-owners) and
- [trustworthiness for all](#dasharo-trustworthiness-for-all).

Dasharo consists of [commercial services](#productized-services) available for
business customers, set of [open-source
repositories](https://github.com/orgs/Dasharo/repositories), and [quality
control](../../unified-test-documentation/overview/) which help to provide
scalable, modular, easy to combine open-source BIOS, UEFI, and firmware
solutions. It offers the components that are needed to develop and maintain a
high quality, and modular firmware, for the stability and security of your
platform.

For individuals Dasharo provides optional features in subscription model called
[Supporters Entrance](../dts/#how-to-get-dasharo-tools-suite-supporters-entrance).

## Why 3mdeb created Dasharo?

3mdeb created Dasharo to establish a recognized brand with a proven history of
successful firmware integrations. Dasharo aims to deliver added
value to customers and the community as an open-source firmware distribution,
such as transparent validation, long-term maintenance, bleeding-edge
integration for modern hardware, and other products requested by the community
and customers.

3mdeb has been providing services related to open-source firmware for years and
has been asked multiple times by various parties to create a recognized brand.
Therefore, the creation of Dasharo was a move to fulfill that need and
establish a marketing vehicle to deliver value to customers.

In addition, 3mdeb plans to provide a camp for all coreboot refugees, including
platforms moved to branches due to the need for code evolution, such as Intel
[Intel Quark SoC deprecation][intel-quark] and [LEGACY_SMP_INIT &
RESOURCE_ALLOCATOR_V3][legacy-smp]. We want to provide solutions for those
requiring long-term maintenance and firmware support. More elaborate
explanation of our position you can find
[below](#why-dasharo-team-is-against-moving-code-to-branches-in-coreboot).

Dasharo typically supports fully open platforms like [Raptor Computing Systems
Talos II][raptor] family, [ASUS KGPE-D16][kgpe-d16], and other which are not as
open but provide modern computing experience, such as [MSI PRO Z690-A
DDR4/DDR5][msi-z690a]. The goal is to provide a reliable, secure, and scalable
firmware solution for a wide range of platforms and applications, aligning with
the vision of a new golden age of computing advocated by experts in computer
architecture.

## What Dasharo provides?

Dasharo has 10 rules that govern the production and release of firmware within
its ecosystem. Dasharo rules define what we deliver with every release. These
rules are:

1. Every release of firmware produced by Dasharo Ecosystem must contain [source
code](https://github.com/Dasharo), binary, SHA256 hash, and Dasharo
cryptographic signature of that hash.
1. Dasharo Universe contains structured documentation for key activities
related to open-source firmware life-cycle: initial deployment, update and
recovery.
1. Cryptographic keys hierarchy should be followed:

    + [CEO/Founder](https://github.com/3mdeb/3mdeb-secpack/blob/master/keys/owner-key/piotr-krol-key.asc)
(GPG fingerint: `E030 9B2D 85A6 7E84 6329  E34B B2EE 71E9 67AA 9E4C`) which
signs
    + [3mdeb Master
Key](https://github.com/3mdeb/3mdeb-secpack/blob/master/keys/master-key/3mdeb-master-key.asc)
(GPG fingerint: `1B57 85C2 965D 84CF 85D1  652B 4AFD 81D9 7BD3 7C54`) which
signs
    + [3mdeb Dasharo Master
Key](https://github.com/3mdeb/3mdeb-secpack/blob/master/dasharo/3mdeb-dasharo-master-key.asc)
(GPG fingerint: `0D5F 6F1D A800 329E B7C5  97A2 ABE1 D0BC 6627 8008`) which
signs
    + [Customer Open Source Firmware Release x.y Signing
Key](https://github.com/3mdeb/3mdeb-secpack/tree/master/customer-keys) (e.g.
Novacustom Open Source Firmware Release 1.0 Signing Key)
    + or [dedicated 3mdeb
keys](https://github.com/3mdeb/3mdeb-secpack/tree/master/dasharo) to given
platform.

    Keys can be found in
    [3mdeb-secpack](https://github.com/3mdeb/3mdeb-secpack) repository.

1. Every release of firmware produced by Dasharo Ecosystem must have an
attached test report according to requirements. Every test should be described
by test specification documentation.
1. Customer-specific Dasharo validation procedures are delivered with the
release notes directly to the customer and does not have to be publicly
available.
1. Every firmware produced by Dasharo Ecosystem use [Semantic Versioning
2.0.0](https://semver.org/) compatible versioning scheme. For details please
check [description](../../dev-proc/versioning).
1. Every firmware produced by Dasharo Ecosystem should use [Keep A Changelog
1.0.0](https://keepachangelog.com/en/1.0.0/) compatible scheme as changelog
format.
1. Every Dasharo firmware release should be delivered with integrity and
signature verification procedures.
1. Every Dasharo firmware release must contain a detailed description of
components and links to the range of code changes since the last release.
1. Dasharo Ecosystem uses open-source software to create and maintain its
firmware solutions, and the company strives to maintain transparency in its
processes and procedures.

These 10 rules are designed to ensure that every release of firmware produced
by Dasharo Ecosystem is reliable, secure, and meets the needs of customers and
the community. By following these rules, Dasharo Ecosystem provides a
consistent and high-quality firmware solution for a wide range of platforms and
applications.

[coreboot-scope]: https://doc.coreboot.org/#scope-of-the-coreboot-project
[dtsos]: ../../dasharo-tools-suite/overview/
[lvfs]: https://fwupd.org/lvfs/docs/consulting
[gerrit-review]: https://review.coreboot.org/c/homepage/+/63402
[cb-distro]: https://doc.coreboot.org/distributions.html
[intel-quark]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/YRJQIPVK5WHACT64TH42CLGD4TXG3XTS/#PZUIFZZHRK7M3NLBNLI6VUBD4O52245B
[vpub]: https://vpub.dasharo.com/

## What is Dasharo binary blob policy?

Modern x86 platforms' firmware requires closed source blobs to be integrated
into the image to properly initialize the silicon. The ecosystem is shifting
towards designs and technologies with a lot of small microcontrollers and
intellectual property (IP) blocks specialized in a very thin range of tasks.
Those microcontrollers and IP blocks typically require firmware blobs as well.
Some of the blobs are clearly visible, some may be obfuscated and hidden inside
the silicon or other firmware blobs (e.g. Intel Management Engine region
contains multiple other blobs besides the ME firmware -
[more about Intel ME blob](../me)).

So Dasharo's binary blob policy is as follows:

> Integrate only the necessary amount of blobs required for proper platform
> operation and minimize the amount of blobs that are optional whenever
> possible by providing open equivalent implementations or removing them if
> there is no functional impact on the platform operation. Ultimately the blobs
> should be attested and properly documented. Dasharo Team is trying to achieve
> it by working on [firmware SBOMs](https://github.com/Dasharo/dasharo-issues/issues/129).

Dasharo also works without blobs on platforms that allow that. For example,
ASUS KGPE-D16 can run without any blobs (officially there is no PSP on that
hardware, and Opteron 6200 series CPUs can run without microcode patches).
There is also a libre, POWER9-based server/workstation Talos II by Raptor
Computing Systems, which also do not use any binary blobs, however it is more
expensive than x86 platforms.

## Why Dasharo?

### Open-source firmware ecosystem problems

Every open-source project has its own internal dynamics, history and politics.
We are always looking for a solution that endorse non-aggression principle and
peaceful coexistence, which hopefully will allow everyone to compete based on
the same rules. We believe that market is big enough for all players and, if
not we should make market bigger, not fight for every possible piece causing
collateral damage.

Eventually, in the community, we are all human beings, including all our good
and bad features. In some cases, sympathy and antipathy cause unexpected
dynamics. This impacts every community.

We also should be aware that the open-source ecosystem is a place of
[OPSEC](https://en.wikipedia.org/wiki/Operations_security) and
[PSYWAR](https://en.wikipedia.org/wiki/Psychological_warfare) techniques use,
which leads to redirecting energy and resources into directions that make
open-source community activity less competitive.

In our opinion, massive energy is wasted in the open-source firmware community
because of incorrect focus, like religious flame wars about philosophical
principles, security paranoia without having an idea of threat modeling, or
revolutionary ideas and plans for how to overthrow multibillion-dollar industry
overlords. Although we may enjoy discussion during
[Dasharo open-source firmware vPubs][vpub] during everyday job would like to
focus on delivering value to those who can vote by choosing open-source
firmware/hardware/ISA based product to help change the computer industry.

Overall there is no economy around open-source firmware, and nobody seems to
care much about that. It impacts the upstreaming process, the number of
contributors, and reviewers. There are huge players with their own interests,
small open-source firmware vendors like 3mdeb and community members essentially
working for free. Without middle-size companies standing behind open-source
firmware-based products, not much will change. To fill the space between big
players and small boutique dev companies, we have to have products with the
volume on the market because the hardware market understands only sales
volumes, nothing else.

We want to work on changing the above paradigms or at least improve the
state-of-the-art relation in the community to the level where threats will have
a reasonably small impact. We believe that open-source firmware is a critical
tool, which should be used consciously to ensure privacy and liberty.

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

## Why Dasharo?

### Open-source firmware ecosystem problems

Every open-source project has its own internal dynamics, history and politics.
We are always looking for a solution that endorse non-aggression principle and
peaceful coexistence, which hopefully will allow everyone to compete based on
the same rules. We believe that market is big enough for all players and, if
not we should make market bigger, not fight for every possible piece causing
collateral damage.

Eventually, in the community, we are all human beings, including all our good
and bad features. In some cases, sympathy and antipathy cause unexpected
dynamics. This impacts every community.

We also should be aware that the open-source ecosystem is a place of
[OPSEC](https://en.wikipedia.org/wiki/Operations_security) and
[PSYWAR](https://en.wikipedia.org/wiki/Psychological_warfare) techniques use,
which leads to redirecting energy and resources into directions that make
open-source community activity less competitive.

In our opinion, massive energy is wasted in the open-source firmware community
because of incorrect focus, like religious flame wars about philosophical
principles, security paranoia without having an idea of threat modeling, or
revolutionary ideas and plans for how to overthrow multibillion-dollar industry
overlords. Although we may enjoy discussion during
[Dasharo open-source firmware vPubs][vpub] during everyday job would like to
focus on delivering value to those who can vote by choosing open-source
firmware/hardware/ISA based product to help change the computer industry.

Overall there is no economy around open-source firmware, and nobody seems to
care much about that. It impacts the upstreaming process, the number of
contributors, and reviewers. There are huge players with their own interests,
small open-source firmware vendors like 3mdeb and community members essentially
working for free. Without middle-size companies standing behind open-source
firmware-based products, not much will change. To fill the space between big
players and small boutique dev companies, we have to have products with the
volume on the market because the hardware market understands only sales
volumes, nothing else.

We want to work on changing the above paradigms or at least improve the
state-of-the-art relation in the community to the level where threats will have
a reasonably small impact. We believe that open-source firmware is a critical
tool, which should be used consciously to ensure privacy and liberty.
