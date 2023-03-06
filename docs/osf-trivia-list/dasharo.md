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

## What is open-source firmware distribution?

Dasharo is 3mdeb's firmware distribution and all its components are
open-source. We provide releases in binary form. As you know in most cases on
x86 for firmware to be useful it has to cooperate with closed blobs. In all
binary releases we are making sure we provide information where all components
are coming from.

Dasharo works without blobs on platforms that allow that. When we saying
Dasharo open-source firmware distribution we mean code that is delivered by
3mdeb that is open-source. We have no influence on the code provided by 3rd
parties (e.g. FSP, ME, GbE etc.).

In coreboot community there was some controversy about calling Dasharo
open-source firmware distribution (for details please check [gerrit review][gerrit-review].
We respect coreboot community opinion, so we agreed that in case of coreboot
documentation it would be better to use open-source based firmware
distribution. It doesn't mean we agree with that decision:

* Definitions and rules used in coreboot documentation review
* Rules seem not to be applied equally to all contributors of
  [coreboot distribution][cb-distro]

## Why Dasharo is not called coreboot firmware distribution?

Dasharo is not coreboot firmware distribution because we also may imagine
Dasharo pure EDKII, oreboot or based on any other open-source firmware
framework. Dasharo typically is based on coreboot and EDKII, plain coreboot is
not enough in most cases for booting modern computer.

## What value Dasharo provide in comparison to coreboot?

* Dasharo is open-source firmware distribution based on
  [coreboot](https://coreboot.org) and other open-source firmware frameworks
  (e.g. [Tianocore EDKII](https://github.com/tianocore/edk2)), you can think
  about Dasharo and coreboot relation in the same way as you think about
  Debian/Ubuntu/RedHat and Linux. That means it can provide better
  cost-effectiveness, security, transparency and customizability than
  proprietary alternative.
* There are seven characterestics of Dasharo:
    - [zero-touch initial deployment](#dasharo-zero-touch-initial-deployment),
    - [clean and simple code](#dasharo-clean-and-simple-code),
    - [long-term maintenance](#dasharo-long-term-maintenance),
    - [professional support](#dasharo-support-package),
    - [transparent validation](#dasharo-transparent-validation),
    - [privacy-respecting implementation](#dashro-privacy-respecting-implementation),
    - [liberty for the owners](#dasharo-liberty-for-the-owners),
    - [trustworthiness for all](#dasharo-trustworthiness-for-all).

### Dasharo Zero-Touch Initial Deployment

Documentation supported hardware provide information about initial deployment,
updates and recovery procedures. Developed by Dasharo Team [Dasharo Tools Suite
(DTS)][dtsos] operating system support users by automating the deployment
process, which help reducing errors and inconsistencies, and make sure the
firmware can be further updated to new version without any problems. DTS also
provide controlled and secure environment for initial deployment and update of
firmware, reducing the risk of tampering or unauthorized changes.

Dasharo Zero-Touch Initial Deployment is smooth, effortless and user-friendly
process, which reduce user frustration and improve satisfaction.

Use of DTS largely improve firmware adoption, hardware compatibility reporting
and binary blobs transmission, as well as recovery.

For more details about zero-touch initial deployment please read relevant
Dasharo Tools Suite
[documentation](../../dasharo-tools-suite/documentation/#dasharo-zero-touch-initial-deployment).

### Dasharo Clean and Simple Code

* Each supported platform has its own branches in Dasharo's coreboot repository:
    - `<board_name>/develop`, e.g. `msi_ms7d25/develop`, used for bug fixes and
    development of new features.
    - `<board_name>/release`, e.g. `msi_ms7d25/release`, contains only the
    released and validated code. It is used to build the firmware binaries
    distributed to the community through Dasharo releases.
* Each supported platform has a build scripts included in Dasharo's coreboot
  repository to simplify the complex build instructions

### Dasharo Long Term Maintenance

* We provide long term maintenance - coreboot community for various reasons, do
  not merge some patches, because of understaffing, lack of reviewers. Some
  changes have long way to upstream, we maintain those patches and make them
  work before those will go upstrea. If ever, we are committed to maintain
  platforms which are moved to branch in coreboot.
* Firmware update - we are registered [consultants for fwupd/LVFS][lvfs] and
  enable customers and community platforms, so they can get seamless firmware
  update in Linux.

### Dasharo Support Package

* Support - Dasharo Team is paid to provide support in the community through
  [Dasharo Matrix Space][dasharo-matrix], of course we want to introduce some
  commercial products related to the support to make the business feasible, but
  some level of support always would be available to the community.

### Dasharo Transparent Validation

* We provide transparent validation results - coreboot in itself provide no
  guarantees around release quality and do not provide binary distribution (for
  reference please check [coreboot project scope][coreboot-scope], we provide
  those in scope of validation we perform.

### Dasharo Trustworthiness for All

* We provide ready to use binaries with GPG based signing scheme that improve
  verification where firmware coming from.
