---
template: giscus.html
---

# Trenchboot as Anti Evil Maid

## Abstract

As Qubes OS users, promoters, and developers, we understand how essential it is
to be aware of the latest developments in maintaining the security of your
favorite operating system. We're excited to share our plans to integrate the
TrenchBoot Project into Qubes OS's new Anti-Evil Maid (AEM) implementation. As
you may know, traditional firmware security measures like UEFI Secure Boot and
measured boot, even with a Static Root of Trust (SRT), may only sometimes be
enough to ensure a completely secure environment for your operating system.
Compromised firmware may allow for the injection of malicious software into
your system, making it difficult to detect. To overcome these limitations, many
silicon vendors have started implementing Dynamic Root of Trust (DRT)
technologies to establish a secure environment for operating system launch and
integrity measurements. We're excited to take advantage of these advancements
through integration with the [TrenchBoot Project][tb_org].

The usage of DRT technologies like Intel Trusted Execution Technology (TXT) or
AMD Secure Startup becomes more and more significant, for example, Dynamic Root
of Trust for Measurement (DRTM) requirements of [Microsoft Secured Core
PCs][ms_sec_core].  In open-source projects, DRTM hasn't found its place yet,
but that gradually changes. The demand on having firmware independent Roots of
Trust is increasing and projects that satisfy this demand are growing, for
instance, [TrenchBoot][tb_org].  TrenchBoot is a framework that allows
individuals and projects to build security engines to perform launch integrity
actions for their systems. The framework builds upon Boot Integrity
Technologies (BITs) that establish one or more Roots of Trust (RoT) from which
a degree of confidence that integrity actions were not subverted. The project
has grown a lot thanks to the previous [NLnet NGI0 PET grant][nlnet_open_drtm]
and now it looks for further expansion into extensive use of the DRT
technologies in open-source and security-oriented operating systems like
[Qubes OS][qubes_os_rg]. [Qubes OS Anti Evil Maid (AEM)][it_aem] software
heavily depends on the availability of the DRTM technologies to prevent the
[Evil Maid attacks][em_attacks].  However, the project hasn't evolved much
since the beginning of 2018 and froze on the support of TPM 1.2 with Intel TXT
in legacy boot mode (BIOS). This effectively limits the usage of this security
software to older Intel machines only. TPM 1.2 implemented SHA1 hashing
algorithm which is nowadays considered weak in the era of forever-increasing
computer performance and quantum computing. The solution to this problem comes
with a newer TPM 2.0 with more agile cryptographic algorithms and SHA256
implementation by default.  Qubes OS AEM software suffers from the following:

1. Lack of TPM 2.0 support to handle more secure hashes and safer design of the
   TPM firmware according to a newer specification.
2. Qubes OS AEM has never supported any AMD processors with AMD Secure Startup
   technology. Implementing AMD support would make a huge impact and broaden
   the usage of DRTM technologies.

The initial AEM implementation relied on the [Trusted Boot project][tboot_wiki],
Intel's reference implementation of Intel TXT. It had never any plans to
support AMD processors. TrenchBoot is filling this gap supporting both Intel
and AMD hardware which makes it an ideal target to replace Trusted Boot in
Qubes OS AEM implementation. Furthermore, the project grant would be used to
implement the missing pieces in the Qubes OS AEM software to cover the AMD and
Intel support for both TPM 1.2 and TPM 2.0.

[ms_sec_core]: https://trenchboot.org/
[tb_org]: https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure#what-makes-a-secured-core-pc
[nlnet_open_drtm]: https://nlnet.nl/project/OpenDRTM/
[qubes_os_org]: https://www.qubes-os.org/
[it_aem]: https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html
[em_attacks]: http://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html
[tboot_wiki]: https://sourceforge.net/p/tboot/wiki/Home/

## Compare your own project with existing or historical efforts

3mdeb is a licensed provider for quality coreboot consulting services for 7
years. We are well-known in the open-source community for maintaining firmware
of the PC Engines APU series platform for over 7-years. Delivering high-quality
firmware releases each month and providing technical support on PC Engines and
OPNSense forums. 3mdeb embedded systems developers are experienced engineers
accustomed to operating systems development. Our developers have contributed to
the [fwupd support for Qubes OS][qubes_fwupd]. 3mdeb is also regularly
co-organizing mini-conference events with Qubes OS maintainer Marek
Marczykowski-Górecki where various topics related to Qubes OS security are
discussed. Among them, the Anti Evil Maid was frequently presented by 3mdeb
engineers:

- [Anti Evil Maid for Intel coreboot-based platform][aem_intel]
- [Anti Evil Maid for modern AMD UEFI-based platform][aem_amd]

3mdeb, with financial support from Qubes OS, developed a proof of concept
replacing Trusted Boot with TrenchBoot on Intel hardware with TPM 1.2. Qubes OS
and 3mdeb already tested a new solution with Qubes OS Anti Evil Maid, which is
available for community use. The result of this solution can be seen in the
published blog post that concludes the first phase of integrating TrenchBoot
Anti Evil Maid for Qubes OS. The numbering of the next phases of the project
will commence with number 2 in order to maintain consistency with the work
already completed in [phase 1][phase1_blog_post]. The following application
describes the remaining work required to have production quality adoption in
one of the most popular secure operating system on the market.

[qubes_fwupd]: https://blog.3mdeb.com/2020/2020-07-14-qubesos-fwupd-core/
[aem_intel]: https://www.youtube.com/watch?v=YE2FbFlszI4
[aem_amd]: https://www.youtube.com/watch?v=rM0vRi6qABE
[phase1_blog_post]: TBD blog post

## What are the significant technical challenges you expect to solve

First of all Qubes OS AEM software consists of software packages providing
Trusted Boot and the [Qubes OS TPM scripts][aem_scripts]. These software
packages would need to replace the Trusted Boot with TrenchBoot supported GRUB2
and Xen.

Secondly, the TPM scripts require adding support for TPM 2.0 equivalent
functionality. AEM requires access to non-volatile RAM inside TPM which is
defined differently in the TPM 2.0 specification compared to TPM 1.2.

Another challenge would be to update the TrenchBoot components for AMD
platforms to the recent boot protocol, which will allow AMD platforms to take
advantage of the QubesOS AEM feature, and TrenchBoot.

[aem_scripts]: https://github.com/QubesOS/qubes-antievilmaid/blob/master/sbin/

## Requested support

1. Phase 2 - TPM 2.0 support in Qubes OS AEM (Intel hardware):

    + Implement support for TPM 2.0 module in Xen

        Required to measure Dom0 kernel and initial ram disk before they are
        executed.

    + Implement support for TPM 2.0 event log in Xen

        Required to log the Dom0 kernel and initial ram disk hashes to the TPM
        event log. The event log could be used for future system attestation.

    + Implement parallel CPU cores bring-up for DRTM launch

        Currently the CPU cores are being woken up in parallel, but later they
        are hacked to be waiting in a queue. If any interrupt would come at
        that time, it could be a serious danger. It has to be fixed as soon as
        possible, as required by Intel TXT specification.

    + Integrate TPM 2.0 software stack into Qubes OS Dom0

    + Extend the AEM scripts to detect TPM version on the platform

        While AEM fully supports TPM 1.2 there is no support for TPM 2.0 at
        all. When the TPM family is determined the script should use the
        appropriate software stack for given TPM. The task implements the AEM
        TPM 1.2 equivalent functionalities using TPM 2.0 software stack and as
        a result allowing the use of TPM 2.0 with Qubes OS AEM. It will require
        implementing the access to TPM 2.0 NVRAM, sealing and unsealing the
        secret data and generating TOTP.

    + Extend the AEM scripts to use appropriate software stack for TPM 2.0

        Currently, only TPM 1.2 is supported in Qubes OS AEM service code. The
        3 items above will ensure the necessary software for TPM 2.0 is
        available and AEM scripts executed early from the initrd can detect
        which TPM family is present on the platform and use appropriate
        software stack and functions. TPM 1.2 and TPM 2.0 software stacks are
        not compatible so the scripts themselves must use proper API for given
        TPM and its respective software stack.

    + Update Qubes OS AEM documentation

    + Test the solution on Intel hardware with TPM 1.2 and 2.0 using legacy
      boot mode

2. Phase 3 - Update to the newest TrenchBoot boot protocol:

    + Code rebase onto the most recent work implementing Secure Launch protocol
      being upstreamed to Linux and GRUB

        The current state of TrenchBoot support has diverged with what was
        developed for QubesOS AEM for Intel hardware with TPM 1.2. The task
        aims to update the work and align with the TrenchBoot boot protocol
        being upstreamed to GRUB and Linux kernel. Xen shall take similar
        approach as Linux kernel in terms of DRTM launch.

    + Test the solution on Intel hardware with TPM 1.2 and TPM 2.0 using
      legacy boot mode

3. Phase 4 - AMD support for Qubes OS AEM with TrenchBoot:

    + Update the Secure Kernel Loader (formerly LandingZone) package support
      for QubesOS

        Since the initial work done by 3mdeb engineers for AMD AEM in Qubes OS
        a lot of time has passed and Secure Kernel Loader - SKL (formerly
        Landing Zone) has improved a lot and added new features. SKL is an
        open-source module written by TrenchBoot developers required by AMD
        Secure Startup technology to perform DRTM launch. The task aims to
        refresh the previous work and update the SKL package for Qubes OS to
        the newest revision.

    + TrenchBoot Secure Kernel Loader (SKL) improvements for AMD server
      CPUs with multiple nodes

        While SKL was extensively tested on System on Chip and single CPU
        platforms, it was not much tested on workstation/server segment CPUs
        which are more complex. For example one server CPU package may contain
        two independent CPUs inside called nodes. Each node will enable
        protection on the SKL during DRTM execution. This protection has to be
        disabled on each node when TrenchBoot DRTM tasks are done. The task
        implements the correct support for server CPUs in TrenchBoot SKL.

    + Update TrenchBoot boot protocol for AMD in GRUB2

        Some work to implement TrenchBoot support for Qubes OS on AMD hardware
        has been done. GRUB2 with TrenchBoot support has been added to Qubes
        building system on [3mdeb fork][qubes_grub2_fork]. The task aims to
        update the work and align with the TrenchBoot boot protocol being
        upstreamed to GRUB2 and Linux kernel.

    + Update TrenchBoot boot protocol for AMD in Secure Kernel Loader

        The task aims to update the TrenchBoot boot protocol for AMD platforms
        in Secure Kernel Loader and align with the TrenchBoot boot protocol
        being upstreamed to GRUB2 and Linux kernel.

    + Test the solution on AMD hardware with TPM 2.0 and TPM 1.2 with legacy
      boot mode

[qubes_grub2_fork]: https://github.com/Tren/qubes-grub2/tree/trenchboot_support

## Projects or organizations relevant to this project before?

1. [Qubes OS](https://www.qubes-os.org/)
2. [Xen Hypervisor](https://xenproject.org/)
3. [GNU GRUB](https://www.gnu.org/software/grub/)
4. [TrenchBoot](https://trenchboot.org/)
5. [Invisible Things Lab](https://invisiblethingslab.com/)
6. [Apertus Solutions](https://apertussolutions.com/)
7. [Oracle](https://www.oracle.com/)
8. [3mdeb](https://3mdeb.com/)

## The ecosystem of the project

3mdeb has a good relationship with the maintainers of relevant projects which
will participate in review of the work:

- Marek Marczykowski-Górecki (Invisible Things Lab CTO) - Qubes OS maintainer
- Andrew Cooper (Citrix) - Xen Hypervisor Maintainer
- Daniel Kiper (Oracle) - GRUB2 Maintainer
- Daniel Smith (Apertus Solutions) - TrenchBoot founder and maintainer

## Review

Further reviews and suggestions are welcome. You can do it in two ways:

- using Giscus on the bottom of this page
- contributing to this repository directly via Pull Request
