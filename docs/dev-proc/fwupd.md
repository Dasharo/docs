# fwupd and LVFS

## Introduction

This document describes the process for generating fwupd cabinet files,
uploading them to LVFS, and serving them to end-users.

## Prerequisites

fwupd integration depends on the capsule update protocol being implemented for
the platform. Please make sure capsule update is enabled and functional on the
platform before proceeding with fwupd integration.

## Building a cabinet

fwupd uses cabinet archives (.cab files) for storing firmware and its metadata.
A cabinet contains, at minimum:

- The firmware binary (in our case, this will be the capsule update file)
- A small XML file with metadata (including the update protocol and GUID of the
  device)

For coreboot, a helper script to automate cabinet generation is provided in the
coreboot repo's root directory.

First, start by building the capsule file:

```bash
./capsule.sh make -t keys/TestRoot.pub.pem \
                  -o keys/TestSub.pub.pem \
                  -s keys/TestCert.pem -b
Overwrite already existing 'novacustom-mtl-h-v1.0.0-rc2.cap'? [y/N] y
Created the capsule at 'novacustom-mtl-h-v1.0.0-rc2.cap'
```

Now prepare the cabinet:

```bash
./capsule_cabinet.sh novacustom-mtl-h-v1.0.0-rc2.cap
File novacustom-mtl-h-v1.0.0-rc2.cap.cab created
```

## Local testing

Use fwupdmgr to locally test the cabinet:

```bash
sudo fwupdmgr install novacustom-mtl-h-v1.0.0-rc2.cap.cab --allow-reinstall
[sudo] password for ubuntu:
Waiting…                 [***************************************]
Successfully installed firmware
An update requires a reboot to complete. Restart now? [y|N]:
```

Press `y` to restart and check if the update proceeds without errors.

## Uploading to LVFS

Follow [upstream fwupd documentation](https://lvfs.readthedocs.io/en/latest/upload.html)
for a detailed guide for uploading cabinets to LVFS.
