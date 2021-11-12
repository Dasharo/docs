# Dasharo Compatibility: generic test setup

## Test setup

Test setup is a set of procedures to be executed before the test execution.
Typically, the same setup can be reused by multiple test cases, so there is no
need to execute the setup actions before each independent case.

### Generic test setup

#### Firmware

1. Obtain `FIRMWARE` binary
    1. you can download it from [release](../release.md)
       section
    1. or you can build one yourself as shown in the
       [Building manual](../building-manual.md) section
1. Flash `FIRMWARE` binary to the DUT
    1. If coreboot is not yet installed: Refer to [setup](../setup.md)
