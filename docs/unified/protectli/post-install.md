# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality.

=== "VPx6xx"
    ## Windows

    This section covers Windows post-install steps tested on Windows 11.

    ### Qualcomm Atheros cards may be missing driver

    If you experience Windows to fail to recognize Qualcomm Atheros WiFi cards,
    you may need to install the necessary driver manually.

    Download the Windows driver from [ath-drivers.eu](https://www.ath-drivers.eu/download-driver-nr-382-for-atheros-QCA6174A-and-Windows10.html)
    Using `Device Manager`, select `Update Driver` for `Network Device` located in
    `Other devices` and choose to install the downloaded driver.

    ## Linux

    This section covers Linux post-install steps tested on Ubuntu 22.04. It is
    likely that similar procedures would for others Linux distributions as well.

    ### Cards using ath10k_pci driver report a firmware failure at module load

    If you experience ath10k_pci failing to load with error in dmesg similar to:

    ```text
    [   11.098547] ath10k_pci 0000:07:00.0: wmi unified ready event not received
    [   11.148567] ath10k_pci 0000:07:00.0: device has crashed during init
    [   11.176535] ath10k_pci 0000:07:00.0: device has crashed during init
    [   11.176539] ath10k_pci 0000:07:00.0: failed to wait for target init: -70
    [   11.177684] ath10k_pci 0000:07:00.0: could not init core (-110)
    [   11.177711] ath10k_pci 0000:07:00.0: could not probe fw (-110)
    ```

    follow https://kb.protectli.com/kb/wifi-on-the-vault/ (Firmware Fix section)
    to fix the problem.
