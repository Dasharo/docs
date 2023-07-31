

# Dasharo Compatibility: Battery boot block

## Test cases common documentation

**Test setup**

1. Proceed with the
    [Generic test setup: firmware](../../generic-test-setup#firmware).
1. Proceed with the
    [Generic test setup: OS installer](../../generic-test-setup#os-installer).
1. Proceed with the
    [Generic test setup: OS installation](../../generic-test-setup#os-installation).
1. Proceed with the
    [Generic test setup: OS boot from disk](../../generic-test-setup#os-boot-from-disk).
1. DUT not plugged in to the charger.

## BBB001.001 Boot block when battery level is low (Ubuntu 22.04)

**Test description**

This test aims to verify that booting into the OS is blocked when the battery
level sits below 5%.

**Test configuration data**

1. `FIRMWARE` = Dasharo
1. `OPERATING_SYSTEM` = Ubuntu 22.04

**Test setup**

1. Proceed with the
    [Test cases common documentation](#test-cases-common-documentation) section.

**Test steps**

1. Power on the DUT.
1. Boot into the system.
1. Log into the system by using the proper login and password.
1. Open a terminal window and run following bash script:

```bash
get_battery_level() {
    battery_level=$(cat /sys/class/power_supply/BAT0/capacity)
    echo "$battery_level"
}
target_battery_level=5
while true; do
    current_battery_level=$(get_battery_level)
    echo "Current battery level: $current_battery_level%"
    if [ "$current_battery_level" -le "$target_battery_level" ]; then
        echo "Battery level reached 5%. Stopping stress-ng."
        break
    fi
    stress-ng --cpu 0 --timeout 10s
done
```

1. After the script finished working, reboot the DUT.

**Expected result**

1. The bash script reads current battery charge level and stresses the CPU until
    the battery charge level reaches 5%. Example output:

```bash
Current battery level: 92%
stress-ng: info:  [25309] setting to a 10 secs run per stressor
stress-ng: info:  [25309] dispatching hogs: 16 cpu
```

1. After reboot, booting into the OS should be blocked and following warning
    message should appear:

    ![boot_block](/docs/images/battery_block_popup.jpg)
