## Abstract

### Can you explain the whole project and its expected outcome(s).

The project, UEFI Capsule Update for coreboot with EDK II, aims to improve the
firmware update process by integrating UEFI capsule update methods into coreboot
with EDK II open-source firmware frameworks. UEFI capsule update is an
industry-standard approach widely supported by hardware vendors, providing a
secure and reliable method for delivering firmware updates. By adopting UEFI
capsule update methods, the project aims to simplify the update process and
enhance the user experience, providing a more secure and reliable approach
compared to complex flashrom-based updates, which are still common in the
open-source firmware distributions based on coreboot. Due to security measures,
OS-level access to firmware is intentionally restricted, which in turn makes it
increasingly challenging to apply firmware updates from the operating system.
This limitation poses difficulties in utilizing traditional flashrom-based
methods for firmware updates. The expected outcomes of the project include
enhanced firmware update capabilities, a simplified user experience, heightened
security, and enhanced compatibility, all achieved by seamlessly integrating
with fwupd, a popular firmware update management tool for Linux systems.

### Explain what the requested budget will be used for?
### Does the project have other funding sources, both past and present?


**Task 1. Enable Capsule Updates in coreboot**

This task aims to enhance the coreboot framework by adding support for UEFI
Capsule Update.

* Enable memory access above 4GB

Modify coreboot to operate in 64-bit mode and enable access to memory above the
4GB limit.

* Parse capsule location from UEFI variables in coreboot

Implement a mechanism for coreboot to identify the memory location of the
capsule images from drivers to UEFI variables. This milestone ensures accurate
retrieval of capsule images by coreboot.

* Gather capsules into one region

Rewrite the existing capsule coalescing logic to consolidate all firmware update
capsules into a single memory region.

* Reserve memory containing capsules and pass it to the payload

Implement the necessary changes in coreboot to reserve the memory region
containing the capsules. Pass this information to the UEFI payload using the
Hand-Off Block (HOB) data structure.

* Add SMI handler for flashing firmware updates

Implement a handler able of writing to SPI flash. Similar handler already
exists, but it is limited to SMMSTORE region, used to implement secure UEFI
variables. New handler would allow to overwrite whole BIOS image, so it must not
be enabled unless a valid capsule update is present.

**Task 2. Enable capsule updates in coreboot EDK II UEFI Payload**

The UEFI payload integration task involves integrating the enhanced coreboot
firmware with the UEFI system. Additionally, parsing the version reported by
coreboot and incorporating it into the EFI System Resource Table (ESRT) ensures
accurate tracking of system firmware updates. These integrations enhance
firmware reliability, provide advanced update capabilities, and enable a
seamless user experience.

* Implement PlatformFlashAccessLib leveraging coreboot SMI handler

Create a library instance that enables flash access operations within the UEFI
platform with the help of SMI handler implemented in coreboot.

* Modify FDF/DSC files and capsule processing

Update the Firmware Descriptor (FDF) and Device Scope Configuration (DSC) files.
Enable boot mode selection and invoke ProcessCapsules() at the necessary stages
during the firmware update process.

* Parse version reported by coreboot for ESRT

Extract coreboot version information and incorporate it into the EFI System
Resource Table (ESRT) within UEFI, to reflect the updated firmware and prevent
rolling back to earlier versions.

* Develop process for building capsules from coreboot.rom 

Establish a streamlined workflow to generate capsules containing the
coreboot.rom image and automate the process where possible.

**Task 3. Test the solution on a hardware**

In this task, the UEFI Capsule Update will be tested on the hardware to ensure
its proper functionality and compatibility.

* Verify feature using test signing keys

Validate the CAPSULE_ENABLE feature using test signing keys before using
product-specific signing keys.

* OS block booting verification

Test a mechanism that prevents the operating system from booting until a reboot
occurs after the firmware update process. The primary objective is to ensure
that the system remains secure and stable after firmware updates are applied.

**Task 4. Secure Firmware Signing**

In this task the focus is on implementing secure firmware signing processes to
ensure the integrity and authenticity of firmware updates. The use of OpenSSL
utilities for generating signing keys enhances security, while the developed
binary compilation procedure simplifies the signing process for end-users.

* Generate signing keys using OpenSSL utilities

Utilize OpenSSL command line utilities to generate the necessary signing keys
for the capsule update process.

* Develop binary compilation without using a private key

This milestone involves creating a comprehensive procedure for users, outlining
the process of signing binaries without the use of a private key, ensuring a
consistent and efficient signing process.

* End-user documentation

Create comprehensive documentation for end-users, including detailed
instructions on how to perform firmware updates and utilize the provided
features effectively.

**Task 5. Enhanced Boot Process with vboot A/B Support**

This task aims to establish a more secure, stable, and user-friendly firmware
update process. The incorporation of the vboot A/B scheme will provide a
reliable fallback in case of problematic updates, while the automated execution
of the UX capsule will enhance the end-user experience during firmware updates.

* Add support for the vboot A/B scheme

Enhance the firmware update mechanism to support the vboot A/B scheme, providing
a fallback option in case of unstable updates.

* Automate the creation and execution of the UX capsule

Use UX capsule to convey message to the user that the update is in progress.
Because update takes significantly more time than normal boot, impatient user
may think that the boot process is stuck and try to force a platform reboot,
which in turn may end up with non-working platform.

**Task 6. Test and release UEFI Capsule Update for coreboot and EDK II**

Task 6 involves testing and release of firmware updates for both MSI PRO Z790-P
and MSI PRO Z690-A DDR4/DDR5 platforms. The primary focus is to verify the
successful update process, ensuring system stability and security after applying
the new firmware update method.

* Test and publish release for MSI PRO Z790-P

Verify the successful update process and ensure system stability and security
after applying the new firmware update method.

* Test and publish release for MSI PRO Z690-A DDR4/DDR5

Verify the successful update process and ensure system stability and security
after applying the new firmware update method.

**Task 7. Upstream of the UEFI Capsule Update for coreboot with EDK II in
coreboot**

The primary objective is to merge the UEFI Capsule Update functionality directly
into the coreboot codebase, ensuring its availability as part of the coreboot
project and expanding the firmware update capabilities for coreboot-supported
systems.

The code implementing UEFI Capsule Update for coreboot with EDK II shall be
upstreamed to the official coreboot repository at https://review.coreboot.org/.

**Task 8. Upstream of the UEFI Capsule Update for coreboot with EDK II in EDK
II**

The goal is to ensure that the UEFI Capsule Update implementation becomes a part
of the official codebase, contributing to the wider EDK II ecosystem and
enhancing the firmware update capabilities for coreboot-supported systems.

The code implementing UEFI Capsule Update for coreboot with EDK II shall be
upstreamed to the official EDK II repository at
https://github.com/tianocore/edk2.

### What are significant technical challenges you expect to solve during the
### project, if any?

The coreboot and EDK II firmware frameworks need to be modified to support UEFI
capsule update methods. This integration requires understanding and implementing
the UEFI specification, especially the EFI_FIRMWARE_MANAGEMENT_PROTOCOL, FMP
capsule format, and EFI System Resource Table (ESRT). Adapting coreboot and EDK
II to support these mechanisms will involve extensive code changes and ensuring
compatibility with the UEFI standard. Solving these challenges will involve
significant code modifications, rigorous testing, and an active collaboration
with the coreboot and EDK II communities to ensure successful integration and
smooth functionality.
