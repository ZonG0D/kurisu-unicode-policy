kurisu unicode policy enforcer

This repo implements token-level validation and a sink guard that blocks a small set
of forbidden unicode dash codepoints. It includes CI checks and unit tests.

Usage
- Register runtime.validators.unicode_ban.on_token with your sampler/token emitter.
- Wrap final output with runtime.sink_guard.safe_emit before writing to users.
