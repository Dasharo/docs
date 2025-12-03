# Dasharo Beta

## Introduction

This document explains the Dasharo Beta update channel, how to enroll in it and
how to downgrade back to stable.

The Dasharo Beta update channel provides pre-release binaries ready for public
testing by a group of beta testers. These binaries are not thoroughly tested,
but provide a preview of future features and enhancements.

Dasharo Beta is only available for a select group devices. Currently, these
include:

- NovaCustom V540TU
- NovaCustom V560TU

## Joining the beta tester group

Please follow the steps [here](https://docs.dasharo.com/ways-you-can-help-us/#join-dasharo-beta-testing-group)
to join the Dasharo Beta Testing group.

## Enabling

To enable Dasharo Beta updates, execute this command in a terminal:

```bash
fwupdmgr enable-remote lvfs-testing
```

## Checking for updates

To check for updates:

```bash
fwupdmgr refresh
fwupdmgr get-updates
```

> Beta Releases are also announced through the `Dasharo - Beta` channel in the
> Dasharo Matrix Space.

## Updating

To update:

```bash
fwupdmgr update
```

## Downgrading

To downgrade:

```bash
fwupdmgr downgrade
```
