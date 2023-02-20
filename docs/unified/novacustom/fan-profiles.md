# Fan profiles settings

There are two fan profiles implemented. The profiles can be selected via the
[Power Management Options](/dasharo-menu-docs/dasharo-system-features/#power-management-options)
menu in Setup Menu.

Fan profiles are defined as follows:

## Silent fan profile

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 25            |
| 65               | 30            |
| 75               | 35            |
| 100              | 100           |

## Performance fan profile

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 25            |
| 55               | 35            |
| 75               | 60            |
| 100              | 100           |

> Values inbetween curve points are interpolated linearly.
