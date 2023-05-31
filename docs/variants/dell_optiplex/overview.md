# Overview

<!--

_**TBD**: this page should contain most important information about Dasharo OSF
support for Dell OptiPlex 7010/9010 including presentations, demos, external
resources, reviews etc. Currently it just points to subsecations of the
documentation._

-->

<center>
![](../../images/dell_optiplex_9010.jpg)
</center>

Dell OptiPlex 7010/9010 SFF is small SOHO desktop computer sometimes used as
[firewall or NAS](https://www.reddit.com/r/homelabsales/comments/uzspg3/comment/iadcyb6/?utm_source=share&utm_medium=web2x&context=3).
To learn more about our motivation for the coreboot port and Dasharo compatible
with Dell OptiPlex 7010/9010 SFF please check [references](#references) section.
If you want to build, initially deploy, update or recover your setup please
check documentation sections on the left.

## Status

Dasharo compatible with Dell OptiPlex 7010/9010 is a community-driven effort.
We work on this in our free time, since we have no sponsor for this project. To
address the issue we organize virtual hackathon called [OptiPlex
Tuesday](https://3mdeb.com/events/) on Dasharo Matrix almost every Tuesday. If
you are interested in this project, you can consider joining the event or
[supporting us in other way](../../ways-you-can-help-us.md).

The most advanced code is on [rel_v0.1.0
branch](https://github.com/Dasharo/coreboot/pull/202) and the most advanced
documentation related to `rel_v0.1.0` branch is already available from menu on
the left. This code supports only `Dasharo (coreboot+SeaBIOS)`, so legacy boot.
UEFI is also quite ready, but we need to release `v0.1.0` properly first.

## References

* [Dell OptiPlex and coreboot - a story about porting cursed hardware (part 1)](https://blog.3mdeb.com/2020/2020-06-24-dell-optiplex-port/)
* [Dell OptiPlex and coreboot - a story about porting cursed hardware (part 2)](https://blog.3mdeb.com/2021/2021-06-01-optiplex_part2/)
* [Dasharo for Dell OptiPlex 7010 / 9010](https://blog.3mdeb.com/2021/2021-11-26-optiplex-dasharo/)
