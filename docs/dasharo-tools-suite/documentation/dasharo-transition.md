# Dasharo firmware transition

This document describes Dasharo Firmware transition via DTS. The transition can
only be done from a specific firmware to a specific firmware only for a limited
set of platforms. For supported platforms and firmwares check [this
page](./supported-hardware-workflows.md).

Currently supported platforms and transitions:

* PC Engines apu2/3/4/6: transition from [Dasharo
  (coreboot+Seabios)](../../variants/pc_engines/releases_seabios.md) to [Dasharo
  (coreboot+UEFI)](../../variants/pc_engines/releases_uefi.md).

## The workflow

Firstly, boot to DTS as described in [running DTS documentation](./running.md).
Then, if your paltform and firmware support the transition - you should see
`6) Transition Dasharo Firmware` option. After presssing `6` you should see DTS
transition process. After the transition your paltform will reboot
automatically. Here is an example:

```bash
 Dasharo Tools Suite Script 2.5.0 
 (c) Dasharo <contact@dasharo.com> 
 Report issues at: https://github.com/Dasharo/dasharo-issues 
*********************************************************
**                HARDWARE INFORMATION 
*********************************************************
**    System Inf.: PC Engines apu3
** Baseboard Inf.: PC Engines apu3
**       CPU Inf.: AMD GX-412TC SOC                               
**    RAM DIMM 0: Not Specified
*********************************************************
**                FIRMWARE INFORMATION 
*********************************************************
** BIOS Inf.: coreboot v24.08.00.01
*********************************************************
**                DPP credentials 
*********************************************************
**      Email: ***************
**   Password: ***************
*********************************************************
**     1) Dasharo HCL report
**     2) Update Dasharo Firmware
**     3) Restore firmware from Dasharo HCL report
**     4) Edit your DPP keys
**     6) Transition Dasharo Firmware
*********************************************************
R to reboot  P to poweroff  S to enter shell  
K to launch SSH server  L to disable sending DTS logs 
C to display DPP credentials 

Enter an option:
6
Gathering flash chip and chipset information...
Chipset found
vendor="Winbond" name="W25Q64BV/W25Q64CV/W25Q64FV"
Chipset size
8M
Waiting for network connection ...
Network connection have been established!
Downloading board configs repository
Checking if board is Dasharo compatible.
Waiting for system clock to be synced ...

Please, select Dasharo firmware version to install:

  d) DPP version (coreboot + UEFI)
  b) Back to main menu

Enter an option: d

Subscription version (cooreboot + EDK2) selected
Downloading Dasharo firmware...
Checking Dasharo firmware checksum... Verified.


Please verify detected hardware!

Board vendor: PC Engines
System model: apu3
Board model: apu3

Does it match your actual specification? (Y|n) y

Following firmware will be used to deploy Dasharo:
Dasharo BIOS firmware:
  - link: dasharo-pcengines-uefi/v0.9.0/pcengines_apu3_v0.9.0.rom
  - hash: ae4f2cd5f3b2cd18e665e24ad48b2e623bb70cd2d9f7e7f647ca275bee2e4f21

You can learn more about this release on: https://docs.dasharo.com/

Do you want to deploy this Dasharo Firmware on your platform (Y|n) y

Found file config at 0x1eae40, type raw, compressed 3854, size 12269
Transitioning Dasharo firmware...
Successfully transitioned Dasharo firmware
Syncing disks... Done.
The computer will reboot automatically in 5 seconds
Rebooting in 5 s:
5...
4...
3...
2...
1...
Rebooting
```
