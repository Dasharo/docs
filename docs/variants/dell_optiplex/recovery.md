# Recovery

Following procedure describe how to recover Dell OptiPlex 7010/9010 SFF from
[brick state](https://en.wikipedia.org/wiki/Brick_(electronics)).

We recommend to use 3mdeb Remote Test Environment bundle, which can be bought
in our [shop](), but other methods like use of CH341 or Raspberry Pi as SPI
programming tool also may work.

## Taking apart

Let's start with getting access to SPI chips so we can hook Pomona clips.

### Open case

![type:video](https://www.youtube.com/embed/ohZDMtBGsQw)

### Remove heatsink

![type:video](https://www.youtube.com/embed/TiUSTo-XwPo)

## Hooking RTE

* Prepare Pomona wires

* Connect SOIC-16 Pomona to RTE

* Disconnect hardware
