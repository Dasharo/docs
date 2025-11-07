# Sovereign Boot Provisioning Wizard

## Introduction and motivation

Sovereign Boot Provisioning Wizard is an UEFI application designed to guide
end users through the provisioning of UEFI Secure Boot. The objective is to
offer a user-controllable mechanism for managing platform trust relationships
and establishing UEFI Secure Boot infrastructure, with a primary focus on
transparency, informed consent, and usability.

Unlike traditional firmware interfaces, which expose UEFI Secure Boot as a
collection of loosely connected toggleable settings and unmanaged certificate
stores, this application presents a coherent, wizard-like experience. Its
purpose is to make the process of reviewing and enrolling platform keys
intuitive for users who are not security experts.

## Specification

The application is implemented based on the [Sovereign Boot Provisioning
Wizard
Specification](https://github.com/3mdeb/verified-boot/blob/55df31bf0645767e18c4dac7e19bf62d788e9df8/verified_boot_app_spec.md#sovereign-boot-provisioning-wizard)
(current revision v0.1.0).

## Credits

This research has been supported by [Power Up
Privacy](https://powerupprivacy.com/), a privacy advocacy group that seeks to
supercharge privacy projects with resources so they can complete their mission
of making our world a better place.

Author of the idea and motivation: [Patrick Schleizer](https://github.com/adrelanos).

Design and technical support: [Aaron Rainbolt](https://github.com/ArrayBolt3).

## Contribution

One may contribute to the project in many ways:

* request features and changes, report issues via
  [GitHub](https://github.com/Dasharo/dasharo-issues/issues/new/choose) (use
  [SovereignBoot
  label](https://github.com/Dasharo/dasharo-issues/labels/SovereignBoot))
* open Pull Requests to [Dasharo EDK2](https://github.com/Dasharo/edk2)
  (application code is under
  `DasharoModulePkg/Application/SovereignBootWizard`)
* open Pull Requests to [verified-boot
  repository](https://github.com/3mdeb/verified-boot) to suggest changes to
  the specification

## Future ideas

This is backlog of future ideas and improvements obtained via community
feedback:

* [Add BIOS Boot Password feature](https://github.com/Dasharo/dasharo-issues/issues/1547)
* [Handle OptionROMs in Sovereign Boot Wizard](https://github.com/Dasharo/dasharo-issues/issues/1548)
* [Key discovery on filesystems in Sovereign Boot Wizard](https://github.com/Dasharo/dasharo-issues/issues/1550)
* [Supporting different security models in Sovereign Boot Wizard](https://github.com/Dasharo/dasharo-issues/issues/1551)
* [Implement Sovereign Boot Wizard lockdown mode](https://github.com/Dasharo/dasharo-issues/issues/1552)

Feel free to suggest new improvements and features to extend the Sovereign
Boot Provisioning Wizard.

If you have any questions about Sovereign Boot Provisioning Wizard, visit the
[FAQ](../osf-trivia-list/sovereign-boot-wizard.md).

## Releases

### RC4 - 2025-09-30

#### Fixed

* [Sovereign Boot Wizard does not discover alternative bootloaders yet](https://github.com/Dasharo/dasharo-issues/issues/1549)

#### Binaries

[qemu_q35_sovereign-boot-rc4.rom](https://cloud.3mdeb.com/index.php/s/ZyDFLrppzEfoP22/download){.md-button}
[qemu_q35_sovereign-boot-rc4.rom.sha256](https://cloud.3mdeb.com/index.php/s/WtSgMSe3PqBQnxy/download){.md-button}

#### SBOM

* [coreboot based on 24.12 revision qemu_q35_sovereign_boot-rc4](https://github.com/Dasharo/coreboot/tree/qemu_q35_sovereign_boot-rc4)
    + [License](https://github.com/Dasharo/coreboot/blob/qemu_q35_sovereign_boot-rc4/COPYING)
* [Dasharo EDKII fork based on edk2-stable202502 revision sovereign-boot-rc4](https://github.com/Dasharo/edk2/tree/sovereign-boot-rc4)
    + [License](https://github.com/Dasharo/edk2/blob/sovereign-boot-rc4/License.txt)

#### Building

Follow the [instructions for
QEMU](../variants/qemu_q35/building-manual.md#procedure). Checkout
`qemu_q35_sovereign_boot-rc4` tag on coreboot repository and use new
`qemu_svboot` target as an argument to `./build.sh` script.

#### Video demonstration

Watch a short demonstration of Sovereign Boot Wizard in action. This video
covers the new features of the Sovereign Boot Wizard and complements the
documentation.

<div class="video-wrapper">
  <iframe
    src="https://www.youtube.com/embed/lmQLamzZ-lE?si=bduowzxhe8-jOlci"
    title="Sovereign Boot Wizard RC4 Demo"
    frameborder="0"
    allow="accelerometer; autoplay;
      clipboard-write; encrypted-media;
      gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

### RC3 - 2025-08-29

#### Added

* Filtering and skipping Microsoft certificates in the image signatures
* Sovereign Boot tested on Hardkernel ODROID-H4 hardware

#### Fixed

* [Measured boot reports volume full error when chaining EFI binary from the
  Sovereign Boot Provisioning
  Wizard](https://github.com/Dasharo/dasharo-issues/issues/1479)
* [UEFI Secure Boot variables protection not yet tested](https://github.com/Dasharo/dasharo-issues/issues/1478)

#### Known issues

* [Sovereign Boot Wizard does not discover alternative bootloaders yet](https://github.com/Dasharo/dasharo-issues/issues/1549)

#### SBOM

* [coreboot based on 24.12 revision hardkernel_odroid_h4_sovereign_boot-rc3](https://github.com/Dasharo/coreboot/tree/hardkernel_odroid_h4_sovereign_boot-rc3)
    + [License](https://github.com/Dasharo/coreboot/blob/hardkernel_odroid_h4_sovereign_boot-rc3/COPYING)
* [coreboot based on 24.12 revision qemu_q35_sovereign_boot-rc3](https://github.com/Dasharo/coreboot/tree/qemu_q35_sovereign_boot-rc3)
    + [License](https://github.com/Dasharo/coreboot/blob/qemu_q35_sovereign_boot-rc3/COPYING)
* [Dasharo EDKII fork based on edk2-stable202502 revision sovereign-boot-rc3](https://github.com/Dasharo/edk2/tree/sovereign-boot-rc3)
    + [License](https://github.com/Dasharo/edk2/blob/sovereign-boot-rc3/License.txt)

#### Building

* ODROID-H4

    Follow the [instructions for
    ODROID-H4](../variants/hardkernel_odroid_h4/building-manual.md#building) by
    using `hardkernel_odroid_h4_sovereign_boot-rc3` tag to checkout coreboot
    repository. The resulting file will be placed in
    `<coreboot_dir>/build/coreboot.rom`.

* QEMU:

    Follow the [instructions for
    QEMU](../variants/qemu_q35/building-manual.md#procedure). Checkout
    `qemu_q35_sovereign_boot-rc3` tag on coreboot repository and use new `qemu_svboot`
    target as an argument to `./build.sh` script.

#### Video demonstration

Watch a short demonstration of Sovereign Boot Wizard in action. This video
covers the new features of the Sovereign Boot Wizard and complements the
documentation.

<div class="video-wrapper">
  <iframe
    src="https://www.youtube.com/embed/z316ml12hm8?si=xxeA4XMQt8Lnevr4"
    title="Sovereign Boot Wizard RC3 Demo"
    frameborder="0"
    allow="accelerometer; autoplay;
      clipboard-write; encrypted-media;
      gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

### RC2 - 2025-07-31

#### Added

* Parsing of signatures embedded into boot options:
    + Enumerating all signatures present in the image
    + Certificate chain enumeration for each signature
    + Certificate validity time checks
    + Signature integrity checks against the image hash
    + Check for certificate/hash presence in DB and DBX
* Calculation of image and certificate SHA256 hashes
* Detection of unsigned images and displaying their hashes
* Parsing DER encoded X509 certificates and exposing the information in
  human-readable format
* Enrolling the certificates and image hashes to DB/DBX
* Ephemeral PK enrollment to finalize provisioning of Sovereign Boot
* Option to skip trust decision for a certificate or image

#### Known issues

* [Measured boot reports volume full error when chaining EFI binary from the
  Sovereign Boot Provisioning
  Wizard](https://github.com/Dasharo/dasharo-issues/issues/1479)
* [UEFI Secure Boot variables protection not yet tested](https://github.com/Dasharo/dasharo-issues/issues/1478)

#### SBOM

* [coreboot based on 24.12 revision qemu_q35_sovereign_boot-rc2](https://github.com/Dasharo/coreboot/tree/qemu_q35_sovereign_boot-rc2)
    + [License](https://github.com/Dasharo/coreboot/blob/qemu_q35_sovereign_boot-rc2/COPYING)
* [Dasharo EDKII fork based on edk2-stable202502 revision sovereign-boot-rc2](https://github.com/Dasharo/edk2/tree/sovereign-boot-rc2)
    + [License](https://github.com/Dasharo/edk2/blob/sovereign-boot-rc2/License.txt)

#### Building

Follow the [instructions for
QEMU](../variants/qemu_q35/building-manual.md#procedure). Checkout
`qemu_q35_sovereign_boot-rc2` tag on coreboot repository and use new
`qemu_svboot` target as an argument to `./build.sh` script.

#### Testing

Currently implemented set of functionalities can be validated using
[OSFV](https://github.com/Dasharo/open-source-firmware-validation).

1. Clone the repository and checkout the revision with tests:

    ```bash
    git clone https://github.com/Dasharo/open-source-firmware-validation.git
    git checkout sovereign-boot-rc2
    ```

2. Set up the testing environment as described in
   [README.md](https://github.com/Dasharo/open-source-firmware-validation?tab=readme-ov-file#initializing-environment).
3. Download the `qemu_q35.rom` binary from [Binaries section](#binaries) and
   place it in the `open-source-firmware-validation` directory.
4. Obtain the DTS v2.5.0 image from the [DTS release
   page](https://github.com/Dasharo/meta-dts/releases) and place it, e.g. in
   `$HOME` directory.
5. Obtain the Sovereign Boot [test data
   image](https://cloud.3mdeb.com/index.php/s/DxMziEtRmpdwqBK/download)
   (`svboot_test_data.img`) and place it, e.g. in `$HOME` directory.
6. Start the QEMU with the following command in separate window/tab in the
   `open-source-firmware-validation` directory:

    ```bash
    HDD_PATH=~/dts-base-image-v2.5.0.wic HDD2_PATH=~/svboot_test_data.img \
      ./scripts/ci/qemu-run.sh graphic os
    ```

7. Start the new test cases in the window where test environment was prepared:

    ```bash
    robot -L TRACE -v rte_ip:127.0.0.1 -v snipeit:no -v config:qemu \
      -t "SVB004*" dasharo-security/sovereign-boot.robot
    ```

#### Video demonstration

Watch a short demonstration of Sovereign Boot Wizard in action. This video
covers the new features of the Sovereign Boot Wizard and complements the
documentation.

<div class="video-wrapper">
  <iframe
    src="https://www.youtube.com/embed/jaDbdBFU1KI?si=lpiHDN3-MLXhmTRB"
    title="Sovereign Boot Wizard RC2 Demo"
    frameborder="0"
    allow="accelerometer; autoplay;
      clipboard-write; encrypted-media;
      gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>

### RC1 - 2025-06-30

#### Added

* First engineering release of the Sovereign Boot Provisioning Wizard
* Basic parsing of boot options: displaying description, hardware path and file path
* Integration of the Sovereign Boot Provisioning Wizard into UEFI Boot Manager:
    + wizard is invoked during boot when system is unprovisioned
    + wizard is invoked when system is provisioned and the boot option does not
      pass the UEFI Secure Boot verification
* Integration of the Sovereign Boot Provisioning Wizard into UEFI firmware
  setup:
    + wizard can be disabled/enabled in the UEFI Secure Boot Configuration menu
    + wizard can be manually invoked from the UEFI Secure Boot Configuration menu
    + disabling the wizard causes to reset the UEFI Secure Boot keys to defaults

#### SBOM

* [coreboot based on 24.12 revision qemu_q35_sovereign_boot-rc1](https://github.com/Dasharo/coreboot/tree/qemu_q35_sovereign_boot-rc1)
    + [License](https://github.com/Dasharo/coreboot/blob/qemu_q35_sovereign_boot-rc1/COPYING)
* [Dasharo EDKII fork based on edk2-stable202502 revision sovereign-boot-rc1](https://github.com/Dasharo/edk2/tree/sovereign-boot-rc1)
    + [License](https://github.com/Dasharo/edk2/blob/sovereign-boot-rc1/License.txt)

#### Building

Follow the [instructions for
QEMU](../variants/qemu_q35/building-manual.md#procedure) (`qemu_full` target).

#### Testing

Currently implemented set of functionalities can be validated using
[OSFV](https://github.com/Dasharo/open-source-firmware-validation).

1. Clone the repository and checkout the revision with tests:

    ```bash
    git clone https://github.com/Dasharo/open-source-firmware-validation.git
    git checkout fce9dbc78007fb94c23070974834e47784205af4
    ```

2. Set up the testing environment as described in [README.md](https://github.com/Dasharo/open-source-firmware-validation?tab=readme-ov-file#initializing-environment).
3. Download the `qemu_q35.rom` binary from [Binaries section](#binaries) and
   place it in the `open-source-firmware-validation` directory.
4. Obtain the DTS v2.5.0 image from the [DTS release
   page](https://github.com/Dasharo/meta-dts/releases) and place it, e.g. in
   `$HOME` directory.
5. Start the QEMU with the following command in separate window/tab in the
   `open-source-firmware-validation` directory:

    ```bash
    HDD_PATH=~/dts-base-image-v2.5.0.wic ./scripts/ci/qemu-run.sh graphic os
    ```

6. Start the test suite in the window where test environment was prepared:

    ```bash
    robot -L TRACE -v rte_ip:127.0.0.1 \
        -v snipeit:no -v config:qemu \
        dasharo-security/sovereign-boot.robot
    ```

#### Video demonstration

Watch a short demonstration of Sovereign Boot Wizard in action. This video
covers basic usage of the Sovereign Boot Wizard and complements the
documentation.

<div class="video-wrapper">
  <iframe
    src="https://www.youtube.com/embed/sCohCVvcp7E?si=bgJkdJwGFHY0u_9I"
    title="Sovereign Boot Wizard RC1 Demo"
    frameborder="0"
    allow="accelerometer; autoplay;
      clipboard-write; encrypted-media;
      gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin"
    allowfullscreen>
  </iframe>
</div>
