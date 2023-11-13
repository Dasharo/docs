# Fan profiles settings

There are two fan profiles implemented. The profiles can be selected via the
[Power Management Options](/dasharo-menu-docs/dasharo-system-features/#power-management-options)
menu in the Setup Menu.

Fan profiles are defined as follows:

## Silent fan profile

# Releases newer than v1.4.0 11th Gen and v1.6.0 12th Gen

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 20            |
| 65               | 25            |
| 75               | 35            |
| 85               | 100           |

# Releases v1.4.0 11th Gen and v1.6.0 12th Gen or older

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 25            |
| 65               | 30            |
| 75               | 35            |
| 100              | 100           |

## Performance fan profile

# Releases newer than v1.4.0 11th Gen and v1.6.0 12th Gen

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 25            |
| 55               | 35            |
| 75               | 60            |
| 85               | 100           |

# Releases v1.4.0 11th Gen and v1.6.0 12th Gen or older

| Temperature [°C] | Fan speed [%] |
|------------------|---------------|
| 0                | 25            |
| 55               | 35            |
| 75               | 60            |
| 100              | 100           |

> Values in-between curve points are interpolated linearly.
