# Dasharo Compatibility: Platform suspend and resume

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Install the `pm-utils` package: `sudo apt-get install pm-utils`.

## SUSP001.001 Platform suspend and resume (Ubuntu 22.04, wakeup flag)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, the wakeup flag
is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command to set the wakeup
    flag:

    ```bash
    rtcwake --mode no --seconds 60
    ```

1. Execute the following command to enter the DUT into sleep mode:

    ```bash
    pm-suspend
    ```

1. Wait 60 seconds.
1. Log into the system again.
1. Execute the following command to get the results of suspend:

    ```bash
    cat /var/log/pm-suspend.log
    ```

1. Note the results.

**Expected result**

1. After entering the second command the DUT should enter sleep mode.
1. The DUT should automatically awaken after 60 seconds.
1. The output of the third command should contain information about suspend
    mode, especially information about moments of entering and leaving it. Also,
    it should not contain information that any suspend and awake hook fails.
    The example output from this command has been shown in the
    [Summary example output](#summary-example-output) section.

## SUSP002.001 Platform suspend and resume (Ubuntu 22.04, press key)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, pressing any key
on the keyboard is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command to enter DUT into
    sleep mode:

    ```bash
    pm-suspend
    ```

1. Wait 15 seconds.
1. Press any key on the keyboard to resume the system.
1. Log into the system again.
1. Execute the following command to get the results of suspend:

    ```bash
    cat /var/log/pm-suspend.log
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second command should contain information about suspend
    mode, especially information about moments of entering and leaving it. Also,
    it should not contain information that any suspend and awake hook fails.
    The example output from this command has been shown in the
    [Summary example output](#summary-example-output) section.

## SUSP003.001 Platform suspend and resume (Ubuntu 22.04, push power button)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, pushing the
power button is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command to enter DUT into
    sleep mode:

    ```bash
    pm-suspend
    ```

1. Wait 15 seconds.
1. Push the power button to resume the system.
1. Log into the system again.
1. Execute the following command to get the results of suspend:

    ```bash
    cat /var/log/pm-suspend.log
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second command should contain information about suspend
    mode, especially information about moments of entering and leaving it. Also,
    it should not contain information that any suspend and awake hook fails.
    The example output from this command has been shown in the
    [Summary example output](#summary-example-output) section.

## SUSP004.001 Platform suspend and resume (Ubuntu 22.04, Wake-on-LAN)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, the Wake-on-LAN
mechanism is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu 22.04`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and execute the following command to obtain the device
    lowest MAC address:

    ```bash
    ip address
    ```

    > Note, that the output of the above command might include information about
    all communication interfaces with their MAC addresses. In the Wake-on-LAN
    procedure, only the lowest MAC address of the active interface will be
    needed.

1. Execute the following command to enter DUT into sleep mode:

    ```bash
    pm-suspend
    ```

1. Wait 15 seconds.
1. On another active machine execute the following command to send a magic
    pocket:

    ```bash
    wakeonlan <DUT MAC address>
    ```

1. Log into the system (on the DUT) again.
1. Execute the following command to get the results of suspend:

    ```bash
    cat /var/log/pm-suspend.log
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second command should contain information about suspend
    mode, especially information about moments of entering and leaving it. Also,
    it should not contain information that any suspend and awake hook fails.
    The example output from this command has been shown in the
    [Summary example output](#summary-example-output) section.

## Summary example output

Below is shown an example output from the command `cat /var/log/pm-suspend.log`:

```bash
Initial commandline parameters: 
wto, 10 sty 2023, 14:32:00 CET: Running hooks for suspend.
Running hook /usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend:
/usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/000record-status suspend suspend:
/usr/lib/pm-utils/sleep.d/000record-status suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/00logging suspend suspend:
Linux user-NS5x-NS7xPU 5.17.0-1025-oem #26-Ubuntu SMP PREEMPT Wed Dec 7 12:41:04 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
Module                  Size  Used by
ccm                    20480  6
rfcomm                 81920  4
snd_hda_codec_hdmi     73728  1
snd_hda_codec_realtek   151552  1
snd_hda_codec_generic   102400  1 snd_hda_codec_realtek
cmac                   16384  3
algif_hash             16384  1
algif_skcipher         16384  1
af_alg                 32768  6 algif_hash,algif_skcipher
bnep                   28672  2
snd_sof_pci_intel_tgl    16384  0
snd_sof_intel_hda_common   102400  1 snd_sof_pci_intel_tgl
soundwire_intel        40960  1 snd_sof_intel_hda_common
soundwire_generic_allocation    16384  1 soundwire_intel
intel_rapl_msr         20480  0
soundwire_cadence      36864  1 soundwire_intel
intel_rapl_common      40960  1 intel_rapl_msr
snd_sof_intel_hda      20480  1 snd_sof_intel_hda_common
intel_tcc_cooling      16384  0
snd_sof_pci            20480  2 snd_sof_intel_hda_common,snd_sof_pci_intel_tgl
snd_sof_xtensa_dsp     16384  1 snd_sof_intel_hda_common
snd_sof               163840  2 snd_sof_pci,snd_sof_intel_hda_common
joydev                 32768  0
x86_pkg_temp_thermal    20480  0
intel_powerclamp       20480  0
snd_soc_hdac_hda       24576  1 snd_sof_intel_hda_common
snd_hda_ext_core       32768  3 snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_sof_intel_hda
snd_soc_acpi_intel_match    61440  2 snd_sof_intel_hda_common,snd_sof_pci_intel_tgl
snd_soc_acpi           16384  2 snd_soc_acpi_intel_match,snd_sof_intel_hda_common
soundwire_bus          94208  3 soundwire_intel,soundwire_generic_allocation,soundwire_cadence
coretemp               24576  0
ledtrig_audio          16384  2 snd_hda_codec_generic,snd_sof
i915                 3178496  4
snd_soc_core          339968  4 soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_soc_hdac_hda
snd_compress           24576  1 snd_soc_core
ac97_bus               16384  1 snd_soc_core
snd_pcm_dmaengine      16384  1 snd_soc_core
snd_hda_intel          53248  3
snd_intel_dspcfg       32768  2 snd_hda_intel,snd_sof_intel_hda_common
snd_intel_sdw_acpi     20480  2 snd_sof_intel_hda_common,snd_intel_dspcfg
snd_hda_codec         155648  5 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec_realtek,snd_soc_hdac_hda
snd_hda_core          110592  9 snd_hda_codec_generic,snd_hda_codec_hdmi,snd_hda_intel,snd_hda_ext_core,snd_hda_codec,snd_hda_codec_realtek,snd_sof_intel_hda_common,snd_soc_hdac_hda,snd_sof_intel_hda
snd_hwdep              16384  1 snd_hda_codec
snd_pcm               147456  10 snd_hda_codec_hdmi,snd_hda_intel,snd_hda_codec,soundwire_intel,snd_sof,snd_sof_intel_hda_common,snd_compress,snd_soc_core,snd_hda_core,snd_pcm_dmaengine
iwlmvm                581632  0
uvcvideo              110592  0
snd_seq_midi           20480  0
videobuf2_vmalloc      20480  1 uvcvideo
snd_seq_midi_event     16384  1 snd_seq_midi
kvm_intel             425984  0
snd_rawmidi            45056  1 snd_seq_midi
ttm                    81920  1 i915
videobuf2_memops       20480  1 videobuf2_vmalloc
mac80211             1245184  1 iwlmvm
kvm                  1032192  1 kvm_intel
videobuf2_v4l2         32768  1 uvcvideo
binfmt_misc            24576  1
crct10dif_pclmul       16384  1
libarc4                16384  1 mac80211
drm_kms_helper        323584  1 i915
snd_seq                73728  2 snd_seq_midi,snd_seq_midi_event
videobuf2_common       77824  4 videobuf2_vmalloc,videobuf2_v4l2,uvcvideo,videobuf2_memops
ghash_clmulni_intel    16384  0
cec                    77824  2 drm_kms_helper,i915
mei_hdcp               24576  0
snd_seq_device         16384  3 snd_seq,snd_seq_midi,snd_rawmidi
aesni_intel           376832  8
mei_pxp                20480  0
videodev              249856  3 videobuf2_v4l2,uvcvideo,videobuf2_common
snd_timer              40960  2 snd_seq,snd_pcm
rc_core                65536  1 cec
crypto_simd            16384  1 aesni_intel
pmt_telemetry          16384  0
nls_iso8859_1          16384  1
mc                     65536  4 videodev,videobuf2_v4l2,uvcvideo,videobuf2_common
iwlwifi               466944  1 iwlmvm
pmt_class              16384  1 pmt_telemetry
cryptd                 24576  3 crypto_simd,ghash_clmulni_intel
snd                   102400  20 snd_hda_codec_generic,snd_seq,snd_seq_device,snd_hda_codec_hdmi,snd_hwdep,snd_hda_intel,snd_hda_codec,snd_hda_codec_realtek,snd_sof,snd_timer,snd_compress,snd_soc_core,snd_pcm,snd_rawmidi
input_leds             16384  0
i2c_algo_bit           16384  1 i915
mei_me                 45056  2
rapl                   20480  0
fb_sys_fops            16384  1 drm_kms_helper
btusb                  61440  0
syscopyarea            16384  1 drm_kms_helper
cfg80211              978944  3 iwlmvm,iwlwifi,mac80211
intel_cstate           20480  0
serio_raw              20480  0
ee1004                 20480  0
soundcore              16384  1 snd
hid_multitouch         28672  0
mei                   135168  5 mei_hdcp,mei_pxp,mei_me
btrtl                  24576  1 btusb
sysfillrect            20480  1 drm_kms_helper
sysimgblt              16384  1 drm_kms_helper
btbcm                  24576  1 btusb
intel_vsec             20480  0
igen6_edac             24576  0
intel_pmc_mux          16384  0
btintel                40960  1 btusb
typec                  61440  1 intel_pmc_mux
btmtk                  16384  1 btusb
intel_hid              24576  0
mac_hid                16384  0
bluetooth             782336  34 btrtl,btmtk,btintel,btbcm,bnep,btusb,rfcomm
intel_scu_pltdrv       16384  1
sparse_keymap          16384  1 intel_hid
system76_acpi          20480  0
ecdh_generic           16384  2 bluetooth
ecc                    36864  1 ecdh_generic
sch_fq_codel           20480  2
msr                    16384  0
parport_pc             49152  0
ppdev                  24576  0
lp                     28672  0
parport                65536  3 parport_pc,lp,ppdev
drm                   589824  5 drm_kms_helper,i915,ttm
ramoops                32768  0
pstore_blk             16384  0
reed_solomon           28672  1 ramoops
pstore_zone            28672  1 pstore_blk
efi_pstore             16384  0
ip_tables              32768  0
x_tables               53248  1 ip_tables
autofs4                45056  2
hid_generic            16384  0
sdhci_pci              65536  0
intel_lpss_pci         28672  0
i2c_hid_acpi           16384  0
r8169                  94208  0
nvme                   49152  2
cqhci                  36864  1 sdhci_pci
i2c_i801               36864  0
intel_lpss             16384  1 intel_lpss_pci
i2c_hid                32768  1 i2c_hid_acpi
xhci_pci               24576  0
crc32_pclmul           16384  0
psmouse               176128  0
thunderbolt           327680  0
nvme_core             131072  3 nvme
i2c_smbus              20480  1 i2c_i801
sdhci                  81920  1 sdhci_pci
realtek                32768  1
idma64                 20480  0
xhci_pci_renesas       20480  1 xhci_pci
video                  53248  1 i915
hid                   147456  3 i2c_hid,hid_multitouch,hid_generic
pinctrl_tigerlake      32768  1
            total        used        free      shared  buff/cache   available
Mem:        16222784      799048    13969784      210248     1453952    14918760
Swap:        2097148           0     2097148
/usr/lib/pm-utils/sleep.d/00logging suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/00powersave suspend suspend:
/usr/lib/pm-utils/sleep.d/00powersave suspend suspend: success.

Running hook /etc/pm/sleep.d/10_grub-common suspend suspend:
/etc/pm/sleep.d/10_grub-common suspend suspend: success.

Running hook /etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend:
/etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/40inputattach suspend suspend:
/usr/lib/pm-utils/sleep.d/40inputattach suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend:
/usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend:
Selected interface 'wlp44s0'
OK
/usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/75modules suspend suspend:
/usr/lib/pm-utils/sleep.d/75modules suspend suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/90clock suspend suspend:
/usr/lib/pm-utils/sleep.d/90clock suspend suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend:
/usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend:
/usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/95led suspend suspend:
/usr/lib/pm-utils/sleep.d/95led suspend suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend:
Kernel modesetting video driver detected, not using quirks.
/usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/99video suspend suspend:
kernel.acpi_video_flags = 0
/usr/lib/pm-utils/sleep.d/99video suspend suspend: success.

wto, 10 sty 2023, 14:32:00 CET: performing suspend
wto, 10 sty 2023, 14:32:21 CET: Awake.
wto, 10 sty 2023, 14:32:21 CET: Running hooks for resume
Running hook /usr/lib/pm-utils/sleep.d/99video resume suspend:
/usr/lib/pm-utils/sleep.d/99video resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend:
/usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/95led resume suspend:
/usr/lib/pm-utils/sleep.d/95led resume suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend:
/usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/94cpufreq resume suspend:
/usr/lib/pm-utils/sleep.d/94cpufreq resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/90clock resume suspend:
/usr/lib/pm-utils/sleep.d/90clock resume suspend: not applicable.

Running hook /usr/lib/pm-utils/sleep.d/75modules resume suspend:
Reloaded unloaded modules.
/usr/lib/pm-utils/sleep.d/75modules resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend:
Selected interface 'wlp44s0'
OK
/usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/50unload_alx resume suspend:
/usr/lib/pm-utils/sleep.d/50unload_alx resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/40inputattach resume suspend:
/usr/lib/pm-utils/sleep.d/40inputattach resume suspend: success.

Running hook /etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend:
/etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend: success.

Running hook /etc/pm/sleep.d/10_grub-common resume suspend:
/etc/pm/sleep.d/10_grub-common resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/00powersave resume suspend:
/usr/lib/pm-utils/sleep.d/00powersave resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/00logging resume suspend:
/usr/lib/pm-utils/sleep.d/00logging resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/000record-status resume suspend:
/usr/lib/pm-utils/sleep.d/000record-status resume suspend: success.

Running hook /usr/lib/pm-utils/sleep.d/000kernel-change resume suspend:
/usr/lib/pm-utils/sleep.d/000kernel-change resume suspend: success.

wto, 10 sty 2023, 14:32:26 CET: Finished.
```
