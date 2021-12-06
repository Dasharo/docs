# Deployment

Deployment section of Dasharo Knowledge Base FAQ consider topic of open source
firmware deployment, what may include operations of reading and writing SPI NOR
flash, as well as binary modifications.

If you can't find the answer to your questions feel free to contact us through
[Community Channels](../index.md#community) or submit issue through [Dasharo
Github](https://github.com/Dasharo/dasharo-issues).

## What to do when flashrom returns `Could not get I/O privileges (Operation not permitted)`?

If you see a flashrom error like this:

``` console
ERROR: Could not get I/O privileges (Operation not permitted).
You need to be root.
Error: Programmer initialization failed.
```

It means you have insufficient privileges to perform initialization. Please use
`sudo` before `flashrom` command.

## What to do when flashrom returns `/dev/mem mmap failed: Operation not permitted`?

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

Please note we consider further mitigations in [Dasharo Roadmap](../ecosystem/roadmap.md).
