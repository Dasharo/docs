# Deployment

Deployment section of Dasharo Knowledge Base FAQ considers topic of open-source
firmware deployment, which may include operations of reading and writing SPI NOR
flash, as well as binary modifications.

If you can't find the answer to your questions feel free to contact us through
[Community Channels](../index.md#community) or submit issue through [Dasharo
Github](https://github.com/Dasharo/dasharo-issues).

## Flashrom

Following sections explain how to deal with most common `flashrom` problem.

### How to install Dasharo flashrom fork ?

Following procedure is for advanced users who are familiar with
source compilation and can resolve potential missing depenencies or
other typical compilation problems. If you are not familar with
compilation from source we recommend use of Dasharo Tools Suite,
which is minimal Linux environment to deploy, update, and maintain
firmware on Dasharo-supported devices. Please follow [DTS
documentation](../../dasharo-tools-suite/overview). Otherwise please follow compilation procedure.

Currently, the latest flashrom release lacks support for Alder Lake
S and Comet Lake U internal flashing. Because of this, we need to
build flashrom from [Dashro
fork](https://github.com/Dasharo/flashrom/tree/dasharo-release).
The procedure was tested on [Ubuntu 22.04 desktop amd64
ISO](https://releases.ubuntu.com/22.04/ubuntu-22.04.1-desktop-amd64.iso)
burned on the USB stick. It may work on other Debian-based distributions.

Boot the Ubuntu live image and select the `Try Ubuntu` option. Open a terminal
and proceed with the commands below.

Install build dependencies:

```bash
sudo apt-get update
sudo apt-get install git build-essential pkg-config libpci-dev udev
```

Obtain source code:

```bash
git clone https://github.com/Dasharo/flashrom.git -b dasharo-release
cd flashrom
```

Build and install flashrom:

```bash
sudo make install
```

### Perform dry run to detect the problems early

Most of the problems can be detected early and avoided without attempting to
flash the firmware. You may check for most of the errors described here by
doing a dry run (not passing any firmware binary):

```bash
sudo flashrom -p internal
```

In below sections there are example errors that you may find in the output of
above command.

### `Could not get I/O privileges (Operation not permitted)`

If you see a flashrom error like this:

``` console
ERROR: Could not get I/O privileges (Operation not permitted).
You need to be root.
Error: Programmer initialization failed.
```

It means you have insufficient privileges to perform initialization. Please use
`sudo` before `flashrom` command.

### `/dev/mem mmap failed: Operation not permitted`

``` console
/dev/mem mmap failed: Operation not permitted
FAILED!
FATAL ERROR!
Error: Programmer initialization failed.
```

Linux kernel restricts access to IOMEM. To fix that add `iomem=relaxed` to the
kernel command line.

Recommended way to fix the problem:

* Edit `/etc/default/grub`:

  ``` bash
  GRUB_CMDLINE_LINUX="iomem=relaxed"
  ```

* Update GRUB2 config with:

  ``` bash
  sudo update-grub2
  ```

* Alternatively, if previous command doesn't work:

  ``` bash
  sudo grub-mkconfig -o /boot/grub/grub.cfg
  ```

* Reboot and try `flashrom` command again

Other method:

* Edit `grub.cfg` in `/boot/grub/`:

  ``` bash
  linux /boot/vmlinuz-4.15.0-115-generic ro quiet iomem=relaxed
  ```

* Reboot and try `flashrom` command again

Last resort you can try to modify boot option runtime. YMMV:

* If your computer uses BIOS for booting, then hold down the ++shift++, or if
  your computer uses UEFI for booting, press ++esc++ several times, while GRUB
  is loading to get the boot menu. And, after getting a GRUB menu, press ++e++
  on a boot entry to append `iomem=relaxed` to kernel command line and press
  ++ctrl+x++ or ++f10++ to boot. Although this setting is temporary and will
  last only during the next boot, this way is faster and a customer doesn't
  need to re-generate anything.

Please note having it as a temporary setting maybe is slightly better for security
_(there's a reason why it's disabled by default)_.

If the above does not resolve the problem, the kernel may be compiled with strict
devmem, which prohibits accessing the IOMEM. You should then take different
Linux system.

### `Transaction error between offset ...`?

``` console
SPI Configuration is locked down.
FREG0: Flash Descriptor region (0x00000000-0x00000fff) is read-only.
FREG2: Management Engine region (0x00005000-0x005fffff) is locked.
Not all flash regions are freely accessible by flashrom. This is most likely
due to an active ME. Please see https://flashrom.org/ME for details.
At least some flash regions are read protected. You have to use a flash
layout and include only accessible regions. For write operations, you'll
additionally need the --noverify-all switch. See manpage for more details.
Enabling hardware sequencing due to multiple flash chips detected.
OK.
Found Programmer flash chip "Opaque flash chip" (12288 kB, Programmer-specific) mapped at physical address 0x0000000000000000.
Reading flash... Transaction error between offset 0x00005000 and 0x0000503f (= 0x00005000 + 63)!
Read operation failed!
FAILED.
```

Most probably it means problem lays in ME not allowing to read its region. One
of the method to mitigate the issues is to put ME in Manufacturing Mode. Such
operation depends on ME version, SPI flash layout and platform design. Detail
information you should find in sections dedicated to given hardware. To access
documentation for supported hardware please go to [Hardware Compatibility
List](../variants/hardware-compatibility-list.md).

Please note we consider further mitigations in [Dasharo Roadmap](../ecosystem/roadmap.md).

### `WARNING: No chipset found`

If you see the following in the flashrom output:

```txt
WARNING: No chipset found. Flash detection will most likely fail.
No EEPROM/flash device found.
Note: flashrom can never write if the flash chip isn't found automatically.
```

that means your flashrom version is incorrect. Follow the procedure of
[building flashrom](#how-to-install-dasharo-flashrom-fork) or use
[DTS](../../dasharo-tools-suite/overview).

### Chip write protection enabled

If you see anything like this in the flashrom output (or similar, the hex
number may differ):

```txt
PR0: Warning: 0x001c0000-0x01ffffff is read-only.
```

That means you did not disable `BIOS boot medium lock` correctly. GO back to
firmware setup and disable the option as described in
[Prerequisites](#prerequisites). Flashrom update procedure containing
`--ifd -i bios` parameters will fails if you do not disable the protection.
The procedure using the `--fmap -i RW_SECTION_A -i RW_SECTION_B` parameters
is not affected.

### `Warning: BIOS region SMM protection is enabled!`

If you see anything like this in the flashrom output (or similar, the hex
number may differ):

```txt
Warning: BIOS region SMM protection is enabled!
Warning: Setting Bios Control at 0xdc from 0xaa to 0x89 failed.
New value is 0xaa.
```

Any attempt to flash the firmware will fail. That means you did not disable
`Enable SMM BIOS write protection` option correctly. Go back to firmware setup
and disable the option as described in [Prerequisites](#prerequisites).

## How to use flashrom to backup vendor BIOS?

<!-- BIOS backup section is very generic and should be treated as such.
This section even can be replaced with Dasharo Tools Suite, fwupd, or other
tools that can simplify the operation for the user -->

It is always a good idea to backup the original BIOS of your hardware, before
switching to open-source firmware.

* Boot [Dasharo Tools Suite](../../../dasharo-tools-suite/documentation#bootable-usb-stick)
* Choose option 9) Shell.
* Read content of SPI NOR flash:

  ``` console
  flashrom -p internal -r bios_backup_`date +%Y%m%d`.bin

  flashrom v1.2-551-gf47ff31 on Linux 5.10.0-9-amd64 (x86_64)
  flashrom is free software, get the source code at https://flashrom.org

  Using clock_gettime for delay loops (clk_id: 1, resolution: 1ns).
  Found chipset "Intel Q77".
  Enabling flash write... SPI Configuration is locked down.
  The Flash Descriptor Override Strap-Pin is set. Restrictions implied by
  the Master Section of the flash descriptor are NOT in effect. Please note
  that Protected Range (PR) restrictions still apply.
  Enabling hardware sequencing due to multiple flash chips detected.
  OK.
  Found Programmer flash chip "Opaque flash chip" (12288 kB, Programmer-specific) mapped at physical address 0x0000000000000000.
  Reading flash... done.
  ```

If you face any issues, please refer to the troubleshooting section for
hardware platform.
