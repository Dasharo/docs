# Legacy -> UEFI Update

This document describes the process of updating the platform's legacy SeaBIOS
to Dasharo firmware based on EDK II.

## OS compatibility

Switching from BIOS to UEFI-based firmware might cause compatibility issues if
you already had an operating system installed on your platform. Some OSs can
handle the switch without any issues, while others may need to be reinstalled.
We have tested the update on several operating systems. The results are
presented in the table below:

### Ubuntu

Can be booted from UEFI.

### OPNSense

Can be booted from UEFI.

### pfSense

Requires OS reinstall.
