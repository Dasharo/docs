# Dasharo Test Specifiaction - overview

The release procedure is always preceded by validation procedure. It is done
on the basis of the test documentation, which can be found in this submenu.
To properly use the documentation, it is advisable to read the following
brief description of its components.

## Test Matrix

Test Matrix is the document which shows platform-dedicated test suites and
test cases. Based on it, the customer may scope the checks performed by the
validation team each time before firmware release.

## Generic test setup

Generic test setup is the document which describes all the steps that are
performed before testing the various functionalities.

## Dasharo modules

Tests performed during validation procedure can be divided into test modules,
test suites and test cases.

Test cases are the smallest component of validation procedure. Their task
is to check, that the given functionality works properly under a certain
conditions.

Test suites group test cases related to the given functionality, while
test modules groups test cases related to the similar functionalities
(i. e. test suites which task is to check if differently OS boot properly
on the platform).

Currently in Dasharo test specification the following test modules can
be distinguished:

* `Dasharo Compatibility` which contains test suites related to the basic
    functionailited of the device.
* `Dasharo Security` which contains test suites related to the platform
    security and supporting security modules.
* `Dasharo Performance` which contains test suites related to the platform
    booting performance.

## Supported Operating Systems*

* Windows 11
* Ubuntu 22.04
* Ubuntu Server 22.04 LTS
* Debian 11.0
* Fedora 41
* FreeBSD 13.2
* Proxmox VE 7.4
* OPNsense 23.01
* pfSense CE 2.6.0

`* Unless specified otherwise in the test`
(as of 17 June 2024)
