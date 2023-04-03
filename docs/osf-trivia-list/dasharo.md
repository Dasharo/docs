# What is Dasharo?

Dasharo is registered trademark and product developed by [3mdeb](https://3mdeb.com).

Dasharo is an open-source firmware distribution focusing on
[carefully selected hardware platforms](#can-you-port-dasharo-to-my-mainboard),
[zero-touch initial deployment](#dasharo-zero-touch-initial-deployment),
[clean and simple code](#dasharo-clean-and-simple-code),
[long-term maintenance](#dasharo-long-term-maintenance),
[professional support](#dasharo-professional-support),
[transparent validation](#dasharo-transparent-validation),
[extensive and structured documentation](https://github.com/Dasharo/docs#navigation-menu),
[privacy-respecting implementation](#future-work),
[liberty for the owners](#future-work) and
[trustworthiness for all](#future-work).

Dasharo consists of [productized services](#dasharo-professional-support), set
of [open-source repositories](https://github.com/orgs/Dasharo/repositories),
and [quality control](#dasharo-transparent-validation) which help to provide
scalable, modular, easy to combine open-source BIOS, UEFI, and firmware
solutions. It offers the components that are needed to develop and maintain a
high quality, and modular firmware, for the stability and security of your
platform.

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

## What value Dasharo provides in comparison to coreboot?

* Dasharo is open-source firmware distribution based on
  [coreboot](https://coreboot.org) and other open-source firmware frameworks
  (e.g. [Tianocore EDKII](https://github.com/tianocore/edk2)), you can think
  about Dasharo and coreboot relation in the same way as you think about
  Debian/Ubuntu/RedHat and Linux. That means it can provide better
  cost-effectiveness, security, transparency and customizability than
  proprietary alternative.
* There are seven characterestics of Dasharo:
    - [carefully selected hardware platforms](#can-you-port-dasharo-to-my-mainboard),
    - [zero-touch initial deployment](#dasharo-zero-touch-initial-deployment),
    - [clean and simple code](#dasharo-clean-and-simple-code),
    - [long-term maintenance](#dasharo-long-term-maintenance),
    - [professional support](#dasharo-professional-support),
    - [transparent validation](#dasharo-transparent-validation),
    - [extensive and structured documentation](https://github.com/Dasharo/docs#navigation-menu),
    - [privacy-respecting implementation](#future-work),
    - [liberty for the owners](#future-work),
    - [trustworthiness for all](#future-work).

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
[documentation](../../dasharo-tools-suite/documentation/#dasharo-zero-touch-initial-deployment).

### Dasharo Clean and Simple Code

Dasharo is an open-source distribution project with a simple code structure
described in detail [here](../../../dev-proc/source-code-structure). While the
project benefits from the simplicity of the coreboot source code, it is
continuously researching and improving its development process and tools to
provide a superior experience for developers.  One example of this ongoing work
is the improvements made to fork maintenance, currently being tracked in [this
issue](https://github.com/Dasharo/dasharo-issues/issues/310) on the Dasharo
GitHub repository. The project also explores the concept of a bootstrapable
toolchain, discussed in the [build process
section](../../osf-trolling-list/build_process) of the project documentation. 

### Dasharo Long Term Maintenance

* We provide long term maintenance - coreboot community for various reasons, do
  not merge some patches, because of understaffing, lack of reviewers. Some
  changes have long way to upstream, we maintain those patches and make them
  work before those will go upstrea. If ever, we are committed to maintain
  platforms which are moved to branch in coreboot.
* Firmware update - we are registered [consultants for fwupd/LVFS][lvfs] and
  enable customers and community platforms, so they can get seamless firmware
  update in Linux.

### Dasharo Professional Support

Dasharo Support coming in form of three following packages:

* Dasharo Community Support (DCP) - donation driven development.
* Dasharo Support Package (DSP) - annual firmware support package.
* Dasharo Enterprise Package (DEP) - custom SLA, corporate and open roadmap
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

* We provide transparent validation results - coreboot in itself provide no
  guarantees around release quality and do not provide binary distribution (for
  reference please check [coreboot project scope][coreboot-scope], we provide
  those in scope of validation we perform.

### Dasharo Trustworthiness for All

* We provide ready to use binaries with GPG based signing scheme that improve
  verification where firmware coming from.

<!-- markdownlint-disable-next-line MD013 -->
## What are the differences between the official coreboot repository and the Dasharo repository?

Dasharo focuses on specific platforms listed in [supported
hardware](../variants/overview) section of Dasharo Universe documentation.

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

* **Privacy-respecting implementation**: By working on solutions that allow users
  to deactivate potentially malicious components, like ME or PSP, the firmware
  will respect user privacy and help mitigate data privacy concerns. This
  approach gives users more control over their devices and reduces the risk of
  unauthorized access or surveillance. Discussion and more detail in dedicated
  [issue](https://github.com/Dasharo/dasharo-issues/issues/392).
* **Liberty for the owners**: Respecting the liberty of hardware owners to repair
  and transfer ownership without risking the leak of personally identifiable
  data is crucial. This approach supports the right-to-repair movement and
  ensures that users maintain control over their personal information even when
  they modify or pass on their devices. Discussion and more detail in dedicated
  [issue](https://github.com/Dasharo/dasharo-issues/issues/393).
* **Trustworthiness for all**: By publishing known good measurements for each boot
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

* Dasharo supports mainboard X; I have mainboard Y (or X'). Can you teach me
  how to port Dasharo to my mainboard?
* Can you help me port Dasharo to my mainboard?

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
consider [ways to help us](../../ways-you-can-help-us/) to gain a reputation
that can lead to influencing Dasharo Community Supported roadmap.
