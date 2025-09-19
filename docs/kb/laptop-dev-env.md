# NovaCustom laptop development environment

This document describes the process of configuring a development and debugging
environment for NovaCustom laptops.

The instruction is applicable for PCs running Fedora. If you're using a
different distro, some commands (e.g. package installation) may be different.

## Embedded Controller

This section describes the development environment for EC firmware on NovaCustom
devices. The Embedded Controller firmware is heavily based on
[System76 EC](https://github.com/system76/ec) firmware and makes use of
open-source debugging tools and software also developed by System76.

### Flashing

This section outlines the parts and software needed to perform external flashing
of the Embedded Controller.

<!-- markdownlint-disable MD013 -->
<!-- Need to have full-size grid table for the renderer to pick it up -->
+------------+-----------------------------------------+---------------------------------------+
|    Size    |             14 inch models              |         15 and 16 inch models         |
+============+=========================================+=======================================+
| Programmer | Arduino Mega 2560                       | Arduino Mega 2560                     |
+------------+-----------------------------------------+---------------------------------------+
| Adapter    | 2x12 pin 2.54mm to 24 pin **0.5mm** FFC | 2x12 pin 2.54mm to 24 pin **1mm** FFC |
+------------+-----------------------------------------+---------------------------------------+
| Cables     | **FFC 0.5mm pitch 24 pin**              | **FFC 1.0mm pitch 24 pin**            |
|            |                                         |                                       |
|            | USB-A to USB-B                          | USB-A to USB-B                        |
|            |                                         |                                       |
|            | USB-C to USB-C                          | USB-C to USB-C                        |
+------------+-----------------------------------------+---------------------------------------+
| Software   | ecflash                                 | ecflash                               |
+------------+-----------------------------------------+---------------------------------------+
<!-- markdownlint-enable MD013 -->

#### Preparation

1. Obtain a copy of the EC firmware and tools:

    ```bash
    git clone https://github.com/Dasharo/ec.git
    cd ec
    git submodule update --init --checkout
    ./scripts/deps.sh
    ```

1. Follow the on-screen instructions to finish configuring your development
environment.
1. Connect the Arduino to your workstation with a USB-A to USB-B cable. Do not
connect the target laptop yet.
1. Flash the Arduino with debugger firmware:

    ```bash
    make BOARD=arduino/mega2560
    make BOARD=arduino/mega2560 flash
    ```

1. In the EC directory, build the EC flashing application:

    ```bash
    cargo build --manifest-path ecflash/Cargo.toml --example isp --release
    ```

#### Flash the target laptop

1. Connect the Arduino to the target laptop with the appropriate FFC cable for
   your model. If the cable is narrower than the socket on the laptop, align the
   cable and socket to pin 0 (to the left).
1. Connect a second cable (e.g. USB-C to USB-C) from the workstation to the
   target - this cable is needed provide grounding.
1. Flash the target:

    ```bash
    sudo ecflash/target/release/examples/isp [path/to/firmware.rom]
    ```

##### Troubleshooting

In case flashing fails, try the following:

- Try running the command again, sometimes it starts working on the third
  attempt
- Try another grounding cable, USB-A to USB-C, or even HDMI to HDMI have been
  shown to work
- Try with / without the internal battery connected
- Try with / without the AC adapter connected
- Try plugging in the AC adapter right before / after running the command (last
  resort)

### Building

Build EC firmware:

```bash
make BOARD=your/board
```

### Debugging

#### Build EC firmware with debugger support enabled

1. In file `src/board/system76/common/common.mk`, enable parallel port debugging
    and choose the log level to get the verbosity you need:

    ```makefile
    # Set log level
    # 0 - NONE
    # 1 - ERROR
    # 2 - WARN
    # 3 - INFO
    # 4 - DEBUG
    # 5 - TRACE
    CFLAGS+=-DLEVEL=4

    # Uncomment to enable debug logging over keyboard parallel port
    CFLAGS+=-DPARALLEL_DEBUG

    # Uncomment to enable I2C debug on 0x76
    #CFLAGS+=-DI2C_DEBUGGER=0x76
    ```

1. Build firmware for the target:

    ```bash
    make BOARD=your/board
    ```

    |   Model   |        BOARD        |
    | --------- | ------------------- |
    | NV4xMZ/MB | novacustom/nv4x_tgl |
    | NS5xMU    | novacustom/ns5x_tgl |
    | NS7xMU    | novacustom/ns5x_tgl |
    | NV4xPZ    | novacustom/nv4x_adl |
    | NS7xPU    | novacustom/ns5x_adl |
    | V540TU    | novacustom/v540tu   |
    | V560TU    | novacustom/v560tu   |
    | V540TNx   | novacustom/v540tnx  |
    | V560TNx   | novacustom/v560tnx  |

1. Disconnect power from the target.

1. Flash the firmware to the target:

    ```bash
    make BOARD=your/board flash_external
    # or
    sudo ecflash/target/release/examples/isp path/to/your/ec.rom
    ```

1. Start the console:

    ```bash
    make BOARD=your/board console_external
    ```

1. Connect power to the target.

1. Power on the target and observe the console for logs.

## BIOS

This section describes the development environment for x86 firmware on
NovaCustom devices.

### Flashing

This section outlines the parts and software needed to perform external flashing
of the BIOS.

BIOS flashing is the same as with other platforms, except on ADL and MTL models,
where the BIOS chip has a WSON-8 form factor. The following table of specs is
provided for convenience:

| CPU generation | Tiger Lake | Alder Lake | Meteor Lake |
| --- | --- | --- | --- |
| Programmer | CH341a | CH341a | **CH341a v1.2 with voltage switch** |
| Probe | SOIC-8 | **WSON-8** | **WSON-8** |
| Voltage | 3.3v | 3.3v | **1.8v** |
| Software | flashrom | flashrom | flashrom |

Use flashrom with the CH341a programmer:

```bash
flashrom -p ch341a --ifd -i bios -w [path/to/coreboot.rom]
```

### Building

Please refer to the [NovaCustom building manual](../unified/novacustom/building-manual.md).

### Debugging

Laptop firmware debugging is made difficult by the lack of user-accessible
serial ports or other debug facilities. On NovaCustom laptops, we may gain
serial console output from coreboot by sending it through the EC, to the EC
debugger.

#### Requirements

- Target flashed with debug EC firmware
- EC debugger connected to the target

#### Enabling EC console redirection

##### coreboot

1. Open your coreboot menuconfig
1. Go to the `Console` menu and enable `System76 EC console output`:

    ```text
    [...]
    [ ] SMBus console output
    [*] System76 EC console output
        Default console log level (7: DEBUG)  --->
    [*] Use loglevel prefix to indicate line loglevel
    [*] Use ANSI escape sequences for console highlighting
    [...]
    ```

##### edk2

1. Open your coreboot menuconfig
1. Go to the `Payload` menu
1. Set `edk2 build` to `Generate edk2 debug build`:

    ```text
    [...]
    (3323ed481d35096fb6a7eae7b49f35eff00f86cf) Insert a commit's SHA-1 or a branch name
      edk2 build (Generate edk2 debug build)  --->
    (3rdparty/dasharo-blobs/novacustom/bootsplash.bmp) edk2 Bootsplash path and filename
    [...]
    ```

1. Go to the `Dasharo specific payload options` submenu
1. Select `Enable edk2 logging to System76 EC`

    ```text
    [*] Enable edk2 logging to System76 EC
    [*] Skip PS/2 keyboard detection check
    [*] Include iPXE in edk2 payload
    [...]
    ```

#### Capturing logs

Open your EC debug console and observe the console output. You should see
coreboot and edk2 debug messages on your console.
