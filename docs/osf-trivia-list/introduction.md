# Open Source Firmware Trivia Questions List (OSFTQL)

Goal of following questions list is to provide answers to terribly trivial
topics or questions that were asked and answered gazillion times. We believe to
move forward with so limited resources we have to stop wasting community
precious time on something we agree on, but move forward with discussion.

Other role of this list is to create taxonomy of OSF trivia questions for
community and Dasharo customers, to avoid repeating explanation of topics which
most of community already agree on.

<!--

## `[OSFTQL0001]` Where is firmware?

TODO: draw diagram based on famous training materials, that show where we have
firmware and where firmware will be in future

## `[OSFTQL0002]` Will OSF project support device X?

TODO: Explain how wrong is this question and why often there is no answer to it
on mailing list.

-->

## `[OSFTQL0003]` Binary blobs - what are they? What do we need them for?

Binary blobs are a term referring to proprietary, closed-source software
components. They are called "blobs" because, unlike open-source code, you can't
see their internal structure, nor verify their security; they are an
undifferentiated mass (or "blob") of binary data. While often frowned upon in
the Open Source community for being inauditable and suspicious, some are
required by coreboot for most of the recent platforms.
Here are some common types of binary blobs you might encounter when working
with coreboot:

* **CPU Microcode:**
    - Modern CPUs often require microcode updates to fix bugs or security
   vulnerabilities. These microcode updates are usually distributed as binary
   blobs.

* **Memory Initialization:**
    - Some platforms require binary blobs for memory initialization. The code
   that sets up the RAM is sometimes provided only in binary form by the
   hardware manufacturer.

* **Video BIOS:**
    - The video BIOS (VBIOS) is a piece of firmware that initializes the
   graphics hardware. In some cases, the VBIOS might be required to get
   graphical output during the boot process.

* **Management Engine (ME) Firmware (Intel platforms):**
    - Intel's Management Engine is a controversial component required for
   Intel systems to boot. It requires a binary blob.

* **Platform Security Processor (PSP) Firmware (AMD platforms):**
    - Similar to Intel's ME, AMD's Platform Security Processor (PSP) requires
   binary firmware to function.

* **Firmware Support Package (FSP) (Intel platforms):**
    - Intel provides a Firmware Support Package (FSP) which is a binary blob
   used to initialize the processor, memory, and chipset on some Intel
   platforms.

* **Embedded Controller (EC) Firmware:**
    - The firmware for the embedded controller (which handles things like
   power management, fan control, etc.) may also be a binary blob.

To see in fine detail which are required for your platform of interest,
please refer to
[this coreboot wiki page](http://web.archive.org/web/20240903193137/https://www.coreboot.org/Binary_situation).
