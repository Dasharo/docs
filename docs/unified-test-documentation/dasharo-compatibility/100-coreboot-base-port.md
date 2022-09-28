# Dasharo: coreboot base port

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup/#firmware).
1. Connect to the UART debug interface and open a serial console.

## CBP001.001 Boot into coreboot stage bootblock

**Test description**

This test aims to verify that DUT during booting procedure reaches
stage bootblock. The bootblock is the first stage executed after CPU reset,
its main task is to set up everything for a C-environment.

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Test steps**

1. Power on the DUT.
2. Read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

    ```bash
    bootblock starting
    ```

## CBP002.001 Boot into coreboot stage romstage

**Test description**

This test aims to verify that DUT during booting procedure reaches
stage romstage. The romstage initializes the DRAM and prepares everything
for device init.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

    ```bash
    romstage starting
    ```

## CBP003.001 Boot into coreboot stage postcar

**Test description**

This test aims to verify that DUT during booting procedure reaches
stage postcar. The postcar tears down CAR and loads the ramstage.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

    ```bash
    postcar starting
    ```

## CBP004.001 Boot into coreboot stage ramstage

**Test description**

This test aims to verify that DUT during booting procedure reaches
stage ramstage. The ramstage does the main device init.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string the with phrase:

    ```bash
    ramstage starting
    ```

## CBP005.001 Resource allocator v4 - gathering requirements

**Test description**

This test aims to verify that DUT reaches the `gathering requirements`
stage for Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain a string with the phrase:

    ```bash
    Pass 1 (gathering requirements)
    ```

## CBP006.001 Resource allocator v4 - allocating resources

**Test description**

This test aims to verify that DUT reaches the `allocating resources` stage for
Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = Dasharo

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain a string with the phrase:

    ```bash
    Pass 2 (allocating resources)
    ```
