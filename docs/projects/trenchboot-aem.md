---
template: giscus.html
---

# Trenchboot as Anti Evil Maid

## Abstract

The firmware is the heart of the security of a given system and should be
always up-to-date to maintain the security of the computer. However, being up
to date does not prevent the firmware vulnerabilities to appear. The Static
Root of Trust (SRT) like Unified Extensible Firmware Interface (UEFI) Secure
Boot and measured boot provided by the firmware is not always sufficient to
establish a secure environment for an operating system. In case the firmware is
compromised, it could inject malicious software into operating system
components and prevent the machine owner from detecting it. Silicon vendors
implement alternative technologies to establish a Dynamic Root of Trust (DRT)
to provide a secure environment for operating system launch and integrity
measurements. These integrity measurements either from SRT or DRT can be used
for operating system attestation. However, DRT technologies are designed in a
way to provide the ability to establish a secure environment for integrity
measurements at any arbitrary point of time instead of relying on the firmware
which requires machine reset to establish the aforementioned secure
environment.

The usage of DRT technologies like Intel Trusted Execution Technology (TXT) or
AMD Secure Startup becomes more and more significant, for example, Dynamic Root
of Trust for Measurement (DRTM) requirements of
[Microsoft Secured Core PCs][ms_sec_core]. In open-source projects, DRTM hasn't
found its place yet, but that gradually changes. The demand on having firmware
independent Roots of Trust is increasing and projects that satisfy this demand
are growing, for instance, [TrenchBoot][tb_org]. TrenchBoot is a framework that
allows individuals and projects to build security engines to perform launch
integrity actions for their systems. The framework builds upon Boot Integrity
Technologies (BITs) that establish one or more Roots of Trust (RoT) from which
a degree of confidence that integrity actions were not subverted. The project
has grown a lot thanks to the previous [NLnet NGI0 PET grant][nlnet_opendrtm]
and now it looks for further expansion into extensive use of the DRT
technologies in open-source and security-oriented operating systems like
[Qubes OS][qubes_os_org]. [Qubes OS Anti Evil Maid (AEM)][it_aem] software
heavily depends on the availability of the DRTM technologies to prevent the
[Evil Maid attacks][em_attacks]. However, the project hasn't evolved much since
the beginning of 2018 and froze on the support of TPM 1.2 with Intel TXT in
legacy boot mode (BIOS). This effectively limits the usage of this security
software to older Intel machines only. TPM 1.2 implemented SHA1 hashing
algorithm which is nowadays considered weak in the era of forever-increasing
computer performance and quantum computing. The solution to this problem comes
with a newer TPM 2.0 with more agile cryptographic algorithms and SHA256
implementation by default. Qubes OS AEM software suffers from the following:

1. Lack of TPM 2.0 support to handle more secure hashes and safer design of the
   TPM firmware according to a newer specification.
2. Lack of UEFI mode support. All modern systems boot in UEFI mode only, legacy
   boot modes are being deprecated and dropped from the PC firmware. This
   effectively limits the usage of AEM on most if not all modern machines.
3. Qubes OS AEM has never supported any AMD processors with AMD Secure Startup
   technology. Implementing AMD support would make a huge impact and broaden
   the usage of DRTM technologies.

The initial AEM implementation relied on the [Trusted Boot][tboot_wiki],
Intel's reference implementation of Intel TXT. It had never any plans to
support AMD processors. TrenchBoot is filling this gap supporting both Intel
and AMD hardware which makes it an ideal target to replace Trusted Boot in
Qubes OS AEM implementation. Furthermore, the project grant would be used to
implement the missing pieces in the Qubes OS AEM software to cover the AMD and
Intel support for both TPM 1.2 and TPM 2.0.

## Compare your own project with existing or historical efforts

3mdeb is a licensed provider for quality coreboot consulting services since
2016. We are well-known in the open-source community for maintaining firmware
of the PC Engines APU series platform since 2016. Delivering high-quality
firmware releases each month and providing technical support on PC Engines and
OPNSense forums. 3mdeb embedded systems developers are experienced engineers
accustomed to operating systems development. Our developers have contributed to
the [fwupd support for Qubes OS][8]. 3mdeb is also regularly co-organizing
mini-conference events with Qubes OS maintainer Marek Marczykowski-Górecki
where various topics related to Qubes OS security are discussed. Among them,
the Anti Evil Maid was frequently presented by 3mdeb engineers:

- [Anti Evil Maid for Intel coreboot-based platform][aem_intel]
- [Anti Evil Maid for modern AMD UEFI-based platform][aem_amd]

A similar approach was already tried by Assured Information Security (AIS) to
boot [Xen in UEFI mode with Intel TXT DRTM technology][ais_aem], however, this
is only a small portion of the work covered by our proposal. Additionally,
Qubes OS does not launch using Xen.efi like in the AIS work, but uses
[Multiboot2 protocol with GRUB2][qubes_mb2] instead which makes this approach
unusable. Moreover, the Xen.efi approach is much more complex and assumes usage
of Trusted Boot, limiting the feature to Intel hardware only.

## What are the significant technical challenges you expect to solve

First of all Qubes OS AEM software consists of software packages providing
Trusted Boot and the [Qubes OS TPM scripts][aem_scripts]. These software
packages would need to replace the Trusted Boot with TrenchBoot supported GRUB2
and Xen. Secondly, the TPM scripts require adding support for TPM 2.0
equivalent functionality. AEM requires access to non-volatile RAM inside TPM
which is defined differently in the TPM 2.0 specification compared to TPM 1.2.

Another challenge would be to make Xen possible to boot in UEFI boot mode
without Boot Services defined in UEFI specification. Boot Services are a set of
functions exposed in UEFI structures that are used to help with handling the
boot process. However, the main principle of DRTM technologies is to not depend
on any external code that is not a part of the operating system software to be
executed after DRTM. UEFI Boot Services are a part of the firmware of which
DRTM tries to be independent. The whole security concept of DRTM depends on
cutting the ties with firmware. Thus the work includes implementing the
capability in Xen to not use the UEFI Boot Services, which would be terminated
by GRUB2 before DRTM is executed. Xen also contains an option to not use the
UEFI Runtime Services. Runtime Services is a set of functions available
throughout the whole machine lifetime, it means some firmware functionalities are
available even when the operating system is launched.

Removing the Boot Services from Xen brings certain drawbacks to the system,
because the Boot Services hold very important information like memory map, TPM
event log, graphics framebuffer etc. This information must be extracted by
GRUB before Boot Services are terminated and passed to the Xen. The proposed
solution is to pass this information via the Multiboot2 tags defined in the
specification for this particular Boot Services information.

## Requested support

1. Phase 1: TrenchBoot Intel TXT and TPM 1.2 support

    + Add TPM 1.2 support for Intel TXT in TrenchBoot GRUB2

        The TrenchBoot support hasn't been implemented and verified with TPM
        1.2 on Intel TXT path. This requirement ensures the TPM 1.2 is also
        supported for older Intel hardware with Intel TXT.

    + Xen Secure Launch - Intel TXT support in Xen for TrenchBoot

        Due to the requirements of Intel TXT and how it is utilised, it is
        impossible to use the Xen boot protocols defined in the UEFI or Multiboot2
        specifications. This task aims to create a custom Intel TXT entry point for
        Xen which would hand-off to the standard Multiboot2 entry point and enable
        direct launch of Xen by GRUB via DRTM on Intel hardware. Additionally there
        is no support for launching Xen with Intel TXT other than Trusted Boot. It
        has to be ported from Trusted Boot specific code:

         * constructing MLE header
         * waking up APs
         * restoring MTRRs
         * reserving the TXT memory
         * reenabling SMIs
         * handling TXT shutdown and S3 resume/suspend
         * TPM event log finding

    + Test the solution on Intel hardware with TPM 1.2 with legacy boot mode

2. Phase 2 - Qubes OS AEM TPM 2.0 support:

    + Extend the AEM scripts to detect TPM version on the platform

        As TPM 1.2 and TPM 2.0 use different software stacks and tools, it is
        necessary to distinguish the TPM module family and use the appropriate
        software. The task will implement the logic to distinguish the TPM
        families.

    + Extend the AEM scripts to use appropriate software stack for TPM 2.0

        While AEM fully supports TPM 1.2 there is no support for TPM 2.0 at
        all. When the TPM family is determined the script should use the
        appropriate software stack for given TPM. The task implements the AEM
        TPM 1.2 equivalent functionalities using TPM 2.0 software stack and as
        a result allowing the use of TPM 2.0 with Qubes OS AEM. It will require
        implementing the access to TPM 2.0 NVRAM, sealing and unsealing the
        secret data and generating TOTP.

    + Test the solution on Intel hardware with TPM 2.0 with legacy boot mode

3. Phase 3 - Qubes OS AEM AMD support:

    + Rebase and refresh TrenchBoot GRUB2 for QubesOS

        Some work to implement TrenchBoot support for Qubes OS on AMD hardware
        has been done. GRUB2 with TrenchBoot support has been added to Qubes
        building system on [3mdeb fork](https://github.com/3mdeb/qubes-grub2/tree/trenchboot_support)
        The task aims to refresh the work and align with the upstream
        [Qubes OS GRUB2 repository](https://github.com/QubesOS/qubes-grub2)

    + Clean up the Secure Kernel Loader (formerly LandingZone) package support
      for QubesOS

        Since the initial work done by 3mdeb engineers for AMD AEM in Qubes OS a
        lot of time has passed and Secure Kernel Loader - SKL (formerly Landing
        Zone) has improved a lot and added new features. SKL is an open-source
        module written by TrenchBoot developers required by AMD Secure Startup
        technology to perform DRTM launch. The task aims to refresh the previous
        work and upate the SKL package for Qubes OS to the newest revision.

    + TrenchBoot Secure Kernel Loader (SKL) improvements for AMD server CPUs with
      multiple nodes

        While SKL was extensively tested on System on Chip and single CPU
        platforms, it was not much tested on workstation/server segment CPUs which
        are more complex. For example one server CPU package may contain two
        independent CPUs inside called nodes. Each node will enable protection on
        the SKL during DRTM execution. This protection has to be disabled on each
        node when TrenchBoot DRTM tasks are done. The task implements the correct
        support for server CPUs in TrenchBoot SKL.

    + Test the solution on AMD hardware with TPM 2.0 and TPM 1.2 with legacy boot
      mode

4. Phase 4 - Xen UEFI boot mode with DRTM:

    + TrenchBoot support for UEFI boot mode for AMD in GRUB

        While TrenchBoot DRTM was extensively tested on Intel hardware with UEFI
        firmware and Linux, it was not on AMD platforms. This task ensures that
        DRTM works with UEFI boot mode on AMD processors in GRUB2 and Linux without
        UEFI Boot Services.

    + TrenchBoot support for UEFI boot mode in Xen

        When UEFI boot mode with TrenchBoot is working with GRUB2 and Linux, all
        that is missing to fully support AMD and Intel hardware with Qubes OS AEM
        is the Xen support to boot in UEFI mode without Boot Services. This
        requires a significant amount of work to make sure that all information
        that Xen would obtain from UEFI Boot Services would be still available. The
        information has to be passed by GRUB2 to Xen via Multiboot2 protocol:

         * EFI memory map
         * Framebuffer information
         * PCI devices information with their option ROMs

        Additionally "EFI boot services not terminated" Multiboot2 tag must not be
        passed to Xen by GRUB2 on DRTM launch when GRUB2 will terminate Boot
        Services. Xen should detect such situation and act according to the state
        of Boot Services. Xen will be implemented to:

         * parse the EFI memory map, framebuffer information and PCI devices
           information passed by GRUB2
         * do not expose the "EFI boot services" Multiboot2 tag indicating that
           Xen can be executed without UEFI Boot Services presence
         * allocate the memory space for the trampoline used to launch other
           processors or use the allocation done by GRUB2 if necessary
         * do not go error path when Boot Services are not present and skip all
           calls to UEFI Boot Services by using the information provided by GRUB2

    + Test the solution on AMD and Intel hardware with TPM 2.0 and TPM 1.2 with
      legacy and UEFI boot mode

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

[ms_sec_core]: https://docs.microsoft.com/en-us/windows-hardware/design/device-experiences/oem-highly-secure#what-makes-a-secured-core-pc
[tb_org]: https://trenchboot.org/
[nlnet_open_drtm]: https://nlnet.nl/project/OpenDRTM/
[qubes_os_org]: https://www.qubes-os.org/
[it_aem]: https://blog.invisiblethings.org/2011/09/07/anti-evil-maid.html
[em_attacks]: http://theinvisiblethings.blogspot.com/2009/10/evil-maid-goes-after-truecrypt.html
[tboot_wiki]: https://sourceforge.net/p/tboot/wiki/Home/
[qubes_fwupd]: https://blog.3mdeb.com/2020/2020-07-14-qubesos-fwupd-core/
[aem_intel]: https://www.youtube.com/watch?v=YE2FbFlszI4
[aem_amd]: https://www.youtube.com/watch?v=rM0vRi6qABE
[ais_aem]: https://www.youtube.com/watch?v=6NScGNSg3ks
[qubes_mb2]: https://github.com/QubesOS/qubes-issues/issues/4902
[aem_scripts]: https://github.com/QubesOS/qubes-antievilmaid/blob/master/sbin/
