# Laboratory stand dedicated to [DEVICE_NAME] assembly guide

## Introduction

This document describes the assembly procedure dedicated to [DEVICE_NAME]
testing stand.

## Prerequisites

The below table contains information about all elements which are needed to
create the testing stand.

* [device]
* [element1]
* [element2]

## Pre-setup activities

The following subsections describe the method of preparing all the
components of the laboratory stand.

### [DEVICE_NAME]

[DEVICE_NAME] platform should be prepared in accordance with the
[Assembly](some.md#some-section) documentation.

### [EG.] RTE

RTE (acronym: Remote Testing Environment) should be prepared in accordance with
[Quick start guide](../rte/v1.1.0/quick-start-guide.md) documentation dedicated
to the device.

### [EG.] Sonoff

Sonoff should be prepared in accordance with
[Quick start guide](../sonoff/quick-start-guide.md) documentation dedicated to
the device.

## Connections

The following sections describe how to enable all of the following features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* external flashing with the RTE.
* [optional-connections] eg:

    - Sonoff connections,
    - piKVM connections,
    - can output/intput,
    - ethernet connection.

### Serial connection

<!--This section should contain neccesary connections to establish serial
connections between the device and RTE-->

1. ...
1. ...

### Power supply controlling

<!--This section should contain instruction to connecting power source to the
device-->

1. ...
1. ...

### Basic power operations enabling

<!--This section should contain information about controlling device's power
states and connections using dedicated software/hardware-->

1. ...
1. ...

### External flashing enabling

<!--This section should contain steps to make required connections to further
proceed with external flashing-->

1. ...
1. ...

### Complete Setup

[EXAMPLE:]

After preparing all of the connections also three activities should be
performed to enable all of the test stand features:

1. Connect Sonoff to the mains:

    ![IMG](images/sonoff_connected.jpg)

1. Connect the RTE to the Internet by using the Ethernet cable.
1. Connect the RTE to the mains by using the microUSB 5 V/2 A power supply.
1. [optional-step]

Complete setup should looks as follows:

<!--the `some-image.jpg` should be replaced and presenting photo of fully
connected setup-->

![Complete](images/some-image.jpg)

## Theory of operation

The following sections describe how to use all of the enabled features:

* serial connection to the platform,
* controlling power supply,
* enabling basic power actions with the platform (power off/power on/reset),
* [optional-features]

### Serial connection

The method of setting and using serial connection is described in the
[Serial connection guide](../rte/v1.1.0/serial-port-connection-guide).

### [Eg-for-sonoff] Power supply controlling

Power supply controlling (in this case: controlling the state of Sonoff)
should be performed based on the `sonoff.sh` script implemented in `meta-rte`
(OS image dedicated to the RTE platform).

[Sonoff power supply controlling](../sonoff/quick-start-guide.md#power-supply-controlling).

### [EG-for-RTE-ctrl]Basic power operations

Basic power operations should be performed based on the `rte_ctrl` script
implemented in `meta-rte` (OS image dedicated to the RTE platform). To perform
basic power operations use the below-described commands:

[RTE Basic power operations](../rte/v1.1.0/quick-start-guide.md#basic-power-operations).

> Note, that in order for the above commands to work properly, the platform
should be powered up: both Sonoff and the power supply must be turned on.

### External flashing

1. ...
1. ...
