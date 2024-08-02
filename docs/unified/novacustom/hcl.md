# Hardware Compatibility Lists

The following compatibility list contains devices and accessories that have been
tested to work with Dasharo firmware.

Feel free to perform different tests and report your results via
[email](mailto:contact@dasharo.com) or submit a Pull Request to
[Dasharo documentation repository](https://github.com/Dasharo/docs) or by using
[Dasharo issues repository](https://github.com/Dasharo/dasharo-issues/issues).

Devices listed with `Official support` are tested for each firmware release and
are guaranteed to be compatible. Reports noted as `Internal testing` come from
internal employee testing carried out by us, but aren't guaranteed to work.
Reports from the community should link to the appropriate GitHub PR and / or
issue from which the report is sourced.

=== "USB-C HCL (11 Dec 2023)"

    This section is for USB Type-C accessories: docks, hubs, power supplies and
    other types of peripherals.

    === "NS5x/7x 12th Gen"
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Wavlink | UMD05 Pro (1) | v1.7.2 | No issues (2) | Official support |
        | Wavlink | UG69PD2 (3) | v1.7.2 | DisplayLink (4) | Official support |

        </div>

        1. Rev.C1 and Rev.E
        2. DP Alt mode: Synaptics VMM5310 DP MST hub, two upstream DP 1.4 lanes,
           DSC 1.2 decompression, up to 2x 4K60 + 1x 4K30 depending on source.
        3. Rev.A1
        4. Up to 2x 5K60 supported. OS driver required.

        ### Hubs

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | No issues | Official support |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | One video output usable at a time | Official support |

    === "NV4x 12th Gen"
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Wavlink | UMD05 Pro (1) | v1.7.2 | No issues (2) | Official support |
        | Wavlink | UG69PD2 (3) | v1.7.2 | DisplayLink (4) | Official support |
        | Lenovo | USB-C Dock Gen2 |  v0.9.0 | <ul><li>Can overdraw power from the dock, fixed in v1.7.2</li><li>Power button not supported</li> | Internal testing |
        | Lenovo | Universal USB-C Dock | v0.9.0 | <ul><li> Need 130W power supply option to not overdraw, fixed in v1.7.2</li><li>Power button not supported</li> | Internal testing |
        | Belkin | USB-C 11-in-1 Multiport Dock | v0.9.0 | No issues | Internal testing |

        </div>

        1. Rev.C1 and Rev.E
        2. DP Alt mode: Synaptics VMM5310 DP MST hub, two upstream DP 1.4 lanes,
           DSC 1.2 decompression, up to 2x 4K60 + 1x 4K30 depending on source.
        3. Rev.A1
        4. Up to 2x 5K60 supported. OS driver required.

        ### Hubs

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | No issues | Official support |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | One video output usable at a time | Official support |
        | CableMatters | Triple Display Travel Hub (201431-BLK) | v0.9.0 | No issues | Internal testing |

    === "NS5x/7x 11th Gen"
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Wavlink | UG69PD2 (1) | v1.5.2 | DisplayLink (2) | Official support |

        </div>

        1. Rev.A1
        2. Up to 2x 5K60 supported. OS driver required.

        ### Hubs

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Levin | 7-in-1 Type-C Hub Pro | v1.5.2 | No issues | Official support |
        | Generic | 8-in-1 Type-C Hub | v1.5.2 | One video output usable at a time | Official support |

    === "NV4x 11th Gen"
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Wavlink | UG69PD2 (1) | v1.5.2 | DisplayLink (2) | Official support |

        </div>

        1. Rev.A1
        2. Up to 2x 5K60 supported. OS driver required.

        ### Hubs

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Levin | 7-in-1 Type-C Hub Pro | v1.5.2 | No issues | Official support |
        | Generic | 8-in-1 Type-C Hub | v1.5.2 | One video output usable at a time | Official support |
        | Belkin | USB-C 11-in-1 Multiport Dock | v0.9.0 | No issues | Internal testing |

    === "NV4x 12th Gen __(Heads)__"
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | Wavlink | UMD05 Pro (1) | v1.7.2 | No issues (2) | Official support |

        </div>

        1. Rev.C1 and Rev.E
        2. DP Alt mode: Synaptics VMM5310 DP MST hub, two upstream DP 1.4 lanes,
           DSC 1.2 decompression, up to 2x 4K60 + 1x 4K30 depending on source.
    === "V54 / V56 14th Gen."
        <div class="annotate" markdown>

        ### Docks

        | Manufacturer | Model | Dasharo version | Notes | Source |
        |---|---|---|---|---|
        | NovaCustom | Echo 11 Thunderbolt 4 ECHO-DK11-T4  | v0.9.0 | No issues | Official support |

        </div>


    > **Note on DisplayLink compatibility:** DisplayLink requires a driver to
    > function correctly. On Windows, the driver should install automatically if
    > network is connected and Windows Update is enabled. On Linux, consult your
    > distribution's documentation on DisplayLink compatibility. Preboot video
    > output is not supported.
