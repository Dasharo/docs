---
template: giscus.html
---

# UEFI Capsule Update for coreboot with EDK II

## Abstract

The project integrates UEFI capsule update methods into coreboot with EDK II
firmware frameworks to streamline firmware updates. UEFI capsule update is an
industry-standard approach widely supported by hardware vendors, providing a
secure method for delivering firmware updates.

By adopting UEFI capsule update methods, the project aims to simplify the update
process and enhance the user experience, providing a more reliable approach
compared to complex flashrom-based updates, which are still common in the
open-source firmware distributions based on coreboot. Due to security measures,
OS-level access to firmware is intentionally restricted, which in turn makes it
increasingly challenging to apply firmware updates from the operating system.
This limitation poses difficulties in utilizing traditional flashrom-based
methods for firmware updates. The expected outcomes of the project include
enhanced firmware update capabilities, a simplified user experience, heightened
security, and enhanced compatibility.

## Involvement with projects or organisations relevant to this project

Relevant projects:

- coreboot [\[1\]][1]
- Dasharo compatible with MSI PRO Z690-A DDR4 (and the subsequent port for the
- DDR5 variant) [\[2\]][2]
- Dasharo compatible with Dell Optiplex [\[3\]][3]
- EDKII [\[4\]][4]
- Fwupd (LVFS) [\[5\]][5]
- U-Boot [\[6\]][6]

3mdeb has been a licensed provider of quality coreboot consulting services
since 2016. We are well-known in the open-source community for maintaining th
firmware of the PC Engines APU series platform since 2016, delivering
high-quality firmware releases each month and providing technical support on PC
Engines and OPNSense forums. Our contribution to the coreboot project reaches
(as of 26th of July 2023):

**319** individual patches merged to the official coreboot repository
**33481** lines of code added
**41097** lines of code removed

Moreover, we constantly develop Dasharo, which is an open-source firmware
distribution focusing on clean and simple code, long-term maintenance,
transparent validation, privacy-respecting implementation, liberty for the
owners, and trustworthiness for all. More details can be found here [\[7\]][7].

[1]: https://github.com/coreboot/coreboot
[2]: https://docs.dasharo.com/unified/msi/overview/
[3]: https://docs.dasharo.com/variants/dell_optiplex/overview/
[4]: https://github.com/tianocore/edk2
[5]: https://github.com/fwupd/fwupd
[6]: https://u-boot.readthedocs.io/
[7]: https://docs.dasharo.com/

## Project scope

**Task 1. Enable Capsule Updates in coreboot**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/31)

This task enhances coreboot by enabling support for UEFI Capsule Update. It
modifies coreboot to be able to
access beyond 4GB, and implements mechanisms for identifying capsule image
locations. Capsule coalescing logic is ported to coreboot to consolidate firmware update
capsules into a single memory region. coreboot is adjusted to reserve this
memory region and pass the information to the UEFI payload. Additionally, a new
SMI handler is implemented to write to SPI flash, enabling full BIOS image overwrite
only when a valid capsule update is present.

- Enable memory access above 4GB
- Parse capsule location from UEFI variables in coreboot
- Gather capsules into one region
- Reserve memory containing capsules and pass it to the payload
- Add SMI handler for flashing firmware updates

**Task 2. Enable capsule updates in coreboot EDK II UEFI Payload**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/32)

The UEFI payload integration phase integrates enhanced coreboot firmware with
the UEFI system, ensuring accurate tracking of firmware updates via the EFI
System Resource Table (ESRT). A library instance facilitates flash access
operations within UEFI, supported by an SMI handler in coreboot.

Updates to Firmware Descriptor (FDF) and Device Scope Configuration (DSC) files
are made, enabling boot mode selection and invoking ProcessCapsules() during
firmware updates. coreboot version information is extracted and incorporated
into the ESRT to prevent rollback. The workflow is streamlined to generate
capsules containing coreboot.rom images, with automation where feasible.

- Implement PlatformFlashAccessLib leveraging coreboot SMI handler
- Modify FDF/DSC files and capsule processing
- Parse version reported by coreboot for ESRT
- Develop process for building capsules from coreboot.rom

**Task 3. Test the solution on a hardware**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/33)

This task will involve testing the UEFI Capsule Update on hardware to ensure its
proper functionality and compatibility. The CAPSULE_ENABLE feature will be
validated using test signing keys before transitioning to product-specific ones.
Furthermore, a mechanism will be tested to prevent the operating system from
booting until a reboot occurs following the firmware update process. The primary
objective is to ensure that the system remains secure and stable after firmware
updates are applied.

- Verify feature using test signing keys
- OS block booting verification

**Task 4. Secure Firmware Signing**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/34)

This task focuses on implementing secure firmware signing processes for update
integrity and authenticity. OpenSSL utilities are used for generating signing
keys, enhancing security. A streamlined binary compilation procedure simplifies
the signing process for end-users. OpenSSL command line utilities are utilized
to generate necessary signing keys. The milestone includes creating a
user-friendly procedure for binary signing without embedding private keys into
build system, ensuring consistency and efficiency. Comprehensive documentation
for end-users will be provided, detailing firmware update procedures and feature
utilization.

- Generate signing keys using OpenSSL utilities
- Develop binary compilation without using a private key
- End-user documentation

**Task 5. Enhanced Boot Process with vboot A/B Support**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/35)

This task improves the firmware update process for security, stability, and
user-friendliness. Integrating the vboot A/B scheme ensures a reliable fallback
for problematic updates, while automated execution of the UX capsule enhances
the user experience. Enhancements will support the vboot A/B scheme for
fallbacks and use the UX capsule to inform users of update progress. This
prevents user impatience during longer update times, reducing the risk of
platform malfunction due to premature reboot attempts.

- Add support for the vboot A/B scheme
- Automate the creation and execution of the UX capsule

**Task 6. Test and release UEFI Capsule Update for coreboot and EDK II**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/36)

This task involves the testing and release of firmware updates for MSI
platforms. The main objective is to thoroughly verify the successful update
process and ensure system stability and security after implementing the new
firmware update method. This entails rigorous testing to guarantee the
reliability and integrity of the updated firmware on both platforms.

- Test and publish release for MSI PRO Z790-P
- Test and publish release for MSI PRO Z690-A DDR4/DDR5

**Task 7. Upstream of the UEFI Capsule Update for coreboot with EDK II in
coreboot**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/37)

The primary objective is to upstream the UEFI Capsule Update functionality
directly into the coreboot codebase, ensuring its availability as part of the
coreboot project and expanding the firmware update capabilities for
coreboot-supported systems. The code implementing UEFI Capsule Update for
coreboot with EDK II shall be upstreamed to the official coreboot repository at
[review.coreboot.org](https://review.coreboot.org/).

**Task 8. Upstream of the UEFI Capsule Update for coreboot with EDK II in EDK
II**

- [GitHub Milestone for tracking
  progress](https://github.com/Dasharo/dasharo-issues/milestone/38)

The objective is to integrate the UEFI Capsule Update implementation into the
official codebase, contributing to the EDK II ecosystem and improving firmware
update capabilities for coreboot-supported systems. The code implementing UEFI
Capsule Update for coreboot with EDK II will be upstreamed to the official EDK
II repository at
[github.com/tianocore/edk2](https://github.com/tianocore/edk2).

## Compare your own project with existing or historical efforts

3mdeb's embedded systems developers are experienced engineers accustomed to
firmware development on desktops. There are a few successfully enabled coreboot
supported Dell machines that were enabled by 3mdeb and other platforms based on
Intel FSP. By leveraging our knowledge and experience from the ESRT project,
which plays a vital role within the operating system to initiate capsule updates
at the system level, we bring valuable insights and advancements to the firmware
update process.

Through our contributions, we aim to promote open-source firmware adoption and
facilitate a more robust and secure firmware update process, benefiting
open-source firmware community and and ensuring a user-friendly and efficient
firmware update experience for end-users.

- MSI Z690-A PRO DDR4 / DDR5: <https://review.coreboot.org/c/coreboot/+/63463>
- Dell OptiPlex 7010/9010 SFF: <https://review.coreboot.org/c/coreboot/+/40351>
- Dell Precision T1650: <https://review.coreboot.org/c/coreboot/+/62212>
- Libretrend LT1000: <https://review.coreboot.org/c/coreboot/+/30360>
- Protectli FW2B/FW4B: <https://review.coreboot.org/c/coreboot/+/32076>
- Protectli FW6: <https://review.coreboot.org/c/coreboot/+/33839>
- Fwupd for BSD: <https://www.phoronix.com/news/FWUPD-To-The-BSDs>
- EFI System Resource Table (ESRT): <https://reviews.freebsd.org/rG24f398e7a153a05a7e94ae8dd623e2b6d28d94eb>

## Significant technical challenges you expect to solve during the project

The coreboot and EDK II firmware frameworks need to be modified to support UEFI
capsule update methods. This integration requires understanding and implementing
the UEFI specification, especially the EFI_FIRMWARE_MANAGEMENT_PROTOCOL, FMP
capsule format, and EFI System Resource Table (ESRT).

Adapting coreboot and EDK II to support these mechanisms will involve extensive
code changes and ensuring compatibility with the UEFI standard. Solving these
challenges will involve significant code modifications, rigorous testing, and an
active collaboration with the coreboot and EDK II communities to ensure
successful integration and smooth functionality.

## Ecosystem of the project

Although 3mdeb will be responsible for the whole implementation and testing,
anyone is also welcome to test, develop code, and report issues after the
results will be published. For the project to be successful, the outcomes should
be included in the upstream coreboot and edk2 projects for the benefit of the
wider community. That is why we expect high level of engagement with communities
of both of this projects at each stage of the project, to make sure the proposed
solution can be accepted upstream.

There are members of the open-source community interested in this outcome:

- Richard Hughes - *This proposal is an important step forward for coreboot
moving towards the industry standard UpdateCapsule update method. With this
functionality we can use the existing generic capsule plugin rather than having
to configure each board with flashrom. From a security point of view, updating
using flashrom means the SPI device cannot be locked at runtime, and moving to
UpdateCapsule allows the vendor to secure the platform significantly. This
proposal is an important step forward for coreboot.*

- Wessel klein Snakenborg (NovaCustom) - *As a leading provider of customizable
and privacy-focused laptops, NovaCustom is committed to offering our customers
the most secure and seamless user experience. We are dedicated to providing our
valued customers with the best possible user experience. The project, UEFI
Capsule Update for coreboot with EDK II, perfectly aligns with this commitment.
By integrating the widely supported UEFI capsule update methods into our
open-source firmware frameworks, we aim to highly improve the firmware update
process for our users. With this implementation, updating firmware becomes a
breeze, as our customers can seamlessly utilize the popular firmware update
management tool for Linux systems: fwupd. This user-friendly approach ensures
that our customers can easily and securely keep their laptops up-to-date with
the latest features and security enhancements. Increasing the accessibility of
the firmware update procedure encourages people to perform firmware updates more
promptly, thereby enhancing the overall security of coreboot+EDK-II.*

## Review

Further reviews and suggestions are welcome. You can do it in two ways:

- using Giscus on the bottom of this page
- contributing to this repository directly via Pull Request

## Funding

This project is partially funded through
[NGI0 Entrust](https://nlnet.nl/entrust), a fund established by
[NLnet](https://nlnet.nl) with financial support from the European Commission's
[Next Generation Internet](https://ngi.eu) program. Learn more at the
[NLnet project page](https://nlnet.nl/project/UEFICapsuleUpdate/).

<div style="display: flex; justify-content: center;">
    <a href="https://nlnet.nl"><img src="https://nlnet.nl/logo/banner.png"
    alt="NLnet foundation logo" height="40" /></a>
    <a href="https://nlnet.nl/entrust"><img
    src="https://nlnet.nl/image/logos/NGI0_tag.svg" alt="NGI Zero logo"
    height="40" /></a>
</div>
