# Frequenty Asked Questions about Dasharo

## What is Dasharo?

Dasharo is registered trademark and product developed by [3mdeb](https://3mdeb.com).

Dasharo is an open-source firmware distribution focusing on:

- [carefully selected hardware platforms](#can-you-port-dasharo-to-my-mainboard),
- [zero-touch initial deployment](#dasharo-zero-touch-initial-deployment),
- [clean and simple code](#dasharo-clean-and-simple-code),
- [long-term maintenance](#dasharo-long-term-maintenance),
- [professional support](#dasharo-professional-support),
- [transparent validation](#dasharo-transparent-validation),
- [extensive and structured documentation](https://github.com/Dasharo/docs#navigation-menu),
- [privacy-respecting implementation](#future-work),
- [liberty for the owners](#future-work) and
- [trustworthiness for all](#future-work).

Dasharo consists of [productized services](#dasharo-professional-support), set
of [open-source repositories](https://github.com/orgs/Dasharo/repositories),
and [quality control](https://docs.dasharo.com/unified-test-documentation/overview/)
which help to provide scalable, modular, easy to combine open-source BIOS, UEFI,
and firmware solutions. It offers the components that are needed to develop
and maintain a high quality, and modular firmware, for the stability and
security of your platform.

For individuals Dasharo provides optional features in subscription model called
[Dasharo Pro Package](../dev-proc/versioning.md#dasharo-entry-subscription-releases).

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
check [description](https://docs.dasharo.com/dev-proc/versioning).
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

## What is open-source firmware distribution?

Dasharo is 3mdeb's firmware distribution and all its components are
open-source. We provide releases in binary form. As you know in most cases on
x86 for firmware to be useful it has to cooperate with closed blobs. In all
binary releases we are making sure we provide information where all components
are coming from.

Dasharo works without blobs on platforms that allow that. When we are saying
Dasharo open-source firmware distribution we mean code that is delivered by
3mdeb that is open-source. We have no influence on the code provided by 3rd
parties (e.g. FSP, ME, GbE etc.).

In coreboot community there was some controversy about calling Dasharo
open-source firmware distribution (for details please check [gerrit
review][gerrit-review]). We respect coreboot community opinion, so we agreed
that in case of coreboot documentation it would be better to use open-source
based firmware distribution. It doesn't mean we agree with that decision:

- Definitions and rules used in coreboot documentation review are not clear.
- Rules seem not to be applied equally to all contributors of
  [coreboot distribution][cb-distro].

## Why Dasharo is not called coreboot firmware distribution?

While the coreboot is now the default open-source framework for Dasharo, we do
not want to limit Dasharo to one framework. We also expect another firmware
frameworks to be a base for Dasharo, such as
[U-Boot](https://u-boot.readthedocs.io/en/latest/),
[oreboot](https://github.com/oreboot/oreboot),
[Slim Bootloader](https://slimbootloader.github.io/), or pure
[EDK II](https://github.com/tianocore/edk2).

Moreover, coreboot is not enough in most cases for booting modern computer.
Most Dasharo flavors are currently based on coreboot with EDK II payload, but
we also have [coreboot with
skiboot/heads](https://docs.dasharo.com/variants/talos_2/releases/) payload,
and we expect more flavors to appear in the future.

## What value Dasharo provides in comparison to coreboot?

- Dasharo is open-source firmware distribution based on
  [coreboot](https://coreboot.org) and other open-source firmware frameworks
  (e.g. [Tianocore EDKII](https://github.com/tianocore/edk2)), you can think
  about Dasharo and coreboot relation in the same way as you think about
  Debian/Ubuntu/RedHat and Linux. That means it can provide better
  cost-effectiveness, security, transparency and customizability than
  proprietary alternative.
- There are seven characterestics of Dasharo:
    + [carefully selected hardware platforms](#can-you-port-dasharo-to-my-mainboard),
    + [zero-touch initial deployment](#dasharo-zero-touch-initial-deployment),
    + [clean and simple code](#dasharo-clean-and-simple-code),
    + [long-term maintenance](#dasharo-long-term-maintenance),
    + [professional support](#dasharo-professional-support),
    + [transparent validation](#dasharo-transparent-validation),
    + [extensive and structured documentation](https://github.com/Dasharo/docs#navigation-menu),
    + [privacy-respecting implementation](#future-work),
    + [liberty for the owners](#future-work),
    + [trustworthiness for all](#future-work).

### Dasharo Zero-Touch Initial Deployment

Documentation supported hardware provides information about initial deployment,
updates and recovery procedures. Developed by Dasharo Team [Dasharo Tools Suite
(DTS)][dtsos] operating system supports users by automating the deployment
process, which helps reducing errors and inconsistencies, and make sure the
firmware can be further updated to new version without any problems. DTS also
provides controlled and secure environment for initial deployment and update of
firmware, reducing the risk of tampering or unauthorized changes.

Dasharo Zero-Touch Initial Deployment is smooth, effortless and user-friendly
process, which reduces user frustration and improves satisfaction.

Use of DTS largely improves firmware adoption, hardware compatibility reporting
and binary blobs transmission, as well as recovery.

For more details about zero-touch initial deployment please read relevant
DTS
[documentation](https://docs.dasharo.com/dasharo-tools-suite/documentation/#dasharo-zero-touch-initial-deployment).

### Dasharo Clean and Simple Code

Dasharo is an open-source distribution project with a simple code structure
described in detail
[here](https://docs.dasharo.com/dev-proc/source-code-structure). While the
project benefits from the simplicity of the coreboot source code, it is
continuously researching and improving its development process and tools to
provide a superior experience for developers.  One example of this ongoing work
is the improvements made to fork maintenance, currently being tracked in [this
issue](https://github.com/Dasharo/dasharo-issues/issues/310) on the Dasharo
GitHub repository. The project also explores the concept of a bootstrapable
toolchain, discussed in the [build process
section](https://docs.dasharo.com/osf-trolling-list/build_process)
of the project documentation.

### Dasharo Long Term Maintenance

- We provide long term maintenance - coreboot community for various reasons, do
  not merge some patches, because of understaffing, lack of reviewers. Some
  changes have long way to upstream, we maintain those patches and make them
  work before those will go upstrea. If ever, we are committed to maintain
  platforms which are moved to branch in coreboot.
- Firmware update - we are registered [consultants for fwupd/LVFS][lvfs] and
  enable customers and community platforms, so they can get seamless firmware
  update in Linux.

### Dasharo Professional Support

Dasharo Support coming in form of three following packages:

- Dasharo Community Support (DCP) - donation driven development.
- Dasharo Support Package (DSP) - annual firmware support package.
- Dasharo Enterprise Package (DEP) - custom SLA, corporate and open roadmap
  alignment advisroy.

The Dasharo Community Support Program is an open-source firmware support
initiative that leverages the expertise of community members and developers to
improve firmware solutions for a range of hardware models.

Platforms in scope of the program should comply with Dasharo quality criteria,
which we slowly gather in [Dasharo Certification
Program](#what-is-dasharo-certification-program).

3mdeb supports and maintains DCP-approved firmware through Dasharo Support
Package (DSP) and Dasharo Enterprise Package (DEP). These packages offer
essential services like porting to new platforms, developing device drivers,
debugging, and fixing bugs. Companies can rely on 3mdeb's expertise to ensure
their systems remain secure, up-to-date, and reliable.

If you are interested in our services please contact us
[here](https://3mdeb.com/contact/).

### Dasharo Transparent Validation

- We provide transparent validation results - coreboot in itself provide no
  guarantees around release quality and do not provide binary distribution (for
  reference please check [coreboot project scope][coreboot-scope], we provide
  those in scope of validation we perform.

### Dasharo Trustworthiness for All

- We provide ready to use binaries with GPG based signing scheme that improve
  verification where firmware coming from.

<!-- markdownlint-disable-next-line MD013 -->
## What are the differences between the official coreboot repository and the Dasharo repository?

Dasharo focuses on specific platforms listed in [supported
hardware](../variants/overview.md) section of Dasharo Universe documentation.

Dasharo repository contains release tags which are associated with Dasharo
Certification Program providing certain quality criteria including test
results. We always trying to minimize delta, but sometimes it can be up to 5k
SLOC (or more I guess e.g. Talos II coreboot support).

## What is Dasharo Certification Program?

The Dasharo Certification Program (DCP) is a highly specialized certification
program that benchmarks open-source firmware ecosystem deliverables. The
program ensures that firmware is stable, secure, and dependable while aligning
with the Dasharo values. DCP encourages developers to create their version of
Dasharo or contribute to the Dasharo project or coreboot upstream, enabling
them to leverage the power of open-source development to create custom firmware
tailored to their specific needs based on years of Dasharo quality assurance
results. The program's rigorous certification process entails comprehensive
testing in the Dasharo Certification Lab, ensuring that the firmware binary
meets the strict standards established by the program. By aligning with the
Dasharo values, the certification program improves the overall posture of the
open-source firmware ecosystem, making it long-term maintainable, sustainable,
and trustworthy and providing specific service level agreements and warranties
to commercial customers and the community.

## What is DCP-approved firmware?

The Dasharo-certified firmware provides long-term maintenance over ten years
after the CPU microarchitecture release, which means that OEM, ODM, hardware
vendors, and other companies can rely on the firmware for a long time without
worrying about end-of-life issues. Moreover, DCP-approved firmware vendors must
provide professional support channels to ensure that other business entities
can rely on those channels for long-term support regarding firmware and
software.

The validation process for DCP firmware is transparent. Test results and bug
reports are always publicly available, allowing the community to continually
identify issues and improve the firmware. However, in case of a security
embargo, the results can be kept under a strict but well-defined policy,
ensuring the security of the firmware.

### Future work

These future goals align with the values of privacy, liberty, and
trustworthiness in the context of firmware development and the broader tech
industry. We would like to implement following features as part of Dasharo
Certification Program:

- **Privacy-respecting implementation**: By working on solutions that allow users
  to deactivate potentially malicious components, like ME or PSP, the firmware
  will respect user privacy and help mitigate data privacy concerns. This
  approach gives users more control over their devices and reduces the risk of
  unauthorized access or surveillance. Discussion and more detail in dedicated
  [issue](https://github.com/Dasharo/dasharo-issues/issues/392).
- **Liberty for the owners**: Respecting the liberty of hardware owners to repair
  and transfer ownership without risking the leak of personally identifiable
  data is crucial. This approach supports the right-to-repair movement and
  ensures that users maintain control over their personal information even when
  they modify or pass on their devices. Discussion and more detail in dedicated
  [issue](https://github.com/Dasharo/dasharo-issues/issues/393).
- **Trustworthiness for all**: By publishing known good measurements for each boot
  phase and storing those measurements in tamper-resistant mediums, such as
  TPM, during the boot process will increase security and confidence in the
  firmware. Users and other stakeholders can verify that the firmware executed
  during the boot process is genuine and uncompromised by making reference
  measurements publicly available. Discussion and more detail in dedicated
  [issue](https://github.com/Dasharo/dasharo-issues/issues/394).

<!--
## What is Dasharo Community Support?

## What is Dasharo Support Package?

## What is Dasharo Enterprise Support?

## Why Dasharo Team is against moving code to branches in coreboot?

## What is the difference between open-source firmware development in free time
and open-source firmware development as a business?

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

## Can you port Dasharo to my mainboard?

There are other versions of the same questions:

- Dasharo supports mainboard X; I have mainboard Y (or X'). Can you teach me
  how to port Dasharo to my mainboard?
- Can you help me port Dasharo to my mainboard?

**TL;DR: No, we can't. In Dasharo, we support only carefully selected targets.**

The answer to that question requires understanding many aspects of the
open-source firmware business we learned over the years. The critical point is
that we can't help to port arbitrary targets. Hardware has to be carefully
selected to bring the most benefits to the open-source firmware community and
improve the sustainability of the ecosystem. Random hardware porting lead to an
unmaintainable stack of platforms that no one adapts in scale, which does not
lead to market change in the correct direction. Lack of commercial adoption is
part of coreboot problems as a project, and we would like to avoid this
mistake.

We have strict criteria based on various aspects explained in Dasharo Community
Support section.

Dasharo Team tries to select platforms with long-term availability potential.

Because we are fully responsible for hardware that we enable in open-source
firmware ecosystem, our releases have to pass the Dasharo Certification
criteria.  The whole effort is relatively expensive and, in most cases, not
feasible for enabling one platform. That's why in most cases, our customers are
OEM/ODM, angel investors, or communities that need reasonable quantities of
hardware (>200pcs).

If the board comes with variants with minimal differences required for support
in an open-source firmware stack, and one of the variants is part of the
Dasharo Support Package, Dasharo Enterprise Package, or Dasharo Community
Support, there is a chance to put that hardware on the relevant roadmap. In
such a case, don't hesitate to contact us; we will see what we can do. However,
the community member who requested support for the platform should also offer
their help in validating the firmware and maintenance. That kind of request
will be more than welcome from active community members. New members should
consider [ways to help us](https://docs.dasharo.com/ways-you-can-help-us/)
to gain a reputation that can lead to influencing Dasharo Community Supported
roadmap.

[coreboot-scope]: https://doc.coreboot.org/#scope-of-the-coreboot-project
[dtsos]: ../dasharo-tools-suite/overview.md
[lvfs]: https://fwupd.org/lvfs/docs/consulting
[gerrit-review]: https://review.coreboot.org/c/homepage/+/63402
[cb-distro]: https://doc.coreboot.org/distributions.html
[intel-quark]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/YRJQIPVK5WHACT64TH42CLGD4TXG3XTS/#PZUIFZZHRK7M3NLBNLI6VUBD4O52245B
[legacy-smp]: https://mail.coreboot.org/hyperkitty/list/coreboot@coreboot.org/thread/EEEBFATYHWIPRDXLCUEFNDZ4FYYVA4QM/#QHIYXYTVOGXENJXUOWOXUZOTLV5OS4LB
[raptor]: ../variants/talos_2/releases.md
[kgpe-d16]: ../variants/asus_kgpe_d16/releases.md
[msi-z690a]: ../unified/msi/overview.md
[vpub]: https://vpub.dasharo.com/
[dasharo-matrix]: https://matrix.to/#/#dasharo:matrix.org
