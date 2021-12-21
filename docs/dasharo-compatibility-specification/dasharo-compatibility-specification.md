# Dasharo compatibility test specification

Each time the firmware release procedure is preceded by the validation procedure.
Its main tasks are: 
* make sure, that the new firmware meets the requirements related to current
    stage acceptance criteria,
* make sure, that add new features don't affect with damaging the old ones.

Validation procedure is carried out on a specially laboratory stand designed
for this purpose by performing the specific set of tests. Test are performed
on the basis of the automated infrastructure - this provides their greater
stability and repeatability. Any automated test was witten based on the test
documentation, which is publicly available in this section.

## Dasharo compatibility test infrastruture

[To add: regression testing architecture]

## Dasharo compatibility modules

Tests preformed during validation procedure can be divided into test modules, 
test suites and test cases.

Test cases are the smallest component of validation procedure. Their task is
to check, that the given functionallity works properly under a certain 
conditions. 

Test suites group test cases related to the given functionality, while test
modules groups test cases related to the similar functionalities (i. e. test
suites which task is to check if differently OS boot properly on the platform).

Currently in Dasharo test specification the following test groups can be
distinguished:
* Dasharo flashing (which contains test suites related to firmware building
    and platform flashing with the firmware),
* Dasharo Security (which contains test suites related to the platform
    security and supporting security modules),
* Dasharo Compatibility (which contains test suites not related to another test
    groups or their presence for a given platform is required by the customer).


## Dasharo compatibility test matrix

The test matrix decribes, which test cases and test suites are compatible with
a given device or group of devices. If the given test is compatible with the
platform, the customer might be sure, that before releasing the new firmware
version this test was executed and its result might be read from the
spreadsheet with test results. Also, log from the test might be obtained
from `release` section.

The test matrix is available under the following 
[link](https://docs.google.com/spreadsheets/d/1MPbz8OIDuuErZOHdnkxZnUo4snLptQU_mBKat3H2Mow/edit?usp=sharing).