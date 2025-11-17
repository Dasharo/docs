# Dasharo Beta

## Introduction

This document explains the Dasharo Beta update channel, how to enroll in it and
how to downgrade back to stable.

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
