# Flashrom Write Protection – Test Specification

## Test cases

### WPR001.001 BIOS WP enable

#### Test description

This test aims to verify if it's possible to set the write protection and  
whether it actually works.

#### Test configuration data

1. `FIRMWARE` = coreboot

2. `OPERATING_SYSTEM` = Ubuntu 20.04

#### Test setup

1. Proceed with the [Generic test setup: firmware](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#firmware)

2. Proceed with the [Generic test setup: OS installer](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installer)

3. Proceed with the [Generic test setup: OS installation](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installation)

4. Proceed with the [Generic test setup: OS boot from disk](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-boot-from-disk)

5. Install flashrom and cbfstool tools with the below commands:

    - In order to build flashrom we will need some packages and libraries.  
For Debian based distros execute:  

            `sudo apt-get install git make binutils build-essential ca-certificates \`  
            `libpci-dev libftdi-dev libusb-1.0-0-dev`

    - Now clone the flashrom repository and fetch the patchset:  

            `git clone https://github.com/flashrom/flashrom`  
            `cd flashrom`  
            `git fetch https://review.coreboot.org/flashrom refs/changes/13/59713/7 && \`  
            `git checkout FETCH_HEAD`  

    - Build flashrom:  

            `make`

6. Ensure the WP pin jumper on the flash is not placed.

#### Test steps

1. Clear SPI write protection:  

        `./flashrom -p internal --wp-disable`  
        `./flashrom -p internal --wp-range=0,0`

2. Check protection status:  

        `./flashrom -p internal --wp-status`

3. See what protection ranges are available for the chip:  

        `./flashrom -p internal --wp-list`

4. Set protection range e.g.(details on WP ranges [here](https://docs.dasharo.com/variants/asus_kgpe_d16/spi-wp/)):  

        `./flashrom -p internal --wp-range=0x007fc000,0x00004000`  
        `./flashrom -p internal --wp-enable`

5. Verify  protection status:

        `./flashrom -p internal --wp-status`

#### Expected result

1. Flashrom should report:  

        `Sucessfully set the requested protection range.`
    and

        `Sucessfully set the requested mode.`

2. WP status should change between 2. and 5. test steps. Output samples:

    Step 2:

    ```
    WP config bits: SRP1=0 SRP0=0 CMP=0 SEC=0 TB=0 BP2=0 BP1=0 BP0=0
    Protection range: start=0x00000000 length=0x00000000 (none)
    Protection mode: disabled
    ```

    Step 5:

    ```
    WP config bits: SRP1=0 SRP0=1 CMP=0 SEC=1 TB=0 BP2=0 BP1=1 BP0=1
    Protection range: start=0x007fc000 length=0x00004000 (upper 1/512)
    Protection mode: hardware
    ```

### WPR002.001 BIOS WP range changing

#### Test description

This test aims to verify whether it is possible to change the range of the  
protected memory.

#### Test configuration data

1. `FIRMWARE` = coreboot

2. `OPERATING_SYSTEM` = Ubuntu 20.04

#### Test setup

1. Proceed with the [Generic test setup: firmware](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#firmware)

2. Proceed with the [Generic test setup: OS installer](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installer)

3. Proceed with the [Generic test setup: OS installation](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installation)

4. Proceed with the [Generic test setup: OS boot from disk](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-boot-from-disk) 

5. Install flashrom and cbfstool tools with the below commands with the below commands:  

    - In order to build flashrom we will need some packages and libraries.  
For Debian based distros execute:  

            `sudo apt-get install git make binutils build-essential ca-certificates \`  
            `libpci-dev libftdi-dev libusb-1.0-0-dev`

    - Now clone the flashrom repository and fetch the patchset:  

            `git clone https://github.com/flashrom/flashrom`  
            `cd flashrom`  
            `git fetch https://review.coreboot.org/flashrom refs/changes/13/59713/7 && \`  
            `git checkout FETCH_HEAD`  

    - Build flashrom:  

            `make`

#### Test steps

1. Check protection status:  

        `./flashrom -p internal --wp-status`

2. Disable write protection:  

        `./flashrom -p internal --wp-disable`

3. See what protection ranges are available for the chip:  

        `./flashrom -p internal --wp-list`

4. Change write protection range e.g.(details on WP ranges [here](https://docs.dasharo.com/variants/asus_kgpe_d16/spi-wp/)):  

        `./flashrom -p internal --wp-range=0x008000,0x00001000`  
        `./flashrom -p internal --wp-enable`  

5. Verify protection status:  

        `./flashrom -p internal --wp-status`

#### Expected result

1. Flashrom should report:  

        `Sucessfully set the requested protection range.`
    and

        `Sucessfully set the requested mode.`
2. WP status should change between 1. and 5. test steps.

### BIOS WP disable

### Test description

This test aims to verify whether it is possible to remove write protecion.

#### Test configuration data

1. `FIRMWARE` = coreboot

2. `OPERATING_SYSTEM` = Ubuntu 20.04

#### Test setup

1. Proceed with the [Generic test setup: firmware](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#firmware)

2. Proceed with the [Generic test setup: OS installer](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installer)

3. Proceed with the [Generic test setup: OS installation](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-installation)

4. Proceed with the [Generic test setup: OS boot from disk](https://novacustom.gitlab.io/dasharo-compatibility/dasharo-compatibility/generic-test-setup/#os-boot-from-disk)

5. Install flashrom and cbfstool tools with the below commands with the below commands:

    - In order to build flashrom we will need some packages and libraries.  
For Debian based distros execute:  

            `sudo apt-get install git make binutils build-essential ca-certificates \`  
            `libpci-dev libftdi-dev libusb-1.0-0-dev`

    - Now clone the flashrom repository and fetch the patchset:  

            `git clone https://github.com/flashrom/flashrom`  
            `cd flashrom`  
            `git fetch https://review.coreboot.org/flashrom refs/changes/13/59713/7 && \`  
            `git checkout FETCH_HEAD`  

    - Build flashrom:  

            `make`

#### Test steps

1. Check protection status:  

        `./flashrom -p internal --wp-status`

2. Clear SPI write protection:  

        `./flashrom -p internal --wp-disable`  
        `./flashrom -p internal --wp-range=0,0`

3. Verify protection status:  

        `./flashrom -p internal --wp-status`

#### Expected result

1. Command return from step 3. of test steps should include:  

        `Protection range: start=0x00000000 length=0x00000000 (none)`  
        `Protection mode: disabled`
