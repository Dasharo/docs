# Recovery

---------------------

## **Prequisitions**

1. To proceed with recovery `.rom` file with backup vendor firmware will be
    neccesary eg. `backup.rom`.

    Backup file should be generated before making any changes in device flash
    chip according to documentation in
    [BIOS backup](https://docs.dasharo.com/variants/dell_optiplex/initial-deployment/#bios-backup)
    section.

1. Set jumper according to
    [hardware preparation](https://docs.dasharo.com/variants/dell_optiplex/initial-deployment/#hardware-preparation)

1. Install flashrom using
    [flashrom installation guide](https://docs.dasharo.com/variants/dell_optiplex/initial-deployment/#flashrom-installation)

---------------------

## **Internal flashing**

Flash firmware on you Dell OptiPlex machine using below command:

```bash
sudo flashrom -p internal -i me -w <optiplex_firmware>
```

for example:

```bash
sudo flashrom -p internal -i me -w /tmp/backup.rom
```

output:

```bash
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
Reading ich descriptor... done.
Using regions: "me", "bios".
Reading old flash chip contents... done.
Erasing and writing flash chip... Erase/write done.
Verifying flash... VERIFIED.
```

If you get a warning:

```bash
WARNING! You may be running flashrom on an unsupported laptop.
```

And programmer initialization failed, run command:

```bash
flashrom -p internal:laptop=this_is_not_a_laptop -w /tmp/backup.rom -i me
```

If you have placed the jumper correctly, you should see the following message
in flashrom's output:

```bash
The Flash Descriptor Override Strap-Pin is set. Restrictions implied by
the Master Section of the flash descriptor are NOT in effect. Please note
that Protected Range (PR) restrictions still apply.
```

A newer version of flashrom may not display the warning about unsupported
chipset as it already may be marked as tested. Our team has verified that
the flashrom updates firmware reliably on this chipset.

If you will face any issues please refer to
[troubleshooting section](https://docs.dasharo.com/variants/dell_optiplex/initial-deployment/#troubleshooting).
