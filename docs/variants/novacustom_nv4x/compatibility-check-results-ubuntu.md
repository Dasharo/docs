# Checkbox logs comparison

## Introduction

Checkbox is a flexible test automation software. It’s the main tool used in
Ubuntu Certification program.

You can use checkbox without any modification to check if your system is
behaving correctly or you can develop your own set of tests to check your
needs.

Checkbox optionally generates test reports in different formats
(JSON, HTML, etc.) that can be used to easily share the results of
a test session.

## Checkbox comparison - vendor firmware vs Dasharo

### Testing assumptions

1. Tests has been conducted on the same OS version (Ubuntu 22.04 LTS).
1. Tests has been conducted on the same device, firstly with vendor firmware,
    secondly with Dasharo firmware (version 1.2.1).

### Test results

1. Test results - vendor firmware:
    - PASSED: 74,
    - FAILED: 80,
    - NOT SUPPORTED: 25.
1. Test results - Dasharo firmware:
    - PASSED: 74,
    - FAILED: 80,
    - NOT SUPPORTED: 25.

### Fails comparison

The following table collects information about all errors detected by the
certification program. In second column test case name is described, in
third and fourth column the information about bug appearance on vendor/Dasharo
firmware is shown.

| No.    | Test case name                                  | Dasharo firmware | Vendor firmware |
|:------:|:------------------------------------------------|:-----------------|:----------------|
| 1      | graphics/*                                      | YES              | YES             |
| 2      | graphics/*                                      | YES              | YES             |
| 3      | bluetooth4/beacon_eddystone_url_hci0            | YES              | YES             |
| 4      | mediacard/storage-preinserted-disk/by-uuid/*    | YES              | YES             |
| 5      | mediacard/storage-preinserted-disk/by-uuid/*    | YES              | YES             |
| 6      | mediacard/storage-preinserted-disk/by-uuid/*    | YES              | YES             |
| 7      | mediacard/storage-preinserted-disk/by-uuid/*    | YES              | YES             |
| 8      | wireless/wireless_connection_open_ac_nm_wlp55s0 | YES              | YES             |
| 9      | wireless/wireless_connection_open_ax_nm_wlp55s0 | YES              | YES             |
| 10     | wireless/wireless_connection_open_bg_nm_wlp55s0 | YES              | YES             |
| 11     | wireless/wireless_connection_open_n_nm_wlp55s0  | YES              | YES             |
| 12     | wireless/wireless_connection_wpa_ac_nm_wlp55s0  | YES              | YES             |
| 13     | wireless/wireless_connection_wpa_ax_nm_wlp55s0  | YES              | YES             |
| 14     | wireless/wireless_connection_wpa_bg_nm_wlp55s0  | YES              | YES             |
| 15     | wireless/wireless_connection_wpa_n_nm_wlp55s0   | YES              | YES             |
| 16     | tpm2.0_4.1.1/tpm2_import                        | YES              | YES             |
| 17     | tpm2.0_4.1.1/tpm2_clockrateadjust               | YES              | YES             |
| 18     | tpm2.0_4.1.1/tpm2_loadexternal                  | YES              | YES             |
| 19     | tpm2.0_4.1.1/tpm2_rsadecrypt                    | YES              | YES             |
| 20     | tpm2.0_4.1.1/tpm2_activecredential              | YES              | YES             |
| 21     | tpm2.0_4.1.1/tpm2_attestation                   | YES              | YES             |
| 22     | tpm2.0_4.1.1/tpm2_certify                       | YES              | YES             |
| 23     | tpm2.0_4.1.1/tpm2_certifycreation               | YES              | YES             |
| 24     | tpm2.0_4.1.1/tpm2_changeauth                    | YES              | YES             |
| 25     | tpm2.0_4.1.1/tpm2_checkquote                    | YES              | YES             |
| 26     | tpm2.0_4.1.1/tpm2_clear                         | YES              | YES             |
| 27     | tpm2.0_4.1.1/tpm2_create                        | YES              | YES             |
| 28     | tpm2.0_4.1.1/tpm2_createak                      | YES              | YES             |
| 29     | tpm2.0_4.1.1/tpm2_createek                      | YES              | YES             |
| 30     | tpm2.0_4.1.1/tpm2_createpolicy                  | YES              | YES             |
| 31     | tpm2.0_4.1.1/tpm2_createprimary                 | YES              | YES             |
| 32     | tpm2.0_4.1.1/tpm2_dictionarylockout             | YES              | YES             |
| 33     | tpm2.0_4.1.1/tpm2_duplicate                     | YES              | YES             |
| 34     | tpm2.0_4.1.1/tpm2_evictcontrol                  | YES              | YES             |
| 35     | tpm2.0_4.1.1/tpm2_flushcontext                  | YES              | YES             |
| 36     | tpm2.0_4.1.1/tpm2_getcap                        | YES              | YES             |
| 37     | tpm2.0_4.1.1/tpm2_getekcertificate              | YES              | YES             |
| 38     | tpm2.0_4.1.1/tpm2_getrandom                     | YES              | YES             |
| 39     | tpm2.0_4.1.1/tpm2_gettestresult                 | YES              | YES             |
| 40     | tpm2.0_4.1.1/tpm2_gettime                       | YES              | YES             |
| 41     | tpm2.0_4.1.1/tpm2_hash                          | YES              | YES             |
| 42     | tpm2.0_4.1.1/tpm2_hmac                          | YES              | YES             |
| 43     | tpm2.0_4.1.1/tpm2_import_tpm                    | YES              | YES             |
| 44     | tpm2.0_4.1.1/tpm2_incrementalselftest           | YES              | YES             |
| 45     | tpm2.0_4.1.1/tpm2_load                          | YES              | YES             |
| 46     | tpm2.0_4.1.1/tpm2_makecredential                | YES              | YES             |
| 47     | tpm2.0_4.1.1/tpm2_nv                            | YES              | YES             |
| 48     | tpm2.0_4.1.1/tpm2_nvcertify                     | YES              | YES             |
| 49     | tpm2.0_4.1.1/tpm2_nvinc                         | YES              | YES             |
| 50     | tpm2.0_4.1.1/tpm2_output_formats                | YES              | YES             |
| 51     | tpm2.0_4.1.1/tpm2_pcrevent                      | YES              | YES             |
| 52     | tpm2.0_4.1.1/tpm2_pcrextend                     | YES              | YES             |
| 53     | tpm2.0_4.1.1/tpm2_pcrlist                       | YES              | YES             |
| 54     | tpm2.0_4.1.1/tpm2_pcrreset                      | YES              | YES             |
| 55     | tpm2.0_4.1.1/tpm2_print                         | YES              | YES             |
| 56     | tpm2.0_4.1.1/tpm2_quote                         | YES              | YES             |
| 57     | tpm2.0_4.1.1/tpm2_readclock                     | YES              | YES             |
| 58     | tpm2.0_4.1.1/tpm2_readpublic                    | YES              | YES             |
| 59     | tpm2.0_4.1.1/tpm2_rsaencrypt                    | YES              | YES             |
| 60     | tpm2.0_4.1.1/tpm2_selftest                      | YES              | YES             |
| 61     | tpm2.0_4.1.1/tpm2_send                          | YES              | YES             |
| 62     | tpm2.0_4.1.1/tpm2_setclock                      | YES              | YES             |
| 63     | tpm2.0_4.1.1/tpm2_setprimarypolicy              | YES              | YES             |
| 64     | tpm2.0_4.1.1/tpm2_sign                          | YES              | YES             |
| 65     | tpm2.0_4.1.1/tpm2_startup                       | YES              | YES             |
| 66     | tpm2.0_4.1.1/tpm2_stirrandom                    | YES              | YES             |
| 67     | tpm2.0_4.1.1/tpm2_testparms                     | YES              | YES             |
| 68     | tpm2.0_4.1.1/tpm2_unseal                        | YES              | YES             |
| 69     | tpm2.0_4.1.1/tpm2_verifysignature               | YES              | YES             |
| 70     | audio/detect_sinks_sources                      | YES              | YES             |
| 71     | suspend/*                                       | YES              | YES             |
| 72     | suspend/*                                       | YES              | YES             |
| 73     | suspend/audio_before_suspend                    | YES              | YES             |
| 74     | suspend/bluetooth_obex_send_after_suspend_auto  | YES              | YES             |
| 75     | suspend/bluetooth_obex_send_before_suspend      | YES              | YES             |
| 76     | usb/storage-preinserted-disk/by-uuid/0868-01F6  | YES              | YES             |
| 77     | usb/storage-preinserted-disk/by-uuid/*          | YES              | YES             |
| 78     | usb/storage-preinserted-disk/by-uuid/*          | YES              | YES             |
| 79     | usb/storage-preinserted-disk/by-uuid/*          | YES              | YES             |
| 80     | usb/storage-preinserted-disk/by-uuid/452E-652F  | YES              | YES             |

*Full names:

* 2. graphics/1_driver_version_TigerLake-LP_GT2__Iris_Xe_Graphics_
* 3. graphics/1_driver_version_TigerLake-LP_GT2__Iris_Xe_Graphics_
* 5. mediacard/storage-preinserted-disk/by-uuid/0868-01F6
* 6. mediacard/storage-preinserted-disk/by-uuid/2adea2a3-f163-4d14-b6f3-b8d628611e23
* 7. mediacard/storage-preinserted-disk/by-uuid/2d67f8a9-7f79-4419-b1d3-e096ca010512
* 8. mediacard/storage-preinserted-disk/by-uuid/3bb6b676-1c4d-4ffb-8ede-e68f513fcdf1
* 70. suspend/1_driver_version_after_suspend_TigerLake-LP_GT2__Iris_Xe_Graphics__auto
* 71. suspend/2_driver_version_after_suspend_TU117M_auto
* 77. usb/storage-preinserted-disk/by-uuid/2adea2a3-f163-4d14-b6f3-b8d628611e23
* 78. usb/storage-preinserted-disk/by-uuid/2d67f8a9-7f79-4419-b1d3-e096ca010512
* 79. usb/storage-preinserted-disk/by-uuid/3bb6b676-1c4d-4ffb-8ede-e68f513fcdf1

### Logs from tests

Logs are available under this
[link](https://cloud.3mdeb.com/index.php/apps/files/?dir=/projects/novacustom/tat/logs-checkbox&fileid=480327).

## Summary

Test results are the same for vendor and dasharo firmware, no differences.
