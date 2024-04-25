# Post-installation setup

This document contains extra steps to perform after installing Dasharo in order
to enable full functionality.

## Windows

This section covers Windows post-install steps tested on Windows 11.

### Qualcomm Atheros cards may be missing driver

If you experience Windows to fail to recognize Qualcomm Atheros WiFi cards,
you may need to install the necessary driver manually.

Download the Windows driver from [ath-drivers.eu](https://www.ath-drivers.eu/download-driver-nr-382-for-atheros-QCA6174A-and-Windows10.html)
Using `Device Manager`, select `Update Driver` for `Network Device` located in
`Other devices` and choose to install the downloaded driver.
