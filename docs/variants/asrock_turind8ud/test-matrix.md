# Test matrix

## About

The test matrix is used to determine the scope of tests which the DUT is
subjected from before the release of the new binary.

=== "LinuxBoot"

    ## Module: Dasharo compatibility

    |  No.  |   Supported test suite   | Test suite ID | Supported test cases  |
    | :---: | :----------------------- | :-----------: | :-------------------- |
    |  1.   | CPU Status               |      CPU      | All Ubuntu test cases |
    |  2.   | SMBIOS                   |      DMI      | All Ubuntu test cases |
    |  3.   | NVMe                     |      NVM      | All Ubuntu test cases |
    |  4.   | USB HID and Mass Storage |      USB      | All Ubuntu test cases |

    ## Module: Dasharo security

    | No.  |  Supported test suite   | Test suite ID | Supported test cases  |
    | :--- | :---------------------- | :-----------: | :-------------------- |
    | 1.   | Measured Boot           |      MBO      | All Ubuntu test cases |
    | 2.   | Trusted Platform Module |      TPM      | All Ubuntu test cases |
    | 3.   | TPM2 Commands           |    TPMCMD     | All                   |

    ## Module: Dasharo performance

    | No.  |      Supported test suite      | Test suite ID |    Supported test cases    |
    | :--- | :----------------------------- | :-----------: | :------------------------- |
    | 1.   | coreboot boot time measurement |     CBMEM     | All Ubuntu test cases      |
    | 2.   | CPU Frequency                  |      CPF      | All Ubuntu test cases (AC) |
    | 3.   | CPU Temperature                |      CPT      | All Ubuntu test cases (AC) |
    | 4.   | Stability                      |      STB      | All                        |

    ## Module: Dasharo Stability

    | No.  | Supported test suite | Test suite ID |        Supported test cases         |
    | :--- | :------------------- | :-----------: | :---------------------------------- |
    | 1.   | NVMe Detection       |      SNV      | All Ubuntu test cases excl. suspend |
    | 2.   | TPM Detection        |      TPD      | All Ubuntu test cases excl. suspend |
    | 3.   | USB Type-A Detection |      SUD      | All Ubuntu test cases excl. suspend |
