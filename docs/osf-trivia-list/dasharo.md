## What is Dasharo?

Dasharo registered trademark and product developed by
[3mdeb](https://3mdeb.com).

From our experience to be considered as serious player on firmware market there
is need for recognized brand with proved history of successful integrations. We
were asked about that multiple times, by various parties over years of
providing services related to open-source firmware. Finally we decided we have
to make a move and create marketing vehicle under which we can deliver added
value like transparent validation, long-term maintenance, bleeding edge
integration for modern hardware and other products requested by community and
customers.

We also plan to provide camp for all coreboot refugees e.g. platforms moved to
branch because of need for code evolution. For more information please read
about [Intel Quark SoC deprecation][intel-quark], [LEGACY_SMP_INIT &
RESOURCE_ALLOCATOR_V3][legacy-smp]. More elaborate explanation of our position
you can find
[below](#why-dasharo-team-is-against-moving-code-to-branches-in-coreboot).

Dasharo typically may get support for fully open platforms like [Raptor
Computing Systems Talos II][raptor] family, [ASUS KGPE-D16][kgpe-d16] and other
(not so open), but also very new stuff like [MSI Z690A DDR4][msi-z690a].


## What Dasharo provides?

For every supported hardware Dasharo Team provides:

* [Source code](https://github.com/dasharo)
* Test results in 
* [GPG keys](https://github.com/3mdeb/3mdeb-secpack/tree/master/dasharo)
* Signed binaries in release section
* 


## What is Dasharo binary blob policy?

## Why Dasharo?

### Open-source firmware ecosystem problems

Every open-source project has its own internal dynamics, history and politics.
We always looking for solution which endorse non-aggression principle and
peaceful coexistence which hopefully will allow everyone compete based on the
same rules. We believe that market is big enough for all players and, if not we
should make market bigger not fight for every possible piece causing collateral
damage.

Eventually in community we are all human beings including all our good and bad
features. In some cases sympathy and antipathy cause unexpected dynamics. This
impact every community.

We also should be aware that open-source ecosystem is place of use of
[OPSEC](https://en.wikipedia.org/wiki/Operations_security) and
[PSYWAR](https://en.wikipedia.org/wiki/Psychological_warfare) techniques, which
leads to redirecting energy and resources into directions that make open-source
community activity less competitive.

In our opinion massive energy is wasted in open-source firmware community
because of incorrect focus like religious flame wars about philosophical
principles, security paranoia without having idea of threat modelling, or
revolutionary ideas and plans how to overthrow multibillion dollar industry
overlords. Although we may enjoy discussion during [Dasharo open-source
firmware vPubs][vpub] during everyday job would like to focus on delivering
value to those who can vote by choosing open-source firmware/hardware/ISA based
product to help change computer industry.

Overall there is no economy around open-source firmware and nobody seem to care
much about that. It impact upstreaming process, number of contributors and
reviewers. There are huge players with their own interest, small open-source
firmware vendors like 3mdeb, and community members essentially working for
free. Without middle size companies standing behind open-source firmware based
products not much will change. To fill space between big players and small
butique dev companies we have to have products with volume on market, because
hardware market understand only sales volumes nothing else.

We want to work on changing above paradigms or at least improve state of the
art relation in community to the level above on which threats will have
reasonably small impact. We believe that open-source firmware is critical tool,
which should be used consciously to ensure privacy and liberty.

## What is open-source firmware distribution?

Dasharo is 3mdeb firmware distribution and all its components are open-source.
We provide releases in binary form. As you know in most cases on x86 for
firmware do be useful it has to cooperate with closed blobs. In all binary
releases we made we provide information where all components coming from.

Dasharo works without blobs on platforms that allow that. When we saying
Dasharo open-source firmware distribution we mean code that is delivered by
3mdeb that is open-source e, we have no influence on code of 3rd parties (e.g.
FSP, ME, GbE etc.).

In coreboot community there was some controversy about calling Dasharo
open-source firmware distribution (for details please check [gerrit review][gerrit-review].
We respect coreboot community opinion, so we agreed that in case of coreboot
documentation it would be better to use open-source based firmware
distribution. It doesn't mean we agree with that decision:
- Definitions and rules used in coreboot documentation review
- Rules seem to no be applied equally to all contributors of [coreboot
distribution][cb-distro]
- 



## Why Dasharo is not called coreboot firmware distribution?

Dasharo is not coreboot firmware distribution because we also may imagine
Dasharo pure EDKII, oreboot or based on any other open-source firmware
framework. Dasharo typically is based on coreboot and EDKII, plain coreboot is
not enough in most cases for booting modern computer.

## What value Dasharo provide in comparison to coreboot?

- Dasharo is open-source firmware distribution based on coreboot and other
open-source firmware frameworks, you can think about Dasharo and coreboot
relation in the same way as you think about Debian/Ubuntu/RedHat and Linux.
- We provide long term maintenance - coreboot community for various reasons, do
not merge some patches, because understaffing, lack of reviewer some changes
have long way to upstream, we maintain those patches and make them work
before those will go upstream, if ever, we are committed to maintain platforms
which are moved to branch in coreboot.
- We provide transparent validation results - coreboot in itself provide no
guarantees around release quality and do not provide binary distribution (for
reference please check [coreboot project scope][coreboot-scope], we provide
those in scope of validation we perform.
- We provide seamless deployment - our documentation provide information about
initial deployment, updates and recovery procedures. We working on commercial
product called [Dasharo Tools Suite OS][dtsos], which will largely improve firmware
deployment, hardware compatibility reporting and  binary blobs transmission
wherever it is necessary, as well as recovery.
- Firmware update - we are registered [consultants for fwupd/LVFS][lvfs] and enable
customers and community platforms, so they can get seamless firmware update in
Linux.
- Support  - Dasharo team is paid to provide support in community through
[Dasharo Matrix Space][dasharo-matrix], of course we want to introduce some
commercial products related to support to make business feasible, but some
level of support always would be available to community.
- We provide ready to use binaries with GPG based signing scheme that improve
verification where firmware coming from.

<!--
## Why Dasharo Team is against moving code to branches in coreboot?
-->

## Why there is no AMD mainboard supported in Dasharo ?

Unfortunately, from the perspective of a small open-source firmware vendor, it
isn't easy to work with AMD. Despite our experience with AMD SoCs since 2016,
we could not yet deliver Dasharo for a modern (Zen core-based) platform. We're
trying hard, but Intel has a better ecosystem for open-source firmware
development.

The reason for that state may be because AMD is in a rush, and they are
understaffed in all areas compared to their success. We've been doing AMD
open-source firmware development for 6+ years, including our yearly reports of
open-source firmware status at FOSDEM, but the level of support for small
volume firmware development companies is not yet at the level of competition.

AGESA distribution was a problem in the past, but we solved that, and Dasharo
for AMD is possible. Because Dynamic Root of Trust can work without blob, we
favor AMD, but we can't do anything without a partner who can sponsor the
development effort. We are on the market of open-source firmware vendors, not
hardware vendors.

[coreboot-scope]: https://doc.coreboot.org/#scope-of-the-coreboot-project
[dtsos]: https://github.com/Dasharo/dasharo-issues/issues?q=is%3Aissue+is%3Aopen+label%3ADasharoToolsSuite
[lvfs]: https://fwupd.org/lvfs/docs/consulting
[gerrit-review]: https://review.coreboot.org/c/homepage/+/63402
[cb-distro]: https://doc.coreboot.org/distributions.html
[intel-quark]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/YRJQIPVK5WHACT64TH42CLGD4TXG3XTS/#PZUIFZZHRK7M3NLBNLI6VUBD4O52245B
[legacy-smp]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/EEEBFATYHWIPRDXLCUEFNDZ4FYYVA4QM/#QHIYXYTVOGXENJXUOWOXUZOTLV5OS4LB
[raptor]: ../../variants/talos_2/releases/
[kgpe-d16]: ../../variants/asus_kgpe_d16/releases
[msi-z690a]: ../../variants/msi_z690/overview/
[vpub]: https://vpub.dasharo.com/
