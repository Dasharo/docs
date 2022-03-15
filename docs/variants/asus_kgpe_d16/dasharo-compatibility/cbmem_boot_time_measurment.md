# Dasharo Compatibility: Boot Time Measurement

## Test Cases

### BTM001.001 Coldboot time measurement

**Test description**

This test aims to measure coldboot time.

**Test configuration data**

1. `OPERATING_SYSTEM` = `Ubuntu 20.04`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](generic-test-setup#firmware).

2. Get `cbmem` tool from
[here](https://cloud.3mdeb.com/index.php/s/siyMirafZCPMi3Q/download).

**Test steps**

1. Disconnect the DUT from power source.

2. Connect back the DUT to power source.

3. Power ON the DUT.

4. Use the below command to look at boot timestamps:

        sudo cbmem -T

**Expected result**

1. Read timestamp from last row and second column. Last row may look like this:

        99     4084321 818      selfboot jump

    In this example we take `4084321` timestamp.

2. To get time in seconds, we need to divide the timestamp by 1000000.

        4084321 / 1000000

### BTM002.001 Warmboot time measurement

**Test description**

This test aims to measure warmboot time.

**Test configuration data**

1. `OPERATING_SYSTEM` = `Ubuntu 20.04`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](generic-test-setup#firmware).

2. Get `cbmem` tool from
[here](https://cloud.3mdeb.com/index.php/s/siyMirafZCPMi3Q/download).

**Test steps**

1. Power ON the DUT.

2. Power OFF the DUT.

3. Power ON the DUT.

4. Use the below command to look at boot timestamps:

        sudo cbmem -T

**Expected result**

1. Read timestamp from last row and second column. Last row may look like this:

        99     4084321 818      selfboot jump

    In this example we take `4084321` timestamp.

2. To get time in seconds, we need to divide the timestamp by 1000000.

        4084321 / 1000000


### BTM003.001 Reboot time measurement

**Test description**

This test aims to measure reboot time.

**Test configuration data**

1. `OPERATING_SYSTEM` = `Ubuntu 20.04`

**Test setup**

1. Proceed with the
   [Generic test setup: firmware](generic-test-setup#firmware)

2. Get `cbmem` tool from
[here](https://cloud.3mdeb.com/index.php/s/siyMirafZCPMi3Q/download).

**Test steps**

1. Power ON the DUT.

2. Use the below command to reboot the DUT.

        sudo reboot

3. Wait until DUT reboots.

4. Use the below command to look at boot timestamps:

        sudo cbmem -T

**Expected result**

1. Read timestamp from last row and second column. Last row may look like this:

        99     4084321 818      selfboot jump

    In this example we take `4084321` timestamp.

2. To get time in seconds, we need to divide the timestamp by 1000000.

        4084321 / 1000000
