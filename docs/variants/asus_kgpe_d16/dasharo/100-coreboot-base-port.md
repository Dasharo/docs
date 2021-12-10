# Dasharo: coreboot base port

## Test cases

### CBP001.001 Firmware building

Refer to [building manual](../building-manual.md)

### CBP002.001 Firmware flashing - external programmer

Refer to [setup](../setup.md/#spi)

### CBP004.001 Boot into coreboot stage bootblock

**Test description**

This test verifies whether the DUT during booting procedure reaches 
stage bootblock. The bootblock is the first stage executed after CPU reset, 
its main task is to set up everything for a C-environment.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

            bootblock starting

### CBP004.002 Boot into coreboot stage romstage

**Test description**

This test verifies whether the DUT during booting procedure reaches 
stage romstage. The romstage initializes the DRAM and prepares everything 
for device init.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

            romstage starting

### CBP004.003 Boot into coreboot stage postcar

**Test description**

This test verifies whether the DUT during booting procedure reaches 
stage postcar. The postcar tears down CAR and loads the ramstage.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string with the phrase:

            postcar starting

### CBP004.004 Boot into coreboot stage ramstage

**Test description**

This test verifies whether the DUT during booting procedure reaches 
stage ramstage. The ramstage does the main device init.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain string the with phrase:

            ramstage starting

### CBP005.001 Resource allocator v4 - gathering requirements

**Test description**

This test aims to verify that DUT reaches the `gathering requirements` stage for 
Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain a string with the phrase:

            Pass 1 (gathering requirements)

### CBP005.002 Resource allocator v4 - allocating resources

**Test description**

This test aims to verify that DUT reaches the `allocating resources` stage for 
Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](../dasharo-compatibility/generic-test-setup.md/#firmware)
2. Connect to the UART debug interface and open a serial console.

**Test steps**

1. Power ON the DUT.
2. By using the serial console read the booting procedure stage.

**Expected result**

1. The console output should contain a string with the phrase:

            Pass 2 (allocating resources)