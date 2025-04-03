# Laptop power limits

This article describes how power limiting works on Dasharo firmware for laptops.

## Power sources

A laptop may be powered from AC, or from battery. Each of these two has a limit
on how much power it can provide.

- AC barrel jack: Depends on the wattage of the included power supply
- USB-PD: Depends on the wattage rating of the specific power supply being used,
  and on the contract that was negotiated between the laptop and power supply
- Battery: Depends on the maximum discharge rate specified by the manufacturer
  and on charge level

The embedded controller must observe what sources of power are present and
adjust platform power limits accordingly.

To limit power, the CPU is throttled using the Psys power limit mechanism. This
ensures that the power draw does not exceed the limit, by proactively throttling
CPU performance.

## AC power limit

This limit is a minimum of:

- Power supply wattage x estimated power conversion efficiency
- Maximum current rating of the input power rail
- Wattage of the included AC power supply

## DC power limit

This power limit is a minimum of:

- Battery capacity x 1C discharge rate
- Maximum current rating of the battery power rail
