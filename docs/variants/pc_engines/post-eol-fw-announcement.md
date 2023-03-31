# Post EOL firmware announcement

Dear valued PC Engines hardware owners,

We apologize for the delay in our announcement. We understand that many of you
have eagerly awaited the next PC Engines firmware release. Rest assured that
our commitment to supporting the PC Engines firmware remains strong, and we are
working hard to bring you new features through the upcoming Dasharo firmware
distribution. We appreciate your patience and continued support.

We regret to inform the community that [v4.17.0.3][1] was the last version of
the firmware sponsored by PC Engines. However, 3mdeb has since released
[v4.19.0.1][2], the final version delivered to the community using the existing
model.

As some may know, 3mdeb is a small open-source firmware consulting company
based in Poland. Our team consists of passionate engineers and developers from
open-source software, firmware, and hardware communities, frequent conference
speakers, and people who love to tinker with bits. Every day we develop
bleeding-edge low-level security solutions using top open-source frameworks. We
are committed to continuing support and PC Engines hardware in the open-source
firmware community but can't afford that on our dime.

Since February 2016, we have made [87 binary releases][3] for all PC Engines
hardware platforms from apu1 through famous apu2 up to apu7. We published over
[30k test results][4] from our automated testing framework. Thanks to community
feedback, we created extensive [documentation][5]. Our firmware development
effort extended the lifetime value of PC Engines hardware. Most notable
examples were:

- CPU Core Performance Boost feature enabling - [blog][6]
- DRAM Error Correction Code enabling - [blog][7]
- AMD Cryptographic Coprocessor enabling - [issue tracker][8]
- and many small things like a watchdog or SPI flash lockdown.

According to [PC Engines EOL statement][9] apu2 / apu3 series availability will
be: "Based on an AMD embedded CPU, this platform should have good long term
availability. This CPU should be available until 2024 according to AMD."

We would like to continue support for PC Engines firmware through our Dasharo
open-source firmware distribution. Further releases could include regular
maintenance updates and new features such as UEFI compatibility, fwupd,
Verified Boot, UEFI Setup password, DMA protection, and more. For a complete
list of planned enhancements, please visit the [dasharo-issues repository][10]
on GitHub.

Your support will play a crucial role in determining the roadmap and the speed
of its implementation. We hope you will support our efforts to bring these new
features and improvements to the PC Engines firmware.

We are exploring the possibility of implementing a subscription model for
firmware updates. We would like to hear from you to ensure that the pricing
option is fair and reasonable for our community. We have created a survey to
gather your thoughts and preferences on pricing. Your feedback is important to
us and will help us make informed decisions about the future of our offerings.
Please take about two minutes to participate in [the survey][11]. Your input
will be greatly appreciated.

In case of any questions feel free to [contact us](https://www.dasharo.com/pages/contact/).

[1]: https://pcengines.github.io/#mr-62
[2]: https://pcengines.github.io/#mr-63
[3]: https://pcengines.github.io
[4]: https://docs.google.com/spreadsheets/d/1_uRhVo9eYeZONnelymonYp444zYHT_Q_qmJEJ8_XqJc/edit#gid=0
[5]: https://pcengines.github.io/apu2-documentation/
[6]: https://blog.3mdeb.com/2019/2019-02-14-enabling-cpb-on-pcengines-apu2
[7]: https://blog.3mdeb.com/2018/2018-10-16-enabling-ecc-on-pc-engines-apu2
[8]: https://github.com/pcengines/apu2-documentation/issues/112
[9]: https://www.pcengines.ch/eol.htm
[10]: https://github.com/Dasharo/dasharo-issues/issues?q=is%3Aopen+is%3Aissue+label%3Aenhancement
[11]: https://forms.gle/MHrT2f1du1Afvwvj9
