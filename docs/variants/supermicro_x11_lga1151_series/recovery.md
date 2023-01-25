# Recovery

**Please read the [overview page](../overview) first!**

---

## BIOS Update through BMC

Following instruction was tested on:

* X11SSH-TF v1.01

For information how to identify your mainboard model pelase check
[faq](../faq/#how-to-identify-my-mainboard-model).

Following documentation describes the process of recovering hardware from brick
state with through BMC BIOS Update feature. This feature can be used also for
[initial deployment](../initial-deployment) and [Firmware
Update](../firmawre-update).

### Requirements

#### License activation

Without active license you can't use BIOS Update feature. License key can be
generated using [kasuganosoras
scripts](https://github.com/kasuganosoras/SuperMicro-IPMI-LicenseGenerator).

#### Up to date firmware

Please make sure you using firmware revision 01.60
<center>
![](../../images/supermicro_check_fw_rev.png)
</center>

If not please follow `IPMI Firmware Update_NEW.pdf` instruction from package
that you can download
[here](https://www.supermicro.com/en/support/resources/downloadcenter/firmware/MBD-X11SSH-TF/BMC).
