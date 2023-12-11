# Hardware Compatibility Lists

The following compatibility list contains officially supported devices and
accessories.

For unofficial test results contributed by the community, check out the
[Community Test Results](./community-test-results.md) section.

=== "USB-C HCL (11 Dec 2023)"

    The following is a list of USB Type-C docking stations and hubs that have
    been verified and tested for compatibility by the Dasharo validation team.
    Each firmware release is tested against these docks to ensure compatibility.

    === "NS5x/7x 12th Gen"
        <div class="annotate" markdown>

        | Manufacturer | Model | Dasharo version | Notes |
        |:---:|:---:|:---:|:---:|
        | Wavlink | UMD05 Pro (1) | v1.7.2 | DP Alternate mode (2) |
        | Wavlink | UG69PD2 (3) | v1.7.2 | DisplayLink (4) |
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | DP Alternate mode |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | DP Alternate mode |

        </div>

        1. Rev.C1 and Rev.E
        2. Synaptics VMM5310 DP MST hub, two upstream DP 1.4 lanes, DSC 1.2
           decompression, up to 2x 4K60 + 1x 4K30 depending on source.
        3. Rev.A1
        4. Up to 2x 5K60 supported. OS driver required.

    === "NV4x 12th Gen"
        <div class="annotate" markdown>

        | Manufacturer | Model | Dasharo version | Notes |
        |:---:|:---:|:---:|:---:|
        | Wavlink | UMD05 Pro (1) | v1.7.2 | DP Alternate mode (2) |
        | Wavlink | UG69PD2 (3) | v1.7.2 | DisplayLink (4) |
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | DP Alternate mode |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | DP Alternate mode |

        </div>

        1. Rev.C1 and Rev.E
        2. Synaptics VMM5310 DP MST hub, two upstream DP 1.4 lanes, DSC 1.2
           decompression, up to 2x 4K60 + 1x 4K30 depending on source.
        3. Rev.A1
        4. Up to 2x 5K60 supported. OS driver required.

    === "NS5x/7x 11th Gen"
        <div class="annotate" markdown>

        | Manufacturer | Model | Dasharo version | Notes |
        |:---:|:---:|:---:|:---:|
        | Wavlink | UG69PD2 (1) | v1.7.2 | DisplayLink (2) |
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | DP Alternate mode |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | DP Alternate mode |

        </div>

        1. Rev.A1
        2. Up to 2x 5K60 supported. OS driver required.

    === "NV4x 11th Gen"
        <div class="annotate" markdown>

        | Manufacturer | Model | Dasharo version | Notes |
        |:---:|:---:|:---:|:---:|
        | Wavlink | UG69PD2 (1) | v1.7.2 | DisplayLink (2) |
        | Levin | 7-in-1 Type-C Hub Pro | v1.7.2 | DP Alternate mode |
        | Generic | 8-in-1 Type-C Hub | v1.7.2 | DP Alternate mode |

        </div>

        1. Rev.A1
        2. Up to 2x 5K60 supported. OS driver required.

    > **Note on DisplayLink compatibility:** DisplayLink requires a driver to
    > function correctly. On Windows, the driver should install automatically if
    > network is connected and Windows Update is enabled. On Linux, consult your
    > distribution's documentation on DisplayLink compatibility. Preboot video
    > output is not supported.
