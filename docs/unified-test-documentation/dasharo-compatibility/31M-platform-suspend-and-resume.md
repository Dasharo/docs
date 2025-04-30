# Dasharo Compatibility: Platform suspend and resume

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../generic-test-setup.md#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../generic-test-setup.md#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../generic-test-setup.md#os-installation).

## SUSP001.201 Platform suspend and resume (Ubuntu, wakeup flag)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, the wakeup flag
is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `pm-utils` package: `sudo apt-get install pm-utils`.

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
1. Execute the following command to get the results of suspend process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'suspend suspend: '
    ```

1. Execute the following command to get the results of resume process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'resume suspend: '
    ```

1. Note the results.

**Expected result**

1. After entering the second command the DUT should enter sleep mode.
1. The DUT should automatically awaken after 60 seconds.
1. The output of the third and fourth commands should contain information about
    suspend and resume procedure hooks' status. For none of them, an error
    message should be returned.

    Example output for the suspend process:

    ```bash
    /usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave suspend suspend: success.
    /etc/pm/sleep.d/10_grub-common suspend suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/75modules suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/90clock suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95led suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/99video suspend suspend: success.
    ```

    Example output for the resume process:

    ```bash
    /usr/lib/pm-utils/sleep.d/99video resume suspend: success.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend: success.
    /usr/lib/pm-utils/sleep.d/95led resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend: success.
    /usr/lib/pm-utils/sleep.d/94cpufreq resume suspend: success.
    /usr/lib/pm-utils/sleep.d/90clock resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/75modules resume suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx resume suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach resume suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend: success.
    /etc/pm/sleep.d/10_grub-common resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000kernel-change resume suspend: success.
    ```

## SUSP001.203 Platform suspend and resume (QubesOS, wakeup flag)

**Test description**

This test aims to verify that the DUT platform suspend and resume functionality
works correctly. As a way to wake up the device, the wakeup flag is tested in
this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window in `dom0` and execute the following command to set the
   wakeup flag:

    ```bash
    rtcwake --mode no --seconds 60
    ```

1. Execute the following command to enter the DUT into sleep mode:

    ```bash
    sudo systemctl suspend
    ```

1. Wait 60 seconds.
1. Log into the system again.
1. Execute the following command to get the results of process:

    ```bash
    journalctl | grep systemd-sleep
    ```

1. Note the results.

**Expected result**

1. After entering the `sudo systemctl suspend` command the DUT should enter
   sleep mode.
1. The output of the second command should contain information about performed
   suspend and resume operations. Each suspend and resume of the system should
   be reported in the output of this command with the correct date, an example
   of reporting one suspend and resume operation:

    ```bash
    Feb 10 16:38:55 dom0 systemd-sleep[14729]: Suspending system...
    Feb 10 16:39:10 dom0 systemd-sleep[14729]: System resumed.
    ```

## SUSP002.201 Platform suspend and resume (Ubuntu, press key)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, pressing any key
on the keyboard is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `pm-utils` package: `sudo apt-get install pm-utils`.

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
1. Execute the following command to get the results of suspend process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'suspend suspend: '
    ```

1. Execute the following command to get the results of resume process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'resume suspend: '
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second and third commands should contain information about
    suspend and resume procedure hooks' status. For none of them, an error
    message should be returned.

    Example output for the suspend process:

    ```bash
    /usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave suspend suspend: success.
    /etc/pm/sleep.d/10_grub-common suspend suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/75modules suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/90clock suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95led suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/99video suspend suspend: success.
    ```

    Example output for the resume process:

    ```bash
    /usr/lib/pm-utils/sleep.d/99video resume suspend: success.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend: success.
    /usr/lib/pm-utils/sleep.d/95led resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend: success.
    /usr/lib/pm-utils/sleep.d/94cpufreq resume suspend: success.
    /usr/lib/pm-utils/sleep.d/90clock resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/75modules resume suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx resume suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach resume suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend: success.
    /etc/pm/sleep.d/10_grub-common resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000kernel-change resume suspend: success.
    ```

## SUSP002.203 Platform suspend and resume (QubesOS, press key)

**Test description**

This test aims to verify that the DUT platform suspend and resume functionality
works correctly. As a way to wake up the device, pressing any key on the
keyboard is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window in `dom0` and execute the following command to enter
   the DUT into sleep mode:

    ```bash
    sudo systemctl suspend
    ```

1. Wait 15 seconds.
1. Press any key on the keyboard to resume the system.
1. Log into the system again.
1. Execute the following command to get the results of process:

    ```bash
    journalctl | grep systemd-sleep
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second command should contain information about performed
   suspend and resume operations. Each suspend and resume of the system should
   be reported in the output of this command with the correct date, an example
   of reporting one suspend and resume operation:

    ```bash
    Feb 10 16:38:55 dom0 systemd-sleep[14729]: Suspending system...
    Feb 10 16:39:10 dom0 systemd-sleep[14729]: System resumed.
    ```

## SUSP003.201 Platform suspend and resume (Ubuntu, push power button)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, pushing the
power button is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `pm-utils` package: `sudo apt-get install pm-utils`.

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
1. Execute the following command to get the results of suspend process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'suspend suspend: '
    ```

1. Execute the following command to get the results of resume process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'resume suspend: '
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second and third commands should contain information about
    suspend and resume procedure hooks' status. For none of them, an error
    message should be returned.

    Example output for the suspend process:

    ```bash
    /usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave suspend suspend: success.
    /etc/pm/sleep.d/10_grub-common suspend suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/75modules suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/90clock suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95led suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/99video suspend suspend: success.
    ```

    Example output for the resume process:

    ```bash
    /usr/lib/pm-utils/sleep.d/99video resume suspend: success.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend: success.
    /usr/lib/pm-utils/sleep.d/95led resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend: success.
    /usr/lib/pm-utils/sleep.d/94cpufreq resume suspend: success.
    /usr/lib/pm-utils/sleep.d/90clock resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/75modules resume suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx resume suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach resume suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend: success.
    /etc/pm/sleep.d/10_grub-common resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000kernel-change resume suspend: success.
    ```

## SUSP003.203 Platform suspend and resume (QubesOS, push power button)

**Test description**

This test aims to verify that the DUT platform suspend and resume functionality
works correctly. As a way to wake up the device, pushing the power button is
tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = QubesOS stable

**Test setup**

1. Proceed with the
   [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window in `dom0` and execute the following command to enter
   the DUT into sleep mode:

    ```bash
    sudo systemctl suspend
    ```

1. Wait 15 seconds.
1. Push the power button to resume the system.
1. Log into the system again.
1. Execute the following command to get the results of process:

    ```bash
    journalctl | grep systemd-sleep
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second command should contain information about performed
   suspend and resume operations. Each suspend and resume of the system should
   be reported in the output of this command with the correct date, an example
   of reporting one suspend and resume operation:

    ```bash
    Feb 10 16:38:55 dom0 systemd-sleep[14729]: Suspending system...
    Feb 10 16:39:10 dom0 systemd-sleep[14729]: System resumed.
    ```

## SUSP004.201 Platform suspend and resume (Ubuntu, Wake-on-LAN)

**Test description**

This test aims to verify that the DUT platform suspend and resume
functionality works correctly. As a way to wake up the device, the Wake-on-LAN
mechanism is tested in this case.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = `Ubuntu`

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.
1. Install the `pm-utils` package: `sudo apt-get install pm-utils`.

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
1. Execute the following command to get the results of suspend process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'suspend suspend: '
    ```

1. Execute the following command to get the results of resume process:

    ```bash
    cat /var/log/pm-suspend.log | grep 'resume suspend: '
    ```

1. Note the results.

**Expected result**

1. After entering the first command the DUT should enter sleep mode.
1. The output of the second and third commands should contain information about
    suspend and resume procedure hooks' status. For none of them, an error
    message should be returned.

    Example output for the suspend process:

    ```bash
    /usr/lib/pm-utils/sleep.d/000kernel-change suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave suspend suspend: success.
    /etc/pm/sleep.d/10_grub-common suspend suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/75modules suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/90clock suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/94cpufreq suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95led suspend suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler suspend suspend: success.
    /usr/lib/pm-utils/sleep.d/99video suspend suspend: success.
    ```

    Example output for the resume process:

    ```bash
    /usr/lib/pm-utils/sleep.d/99video resume suspend: success.
    /usr/lib/pm-utils/sleep.d/98video-quirk-db-handler resume suspend: success.
    /usr/lib/pm-utils/sleep.d/95led resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/95hdparm-apm resume suspend: success.
    /usr/lib/pm-utils/sleep.d/94cpufreq resume suspend: success.
    /usr/lib/pm-utils/sleep.d/90clock resume suspend: not applicable.
    /usr/lib/pm-utils/sleep.d/75modules resume suspend: success.
    /usr/lib/pm-utils/sleep.d/60_wpa_supplicant resume suspend: success.
    /usr/lib/pm-utils/sleep.d/50unload_alx resume suspend: success.
    /usr/lib/pm-utils/sleep.d/40inputattach resume suspend: success.
    /etc/pm/sleep.d/10_unattended-upgrades-hibernate resume suspend: success.
    /etc/pm/sleep.d/10_grub-common resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00powersave resume suspend: success.
    /usr/lib/pm-utils/sleep.d/00logging resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000record-status resume suspend: success.
    /usr/lib/pm-utils/sleep.d/000kernel-change resume suspend: success.
    ```

## SUSP005.201 Cyclic platform suspend and resume (Ubuntu)

The test is fully automated. Refer to https://github.com/Dasharo/open-source-firmware-validation/tree/develop
