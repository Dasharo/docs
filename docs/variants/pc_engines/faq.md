# FAQ
<!-- markdownlint-disable-next-line MD013 -->
## What BIOS Version can I install with my Dasharo (coreboot+SeaBIOS) Subscription on an apu2/3/4/6 motherboard?

When you subscribe to a Dasharo (coreboot+SeaBIOS) Pro Package for
Network Appliance, the BIOS version updates available to you are determined by
Dasharo's release cycle and testing scope.

1. **Upcoming BIOS Version:**
The next BIOS version that you will be able to install will most likely be
tagged as 24.08.00.01. For detailed insights into the versioning
scheme, please refer to the coreboot release notes here: [Coreboot Release Notes](https://doc.coreboot.org/releases/coreboot-24.02-relnotes.html?highlight=releases#release-number-format-update)
as well as discussion about [Dasharo Versioning](https://github.com/Dasharo/dasharo-issues/issues/762).

1. **Test Scope:**
While the exact test scope for the upcoming BIOS version is currently being
finalized, it will offer feature parity with version 4.19.0.1. The test scope
for version 4.19.0.1, which might give you an idea of what to expect, can be
found in this document: [Dasharo Test Scope Document](https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0).

1. **Release Information:**
Detailed information about the release, including the scope and enhancements,
will be communicated through our release newsletter. Additionally, all release
notes and relevant updates will be made available on the Dasharo documentation
site at [Dasharo Release Documentation](https://docs.dasharo.com/variants/pc_engines/releases_seabios/).
<!-- markdownlint-disable-next-line MD013 -->
## How much would it cost me to switch my subscription for Network Appliance from already purchased (coreboot+UEFI) to (coreboot+SeaBIOS)?

We can switch your subscription from [Dasharo (coreboot+UEFI) Pro Package
for Network Appliance](https://shop.3mdeb.com/shop/dasharo-entry-subscription/1-year-dasharo-entry-subscription-for-network-appliance/)
to the [Dasharo (coreboot+SeaBIOS) Pro Package for Network Appliance](https://shop.3mdeb.com/shop/dasharo-entry-subscription/1-year-dasharo-entry-subscription-for-network-appliance-corebootseabios/)
at no extra cost. This change can be made until the end of May 2024, but only if
the purchase was made before the official [(coreboot+UEFI) release](https://docs.dasharo.com/variants/pc_engines/releases_uefi/)
which occurred on 2024-04-02.

If you are interested, please contact us at shopping@3mdeb.com and provide your
order number.

## The Dasharo (coreboot+UEFI) version is 0.9.x. Does this mean it is still in beta?

No, our policy for versioning is that we never release 1.x.y as a first
release. We cannot validate it at the mass production readiness level.
Validation results are always linked on the release page, or you can find those
directly in [Google
Sheet](https://docs.google.com/spreadsheets/d/1wSE6xA3K3nXewwLn5lV39_2wZL1kg5AkGb4mvmG3bwE/edit#gid=1670191276).
We switch to v1.x.y when volume reaches critical mass, and we can assure there
is a certain level of compatibility and long enough time passed to report most
critical issues.

You should always check test results and decide if you need an updated firmware
version and if provided results cover your workload. We don't know your
workload, so we cannot production readiness level. Current test results can be
good enough for one customer to run production workloads. It may be
insufficient for others and would be considered beta. We are happy to extend
our test scope to cover more cases. Let us know about your use case in
[dasharo-issues](https://github.com/Dasharo/dasharo-issues).

## Why is Dasharo (coreboot+SeaBIOS) more expensive than Dasharo (coreboot+UEFI)?

There are many reasons for that. Most importantly, more resources are needed to
maintain code and releases. First, we have a fork of
[SeaBIOS](https://github.com/pcengines/seabios). Second, we have
[sortbootorder](https://github.com/pcengines/sortbootorder) depends on coreboot
toolchain changes and libpayload. Third, tests are in legacy infrastructure
with ongoing migration to
[OSFV](https://github.com/Dasharo/open-source-firmware-validation); even if
migrated, we have too little Dasharo (coreboot+SeaBIOS) supported hardware to
benefit from the effect of scale because Dasharo (coreboot+SeaBIOS) components
do not easily benefit from Dasharo (coreboot+UEFI) changes price have to be
higher.

Dasharo (coreboot+SeaBIOS) was 50% discounted for quite some time before its
first release.

We understand that it can be expensive for individual customers, so we are
always open to providing discounts for those who contribute to the project
meaningfully. The following tiers are eligible for discounts of up to 100%:

* [Beta
Testers](https://docs.dasharo.com/ways-you-can-help-us/#join-dasharo-beta-testing-group)
    - 100% discount for the time of being active Beta Tester.
* Top 5 active members on [Dasharo
Matrix](https://matrix.to/#/#dasharo:matrix.org) and [Dasharo Github
Issues](https://github.com/Dasharo/dasharo-issues)- 100% discount for 1 year.
* Code contributors, testers, and issue reporters - depends on severity and
size of contributions.
