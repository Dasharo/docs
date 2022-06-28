# FAQ

## I see white LED, but no output, is my board broken?

There maybe many reasons of this behavior.

One may be, it boots fine but there is no visible output. It may mean firmware
stuck at some point or maybe platform booting normally but all output is
disabled.

Debugging that requires rebuilding with `CONFIG_DEFAULT_CONSOLE_LOGLEVEL_8=y`.
Instruction for that can be found [here](../building-manual/#debug-build).

## Is it safe to work without heatsink?

It should be safe for debugging and recovery purposes. CPU after ~1min will
reach temperature limits and will shutdown the platform.

## CPU was replaced & warm reset required loop

If serial console logs contain:

```bash
[NOTE ]  ME: Wrong mode : 15
[NOTE ]  ME: HFS error : 15
[NOTE ]  ME: FWS2: 0xffffffff
[NOTE ]  ME:  Bist in progress: 0x1
[NOTE ]  ME:  ICC Status      : 0x3
[NOTE ]  ME:  Invoke MEBx     : 0x1
[NOTE ]  ME:  CPU replaced    : 0x1
[NOTE ]  ME:  MBP ready       : 0x1
[NOTE ]  ME:  MFS failure     : 0x1
[NOTE ]  ME:  Warm reset req  : 0x1
[NOTE ]  ME:  CPU repl valid  : 0x1
[NOTE ]  ME:  (Reserved)      : 0x3
[NOTE ]  ME:  FW update req   : 0x1
[NOTE ]  ME:  (Reserved)      : 0xf
[NOTE ]  ME:  Current state   : 0xff
[NOTE ]  ME:  Current PM event: 0xf
[NOTE ]  ME:  Progress code   : 0xf
[NOTE ]  CPU was replaced & warm reset required...
[INFO ]  system_reset() called!
```

It means ME is broken and backup firmware would be required to recover it.
Please follow
[additional recovery step](../recovery/#optional-step-7-flash-8mb-me-part)
to fix that problem.

This may happen accidentally when you flash whole 12MB BIOS binary without
passing parameters about FMAP.
