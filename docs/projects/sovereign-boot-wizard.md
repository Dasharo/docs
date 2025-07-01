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

## Releases

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

#### Binaries

[qemu_q35.rom](https://cloud.3mdeb.com/index.php/s/5ttD8Fd5TjWcqfa/download){.md-button}
[sha256](https://cloud.3mdeb.com/index.php/s/7x3HpsCBJFgmbQM/download){.md-button}

#### SBOM

* [coreboot based on 24.12 revision qemu_q35_sovereign_boot-rc1](https://github.com/Dasharo/coreboot/tree/qemu_q35_sovereign_boot-rc1)
    + [License](https://github.com/Dasharo/coreboot/blob/qemu_q35_sovereign_boot-rc1/COPYING)
* [Dasharo EDKII fork based on edk2-stable202408.01 revision sovereign-boot-rc1](https://github.com/Dasharo/edk2/tree/sovereign-boot-rc1)
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
