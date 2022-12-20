# Dasharo System Features

When entering the `Dasharo System Features` menu, one may see the following
submenus to appear:

- [Dasharo System Features](#dasharo-system-features)
    + [Dasharo Security Options](#dasharo-security-options)
    + [Networking Options](#networking-options)
    + [USB Configuration](#usb-configuration)
    + [Intel Management Engine Options](#intel-management-engine-options)
    + [Chipset Configuration](#chipset-configuration)

![](/images/menus/dasharo_features.jpeg)

## Dasharo Security Options

This section is under construction...

## Networking Options

This section is under construction...

## USB Configuration

This section is under construction...

## Intel Management Engine Options

This submenu is used to access Intel Management Engine related options.
Currently the only option available is `Intel ME mode` which allows to enable
or disable Management Engine:

![](/images/menus/me_menu.jpeg)

On the right side of the window there is a help section describing the option
meaning. If the windows is too small, the help section may be divided. To
scroll the help section use `D` or `d` keys to scroll down and `U` or `u` to
scroll up.

Intel ME can be disabled in two ways:

- `Disabled (Soft)` - when set, causes the Dasharo firmware to send
  `ME_DISABLE` command via MEI/HECI. MEI/HECI interface is being hidden from OS
  when ME is disabled.
- `Disabled (HAP)` - when set, causes the Dasharo firmware to set HAP bit in
  the flash descriptor. MEI/HECI interface is being hidden from OS when ME is
  disabled. HAP method is much more efficient as it halts the ME firmware
  execution even earlier than Soft Disable described above

![](/images/menus/me_menu2.jpeg)

When the mode is set to `Enabled`, Dasharo enables the Intel Management engine
by either sending `ME_ENABLE` command via MEI/HECI or clearing the HAP bit in
flash descriptor, depending on the previously active ME mode. MEI/HECI device
should be functional in OS when ME is enabled.

Any change in the Dasharo firmware setup requires saving the changes and a
platform reset (unless specified otherwise).

For more information about neutering and disabling ME see also
[me_cleaner](https://github.com/corna/me_cleaner).

NOTE: [me_cleaner](https://github.com/corna/me_cleaner) is not supported on all
platforms! If a platform supports [me_cleaner](https://github.com/corna/me_cleaner)
(i.e. ME version is lower or equal 11.x) it is recommended to set HAP bit and
clean the ME region with `me_cleaner` script permanently.

## Chipset Configuration

This section is under construction...
