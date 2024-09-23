# EC power states- brief explanation

## Power states

This section describes the logic used by the EC to control platform power states
depending on AC adapter presence.

### Shutdown, with AC connected

The machine switches to system power state S5, using little to no
power. As a result pressing the power button to turn it on, will result in
a warmboot. (S0 → S5 → S0)

### AC detach while turned off

EC disables all power planes, and the platform is set to G3 power state.
Therefore, in that case pressing the power button results in a coldboot.
(S0 → S5 → G3 → S0)

### Shutdown, with AC disconnected

The machine actually enters S5 and proceeds to G3 soon after. Pressing the
power button will result a coldboot. (S0 → S5 → G3 → S0 )
