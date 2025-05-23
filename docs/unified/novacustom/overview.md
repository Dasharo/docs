# Overview

Select your Dasharo firmware flavor:

=== "Dasharo (coreboot + UEFI)"
    NovaCustom laptops come with this firmware variant out of the box.

    ## Models

    === "V54 Series"
        __NovaCustom V54__ is a series of 14 inch laptops based on 14th
        Generation Intel Core Ultra processors (Meteor Lake):

        ![](../../images/v540tu-front.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [V54 Series](https://configurelaptop.eu/v54-series/)

        </div>

    === "V56 Series"
        __NovaCustom V56__ is a series of 16 inch laptops based on 14th
        Generation Intel Core Ultra processors (Meteor Lake):

        ![](../../images/v560tu-front.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [V56 Series](https://configurelaptop.eu/v56-series/)

        </div>

    === "NS5x/7x 12th Gen"
        __NovaCustom NS5x/7x 12th Gen__ are 15 and 17 inch laptops based on 12th
        generation Intel Core processor (Alder Lake):

        ![](../../images/NS51-front-1.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [NS51 Series](https://novacustom.com/product/ns51-series/)
        - [NS70 Series](https://novacustom.com/product/ns70-series/)

        </div>

    === "NV4x 12th Gen"
        __NovaCustom NV4x 12th Gen__ is a 14 inch laptop based on 12th
        generation Intel Core processor (Alder Lake):

        ![](../../images/NV4x-front-1.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [NV41 Series](https://novacustom.com/product/nv41-series/)

        </div>

    === "NS5x/7x 11th Gen"
        __NovaCustom NS5x/7x 11th Gen__ are 15 and 17 inch laptops based on 11th
        generation Intel Core processor (Tiger Lake):

        ![](../../images/NS51-front-1.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [NS51 Series](https://novacustom.com/product/ns51-series/)
        - [NS70 Series](https://novacustom.com/product/ns70-series/)

        </div>

    === "NV4x 11th Gen"
        __NovaCustom NV4x 11th Gen__ is a 14 inch laptop based on 11th
        generation Intel Core processor (Tiger Lake):

        ![](../../images/NV40-front-1.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [NV40 Series](https://novacustom.com/product/nv40-series/)

        </div>

    For more information on the hardware, please refer to the links above.

    ## Firmware

    Each firmware release contains of two parts:

    - [BIOS](https://en.wikipedia.org/wiki/BIOS) firmware,
    - [EC (Embedded Controller)](https://en.wikipedia.org/wiki/Embedded_controller)
      firmware.

    They both interact with each other tightly, so keeping their compatible versions
    in sync is important. Information on compatibility should always be explained
    on the release pages:

    <div class="annotate" markdown>

    - V54 Series
        * [V540TU](../../variants/novacustom_v540tu/releases.md) (1)
        * [V540TNx](../../variants/novacustom_v540tnx/releases.md) (2)
    - V56 Series
        * [V560TU](../../variants/novacustom_v560tu/releases.md) (3)
        * [V560TNx](../../variants/novacustom_v560tnx/releases.md) (4)
    - [NV4x 12th Gen](../../variants/novacustom_nv4x_adl/releases.md)
    - [NV4x 11th Gen](../../variants/novacustom_nv4x_tgl/releases.md)
    - [NS5x/7x 12th Gen](../../variants/novacustom_ns5x_adl/releases.md)
    - [NS5x/7x 11th Gen](../../variants/novacustom_ns5x_tgl/releases.md)

    </div>

    1. 14 inch, Integrated graphics
    2. 14 inch, Discrete NVIDIA graphics
    3. 16 inch, Integrated graphics
    4. 16 inch, Discrete NVIDIA graphics

=== "Dasharo (coreboot + Heads)"
    Heads-based firmware is offered as a Dasharo Pro Package option.

    !!! note

        This section applies to users of the Heads-based firmware version. If
        you are unsure which firmware version you're using, select
        `coreboot + UEFI` instead.

    ## Models
    === "V54 Series"
        __NovaCustom V54 series__ are 14 inch laptops based on 14th Generation
        Intel Core Ultra processors (Meteor Lake):

        ![](../../images/v560tu-front.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [V54 Series](https://configurelaptop.eu/v54-series/)

        </div>


    === "V56 Series"
        __NovaCustom V56 serues__ are 16 inch laptops based on 14th Generation
        Intel Core Ultra processors (Meteor Lake):

        ![](../../images/v560tu-front.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [V56 Series](https://configurelaptop.eu/v56-series/)

        </div>

    === "NV4x 12th Gen"
        __NovaCustom NV4x 12th Gen__ is a 14 inch laptop based on 12th
        generation Intel Core processor (Alder Lake):

        ![](../../images/NV4x-front-1.png){ align=right width=50% }

        <div class="grid cards" markdown>

        - [NV41 Series](https://novacustom.com/nv41-series/)

        </div>

    For more information on the hardware, please refer to the references in above
    links.

    ## Firmware

    Each firmware release contains of two parts:

    - [BIOS](https://en.wikipedia.org/wiki/BIOS) firmware,
    - [EC (Embedded Controller)](https://en.wikipedia.org/wiki/Embedded_controller)
      firmware.

    They both interact with each other tightly, so keeping their compatible versions
    in sync is important. Information on compatibility should always be explained
    on the release pages:

    <div class="annotate" markdown>

    - V56 Series
        * [V560TU](../../variants/novacustom_v560tu/releases_heads.md) (1)
    - V54 Series
        * [V540TU](../../variants/novacustom_v540tu/releases_heads.md)
    - [NV4x 12th Gen](../../variants/novacustom_nv4x_adl/releases_heads.md)

    </div>

    1. 16 inch, Integrated graphics
