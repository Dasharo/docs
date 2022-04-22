# FAQ

## Will this work on my `MSI PRO Z690-A WIFI DDR5` or `MSI PRO Z690-A DDR5` ?

Not yet. The build is configured for the DDR4 only. It might be extended with
the DDR5 variant in the future. **Do not try that**.

## Will this work on my `MSI PRO Z690-A DDR4` ?

Although we do not own that one and cannot give promises, we believe that it
should work the same as the `MSI PRO Z690-A WIFI DDR4`. This is almost the
same board, just with no WiFi card.

## Can i safely try this on my board?

If you are afraid of bricking the board and have no means of
[recovering from failed installation](../recovery), we **do not recommend**
trying it out until at least the v1.0.0 is released. Recovery process is not
suitable for inexperienced users right now. We will be trying to make it
easier, and if that happens, we may cahnge our recommendation here.

## Can I destroy my hardware by installing this firmware?

We give no warranty, although it is highly unlikely, provided that you use the
supported board model and follow the [installation
manual](../installation-manual). In the worst scenario, you might "brick" the
board, rendering it unbootable. It can be fixed by following the [recovery
procedure](../recovery).

## How can I know if the board is "bricked"?

In such a case, you would get stuck with black screen on the display. There
will be no beeping sounds from the buzzer as well. The only way to get some
information on what's going on in that state is to use the
[Serial header](../development/#hardware-connection) to read out error
information.

## What can be the reason of board "bricking"?

The most common reason would be the fact that you DDR memory modules are not
initializad properly.

The other reason might be improper or interrupted installation. Please make
sure to follow the [Installation Manual](../installation-manual) correctly.

## How can I "unbrick" my board?

Please follow the [recovery procedure](../recovery).

## Which CPUs are supported?

We can say the "supported" one is the one we have verified. It is the
`Intel Core i5-12600K` and you can check that in the
[Hardware Configuration Matrix](../hardware-matrix).

In practice, any Alder Lake-S Processor with integrated GPU
(which means no F-series).

F-series is not supported because currently the PCIe ports are not initialized,
so there is no other way to get video output (or any other signs of system being
functional, unless you have a way to get logging from the
[Serial header](../development/#hardware-connection)) to know that it is
actually working.

12900KS is rather unknown at the moment, because it was released later and may
require more recent microcode.

## Which DDR4 memory modules are supported?

We can say the "supported" one is the one we have verified. It is the
`Kingston Fury Beast KF436C17BBK4/32` part populated in all 4 slots, and you
can check that in the [Hardware Configuration Matrix](../hardware-matrix).

No other memory modules or combination in slots were verified so far. This is
on the roadmap for future releases.

Some mention about the Motherboard Memory Compatibiliy List not applying to
Dasharo due to the differences between IBV modified code and Intel reference
FSP

Maybe linking the PDFs that we had to go though when we picked the memory
modules, since Intel maintains its own FSP compatibility list so we are
expecting those to work. Are those public?

## What is the memory profile?

Currently, Dasharo firmware picks the highest standard SPD Profile, no support
for XMP ones. This means that on the Kingston modules it is actually working at
2400 MHz, but it is expected to work all the way to 3200 MHz.
