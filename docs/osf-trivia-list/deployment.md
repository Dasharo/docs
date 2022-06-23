# Deployment

Deployment section of Dasharo Knowledge Base FAQ considers topic of open-source
firmware deployment, which may include operations of reading and writing SPI NOR
flash, as well as binary modifications.

If you can't find the answer to your questions feel free to contact us through
[Community Channels](../index.md#community) or submit issue through [Dasharo
Github](https://github.com/Dasharo/dasharo-issues).

## Flashrom

Following sections explain how to deal with most common `flashrom` problem.

### How to install flashrom ?

* Install flashrom v1.1 or newer with your distribution's package manager if
  you don't have it installed yet. If your distro doesn't provide flashrom or
  provides an outdated one, you can build it yourself using
  [this instruction](https://www.flashrom.org/Downloads).
* Or compile recent version of flashrom:

  ``` console
  sudo apt install libpci-dev libftdi-dev libusb-1.0-0-dev
  git clone https://github.com/flashrom/flashrom.git
  cd flashrom
  sudo make install
  ```

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
