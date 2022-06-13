# FAQ

## I see white LED, but no output, is my board broken?

There maybe many reasons of this behavior.

One may be, it boots fine but there is no visible output. It may mean firmware
stuck at some point or maybe platform booting normally but all output is
disabled.

Debugging that requires rebuilding with `CONFIG_DEFAULT_CONSOLE_LOGLEVEL_8=y`. Instruction for that can be found [here](../building-manual/#debug-build)

## Is it safe to work without heatsink?

It should be safe for debugging and recovery purposes. CPU after ~1min will
reach temperature limits and will shutdown the platform.

