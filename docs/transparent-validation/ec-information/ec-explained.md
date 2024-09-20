# EC power states in NovaCustom laptops

## Way the EC works right now

### Turning off the computer while charger is plugged in

The machine switches to system power state S5, using little to no
power. As a result pressing the power button to turn it on, will result in
a warmboot. (S0 → S5 → S0)

### Cutting off power feed while in S5

EC disables all power planes, and the platform is set to G3 power state.
Therefore, in that case pressing the power button results in a coldboot.
(S0 → S5 → G3 → S0)

### Turning the computer off while not plugged in

The machine actually enters S5 briefly and immediately after, it switches
to G3 like intended. Like mentioned before, turning the computer from G3
results in a coldboot. (S0 → S5 → G3 → S0 )
