# Dasharo comapitbility: coreboot base port

## Test cases

### CBP001.001 Boot into coreboot stage bootblock

**Test description**

This test verifies whether the DUT during booting procedure reaches
stage bootblock. The bootblock is the first stage executed after CPU reset,
its main task is to set up everything for a C-environment.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain string with the phrase:

```
bootblock starting
```

### CBP002.002 Boot into coreboot stage romstage

**Test description**

This test verifies whether the DUT during booting procedure reaches
stage romstage. The romstage initializes the DRAM and prepares everything
for device init.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain string with the phrase:

```
romstage starting
```

### CBP004.003 Boot into coreboot stage postcar

**Test description**

This test verifies whether the DUT during booting procedure reaches
stage postcar. The postcar tears down CAR and loads the ramstage.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain string with the phrase:

```
postcar starting
```

### CBP004.004 Boot into coreboot stage ramstage

**Test description**

This test verifies whether the DUT during booting procedure reaches
stage ramstage. The ramstage does the main device init.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the 
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain string the with phrase:

```
ramstage starting
```

### CBP005.001 Resource allocator v4 - gathering requirements

**Test description**

This test aims to verify that DUT reaches the `gathering requirements` stage for
Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain a string with the phrase:

```
Pass 1 (gathering requirements)
```

### CBP005.002 Resource allocator v4 - allocating resources

**Test description**

This test aims to verify that DUT reaches the `allocating resources` stage for
Resource Allocator v4 during booting procedure.

**Test configuration data**

1. `FIRMWARE` = coreboot

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](generic-test-setup.md#firmware).

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Test steps**

1. Power on the DUT.
1. Read coreboot loading logs.

**Expected result**

1. The console output should contain a string with the phrase:

```
Pass 2 (allocating resources)
```
